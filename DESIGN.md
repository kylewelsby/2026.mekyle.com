# Design: founder homepage

This file describes the homepage at `/`. The privacy page keeps the older Nord design in `sass/_variables.scss`. `PRODUCT.md` holds the audiences and the brand commitments.

The design came from a prototype round in October 2026. The prototype branch `feat/viacara-founder-page-prototypes` keeps the variants that Kyle compared. Kyle chose variant F: one full curtain, pink to grey.

## Page structure

1. **Hero.** Kyle's name as a large white wordmark. The cut-out portrait stands in front of the name. The pink linen curtain fills the background.
2. **Letter.** A light card that overlaps the hero. It holds the founder's letter, the film, the join action and the transcript.
3. **Curtain run.** The curtain continues behind the letter. It fades from pink to grey and then runs into the laptop photograph with no visible join.
4. **Engineering.** The laptop photograph, then "Hiring a product engineer?", the engineering record and two testimonials on a soft floor haze.
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
- In the wordmark, the arm of the ribbon "r" runs level through the "t" stem and becomes its crossbar. The crossbar sits at the height of the arm, a little below the x-height. Keep this join in all three wordmark files. After an edit, change the `?v=` value on the wordmark images, because `/brand/*` is cached as immutable.
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
- The letter overlaps the hero by `clamp(6rem, 13vw, 12rem)` (4rem on phones). The cut-out stays solid down to the top of the letter; its fade sits inside the overlap, so the body never fades over the curtain.
- Buttons never wrap. `.f-pill` uses `white-space: nowrap`, and a label stays short enough to fit a 360 px phone ("Join ViaCara", "Email kyle.welsworth@pm.me").
- The letterhead holds the name and role only. The engineering section follows the letter, so it needs no jump link. The letter names `hello@viacara.com` for ViaCara questions; the engineering section names Kyle's own email.
- The ring around "first two" is ViaCara's `circle-05`, mirrored, with its specks removed (`circle-05-mirrored.svg`). A pixel test against the Urbanist glyphs set its size: it keeps 0.07em clear of "first two" and stays clear of the lines above and below. Its side margins are wider than its overshoot, so it does not touch the words beside it. Measure again if the words or the type change.

## Motion

- The name rises in once on load.
- With scroll-driven animation support, the name drifts down 26vh over the first screen. This is CSS only.
- `prefers-reduced-motion: reduce` turns all motion off.

## Performance

- The homepage loads `founder.css` only. The privacy page loads `style.css`.
- The cut-out is the LCP image with `fetchpriority="high"`. Photographs below the fold load lazily.
- Backgrounds use `image-set()`: the 1680 file at 1x and the 3360 file at 2x. Phones up to 720 px wide take the 1680 file up to 2x and the 3360 file at 3x, because the backgrounds there are about 1735 device pixels wide at 2x. Images use `srcset` and `sizes`.
- The film loads only when someone presses play (`preload="none"`). It comes from `assets.viacara.com`, which the CSP allows in `media-src`. The poster is a lazy `<img>`, not the `poster` attribute, so it does not compete with the hero.

## Social cards

`scripts/social-card/card.html` is the template for the Open Graph card (1200x630) and the Twitter card (1200x600). `scripts/capture-social-images.sh` renders it with Chrome into `static/images/`. The template uses the site's own files: the pink linen tile, the cut-out, the split white wordmark, the ViaCara lockup and the hand-drawn underline.

- **Layout:** the name in two lines at the top left, the cut-out at the right with the face at thumbnail size, and a sky letterhead at the bottom left. The letterhead reads "Founder of ViaCara", then "Software engineer since 1999" and `mekyle.com`.
- **Name contrast:** a soft plum ellipse (`rgba(46, 16, 30, 0.56)` at the centre) sits behind the white name. The curtain folds are bright, so the name needs it. The ellipse stays below the cut-out and the letterhead.
- **Small sizes:** a feed shows the card at about 550 px wide. Keep the name and the letterhead text at their sizes, and test a change at that width.
- **X label:** X puts the domain over the bottom-left corner of the image. On the 600 px card, the letterhead sits 68 px from the bottom so that the label does not cover it.
- **ViaCara lockup:** it stays blue on the sky letterhead, with clear space on each side. Do not recolour it for the curtain.
- **Cache:** `/images/*` is cached as immutable. Change the `?v=` value on `og:image` and `twitter:image` in `templates/base.html` when you render new cards.
