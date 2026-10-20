#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["pillow>=11", "numpy>=2"]
# ///
"""Renders the favicons from the hero cut-out on a pink radial gradient.

Usage: scripts/render-favicons.py
"""
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "static"
CUTOUT = ROOT / "static/media/kyle-curtain-arms-crossed-cutout-2400.webp"
CUTOUT_HAIR_TOP_Y = 386
CUTOUT_CHIN_Y = 1125
CUTOUT_HEAD_X = 804

SIZE = 1440
CENTRE = SIZE / 2
RADIUS = SIZE * 0.467
HEAD_FRACTION = 0.55
SQUARE_HEAD_FRACTION = 0.48

PINK_LIGHT = np.array([227, 206, 211])
PINK_MID = np.array([199, 160, 166])
PINK_DEEP = np.array([133, 89, 92])
GRADIENT_SPAN = SIZE * 0.62
GRADIENT_KNEE = 0.55


def distance_from(centre_y):
    y, x = np.mgrid[0:SIZE, 0:SIZE].astype(float)
    return np.hypot(x - CENTRE, y - centre_y)


def background(alpha=1.0):
    t = np.clip(distance_from(CENTRE * 0.8) / GRADIENT_SPAN, 0, 1)[..., None]
    rgb = np.where(
        t < GRADIENT_KNEE,
        PINK_LIGHT + (PINK_MID - PINK_LIGHT) * t / GRADIENT_KNEE,
        PINK_MID + (PINK_DEEP - PINK_MID) * (t - GRADIENT_KNEE) / (1 - GRADIENT_KNEE),
    )
    rgba = np.dstack([rgb, np.broadcast_to(alpha, (SIZE, SIZE)) * 255])
    return Image.fromarray(rgba.astype(np.uint8), "RGBA")


def person(head_fraction, hair_top_y):
    cutout = Image.open(CUTOUT).convert("RGBA")
    scale = SIZE * head_fraction / (CUTOUT_CHIN_Y - CUTOUT_HAIR_TOP_Y)
    cutout = cutout.resize((round(cutout.width * scale), round(cutout.height * scale)), Image.LANCZOS)
    layer = Image.new("RGBA", (SIZE, SIZE))
    layer.alpha_composite(cutout, (round(CENTRE - CUTOUT_HEAD_X * scale), round(hair_top_y - CUTOUT_HAIR_TOP_Y * scale)))
    return layer


def round_icon():
    disc = np.clip(RADIUS - distance_from(CENTRE) + 0.5, 0, 1)
    figure = person(HEAD_FRACTION, CENTRE - RADIUS - SIZE * 0.03)
    hair_free = background(disc)
    hair_free.alpha_composite(figure)
    clipped = background()
    clipped.alpha_composite(figure)
    clipped = np.asarray(clipped, dtype=float).copy()
    clipped[..., 3] = disc * 255
    rgba = np.asarray(hair_free, dtype=float).copy()
    rgba[int(CENTRE):] = clipped[int(CENTRE):]
    return Image.fromarray(rgba.astype(np.uint8), "RGBA")


def square_icon():
    art = background()
    art.alpha_composite(person(SQUARE_HEAD_FRACTION, SIZE * 0.13))
    return art.convert("RGB")


def main():
    round_art = round_icon()
    frames = {px: round_art.resize((px, px), Image.LANCZOS) for px in (16, 32, 48, 192)}
    for px in (16, 32, 192):
        frames[px].save(OUT / f"favicon-{px}x{px}.png", optimize=True)
    frames[48].save(OUT / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)], append_images=[frames[16], frames[32]])
    square_icon().resize((180, 180), Image.LANCZOS).save(OUT / "apple-touch-icon.png", optimize=True)


if __name__ == "__main__":
    main()
