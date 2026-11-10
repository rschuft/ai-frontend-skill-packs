# System feedback, latency and asynchronous state

## Diagnose the wait

Separate time-to-acknowledgement from time-to-result. A 5-second operation that acknowledges instantly and communicates progress may be usable; a 300 ms operation with no visible state may feel broken. Record action, visible response, network conditions, result certainty, and whether users retry.

## UI state model

Define `idle -> pending -> succeeded | failed | cancelled | unknown` transitions (adapt to actual task). Make each state distinguishable visually and semantically. Confirmation should describe *what happened*, not simply show a toast. For irreversible changes, ensure durable persistence before claiming success.

## Remediation

1. **Immediate acknowledgement:** Show pressed/pending state on initiation. Keep action label and subject visible; disable duplicates only when necessary and provide a safe exit.
2. **Progress:** For bounded work, use true determinate progress. For uncertain work, state current stage and realistic wait without fabricated percentages. Use skeletons only when they match eventual content and prevent layout shift.
3. **Continuity:** Preserve selection, query and scroll context. Avoid modal progress blocking unrelated work unless the workflow genuinely requires a lock.
4. **Completion:** Provide clear success, where result went, and next action. State if an operation is still pending/queued versus complete.
5. **Error recovery:** Give a plain explanation, preserve draft, suggest safe retry where supported, expose reconciliation when state is uncertain.
6. **Performance:** Measure at interaction and network layers; optimize long tasks, streaming, caching and rendering before compensating with animation.

## Anti-patterns

Doherty's 400ms threshold is a historical usability heuristic, not a universal hard SLA. Purposefully delaying a fast result to seem trustworthy, showing artificial progress as real, dismissing success before persistence, or looping a spinner without state are unacceptable substitutes for accuracy. Animation must respect reduced-motion settings.

## Tests

Inspect rapid taps, double submits, timeouts, offline/online transitions, cancellation, stale requests, out-of-order responses, duplicate confirmations and screen-reader announcements. Track acknowledgement latency and successful task completion separately. Failure paths are as important as success paths.

Sources: https://lawsofux.com/doherty-threshold/ ; https://lawsofux.com/goal-gradient-effect/ ; https://lawsofux.com/selective-attention/ ; https://lawsofux.com/articles/2020/ux-psychology-google-search/
