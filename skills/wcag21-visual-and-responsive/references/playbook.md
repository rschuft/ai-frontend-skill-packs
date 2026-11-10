# Visual presentation, contrast and reflow — diagnostic and repair playbook

**Primary criteria:** 1.3.4, 1.4.1, 1.4.3–1.4.6, 1.4.8–1.4.13. Consider 2.4.7 for focus indicators. Reference: https://www.w3.org/WAI/WCAG21/Understanding/reflow

## Distinguish requirements before measuring

| Barrier | Criterion | Operative test |
| --- | --- | --- |
| Information conveyed by hue alone | 1.4.1 A | Remove color interpretation; check shape/text/other cue |
| Ordinary / large text contrast | 1.4.3 AA | >=4.5:1 normal, >=3:1 large; rendered colors and image backgrounds |
| Enhanced text contrast | 1.4.6 AAA | >=7:1 normal, >=4.5:1 large |
| Essential control/graphic visual indication | 1.4.11 AA | >=3:1 against adjacent color(s) |
| User text enlargement | 1.4.4 AA | Increase up to 200% with no loss |
| Content reflow | 1.4.10 AA | 320 CSS px vertical content or 256 CSS px horizontal content without 2D page scroll for standard content |
| User-specified spacing | 1.4.12 AA | Apply all four text-spacing overrides together with no loss |
| Additional hover/focus content | 1.4.13 AA | dismissible where required, hoverable, persistent |
| Images of text | 1.4.5 AA / 1.4.9 AAA | Prefer actual text, account for exceptions |

Beware: focus-visible appearance metrics commonly cited from WCAG 2.2 are not normative WCAG 2.1 2.4.7 values. Determine contrast from actual **composited** colors, not just CSS declarations when transparency, gradients or overlays change the visible result.

## CSS repairs

```css
/* Resilient layout and text */
.page { width: min(100% - 2rem, 74rem); margin-inline: auto; }
.controls { display: flex; flex-wrap: wrap; gap: .75rem; }
.card { min-width: 0; overflow-wrap: anywhere; }
.content { line-height: 1.5; }
.button:focus-visible { outline: 3px solid currentColor; outline-offset: 3px; }
@media (max-width: 40rem) { .sidebar-layout { display: block; } }
```

A fixed height on form fields or buttons often defeats user spacing overrides. An oversized fixed-width table can be placed in a **local scroll container** when its two-dimensional layout is truly essential; don't excuse unrelated horizontal page overflow. Use appropriate `min-width:0`, responsive columns, natural wrapping, fluid sizing and visible control states.

**Override test** (developer-tools or browser automation injection, not production stylesheet):

```css
* { line-height: 1.5 !important; letter-spacing: .12em !important;
    word-spacing: .16em !important; }
p { margin-bottom: 2em !important; }
```

The formal test also requires paragraph spacing of at least 2x font size; injected rules must be checked for how styles actually resolve. These are **override tolerance** settings: page defaults need not use them.

## Hover/focus content

If pointer hover or keyboard focus makes additional content appear and disappear, test Escape or equivalent dismissal (when required), pointer movement into the additional content, and persistence until hover/focus removed, dismissed or information invalid. Do not blindly assert that every tooltip must trap focus or auto-close instantly; those can introduce new failures.

## Validation matrix

Use browser at desktop and 320-equivalent widths, 200% text scale, 400% zoom as relevant, both device orientations, high-contrast/forced-colors settings, color scheme variants and keyboard states. Measure CSS px not screenshots scaled by device pixel ratio. Document specific exceptions (logo, incidental, inactive, essential 2D) rather than applying them globally. Automation detects candidate pairs and overflow; manual testing decides meaning, exceptions, hidden content and actual task completion.
