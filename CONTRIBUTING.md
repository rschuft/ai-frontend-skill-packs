# Contributing to AI Frontend Skill Packs

This repository publishes reusable **agent skills** for UX, accessibility, visual design, and application security. Contributions should improve what agents can diagnose, implement, or verify—not merely expand a list of design opinions.

## Repository layout

```text
skills/                       56 canonical SKILL.md directories (14 per family)
knowledge/ux-laws/            Laws, articles, classification, recipes, and schemas
knowledge/wcag/               Shared taxonomy and recipes; 2.1/2.2 normative catalogs, 3.0 draft research
knowledge/visual-design/      Principles, elements, articles, Gestalt, and recipes
knowledge/security/           ASVS 5.0.0 index, security taxonomy, recipes, and mappings
integration/                  Optional routing guidance for consuming projects
evaluation/                   Classification and skill-invocation scenarios
scripts/install.py            Offline installation into Claude Code and Codex projects
scripts/resolve_wcag_target.py  WCAG standard/level selection
scripts/check_wcag_audit.py   WCAG report coverage checker (not certification)
scripts/resolve_security_target.py  OWASP ASVS baseline/level selection
scripts/check_security_audit.py    ASVS report completeness checker (not certification)
scripts/validate_pack.py      Skill catalog, metadata, and reference consistency checks
scripts/test_pack.py          Installer and WCAG audit regression tests
scripts/test_security_pack.py Security policy and audit regression tests
manifest.json                Machine-readable skill registry
NOTICE.md                     Third-party attribution and license boundaries
```

`skills/` is the canonical publication source. The `.claude/skills/` and `.agents/skills/` directories in consuming applications are generated installation copies, not separate sources of truth.

## A useful contribution

Prefer improving an existing specialist over introducing overlapping skills. A skill or knowledge change should provide:

1. **A reproducible problem:** observable UI symptoms and the affected workflow or component.
2. **A diagnostic distinction:** how to separate this issue from similar-looking problems.
3. **Provenance:** authoritative source links, applicability, and limits of the evidence.
4. **A remediation path:** concrete design or implementation guidance, including trade-offs and counterexamples.
5. **Acceptance criteria:** tests or observable behavior that could falsify the proposed fix.

Keep the four workflow skills in each family—diagnose, review, build, validate—separate from specialist playbooks. Update classifications, recipes, and evaluation cases together when adding a new issue type. Match skill folder names, YAML `name` and `description` frontmatter, and `manifest.json` records. If source data under `knowledge/` is mirrored into a diagnosis skill's `references/`, update both copies byte-for-byte.

## Skill document format

Follow [the skill authoring convention](docs/skill-authoring.md) for all 42 `SKILL.md` files: YAML-compatible, double-quoted descriptions; one H1; then `## Scope` and `## Procedure`. Other sections are optional when they add distinct guidance. The description is the discovery trigger, while the body provides the execution guidance.

CI also runs `markdownlint-cli2` against the canonical skill files and authoring documentation. To run it locally (Node.js required only for this optional contributor check):

```bash
npx --yes markdownlint-cli2@0.24.0 "skills/**/SKILL.md" "docs/skill-authoring.md" "CONTRIBUTING.md"
```

## Authority and source rules

- Treat **WCAG 2.1 and 2.2** as versioned normative references. The default is WCAG 2.2 AA, but requirements may select another supported target. Keep conformance outcomes tied to the selected version.
- Treat **WCAG 3.0 Working Draft** content as advisory research, never as an implemented 2.x conformance requirement or a certification basis.
- Treat **OWASP ASVS 5.0.0** as the application requirements authority; its local index covers IDs and levels only. Review authoritative OWASP wording for each normative claim. Preserve version-prefixed requirement IDs, separate unknown from fail, and require evidence for a pass. No scans, report helpers or skills certify application security.
- Treat **OWASP Top 10:2025** as risk awareness; **WSTG 4.2** as authorized testing methodology; **NIST SSDF 1.1 final** as secure-development process guidance; and **NIST CSF 2.0** as optional governance alignment. Do not treat SSDF 1.2 draft as final.
- Only perform active security testing on targets explicitly authorized by the task. Avoid leaking credentials, PII, or production data in test outputs.
- Treat **UX laws and aesthetic-design guidance** as context-dependent heuristics, not mandatory pass/fail standards. Accessible and usable behavior takes precedence over purely aesthetic preferences.
- Write original operational synthesis; don't copy entire external articles, third-party graphics, commercial fonts, or other copyrighted material. Preserve source links and update [NOTICE.md](NOTICE.md) when attribution scope changes.

## Validate changes

Requires Python 3.11+; no third-party Python packages are needed for the built-in checks:

```bash
python scripts/validate_pack.py
python -m unittest discover -s scripts -p 'test_*.py' -v
```

These checks cover skill metadata, semantic catalogs, mirrored reference files, install behavior, WCAG report structures and skill formatting. They **do not** verify live agent skill selection, browser behavior, actual usability outcomes, screen-reader support, or legal/WCAG conformance or actual application security. Evaluate those separately when a change affects them.

### Source control and text consistency

Git tracks source changes and verifies committed objects. There is no separate
SHA-256 inventory to regenerate. CI validates structural correctness and runs
the focused regression suite; changes to workflows, issue templates, and
repository policies do not require checksum updates.

Keep committed text files in **LF** format. `.gitattributes` defines the
checkout policy across operating systems.

## Scope of contributions

Keep the pack dependency-free and self-contained when installed into a different repository. Prefer small, testable additions with clear provenance to generic guidance or complex build tooling. Describe any behavior you have not verified as untested rather than claiming conformance or production readiness.

## Application security reference boundaries

The `knowledge/security/asvs/5.0.0/index.json` reduced ASVS index and installed mirror have separate [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) attribution; other independently authored guidance remains MIT-licensed. Do not copy full OWASP requirement text into the pack or silently relicense upstream material. For an ASVS version update, validate all 345 IDs, levels and chapter mappings against the stable upstream release, then update evaluation expectations and the versioned reference directory deliberately.
