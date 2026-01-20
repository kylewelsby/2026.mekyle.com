# Project Context

## Purpose
A high-performance portfolio site for Staff/Principal Engineers that achieves 100/100 Lighthouse scores while maintaining minimal maintenance overhead. The site emphasizes professional presence through impact-focused content rather than exhaustive project lists.

## Tech Stack
- **Zola v0.21.0** - Rust-powered static site generator (single binary, no dependencies)
- **Sass/SCSS** - Compiled by Zola
- **Tera** - Jinja2-inspired templating engine
- **Cloudflare Pages** - Deployment with unlimited free bandwidth

## Project Conventions

### Code Style
- Use CSS custom properties for theming (Nord color palette)
- System font stack for zero network requests
- Inline critical CSS (<14KB compressed)
- Minimize/eliminate JavaScript where possible

### Architecture Patterns
- Template inheritance via Tera (`base.html` → `page.html`)
- Co-located content with images in content directories
- SCSS partials prefixed with underscore (e.g., `_variables.scss`)
- Static assets copied as-is from `static/` directory

### Design System
Nord Theme color palette:
- Primary background: `#2E3440`
- Secondary background: `#3B4252`
- Elevated surfaces: `#434C5E`
- Borders: `#4C566A`
- Primary text: `#ECEFF4`
- Body text: `#D8DEE9`
- Primary accent (links): `#88C0D0`
- Secondary accent: `#81A1C1`
- Success: `#A3BE8C`
- Warning: `#EBCB8B`
- Error: `#BF616A`

### Performance Targets
- LCP (Largest Contentful Paint): ≤2.5s
- INP (Interaction to Next Paint): ≤200ms
- CLS (Cumulative Layout Shift): ≤0.1
- Goal: 100/100 on all Lighthouse categories

### Git Workflow
Standard feature branch workflow with descriptive commit messages.

## Domain Context
This is a Staff/Principal Engineer portfolio site. Content should:
- Focus on 4-6 quantified accomplishments with specific metrics
- Demonstrate multiplier effects and technical leadership
- Use language signaling leadership scope ("Led technical direction...", "Established standards across...")
- Balance accomplishments with humility (facts over superlatives)
- Handle NDA constraints by focusing on process over proprietary details

## Important Constraints
- No JavaScript unless absolutely necessary (CSS-only solutions preferred)
- Images must use modern formats (AVIF/WebP) with fallbacks
- Never lazy-load LCP (hero) images
- Critical CSS must be under 14KB compressed
- All images need explicit width/height to prevent CLS

## External Dependencies
- **Cloudflare Pages** - Hosting and CDN
- Build command: `zola build`
- Output directory: `public`
- Environment variable: `ZOLA_VERSION=0.21.0`

## Key Features
- **llms.txt** - AI-readable markdown file at site root for LLM context
- **JSON-LD** - ProfilePage and Person schemas for SEO
- **Open Graph** - Social sharing metadata (1200×630px images)
- **RSS/Atom feeds** - Via `generate_feeds = true` in config
