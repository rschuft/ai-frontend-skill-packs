# Review evidence and prioritization

## Evidence classification

- **Observed:** A visible screenshot state, video or running UI confirms an interface property. This does not automatically establish the user consequence or causal mechanism.
- **Code-derived:** The source code shows behavior or constraints. Actual runtime and assistive technology behavior may differ.
- **Reported:** A user or stakeholder describes the problem. Treat as relevant but distinguish reports from reproducible observation.
- **Hypothesis:** A design heuristic suggests a risk; provide a simple way to test it instead of listing as confirmed defect.

Include `user goal + location + symptom + condition` in every finding. For example: `When adding a second address on a narrow viewport, the shipping label is visually closer to the billing field, causing ambiguity about which field is required.`

## Prioritize by consequences

Rank by severity, frequency, persistence, recoverability and affected population. A low-frequency security, data-loss, consent or assistive-technology blocker takes precedence over a highly visible cosmetic flaw. Distinguish quick fixes from architectural causes without turning the review into implementation scope creep.

## Avoid common review failures

- **Law bingo:** Do not cite eight psychology principles for a single misaligned label. Select the closest applicable mechanism and a test.
- **Assumed behavior:** Never claim that a button is broken based solely on its screenshot.
- **Beautiful means good:** Appearance preference is not task completion.
- **Novel means bad:** Novel navigation can suit exploration, but has a greater burden of validation for routine workflows.
- **Less means better:** Removing visible features may increase hidden work and expert navigation cost.
- **Performance means 400ms:** A heuristic is not a universal budget; identify actual acknowledgement and completion latency.
- **Forced best practice:** Observe product/user context before proposing broad redesign or new dependencies.

## Output order

Lead with the most harmful confirmed problem, not scores, charts or count summaries. For each issue, give affected task, evidence grade, candidate root cause, practical repair, counterargument/tradeoff and disconfirming test. Separate reproducible bugs, likely UX problems and exploratory hypotheses.
