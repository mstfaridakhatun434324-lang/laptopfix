#!/usr/bin/env python3
"""Interlinking engine: deterministic related-article scoring + link audit.

RULE (documented, scriptable to 5,000 articles):
  For article A, every other article B gets a score:
    +10  if B is in the SAME category as A
    +2   per shared significant word between A's and B's titles
  Significant words = title tokens minus STOPWORDS. Top 4 scorers (excluding A
  itself) become A's related set, written to data/related.json
  ({slug: [slug, ...]}), which the theme renders as the "Related fixes" block.

  In-content contextual links live in the article markdown itself. At 5k scale
  the content step consumes this scorer's ranked list and linkifies the top
  candidates where their topic is mentioned. This script also AUDITS bodies:
  every article must contain >= 2 in-content links to /articles/<slug>/.

Run:  python3 scripts/build_related.py
"""
import json
import os
import re
import sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content", "articles")
DATA_OUT = os.path.join(ROOT, "data", "related.json")

STOPWORDS = {
    "windows", "laptop", "laptops", "pc", "fix", "fixes", "fixed", "fixing",
    "how", "to", "on", "a", "an", "the", "and", "for", "of", "in", "with",
    "your", "you", "it", "its", "s", "vs", "work", "works", "working",
    "here", "s", "11", "10", "but", "not", "are", "is", "at", "by",
}


def parse(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    meta, body = {}, ""
    if m:
        for line in m.group(1).splitlines():
            mm = re.match(r"^(title|slug):\s*(.*)$", line)
            if mm:
                meta[mm.group(1)] = mm.group(2).strip().strip('"').strip("'")
            mc = re.match(r"^categories:\s*\[\"?(.*?)\"?\]$", line)
            if mc:
                meta["category"] = mc.group(1)
        body = m.group(2)
    slug = meta.get("slug") or os.path.basename(path)[:-3]
    return slug, meta.get("title", slug), meta.get("category", ""), body


def tokens(title):
    return {t for t in re.findall(r"[a-z0-9]+", title.lower())
            if t not in STOPWORDS and len(t) > 2}


def main():
    articles = {}
    for fn in sorted(os.listdir(CONTENT)):
        if fn.endswith(".md"):
            slug, title, cat, body = parse(os.path.join(CONTENT, fn))
            articles[slug] = {"title": title, "category": cat,
                              "tokens": tokens(title), "body": body}

    # inverted index for O(total tokens) scoring
    postings = defaultdict(list)
    for slug, a in articles.items():
        for t in a["tokens"]:
            postings[t].append(slug)

    related = {}
    for slug, a in articles.items():
        scores = defaultdict(int)
        for t in a["tokens"]:
            for other in postings[t]:
                if other != slug:
                    scores[other] += 2
        for other, b in articles.items():
            if other != slug and b["category"] == a["category"]:
                scores[other] += 10
        ranked = sorted(scores.items(), key=lambda kv: (-kv[1], kv[0]))
        related[slug] = [s for s, _ in ranked[:4]]

    os.makedirs(os.path.dirname(DATA_OUT), exist_ok=True)
    with open(DATA_OUT, "w", encoding="utf-8") as f:
        json.dump(related, f, indent=2)
    print(f"related.json written for {len(related)} articles")

    # ---- link audit ----
    link_re = re.compile(r"\]\(/articles/([a-z0-9\-]+)/?\)")
    ok = True
    for slug, a in articles.items():
        found = link_re.findall(a["body"])
        # count distinct valid targets that exist
        valid_targets = {t for t in found if t in articles and t != slug}
        status = "OK " if len(valid_targets) >= 2 else "FAIL"
        if len(valid_targets) < 2:
            ok = False
        print(f"[{status}] {slug}: {len(valid_targets)} in-content links -> {sorted(valid_targets)}")
        unknown = {t for t in found if t not in articles}
        if unknown:
            print(f"       WARNING unknown targets: {sorted(unknown)}")
            ok = False
    if not ok:
        print("LINK AUDIT FAILED")
        sys.exit(1)
    print("LINK AUDIT PASSED")


if __name__ == "__main__":
    main()
