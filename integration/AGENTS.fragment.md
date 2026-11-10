## Frontend UI/UX and accessibility skills

When implementing, changing, assessing, or validating a user-facing interface, select the appropriate project-installed skills instead of loading the entire pack:

- Unclear usability problem or surprising behavior → `ux-diagnose` → relevant `ux-*` specialist; evidence-based interface critique → `ux-review`.
- Accessibility complaint or barrier → `wcag21-diagnose` → relevant `wcag21-*` specialist; accessibility audit → `wcag21-review`.
- Design or code changes → `ux-build` and applicable `wcag21-build` guidance; post-change testing → `ux-validate` and `wcag21-validate`.
- When the issue implicates both usability and accessibility, use both families and one shared finding, but do **not** equate heuristics with mandatory success criteria.

Favor native HTML semantics; observable task outcomes; keyboard, pointer, zoom, and relevant assistive-technology verification. Assign explicit WCAG 2.1 criteria and levels when applicable. Treat WCAG 2.1 success criteria as the authoritative requirement for a WCAG 2.1 audit; user-consent, safety, truthful interaction state, and accessibility override purely aesthetic/conversion heuristics. Do not silently add 2.2-only criteria; use WCAG 2.1 AA as a planning assumption only absent an explicit scope/level. A clean automated scan never establishes full conformance. Only reference sources and specialist playbooks relevant to the observed problem; do not load every skill.
