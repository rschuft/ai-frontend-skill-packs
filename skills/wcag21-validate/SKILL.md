---
name: wcag21-validate
description: Validate WCAG 2.1 fixes and audit evidence with automation plus keyboard, visual, assistive technology and end-to-end process tests. Use for regression testing, release gates, accessibility sign-off and checking whether an audit result supports an A/AA/AAA claim.
---

# Validate WCAG 2.1 evidence, not just scanners

1. Define WCAG **2.1** level and scope, user tasks, browser/AT combinations and responsive states. Read `../wcag21-diagnose/references/conformance.json` and `references/manual-and-automation.md`.
2. For each criterion at target level, classify `pass`, `fail`, `not_applicable`, `not_tested`, or `needs_manual_review` with evidence; require documented reason for not applicable. Absence of known failures does not constitute a pass.
3. Use **automation** for candidate structural failures, labels and some contrast checks; use **manual** keyboard, screen reader, media equivalence, text scaling, timeout, error and context behavior tests. Automated checks are incomplete by design.
4. Retest exact failure steps, state transitions and downstream processes after each fix. Check non-interference conditions (1.4.2, 2.1.2, 2.3.1, 2.2.2), including third-party content.
5. Run `scripts/check_audit.py` from the extracted pack on a structured audit report for **completeness**, not for automated certification. It refuses to call partial or unsupported result conformant.

## Release language

Report: `Verified in [scope, browser, AT, device, date] against [SC]`, `Needs manual review`, or `Not tested`. Do not say `WCAG compliant` from linting or single-sample tests; formal conformance requires full pages, complete processes, supported technology and non-interference.
