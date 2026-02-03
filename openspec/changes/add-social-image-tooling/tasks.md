## 1. Social Image Generation Script

- [x] 1.1 Create `scripts/generate_social_images.py` with Pillow-based image compositing
- [x] 1.2 Read author name and job title from `config.toml`
- [x] 1.3 Generate OG image (1200x630) with Nord gradient, circular profile photo and text overlay
- [x] 1.4 Generate Twitter card (1200x600) cropped from OG image
- [x] 1.5 Add cross-platform font fallback (macOS + Linux)
- [x] 1.6 Add CLI argument support (--name, --title, --tagline, --accent, --bg-top, --bg-bottom, --text-primary, --text-secondary)

## 2. Claude Code Slash Command

- [x] 2.1 Create `.claude/commands/generate-social-images.md` with flag documentation and instructions

## 3. Metadata Improvements

- [x] 3.1 Update `config.toml` title to 50-60 character optimal range
- [x] 3.2 Update `config.toml` description to 110-160 character optimal range
- [x] 3.3 Update `config.toml` keywords to broader positioning (removed domain-specific narrowing)
- [x] 3.4 Update `templates/base.html` to use dedicated `twitter-card.jpg` for Twitter image

## 4. Verification

- [x] 4.1 Run `zola build` and confirm successful build
- [x] 4.2 Verify OG image and Twitter card are present in `public/images/`
- [x] 4.3 Verify meta tags in built HTML contain correct image paths
- [x] 4.4 Test script with CLI overrides (--title, --tagline)
