## ✨ ADDED Requirements

### ♿ Requirement: WCAG 2.1 AA Compliance

The site SHALL comply with WCAG 2.1 Level AA:
- All colour contrast ratios meet minimum requirements
- All interactive elements are keyboard accessible
- All images have appropriate alt text
- Semantic HTML is used throughout

#### ✅ Scenario: Colour contrast passes
- **WHEN** contrast ratios are measured
- **THEN** body text (#D8DEE9 on #2E3440) has 9.4:1 ratio (AAA) ✅
- **AND** links (#88C0D0 on #2E3440) have 7.2:1 ratio (AAA) ✅

### ⌨️ Requirement: Keyboard Navigation

The site SHALL be fully navigable with keyboard only:
- All interactive elements are focusable
- Tab order follows logical reading order
- Focus indicators are clearly visible
- Skip-to-content link is first focusable element

#### ✅ Scenario: Tab navigation works
- **WHEN** a user presses Tab repeatedly
- **THEN** focus moves through all interactive elements
- **AND** focus order matches visual layout

#### ✅ Scenario: Skip link is available
- **WHEN** keyboard user first tabs into the page
- **THEN** a "Skip to content" link is focused first
- **AND** activating it skips to main content

### 🎯 Requirement: Focus Indicators

The site SHALL display visible focus indicators:
- 2px solid outline using `--nord8` colour
- 2px outline offset for visibility
- `:focus-visible` used to show focus only for keyboard users

#### ✅ Scenario: Focus is visible
- **WHEN** an element receives keyboard focus
- **THEN** a frost blue outline is displayed
- **AND** the outline is visible against all backgrounds

### 🔊 Requirement: Screen Reader Support

The site SHALL support screen readers:
- Semantic HTML elements (header, main, nav, section, footer)
- ARIA labels where semantic HTML is insufficient
- Descriptive alt text on all images
- Decorative elements marked with `aria-hidden="true"`

#### ✅ Scenario: Screen reader announces content
- **WHEN** VoiceOver navigates the page
- **THEN** all content is announced
- **AND** landmarks are identified correctly

#### ✅ Scenario: Decorative elements are hidden
- **WHEN** skills scroll background is encountered
- **THEN** it is not announced (aria-hidden="true")
- **AND** it does not interfere with content reading

### 🎬 Requirement: Reduced Motion Support

The site SHALL respect user preferences for reduced motion:
- `@media (prefers-reduced-motion: reduce)` disables animations
- Skills scroll animation stops
- No auto-playing video or audio

#### ✅ Scenario: Animations respect preferences
- **WHEN** user has enabled reduced motion
- **THEN** all CSS animations are disabled or paused
- **AND** content remains fully accessible

### 🖼️ Requirement: Alt Text

All images SHALL have appropriate alt text:
- Hero portrait: "Kyle Welsby"
- Decorative images: empty alt="" or aria-hidden
- Icons: aria-label on parent link

#### ✅ Scenario: Portrait has alt text
- **WHEN** the hero image is encountered
- **THEN** alt text "Kyle Welsby" is provided
- **AND** screen readers announce the image appropriately
