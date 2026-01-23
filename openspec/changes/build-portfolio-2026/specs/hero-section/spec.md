## 🔄 MODIFIED Requirements

### 🖼️ Requirement: Hero Layout

The hero section SHALL display:
1. 👤 Name heading (Kyle Welsby) - centred
2. 💼 Title (Staff Software Engineer) - centred, accent colour
3. 🌊 Dual oscillating waves at bottom (blue and coral)
4. 🔗 Network connector lines background with sparking dots

The hero SHALL NOT include:
- Portrait image (removed)
- Tagline text (removed)
- Social links (moved to footer)

#### 🖥️ Scenario: Hero renders on desktop
- **WHEN** the homepage is viewed on desktop
- **THEN** the name and title are prominently displayed and centred
- **AND** the waves animate smoothly at the bottom
- **AND** the network background is subtly visible

#### 📱 Scenario: Hero renders on mobile
- **WHEN** the homepage is viewed on mobile
- **THEN** the layout remains centred and readable
- **AND** the wave height scales down appropriately
- **AND** all content remains visible

## ✨ ADDED Requirements

### 🌊 Requirement: Oscillating Waves

The hero SHALL include dual animated waves:
- Blue wave: Nord10 (#5E81AC) at 50% opacity
- Coral wave: Nord12 (#D08770) at 40% opacity
- Waves positioned at bottom of hero section
- Waves oscillate in opposite directions (creates flowing effect)
- Animation duration: 10-13s ease-in-out infinite

#### ✅ Scenario: Waves animate correctly
- **WHEN** the hero section is rendered
- **THEN** the blue wave drifts left and right
- **AND** the coral wave drifts in the opposite direction
- **AND** the waves create a flowing, oscillating effect

#### ♿ Scenario: Reduced motion support
- **WHEN** user has prefers-reduced-motion enabled
- **THEN** wave animations are disabled
- **AND** waves display in static position

### 🔗 Requirement: Network Connector Background

The hero SHALL include a network pattern background:
- SVG pattern with dots and connector lines
- Frost blue colour (#88C0D0) at ~12% overall opacity
- Pattern repeats across full viewport
- 12 spark dots with staggered pulse animations
- Spark animation: scale up and glow effect

#### ✅ Scenario: Network pattern displays
- **WHEN** the page loads
- **THEN** the network pattern is visible behind all content
- **AND** the pattern tiles seamlessly
- **AND** spark dots pulse at random intervals

#### ⚡ Scenario: Performance is maintained
- **WHEN** animations are running
- **THEN** no layout shift occurs (CLS = 0)
- **AND** animations run on GPU (transform/opacity only)
- **AND** Lighthouse score remains 100/100

## ❌ REMOVED Requirements

### 🖼️ Requirement: Portrait Pop-out Effect
**Removed** - Portrait image and horizontal divider effect removed from hero.

### 📷 Requirement: Hero Image Optimisation
**Removed** - No hero image in new design.

### 🔗 Requirement: Hero Social Links
**Removed** - Social links moved to site footer.

### 📜 Requirement: Skills Scroll Background
**Removed** - Replaced by network connector background.
