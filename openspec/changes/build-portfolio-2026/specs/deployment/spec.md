## ✨ ADDED Requirements

### ☁️ Requirement: Cloudflare Pages Hosting

The site SHALL be deployed to Cloudflare Pages:
- Production branch: `main`
- Build command: `zola build`
- Build output directory: `public`
- Environment variable: `ZOLA_VERSION=0.19.2`

#### ✅ Scenario: Build succeeds on Cloudflare
- **WHEN** code is pushed to main branch
- **THEN** Cloudflare Pages triggers a build
- **AND** the site is deployed to production

#### ✅ Scenario: Preview deployments work
- **WHEN** a pull request is opened
- **THEN** a preview deployment is created
- **AND** the preview URL is available for testing

### 🌐 Requirement: Custom Domain

The site SHALL be served from the custom domain:
- Primary domain: `mekyle.com`
- SSL: Automatic via Cloudflare (Full Strict mode) 🔒
- DNS: Managed through Cloudflare

#### ✅ Scenario: Domain resolves correctly
- **WHEN** https://mekyle.com is requested
- **THEN** the site is served
- **AND** HTTPS is enforced

### ↪️ Requirement: WWW Redirect

The site SHALL redirect www subdomain to apex domain:
- `https://www.mekyle.com/*` redirects to `https://mekyle.com/*`
- Redirect type: 301 (permanent)
- Path is preserved

#### ✅ Scenario: WWW redirects to apex
- **WHEN** https://www.mekyle.com/about is requested
- **THEN** a 301 redirect is returned
- **AND** the redirect target is https://mekyle.com/about

### 💾 Requirement: Cache Headers

The site SHALL configure cache headers via `_headers` file:

**Security headers (all paths)** 🔒:
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `X-XSS-Protection: 1; mode=block`
- `Referrer-Policy: strict-origin-when-cross-origin`

**Static assets (css, js, images)** 📦:
- `Cache-Control: public, max-age=31536000, immutable`

**HTML pages** 📄:
- `Cache-Control: public, max-age=0, must-revalidate`

**llms.txt** 🤖:
- `Cache-Control: public, max-age=86400`

#### ✅ Scenario: Static assets are cached long-term
- **WHEN** a CSS file is requested
- **THEN** Cache-Control header includes immutable
- **AND** max-age is 1 year

#### ✅ Scenario: HTML is revalidated
- **WHEN** HTML is requested
- **THEN** Cache-Control requires revalidation
- **AND** browsers check for updates on each visit

### 🔒 Requirement: Security Headers

The site SHALL include security headers on all responses:
- `X-Content-Type-Options: nosniff`
- `X-Frame-Options: DENY`
- `Referrer-Policy: strict-origin-when-cross-origin`

#### ✅ Scenario: Security headers are present
- **WHEN** any page is requested
- **THEN** security headers are included in the response
- **AND** clickjacking and MIME-sniffing are prevented
