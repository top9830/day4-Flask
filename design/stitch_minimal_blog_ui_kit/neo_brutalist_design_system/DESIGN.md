---
name: Neo-Brutalist Design System
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#4b4731'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#7c775f'
  outline-variant: '#cdc7aa'
  surface-tint: '#6a5f00'
  primary: '#6a5f00'
  on-primary: '#ffffff'
  primary-container: '#ffe600'
  on-primary-container: '#726600'
  inverse-primary: '#dec800'
  secondary: '#0c00e0'
  on-secondary: '#ffffff'
  secondary-container: '#2f32ff'
  on-secondary-container: '#cccdff'
  tertiary: '#5e5e5e'
  on-tertiary: '#ffffff'
  tertiary-container: '#e4e4e4'
  on-tertiary-container: '#656565'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#fde400'
  primary-fixed-dim: '#dec800'
  on-primary-fixed: '#201c00'
  on-primary-fixed-variant: '#504700'
  secondary-fixed: '#e0e0ff'
  secondary-fixed-dim: '#bfc2ff'
  on-secondary-fixed: '#02006d'
  on-secondary-fixed-variant: '#0d00ee'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1b1b1b'
  on-tertiary-fixed-variant: '#474747'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-2xl:
    fontFamily: Space Grotesk
    fontSize: 120px
    fontWeight: '700'
    lineHeight: 100px
    letterSpacing: -0.05em
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 72px
    fontWeight: '700'
    lineHeight: 64px
    letterSpacing: -0.03em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 32px
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '500'
    lineHeight: 28px
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-bold:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '700'
    lineHeight: 16px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  border-width: 3px
  shadow-offset: 6px
---

## Brand & Style

This design system is built on the philosophy of "Raw Impact." It rejects the softness and gradients of modern web aesthetics in favor of a stark, honest, and high-energy interface. It is designed for brands that want to appear disruptive, confident, and unapologetically loud. 

The aesthetic is characterized by a "low-fidelity/high-intent" look. By using heavy strokes and a restricted, high-contrast palette, the UI demands attention and ensures that hierarchy is never subtle. The target audience includes creative platforms, experimental portfolios, and bold fintech or media outlets that want to stand out in a sea of sameness.

## Colors

The color strategy for this design system is based on maximum contrast. 

- **Primary (Yellow):** Used for primary actions and background blocks that need to pop against the white canvas.
- **Secondary (Blue):** Used for accents, links, and secondary interactive elements to provide a cold counter-balance to the yellow.
- **Background:** Strictly `#FFFFFF` to ensure the heavy black borders and vibrant primaries maintain their intensity.
- **Borders & Text:** Strictly `#000000`. No grays are permitted in the core structural elements.

## Typography

Typography is treated as a structural element rather than just a medium for reading. **Space Grotesk** provides the technical, geometric edge required for headlines, while **Work Sans** ensures legibility for dense body text.

To achieve the "overlapping" effect requested in the design system, display sizes use tight line-heights (often less than 100% of font size) and negative letter-spacing. Headlines should be placed with tight margins, occasionally bleeding into adjacent sections or containers to create a sense of raw urgency.

## Layout & Spacing

This design system utilizes a rigid 12-column grid with heavy 24px gutters. Spacing is strictly mathematical, moving in 8px increments to maintain a disciplined structure despite the visual chaos of the overlaps.

Layouts should favor asymmetry. Large blocks of primary color should be used to anchor sections, often with containers that do not align perfectly with the text inside them, creating a "shifted" or "misprinted" look common in brutalist print design. Use generous outer margins (80px+) to allow the internal elements to breathe and feel more impactful.

## Elevation & Depth

This design system completely avoids blurs, soft shadows, and gradients. Depth is created through **Hard Shadows**—solid black rectangular fills offset from the parent container.

1.  **Level 0:** Flat on the white background with a 3px black border.
2.  **Level 1:** Container with a 3px border and a solid black shadow offset by 6px (bottom-right).
3.  **Interactive State:** On hover, the container translates 2px towards the shadow. On click/press, the container translates the full 6px to "cover" the shadow, simulating a physical button press.

## Shapes

The shape language is strictly rectangular. All corners are set to `0px` (Sharp). This reinforces the "unpolished" and "industrial" nature of the design system. Rounded corners or circular elements should be avoided unless they are functional (like a toggle thumb), and even then, they should be encased in a square container.

## Components

- **Buttons:** Large, rectangular blocks with a 3px black border. Primary buttons use the Yellow background; secondary use Blue. All buttons must have a solid black "Hard Shadow" offset.
- **Input Fields:** Stark white backgrounds with 3px black borders. Placeholder text should be high-contrast (50% opacity black). On focus, the border thickness remains the same, but the background of the label or the field itself can shift to Yellow.
- **Cards:** White or Yellow backgrounds. Cards are the primary container for the hard-shadow effect. Content inside cards should have aggressive padding (24px+).
- **Checkboxes & Radios:** Sharp squares. When selected, they are filled with a solid black "X" or a solid black square rather than a checkmark or dot.
- **Chips/Badges:** Small rectangular blocks with 2px borders. Used to categorize content without the heavy shadow used for interactive buttons.
- **Overlapping Elements:** Header text should frequently "crash" into the top of a card or an image, breaking the container's top border to create a layered, high-impact editorial feel.