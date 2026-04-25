---
name: Quietude Editorial
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#414848'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#717878'
  outline-variant: '#c1c8c7'
  surface-tint: '#446464'
  primary: '#173838'
  on-primary: '#ffffff'
  primary-container: '#2f4f4f'
  on-primary-container: '#9ec0bf'
  inverse-primary: '#abcdcd'
  secondary: '#5d5f5e'
  on-secondary: '#ffffff'
  secondary-container: '#dcdddc'
  on-secondary-container: '#5f6161'
  tertiary: '#492c1d'
  on-tertiary: '#ffffff'
  tertiary-container: '#634232'
  on-tertiary-container: '#ddb09b'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c6e9e9'
  primary-fixed-dim: '#abcdcd'
  on-primary-fixed: '#002020'
  on-primary-fixed-variant: '#2c4c4c'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c7c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#ffdbcb'
  tertiary-fixed-dim: '#ebbda7'
  on-tertiary-fixed: '#2e1508'
  on-tertiary-fixed-variant: '#603f2f'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  headline-xl:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
  headline-lg:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.7'
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Public Sans
    fontSize: 13px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  space-xs: 0.5rem
  space-sm: 1rem
  space-md: 2rem
  space-lg: 4rem
  space-xl: 8rem
  container-max: 1120px
  text-max: 680px
  gutter: 24px
---

## Brand & Style

This design system is built on the principles of **Minimalism** and editorial excellence. It prioritizes the reading experience by removing visual noise and focusing on typographic hierarchy. The brand personality is intellectual, calm, and sophisticated—evoking the feeling of a high-end print journal or a quiet library. 

The target audience consists of long-form readers and writers who value focus over distraction. The UI uses heavy whitespace and a restrained color palette to create an emotional response of clarity and repose.

## Colors

The palette is rooted in organic, low-fatigue tones. 
- **Primary/Accent:** A muted Forest Green used sparingly for links, call-to-actions, and active states to guide the eye without shouting.
- **Backgrounds:** A tiered system of soft whites (Paper) and very light grays (Parchment) to provide subtle separation between sections.
- **Text:** Deep Charcoal is used instead of pure black to reduce harsh contrast on digital screens, maintaining a "printed ink" aesthetic.
- **Dividers:** Extremely low-contrast grays used for structural definition.

## Typography

This design system utilizes a classic pairing of a literary serif and a functional sans-serif. 
- **Headings:** Newsreader provides an authoritative, traditional feel. It should be used with tight line-heights and slight tracking adjustments for larger titles.
- **Body:** Public Sans is chosen for its exceptional readability at various sizes. A generous line-height of 1.7 is mandated for body text to prevent "line-skipping" during long reading sessions.
- **Labels:** Small caps or increased letter-spacing should be applied to metadata and category labels to distinguish them from body prose.

## Layout & Spacing

The layout follows a **Fixed Grid** model for desktop, centered to create a focused reading column. 
- **Rhythm:** A 8px base unit drives all spacing.
- **Whitespace:** Large vertical gaps (8rem) are used between major content sections to signal a change in context.
- **The Golden Column:** Article content is restricted to a maximum width of 680px to maintain optimal characters-per-line (CPL) for reading comfort.
- **Margins:** Page margins are wide, pushing the content to the "stage" of the viewport.

## Elevation & Depth

This design system avoids heavy shadows, favoring **Tonal Layers** and **Low-contrast Outlines**.
- **Surface Depth:** Depth is achieved by shifting the background color from the main canvas (Soft White) to a secondary surface color (Light Gray).
- **Outlines:** Borders should be 1px wide and use a color only slightly darker than the surface they sit on.
- **Interactivity:** Elements like cards may use a very soft, diffused ambient shadow (5% opacity) on hover to indicate tactility without breaking the minimal aesthetic.

## Shapes

The shape language is "Soft," utilizing small corner radii to take the edge off the geometric grid while maintaining a professional, structured appearance. 
- **Standard Radius:** 4px (0.25rem) for cards and input fields.
- **Large Radius:** 8px (0.5rem) for featured image containers.
- **Interactive Elements:** Buttons follow the standard 4px radius; avoid pill-shapes as they are too casual for this editorial tone.

## Components

- **Simple Cards:** Use a background color one step removed from the main canvas. Borders are optional; if used, they should be subtle. Typography within the card must maintain the serif/sans-serif hierarchy.
- **Clean Form Inputs:** Use a 1px border. On focus, the border color transitions to the primary Forest Green. Labels should use the `label-sm` style.
- **Subtle Dividers:** 1px horizontal lines using a light gray. Dividers should never span the full width of the container; they should have significant horizontal margins.
- **Buttons:** Solid primary color for the main action, with white text. Ghost buttons (border only) for secondary actions.
- **Breadcrumbs & Metadata:** Small, desaturated text using Public Sans to remain unobtrusive.
- **Blockquotes:** Use a thicker vertical border in the accent color on the left side, paired with italicized Newsreader typography.