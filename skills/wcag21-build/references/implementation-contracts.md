# Implementation contracts (WCAG 2.1)

These are **starting patterns**, not a proof of conformance. Use the relevant W3C Understanding and specialist playbook for exceptions and manual verification.

## Controls, navigation, forms

- Link means navigate; button means act. Use accessible visible labels, semantic form controls, grouping, stable IDs and native disabled/required states.
- Build keyboard support and focus behavior with native HTML first; implement ARIA APG pattern only if custom semantics are necessary. A custom menu needs focus management, arrow-key behavior and matching state.
- In SPA routing, update document title, announce context appropriately and manage focus. Maintain a working, focus-visible skip link to main content.
- For icon-only actions, supply accurate accessible name and keyboard control; if text is visible, ensure name contains it (2.5.3).

```html
<a class="skip-link" href="#main">Skip to main content</a>
<main id="main" tabindex="-1"><h1>Account settings</h1></main>
<label for="phone">Phone number</label>
<input id="phone" name="phone" type="tel" autocomplete="tel" />
<button type="button" aria-expanded="false" aria-controls="details">Show details</button>
<section id="details" hidden>More details...</section>
```

When toggling `details.hidden`, also update `aria-expanded` atomically. Do not add `aria-hidden` to a subtree containing active focus. On a modal open/close, move focus appropriately and restore it, rather than creating a keyboard trap. Never remove focus outlines without a visibly equivalent replacement.

## Responsive and visual

- Ordinary text contrast at least 4.5:1, large text at least 3:1 (1.4.3 AA); qualifying non-text UI/graphics 3:1 (1.4.11 AA). AAA enhanced text 7:1 / 4.5:1; account for exceptions.
- Do not rely on color alone. Text and labels should survive 200% enlargement, 320 CSS px reflow and user spacing override. Build with content-based sizing and wrapping.
- Test both orientations; exception only if particular orientation is essential. Preserve visible hover/focus extra content with required dismissible, hoverable, persistent properties.

## Dynamic state

```html
<p id="save-status" role="status"></p>
```

Populate the status when saved; do not force focus onto routine nonurgent status messages. Errors should be text-identifiable, programmatically associated to fields and provide suggestions where possible. Do not fire assertive alerts on every keypress.

## Media and time

- Provide appropriate text alternatives, captions, audio descriptions and live equivalents. The file existing is not a quality test.
- Avoid autoplay; expose control if autoplay audio continues >3s; provide pause/stop/hide mechanisms for qualifying moving or updating content.
- Build secure expiration flow that can preserve draft state; test allowed adjustment/extension mechanics and AAA disclosure where applicable.
- Avoid dangerous flashing. Honor reduced-motion for nonessential interaction motion; it does not substitute for seizure protection.

## Input modality

- Single-pointer path-independent equivalents for gestures when required; make activation cancelable; preserve correct label in accessible name.
- AAA target size 44×44 CSS px unless an exception; do not transpose newer 2.2 minimums to a 2.1 audit.

## Test-first obligations

For every changed component, test: (1) semantic roles/names/states, (2) keyboard operation and focus sequence, (3) errors and user recovery, (4) 200% enlargement/reflow where UI can clip, (5) status announcements for updates, (6) affected screen reader/browser combinations, (7) threat/security implications. Capture each known failing state as a focused regression test; don't use hundreds of expensive end-to-end launches where unit contract tests can cover invariants.
