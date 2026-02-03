## MODIFIED Requirements

### Requirement: Meta Tags

The site SHALL include the following meta tags:
- `<title>` between 50 and 60 characters
- `<meta name="description">` between 110 and 160 characters
- `<meta name="keywords">` with relevant terms
- `<meta name="author">` set to "Kyle Welsby"
- `<link rel="canonical">` pointing to https://mekyle.com/

#### Scenario: Title is optimised
- **WHEN** the page is indexed
- **THEN** the title includes name, role and specialisation
- **AND** it is between 50 and 60 characters

#### Scenario: Description is optimised
- **WHEN** search results display the page
- **THEN** the description summarises expertise, experience and location
- **AND** it is between 110 and 160 characters
- **AND** it differentiates from LinkedIn profile summary

### Requirement: Twitter Card Tags

The site SHALL include Twitter Card meta tags:
- `twitter:card`: "summary_large_image"
- `twitter:site`: "@halfcube"
- `twitter:title`: Name and role
- `twitter:description`: Brief summary
- `twitter:image`: Dedicated Twitter card image URL at `/images/twitter-card.jpg`

#### Scenario: Twitter preview displays correctly
- **WHEN** the URL is shared on Twitter/X
- **THEN** a large image card is displayed using the dedicated Twitter card image
- **AND** title and description are shown

### Requirement: OG Image

The site SHALL include a social sharing image:
- Dimensions: 1200x630 pixels
- Format: JPG (quality 90, optimised)
- Design: Nord gradient background (#2E3440 to #3B4252) with circular profile photo, name, job title in frost blue (#88C0D0), keyword CTA and site URL
- Located at `/images/og-image.jpg`

#### Scenario: OG image loads
- **WHEN** social platforms request the OG image
- **THEN** a valid JPEG image is returned at `/images/og-image.jpg`
- **AND** dimensions are 1200x630 pixels

#### Scenario: OG image content is readable
- **WHEN** the OG image is previewed
- **THEN** the name is displayed as a clear headline
- **AND** the job title is visible as a subheadline
- **AND** keywords and location are shown as a call-to-action

## ADDED Requirements

### Requirement: Social Image Generation Script

The project SHALL include a reusable Python script at `scripts/generate_social_images.py` that generates social sharing images from project config.

The script SHALL:
- Read author name and job title from `config.toml` as defaults
- Read the profile photo from `static/images/profile.webp`
- Composite a Nord-themed gradient background with circular profile photo, text overlay (name, title, tagline, URL) and accent line
- Output OG image (1200x630) to `static/images/og-image.jpg`
- Output Twitter card (1200x600, cropped from OG) to `static/images/twitter-card.jpg`
- Support macOS and Linux font paths with graceful fallback
- Require only `Pillow` and `tomli` (or Python 3.11+ `tomllib`) as dependencies
- Accept CLI flags to override: `--name`, `--title`, `--tagline`, `--accent`, `--bg-top`, `--bg-bottom`, `--text-primary`, `--text-secondary`

A Claude Code slash command at `.claude/commands/generate-social-images.md` SHALL provide an interactive interface to the script via `/generate-social-images`.

#### Scenario: Script generates images from config
- **WHEN** `python3 scripts/generate_social_images.py` is run without arguments
- **THEN** `static/images/og-image.jpg` is created at 1200x630 pixels
- **AND** `static/images/twitter-card.jpg` is created at 1200x600 pixels
- **AND** both images use the current name and title from `config.toml`

#### Scenario: Script accepts CLI overrides
- **WHEN** `python3 scripts/generate_social_images.py --title "Staff Engineer" --accent "#81A1C1"` is run
- **THEN** the generated images use "Staff Engineer" as the job title
- **AND** the accent colour is `#81A1C1` instead of the default

#### Scenario: Script reflects config updates
- **WHEN** the job title in `config.toml` is changed
- **AND** the script is re-run without arguments
- **THEN** the generated images display the updated title

#### Scenario: Script runs cross-platform
- **WHEN** the script is run on macOS or Linux
- **THEN** it finds a suitable system font
- **AND** generates valid images without errors
