## 1. Homepage

- [x] 1.1 Port variant F into `templates/index.html` with fixed IDs and `main-content` for the skip link
- [x] 1.2 Add `html_attrs`, `styles` and `footer` blocks to `templates/base.html`
- [x] 1.3 Port the F styles into `sass/founder.scss` with production asset paths
- [x] 1.4 Copy only the assets that F uses into `static/media/`, `static/brand/` and `static/fonts/`
- [x] 1.5 Remove the old homepage styles and data

## 2. Content and metadata

- [x] 2.1 Update `config.toml` title, description and keywords
- [x] 2.2 Update the Person JSON-LD (job title and ViaCara)
- [x] 2.3 Rewrite `static/llms.txt` to match the page
- [x] 2.4 Capture new social cards from the hero
- [x] 2.5 Update `CLAUDE.md`; add `DESIGN.md` and `PRODUCT.md`

## 3. Delivery

- [x] 3.1 Add `media-src` for `assets.viacara.com` to the CSP
- [x] 3.2 Build with `zola build`
- [x] 3.3 Run Lighthouse on the Cloudflare Pages preview
- [ ] 3.4 Kyle approves the pull request
