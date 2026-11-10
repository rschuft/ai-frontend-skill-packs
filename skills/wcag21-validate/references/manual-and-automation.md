# Accessibility validation: coverage vs evidence

## Test ladder

1. **Static/in-memory unit checks:** source analysis for missing labels, forbidden components, contract tests for state transitions; fast but limited.
2. **DOM and browser automation:** axe-core / Accessibility Insights / Playwright accessibility queries for candidate problems, roles, names, focus state, some CSS contrast and reflow metrics; record versions and rule IDs. Automated rule coverage is *not* success-criterion coverage.
3. **Manual browser-only:** keyboard-only flow, focus visibility, zoom, text spacing override, pointer cancellation, reduced motion, moving content, error recovery and page-level semantics.
4. **Assistive technology:** screen reader/browser interaction; verify meaning, state, announcements and reading order. Test AT combinations that users actually rely upon; do not assume any one pairing covers all.
5. **Content expert / human judgment:** equivalent alternatives for media and diagrams, linguistic purpose, captions quality, context changes, process completeness and exceptions.
6. **Conformance review:** full pages, complete processes, accessibility-supported ways of using relied-upon technology, non-interference and accurate scope statement.

## Common falsifications

- “axe found zero violations” => only automated rules passed for inspected states.
- “Lighthouse 100” => not a formal WCAG 2.1 conformance assessment.
- “All images have alt” => not proof that the alternatives mean the right thing.
- “Controls have roles” => not proof that keyboard interaction and user-facing state match.
- “Color contrast meets 4.5” => not proof that color alone is unused or non-text cues meet 3:1.
- “We tested desktop” => not evidence at 320 CSS px, 200% text resize, mobile touch and screen reader combinations.
- “Scanning returned no 4.1.1 errors” => WCAG 2.1 2025 considers 4.1.1 always satisfied for HTML/XML; actual affected accessibility semantics remain important.

## A structured audit gate

The supplied `scripts/check_audit.py` requires a report describing version, level, scope, and per-criterion outcomes. It rejects unknown or missing criteria, undocumented N/A, and unsupported declarations. Its `coverage_complete` means every in-scope criterion has a determinate result (including failure), **not** that a website conforms. A report is **eligible_for_independent_conformance_review** only when every expected criterion is a substantiated pass or N/A and all five conformance requirement reviews are explicitly complete; even then the script cannot verify truthfulness, representativeness or accessibility support.

Use the structured format in `evaluation/sample-audit.json` and check the included README for CLI invocation. The scanner cannot itself interact with browser, mobile device or assistive technology.
