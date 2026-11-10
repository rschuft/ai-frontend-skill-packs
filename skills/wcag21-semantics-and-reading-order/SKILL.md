---
name: wcag21-semantics-and-reading-order
description: Fix WCAG 2.1 semantic HTML, headings, relationships, data tables, meaningful reading order and non-sensory instructions. Use for screen reader structure and DOM ordering defects.
---

# Structure and reading order

**Trigger:** Heading hierarchy, lists, tables, linear order, landmarks and semantic identification. **Diagnosis question:** Does presentation imply a relationship or sequence that is unavailable programmatically?

Primary WCAG 2.1 criteria: **1.3.1, 1.3.2, 1.3.3, 1.3.6**. See the detailed operational guidance in `references/playbook.md`. For every targeted SC, read the matching entry in `../wcag21-diagnose/references/criteria.json`, including its normative link, applicability/exception warning and method. A standard's original text always prevails over these notes.

## Procedure

1. Reproduce observed barrier on actual page/component, state, input modality and user task. Distinguish a confirmed fail from suspected fail or non-applicable SC.
2. Use playbook differential diagnosis to choose the specific requirement, not a catch-all accessibility label. Consult `../wcag21-diagnose/references/cross_criterion_conflicts.json` when several SCs appear related.
3. Implement the smallest robust remediation, preferring native semantics and accessible functionality over superficial ARIA or test suppression. Check normal, focused, disabled, loading and error states relevant to this feature.
4. Verify with criterion-specific steps from the catalog and playbook, including manual/assistive-technology checks where required. Record evidence and browser/AT context; automated tool output alone is not WCAG conformance proof.
5. For comprehensive review use `wcag21-review`; for implementation orchestration use `wcag21-build`; for post-change assurance use `wcag21-validate`.

## Failure discipline

A visual screenshot cannot confirm the accessibility tree or DOM reading order. Never label an item as a WCAG 2.1 failure from visual appearance alone when behavioral evidence is required. Distinguish A/AA/AAA and applicability exceptions. Report exact user harm, criterion ID, practical repair and test. Do not assert legal compliance.
