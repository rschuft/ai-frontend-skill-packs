# WCAG source authority and method

**Reviewed 2026-11-10.** This repository supports **WCAG 2.2 (default)** and **WCAG 2.1 (explicit legacy target)** as separate W3C Recommendation inventories. It also provides a dated **WCAG 3.0 Working Draft** research reference, not a conformance target.

| Version | Status | Canonical source | Local authoritative-index synthesis |
| --- | --- | --- | --- |
| 2.1 | W3C Recommendation, updated 2025-05-06 | https://www.w3.org/TR/WCAG21/ | `2.1/criteria.json` (78, including historically listed 4.1.1), `2.1/conformance.json` |
| 2.2 | W3C Recommendation, updated 2024-12-12 | https://www.w3.org/TR/WCAG22/ | `2.2/criteria.json` (86), `2.2/conformance.json` |
| 3.0 | **Working Draft 2026-09-10** | https://www.w3.org/TR/2026/WD-wcag-3.0-20260910/ | `3.0/draft-guidance.json` advisory summary only |

W3C explains nine new criteria in https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/ . 2.2 removes 4.1.1 Parsing. The current 2.1 recommendation describes 4.1.1 as always satisfied for HTML/XML; accessibility problems should still be reported under their actual affected criteria. WCAG 2.2 has 31 A, 24 AA and 31 AAA criteria; AA cumulative total is 55. 2.1 has 30 A, 20 AA and 28 AAA; AA cumulative total is 50.

## Information architecture

`standards.json` and `standard-selection.md` establish the deterministic target-selection policy. `issue_taxonomy.json`, `remediation_recipes.json` and `cross_criterion_conflicts.json` cover the **union** of applicable cases; classifiers must filter by the selected *version and level*. `3.0/draft-guidance.json` is only an optional, dated advisory lens. The 14 `wcag-*` skills are version-independent and share this version-aware catalog. No installed-skill migration or compatibility aliases are provided.

## Supplementary guidance (informative)

- Understanding WCAG 2.2: https://www.w3.org/WAI/WCAG22/Understanding/ — criterion intent, applicability, exceptions, examples, common failures.
- Techniques for WCAG 2.2: https://www.w3.org/WAI/WCAG22/Techniques/ — technology-specific sufficient/advisory techniques and examples; **not mandatory technical implementations**.
- Understanding WCAG 2.1: https://www.w3.org/WAI/WCAG21/Understanding/ ; Techniques: https://www.w3.org/WAI/WCAG21/Techniques/ .
- WCAG-EM methodology: https://www.w3.org/WAI/test-evaluate/conformance/wcag-em/ — scope, sampling, evaluation and reporting considerations.
- WAI-ARIA APG: https://www.w3.org/WAI/ARIA/apg/patterns/ — optional implementation patterns, not itself a replacement for normative criteria.
- WCAG 3.0 explainer: https://www.w3.org/WAI/standards-guidelines/wcag/wcag3-intro/ . The draft may change; do not import proposed conformance models into WCAG 2.x claims.

**Method/limits:** The criterion catalogs contain original operational summaries with symptoms, remediation, verification guidance, caveats, and canonical W3C links. The supporting Understanding, Techniques, ACT and glossary libraries are **not** mirrored wholesale. W3C Recommendations, not these derivative summaries, determine conformance. Browser/assistive technology testing and human assessment remain necessary; running a scanner or the included JSON coverage checker is not certification. No jurisdiction-specific legal compliance is inferred.

**Attribution:** W3C source publications remain W3C material; see https://www.w3.org/copyright/ . Original operational syntheses and links are supplied without W3C endorsement, copyrighted logos, or verbatim full standards text.
