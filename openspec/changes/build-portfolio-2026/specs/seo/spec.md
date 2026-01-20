## ✨ ADDED Requirements

### 🏷️ Requirement: Meta Tags

The site SHALL include the following meta tags:
- `<title>` under 60 characters
- `<meta name="description">` under 155 characters
- `<meta name="keywords">` with relevant terms
- `<meta name="author">` set to "Kyle Welsby"
- `<link rel="canonical">` pointing to https://mekyle.com/

#### ✅ Scenario: Title is optimised
- **WHEN** the page is indexed
- **THEN** the title is "Kyle Welsby | Staff Software Engineer | AI & Fintech Systems"
- **AND** it is under 60 characters

#### ✅ Scenario: Description is optimised
- **WHEN** search results display the page
- **THEN** the description summarises expertise and location
- **AND** it is under 155 characters

### 📱 Requirement: Open Graph Tags

The site SHALL include Open Graph tags for social sharing:
- `og:type`: "profile"
- `og:title`: Name and role
- `og:description`: Brief summary
- `og:url`: Canonical URL
- `og:image`: OG image URL (1200x630)
- `og:image:width`: 1200
- `og:image:height`: 630
- `og:locale`: "en_GB"
- `profile:first_name`: "Kyle"
- `profile:last_name`: "Welsby"

#### ✅ Scenario: Social preview displays correctly
- **WHEN** the URL is shared on LinkedIn or Twitter
- **THEN** the preview shows the OG image
- **AND** title and description are displayed

### 🐦 Requirement: Twitter Card Tags

The site SHALL include Twitter Card meta tags:
- `twitter:card`: "summary_large_image"
- `twitter:site`: "@halfcube"
- `twitter:title`: Name and role
- `twitter:description`: Brief summary
- `twitter:image`: OG image URL

#### ✅ Scenario: Twitter preview displays correctly
- **WHEN** the URL is shared on Twitter/X
- **THEN** a large image card is displayed
- **AND** title and description are shown

### 📊 Requirement: JSON-LD Structured Data

The site SHALL include JSON-LD structured data with:
- `@type`: "ProfilePage" wrapper
- `mainEntity` of `@type`: "Person"
- Properties: name, jobTitle, description, url, email, telephone, image
- `sameAs` array with social profile URLs
- `knowsAbout` array with technical skills
- `workLocation` with current location
- `alumniOf` with previous employers

#### ✅ Scenario: Schema validates
- **WHEN** structured data is tested with Google's Rich Results Test
- **THEN** no errors are reported
- **AND** Person entity is recognized

### 🤖 Requirement: Robots.txt

The site SHALL include a robots.txt file that:
- Allows all crawlers
- References sitemap.xml
- Does not block any content

#### ✅ Scenario: Crawlers can access all content
- **WHEN** a search engine crawler visits
- **THEN** robots.txt permits full crawling
- **AND** sitemap location is provided

### 🖼️ Requirement: OG Image

The site SHALL include a social sharing image:
- Dimensions: 1200x630 pixels
- Format: JPG
- Design: Nordic theme with name prominent
- Located at `/images/og.jpg`

#### ✅ Scenario: OG image loads
- **WHEN** social platforms request the OG image
- **THEN** a valid image is returned
- **AND** dimensions match OG tag specifications
