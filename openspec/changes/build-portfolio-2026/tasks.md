# 📋 Tasks: mekyle.com 2026 Rebuild

## 🏗️ Phase 1: Project Setup

- [x] **1.1** Create new repository `2026.mekyle.com`
- [x] **1.2** Initialise Zola project with `zola init`
- [x] **1.3** Configure `config.toml` (base URL, Sass, HTML minification, markdown settings)
- [x] **1.4** Set up directory structure per spec
- [ ] **1.5** Add `claude.md` to repository root
- [x] **1.6** Configure `.gitignore` (public/, .DS_Store, etc.)

## 🧱 Phase 2: Base Templates & Styling

- [x] **2.1** Create `templates/base.html` with HTML5 doctype, meta tags, critical CSS, JSON-LD
- [x] **2.2** Create `templates/index.html` (homepage)
- [x] **2.3** Create `templates/page.html` (generic pages)
- [x] **2.4** Set up Sass architecture (_variables, _reset, _base, _skills-scroll, _hero, _layout, style.scss)

## 🎨 Phase 3: Nord Theme Implementation

- [x] **3.1** Define CSS custom properties for Nord palette
- [x] **3.2** Set up system font stack (no web fonts)
- [x] **3.3** Style typography hierarchy (h1-h6, body, code)
- [x] **3.4** Style links with frost blue accent (`#88C0D0`)
- [x] **3.5** Create focus states for accessibility
- [ ] **3.6** Test colour contrast ratios (WCAG AA minimum)

## 📜 Phase 4: Scrolling Skills Background

- [x] **4.1** Create skills list data (TOML or inline)
- [x] **4.2** Implement CSS keyframe animation for horizontal scroll
- [x] **4.3** Create multiple rows with varied speeds/directions
- [x] **4.4** Add subtle opacity for depth effect (0.1-0.15)
- [x] **4.5** Ensure animation respects `prefers-reduced-motion`
- [ ] **4.6** Test performance impact (should not affect LCP)

## 🖼️ Phase 5: Hero Section

- [ ] **5.1** Prepare hero portrait image (WebP, AVIF, responsive srcset)
- [x] **5.2** Implement pop-out CSS effect (clip-path or layered z-index)
- [x] **5.3** Add positioning statement text
- [x] **5.4** Style call-to-action links (LinkedIn, GitHub, Email)
- [ ] **5.5** Test on mobile (may need simplified version)

## 📝 Phase 6: Content Sections

- [x] **6.1** Write positioning statement (1-2 sentences)
- [x] **6.2** Compile 4-6 quantified accomplishments
- [x] **6.3** Create About section content
- [x] **6.4** Create Hobbies/Interests section (Zouk, DJing)
- [x] **6.5** Create contact links section (no form)

## 🔍 Phase 7: SEO & Structured Data

- [x] **7.1** Write meta title (under 60 chars)
- [x] **7.2** Write meta description (under 155 chars)
- [x] **7.3** Implement JSON-LD Person schema
- [x] **7.4** Implement JSON-LD ProfilePage schema
- [x] **7.5** Add Open Graph tags for social sharing
- [x] **7.6** Add Twitter Card tags
- [ ] **7.7** Create OG image (1200x630, Nordic theme)
- [x] **7.8** Add canonical URL
- [x] **7.9** Create `robots.txt`

## 🎁 Phase 8: Easter Eggs

- [x] **8.1** Write `llms.txt` content with AI greeting injection
- [ ] **8.2** Test llms.txt with Claude/ChatGPT
- [x] **8.3** Implement console greeting (styled console.log)
- [ ] **8.4** (Optional) Add `humans.txt`
- [ ] **8.5** (Optional) Implement Konami code Easter egg

## ⚡ Phase 9: Performance Optimisation

- [ ] **9.1** Identify and inline critical CSS (< 14KB gzipped)
- [ ] **9.2** Async load full stylesheet
- [x] **9.3** Add `fetchpriority="high"` to hero image
- [ ] **9.4** Add `loading="lazy"` to non-hero images
- [x] **9.5** Add explicit width/height to all images
- [x] **9.6** Configure cache headers (`_headers` file)
- [ ] **9.7** Run Lighthouse audit - target 100/100
- [ ] **9.8** Test on WebPageTest and slow 3G

## ♿ Phase 10: Accessibility

- [x] **10.1** Add skip-to-content link
- [x] **10.2** Ensure all images have descriptive alt text
- [x] **10.3** Check heading hierarchy (single h1, logical h2-h6)
- [ ] **10.4** Test keyboard navigation
- [ ] **10.5** Test with screen reader (VoiceOver)
- [x] **10.6** Verify focus indicators are visible
- [x] **10.7** Check `prefers-reduced-motion` is respected
- [ ] **10.8** Run axe DevTools audit

## ☁️ Phase 11: Deployment

- [ ] **11.1** Create Cloudflare Pages project
- [ ] **11.2** Connect GitHub repository
- [ ] **11.3** Configure build settings (zola build, ZOLA_VERSION=0.19.2)
- [ ] **11.4** Configure custom domain `mekyle.com`
- [ ] **11.5** Set up redirects (www to apex)
- [ ] **11.6** Test deployment preview
- [ ] **11.7** Deploy to production

## ✅ Phase 12: Final Review

- [ ] **12.1** Cross-browser testing (Chrome, Firefox, Safari, Edge)
- [ ] **12.2** Mobile testing (iOS Safari, Android Chrome)
- [ ] **12.3** Final Lighthouse audit - confirm 100/100
- [ ] **12.4** Spell check all content
- [ ] **12.5** Verify all links work
- [ ] **12.6** Test llms.txt with multiple AI assistants
- [ ] **12.7** Archive 2021 repository
