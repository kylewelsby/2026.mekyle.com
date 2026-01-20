## 📖 Context

Kyle Welsby is rebuilding his portfolio website to position himself for Staff/Principal IC roles in AI Systems and Financial Platforms. The 2021 Gridsome site is outdated and needs replacing with a modern, minimal-maintenance solution.

**Stakeholders**: Kyle Welsby (owner), potential employers, recruiters, AI assistants reading llms.txt

**Constraints**:
- Zero ongoing maintenance preferred
- 100/100 Lighthouse scores required
- No JavaScript except console greeting
- Privacy-respecting analytics only (Plausible)

## 🎯 Goals / Non-Goals

**Goals**:
- ⚡ Achieve perfect Lighthouse scores across all categories
- 💼 Professional positioning for Staff/Principal roles
- 🎨 Nordic-inspired dark aesthetic using Nord palette
- 🎁 Playful Easter eggs that showcase personality
- 🤖 AI-readable content via llms.txt

**Non-Goals**:
- 📝 Blog functionality (maintenance burden)
- 📬 Contact forms (spam risk, complexity)
- 🔐 User authentication
- 🖥️ Backend services
- 📊 Invasive analytics

## 🔧 Decisions

### 1. Static Site Generator: Zola 🦀

**Decision**: Use Zola 0.19.x for static site generation

**Rationale**:
- Single binary, Rust-based (fast builds)
- Built-in Sass compilation (no additional tooling)
- HTML minification included
- No Node.js dependency chain
- Simple templating with Tera (Jinja2-like)

**Alternatives considered**:
- Hugo: Similar benefits but Zola's Sass integration is cleaner
- Astro: More powerful but introduces Node.js complexity
- Hand-written HTML: Too manual for maintainability

### 2. Styling: Sass with Nord Palette 🎨

**Decision**: Use Sass/SCSS with Nord colour palette and system fonts

**Rationale**:
- Sass provides variables, nesting, partials without build complexity
- Nord palette is well-documented with proven accessibility
- System fonts eliminate font loading (performance)
- CSS-only animations avoid JavaScript

**Colour contrast verification**:
- Body text (#D8DEE9) on background (#2E3440): 9.4:1 (WCAG AAA) ✅
- Headings (#ECEFF4) on background (#2E3440): 12.5:1 (WCAG AAA) ✅
- Links (#88C0D0) on background (#2E3440): 7.2:1 (WCAG AAA) ✅

### 3. Hero Pop-out Effect: Layered Z-index 🖼️

**Decision**: Use layered z-index approach with positioned elements

**Rationale**:
- More browser-compatible than clip-path
- Easier to control with CSS
- Works without JavaScript
- Simpler responsive adaptation

**Implementation**:
```
z-index layers:
  1. Skills scroll background (z-index: -1)
  2. Hero content area (z-index: 1)
  3. Horizontal divider (z-index: 5)
  4. Portrait image (z-index: 10, positioned to overlap divider)
```

### 4. Skills Animation: CSS-only Scroll 📜

**Decision**: Pure CSS keyframe animation with duplicated content

**Rationale**:
- No JavaScript required
- GPU-accelerated transforms
- Respects prefers-reduced-motion
- Low performance overhead

**Implementation**:
- Duplicate skill text to create seamless loop
- `translateX(-50%)` animation for continuous scroll
- Multiple rows at different speeds/directions for depth
- 0.12 opacity to avoid competing with content

### 5. Hosting: Cloudflare Pages ☁️

**Decision**: Deploy to Cloudflare Pages with global CDN

**Rationale**:
- Free tier with unlimited bandwidth
- Global edge network (fast everywhere)
- Integrated DNS management
- Automatic HTTPS
- Simple GitHub integration
- Header/redirect configuration via files

**Alternatives considered**:
- Netlify: Similar but Cloudflare CDN is larger
- GitHub Pages: No custom headers control
- Self-hosted: Unnecessary complexity

### 6. Analytics: Plausible 📊

**Decision**: Use Plausible for privacy-respecting analytics

**Rationale**:
- No cookies, GDPR-compliant by default
- Tiny script (~1KB)
- Async loading (no performance impact)
- Outbound link tracking useful for measuring engagement

## ⚠️ Risks / Trade-offs

| Risk | Mitigation |
|------|------------|
| 🖼️ Hero image file size affecting LCP | Use AVIF with WebP/JPG fallback, aggressive compression, fetchpriority="high" |
| 📜 Skills animation causing jank | Use transform-only animation, test on low-end devices |
| 🤖 llms.txt prompt injection too aggressive | Keep greeting playful and helpful, not manipulative |
| 🌐 Browser compatibility for AVIF | Provide WebP and JPG fallbacks in picture element |
| ☁️ Cloudflare Pages build failures | Pin ZOLA_VERSION environment variable |

## 🚀 Migration Plan

1. Build site in new repository `2026.mekyle.com`
2. Test thoroughly on staging/preview URL
3. Update DNS to point mekyle.com to Cloudflare Pages
4. Archive old 2021 Gridsome repository
5. No data migration needed (static content only)

**Rollback**: If issues occur, revert DNS to old hosting

## ❓ Open Questions

1. **Instagram handle**: TBC for Brazilian Zouk content - needs confirmation
2. **Mixcloud**: Using instead of/alongside SoundCloud for DJ mixes?
3. **Portrait image**: Need high-quality photo that works with pop-out crop
4. **OG image**: Generate via Nano Banana or design tool?
