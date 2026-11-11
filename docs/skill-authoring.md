# Skill authoring convention

All 56 `skills/*/SKILL.md` files use the same top-level layout. The skill's job determines its content, not its heading names.

## Required layout

```markdown
---
name: ux-review
description: "Review frontend interfaces and produce evidence-based findings for a specific user task."
---

# Review a user interface

## Scope

State the task boundary, relevant context, how to choose this skill and when to use another skill.

## Procedure

1. Identify evidence and applicable references.
2. Diagnose or implement the smallest relevant changes.
3. Verify results and state what remains untested.
```

## Frontmatter

- Use exactly `name` and `description`, in that order. `name` must match the skill directory.
- Double-quote `description` as a JSON string. JSON string syntax is a YAML-compatible subset. Escape embedded double quotes and backslashes as needed.
- Keep the description focused on **discovery**: relevant user tasks and observable triggers. It must exactly match the plain-text description in `manifest.json`.
- Do not put activation rules solely in the body. The agent discovers the description before reading the skill content.

## Body structure

- Use exactly one H1 title, followed by `## Scope` and then `## Procedure`. These are the only required H2 sections.
- **Scope** states applicability, limits, assumptions and routing between related skills. It should not simply repeat the description.
- **Procedure** contains the decision path, evidence collection, implementation or review steps, relevant recipes, and verification expectations.
- Add optional H2 sections such as `## Output`, `## Evidence`, `## Boundaries`, `## Failure discipline` and `## Related workflows` only where they communicate genuinely distinct information.
- Keep specialist playbooks and catalogs in `references/`. Read them selectively rather than copying entire catalogs into `SKILL.md`.
- Preserve the distinction between WCAG normative requirements, ASVS security requirements, NIST process guidance, UX heuristics and aesthetic judgment. Never imply a screenshot or automated scan proves WCAG conformance or application security. Security pass/fail assessments require authorized scope and independently checkable evidence.

## Checks

The Python validator uses the standard library to enforce YAML-compatible quoted descriptions and canonical headings. The separate Markdown linter catches Markdown style errors. Both run in CI.

```bash
python scripts/validate_pack.py
python -m unittest discover -s scripts -p 'test_*.py' -v
npx --yes markdownlint-cli2@0.24.0 "skills/**/SKILL.md" "docs/skill-authoring.md" "CONTRIBUTING.md"
```

Markdown linting is a repository contributor check. Neither Node.js nor markdownlint is needed to install or use the skills.
