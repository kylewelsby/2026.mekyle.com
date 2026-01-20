## ✨ ADDED Requirements

### 📜 Requirement: Scrolling Skills Background

The site SHALL display a background layer with horizontally scrolling skill keywords:
- Fixed positioning covering the viewport
- Multiple rows scrolling in alternating directions
- Varied animation speeds for depth effect
- Subtle opacity (0.10-0.15) to avoid competing with content

#### ✅ Scenario: Animation runs smoothly
- **WHEN** the page is loaded
- **THEN** skill keywords scroll horizontally
- **AND** alternating rows scroll in opposite directions
- **AND** the animation loops seamlessly

#### ✅ Scenario: Animation does not block interaction
- **WHEN** the user interacts with the page
- **THEN** the skills background does not intercept clicks
- **AND** content remains fully interactive

### 📋 Requirement: Skills List Content

The skills background SHALL display the following keywords:
```
Ruby, Rails, Rust, Python, Go, TypeScript, PostgreSQL,
Redis, Kafka, Docker, Kubernetes, AWS, GCP,
Distributed Systems, State Machines, Event Sourcing,
API Design, Row Level Security, GDPR, PCI-DSS,
Claude, OpenAI, LangChain, AI Agents, RAG,
System Design, Technical Leadership, Architecture
```

#### ✅ Scenario: Skills are relevant
- **WHEN** the skills are displayed
- **THEN** they reflect Kyle's actual technical expertise
- **AND** they align with Staff/Principal positioning keywords

### 🎨 Requirement: CSS-only Animation

The scrolling animation SHALL be implemented using CSS keyframes only:
- No JavaScript animation
- GPU-accelerated transforms (translateX)
- Duplicated content for seamless looping
- Animation duration: 60-90s per cycle

#### ✅ Scenario: Animation uses CSS transforms
- **WHEN** the animation runs
- **THEN** only CSS `transform: translateX()` is used
- **AND** no JavaScript is executed

### ♿ Requirement: Reduced Motion Support

The animation SHALL respect user preferences for reduced motion:
- When `prefers-reduced-motion: reduce` is set, animation stops
- Static skills display is acceptable fallback

#### ✅ Scenario: Animation respects user preference
- **WHEN** user has enabled reduced motion
- **THEN** the scrolling animation is disabled
- **AND** skills are displayed statically

### ⚡ Requirement: Performance Impact

The skills animation SHALL have minimal performance impact:
- No effect on Largest Contentful Paint (LCP)
- No contribution to Cumulative Layout Shift (CLS)
- Smooth 60fps animation on mid-range devices

#### ✅ Scenario: Animation does not affect LCP
- **WHEN** Lighthouse measures LCP
- **THEN** the skills animation does not delay LCP
- **AND** Performance score remains 100
