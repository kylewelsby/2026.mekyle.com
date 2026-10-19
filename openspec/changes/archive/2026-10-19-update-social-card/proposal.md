## Why

The social cards were a crop of the hero. At feed size they did not say who Kyle is or what ViaCara is, the face was small and the name ran behind his head. Kyle asked for a good generated card on 20 October 2026.

## What Changes

- Add a card template, `scripts/social-card/card.html`, built from the site's own files: the pink linen tile, the cut-out, the split white wordmark, the ViaCara lockup and the hand-drawn underline
- `scripts/capture-social-images.sh` renders the template, not the live hero, so it needs no local server
- Regenerate `static/images/og-image.jpg` (1200x630) and `static/images/twitter-card.jpg` (1200x600)
- Add `og:image:type`, `og:image:width`, `og:image:height`, `og:image:alt` and `twitter:image:alt`; change the `?v=` values
- Describe the card rules in `DESIGN.md`

## Impact

- Affected specs: `founder-homepage` (Social cards requirement)
- Affected code: `scripts/`, `static/images/`, `templates/base.html`, `DESIGN.md`
