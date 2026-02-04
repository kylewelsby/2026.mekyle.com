#!/usr/bin/env python3
"""
Generate social sharing images (OG + Twitter Card) for mekyle.com.

Reads config from config.toml and composites the profile photo with
Nord-themed gradient background and text overlay.

Usage:
    python3 scripts/generate_social_images.py
    python3 scripts/generate_social_images.py --title "Staff Engineer"
    python3 scripts/generate_social_images.py --accent "#81A1C1" --bg-top "#3B4252"
    python3 scripts/generate_social_images.py --tagline "Distributed Systems · Fintech · London"

Requirements:
    pip install Pillow tomli
"""
import argparse
import os
import sys

try:
    import tomli
except ImportError:
    try:
        import tomllib as tomli
    except ImportError:
        print("Error: tomli not found. Install with: pip install tomli")
        print("  (Python 3.11+ has tomllib built-in)")
        sys.exit(1)

from PIL import Image, ImageDraw, ImageFont

# Paths
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(ROOT, "config.toml")
PROFILE_PATH = os.path.join(ROOT, "static", "images", "profile.webp")
OUTPUT_OG = os.path.join(ROOT, "static", "images", "og-image.jpg")
OUTPUT_TWITTER = os.path.join(ROOT, "static", "images", "twitter-card.jpg")

# Dimensions
OG_WIDTH = 1200
OG_HEIGHT = 630
TWITTER_HEIGHT = 600

# Nord palette defaults
DEFAULTS = {
    "bg_top": "#2E3440",
    "bg_bottom": "#3B4252",
    "text_primary": "#ECEFF4",
    "accent": "#88C0D0",
    "text_secondary": "#D8DEE9",
    "tagline": "Distributed Systems · Architecture · Manchester",
    "cta": "View my work \u2192 mekyle.com",
}

# Font paths (macOS + Linux fallbacks)
BOLD_FONT_PATHS = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/SFNS.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
]
REGULAR_FONT_PATHS = [
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/System/Library/Fonts/SFNS.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
]


def hex_to_rgb(hex_colour):
    """Convert hex colour string to RGB tuple."""
    hex_colour = hex_colour.lstrip("#")
    return tuple(int(hex_colour[i : i + 2], 16) for i in (0, 2, 4))


def load_config():
    """Read name, title and keywords from config.toml."""
    with open(CONFIG_PATH, "rb") as f:
        config = tomli.load(f)

    extra = config.get("extra", {})
    site_title = config.get("title", "")
    parts = site_title.split("|")
    job_title = parts[1].strip().split("·")[0].strip() if len(parts) > 1 else ""

    return {
        "name": extra.get("author", "Kyle Welsby"),
        "job_title": job_title or "Senior Software Engineer",
        "keywords": ", ".join(extra.get("keywords", [])[:3]),
        "base_url": config.get("base_url", "https://mekyle.com"),
    }


def load_font(paths, size):
    """Try loading a font from multiple paths, fall back to default."""
    for path in paths:
        if os.path.exists(path):
            try:
                return ImageFont.truetype(path, size)
            except Exception:
                continue
    return ImageFont.load_default()


def draw_gradient(img, top_colour, bottom_colour):
    """Draw a vertical gradient across the image."""
    draw = ImageDraw.Draw(img)
    width, height = img.size
    for y in range(height):
        ratio = y / height
        r = int(top_colour[0] + (bottom_colour[0] - top_colour[0]) * ratio)
        g = int(top_colour[1] + (bottom_colour[1] - top_colour[1]) * ratio)
        b = int(top_colour[2] + (bottom_colour[2] - top_colour[2]) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))


def create_circular_profile(profile_path, size):
    """Load profile image and apply circular mask."""
    profile = Image.open(profile_path).convert("RGBA")
    profile = profile.resize((size, size), Image.LANCZOS)

    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size, size), fill=255)

    result = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    result.paste(profile, (0, 0), mask)
    return result


def generate(config, colours):
    """Generate OG and Twitter card images."""
    bg_top = hex_to_rgb(colours["bg_top"])
    bg_bottom = hex_to_rgb(colours["bg_bottom"])
    text_primary = hex_to_rgb(colours["text_primary"])
    accent = hex_to_rgb(colours["accent"])
    text_secondary = hex_to_rgb(colours["text_secondary"])

    # Create base image with gradient
    img = Image.new("RGB", (OG_WIDTH, OG_HEIGHT), bg_top)
    draw_gradient(img, bg_top, bg_bottom)

    # Profile photo
    profile_size = 420
    profile = create_circular_profile(PROFILE_PATH, profile_size)

    # Glow ring around profile
    glow = Image.new("RGBA", (profile_size + 8, profile_size + 8), (0, 0, 0, 0))
    ImageDraw.Draw(glow).ellipse(
        (0, 0, profile_size + 7, profile_size + 7),
        outline=accent + (100,),
        width=4,
    )

    # Position profile on left
    profile_x = 60
    profile_y = (OG_HEIGHT - profile_size) // 2
    img.paste(glow, (profile_x - 4, profile_y - 4), glow)
    img.paste(profile, (profile_x, profile_y), profile)

    # Load fonts
    font_name = load_font(BOLD_FONT_PATHS, 72)
    font_title = load_font(BOLD_FONT_PATHS, 36)
    font_cta = load_font(REGULAR_FONT_PATHS, 26)
    font_url = load_font(REGULAR_FONT_PATHS, 20)

    # Text positioning
    text_x = profile_x + profile_size + 60
    draw = ImageDraw.Draw(img)

    draw.text((text_x, 200), config["name"], fill=text_primary, font=font_name)
    draw.text((text_x, 290), config["job_title"], fill=accent, font=font_title)

    # Accent line
    draw.rectangle([(text_x, 340), (text_x + 200, 343)], fill=accent + (80,))

    # Keywords / CTA
    draw.text(
        (text_x, 360),
        colours["tagline"],
        fill=text_secondary,
        font=font_cta,
    )

    # CTA
    font_cta_bold = load_font(BOLD_FONT_PATHS, 22)
    draw.text((text_x, 420), colours["cta"], fill=accent, font=font_cta_bold)

    # Save OG image
    img.convert("RGB").save(OUTPUT_OG, "JPEG", quality=90, optimize=True)
    print(f"  OG image:     {OUTPUT_OG} ({os.path.getsize(OUTPUT_OG) // 1024}KB)")

    # Save Twitter card (cropped to 2:1)
    twitter_crop_y = (OG_HEIGHT - TWITTER_HEIGHT) // 2
    twitter_img = img.crop((0, twitter_crop_y, OG_WIDTH, twitter_crop_y + TWITTER_HEIGHT))
    twitter_img.convert("RGB").save(OUTPUT_TWITTER, "JPEG", quality=90, optimize=True)
    print(f"  Twitter card: {OUTPUT_TWITTER} ({os.path.getsize(OUTPUT_TWITTER) // 1024}KB)")


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Generate social sharing images for mekyle.com"
    )
    parser.add_argument(
        "--name", help="Override name (default: from config.toml)"
    )
    parser.add_argument(
        "--title", help="Override job title (default: from config.toml)"
    )
    parser.add_argument(
        "--tagline",
        default=DEFAULTS["tagline"],
        help=f"Keywords/CTA line (default: {DEFAULTS['tagline']})",
    )
    parser.add_argument(
        "--bg-top",
        default=DEFAULTS["bg_top"],
        help=f"Top gradient hex colour (default: {DEFAULTS['bg_top']})",
    )
    parser.add_argument(
        "--bg-bottom",
        default=DEFAULTS["bg_bottom"],
        help=f"Bottom gradient hex colour (default: {DEFAULTS['bg_bottom']})",
    )
    parser.add_argument(
        "--accent",
        default=DEFAULTS["accent"],
        help=f"Accent hex colour for title and URL (default: {DEFAULTS['accent']})",
    )
    parser.add_argument(
        "--text-primary",
        default=DEFAULTS["text_primary"],
        help=f"Primary text hex colour (default: {DEFAULTS['text_primary']})",
    )
    parser.add_argument(
        "--text-secondary",
        default=DEFAULTS["text_secondary"],
        help=f"Secondary text hex colour (default: {DEFAULTS['text_secondary']})",
    )
    parser.add_argument(
        "--cta",
        default=DEFAULTS["cta"],
        help=f"Call-to-action text (default: {DEFAULTS['cta']})",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    print("Generating social images...")
    config = load_config()

    # Apply CLI overrides
    if args.name:
        config["name"] = args.name
    if args.title:
        config["job_title"] = args.title

    colours = {
        "bg_top": args.bg_top,
        "bg_bottom": args.bg_bottom,
        "text_primary": args.text_primary,
        "accent": args.accent,
        "text_secondary": args.text_secondary,
        "tagline": args.tagline,
        "cta": args.cta,
    }

    print(f"  Name:    {config['name']}")
    print(f"  Title:   {config['job_title']}")
    print(f"  Tagline: {colours['tagline']}")
    print(f"  Accent:  {colours['accent']}")
    generate(config, colours)
    print("Done!")


if __name__ == "__main__":
    main()
