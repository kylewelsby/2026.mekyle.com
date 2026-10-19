## ADDED Requirements

### Requirement: Founder-first homepage

The homepage SHALL present Kyle as the founder of ViaCara first, with his engineering record one scroll away.

#### Scenario: Visitor lands on the homepage
- **WHEN** a visitor opens https://mekyle.com/
- **THEN** the first screen shows Kyle's name and his portrait on the linen curtain
- **AND** the founder's letter overlaps the bottom of the hero

#### Scenario: Hiring visitor looks for the record
- **WHEN** a visitor selects "Hiring? See my engineering work"
- **THEN** the page moves to the engineering section with the engineering record, two testimonials and the contact email

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

The Open Graph and Twitter images SHALL show the current hero.

#### Scenario: Link shared on LinkedIn
- **WHEN** someone shares https://mekyle.com/
- **THEN** the preview shows the hero with the name Kyle Welsworth
