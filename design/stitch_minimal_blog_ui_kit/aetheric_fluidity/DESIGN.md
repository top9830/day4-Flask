---
name: Aetheric Fluidity
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#494552'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#7a7583'
  outline-variant: '#cac4d4'
  surface-tint: '#674bb5'
  primary: '#674bb5'
  on-primary: '#ffffff'
  primary-container: '#a78bfa'
  on-primary-container: '#3c1989'
  inverse-primary: '#cebdff'
  secondary: '#a43073'
  on-secondary: '#ffffff'
  secondary-container: '#fc79bd'
  on-secondary-container: '#76014e'
  tertiary: '#0060ac'
  on-tertiary: '#ffffff'
  tertiary-container: '#5a9ff4'
  on-tertiary-container: '#003563'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e8ddff'
  primary-fixed-dim: '#cebdff'
  on-primary-fixed: '#21005e'
  on-primary-fixed-variant: '#4f319c'
  secondary-fixed: '#ffd8e7'
  secondary-fixed-dim: '#ffafd3'
  on-secondary-fixed: '#3d0026'
  on-secondary-fixed-variant: '#85145a'
  tertiary-fixed: '#d4e3ff'
  tertiary-fixed-dim: '#a4c9ff'
  on-tertiary-fixed: '#001c39'
  on-tertiary-fixed-variant: '#004883'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Be Vietnam Pro
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Be Vietnam Pro
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Be Vietnam Pro
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Be Vietnam Pro
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 40px
  element-gap: 24px
  floating-margin: 64px
---

## Brand & Style

This design system is defined by a sense of weightlessness and organic movement. It targets premium lifestyle, wellness, and creative expression platforms where the user experience should feel like a deep breath—calm, expansive, and effortless.

The design style is a sophisticated blend of **Glassmorphism** and **Minimalism**, characterized by high-translucency layers, expansive background blurs, and the total absence of rigid geometry. There are no hard corners or sharp intersections; instead, elements appear to float within a multi-dimensional space, responding to user interaction with fluid, liquid-like transitions. The emotional response is one of serenity and "digital comfort."

## Colors

The palette is built on a foundation of "Ethereal Pastels." Rather than solid fills, color is primarily expressed through soft, multi-stop gradients that mimic the diffusion of light through water or vapor.

- **Primary (Lavender Mist):** Used for focal points and active states.
- **Secondary (Rose Quartz):** Used for accents and secondary interactive elements.
- **Tertiary (Sky Glass):** Used for subtle highlights and depth variations.
- **Neutral:** A range of high-brightness, low-saturation tones that serve as the "void" in which elements float. 

Backgrounds should use mesh gradients blending these four colors at 5%–10% opacity to ensure the "liquid" feel permeates the entire interface.

## Typography

The typography is chosen to complement the rounded aesthetic of the UI. **Plus Jakarta Sans** provides a friendly yet modern headline structure with soft terminals that mirror the pill-shaped containers. **Be Vietnam Pro** is used for body text and labels for its warmth and exceptional readability in airy, high-white-space layouts. 

Text should never be pure black; instead, use a deep, desaturated violet or navy to maintain the softness of the visual hierarchy. Line heights are generous to allow the text to "breathe" alongside the floating elements.

## Layout & Spacing

This design system uses a **No Grid** philosophy, leaning instead on **Dynamic Padding** and **Safe Areas**. While a standard 12-column structure can be used for basic alignment, elements should feel as though they have drifted into their positions rather than being snapped to a grid.

Spacing is extremely generous. High-level containers feature massive internal padding to prevent any feeling of "clutter." Elements should have varying "float" heights, meaning they don't always align on a horizontal axis, creating a more organic, staggered flow. Negative space is treated as a core design element, not just a separator.

## Elevation & Depth

Hierarchy is achieved through **Glassmorphism** and **Ambient Shadows**.

1.  **Backdrop Blurs:** Every container uses a `backdrop-filter: blur(20px)`. This creates a frosted glass effect that tints the background colors as they pass underneath.
2.  **Inner Glows:** Instead of hard borders, use a 1px semi-transparent white "inner stroke" on the top and left edges to simulate light catching the edge of a glass object.
3.  **Soft Shadows:** Shadows must be extremely diffused (blur radii of 40px–80px) and tinted with the primary or secondary color at 5%–10% opacity. Avoid gray or black shadows.
4.  **Floating State:** Elements that are higher in the stack should have a larger blur radius and a slight scale increase (1.02x) to suggest they are floating closer to the user.

## Shapes

The shape language is strictly **Pill-shaped**. Every button, input field, and chip must use a fully rounded border-radius. Larger cards and containers should use a minimum of `3rem` (48px) corner radius to ensure they feel soft and "liquid." 

There are no right angles in this design system. Even the stems of icons and the ends of progress bars should be rounded. Overlapping shapes should use a "blob" aesthetic—subtle, irregular curves that suggest organic growth rather than geometric precision.

## Components

- **Buttons:** Fully pill-shaped with a soft gradient fill and a 1px white inner glow. On hover, the button should gently expand and the shadow should become more vibrant.
- **Cards:** Large containers with `rounded-xl` (3rem) corners. They feature a high-blur backdrop and a very soft, tinted ambient shadow. No visible borders except for the light-catching inner glow.
- **Inputs:** Pill-shaped with a 10% opacity white fill. Focus states should transition the fill to a soft gradient and increase the backdrop blur.
- **Chips:** Small, ethereal bubbles. These use the highest transparency and are used for tagging and filtering, appearing to drift near the elements they describe.
- **Floating Action Buttons (FAB):** Perfectly circular, using a more vivid version of the primary gradient to indicate the highest level of priority.
- **Selection Controls:** Checkboxes and radio buttons are transformed into soft "toggle-blobs" that change shape slightly when active, mimicking the surface tension of a liquid droplet.