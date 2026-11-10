---
name: wcag21-pointer-and-touch
description: Fix WCAG 2.1 touch/gesture alternatives, pointer cancellation, voice-visible label matching, motion activation, AAA 44px targets and concurrent inputs. Use for mobile and pointer access problems.
---

# Pointer, touch and motion input

**Trigger:** Gesture alternatives, cancellation, visible label alignment, target size, motion sensors. **Diagnosis question:** Is an alternative input route missing or a pointer target difficult to operate?

Primary WCAG 2.1 criteria: **2.5.1, 2.5.2, 2.5.3, 2.5.4, 2.5.5, 2.5.6**. See the detailed operational guidance in `references/playbook.md`. For every targeted SC, read the matching entry in `../wcag21-diagnose/references/criteria.json`, including its normative link, applicability/exception warning and method. A standard's original text always prevails over these notes.

## Procedure

1. Reproduce observed barrier on actual page/component, state, input modality and user task. Distinguish a confirmed fail from suspected fail or non-applicable SC.
2. Use playbook differential diagnosis to choose the specific requirement, not a catch-all accessibility label. Consult `../wcag21-diagnose/references/cross_criterion_conflicts.json` when several SCs appear related.
3. Implement the smallest robust remediation, preferring native semantics and accessible functionality over superficial ARIA or test suppression. Check normal, focused, disabled, loading and error states relevant to this feature.
4. Verify with criterion-specific steps from the catalog and playbook, including manual/assistive-technology checks where required. Record evidence and browser/AT context; automated tool output alone is not WCAG conformance proof.
5. For comprehensive review use `wcag21-review`; for implementation orchestration use `wcag21-build`; for post-change assurance use `wcag21-validate`.

## Failure discipline

WCAG 2.1 AAA 44x44 target size differs from WCAG 2.2 AA rule. Never label an item as a WCAG 2.1 failure from visual appearance alone when behavioral evidence is required. Distinguish A/AA/AAA and applicability exceptions. Report exact user harm, criterion ID, practical repair and test. Do not assert legal compliance.
