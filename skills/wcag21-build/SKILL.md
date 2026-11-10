---
name: wcag21-build
description: Implement accessible web UI components and flows against WCAG 2.1 A/AA/AAA requirements. Use while coding forms, dialogs, navigation, menus, responsive layouts, media, live regions, keyboard behavior or design-system components.
---

# Build or repair WCAG 2.1-accessible UI

Start from the user task and concrete component behavior. Unless another target is specified, design for **WCAG 2.1 AA** plus meaningful usability beyond the minimum; do not imply an achieved conformance claim.

1. Determine relevant WCAG SCs from `../wcag21-diagnose/references/criteria.json`, and use `../wcag21-diagnose/references/remediation_recipes.json` for fixes. Load the matching specialist `references/playbook.md` only as needed. Prefer native semantic HTML over ARIA imitation.
2. Implement all states, not a static mock: empty/default/hover/focus/expanded/selected/loading/error/success, keyboard navigation and reversal, assistive-tech announcements, responsive reflow and timeout recovery where relevant.
3. Use patterns in `references/implementation-contracts.md`; pair each change with test assertions at the relevant SC, including a manual test when automated verification is insufficient. Avoid hard-coded sizes that clip under zoom or text-spacing overrides.
4. Run narrowly targeted unit/component tests first; use browser tests for navigation, dynamic behavior and computed accessible names; reserve live screen-reader and cross-device checks for meaningful paths. Do not hide gaps by adding broad ignore rules to axe-core.
5. Confirm that an accessibility fix does not break task behavior, semantics, security, user consent or error recovery.

## Done means

Implementation matches intent, relevant known failures are repaired, new regressions are tested, outstanding AT/manual tests are disclosed and no unsupported conformance certificate is issued. If making a PR, describe exact criteria, evidence and remaining verification work.
