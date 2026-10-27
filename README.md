<p align="center">
  <img src="logo/logo.png" width="128" alt="Harvest Poster Theme logo">
</p>

<h1 align="center">Harvest Poster Theme</h1>

<p align="center">
  A vintage-print Halloween Chrome theme in brown ink, brick orange and bone paper.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/manifest-v3-241c18" alt="Manifest V3">
  <img src="https://img.shields.io/badge/version-1.0.0-d9642a" alt="Version 1.0.0">
  <img src="https://img.shields.io/badge/chrome-dark-f5efe2" alt="Dark chrome">
  <img src="https://img.shields.io/badge/license-non--commercial-a8491a" alt="Non-commercial license">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/vaxicy/harvest-poster-theme/main/store-assets/promo/1400x560.png" alt="Harvest Poster Theme promo" width="700">
</p>

## Overview

Harvest Poster pairs a near-black brown frame with a walnut toolbar, then opens onto a bone-paper New Tab Page where a muted gold Google logo is stamped like ink. Bone ink keeps every tab, bookmark and toolbar icon readable on the dark chrome, links take a warm ember tone, and a single-row shortcut layout keeps the New Tab Page clean.

It is a Halloween theme that avoids the usual orange-and-black costume: the palette is a 1920s print poster — walnut, brick, maize and bone — with the lantern and cat motifs reserved for the mark.

## Design Concept

The source palette is a warm print set: ink brown, walnut, brick orange, maize yellow and bone paper. The two browns carry the chrome, bone paper carries the page *and* the ink on the chrome, brick and maize handle accents, and a deeper ember tone does the links so nothing on the page shouts.

| Color | Hex | RGB | Role |
|---|---|---|---|
| Ink | `#241C18` | 36, 28, 24 | Frame |
| Walnut | `#5A3B2E` | 90, 59, 46 | Toolbar |
| Brick | `#D9642A` | 217, 100, 42 | Buttons |
| Maize | `#E8C27A` | 232, 194, 122 | New Tab header / highlight |
| Paper | `#F5EFE2` | 245, 239, 226 | New Tab background / chrome ink |
| Ember | `#A8491A` | 168, 73, 26 | New Tab links |
| Dark Ink | `#2B201A` | 43, 32, 26 | New Tab text |

## Features

- Pure color, no wallpaper — fast and distraction-free
- Vintage-print palette: walnut, brick, maize and bone
- Dark brown chrome with bone ink — 14.6:1 on the frame
- Tab text, bookmark text and toolbar icons all share the same bone ink
- Single-row shortcut row and a color-matched Google logo for a clean New Tab Page
- No configuration needed — install and enjoy

## Screenshots

| Browser | Palette |
|:-:|:-:|
| <img src="https://raw.githubusercontent.com/vaxicy/harvest-poster-theme/main/store-assets/screenshots/en/screenshot-1-browser.png" width="420" alt="Harvest Poster New Tab"> | <img src="https://raw.githubusercontent.com/vaxicy/harvest-poster-theme/main/store-assets/screenshots/en/screenshot-2-palette.png" width="420" alt="Harvest Poster palette"> |

## Installation

### Load unpacked (development)

1. Download or clone this repository.
2. Open `chrome://extensions` in Chrome.
3. Enable **Developer mode** in the top right.
4. Click **Load unpacked** and select this folder (`harvest-poster-theme`).
5. The theme is active immediately.

### Package for the Chrome Web Store

```
chrome://extensions → Pack extension → select this folder → harvest-poster-theme.zip
```

Upload the resulting `.zip` to the [Chrome Web Store developer dashboard](https://chrome.google.com/webstore/devconsole).

## Store listing copy

Ready to paste into the store listing (also kept in `store-assets/store-description.txt`):

> Harvest Poster is a vintage-print Halloween Chrome theme: dark walnut chrome, a bone-paper New Tab Page, and a muted gold Google logo stamped on it. Bone ink keeps every tab, bookmark and toolbar icon readable on the dark frame. Solid colors only, no wallpaper.

## Project structure

| File | Purpose |
|---|---|
| `manifest.json` | Theme definition (single-file, inlined `theme` field) |
| `logo/logo.png` | 128×128 store icon (transparent background) |
| `store-assets/promo/440x280.png` | Small promo tile |
| `store-assets/promo/1400x560.png` | Marquee promo tile |
| `store-assets/screenshots/en/screenshot-1-browser.png` | Browser mockup screenshot (1280×800) |
| `store-assets/screenshots/en/screenshot-2-palette.png` | Palette introduction screenshot (1280×800) |
| `store-assets/store-description.txt` | Store listing description |
| `scripts/generate-logo-vector.py` | Render all SVG logo candidates with headless Chromium, build contact sheets, export `logo/logo.png` from `SELECTED` |
| `scripts/generate-screenshot-headless.py` | Regenerate the browser mockup via Playwright |
| `scripts/generate-screenshot-2-palette.py` | Regenerate the palette screenshot |
| `scripts/generate-promo.py` | Regenerate both promo tiles (1400×560 window hero, 440×280 dot palette) |
| `LICENSE` | Non-Commercial License (English / 中文) |

## Regenerating assets

Every asset is code-generated, so nothing here is hand-drawn or hand-copied:

```bash
py -3 scripts/generate-logo-vector.py         # candidates + contact sheets + logo/logo.png
py -3 scripts/generate-screenshot-headless.py # store screenshot 1 (browser mockup)
py -3 scripts/generate-screenshot-2-palette.py # store screenshot 2 (palette)
py -3 scripts/generate-promo.py               # promo 440x280 + 1400x560
```

To ship a different icon candidate, change `SELECTED` at the top of `generate-logo-vector.py` and re-run, then re-run the three asset scripts so the promo and screenshots pick up the new logo.

## License

Harvest Poster Theme is released under the Non-Commercial License. See `LICENSE` for full text (English / 中文).
