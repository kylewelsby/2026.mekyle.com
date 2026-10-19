# founder-homepage Specification

## Purpose
The mekyle.com homepage presents Kyle as the founder of ViaCara first, with the founder film and letter, and keeps his engineering record and contact details one scroll away for clients who hire product engineers.

## Requirements

### Requirement: Founder-first homepage

The homepage SHALL present Kyle as the founder of ViaCara first, with his engineering record one scroll away.

#### Scenario: Visitor lands on the homepage
- **WHEN** a visitor opens https://mekyle.com/
- **THEN** the first screen shows Kyle's name and his portrait on the linen curtain
- **AND** the founder's letter overlaps the bottom of the hero

#### Scenario: Hiring visitor looks for the record
- **WHEN** a visitor reads past the letter
- **THEN** the engineering section "Hiring a product engineer?" shows the engineering record, two testimonials and the contact email

#### Scenario: Phone visitor sees the buttons
- **WHEN** the page renders 360 px wide or more
- **THEN** every button label stays on one line

### Requirement: Founder film

The letter SHALL offer the ViaCara founder film with captions, an AI illustration label and a text transcript.

#### Scenario: Visitor plays the film
- **WHEN** a visitor presses "Play the film"
- **THEN** the film plays from `assets.viacara.com` with native controls
- **AND** the Content Security Policy allows the film in `media-src`

#### Scenario: Visitor cannot play video
- **WHEN** a visitor opens "Film transcript"
- **THEN** the full transcript shows as text

### Requirement: Continuous curtain imagery

The curtain SHALL run from the hero to the laptop photograph with no visible seam, kink or band, at 1x and 2x pixel density.

#### Scenario: High-density desktop screen
- **WHEN** the page renders wider than 720 px at a device pixel ratio of 2
- **THEN** the curtain tiles, photographs and floor haze load their 3360 px files

#### Scenario: Phone screen
- **WHEN** the page renders 720 px wide or less
- **THEN** the backgrounds load the 1680 px files up to a device pixel ratio of 2 and the 3360 px files at 3

#### Scenario: Curtain meets the photograph
- **WHEN** the visitor scrolls to the end of the letter
- **THEN** the grey curtain continues into row 0 of the laptop photograph with no visible join

### Requirement: Content parity for AI readers

`static/llms.txt` SHALL match the professional content on the homepage.

#### Scenario: Positioning changes
- **WHEN** the homepage positioning, record or contact details change
- **THEN** `static/llms.txt` changes in the same pull request

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
