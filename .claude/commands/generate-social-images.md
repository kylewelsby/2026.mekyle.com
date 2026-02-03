---
name: generate-social-images
description: Generate or update OG image and Twitter card for social sharing
argument-hint: "[--title 'Job Title'] [--tagline 'Keywords'] [--accent '#hex']"
---

Generate social sharing images (OG + Twitter Card) using the script at `scripts/generate_social_images.py`.

The script reads defaults from `config.toml` but all values can be overridden via CLI flags.

## Available flags

| Flag | Purpose | Default |
|------|---------|---------|
| `--name` | Display name | From `config.toml` `extra.author` |
| `--title` | Job title subtitle | Parsed from `config.toml` `title` |
| `--tagline` | Keywords/CTA line | `Distributed Systems · Architecture · Manchester` |
| `--accent` | Accent hex colour (title, URL, glow) | `#88C0D0` (Nord frost) |
| `--bg-top` | Top gradient hex colour | `#2E3440` (Nord polar night) |
| `--bg-bottom` | Bottom gradient hex colour | `#3B4252` |
| `--text-primary` | Name text hex colour | `#ECEFF4` (Nord snow) |
| `--text-secondary` | Tagline text hex colour | `#D8DEE9` |

## Instructions

1. If the user provided arguments (`$ARGUMENTS`), parse them into the appropriate `--flags` for the script
2. Run the script: `python3 scripts/generate_social_images.py $ARGUMENTS`
3. Read the generated `static/images/og-image.jpg` to show the result
4. Ask if the user wants any adjustments
5. If satisfied, run `zola build` to include the updated images in the build output
