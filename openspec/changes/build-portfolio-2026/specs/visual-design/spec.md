## ✨ ADDED Requirements

### 🎨 Requirement: Nord Colour Palette

The site SHALL use the Nord colour palette with CSS custom properties:

**Polar Night (backgrounds)** 🌙:
- `--nord0: #2E3440` (primary background)
- `--nord1: #3B4252` (elevated surfaces)
- `--nord2: #434C5E` (hover states)
- `--nord3: #4C566A` (borders, disabled)

**Snow Storm (text)** ❄️:
- `--nord4: #D8DEE9` (body text)
- `--nord5: #E5E9F0` (secondary headings)
- `--nord6: #ECEFF4` (primary headings)

**Frost (accents)** 🧊:
- `--nord8: #88C0D0` (primary accent, links)
- `--nord10: #5E81AC` (visited links)

#### ✅ Scenario: Colours are applied consistently
- **WHEN** the site is rendered
- **THEN** the background uses `--nord0`
- **AND** body text uses `--nord4`
- **AND** headings use `--nord6`
- **AND** links use `--nord8`

### 🔤 Requirement: System Font Stack

The site SHALL use system fonts with zero network requests:
```css
--font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI",
             Roboto, "Helvetica Neue", Arial, sans-serif;
--font-mono: ui-monospace, SFMono-Regular, "SF Mono",
             Menlo, Consolas, "Liberation Mono", monospace;
```

#### ✅ Scenario: No font files are loaded
- **WHEN** the site is loaded
- **THEN** no external font requests are made
- **AND** the operating system's native fonts are used

### 📐 Requirement: Typography Scale

The site SHALL use the following typography scale:

| Element | Size | Weight | Line Height |
|---------|------|--------|-------------|
| h1 | 3rem | 700 | 1.1 |
| h2 | 2rem | 600 | 1.2 |
| h3 | 1.5rem | 600 | 1.3 |
| body | 1.125rem | 400 | 1.6 |
| small | 0.875rem | 400 | 1.5 |

#### ✅ Scenario: Headings are styled correctly
- **WHEN** an h1 element is rendered
- **THEN** it uses 3rem font size
- **AND** 700 font weight
- **AND** 1.1 line height

### 📏 Requirement: Spacing System

The site SHALL use an 8px base unit spacing system:
- `--space-1`: 8px
- `--space-2`: 16px
- `--space-3`: 24px
- `--space-4`: 32px
- `--space-6`: 48px
- `--space-8`: 64px
- `--space-12`: 96px

#### ✅ Scenario: Spacing is consistent
- **WHEN** sections are rendered
- **THEN** spacing between sections uses `--space-8` (64px)
- **AND** component spacing uses `--space-4` (32px)

### 📱 Requirement: Responsive Breakpoints

The site SHALL use mobile-first responsive design with these breakpoints:
- `sm`: 640px (large phones)
- `md`: 768px (tablets)
- `lg`: 1024px (small laptops)
- `xl`: 1280px (desktops)

#### 📱 Scenario: Layout adapts to mobile
- **WHEN** viewport is below 640px
- **THEN** base mobile styles are applied
- **AND** content is single-column

#### 🖥️ Scenario: Layout adapts to desktop
- **WHEN** viewport is above 1024px
- **THEN** desktop-optimised layout is applied
- **AND** content width is constrained to readable measure
