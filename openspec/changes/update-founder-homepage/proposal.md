## Why

Kyle founded ViaCara and recorded a founder film. The homepage still presented him as a Senior Software Engineer seeking Staff roles, and the social cards still showed his old name. Kyle compared prototype variants in October 2026 and chose variant F: a founder's letter on one linen curtain, with the engineering record as a P.S. (branch `feat/viacara-founder-page-prototypes`).

## What Changes

- Replace the homepage with the founder design: name hero, letter with the founder film, P.S. with the engineering record, "Outside of work" and a new footer
- Add `sass/founder.scss`; the homepage loads it in place of `style.css`
- Remove the old homepage styles (`_hero`, `_network-bg`, `_waves`, `_sections`, `_skills-scroll`) and the homepage data in `content/_index.md`
- Add 2x photographs and curtain tiles under `static/media/`, wordmarks under `static/brand/` and Urbanist under `static/fonts/`
- Update the title, description, keywords and Person JSON-LD to founder of ViaCara
- Rewrite `static/llms.txt` to match the page
- Allow the film host in the CSP (`media-src`) and cache `/media/*` and `/brand/*`
- Capture the social cards from the hero (`scripts/capture-social-images.sh`); remove the old Nord card generator
- Add `DESIGN.md` and `PRODUCT.md`; update `CLAUDE.md`

## Impact

- Affected specs: new `founder-homepage` capability. It supersedes the hero, skills-scroll and visual-design requirements of `build-portfolio-2026` for the homepage only. The privacy page keeps the Nord design.
- Affected code: `templates/base.html`, `templates/index.html`, `sass/`, `static/`, `config.toml`, `content/_index.md`, `scripts/`
