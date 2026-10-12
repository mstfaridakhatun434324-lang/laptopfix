# awswnv.win — Hugo site scaffold (Phase 1)

Static blog for Windows laptop/PC troubleshooting. Hugo + fully custom theme
(`themes/laptopfix`, no external theme dependency). Designed for 5,000 articles;
this scaffold ships 10 sample articles (2 per category).

## Layout

```
hugo.toml                      # site config (title, taxonomies, outputs, category list)
content/articles/<slug>.md     # articles (one file per article)
themes/laptopfix/
  assets/scss/_variables.scss  # <-- BRAND PALETTE: change colors here
  assets/scss/main.scss        # all styles (compiled by Hugo Pipes)
  assets/js/search.js           # client-side search over /index.json
  layouts/index.html            # homepage: hero + category cards + latest grid
  layouts/index.json            # search index (JSON output)
  layouts/_default/single.html  # article: breadcrumbs, TOC, FAQ, related, prev/next, JSON-LD
  layouts/_default/list.html    # section listing
  layouts/taxonomy/category*.html # category pages
  layouts/partials/            # head, header, footer, article-card, icons
static/images/thumbs/*.webp    # generated thumbnails (do not hand-edit)
static/robots.txt
scripts/
  gen_thumbnails.py  # renders .webp thumbnails with text overlay (pre-build step)
  build_related.py   # interlinking scorer -> data/related.json + link audit
  new_article.py     # frontmatter scaffolder
data/related.json              # generated: {slug: [related slugs]}
```

## Content pipeline (how to add more articles)

1. Pick keywords from `~/workspace/keyword-ideas/keywords.csv`
   (prefer `source=research-verified` first).
2. Scaffold the file:
   `python3 scripts/new_article.py --slug <slug> --title "<Title>" --category "<Category>"`
   Categories (exact strings): `Battery & Power`, `Windows Errors & BSOD`,
   `Drivers & Devices`, `Performance & Speed`, `Windows Update`.
3. Write the body: 1000–1400 words total (incl. FAQ answers). Structure:
   opening (2 paras, no heading) → `## Why this happens` → `## How to fix it`
   with `### Fix 1:` … `### Fix N:` (5–8 fixes, concrete steps) → closing para.
   FAQs go in frontmatter `faqs:` (exactly 4), rendered by the template +
   emitted as FAQPage JSON-LD.
4. **Interlinking (deterministic rule, scriptable):** every article needs ≥2
   in-content markdown links `[text](/articles/<target-slug>/)`.
   Target selection rule: same category (+10) and shared significant title
   words (+2 each) — see `scripts/build_related.py`. At 5k scale the content
   step consumes the scorer's ranked list and linkifies top candidates.
   The theme's "Related fixes" block is fully automatic from
   `data/related.json`.
5. Regenerate derived files:
   ```
   python3 scripts/gen_thumbnails.py      # .webp thumbnails with text overlay
   python3 scripts/build_related.py       # related.json + link audit (fails if <2 links)
   ```
6. Build & verify:
   ```
   ~/.local/bin/hugo --minify
   ```
   Then check `public/` — all articles, category pages, sitemap.xml,
   index.json, RSS.

## Thumbnails

`scripts/gen_thumbnails.py` renders 1200×630 `.webp` files: navy gradient +
pinstripe background, amber category pill, bold white title, `LAPTOPFIX`
footer. Palette constants mirror `assets/scss/_variables.scss` — keep them
in sync when re-skinning. Re-run with `--force` to rebuild all.

## Deploy (later, Phase 2)

- Push this repo to GitHub → Cloudflare Pages → connect repo.
- Build command: `hugo --minify` (Hugo extended is preinstalled on Pages;
  no extra config needed). Publish directory: `public`.
  Note: pin the Hugo version in the Pages project settings
  (environment variable `HUGO_VERSION`, e.g. `0.167.0`) so the Cloudflare
  build matches this scaffold's local build.
- Custom domain: attach in Pages → Custom domains (DNS auto-configured
  since the zone is on Cloudflare).
- Updates: edit markdown → `git push` → Pages rebuilds & deploys (~1–3 min).
