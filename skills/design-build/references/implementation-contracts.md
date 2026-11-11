# Frontend visual implementation contracts

These are **original examples**, not copied design assets. Adapt token names to the project's existing design system. Retain semantic HTML, focus styles, accessible contrast and natural source order.

## Three-level color mapping
```css
:root {
  /* primitives — raw values; example palette only */
  --ink-900: #172033;
  --paper-0: #ffffff;
  --brand-600: #2455aa;
  --space-1: .25rem;
  --space-2: .5rem;
  --space-3: .75rem;
  --space-4: 1rem;
  --space-6: 1.5rem;
  --space-8: 2rem;
  /* semantic roles */
  --color-text-primary: var(--ink-900);
  --color-surface: var(--paper-0);
  --color-action: var(--brand-600);
  --color-on-action: var(--paper-0);
  /* component application */
  --button-primary-bg: var(--color-action);
  --button-primary-fg: var(--color-on-action);
}
/* Change semantic roles, not random primitives; validate actual pairings. */
```

## Flexible layout and legible type
```css
.page { width: min(100% - 2rem, 72rem); margin-inline: auto; }
.feature-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 18rem), 1fr)); gap: var(--space-6); }
.article-body { max-width: 68ch; font-size: 1rem; line-height: 1.6; }
.title { font-size: clamp(1.8rem, 1.2rem + 2vw, 3rem); line-height: 1.1; }
:where(a, button, input):focus-visible { outline: 3px solid var(--color-action); outline-offset: 3px; }
```

## Required screenshot and content matrix
- Mobile narrow, mobile wide, desktop wide; 200% browser zoom/reflow; light/dark (if supported).
- Short, typical and unusually long headings; localization and numbers; actual data density.
- Loading, error, empty, focus, selected and disabled states if applicable.
- Grayscale test for salience; WCAG-compliant actual color pairings (delegate to `wcag-*`).
- Compare DOM/keyboard order with intended visual sequence; never use CSS `order` to fake meaningful reading order.

## Completion evidence
Record the original symptom, changed tokens/components, before/after comparison method, and untested states. A pleasant screenshot is not evidence of accessibility or usability conformance.
