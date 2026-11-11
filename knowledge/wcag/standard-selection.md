# Selecting WCAG standards and levels

This policy governs all version-independent `wcag-*` skills. WCAG 2.1 and 2.2 are separate conformance catalogs; WCAG 3.0 is research-only.

## Deterministic order

1. **Explicit task/contract**: honor a named WCAG version and level, such as WCAG 2.1 AA. Do not infer requirements from jurisdiction or platform.
2. **Project policy**: if not explicit, use `.frontend-a11y.json` from the consuming project's root (if present), or unambiguous written project/`AGENTS.md` policy. If those conflict, ask/record an explicit resolution before asserting conformance.
3. **Default**: WCAG **2.2 AA** for new work, clearly labeled a *planning fallback*, not a universal legal requirement.

Project policy example (optional file in **consuming** project; the distribution does not create it):

```json
{ "standard": "WCAG 2.2", "level": "AA", "wcag3_advisory": false }
```

If you can execute Python in the distribution checkout, `python scripts/resolve_wcag_target.py --project /path/to/app --json` resolves that file; `--task-standard 'WCAG 2.1' --task-level AA` overrides it. This helper does **not** parse natural-language prompts or `AGENTS.md`; the agent must pass extracted explicit requirements and resolve contradictory prose before formal reporting. A skills-only installation includes this written policy but not necessarily the executable script.

## Authoritative catalogs and levels

| Selected target | Catalog | A | A+AA | A+AA+AAA |
|---|---|---:|---:|---:|
| WCAG 2.1 | `2.1/criteria.json` | 30 | 50 | 78 |
| WCAG 2.2 | `2.2/criteria.json` | 31 | 55 | 86 |

For 2.1, retain historical **4.1.1 Parsing** in the 78-item inventory; W3C's updated 2.1 text considers it always satisfied for HTML/XML. For 2.2, **omit 4.1.1** and include nine new criteria at their designated levels. Never blend requirement sets or change target mid-audit without recording an explicit new assessment.

WCAG **3.0** (Working Draft dated 2026-09-10) is **not** a normative conformance target: no A/AA/AAA mapping, no pass/fail certification, no substitution for 2.x. Only use `3.0/draft-guidance.json` when requested explicitly for research or when `wcag3_advisory: true` adds a distinct appendix; include snapshot date and draft caveat.

For any audit, output selected version, level, selection source, scope, criteria coverage, actual test methods and unresolved manual work. W3C Recommendations override synthesized catalog guidance if discrepancies arise; W3C Understanding and Techniques are informative.
