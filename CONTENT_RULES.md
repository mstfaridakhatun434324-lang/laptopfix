# Content Rules — awswnv.win article pipeline

These rules apply to every article generated for the 5,000-article batch.
They are already applied to the 10 sample articles in `content/articles/`.

## Length & quality
- 1,000–1,400 words per article. Unique, human-reading, AdSense-compliant.
- English, Windows laptop/PC troubleshooting niche only.

## Internal linking (automatic)
- Every article: ≥2 contextual in-content links to other articles.
- Related block built by `scripts/build_related.py` (same category + shared title words).

## Official outbound links (editorial)
- Every article MUST include 1–3 contextual outbound links to official sources
  where genuinely helpful (driver downloads, BIOS updates, Microsoft tools,
  manufacturer diagnostics). Never link for its own sake.
- Use markdown links: `[anchor text](URL)`. The theme's render hook
  (`layouts/_default/_markup/render-link.html`) automatically adds
  `target="_blank" rel="noopener"` to external links. Do NOT add nofollow —
  these are trusted editorial citations.
- ONLY use URLs from the verified whitelist below (all checked live 2026-10-13).
  Do not invent deep URLs; hub pages are preferred because they don't rot.

### Verified whitelist
| Owner     | URL                                              | Use for                        |
|-----------|--------------------------------------------------|--------------------------------|
| Microsoft | https://support.microsoft.com/en-us/windows     | Windows help, troubleshooters  |
| Microsoft | https://www.microsoft.com/en-us/software-download/windows11 | ISO / Media Creation Tool |
| Microsoft | https://www.catalog.update.microsoft.com/       | Manual KB downloads            |
| Dell      | https://www.dell.com/support                     | Dell drivers, BIOS, diagnostics|
| HP        | https://support.hp.com/us-en                     | HP drivers, BIOS               |
| Lenovo    | https://support.lenovo.com/us/en/                | Lenovo drivers, Vantage        |
| Intel     | https://www.intel.com/content/www/us/en/support/detect.html | Intel Driver & Support Assistant |
| NVIDIA    | https://www.nvidia.com/Download/index.aspx       | GeForce drivers                |
| AMD       | https://www.amd.com/en/support/download/drivers.html | AMD chipset/GPU drivers    |

## Images
- One 1200×630 `.webp` thumbnail per post: real licensed photo + navy gradient
  + amber category pill + title + `awswnv.win` branding (`scripts/gen_thumbnails.py`).
- Photo pool lives in `assets/thumb-bg/` (Pexels license: free commercial use,
  no attribution required). Each post MUST use a unique photo.

## SEO / schema
- Article + FAQPage JSON-LD on every article (in `layouts/_default/single.html`).
  All `jsonify` output inside `<script type="application/ld+json">` MUST be piped
  through `safeJS` to avoid double-encoding.
- Breadcrumbs, TOC, FAQ accordion, prev/next, share buttons are template-driven.
