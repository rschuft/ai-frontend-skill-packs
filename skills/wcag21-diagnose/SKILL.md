---
name: wcag21-diagnose
description: Classify accessibility defects and user barriers against WCAG 2.1 success criteria and route to specialist repair skills. Use for a11y complaints, screenshots, inaccessible UI, keyboard/screen reader failures, or unclear compliance criteria.
---

# Diagnose an accessibility barrier under WCAG 2.1

**Load on demand**, not at every UI task. Standards authority comes from https://www.w3.org/TR/WCAG21/; installed `references/criteria.json` is an operational synthesis, not a replacement for normative criteria. Read `references/issue_taxonomy.json` first, then relevant entries in `references/criteria.json`. Consult `references/glossary-operational.json` for defined terms and `references/input-purposes.json` for the exact Section 7 inventory when relevant. Refer to `references/conformance.json` before asserting conformance.

## Method

1. Establish **user task** and evidence: route, component, state, device, viewport, input modality, assistive technology, steps to reproduce. A screenshot cannot verify keyboard behavior or accessibility tree.
2. Identify observed accessibility barrier. Assign **one primary** taxonomy category and relevant secondary category. Map only to SCs that can be supported by observed or reproducible evidence. Distinguish **confirmed failure**, **suspected failure requiring manual test**, **not applicable**, **not tested** and **pass**.
3. Check correct WCAG 2.1 level and criterion scope. Do not apply WCAG 2.2 additions as though they were in 2.1. Read W3C Understanding page for specific conditional exceptions, technology support and failures as needed; techniques are informative, not mandatory.
4. Use `references/cross_criterion_conflicts.json` for common misclassifications; select matching recipe(s) in `references/remediation_recipes.json`. Read matching specialist's `references/playbook.md` only when root cause is established or implementation requires it.
5. Propose repair with verification using **actual input and assistive technology** where needed. When evidence insufficient, propose a discriminator test rather than an invented failure.

## Output contract

`Finding ID | observed symptom | location/state | evidence vs inference | WCAG 2.1 SC (level) | classification | applicability | impact/priority | concrete repair | validation method | confidence`. For JSON, use `references/finding.schema.json`.

## Constraints

WCAG success criteria are normative; heuristics are not. Accessibility is not determined by aesthetics alone. No automation tool can certify a site. For HTML/XML, the 2025 WCAG 2.1 recommendation considers 4.1.1 always satisfied; report observed semantic damage against the relevant other criterion instead. Do not make legal compliance assertions from this pack.
