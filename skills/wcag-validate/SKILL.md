---
name: wcag-validate
description: Validate WCAG 2.2 (default) or 2.1 audit evidence with automated, keyboard, touch, zoom and assistive technology checks; detect incorrect version/level mixes and report incomplete manual reviews.
---

# Validate WCAG 2.x evidence and version-specific audit coverage

Resolve selected **WCAG 2.2 (default) or 2.1**, conformance level and scope before testing (`../wcag-diagnose/references/standard-selection.md`). A target-selection decision is not proof that the target was met.

1. Load the selected standard's `2.2/criteria.json` / `2.1/criteria.json` and conformance catalog. At **AA** review **55 criteria for 2.2** or **50 criteria for 2.1**. Do not mix versions or import 4.1.1 into 2.2.
2. For all required criteria, require `pass`, `fail`, `not_applicable`, `not_tested` or `needs_manual_review` with evidence and N/A rationale. Differentiate incomplete from failed.
3. Combine automated scanners with keyboard, zoom, responsive, touch/drag alternatives, focus-occlusion, forms, authentication, screen-reader, media and content reviews. Read `references/manual-and-automation.md` and the appropriate specialist playbook.
4. Retest affected complete processes and all relevant states; test the non-interference conditions (1.4.2, 2.1.2, 2.3.1, 2.2.2) even for third-party content.
5. If working in this distribution repository, run `python scripts/check_wcag_audit.py path/to/report.json --json`. The script rejects invalid version/criterion combinations and checks report structure only; in a consuming repository, obtain or implement equivalent tooling rather than assuming this distribution script was installed.
6. Report verified scope, environment, date, selected version/level, failures and missing manual coverage. Do not assert certification. **WCAG 3.0 Working Draft is advisory only** and may never receive A/AA/AAA conformance outcomes.
