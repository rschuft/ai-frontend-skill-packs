---
name: wcag21-keyboard-and-focus
description: Fix WCAG 2.1 keyboard parity, traps, focus order and visibility, single-character shortcuts, dialogs and custom widget keys. Use for keyboard-only failures and inaccessible focus behavior.
---

# Keyboard operation and focus

**Trigger:** Keyboard parity, traps, shortcuts, focus order, visible focus. **Diagnosis question:** Can users complete the operation with keyboard only and determine where focus is?

Primary WCAG 2.1 criteria: **2.1.1, 2.1.2, 2.1.3, 2.1.4, 2.4.3, 2.4.7**. See the detailed operational guidance in `references/playbook.md`. For every targeted SC, read the matching entry in `../wcag21-diagnose/references/criteria.json`, including its normative link, applicability/exception warning and method. A standard's original text always prevails over these notes.

## Procedure

1. Reproduce observed barrier on actual page/component, state, input modality and user task. Distinguish a confirmed fail from suspected fail or non-applicable SC.
2. Use playbook differential diagnosis to choose the specific requirement, not a catch-all accessibility label. Consult `../wcag21-diagnose/references/cross_criterion_conflicts.json` when several SCs appear related.
3. Implement the smallest robust remediation, preferring native semantics and accessible functionality over superficial ARIA or test suppression. Check normal, focused, disabled, loading and error states relevant to this feature.
4. Verify with criterion-specific steps from the catalog and playbook, including manual/assistive-technology checks where required. Record evidence and browser/AT context; automated tool output alone is not WCAG conformance proof.
5. For comprehensive review use `wcag21-review`; for implementation orchestration use `wcag21-build`; for post-change assurance use `wcag21-validate`.

## Failure discipline

Passing a Tab smoke test does not prove keyboard interaction patterns function. Never label an item as a WCAG 2.1 failure from visual appearance alone when behavioral evidence is required. Distinguish A/AA/AAA and applicability exceptions. Report exact user harm, criterion ID, practical repair and test. Do not assert legal compliance.
