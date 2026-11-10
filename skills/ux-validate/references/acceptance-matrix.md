# Task-based acceptance matrix

These are **test designs**, not claimed results. Select cases based on the changed component or user journey. Record environment and expected versus observed outcomes.

| Case | Setup / stimulus | Required observation |
| --- | --- | --- |
| First-use | Fresh state; user asked to achieve a real goal without a tour | Primary task and next action are discoverable without prior instruction |
| Expert path | Returning state; common repeated action | No forced training or unnecessary intermediate screens; shortcuts remain viable |
| Decision | Many comparable options; one atypical valid choice | Users can compare, select and locate the uncommon option without misinterpreting promotion as restriction |
| Memory | Read an item, change page and return | Prior search, filters, selection and task context persist |
| Pointer | Narrow viewport, adjacent controls, touch-capable device | Correct hit areas and no accidental destructive action |
| Keyboard | Tab through and activate every relevant control | Expected activation, visible focus, appropriate order, no trap |
| Screen reader | Labels and state changes on relevant controls | Correct name, role, value and field-error association; timely but not redundant announcements |
| High zoom | 200%+ zoom and narrow layout | Meaningful grouping, content and actions remain readable and reachable |
| Reduced motion | OS/browser reduced-motion preference | Essential state shown without motion dependence |
| Invalid input | Benign formatting variations and actual invalid values | Accepted input normalized safely; errors guide correction and preserve entries |
| Slow network | Delay action response; submit twice | Immediate acknowledgement, truthful status and no unintended duplicate mutation |
| Out-of-order | Two search/filter queries return in reverse sequence | Older result cannot overwrite newer selection |
| Failure | Timeout, error, offline or rejected action | User can tell what happened, what remains uncertain and how to recover safely |
| Interruption | Save partial work, navigate away and return | Resume or discard is explicit; no false saved promise |
| Irreversible action | Payment, publish, permission or deletion | Consequence understood before commit; real final result confirmed afterward |
| Empty state | No items, no permission or exhausted filter | Explanation matches state and provides appropriate next action |
| Consent | Decline permission or plan; attempt reversal | Refusal is accessible and truthful; cancellation or revocation does not require deception-defeating workarounds |

## Interpreting evidence

Automated component tests are evidence of specified behavior, not full usability. Axe-like tooling can detect some accessibility issues, but hands-on keyboard and assistive technology verification remains necessary. A screenshot proves visual state only; it cannot prove server success, click behavior or focus order. Qualitative user tests can reveal wrong assumptions that code-based tests never cover.

For each test: `case ID, surface, device/browser, user role, preconditions, steps, expected result, observed result, pass/fail/untested, evidence artifact`. For a failed case, attach the original UX issue ID so a fix can be traced to its intended outcome.
