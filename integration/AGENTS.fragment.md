## Frontend UX, accessibility, visual design and application security skills

For a frontend UI task, select only relevant project-installed skills. All four families can contribute to one work item but have different authority:

- **UX / behavior:** ambiguous usability, navigation, interaction, task completion → `ux-diagnose`, `ux-review`, `ux-build`, `ux-validate` and a matching `ux-*` specialist.
- **Accessibility / conformance:** barriers, semantics, keyboard, zoom, contrast, assistive technology → `wcag-diagnose`, `wcag-review`, `wcag-build`, `wcag-validate` and matching `wcag-*` specialist.
- **Visual composition / aesthetics:** hierarchy, balance, color theory, typography, spacing, imagery, art direction, design tokens → `design-diagnose`, `design-review`, `design-build`, `design-validate` and matching `design-*` specialist.
- **Application security:** authentication, authorization, untrusted content, browser origin policy, tokens, API trust boundaries, secrets, supply chain → `security-diagnose`, `security-review`, `security-build`, `security-validate` and matching `security-*` specialist.
- **Cross-cutting work:** classify each observation once, attach the different evidence lenses, and apply the smallest coherent repair. Review affected visual states, user tasks, and normative accessibility checks independently.

**Precedence:** security/safety requirements, honest behavior and user consent; specified accessibility requirements; verified UX needs and existing brand/system constraints; then aesthetic heuristics. Select WCAG version and level using explicit task/contract > consuming-project `.frontend-a11y.json` or unambiguous project policy > WCAG 2.2 AA planning default; WCAG 2.1 remains explicit compatibility. WCAG 3.0 is an opt-in, dated Working Draft advisory only, never a conformance target. Resolve policy conflicts and pin the criterion set. WCAG 2.2 AA is a planning fallback unless target scope differs, not a universal legal requirement or certificate. Heuristics such as 60/30/10, golden ratio, one focal point and color psychology are suggestions, not standards. Never imply visual design alone proves WCAG conformance or user success. Read only relevant skill references rather than all catalogs.


**Security baseline:** explicit task/contract > consuming-project `.frontend-security.json` or unambiguous policy > ASVS 5.0.0 Level 2 planning fallback. Require assessment scope, trust boundaries and exact official requirement text before pass/fail claims. OWASP Top 10:2025 is risk awareness; WSTG 4.2 supports authorized testing; NIST SSDF 1.1 is process alignment. No active probing of external or production systems without authorization, no invented evidence or certification. Client checks are not server authorization.
