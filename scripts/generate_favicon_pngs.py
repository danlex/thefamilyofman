#!/usr/bin/env python3
"""Generate favicon PNGs and ICO from a single design source.

Mirrors the geometry in site/favicon.svg so the small raster icons match the
SVG mark. Outputs:
- site/assets/icons/favicon-16.png, favicon-32.png, favicon-48.png
- site/assets/icons/apple-touch-icon.png (180x180)
- site/assets/icons/icon-192.png, icon-512.png  (PWA manifest)
- site/assets/icons/og-image.png  (1200x630 social card)
- site/favicon.ico  (multi-size: 16, 32, 48)

Run: python3 scripts/generate_favicon_pngs.py
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

REPO = Path(__file__).resolve().parent.parent
ICON_DIR = REPO / "site" / "assets" / "icons"
ICON_DIR.mkdir(parents=True, exist_ok=True)


def draw_mark(size: int, *, radius_ratio: float = 0.094) -> Image.Image:
    """Draw the F-monogram at `size` px, matching site/favicon.svg geometry.

    The SVG viewBox is 64; everything is scaled proportionally.
    """
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    s = size / 64.0  # scale factor from viewBox units to pixels
    radius = max(1, int(round(size * radius_ratio)))

    # Background rounded rect
    draw.rounded_rectangle((0, 0, size - 1, size - 1), radius=radius, fill=(17, 17, 17, 255))

    # F glyph rectangles (white on black). Coordinates from the SVG.
    rects = [
        (18, 13, 18 + 9, 13 + 38),   # vertical stem
        (18, 13, 18 + 28, 13 + 9),   # top bar
        (18, 28, 18 + 22, 28 + 8),   # middle bar
    ]
    for x0, y0, x1, y1 in rects:
        draw.rectangle(
            (round(x0 * s), round(y0 * s), round(x1 * s), round(y1 * s)),
            fill=(255, 255, 255, 255),
        )
    return img


def write_png(size: int, name: str) -> None:
    out = ICON_DIR / name
    draw_mark(size).save(out, "PNG", optimize=True)
    print(f"wrote {out.relative_to(REPO)}")


def write_ico() -> None:
    sizes = [(16, 16), (32, 32), (48, 48)]
    base = draw_mark(48)
    out = REPO / "site" / "favicon.ico"
    base.save(out, format="ICO", sizes=sizes)
    print(f"wrote {out.relative_to(REPO)}")


def find_serif_font(px: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Times New Roman Bold.ttf",
        "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
        "/System/Library/Fonts/NewYork.ttf",
        "/Library/Fonts/Georgia.ttf",
    ]
    for c in candidates:
        try:
            return ImageFont.truetype(c, px)
        except OSError:
            continue
    return ImageFont.load_default()


def write_og_image() -> None:
    """1200x630 open-graph card. Mark on left, wordmark + tagline on right."""
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Hairline rule across the top (Steichen-editorial)
    draw.rectangle((0, 0, W, 4), fill=(17, 17, 17))

    # Mark on the left, vertically centered
    mark_size = 360
    mark = draw_mark(mark_size)
    img.paste(mark, (96, (H - mark_size) // 2), mark)

    # Title + tagline on the right
    title_font = find_serif_font(76)
    sub_font = find_serif_font(34)
    small_font = find_serif_font(26)

    text_x = 96 + mark_size + 80
    title = "The Family of Man"
    sub = "Edward Steichen · MoMA 1955"
    tag = "A public wiki — Clervaux Castle, Luxembourg"

    title_y = (H - 76 - 34 - 26 - 40) // 2
    draw.text((text_x, title_y), title, fill=(17, 17, 17), font=title_font)
    draw.text((text_x, title_y + 100), sub, fill=(17, 17, 17), font=sub_font)
    draw.text((text_x, title_y + 150), tag, fill=(107, 107, 107), font=small_font)

    # Hairline rule across the bottom
    draw.rectangle((0, H - 4, W, H), fill=(17, 17, 17))

    out = ICON_DIR / "og-image.png"
    img.save(out, "PNG", optimize=True)
    print(f"wrote {out.relative_to(REPO)}")


def main() -> None:
    # Browser favicons (PNG fallback for clients that don't pick up SVG)
    write_png(16, "favicon-16.png")
    write_png(32, "favicon-32.png")
    write_png(48, "favicon-48.png")
    # Apple touch icon
    write_png(180, "apple-touch-icon.png")
    # PWA manifest
    write_png(192, "icon-192.png")
    write_png(512, "icon-512.png")
    # Maskable manifest icon (same mark but with safe-zone padding handled by rounded rect)
    write_png(512, "icon-512-maskable.png")
    # ICO multi-size
    write_ico()
    # OG / Twitter social card
    write_og_image()


if __name__ == "__main__":
    main()
