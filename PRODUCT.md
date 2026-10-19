# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Inferred from Kyle's brief of 19 October 2026 and the ViaCara repository. Kyle has not confirmed the order.

1. People who meet Kyle through ViaCara: independent therapists, counsellors, coaches and hypnotherapists who saw the founder film on LinkedIn or on viacara.com, plus partners and possible investors. They want to know who the founder is and whether to trust him.
2. Hiring managers, recruiters and engineering leaders. They want proof of Staff or Principal level judgement, the work history, and how to reach Kyle for a contract or a permanent role.
3. Peers and the open-source community, who arrive from GitHub or talks.

## Product Purpose

mekyle.com is Kyle Welsworth's personal site. It leads with Kyle as the founder of ViaCara and features his founder film. It also keeps his engineering record visible, because Kyle may take contract or permanent work while ViaCara grows.

Success: a ViaCara visitor watches the film and goes to the practitioner waitlist. A hiring visitor finds the record and contacts Kyle in under a minute.

## Positioning

An engineer since 1999 who builds platforms where correctness, regulation and cost matter, and who now applies that to ViaCara. The founder story and the engineering record support each other: the history is why the founder is credible, and the founder work is current proof of the engineer.

## Capabilities and Constraints

- Zola static site on Cloudflare Pages. Target: 100/100 Lighthouse.
- Minimal JavaScript. No forms. Contact is by links only.
- Analytics: Plausible only.
- The repository is public. Personal photographs stay out of commits until they ship.
- `static/llms.txt` must match the visible professional content.

## Brand Commitments

- Writing: British English, no em dashes, no Oxford comma, facts over superlatives.
- ViaCara wording, from the ViaCara repository (`docs/brand/founder-voice.md`, `docs/brand/editorial-standard.md`), applies when Kyle writes about ViaCara: say "introduce", "connect" or "find", never "match"; do not write "AI-powered"; make no health claims; do not imply that ViaCara is live; give no launch date; keep the label "The illustrations in this film were made with AI." beside the film.
- ViaCara brand assets (Urbanist, the logo lockups, the colour names) belong to ViaCara Ltd. Use the logo by its rules: clear space, no recolouring.
- Easter eggs in `CLAUDE.md` (the llms.txt greeting, the console greeting) stay.

## Evidence on Hand

- Founder film v8, 97 s, hosted at `https://assets.viacara.com/video/founder-film-1080p.cabb65f5566feaa0.mp4`, with burned-in captions and a VTT.
- Professional portraits by Fiona Finchett, September 2026, kept outside this repository. Credit "Photo: Fiona Finchett".
- Impact narratives, experience, colleague testimonials and talks in `content/_index.md`.
- Absent: a ViaCara launch date, ViaCara customer numbers, ViaCara testimonials. Do not invent them.

## Product Principles

- Founder first, engineer always: ViaCara leads, and the record is never more than one scroll away.
- Prove with real material: the film, the photos and the named outcomes. Do not use adjectives as proof.
- One clear action for each visitor: the waitlist for practitioners, a direct email for hiring.
- Honest status: say what is true today about ViaCara and about Kyle's availability.

## Accessibility & Inclusion

- WCAG 2.2 AA contrast. Keyboard focus is visible.
- The film has a caption track and a text transcript on the page.
- Respect `prefers-reduced-motion`.
