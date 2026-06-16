---
name: MDB-SDG Dashboard
description: Research-grade interactive overview of MDB operations aligned to the 17 SDGs (2016–2025).
colors:
  hue-anchor: "264"
  bg: "oklch(97.5% 0.006 264)"
  surface: "oklch(100% 0 0)"
  surface-muted: "oklch(98.2% 0.004 264)"
  surface-hover: "oklch(98.8% 0.003 264)"
  ink: "oklch(21% 0.025 264)"
  ink-muted: "oklch(37% 0.022 264)"
  ink-subtle: "oklch(44.5% 0.024 264)"
  ink-hint: "oklch(48% 0.022 264)"
  accent: "oklch(48.5% 0.19 264)"
  accent-strong: "oklch(52% 0.2 264)"
  metric-amount: "oklch(52% 0.14 145)"
  border: "oklch(68% 0.02 264)"
  border-muted: "oklch(86% 0.008 264)"
  divider: "oklch(92% 0.006 264)"
  sidebar: "oklch(21% 0.025 264)"
  on-inverse: "oklch(100% 0 0)"
  on-sidebar: "oklch(98.5% 0.004 264)"
  error-bg: "oklch(96% 0.03 25)"
  error-ink: "oklch(40% 0.15 25)"
  error-border: "oklch(88% 0.06 25)"
  focus-map: "oklch(45% 0.1 175)"
typography:
  display:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, sans-serif"
    fontSize: "22px"
    fontWeight: 700
    lineHeight: 1.2
    letterSpacing: "normal"
  headline:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, sans-serif"
    fontSize: "20px"
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: "normal"
  title:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, sans-serif"
    fontSize: "18px"
    fontWeight: 700
    lineHeight: 1.25
    letterSpacing: "normal"
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.5
    letterSpacing: "normal"
  label:
    fontFamily: "-apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, sans-serif"
    fontSize: "13px"
    fontWeight: 600
    lineHeight: 1.25
    letterSpacing: "normal"
rounded:
  sm: "4px"
  md: "8px"
  lg: "12px"
  xl: "16px"
  pill: "999px"
  circle: "50%"
spacing:
  "1": "4px"
  "2": "8px"
  "3": "12px"
  "4": "16px"
  "5": "20px"
  "6": "24px"
  "8": "32px"
  "10": "40px"
  "12": "48px"
  "16": "64px"
components:
  nav-tab-active:
    backgroundColor: "rgba(37,99,235,0.12)"
    textColor: "{colors.accent}"
    typography: "{typography.title}"
    rounded: "6px"
    padding: "10px 20px"
  mdb-button:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-muted}"
    rounded: "{rounded.md}"
    padding: "0"
  mdb-button-selected:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-muted}"
    rounded: "{rounded.md}"
    padding: "0"
  chart-nav-tab-active:
    backgroundColor: "transparent"
    textColor: "{colors.accent}"
    typography: "{typography.label}"
    rounded: "0"
    padding: "12px 16px"
  chart-back-btn:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "8px 14px"
  chart-back-btn-hover:
    backgroundColor: "{colors.surface-hover}"
    textColor: "{colors.ink-muted}"
    typography: "{typography.label}"
    rounded: "{rounded.md}"
    padding: "8px 14px"
---

# Design System: MDB-SDG Dashboard

## 1. Overview

**Creative North Star: "The Research Console"**

This dashboard is built for researchers and policymakers at a desk—not a marketing site. The interface behaves like a familiar analyst workstation: top navigation for views, a persistent MDB filter sidebar, and chart stages that dominate the viewport. Chrome stays quiet so SDG data, maps, and co-occurrence matrices carry the visual weight.

The system rejects decorative dashboard theater. Surfaces are cool-tinted neutrals with a single violet-indigo accent for selection and focus. Typography is one system-ui stack at fixed rem sizes—no display pairing, no fluid hero headings. Density is intentional: chart titles, axis labels, filter controls, and legends coexist without breathing-room padding that would waste analyst screen space.

**Key Characteristics:**

- Data-first layout: charts and maps occupy 80%+ of attention; navigation and filters are structural, not decorative
- Restrained chrome: cool paper backgrounds, ink text, violet accent used only for active/selected states
- UN SDG palette is canonical for all goal-colored data visualization—UI accent never competes with SDG semantics
- Familiar analyst UX: top tabs, dark sidebar filter panel, underline chart sub-nav, pill metric toggles
- Fixed rem type scale (13–22px for UI; chart canvas labels at 12–14px)
- Tonal layering plus light structural shadows—never glassmorphism or gradient hero metrics

## 2. Colors

A cool violet-tinted neutral system with one saturated accent and a secondary green for amount metrics. SDG goal colors live exclusively in chart data—not in UI chrome.

### Primary

- **Deep Violet Indigo** (oklch(48.5% 0.19 264)): Primary accent for active nav tabs, selected MDB borders, chart sub-nav underlines, year-slider handles, and focus rings. Used sparingly—selection and state only.
- **Violet Indigo Strong** (oklch(52% 0.2 264)): Hover emphasis on slider handles, active year tick labels, and stronger focus outlines on map SDG logo selections.

### Secondary

- **Forest Ledger Green** (oklch(52% 0.14 145)): Secondary accent for amount-related metrics in the year-range slider gradient (paired with accent-strong). Distinguishes financial amount from project-count semantics without introducing a third UI accent elsewhere.

### Tertiary

- **Map Focus Teal** (oklch(45% 0.1 175)): Reserved for map-specific focus states where the default violet accent would clash with choropleth color scales.

### Neutral

- **Cool Analyst Paper** (oklch(97.5% 0.006 264)): Page background behind chart stages and content areas.
- **Pure Surface** (oklch(100% 0 0)): Cards, MDB buttons, nav bar, chart wrappers, and floating control pills.
- **Muted Surface** (oklch(98.2% 0.004 264)): Chart drawing areas, slider track backgrounds, and inner chart containers.
- **Inkwell** (oklch(21% 0.025 264)): Primary body text, chart titles, and sidebar panel background.
- **Ink Muted** (oklch(37% 0.022 264)): Secondary labels, back-button text, button label fallbacks.
- **Ink Subtle** (oklch(44.5% 0.024 264)): Inactive chart sub-nav tabs, metric switch labels, helper text.
- **Ink Hint** (oklch(48% 0.022 264)): Axis tick labels and tertiary metadata.
- **Structural Border** (oklch(68% 0.02 264)): Nav bar bottom rule (2px), emphasized borders on hover.
- **Quiet Border** (oklch(86% 0.008 264)): MDB button strokes, back-button borders, input-like controls.
- **Hairline Divider** (oklch(92% 0.006 264)): Chart sub-nav separators, intro section dividers, metric switch borders.
- **On-Inverse** (oklch(100% 0 0)): Text on dark tooltips and sidebar-on-dark contexts.
- **On-Sidebar** (oklch(98.5% 0.004 264)): Tooltip text on near-black overlays.

### Named Rules

**The SDG Sovereignty Rule.** The 17 UN SDG hex colors (`window.SDG_COLORS`) are the only saturated hues permitted in charts, legends, and goal icons. UI chrome accent (violet-indigo) must never recolor SDG data or compete with goal semantics.

**The Quiet Chrome Rule.** The primary accent appears on ≤10% of any screen: active nav, selected filters, slider handles, and focus rings. Its rarity signals interactivity; broad accent fills are prohibited.

## 3. Typography

**Display Font:** System UI stack (`-apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`)
**Body Font:** Same system UI stack (single-family product UI)
**Label/Mono Font:** Same stack at 600 weight; no separate mono—data labels use tabular figures via canvas rendering

**Character:** Neutral, legible, and institutionally calm. No display/body pairing; the type reads as research software, not a campaign landing page.

### Hierarchy

- **Display** (700, 22px, 1.2): Welcome headline on home intro (`home-welcome-first-line`). Rare; one per view maximum.
- **Headline** (700, 20px, 1.25): Chart titles centered above drawing areas (`chart-title`). Primary section headers within chart stages.
- **Title** (700, 18px, 1.25): Top-level nav tab labels (`nav-links a`). MDB button text labels when logos are absent.
- **Body** (400–600, 14–16px, 1.5): Intro prose (`home-welcome-text` at 16px), error messages, map legend rows. Prose capped at ~75ch where it runs in paragraphs.
- **Label** (600, 13px, 1.25): Chart sub-nav tabs, back buttons, metric switch labels, year-slider labels, tooltip text (12px for compact tooltips).

### Named Rules

**The Fixed Scale Rule.** UI type uses fixed px/rem sizes—no `clamp()` fluid headings. Researchers view at consistent DPI; sidebar and chart titles must not shrink unpredictably at breakpoints.

**The One Voice Rule.** One sans-serif family carries every UI element. Display fonts in buttons, labels, or data tables are prohibited.

## 4. Elevation

Hybrid system: tonal layering conveys structure at rest; light shadows appear on interactive lift and floating overlays. The dashboard is not flat—chart wrappers and slider controls float slightly—but it is not materially elevated.

Chart wrappers (`.chart-wrapper`) use `box-shadow: 0 4px 20px rgba(0,0,0,0.08)` on white surfaces. MDB sidebar buttons lift on hover (`0 6px 16px rgba(0,0,0,0.15)`). Floating metric switches and back buttons use tighter shadows (`0 2px 8px`–`0 2px 12px`). Depth between chart stage and drawing area is tonal: white wrapper → muted inner container (`surface-muted`, 16px radius)—no shadow between them.

### Shadow Vocabulary

- **Stage lift** (`box-shadow: 0 4px 20px rgba(0,0,0,0.08)`): Chart wrappers, major content panels.
- **Control float** (`box-shadow: 0 2px 8px rgba(0,0,0,0.08)`): Back buttons, compact overlays at rest.
- **Hover lift** (`box-shadow: 0 6px 16px rgba(0,0,0,0.15)`): MDB sidebar buttons on hover.
- **Selection ring** (`box-shadow: 0 0 0 4px rgba(37,99,235,0.55)`): Selected MDB button—not a drop shadow but structural elevation of focus.
- **Tooltip depth** (`box-shadow: 0 2px 8px rgba(0,0,0,0.3)`): SDG and country tooltips on near-black backgrounds.

### Named Rules

**The Flat Interior Rule.** Inner chart drawing areas are shadowless. Depth inside a chart stage is conveyed by `surface` → `surface-muted` tonal step only.

**The State-Only Lift Rule.** Shadows intensify on hover or selection—never on static decorative containers. If a card isn't interactive, it doesn't lift.

## 5. Components

### Buttons

- **Shape:** 8px corner radius on rectangular controls; circular (50%) for carousel arrows
- **Primary (nav tab active):** `rgba(37,99,235,0.12)` fill, accent text, 10px × 20px padding, 18px/700 type
- **MDB filter button:** White surface, 1px `border-muted` stroke, 8px radius, 3.15:1 aspect ratio, logo-centered. Selected: accent border + 4px blue ring shadow—never full accent fill
- **Back button (`.chart-back-btn`):** White surface, `border-muted` stroke, 8px radius, 8px × 14px padding, 13px/600 label, light float shadow
- **Hover / Focus:** Surface-hover background on back buttons; MDB buttons translateY(-1px) with stronger shadow. All interactive elements: 2px `accent` outline, 2px offset (`focus-visible`)

### Chips

- **Style:** Metric switch uses pill container (`border-radius: 999px`, white 95% opacity, `divider` border, compact shadow). Active metric label gets accent text + 2px accent border—not a filled chip
- **State:** Active label bordered; inactive labels are text-only inside the pill frame

### Cards / Containers

- **Corner Style:** 12px on chart wrappers and slider stages; 16px on inner chart drawing areas
- **Background:** White wrapper (`surface`), muted interior (`surface-muted`) for canvas/chart-container
- **Shadow Strategy:** Stage lift shadow on wrapper only (see Elevation)
- **Border:** 1px `divider` on slider wrappers; 2px `border` on nav bar bottom edge
- **Internal Padding:** 32px block / 24px inline on chart wrappers (`space-8` / `space-6`)

### Inputs / Fields

- **Style:** Year range slider: 4px rail (`divider`), gradient range fill (accent-strong → metric-amount), 16px circular handles with 2px accent border
- **Focus:** Handle hover adds `0 0 0 3px rgba(37,99,235,0.25)` glow
- **Toggle switch:** 48×26px pill track (`switch-track`), 20px thumb, 150ms transitions

### Navigation

- **Top bar:** 112px height (auto on mobile), white surface, 2px bottom border. SDG wheel logo left; view tabs right (Home hidden in lite mode)
- **Chart sub-nav:** Underline tabs—transparent background, 2px bottom border on active, 13px/500 inactive → 600 active
- **Mobile (≤768px):** Sticky nav, hamburger popover via native `<dialog>`/popover, 36px logo, brand name visible

### MDB Sidebar (signature component)

- **Panel:** 240px wide, `sidebar` inkwell background, 16px radius, vertical stack of 9 MDB logo buttons
- **Buttons:** White cards with institutional logos; selected state uses accent ring, not inverted fill
- **Responsive:** At ≤1200px, sidebar becomes horizontal wrap grid (4 columns)

### SDG Tooltip (signature component)

- **Style:** Near-black overlay (`rgba(17,24,39,0.94)`), `on-sidebar` text, 12px, 6px × 10px padding, 4px radius
- **Behavior:** `pointer-events: none`, appears on chart hover; never competes with SDG colors in the data layer

## 6. Do's and Don'ts

### Do:

- **Do** keep charts and maps as the dominant visual element—chrome exists only to filter and navigate data
- **Do** use the UN `SDG_COLORS` array for all goal-related visualization without modification
- **Do** use the violet-indigo accent exclusively for selection, active nav, focus rings, and slider affordances
- **Do** maintain fixed rem type sizes (13px labels, 20px chart titles, 18px nav tabs)
- **Do** respect `prefers-reduced-motion`—disable nav popover animation and intro chevron transitions
- **Do** provide 44px minimum touch targets on mobile nav and chart sub-nav tabs
- **Do** use tonal `surface` / `surface-muted` layering inside chart stages before adding shadows
- **Do** label data precisely: "project count" vs "amount", "MDB", "SDG", "Most Relevant"

### Don't:

- **Don't** use generic SaaS dashboard clichés—no hero metrics, cream backgrounds, or gradient accents in chrome
- **Don't** apply over-decorated data viz treatments that compete with the SDG color system
- **Don't** add consumer-style marketing polish that undermines research credibility
- **Don't** use border-left or border-right greater than 1px as a colored accent stripe on cards or list items
- **Don't** use gradient text (`background-clip: text`) anywhere in the UI
- **Don't** default to glassmorphism—metric switch pills use solid white at 95% opacity, not backdrop blur
- **Don't** put display fonts in buttons, labels, or data tables
- **Don't** recolor SDG icons or chart segments with the UI accent palette
- **Don't** use full-saturation accent fills on inactive or resting states
- **Don't** animate layout properties on page load—view panels may fade in (250ms) but content is visible by default
