## MODIFIED Requirements

### Requirement: Social cards

The Open Graph and Twitter images SHALL come from the card template in `scripts/social-card/card.html`. They SHALL show Kyle's name, his portrait, "Founder of ViaCara" and the site address, and SHALL stay readable at feed size.

#### Scenario: Link shared on LinkedIn
- **WHEN** someone shares https://mekyle.com/
- **THEN** the preview shows the name Kyle Welsworth, the portrait and "Founder of ViaCara"
- **AND** the image has a width, a height and alt text in its meta tags

#### Scenario: Link shared on X
- **WHEN** someone shares https://mekyle.com/ on X
- **THEN** the 1200x600 card shows the same content
- **AND** the domain label that X places at the bottom left does not cover the letterhead

#### Scenario: Card refreshed
- **WHEN** the card template or its assets change
- **THEN** `scripts/capture-social-images.sh` renders both images again
- **AND** the `?v=` values on `og:image` and `twitter:image` change in the same pull request
