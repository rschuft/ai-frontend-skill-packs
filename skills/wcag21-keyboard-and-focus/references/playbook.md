# Keyboard and focus — diagnostic and repair playbook

**Primary criteria:** 2.1.1–2.1.4, 2.4.3, 2.4.7. Closely related: 2.1.2 (non-interference), 4.1.2 (name/role/value), 2.4.1 (skip). References: https://www.w3.org/WAI/ARIA/apg/patterns/ and https://www.w3.org/WAI/WCAG21/Understanding/keyboard

## Differential diagnosis

**Keyboard missing:** a pointer-only click listener, drag handler or hover target. **Trap:** Tab/Shift+Tab cannot leave component or page. **Focus order:** motion between interactive elements changes meaning or makes operation difficult. **Focus visibility:** actual keyboard focus is not visually apparent. **Keyboard shortcut collision:** unmodified characters fire unexpectedly while user types or speaks. **Name/role/state:** control may be keyboard-operable but its role cannot be discovered or state not announced.

## Build with native controls

```html
<button type="button" id="open-dialog">Edit profile</button>
<a href="/settings">Settings</a>
<label for="timezone">Time zone</label>
<select id="timezone"><option>UTC</option></select>
```

Prefer native HTML to generic clickable `<div>`. Native buttons support Enter and Space and preserve exposed state and semantics. A custom widget requires complete keyboard interaction, correct focus management and synchronized accessibility state, not just `tabindex="0"` or `role="button"`.

## Dialog state machine

- Before opening, remember the invoking element; open dialog with accessible name and sensible initial focus. Scope focus appropriately for a modal; keep background non-interactive.
- Tab and Shift+Tab move among controls; Escape closes where expected; never strand users. Maintain visible focus ring.
- On close, restore focus to invoker when still present; otherwise move to logical fallback. Announce state by semantics, not a duplicate live alert.
- Verify browser forward/back navigation and dynamic lists don't leave focus on removed DOM nodes.

A composite widget like tabs, menu or grid may use arrow-key navigation and roving `tabindex`. Consult the exact WAI-ARIA APG pattern: patterns are helpful implementation guidance, not an independent normative WCAG requirement. If a native alternative suffices, it is safer.

## Single-character shortcuts

For letter/number/punctuation keys with no modifiers, support at least one permitted path: turn off, remap to modifiers, or activate only while relevant component has focus. Test actual character entry, speech-input injection and shortcuts on page load. Avoid global `keydown` handlers that consume events inside editable controls.

## Manual tests

Keyboard only: start at address bar, enter page, follow skip link, Tab and reverse Tab every interactive item, open/close menus/dialogs, change selections with arrows, activate buttons with Enter and Space, submit forms, move around 320px layout, finish task. Check focus indicator after rerender, scroll and overlay dismiss. Capture video or exact key sequences when failing; static axe scan cannot prove keyboard completeness.
