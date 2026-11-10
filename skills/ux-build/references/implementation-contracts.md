# UI implementation contracts

A UX repair is complete when users can successfully interact with it across relevant states, not when its initial screenshot looks right. Apply only contracts relevant to the assigned task and current stack.

## Contract 1: Controls and semantics

**Input:** A task action, navigation destination, text field, option group or custom composite. **Output:** Native semantics where possible, meaningful accessible name, keyboard/pointer behavior and unambiguous state. Use links for destinations, buttons for actions, and labeled native inputs for form entry. An icon can decorate a control but must not be its only explanation when meaning is uncertain.

**Pass:** Tab order follows task flow, focus is always visible, action responds through the expected keyboard input, disabled is real rather than cosmetic, and a screen reader conveys name/role/state. For composite patterns use the corresponding WAI-ARIA APG keyboard specification. **Fail:** click handler on an unfocusable `div`; nested buttons; visual-only selected state.

## Contract 2: Asynchronous operations

Model the *meaning* of states, not just the spinner. Example state diagram: `idle -> submitting -> accepted/queued -> committed | failed | cancelled | uncertain`. Some applications can skip `accepted/queued`; others cannot. Distinguish server acknowledgement, in-progress background work and durable completion. Use a stable operation ID when available to reconcile unknown outcomes. Guard against duplicate mutation and stale responses.

**Pass:** With an artificially delayed response, the user sees action acknowledgement and knows what is pending. With a failure, work is preserved and a safe recovery path is shown. A completion message appears only once the result is confirmed. **Fail:** success toast on button click with an unfired network request; endlessly spinning pending state; two identical payments from repeated tapping.

## Contract 3: Forms and data editing

Bind visible labels to every field. Treat benign format normalization differently from validation of meaningful content. Keep draft and server state separate. Show field-level error text near the input and associate it programmatically. Use a review/confirmation step for material irreversible choices, not for every trivial edit. Do not silently accept high-risk ambiguity.

**Pass:** Pasted and keyboard-entered benign variants work, validation failure preserves all unrelated fields, errors can be reached and understood with keyboard and screen reader, and server validation still rejects unsafe input. **Fail:** silent reinterpretation of a monetary amount or deletion of unsaved user-entered data.

## Contract 4: Navigation and context continuity

Represent meaningful route/state in stable URLs where appropriate; preserve user selection, search, filters, sort and draft across detail navigation. Respect browser Back/Forward and focus management. Navigation names should be based on user goals rather than database entities or engineering team structure.

**Pass:** Open a filtered list, inspect one item, go Back: the same filtered result set and relevant position return. Direct link opens a comprehensible page. **Fail:** all navigation resets users to a blank starting page.

## Contract 5: Comparison and decision surfaces

Show dimensions users must compare in a consistent and scannable structure. If many options exist, filtering and grouping should expose rather than conceal alternatives. Defaults should have a legitimate, explainable basis. Preserve access to infrequent but critical actions and expertise-oriented workflows.

**Pass:** Users select a defensible option and can describe why; they can find one intentionally rare option. **Fail:** one promoted option hides terms or appears to be the only available choice.

## Contract 6: Dialogs and overlays

Use standard modal semantics only for genuinely modal conditions. Place focus appropriately on open, maintain focus within genuinely modal dialog, provide an explicit close and Escape behavior where suitable, return focus to its logical trigger, and ensure background interaction cannot accidentally change state. For transient status use nonblocking feedback rather than a modal.

**Pass:** Keyboard-only opening, using, dismissing and returning to task succeeds. **Fail:** keyboard trap, focus jump to page top, unexpected loss of unsaved state.

## Contract 7: Loading, empty, failure and completion

Design each meaningful state intentionally. Empty lists should explain scope and next step; loading placeholders should reflect final layout and avoid jumps; failures should explain consequence and recoverability; completion should show truthful durable result. Alert urgency must reflect actual consequences. Animations need reduced-motion support.

**Pass:** Empty and failed states are testable without network, with clear user action; a result can be verified. **Fail:** silent blank page, undismissable toast, false progress indicator, cheerful but unsubstantiated completion animation.

## Contract 8: Accessibility and responsive layout

Choose relevant WCAG 2.2 criteria based on behavior. Check target size and spacing, zoom/reflow, keyboard, focus order, labels, headings, non-color cues and reduced motion. The 24x24 CSS pixel target rule (SC 2.5.8 AA) includes explicit exceptions and does not replace good target-size design. When the layout compresses, preserve semantic relationships and reading order.

**Pass:** Core task works keyboard-only, at a narrow viewport and substantial zoom with no crucial text clipped or unreachable. **Fail:** a redesigned visual arrangement changes keyboard order or detaches field error from its input.

Reference: https://www.w3.org/TR/WCAG22/ and https://www.w3.org/WAI/ARIA/apg/patterns/
