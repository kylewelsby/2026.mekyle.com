# Design: founder homepage

This file describes the homepage at `/`. The privacy page keeps the older Nord design in `sass/_variables.scss`. `PRODUCT.md` holds the audiences and the brand commitments.

The design came from a prototype round in October 2026. The prototype branch `feat/viacara-founder-page-prototypes` keeps the variants that Kyle compared. Kyle chose variant F: one full curtain, pink to grey.

## Page structure

1. **Hero.** Kyle's name as a large white wordmark. The cut-out portrait stands in front of the name. The pink linen curtain fills the background.
2. **Letter.** A light card that overlaps the hero. It holds the founder's letter, the film, the join action and the transcript.
3. **Curtain run.** The curtain continues behind the letter. It fades from pink to grey and then runs into the laptop photograph with no visible join.
4. **P.S.** The laptop photograph, then the engineering record on a soft floor haze.
5. **Outside of work.** The sofa photograph on a blurred copy of itself.
6. **Footer.** Copyright, privacy, earlier sites and the photography credit.

## Colour

| Token | Value | Use |
|---|---|---|
| `$f-lilac` | `#B9B4CE` | Page ground, footer |
| `$f-sky` | `#EFF7FA` | Letter card |
| `$f-blue` | `#26365A` | Headings in the letter, links, pills |
| `$f-navy` | `#161B2A` | Text on the photographs and floor |
| `$f-ink` | `#2B2B2B` | Body text |
| `$f-storm` | `#5E5E66` | Quiet text, captions |
| `$f-twilight` | `#7985FF` | Hand-drawn underline and ring |
| `$f-overcast` | `#D5D5D5` | Rules in the letter |
| `$f-sheet` | `#F9F9F9` | Text on pills |

The colour names and Urbanist come from the ViaCara brand. Use the ViaCara lockup by its rules: clear space and no recolouring.

## Type

- Urbanist, self-hosted as two variable files (`static/fonts/`). Weights 300 to 700, roman and italic.
- Body 1.1875rem with a line height of 1.6. The letter lead is 1.375rem.
- The name in the hero is an SVG wordmark (`static/brand/`), so it does not wait for the font.
- Inline links keep their underline. Colour alone does not separate them from body text (WCAG 1.4.1).

## Imagery

Fiona Finchett took the photographs in September 2026. Kyle holds a perpetual licence. Credit her in the footer only.

| File | Content |
|---|---|
| `kyle-curtain-arms-crossed-cutout*.webp` | Hero cut-out, 1067 and 1601 px wide |
| `plate-curtain-grey-laptop-{1680,3360}.webp` | Laptop photograph at 1x and 2x |
| `plate-sofa-{1680,3360}.webp` | Sofa photograph at 1x and 2x; `plate-sofa-1280.webp` feeds the blur |
| `linen-{pink,grey}-tile-{1680,3360}.webp` | Periodic curtain tiles, 281 and 562 rows |
| `floor-{top,mid,bottom}-{1680,3360}.webp` | Floor haze between the two photographs |
| `poster-live.webp`, `founder-film.en.vtt` | Film poster and caption track |

### How the curtain joins the photograph

The grey tile and the laptop photograph come from one canvas, so the tile's last row continues row 0 of the photograph.

1. FLUX Fill (`flux-pro-1.0-fill`) grew the photograph's grey linen upward at 2x. It used a texture prompt without the word "curtain", at guidance 30.
2. The tile uses only straight rows near the photograph. It runs down the clean top rows of the photograph, back up through the Fill rows, then down again into row 0. It has no seam cuts and no sideways warps.
3. Near each turn row, a small sideways ease brings the fold slant to zero, so the turn makes no V shape.
4. The Fill rows match the photograph's column brightness. The top rows of the photograph lost a slight vignette, so the photograph and the tile match.
5. The pink tile is the grey tile dyed by brightness to the velvet palette of the hero photograph. It has the same fold positions, so the fade from pink to grey does not ghost.
6. Files are encoded with `cwebp -sharp_yuv` at quality 88 to 90.

If you replace a tile, keep these rules:

- Rebuild the grey tile and the laptop photograph together, or the join breaks.
- Keep the pink and grey tiles at the same size and fold positions.
- Give a replaced file a new name. `static/_headers` caches `/media/*` as immutable.

## Layout rules

- The curtain backgrounds anchor at `center bottom` and repeat on the y axis. The bottom of the run must meet row 0 of the laptop photograph.
- On screens up to 720 px wide, the backgrounds and photographs scale to 222.46% so that Kyle stays in frame. The photographs use a 4:5 crop.
- The letter overlaps the hero by `clamp(6rem, 13vw, 12rem)` (4rem on phones).

## Motion

- The name rises in once on load.
- With scroll-driven animation support, the name drifts down 26vh over the first screen. This is CSS only.
- `prefers-reduced-motion: reduce` turns all motion off.

## Performance

- The homepage loads `founder.css` only. The privacy page loads `style.css`.
- The cut-out is the LCP image with `fetchpriority="high"`. Photographs below the fold load lazily.
- Backgrounds use `image-set()` with 1x and 2x files. Images use `srcset` and `sizes`.
- The film loads only when someone presses play (`preload="none"`). It comes from `assets.viacara.com`, which the CSP allows in `media-src`.
