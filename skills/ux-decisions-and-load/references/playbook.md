# Decision complexity and cognitive load: remediation playbook

## Diagnose root cause

Separate **too many alternatives** from **too much recall**, **opaque distinctions**, **unnecessary steps**, and **inherent domain complexity**. Record the user's actual decision, not merely the number of controls. Ask whether an expert is intentionally viewing a dense overview. A larger but well-grouped choice set can be faster than an opaque sequence of dropdowns.

- **Choice overload / Hick:** user cannot discriminate alternatives. Inspect labels, comparison attributes, obvious defaults, search, filtering and whether variants matter to user goals.
- **Working memory / Miller / chunking:** user must remember an earlier value, search term, list position, or instruction. Look for missing summaries, retained query, side-by-side comparisons and meaningful groups.
- **Cognitive load / Occam:** users expend attention on decorative content, contradictory instructions or extra confirmations. Separate necessary security, informed choice, and validation steps from gratuitous UI.
- **Tesler:** the workflow asks users to do calculations, repeat known data, reconcile states or transform formats the software could handle transparently.

## Repair patterns

1. **Prioritize by intent.** Put the user's most common or critical action in its decision context; subordinate secondary actions without making them undiscoverable. Use action verbs and task-language, not internal modules.
2. **Group before hiding.** Create named conceptual groups; keep mutually comparable alternatives visible together. If there are too many, support filtering, sorting and side-by-side comparison. Measure findability after grouping.
3. **Externalize memory.** Preserve query, filters, selected entity, progress and input summaries across navigation. Use review screens for irreversible decisions and keep them editable.
4. **Offload safe work.** Derive defaults from reliable user or system state, prefill known fields, autocomplete cautiously, validate inline, and mark which values were inferred. Make correction straightforward.
5. **Progressively disclose with a path back.** Hide specialist controls only when the typical task remains complete and users can find advanced features. Avoid seven-step wizards just to reduce items per screen.
6. **Reduce decoration, not clarity.** Prefer labels over cryptic icons. Clear helper text may increase word count while reducing cognitive effort.

## Implementation details

Represent core task, current step and validation state in one stable data model. Preserve draft state during back/forward navigation and interruptions. Reuse layout/field components for consistent semantics. Avoid silent destructive defaults or changing selections when filters update. For AI-suggested answers, show assumption/provenance and affordances to inspect or override.

## Differentiating tests

- First-time users: time to first correct choice, comparison comprehension, misselection, abandonment.
- Experts: common-task latency, keyboard access, shortcut discoverability, ability to bypass unnecessary steps.
- Interruption test: switch away mid-task, return, identify task context and continue without recalling hidden values.
- Adaptive layouts: narrow viewports must not split a single comparison into misleading fragments.

## Conflict / misuse guards

Miller's Law does not mandate 7 items. Hick's Law does not require fewer options when option quality or expert scanning would suffer. Occam's Razor does not justify hiding information. Tesler's Law does not excuse black-box automation. Use actual user outcomes to decide which technique fits.

Source lenses: https://lawsofux.com/choice-overload/ ; https://lawsofux.com/hicks-law/ ; https://lawsofux.com/cognitive-load/ ; https://lawsofux.com/teslers-law/ ; https://lawsofux.com/articles/2015/design-principles-for-reducing-cognitive-load/ ; https://lawsofux.com/articles/2024/teslers-law/
