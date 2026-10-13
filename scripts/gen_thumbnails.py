#!/usr/bin/env python3
"""Generate branded .webp thumbnails with text overlay for every article.

Reads content/articles/*.md frontmatter (title, category, slug) and renders
1200x630 .webp images into static/images/thumbs/<slug>.webp.

Background = one AI-generated photorealistic original per article, read 1:1
from /home/hatch/workspace/ai-photos-5k/<slug>.jpg (never reused across
posts), darkened with a navy gradient for text legibility. Same template
for every thumbnail: amber category pill + wrapped title + awswnv.win footer.

Palette mirrors themes/laptopfix/assets/scss/_variables.scss — keep in sync.
Run:  python3 scripts/gen_thumbnails.py [--force]
"""
import os
import re
import sys
import textwrap
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTENT = os.path.join(ROOT, "content", "articles")
OUTDIR = os.path.join(ROOT, "static", "images", "thumbs")
# AI-generated photorealistic originals, one per article slug (NOT in git).
AIDIR = "/home/hatch/workspace/ai-photos-5k"

# Keep in sync with _variables.scss
NAVY_TOP = (15, 30, 56)
NAVY_BOT = (10, 20, 40)
AMBER = (245, 166, 35)
WHITE = (255, 255, 255)
MUTED = (174, 189, 212)
SITE_NAME = "awswnv.win"

# Display names for category slugs (mirrors content/categories/*/title).
CATEGORY_NAMES = {
    "battery": "Battery & Power",
    "windows-errors": "Windows Errors & BSOD",
    "drivers": "Drivers & Devices",
    "performance": "Performance & Speed",
    "windows-update": "Windows Update",
}

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

W, H = 1200, 630


def parse_frontmatter(path):
    """Minimal YAML frontmatter reader (title/category/slug only)."""
    meta = {}
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return meta
    for line in m.group(1).splitlines():
        mm = re.match(r"^(title|slug):\s*(.*)$", line)
        if mm:
            meta[mm.group(1)] = mm.group(2).strip().strip('"').strip("'")
        mc = re.match(r"^categories:\s*\[\"?(.*?)\"?\]$", line)
        if mc:
            meta["category"] = mc.group(1)
    return meta


def photo_bg(slug):
    """AI-photo background: 1:1 mapping slug -> ai-photos-5k/<slug>.jpg,
    cover-cropped to 1200x630, with a navy gradient overlay (darker at
    bottom) so the overlaid title text stays legible. Falls back to the
    plain gradient if the AI photo is missing."""
    src = os.path.join(AIDIR, slug + ".jpg")
    if os.path.isfile(src):
        img = Image.open(src).convert("RGB")
        # cover-crop to 1200x630
        sr, tr = img.width / img.height, W / H
        if sr > tr:
            nw = int(img.height * tr)
            x0 = (img.width - nw) // 2
            img = img.crop((x0, 0, x0 + nw, img.height))
        else:
            nh = int(img.width / tr)
            y0 = (img.height - nh) // 2
            img = img.crop((0, y0, img.width, y0 + nh))
        img = img.resize((W, H), Image.LANCZOS)
    else:
        img = Image.new("RGB", (W, H), NAVY_BOT)
    # navy gradient overlay: transparent at top -> strong navy at bottom
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    for y in range(H):
        t = y / H
        alpha = int(60 + 150 * (t ** 1.4))  # 60..210
        od.line([(0, y), (W, y)], fill=NAVY_BOT + (alpha,))
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")
    # amber accent bar on the left
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 14, H], fill=AMBER)
    return img


def gradient_bg():
    img = Image.new("RGB", (W, H), NAVY_BOT)
    draw = ImageDraw.Draw(img)
    for y in range(H):
        t = y / H
        r = int(NAVY_TOP[0] + (NAVY_BOT[0] - NAVY_TOP[0]) * t)
        g = int(NAVY_TOP[1] + (NAVY_BOT[1] - NAVY_TOP[1]) * t)
        b = int(NAVY_TOP[2] + (NAVY_BOT[2] - NAVY_TOP[2]) * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b))
    # subtle diagonal pinstripes
    stripe = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(stripe)
    for x in range(-H, W, 46):
        sd.line([(x, 0), (x + H, H)], fill=(255, 255, 255, 10), width=14)
    img = Image.alpha_composite(img.convert("RGBA"), stripe).convert("RGB")
    # amber accent bar on the left
    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, 14, H], fill=AMBER)
    return img


def draw_pill(draw, text, font):
    pad_x, pad_y = 26, 12
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x0, y0 = 70, 56
    draw.rounded_rectangle([x0, y0, x0 + tw + pad_x * 2, y0 + th + pad_y * 2],
                           radius=22, fill=AMBER)
    draw.text((x0 + pad_x, y0 + pad_y - 2), text, font=font, fill=NAVY_BOT)


def render(title, category, slug, out_path):
    img = photo_bg(slug)
    draw = ImageDraw.Draw(img)
    pill_font = ImageFont.truetype(FONT_BOLD, 30)
    title_font = ImageFont.truetype(FONT_BOLD, 66)
    brand_font = ImageFont.truetype(FONT_BOLD, 30)

    draw_pill(draw, category.upper(), pill_font)

    lines = textwrap.wrap(title, width=27)[:4]
    y = 150
    for line in lines:
        # soft shadow for legibility over photos
        draw.text((72, y + 3), line, font=title_font, fill=(0, 0, 0))
        draw.text((70, y), line, font=title_font, fill=WHITE)
        y += 82

    draw.text((70, H - 84), SITE_NAME, font=brand_font, fill=AMBER)
    draw.text((70 + draw.textbbox((0, 0), SITE_NAME, font=brand_font)[2] + 18, H - 80),
              "Windows laptop fixes, step by step",
              font=ImageFont.truetype(FONT_REG, 28), fill=MUTED)
    img.save(out_path, "WEBP", quality=85, method=6)


def main():
    force = "--force" in sys.argv
    os.makedirs(OUTDIR, exist_ok=True)
    made, skipped = 0, 0
    for fn in sorted(os.listdir(CONTENT)):
        if not fn.endswith(".md"):
            continue
        meta = parse_frontmatter(os.path.join(CONTENT, fn))
        slug = meta.get("slug") or fn[:-3]
        out = os.path.join(OUTDIR, slug + ".webp")
        if os.path.exists(out) and not force:
            skipped += 1
            continue
        cat_slug = meta.get("category", "guide")
        render(meta.get("title", slug),
               CATEGORY_NAMES.get(cat_slug, cat_slug.replace("-", " ").title()),
               slug,
               out)
        made += 1
    print(f"thumbnails: {made} generated, {skipped} skipped -> {OUTDIR}")


if __name__ == "__main__":
    main()
