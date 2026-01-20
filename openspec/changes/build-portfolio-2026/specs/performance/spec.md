## ✨ ADDED Requirements

### 💯 Requirement: Lighthouse Scores

The site SHALL achieve 100/100 on all Lighthouse categories:
- ⚡ Performance: 100
- ♿ Accessibility: 100
- ✅ Best Practices: 100
- 🔍 SEO: 100

#### ✅ Scenario: Lighthouse audit passes
- **WHEN** Lighthouse audit is run in Chrome DevTools
- **THEN** all four categories score 100
- **AND** no failing audits are reported

### 📊 Requirement: Core Web Vitals

The site SHALL meet or exceed Core Web Vitals targets:
- 🖼️ Largest Contentful Paint (LCP): < 1.5s
- 📐 Cumulative Layout Shift (CLS): 0
- ⏱️ Time to Interactive (TTI): < 2s
- 🎨 First Contentful Paint (FCP): < 1s on 3G

#### ✅ Scenario: LCP is fast
- **WHEN** the hero image loads
- **THEN** LCP is under 1.5 seconds
- **AND** the image is prioritised with fetchpriority="high"

#### ✅ Scenario: No layout shift
- **WHEN** the page renders
- **THEN** CLS is 0
- **AND** all images have explicit width and height

### 🎨 Requirement: Critical CSS Inlining

The site SHALL inline critical CSS in the `<head>`:
- Critical styles under 14KB compressed
- Includes: reset, body, hero, typography, links, above-fold skills
- Full stylesheet loaded asynchronously

#### ✅ Scenario: First paint is fast
- **WHEN** the page begins loading
- **THEN** critical CSS is immediately available
- **AND** no external CSS request blocks rendering

### 🖼️ Requirement: Asset Optimisation

The site SHALL optimise all assets:
- Images: AVIF primary, WebP/JPG fallback
- Responsive images with srcset
- Lazy loading for non-hero images
- HTML minification enabled
- CSS minification via Sass

#### ✅ Scenario: Images use modern formats
- **WHEN** an image is requested
- **THEN** AVIF is served to supported browsers
- **AND** fallback formats are available

### ⚖️ Requirement: Page Weight

The total page weight SHALL be under 500KB:
- 📄 HTML: under 20KB
- 🎨 CSS: under 15KB
- 🖼️ Images: under 400KB (hero + OG)
- 💻 JavaScript: under 1KB (console greeting only)

#### ✅ Scenario: Page is lightweight
- **WHEN** all resources are loaded
- **THEN** total transfer size is under 500KB
- **AND** no unnecessary resources are loaded

### 🚫 Requirement: No Render-blocking Resources

The site SHALL have no render-blocking resources:
- No external JavaScript (except async Plausible)
- Critical CSS inlined
- Full CSS loaded with `media="print" onload` pattern or similar

#### ✅ Scenario: Render is not blocked
- **WHEN** the browser parses the HTML
- **THEN** no requests block initial render
- **AND** content is visible before external resources load

### 💾 Requirement: Caching Headers

The site SHALL configure optimal cache headers:
- 📄 HTML: `max-age=0, must-revalidate`
- 🎨 CSS/JS: `max-age=31536000, immutable`
- 🖼️ Images: `max-age=31536000, immutable`
- 🤖 llms.txt: `max-age=86400`

#### ✅ Scenario: Static assets are cached
- **WHEN** a returning visitor loads the page
- **THEN** cached assets are used
- **AND** only HTML is re-validated
