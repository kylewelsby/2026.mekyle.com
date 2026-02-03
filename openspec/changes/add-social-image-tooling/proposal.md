## Why

Social sharing images were missing from the deployed site, causing broken previews on LinkedIn and Twitter. Google Search Console also flagged short title/description metadata. A reusable generation script is needed so images stay in sync with config changes without manual design work.

## What Changes

- Add `scripts/generate_social_images.py` that reads `config.toml` and composites profile photo with Nord-themed gradient and text overlay
- Generate two images: OG image (1200x630) and Twitter card (1200x600)
- Update meta title to 50-60 character optimal range
- Update meta description to 110-160 character optimal range
- Use dedicated Twitter card image path separate from OG image
- Update SEO spec to reflect actual file paths and tooling

## Impact

- Affected specs: `seo` (OG Image, Twitter Card, Meta Tags requirements)
- Affected code: `scripts/generate_social_images.py`, `config.toml`, `templates/base.html`, `static/images/og-image.jpg`, `static/images/twitter-card.jpg`
