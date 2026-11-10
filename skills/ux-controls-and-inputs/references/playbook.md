# Interaction mechanics, targets and control behavior

## Diagnose

Separate **target acquisition** (small/distant/crowded hit area), **control semantics** (unclear expected behavior), **input modality** (touch, mouse, pen, keyboard, switch), **responsiveness** and **state bugs**. Record device, viewport, zoom, pointer type, proximity to competing controls, task, and exact state transition.

## Repair steps

1. **Targets and spacing:** Increase real click/touch hit area, separate adjacent actions and place contextual controls near what they operate. Never enlarge only the icon without enlarging its interactive region. Avoid nested interactive elements.
2. **Accessible control primitive:** Prefer native `<button>`, `<a href>`, `<label>`, `<input>` when behavior matches. Retain visible focus and an accessible name; use keyboard-compatible patterns for custom composites.
3. **Feedback and repeat behavior:** Every activation should produce immediate, correct state feedback. Pending submissions must prevent unintended duplicates without trapping the user or suppressing cancellation.
4. **Reversible and destructive actions:** Make consequence clear at the control; use confirmation only when warranted, prefer undo for recoverable state changes, and never hide a destructive action in an unlabeled icon.
5. **State coherence:** Hover, focus, active, selected, pending, success, disabled and error must not contradict one another. A spinner is not a state model.

## Accessibility and measurement

WCAG 2.2 SC 2.5.8 minimum pointer target **24×24 CSS pixels or applicable spacing/other exceptions**; this is a conformance baseline, not an ideal universal target. SC 2.5.5 has a stricter 44×44 target measure at AAA. Keyboard access, focus order and semantics are separate requirements. Source: https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum

## Tests

Run click/tap acquisition in typical and worst-case positions, at 200% zoom and narrow viewports. Confirm keyboard-only traversal, focus and activation, screen-reader names, pointer cancellation, double-click/double-submit prevention, drag alternative when applicable, and inert behavior of disabled controls. Test nearby targets after layout shifts.

Source lenses: https://lawsofux.com/fittss-law/ ; https://lawsofux.com/doherty-threshold/ ; https://lawsofux.com/postels-law/ ; https://www.w3.org/WAI/ARIA/apg/patterns/
