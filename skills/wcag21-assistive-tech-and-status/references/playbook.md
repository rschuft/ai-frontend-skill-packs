# Accessible name/role/value and live status — playbook

**Primary criteria:** 4.1.1, 4.1.2, 4.1.3. Related: 1.3.1, 2.5.3, 3.3.1, 2.4.3. Reference: https://www.w3.org/WAI/WCAG21/Understanding/name-role-value

## Treat accessible tree as a runtime API

For every custom interactive component, determine its accessible **name**, **role**, **value**, **states**, **properties** and whether user-initiated state changes propagate to assistive technology. A visible checkbox can be mouse-operable yet invisible as a checkbox to screen readers. Prefer a real `<input type="checkbox">` with label. For custom widgets, implement both ARIA semantics and all expected keyboard events; a `role` attribute alone never creates native keyboard behavior.

## Correct status-region patterns

```html
<p id="result-status" role="status" aria-live="polite"></p>
<!-- On search completion, update its text without moving focus. -->
```

Use `role="status"` or `aria-live="polite"` for nonurgent search counts, save completion and loading changes. For critical error use a justified assertive channel such as `role="alert"`, avoiding simultaneous duplicate announcements. Initialize the live region before asynchronous update where practical. When an interaction genuinely calls for focus (e.g., route transition or modal), manage focus separately; live announcement alone is not a substitute for keyboard accessibility.

## Interpretation of 4.1.1 Parsing in WCAG 2.1

The **06 May 2025** WCAG 2.1 recommendation includes Note 1: consider 4.1.1 always satisfied for HTML or XML. Do not report invalid nesting or duplicate IDs *as failures of 4.1.1* in HTML/XML. HTML validation is still valuable for engineering quality. If a duplicate ID breaks label association, identify the actual barrier and map to 1.3.1 or 4.1.2. Reference: https://www.w3.org/WAI/WCAG21/Understanding/parsing

## Failure and repair examples

- Icon button with accessible name “button”: give descriptive accessible name, ideally via visible text; then verify speech-control compatibility with 2.5.3.
- Switch updates visually but still exposes unchecked: update `aria-checked` and test accessibility state; if `<input type="checkbox">` works, use that instead.
- Custom listbox exposes generic elements, fails arrow navigation: use an accessible native `<select>` where possible or implement complete composite pattern following WAI-ARIA APG.
- Result count changes silently: expose a status message without forcing focus away from search input.
- Async errors are announced constantly on every keystroke: group or delay to relevant interaction state, choose appropriate politeness.

## Evidence levels

DOM inspection shows markup but not AT rendering. Use browser accessibility pane for computed names/states and test with at least one appropriate screen reader/browser pairing (e.g. NVDA + Firefox/Chrome or VoiceOver + Safari). Prefer a second pairing for critical custom components. Observe updates while focus stays put, then inspect screen-reader announcement logs or user testing notes. Do not certify 4.1.2 or 4.1.3 solely from attribute presence.
