---
name: security-review
description: "Audit frontend and associated API or service security against an explicit OWASP ASVS 5.0.0 level, with threat-boundary evidence, vulnerability triage and NIST SSDF practice alignment. Use for application security reviews and PR audits."
---

# Review application security against a selected baseline

## Scope

Use for an application security review or conformance-gap assessment covering code, browser, APIs, identity, deployment and relevant upstream services. A frontend-only review is limited-scope by definition. No penetration test is authorized merely because a review was requested.

## Procedure

1. Declare application, environment, component and trust-boundary scope, protected assets, identities, explicit permission for tools and chosen ASVS version/level; consult `../security-diagnose/references/standard-selection.md`.
2. Build a requirement ledger from `../security-diagnose/references/asvs/5.0.0/index.json` filtered at the selected cumulative level. Resolve the meaning of each applicable requirement from the pinned official ASVS 5.0.0 source.
3. Inspect code/configuration and available scans, API and identity controls; load only relevant specialists. Independently evaluate higher-risk trust boundaries and NIST SSDF process gaps if requested.
4. For every selected requirement record pass, fail, not applicable, not tested or needs manual verification. Require reproducible evidence for pass/fail and a documented rationale for not applicable; never infer from UI appearance or a clean scanner report.
5. Prioritize verified findings by plausible impact and exposure; include owner, remediation and independent retest plan. Use WSTG 4.2 only for explicitly authorized testing methodology.
6. Validate machine-readable assessment completeness using `security-validate` or the distribution-side audit checker. Report incomplete coverage and untested controls rather than claiming certification.

## Deliverable

Include the assessment scope, baseline/version/level, evidence sources and dates, per-requirement ledger, risk-prioritized findings, test limitations, and a short statement of what remains unknown. Security ratings are context-dependent, not derived solely from ASVS levels.
