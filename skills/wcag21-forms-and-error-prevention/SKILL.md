---
name: wcag21-forms-and-error-prevention
description: Fix WCAG 2.1 input purpose/autocomplete, form labels, visible error text, correction suggestions, safe submission confirmation and help. Use for accessible form building and error recovery.
---

# Forms, input help and error prevention

**Trigger:** Field purposes, instructions, identified errors, correction advice, review and reversal. **Diagnosis question:** Can users identify required inputs, repair errors and avoid irreversible submissions?

Primary WCAG 2.1 criteria: **1.3.5, 3.3.1, 3.3.2, 3.3.3, 3.3.4, 3.3.5, 3.3.6**. See the detailed operational guidance in `references/playbook.md`. For every targeted SC, read the matching entry in `../wcag21-diagnose/references/criteria.json`, including its normative link, applicability/exception warning and method. A standard's original text always prevails over these notes.

## Procedure

1. Reproduce observed barrier on actual page/component, state, input modality and user task. Distinguish a confirmed fail from suspected fail or non-applicable SC.
2. Use playbook differential diagnosis to choose the specific requirement, not a catch-all accessibility label. Consult `../wcag21-diagnose/references/cross_criterion_conflicts.json` when several SCs appear related.
3. Implement the smallest robust remediation, preferring native semantics and accessible functionality over superficial ARIA or test suppression. Check normal, focused, disabled, loading and error states relevant to this feature.
4. Verify with criterion-specific steps from the catalog and playbook, including manual/assistive-technology checks where required. Record evidence and browser/AT context; automated tool output alone is not WCAG conformance proof.
5. For comprehensive review use `wcag21-review`; for implementation orchestration use `wcag21-build`; for post-change assurance use `wcag21-validate`.

## Failure discipline

Submission safeguards have defined scopes at AA versus AAA. Never label an item as a WCAG 2.1 failure from visual appearance alone when behavioral evidence is required. Distinguish A/AA/AAA and applicability exceptions. Report exact user harm, criterion ID, practical repair and test. Do not assert legal compliance.
