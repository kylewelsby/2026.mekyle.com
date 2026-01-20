## 💡 Why

Kyle needs a modern portfolio website to position himself for Staff/Principal IC roles in AI Systems and Financial Platforms. The current 2021 Gridsome site is outdated and requires a rebuild using Zola for minimal maintenance and maximum performance.

## ✨ What Changes

- **NEW**: 🏗️ Zola-based static site with Nord dark theme
- **NEW**: 📜 Scrolling skills background animation (CSS-only)
- **NEW**: 🖼️ Hero section with portrait pop-out effect
- **NEW**: 🤖 llms.txt with AI-greeting Easter egg
- **NEW**: 💻 Console greeting for developers
- **NEW**: ⚡ 100/100 Lighthouse performance optimisation
- **NEW**: ♿ WCAG 2.1 AA accessibility compliance
- **NEW**: ☁️ Cloudflare Pages deployment with optimised caching
- **NEW**: 🔍 SEO with JSON-LD structured data (Person, ProfilePage)

## 🎯 Impact

- **Affected specs**: All new (greenfield project)
  - `site-structure` - Zola config, templates, directory layout
  - `visual-design` - Nord palette, typography, spacing
  - `hero-section` - Portrait pop-out effect
  - `skills-scroll` - Animated background
  - `content` - Homepage, accomplishments, links
  - `seo` - Meta tags, Open Graph, JSON-LD
  - `easter-eggs` - llms.txt, console greeting, humans.txt
  - `performance` - Critical CSS, caching, asset optimisation
  - `accessibility` - WCAG compliance, keyboard nav, screen readers
  - `deployment` - Cloudflare Pages, headers, redirects

- **Affected code**: Entirely new codebase in `2026.mekyle.com/` directory

## ✅ Success Criteria

| Metric | Target |
|--------|--------|
| Lighthouse Performance | 100 |
| Lighthouse Accessibility | 100 |
| Lighthouse Best Practices | 100 |
| Lighthouse SEO | 100 |
| Largest Contentful Paint | < 1.5s |
| Cumulative Layout Shift | 0 |
| Total page weight | < 500KB |

## 🚫 Out of Scope

- Blog functionality
- Contact forms
- User authentication
- Backend services
- Invasive analytics (Plausible included for privacy-respecting tracking)
