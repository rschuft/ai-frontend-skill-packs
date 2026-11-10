---
name: wcag21-assistive-tech-and-status
description: Fix WCAG 2.1 accessible names, roles, values, control states and dynamic live status messages; interpret the updated 4.1.1 Parsing note. Use for ARIA, assistive technology and async UI defects.
---

# Assistive technology semantics and asynchronous status

**Trigger:** Accessible names, roles, values, ARIA states and live status messages. **Diagnosis question:** Does an assistive technology user lack programmatically available UI state or status?

Primary WCAG 2.1 criteria: **4.1.1, 4.1.2, 4.1.3**. See the detailed operational guidance in `references/playbook.md`. For every targeted SC, read the matching entry in `../wcag21-diagnose/references/criteria.json`, including its normative link, applicability/exception warning and method. A standard's original text always prevails over these notes.

## Procedure

1. Reproduce observed barrier on actual page/component, state, input modality and user task. Distinguish a confirmed fail from suspected fail or non-applicable SC.
2. Use playbook differential diagnosis to choose the specific requirement, not a catch-all accessibility label. Consult `../wcag21-diagnose/references/cross_criterion_conflicts.json` when several SCs appear related.
3. Implement the smallest robust remediation, preferring native semantics and accessible functionality over superficial ARIA or test suppression. Check normal, focused, disabled, loading and error states relevant to this feature.
4. Verify with criterion-specific steps from the catalog and playbook, including manual/assistive-technology checks where required. Record evidence and browser/AT context; automated tool output alone is not WCAG conformance proof.
5. For comprehensive review use `wcag21-review`; for implementation orchestration use `wcag21-build`; for post-change assurance use `wcag21-validate`.

## Failure discipline

Do not classify ordinary HTML validation defects as failures of WCAG 2.1 SC 4.1.1. Never label an item as a WCAG 2.1 failure from visual appearance alone when behavioral evidence is required. Distinguish A/AA/AAA and applicability exceptions. Report exact user harm, criterion ID, practical repair and test. Do not assert legal compliance.
