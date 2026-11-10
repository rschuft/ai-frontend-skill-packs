# Color theory and semantic palette playbook

**Discriminate:** Hue harmony is an aesthetic preference; luminance contrast and not-color-alone information have explicit accessibility requirements. Palette harmony does not equal conformance.

## Palette construction
1. Capture existing brand primary, audience/market context and interface function. For a new identity, explore complementary (energetic), analogous (restrained), triadic (playful) and split-complementary (varied with a lead); these are **options**, not guarantees of emotional response.
2. Specify neutral canvas, ink/text ramp, one anchor accent and functional success/warning/error/info roles. Treat the 60/30/10 idea as a visual balance prompt for marketing screens, **not a quantitative rule for product UI**.
3. Encode **primitive → semantic → component** tokens: hue ramp → `text.primary`, `surface.canvas`, `action.primary` → `button.primary.bg`. Make separate light/dark semantic mappings; do not invert hex values mechanically.
4. Draw a **pairing matrix** for body text, links, labels, buttons, chips, focus rings, charts, hover/disabled/error states against their actual rendered backgrounds. Calculate contrast for each applicable pair; validate alpha overlays/gradients over worst-case crop.
5. Add non-color state indicators (text, icons, shape, underlines) and test grayscale/color-vision simulations. A warning cannot be a red dot alone.

## Useful formula: WCAG 2.x relative luminance
For each sRGB channel `c` normalized into 0..1: linearize to `c/12.92` if `c <= 0.04045`, otherwise `((c + .055)/1.055)^2.4`. Luminance = `.2126*R + .7152*G + .0722*B`. Contrast ratio = `(Llighter + .05)/(Ldarker + .05)`. Use the WCAG pack for full applicability, exceptions and conformance claims.

## Design risks
- Blue/orange can be complementary but still unreadable at a specific tone and state.
- Color psychology associations are culturally and context dependent, not deterministic truths.
- Low saturation need not mean low contrast; adjust lightness and surface pairing independently.
- Preserve existing brand constraints unless authorized to change them.

## Acceptance
A role-to-pairing table passes actual applicable WCAG checks in all supported themes, semantic states remain identifiable without hue, and the primary visual hierarchy is intact.

Sources: https://www.digitalpolo.com/color-theory-for-brand-design/ · https://www.digitalpolo.com/contrast-in-design/ · https://www.digitalpolo.com/design-tokens-explained/
