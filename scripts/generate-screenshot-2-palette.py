#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Harvest Poster Theme — store screenshot #2 (theme introduction + palette).

1280x800 RGB. Background is a warm mid-grey (#3A3430) chosen so it is far enough
from every swatch — an assertion enforces that gap so no card can vanish.
"""
import json
import os
import time
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(ROOT))                      # relative paths only (non-ASCII path safety)


def save_png(img, path, tries=5):
    """PIL intermittently raises OSError [Errno 22] on this non-ASCII project path."""
    last = None
    for i in range(tries):
        try:
            img.save(path)
            return
        except OSError as exc:            # pragma: no cover - environment specific
            last = exc
            time.sleep(0.35 * (i + 1))
    raise last

OUT = "store-assets/screenshots/en/screenshot-2-palette.png"
W, H = 1280, 800
MARGIN = 64
RIGHT = W - MARGIN

BG = (58, 52, 48)                        # neutral plum-grey — outside the swatch set
                                         # (the old #4A0A28 equalled the Ink card, so
                                         #  that card vanished into the background)
TEXT_MAIN = (245, 239, 226)
TEXT_DIM = (178, 152, 132)
BORDER = (96, 76, 62)


def hex2rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def lin(v):
    """sRGB -> linear, for relative-luminance based ink selection."""
    v = v / 255.0
    return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4


def font(size, bold=False):
    for name in (("segoeuib.ttf", "seguisb.ttf") if bold else ("segoeui.ttf", "segoeuisl.ttf")):
        p = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts", name)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def text_w(d, s, f):
    return d.textbbox((0, 0), s, font=f)[2]


def main():
    with open("manifest.json", "r", encoding="utf-8") as f:
        m = json.load(f)
    c, props = m["theme"]["colors"], m["theme"]["properties"]

    swatches = [
        ("Ink", "#241C18", "Frame"),
        ("Walnut", "#5A3B2E", "Toolbar"),
        ("Brick", "#D9642A", "Buttons"),
        ("Maize", "#E8C27A", "Header / highlight"),
        ("Paper", "#F5EFE2", "New Tab page / ink"),
        ("Ember", "#A8491A", "Links"),
    ]
    ink = (43, 32, 26)

    # the background must not repeat any swatch, otherwise that card disappears
    for _name, _hx, _role in swatches:
        _c = hex2rgb(_hx)
        _delta = max(abs(BG[i] - _c[i]) for i in range(3))
        assert _delta >= 18, "background %s is too close to swatch %s %s (delta %d)" % (
            "#%02X%02X%02X" % BG, _name, _hx, _delta)

    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    logo = Image.open("logo/logo.png").convert("RGBA").resize((84, 84), Image.LANCZOS)
    img.paste(logo, (MARGIN, 62), logo)
    d.text((MARGIN + 108, 72), "Harvest Poster", font=font(52, True), fill=TEXT_MAIN)
    d.text((MARGIN + 110, 134), "A vintage-print palette — walnut, brick and bone",
           font=font(19), fill=TEXT_DIM)

    gap = 22
    card_w = (RIGHT - MARGIN - gap * 5) // 6
    card_h = 286
    card_y = 258
    f_hex, f_name, f_role = font(19), font(20, True), font(15)

    x = MARGIN
    for name, hx, role in swatches:
        col = hex2rgb(hx)
        # readability: dark swatches get cream ink, pale swatches get espresso ink
        lum = sum(lin(v) * w for v, w in zip(col, (0.2126, 0.7152, 0.0722)))
        card_ink = TEXT_MAIN if lum < 0.25 else ink
        d.rounded_rectangle([x, card_y, x + card_w, card_y + card_h], radius=16,
                            fill=col, outline=BORDER, width=2)
        d.text((x + 16, card_y + card_h - 92), hx, font=f_hex, fill=card_ink)
        d.text((x + 16, card_y + card_h - 64), name, font=f_name, fill=card_ink)
        d.text((x + 4, card_y + card_h + 16), role, font=f_role, fill=TEXT_DIM)
        x += card_w + gap
    last_right = x - gap
    assert last_right <= RIGHT, "swatch row overflows the right margin"

    chips = ["Solid colors, no wallpaper", "Vintage print", "Dark chrome, paper page"]
    f_chip = font(17)
    chip_y = H - MARGIN - 44
    cx = MARGIN
    for chip in chips:
        cw = text_w(d, chip, f_chip) + 44
        d.rounded_rectangle([cx, chip_y, cx + cw, chip_y + 44], radius=22,
                            fill=(70, 52, 42), outline=BORDER, width=2)
        d.text((cx + 22, chip_y + 12), chip, font=f_chip, fill=TEXT_DIM)
        cx += cw + 18
    assert cx - 18 <= RIGHT, "chip row overflows the right margin"
    assert card_y + card_h + 42 < chip_y, "role labels collide with the footer chips"
    assert chip_y + 44 <= H - 12, "footer chips too close to the canvas bottom"

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    save_png(img, OUT)
    print("saved:", OUT, img.size, img.mode, "| last swatch right:", last_right)


if __name__ == "__main__":
    main()
