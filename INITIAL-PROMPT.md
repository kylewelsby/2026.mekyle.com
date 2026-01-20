# Building a high-performance portfolio for Staff/Principal Engineers

A Zola-based static site with Nordic dark theming can achieve **100/100 Lighthouse scores** while maintaining minimal maintenance overhead—the ideal setup for senior engineers who want professional presence without ongoing effort. The key combination: Zola's Rust-powered build speed, the Nord color palette's Arctic-inspired aesthetics, system fonts for zero font-loading delay, and strategic content positioning that emphasizes impact over exhaustive project lists.

This guide covers everything from technical implementation to content strategy, including the emerging **llms.txt convention** for making your portfolio AI-readable—a forward-thinking addition that positions you as technically current.

---

## Zola delivers fast builds with minimal complexity

**Zola v0.21.0** is a single-binary static site generator written in Rust, requiring no dependencies or package managers. Installation is straightforward across platforms: `brew install zola` on macOS, `winget install zola` on Windows, or `cargo install zola` from source.

### Project structure for a portfolio site

```
portfolio/
├── config.toml          # Site configuration
├── content/
│   ├── _index.md        # Homepage
│   ├── about.md
│   ├── projects/
│   │   ├── _index.md    # Projects listing
│   │   └── project-one/
│   │       ├── index.md # Co-located with images
│   │       └── screenshot.png
│   └── blog/
├── sass/
│   ├── style.scss       # Compiles to public/style.css
│   └── _variables.scss  # Partials (underscore prefix = not compiled standalone)
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── page.html
│   └── shortcodes/
└── static/              # Copied as-is to public/
```

### Tera templating essentials

Zola uses **Tera**, a Jinja2-inspired template engine. Template inheritance keeps your code DRY:

```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <title>{% block title %}{{ config.title }}{% endblock %}</title>
  <link rel="stylesheet" href="{{ get_url(path='style.css') }}">
</head>
<body>
  {% block content %}{% endblock %}
</body>
</html>

<!-- templates/page.html -->
{% extends "base.html" %}
{% block title %}{{ page.title }} | {{ config.title }}{% endblock %}
{% block content %}
<article>
  <h1>{{ page.title }}</h1>
  {{ page.content | safe }}
</article>
{% endblock %}
```

Key Zola-specific functions include `get_url()` for link generation, `resize_image()` for automatic image processing with WebP/AVIF output, and `load_data()` for external JSON/TOML files.

### Recommended config.toml for portfolios

```toml
base_url = "https://yourname.dev"
title = "Your Name | Staff Software Engineer"
compile_sass = true
minify_html = true
generate_feeds = true

[markdown]
external_links_target_blank = true
smart_punctuation = true
lazy_async_image = true  # Adds loading="lazy" to all images

[markdown.highlighting]
style = "class"
dark_theme = "dracula"
```

### Deployment recommendation: Cloudflare Pages

Among hosting options, **Cloudflare Pages offers unlimited bandwidth** on the free tier with excellent global edge performance—ideal for a portfolio. Configure with build command `zola build`, output directory `public`, and environment variable `ZOLA_VERSION=0.21.0`. Netlify provides easier setup with native Zola support via `netlify.toml`, while Vercel delivers the fastest build times.

---

## The llms.txt convention makes your site AI-readable

**llms.txt** is a markdown file at your site's root (e.g., `yourname.dev/llms.txt`) that provides curated, LLM-friendly content about you. Proposed by Jeremy Howard in September 2024, it addresses a critical limitation: AI assistants struggle to extract meaningful context from complex HTML pages with navigation, ads, and JavaScript.

### Why it matters for senior engineers

When recruiters or hiring managers paste your portfolio URL into ChatGPT or Claude to learn about you, llms.txt ensures the AI gets **accurate, structured information** rather than garbled HTML. While no major AI provider officially crawls llms.txt yet, the primary value is **user-initiated context provision**—making your professional information easy to share with AI assistants.

### Format specification

```markdown
# Your Name - Principal Software Engineer

> Principal Engineer with 12+ years building distributed systems, AI platforms,
> and regulated fintech infrastructure. Technical leader specializing in
> system design and cross-organizational influence.

Background in [domain], currently focused on [current focus].
Known for [distinctive approach or contribution].

## Professional Background
- [About Me](https://yourname.dev/about.md): Career journey and technical philosophy
- [Resume](https://yourname.dev/resume.md): Complete work history

## Featured Work
- [Distributed Cache System](https://yourname.dev/projects/cache.md): Built multi-region
  cache serving 2M QPS with 99.99% uptime
- [Platform Migration](https://yourname.dev/projects/migration.md): Led migration of
  200+ services to Kubernetes

## Technical Writing
- [Engineering Blog](https://yourname.dev/blog.md): Deep dives on distributed systems
- [Conference Talks](https://yourname.dev/talks.md): QCon, KubeCon presentations

## Optional
- [Contact](https://yourname.dev/contact.md): Professional inquiries
```

The **H1 title is the only required element**. The blockquote provides a summary, H2 sections organize links with descriptions, and the "Optional" section indicates content that can be skipped for shorter context windows. Consider also creating `llms-full.txt` with complete content for easy copying into AI conversations.

---

## Nordic dark palette creates distinctive, accessible design

The **Nord Theme** is the definitive Nordic-inspired color system, featuring 16 carefully selected colors organized into four palettes inspired by Arctic environments. These colors avoid pure black (`#000000`) which causes eye strain, instead using dark blue-grays that evoke frozen polar waters.

### Complete color system

| Purpose | Hex Code | CSS Variable |
|---------|----------|--------------|
| **Primary background** | `#2E3440` | `--bg-primary` |
| **Secondary background** | `#3B4252` | `--bg-secondary` |
| **Elevated surfaces** | `#434C5E` | `--bg-tertiary` |
| **Borders, subtle UI** | `#4C566A` | `--border-primary` |
| **Primary text** | `#ECEFF4` | `--text-primary` |
| **Body text** | `#D8DEE9` | `--text-secondary` |
| **Primary accent (links)** | `#88C0D0` | `--accent-primary` |
| **Secondary accent** | `#81A1C1` | `--accent-secondary` |
| **Success** | `#A3BE8C` | `--success` |
| **Warning** | `#EBCB8B` | `--warning` |
| **Error** | `#BF616A` | `--error` |

### Implementation as CSS custom properties

```css
:root {
  --bg-primary: #2E3440;
  --bg-secondary: #3B4252;
  --bg-tertiary: #434C5E;
  --text-primary: #ECEFF4;
  --text-secondary: #D8DEE9;
  --accent-primary: #88C0D0;
  --accent-secondary: #81A1C1;
  --border-primary: #4C566A;
  --success: #A3BE8C;
  --warning: #EBCB8B;
  --error: #BF616A;
}
```

### Typography that complements Nordic minimalism

For **maximum performance**, use a system font stack with zero network requests:

```css
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
               Roboto, "Helvetica Neue", Arial, sans-serif;
}

code {
  font-family: ui-monospace, SFMono-Regular, "SF Mono",
               Menlo, Consolas, monospace;
}
```

If custom fonts are essential, **Inter** for body text and **Montserrat** for headers align with Nordic functional aesthetics. Self-host using WOFF2 format with `font-display: swap` to prevent invisible text during loading.

### Scandinavian design principles for web

Nordic design emerged from regions with limited natural light, creating a philosophy of **functional minimalism**: every element serves a purpose, neutral foundations with strategic accent colors, and quality over quantity. Apply these by eliminating unnecessary UI elements, using whitespace generously, and restricting accent colors to interactive elements only.

---

## SEO positioning for Staff and Principal Engineer roles

Recruiters search by combining job titles with skills and location. Target these **primary keywords**: Staff Software Engineer, Principal Software Engineer, Technical Lead, IC Track Engineer. Combine with domain keywords: Distributed Systems, AI/ML Systems, Fintech Architecture, Platform Engineering, System Design.

### Meta tag template

```html
<title>Jane Doe | Principal Software Engineer | Distributed Systems & AI</title>
<meta name="description" content="Principal Software Engineer with 12+ years
  building distributed systems, AI platforms, and regulated fintech infrastructure.
  Expertise in technical leadership and scalable architecture.">
```

### JSON-LD structured data

Google specifically supports **ProfilePage** schema for personal sites. Combine it with **Person** schema for rich results:

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfilePage",
  "dateModified": "2026-01-15",
  "mainEntity": {
    "@type": "Person",
    "name": "Your Name",
    "jobTitle": "Principal Software Engineer",
    "description": "Principal Software Engineer with 12+ years...",
    "url": "https://yourname.dev",
    "sameAs": [
      "https://linkedin.com/in/yourname",
      "https://github.com/yourname"
    ],
    "knowsAbout": [
      "Distributed Systems", "AI Systems", "System Design",
      "Technical Leadership", "Fintech Architecture"
    ]
  }
}
</script>
```

### Open Graph for social sharing

```html
<meta property="og:type" content="profile">
<meta property="og:title" content="Jane Doe | Principal Software Engineer">
<meta property="og:image" content="https://yourname.dev/og-image.jpg">
<meta property="profile:first_name" content="Jane">
<meta property="profile:last_name" content="Doe">
```

Image should be **1200×630 pixels** for optimal display across platforms.

---

## Performance techniques for perfect Lighthouse scores

Static sites have inherent performance advantages—no server-side rendering, no database queries. With proper optimization, **100/100 scores are achievable** on all four Lighthouse categories.

### Core Web Vitals targets

| Metric | Target | How to achieve |
|--------|--------|----------------|
| **LCP** (Largest Contentful Paint) | ≤2.5s | Preload hero image, inline critical CSS |
| **INP** (Interaction to Next Paint) | ≤200ms | Minimize/eliminate JavaScript |
| **CLS** (Cumulative Layout Shift) | ≤0.1 | Set explicit image dimensions |

### Critical CSS inlining

Keep above-the-fold CSS **under 14KB compressed** (the maximum for first TCP roundtrip). Inline essential styles directly in the `<head>`, then load the full stylesheet asynchronously:

```html
<head>
  <style>
    /* Critical CSS only - ~3KB gzipped */
    :root { --bg: #2E3440; --text: #ECEFF4; }
    body { font-family: system-ui, sans-serif; margin: 0;
           background: var(--bg); color: var(--text); }
    .hero { min-height: 100vh; }
  </style>

  <link rel="preload" href="/style.css" as="style"
        onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link rel="stylesheet" href="/style.css"></noscript>
</head>
```

### Image optimization strategy

Use modern formats with fallbacks:

```html
<picture>
  <source srcset="/img/hero.avif" type="image/avif">
  <source srcset="/img/hero.webp" type="image/webp">
  <img src="/img/hero.jpg" alt="Description"
       width="1200" height="800" loading="lazy" decoding="async">
</picture>
```

**Critical rule**: Never lazy-load the LCP image (typically your hero image). Use `fetchpriority="high"` instead. AVIF achieves **50-80% compression** versus JPEG; WebP provides **25-34% savings** with 97%+ browser support.

### Minimal JavaScript approach

For a portfolio site, JavaScript is typically needed only for mobile navigation toggling. Use CSS-only alternatives where possible:

```html
<!-- CSS-only mobile nav -->
<input type="checkbox" id="nav-toggle" hidden>
<label for="nav-toggle" class="nav-button">☰</label>
<nav class="nav-menu">...</nav>

<style>
.nav-menu { display: none; }
#nav-toggle:checked ~ .nav-menu { display: block; }
</style>
```

**Zero JS = automatic 100% on Total Blocking Time metric.**

### Caching headers for Cloudflare/Netlify

```toml
# netlify.toml
[[headers]]
  for = "/*.css"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

[[headers]]
  for = "/*.html"
  [headers.values]
    Cache-Control = "public, max-age=0, must-revalidate"
```

Use content hashes in filenames (e.g., `main.abc123.css`) to enable immutable caching while ensuring updates propagate immediately.

---

## Portfolio strategy positions you for Staff+ opportunities

Senior IC portfolios serve fundamentally different purposes than junior developer showcases. Rather than proving basic competence, they function as **professional positioning tools** that communicate your unique value proposition and demonstrate thought leadership.

### The one-page portfolio concept

Chuck Groom recommends condensing your career into **4-6 bullet points** of highest-impact accomplishments with specific metrics. Include:

- Intended role and location
- Years of experience
- Short positioning statement
- **4-6 quantified accomplishments** (the core content)
- Brief personal interests (humanizes you)

**Exclude**: exhaustive skill lists (experienced readers find these unreliable), education (unless advanced degrees), and every project you've touched.

### Presenting work under NDA constraints

Focus on **process over product**: "How I approached designing a high-throughput data pipeline" rather than proprietary implementation details. Use percentages instead of absolute numbers ("12% conversion increase" not specific user counts). Consider password-protected detailed case studies shared directly with hiring managers, with public summaries indicating "detailed case study available upon request."

**Alternatives to NDA-restricted work**: open source contributions, side projects demonstrating similar capabilities, technical blog posts showing your thinking process, and redesign proposals for existing public products.

### Demonstrating technical leadership as an IC

Staff+ engineers influence without direct authority. Showcase **multiplier effects**:

- "Built internal tooling used by 200+ engineers"
- "Created design patterns adopted across 6 teams"
- "Authored technical documentation reducing onboarding time by 40%"

Use language that signals leadership scope: "Led technical direction for..." "Established engineering standards across..." "Partnered with Product leadership to..." These phrases distinguish Staff+ work from senior IC execution.

### Balancing accomplishments with humility

State facts, not superlatives. "Reduced API latency from 200ms to 50ms" beats "Brilliant optimization breakthrough." Acknowledge team contributions: "Led a team of 4 engineers to deliver..." Let impact metrics speak for themselves, and use testimonials for praise rather than self-assessment.

### Content that stays evergreen

Minimize maintenance by focusing on **timeless content**: foundational technical writing in your domain, how-to guides for problems that won't fundamentally change, career insights, and case study frameworks describing process rather than dated specifics. Annual review of bio and accomplishments is sufficient; avoid maintaining a blog you'll abandon.

---

## Putting it all together

For a Staff/Principal Engineer rebuilding their portfolio, the optimal stack combines **Zola** for fast, dependency-free builds; **Cloudflare Pages** for free unlimited bandwidth; the **Nord color palette** for distinctive, accessible dark theming; **system fonts** for instant text rendering; and **llms.txt** for AI-readability.

Structure content around **4-6 quantified accomplishments** rather than exhaustive project lists. Use JSON-LD structured data with Person and ProfilePage schemas for SEO. Inline critical CSS, optimize images to WebP/AVIF, and eliminate JavaScript where possible to achieve perfect Lighthouse scores.

The result: a professional, high-performance portfolio that positions you appropriately for Staff+ roles while requiring minimal ongoing maintenance—exactly what a senior engineer's personal site should be.
