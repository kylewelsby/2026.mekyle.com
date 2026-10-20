# /// script
# requires-python = ">=3.11"
# dependencies = ["pillow>=11", "numpy>=2"]
# ///
"""Renders the favicons from the hero cut-out on the pink linen.

Usage: uv run scripts/render-favicons.py [--out DIR] [--background linen|radial]
"""
import argparse
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
CUTOUT = ROOT / "static/media/kyle-curtain-arms-crossed-cutout-2400.webp"
LINEN = ROOT / "static/media/linen-pink-tile-3360.webp"

SIZE = 1440
CENTRE = SIZE / 2
RADIUS = SIZE * 0.467
HAIR_TOP = 386
CHIN = 1125
HEAD_X = 804
HEAD_FRACTION = 0.55
SQUARE_HEAD_FRACTION = 0.48

PINK_LIGHT = np.array([227, 206, 211])
PINK_MID = np.array([199, 160, 166])
PINK_DEEP = np.array([133, 89, 92])


def ramp(centre_y, inner, mid, outer):
    y, x = np.mgrid[0:SIZE, 0:SIZE].astype(float)
    d = np.clip(np.hypot(x - CENTRE, y - centre_y) / (SIZE * 0.62), 0, 1)[..., None]
    return np.where(
        d < 0.55,
        inner + (mid - inner) * d / 0.55,
        mid + (outer - mid) * (d - 0.55) / 0.45,
    )


def background(kind, centre_y):
    if kind == "radial":
        rgb = ramp(centre_y, PINK_LIGHT, PINK_MID, PINK_DEEP)
    else:
        tile = Image.open(LINEN).convert("RGB")
        tile = tile.crop((1100, 0, 2300, tile.height))
        tile = tile.resize((SIZE, round(tile.height * SIZE / tile.width)), Image.LANCZOS)
        sheet = Image.new("RGB", (SIZE, SIZE))
        for top in range(0, SIZE, tile.height):
            sheet.paste(tile, (0, top))
        sheet = sheet.filter(ImageFilter.GaussianBlur(SIZE / 240))
        rgb = np.asarray(sheet, dtype=float) * ramp(centre_y, 1.12, 1.0, 0.86)
    return Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8), "RGB").convert("RGBA")


def person(head_fraction, hair_top_y):
    cutout = Image.open(CUTOUT).convert("RGBA")
    scale = SIZE * head_fraction / (CHIN - HAIR_TOP)
    cutout = cutout.resize((round(cutout.width * scale), round(cutout.height * scale)), Image.LANCZOS)
    layer = Image.new("RGBA", (SIZE, SIZE))
    layer.alpha_composite(cutout, (round(CENTRE - HEAD_X * scale), round(hair_top_y - HAIR_TOP * scale)))
    return layer


def circle_mask():
    y, x = np.mgrid[0:SIZE, 0:SIZE].astype(float)
    return np.clip(RADIUS - np.hypot(x - CENTRE, y - CENTRE) + 0.5, 0, 1)


def round_icon(kind):
    figure = person(HEAD_FRACTION, CENTRE - RADIUS - SIZE * 0.03)
    art = background(kind, CENTRE * 0.8)
    art.alpha_composite(figure)
    head = np.asarray(figure, dtype=float)[..., 3] / 255
    head[int(CENTRE):] = 0
    rgba = np.asarray(art, dtype=float)
    rgba[..., 3] = np.maximum(circle_mask(), head) * 255
    return Image.fromarray(rgba.astype(np.uint8), "RGBA")


def square_icon(kind):
    art = background(kind, CENTRE * 0.8)
    art.alpha_composite(person(SQUARE_HEAD_FRACTION, SIZE * 0.13))
    return art.convert("RGB")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path, default=ROOT / "static")
    parser.add_argument("--background", choices=["linen", "radial"], default="linen")
    args = parser.parse_args()
    args.out.mkdir(parents=True, exist_ok=True)

    round_art = round_icon(args.background)
    frames = {px: round_art.resize((px, px), Image.LANCZOS) for px in (16, 32, 48, 192)}
    for px in (16, 32, 192):
        frames[px].save(args.out / f"favicon-{px}x{px}.png", optimize=True)
    frames[48].save(args.out / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)], append_images=[frames[16], frames[32]])
    square_icon(args.background).resize((180, 180), Image.LANCZOS).save(
        args.out / "apple-touch-icon.png", optimize=True
    )


if __name__ == "__main__":
    main()
