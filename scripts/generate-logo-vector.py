#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Harvest Poster Theme — vector logo candidates (SVG, headless Chromium).

Register: vintage print. The marks borrow old-poster devices — flat emblems,
rosettes, ticket arches, silhouette cut-outs — rather than glossy app-icon
gradients, and the Halloween symbols (lantern, cat, bat, candle) are treated as
printed silhouettes so they read as artwork, not clip-art.

Playwright screenshots each SVG cell with omit_background=True (true
transparency); PIL only composes the contact sheets, the inline strip and the
official logo/logo.png exported from SELECTED.

Colours come from manifest.json. Change SELECTED and re-run; never hand-copy PNGs.
"""
import json
import math
import os
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(ROOT))                      # relative paths only (non-ASCII path safety)

SIZE = 128
CELL = 512
PREVIEW = 256
SELECTED = "02"
CAND_DIR = Path("logo/candidates")
LOGO_OUT = Path("logo/logo.png")

with open("manifest.json", "r", encoding="utf-8") as f:
    _m = json.load(f)
_C, _P = _m["theme"]["colors"], _m["theme"]["properties"]


def hx(vals):
    return "#%02X%02X%02X" % tuple(vals)


INK = hx(_C["frame"])                              # #241C18
WALNUT = hx(_C["toolbar"])                         # #5A3B2E
BRICK = hx(_C["button_background_secondary"])      # #D9642A
MAIZE = hx(_C["button_background"])                # #E8C27A
PAPER = hx(_C["ntp_background"])                   # #F5EFE2
DEEP_BRICK = hx(_C["ntp_link"])                    # #A8491A

SHADOW = """
  <filter id="ds" x="-35%%" y="-35%%" width="170%%" height="170%%">
    <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="%s" flood-opacity=".22"/>
  </filter>""" % INK


def svg_open(body, defs=""):
    return ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
            'viewBox="0 0 256 256">%s%s</svg>' % (CELL, CELL, defs, body))


def rosette(cx, cy, r_out, r_in, petals, fill):
    out = []
    for i in range(petals):
        a = 360.0 * i / petals
        out.append('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s" '
                   'transform="rotate(%.1f %.1f %.1f)"/>'
                   % (cx, cy - (r_out - r_in) * 0.5, r_out * 0.30, (r_out - r_in) * 0.72,
                      fill, a, cx, cy))
    return "".join(out)


def stars(points, r_out, r_in, fill):
    out = []
    for cx, cy in points:
        pts = []
        for i in range(8):
            r = r_out if i % 2 == 0 else r_in
            a = math.radians(-90 + i * 45)
            pts.append("%.1f %.1f" % (cx + r * math.cos(a), cy + r * math.sin(a)))
        out.append('<path d="M%s Z" fill="%s"/>' % (" L".join(pts), fill))
    return "".join(out)


# ------------------------------------------------------------------ candidates
SVG_01 = svg_open("""
<defs>
  <linearGradient id="em1" x1="0" y1="0" x2="0.4" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<rect x="120" y="26" width="16" height="20" rx="6" fill="%s"/>
<circle cx="128" cy="132" r="92" fill="url(#em1)" filter="url(#ds)"/>
<g fill="%s">
  <path d="M86 112 L112 112 L99 134 Z"/>
  <path d="M144 112 L170 112 L157 134 Z"/>
  <path d="M88 156 Q106 145 121 156 Q137 145 156 156 Q166 149 170 158 Q164 178 128 178
           Q92 178 86 158 Z"/>
</g>
<circle cx="128" cy="132" r="92" fill="none" stroke="%s" stroke-opacity=".35" stroke-width="4"/>
""" % (BRICK, WALNUT, SHADOW, WALNUT, MAIZE, PAPER))

SVG_02 = svg_open("""
<defs>%s</defs>
<g filter="url(#ds)">
  <circle cx="128" cy="128" r="100" fill="%s"/>
  %s
  <circle cx="128" cy="128" r="52" fill="%s"/>
  %s
  <circle cx="128" cy="128" r="18" fill="%s"/>
</g>
""" % (SHADOW, WALNUT, rosette(128, 128, 98, 56, 16, MAIZE), BRICK,
       rosette(128, 128, 50, 20, 10, MAIZE), INK))

SVG_03 = svg_open("""
<defs>
  <mask id="mn3"><rect x="0" y="0" width="256" height="256" fill="#000"/>
    <circle cx="128" cy="122" r="86" fill="#fff"/>
    <circle cx="168" cy="94" r="72" fill="#000"/>
  </mask>
  %s
</defs>
<circle cx="128" cy="122" r="86" fill="%s" mask="url(#mn3)"/>
<g fill="%s" filter="url(#ds)">
  <!-- body -->
  <ellipse cx="128" cy="138" rx="9" ry="12"/>
  <!-- ears -->
  <path d="M120 128 l-3 -10 l8 6 Z"/>
  <path d="M136 128 l3 -10 l-8 6 Z"/>
  <!-- wings: three scallops each side -->
  <path d="M119 132 C104 118 86 116 70 126 C80 128 84 136 86 144 C94 136 100 136 104 142
           C110 134 115 134 119 140 Z"/>
  <path d="M137 132 C152 118 170 116 186 126 C176 128 172 136 170 144 C162 136 156 136 152 142
           C146 134 141 134 137 140 Z"/>
</g>
<circle cx="124" cy="134" r="2.6" fill="%s"/>
<circle cx="132" cy="134" r="2.6" fill="%s"/>
""" % (SHADOW, MAIZE, INK, DEEP_BRICK, DEEP_BRICK))

SVG_04 = svg_open("""
<defs>%s</defs>
<g filter="url(#ds)">
  <!-- thin arch outline instead of a heavy filled frame -->
  <path d="M56 216 V116 a72 72 0 0 1 144 0 V216" fill="none" stroke="%s"
        stroke-width="13" stroke-linecap="round"/>
  <!-- ground line -->
  <path d="M64 216 H192" stroke="%s" stroke-width="9" stroke-linecap="round"/>
  <!-- gourd -->
  <path d="M128 148 C150 164 160 186 156 202 H100 C96 186 106 164 128 148 Z" fill="%s"/>
  <path d="M121 145 h14 v-14 h-14 z" fill="%s"/>
  %s
</g>
""" % (SHADOW, WALNUT, WALNUT, BRICK, WALNUT,
       stars([(84, 104), (172, 104), (128, 116)], 10, 4.2, MAIZE)))

SVG_05 = svg_open("""
<defs>
  <linearGradient id="mn5" x1="0" y1="0" x2="0.6" y2="1">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<circle cx="128" cy="120" r="86" fill="url(#mn5)" filter="url(#ds)"/>
<g fill="%s">
  <path d="M96 216 C96 176 108 152 128 152 C148 152 160 176 160 216 Z"/>
  <circle cx="128" cy="130" r="34"/>
  <path d="M104 106 L98 78 L122 96 Z"/>
  <path d="M152 106 L158 78 L134 96 Z"/>
  <path d="M158 200 C186 196 194 170 180 154 C176 172 168 184 152 190 Z"/>
</g>
<g fill="%s">
  <circle cx="118" cy="126" r="5"/>
  <circle cx="140" cy="126" r="5"/>
</g>
""" % (MAIZE, PAPER, SHADOW, INK, MAIZE))

SVG_06 = svg_open("""
<defs>
  <linearGradient id="fl6" x1="0" y1="1" x2="0.4" y2="0">
    <stop offset="0" stop-color="%s"/>
    <stop offset="1" stop-color="%s"/>
  </linearGradient>
  %s
</defs>
<g filter="url(#ds)">
  <path d="M56 216 V120 a72 72 0 0 1 144 0 V216 Z" fill="%s"/>
  <path d="M70 216 V120 a58 58 0 0 1 116 0 V216 Z" fill="%s"/>
  <rect x="112" y="130" width="32" height="70" rx="6" fill="%s"/>
  <path d="M128 128 C118 112 128 96 128 84 C138 96 148 112 128 128 Z" fill="url(#fl6)"/>
  <path d="M92 206 h72 a8 8 0 0 1 0 16 h-72 a8 8 0 0 1 0 -16 Z" fill="%s"/>
</g>
""" % (DEEP_BRICK, MAIZE, SHADOW, INK, PAPER, MAIZE, BRICK))

CANDIDATES = [
    ("01", "lantern-emblem", "Printed jack-o'-lantern emblem — clearest Halloween", SVG_01),
    ("02", "poster-rosette", "Layered rosette — pure vintage print, no symbol", SVG_02),
    ("03", "bat-moon", "Bat across a crescent — classic silhouette", SVG_03),
    ("04", "ticket-arch", "Arch ticket with gourd and stars — poster framing", SVG_04),
    ("05", "cat-moon", "Black cat against a maize moon — quiet, elegant", SVG_05),
    ("06", "candle-arch", "Candle in an arch — warm and atmospheric", SVG_06),
]


def font(size, bold=False):
    for name in (("segoeuib.ttf", "seguisb.ttf") if bold else ("segoeui.ttf", "segoeuisl.ttf")):
        p = os.path.join(os.environ.get("WINDIR", r"C:\Windows"), "Fonts", name)
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()


def render_cells():
    cells = "".join('<div id="cell%s" style="width:%dpx;height:%dpx">%s</div>' % (num, CELL, CELL, svg)
                    for num, _n, _d, svg in CANDIDATES)
    html = ('<!doctype html><html><head><meta charset="utf-8"><style>'
            'html,body{margin:0;padding:0;background:transparent}'
            '#grid{display:flex;flex-wrap:wrap;width:%dpx}div[id^=cell]{display:block}'
            '</style></head><body><div id="grid">%s</div></body></html>' % (CELL * 3, cells))
    out = {}
    with sync_playwright() as p:
        try:
            b = p.chromium.launch()
        except Exception:
            # bundled headless shell may be missing after a Playwright update
            b = p.chromium.launch(channel="chrome")
        pg = b.new_page(viewport={"width": CELL * 3, "height": CELL * 2})
        pg.set_content(html)
        for num, name, _d, _svg in CANDIDATES:
            path = CAND_DIR / ("%s-%s.png" % (num, name))
            pg.locator("#cell" + num).screenshot(path=str(path), omit_background=True)
            img = Image.open(path).convert("RGBA").resize((PREVIEW, PREVIEW), Image.LANCZOS)
            img.save(path)
            bbox = img.split()[3].getbbox()
            assert bbox, "candidate %s rendered empty" % name
            assert bbox[0] > 6 and bbox[1] > 6 and bbox[2] < PREVIEW - 6 and bbox[3] < PREVIEW - 6, \
                "candidate %s touches the canvas edge: %s" % (name, bbox)
            out[num] = img
            print("candidate %s %s -> alpha bbox %s" % (num, name, bbox))
        b.close()
    return out


def contact_sheet(rendered, bg, txt, sub, path, title):
    cols, rows = 3, 2
    cw, ch = 384, 374
    gap, margin = 28, 40
    W = margin * 2 + cols * cw + (cols - 1) * gap
    H = margin * 2 + 34 + rows * ch + (rows - 1) * gap
    sheet = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(sheet)
    f_title, f_name, f_desc, f_file = font(24, True), font(21, True), font(15), font(14)
    d.text((margin, margin), title, font=f_title, fill=txt)
    y0 = margin + 34
    for i, (num, name, desc, _svg) in enumerate(CANDIDATES):
        r, c = divmod(i, cols)
        x = margin + c * (cw + gap)
        y = y0 + r * (ch + gap)
        big = rendered[num].resize((220, 220), Image.LANCZOS)
        sheet.paste(big, (x + (cw - 220) // 2, y + 14), big)
        d.text((x + 18, y + 250), "%s · %s" % (num, name), font=f_name, fill=txt)
        d.text((x + 18, y + 280), desc, font=f_desc, fill=sub)
        thumb = rendered[num].resize((32, 32), Image.LANCZOS)
        sheet.paste(thumb, (x + 18, y + 330), thumb)
        d.text((x + 60, y + 339), "%s.png  256x256" % name, font=f_file, fill=sub)
        assert y + 300 <= y + 322, "text block collides with the thumbnail row"
    sheet.save(path)
    print("saved:", path, sheet.size)


def inline_strip(rendered, path):
    n, cell, gap, margin = len(CANDIDATES), 108, 22, 30
    W = margin * 2 + n * cell + (n - 1) * gap
    H = margin * 2 + cell + 30
    strip = Image.new("RGB", (W, H), (245, 239, 226))
    d = ImageDraw.Draw(strip)
    f = font(15, True)
    for i, (num, _n, _d, _s) in enumerate(CANDIDATES):
        x = margin + i * (cell + gap)
        img = rendered[num].resize((cell, cell), Image.LANCZOS)
        strip.paste(img, (x, margin), img)
        d.text((x + cell // 2 - 8, margin + cell + 8), num, font=f, fill=(36, 28, 24))
    strip.save(path)
    print("saved:", path, strip.size)


def main():
    CAND_DIR.mkdir(parents=True, exist_ok=True)
    rendered = render_cells()
    contact_sheet(rendered, (245, 239, 226), (36, 28, 24), (140, 118, 104),
                  CAND_DIR / "contact-light.png", "Harvest Poster — vector logo candidates (light)")
    contact_sheet(rendered, (28, 22, 19), (245, 239, 226), (168, 140, 120),
                  CAND_DIR / "contact-dark.png", "Harvest Poster — vector logo candidates (dark)")
    inline_strip(rendered, CAND_DIR / "inline-strip.png")
    sel = [c for c in CANDIDATES if c[0] == SELECTED][0]
    icon = rendered[sel[0]].resize((SIZE, SIZE), Image.LANCZOS)
    icon.save(LOGO_OUT)
    print("official icon from SELECTED=%s (%s):" % (sel[0], sel[1]), LOGO_OUT, icon.size)


if __name__ == "__main__":
    main()
