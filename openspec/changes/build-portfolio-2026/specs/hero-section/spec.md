## ✨ ADDED Requirements

### 🖼️ Requirement: Hero Layout

The hero section SHALL display:
1. 📸 Portrait image positioned to appear as if bursting through a horizontal divider
2. 👤 Name heading (Kyle Welsby)
3. 💼 Title (Staff / Principal Software Engineer)
4. 📝 Positioning statement (1-2 sentences)
5. 🔗 Call-to-action links (LinkedIn, GitHub, Email)

#### 🖥️ Scenario: Hero renders on desktop
- **WHEN** the homepage is viewed on desktop
- **THEN** the portrait is centred with pop-out effect
- **AND** the name and title are prominently displayed
- **AND** social links are horizontally arranged

#### 📱 Scenario: Hero renders on mobile
- **WHEN** the homepage is viewed on mobile
- **THEN** the layout adapts for smaller screens
- **AND** all content remains visible and readable

### ✨ Requirement: Portrait Pop-out Effect

The hero portrait SHALL create a visual effect of the image bursting through a horizontal divider line using layered z-index positioning:
- Skills scroll background: z-index -1
- Hero content area: z-index 1
- Horizontal divider: z-index 5
- Portrait image: z-index 10 (overlapping the divider)

#### ✅ Scenario: Pop-out effect displays correctly
- **WHEN** the hero section is rendered
- **THEN** the portrait appears to break through the divider
- **AND** the effect is achieved with CSS only (no JavaScript)

#### ⚠️ Scenario: Effect degrades gracefully
- **WHEN** CSS features are unsupported
- **THEN** the portrait still displays
- **AND** the layout remains functional

### ⚡ Requirement: Hero Image Optimisation

The hero portrait SHALL be optimised for performance:
- Primary format: AVIF
- Fallback formats: WebP, JPG
- Responsive sizes: 400w, 800w, 1200w
- `fetchpriority="high"` attribute
- Explicit width and height attributes
- Alt text: "Kyle Welsby"

#### ✅ Scenario: Image loads efficiently
- **WHEN** the page loads
- **THEN** the browser selects the appropriate image format
- **AND** the image is prioritised for loading (LCP)
- **AND** no layout shift occurs (CLS = 0)

### 🔗 Requirement: Social Links

The hero SHALL include social links with:
- Inline SVG icons (no external icon fonts)
- Accessible labels (visible text or aria-label)
- Links: LinkedIn, GitHub, Email (mailto:)
- Hover state using frost blue accent

#### ♿ Scenario: Links are accessible
- **WHEN** a screen reader encounters the links
- **THEN** each link has an accessible name
- **AND** the purpose is clear

#### ✨ Scenario: Links have hover feedback
- **WHEN** a link is hovered
- **THEN** visual feedback is provided using `--nord8` accent colour
