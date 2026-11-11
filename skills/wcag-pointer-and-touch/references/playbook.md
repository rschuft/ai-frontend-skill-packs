# Pointer, touch, voice commands and motion sensing — playbook

**Primary criteria:** 2.5.1–2.5.6. Reference: https://www.w3.org/TR/WCAG21/#input-modalities

## Distinguish barriers

- **2.5.1 A (gesture):** multipoint or path-based gestures must have a single-pointer, non-path alternative unless the gesture is essential. Pinch-to-zoom requires zoom controls; freehand drawing may genuinely depend on path.
- **2.5.2 A (cancellation):** single-pointer actions must satisfy one of no-down-event, up-event with abort/undo, up-event reversal or essential down-event. Pointer-up alone is not always enough: verify cancellation by moving away before release or undo.
- **2.5.3 A (label in name):** visible text appears *inside* accessible name so voice users can speak the visible command. Preserve word order preferably at start of name.
- **2.5.4 A (motion):** shake/tilt/body-motion features need ordinary control and a way to disable motion actuation unless an exception applies.
- **2.5.5 AAA (target size):** targets generally at least **44×44 CSS px**, subject to equivalent, inline, unmodified user-agent and essential exceptions. Do not replace this with WCAG 2.2 AA's separate rule.
- **2.5.6 AAA (concurrent mechanisms):** avoid disabling available touch, pen, mouse or keyboard unless essential, a security requirement or a user setting.

## Implementation

For drag-and-drop, add **Move up**/**Move down** or equivalent single-pointer and keyboard controls. Ensure the alternative creates the same final ordering, and announce successful updates. For swipeable galleries, visible Previous/Next buttons work with mouse, touch, keyboard and voice. Touch-action CSS and native browser gestures can interact; test on real mobile devices.

Avoid actions on `pointerdown` where a button's standard `click` handler suffices. For dangerous action, provide explicit confirmation or undo path and test dragging off the button after pointer-down. Ensure pointer capture is released when canceled. Pointer cancellation does not by itself guarantee keyboard support—test 2.1.1 separately.

```html
<button type="button" aria-label="Move item up">Move up</button>
<!-- Visible label 'Move up' is present in accessible name. -->
```

Avoid `aria-label="Previous"` on a visually labelled `Back` button: speech users may say “click Back” and fail if accessible name omits “Back”.

## Verification

Operate with finger, mouse, pen where available, switch devices midtask and test voice-access names. Measure actual clickable boxes using layout APIs rather than text size; document allowed exceptions on AAA target-size audit. Verify path-gesture alternative has equal functional outcome. Test accidental press, drag outside, release, undo and long-press. Do not assert full voice-control support from name matching alone.

## WCAG 2.2 pointer extension

- **2.5.7 AA Dragging Movements:** For each reorder, slider, map, carousel or canvas gesture authored by the app, try to complete the same user objective using one pointer without dragging (e.g., pick then select destination, stepper buttons). Confirm the alternative actually performs the full function; a keyboard-only path does not pass the single-pointer requirement.
- **2.5.8 AA Target Size (Minimum):** Measure *actual* pointer hit boxes in CSS px. Minimum is 24×24 or allowed spacing/inline/equivalent/user-agent/essential exceptions. Use the W3C 24 CSS-px circles test for undersized targets. The old 44 CSS-px SC 2.5.5 is a separate AAA requirement.
Sources: https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements and https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum
