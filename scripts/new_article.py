#!/usr/bin/env python3
"""Scaffold a new article file with the required frontmatter.

Usage:
  python3 scripts/new_article.py --keyword "how to fix X on windows 11" \
      --category "Battery & Power" --slug my-slug --title "My Title" [--date 2026-10-20]

Prints the path of the created file. Fill in the body following the template
in README.md, then run gen_thumbnails.py and build_related.py.
"""
import argparse
import datetime
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content", "articles")

TEMPLATE = """---
title: "{title}"
slug: {slug}
date: {date}
categories: ["{category}"]
tags: []
description: ""
thumbnail: "/images/thumbs/{slug}.webp"
faqs:
  - q: ""
    a: ""
  - q: ""
    a: ""
  - q: ""
    a: ""
  - q: ""
    a: ""
---

<!-- Opening: 2 short paragraphs describing the problem. -->

## Why this happens

## How to fix it

### Fix 1:

### Fix 2:

### Fix 3:

### Fix 4:

### Fix 5:

<!-- Closing paragraph. -->
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--slug", required=True)
    ap.add_argument("--title", required=True)
    ap.add_argument("--category", required=True)
    ap.add_argument("--date", default=datetime.date.today().isoformat())
    args = ap.parse_args()
    path = os.path.join(CONTENT, args.slug + ".md")
    if os.path.exists(path):
        raise SystemExit(f"exists: {path}")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEMPLATE.format(title=args.title.replace('"', "'"),
                                slug=args.slug, date=args.date,
                                category=args.category))
    print(path)


if __name__ == "__main__":
    main()
