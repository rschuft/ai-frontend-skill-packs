# Contributing to AI Frontend Skill Packs

This repository publishes reusable **agent skills** for UX, accessibility, and visual design. Contributions should improve what agents can diagnose, implement, or verify—not merely expand a list of design opinions.

## Repository layout

```text
skills/                       42 canonical SKILL.md directories (14 per family)
knowledge/ux-laws/            Laws, articles, classification, recipes, and schemas
knowledge/wcag/               Shared taxonomy and recipes; 2.1/2.2 normative catalogs, 3.0 draft research
knowledge/visual-design/      Principles, elements, articles, Gestalt, and recipes
integration/                  Optional routing guidance for consuming projects
evaluation/                   Classification and skill-invocation scenarios
scripts/install.py            Offline installation into Claude Code and Codex projects
scripts/resolve_wcag_target.py  WCAG standard/level selection
scripts/check_wcag_audit.py   Report coverage checker (not conformance certification)
scripts/validate_pack.py      Structural, reference, and release-file integrity checks
scripts/test_pack.py          Installer and audit regression tests
manifest.json                Machine-readable skill registry
MANIFEST.sha256               SHA-256 inventory of release-managed files
NOTICE.md                     Third-party attribution and license boundaries
```

`skills/` is the canonical publication source. The `.claude/skills/` and `.agents/skills/` directories in consuming applications are generated installation copies, not separate sources of truth. Existing files under `metadata/` and `licenses/` may preserve historical source-pack names for attribution; they do not name active skills.

## A useful contribution

Prefer improving an existing specialist over introducing overlapping skills. A skill or knowledge change should provide:

1. **A reproducible problem:** observable UI symptoms and the affected workflow or component.
2. **A diagnostic distinction:** how to separate this issue from similar-looking problems.
3. **Provenance:** authoritative source links, applicability, and limits of the evidence.
4. **A remediation path:** concrete design or implementation guidance, including trade-offs and counterexamples.
5. **Acceptance criteria:** tests or observable behavior that could falsify the proposed fix.

Keep the four workflow skills—diagnose, review, build, validate—separate from specialist playbooks. Update classifications, recipes, and evaluation cases together when adding a new issue type. Match skill folder names, YAML `name` and `description` frontmatter, and `manifest.json` records. If source data under `knowledge/` is mirrored into a diagnosis skill's `references/`, update both copies byte-for-byte.

## Authority and source rules

- Treat **WCAG 2.1 and 2.2** as versioned normative references. The default is WCAG 2.2 AA, but requirements may select another supported target. Keep conformance outcomes tied to the selected version.
- Treat **WCAG 3.0 Working Draft** content as advisory research, never as an implemented 2.x conformance requirement or a certification basis.
- Treat **UX laws and aesthetic-design guidance** as context-dependent heuristics, not mandatory pass/fail standards. Accessible and usable behavior takes precedence over purely aesthetic preferences.
- Write original operational synthesis; don't copy entire external articles, third-party graphics, commercial fonts, or other copyrighted material. Preserve source links and update [NOTICE.md](NOTICE.md) when attribution scope changes.

## Validate changes

Requires Python 3.11+; no third-party Python packages are needed for the built-in checks:

```bash
python scripts/validate_pack.py
python -m unittest discover -s scripts -p 'test_*.py' -v
```

These checks cover skill metadata, semantic catalogs, mirrored reference files, install behavior, WCAG report structures, and SHA-256 file inventory. They **do not** verify live agent skill selection, browser behavior, actual usability outcomes, screen-reader support, or legal/WCAG conformance. Evaluate those separately when a change affects them.

### Release checksum discipline

`manifest.json` is the semantic catalog of skills. `MANIFEST.sha256` is the byte-level integrity inventory of the repository's release-managed files, including this guide and `README.md`.

After modifying tracked release files, recompute their SHA-256 values in `MANIFEST.sha256`. Add a checksum line for each new release-managed file and delete obsolete entries. Every line has the form `<lowercase SHA-256>  <repo-relative POSIX path>`, and lines should be sorted by path. Do not add `.gitignore`, local virtual environments, Git metadata, test caches, or user-specific files: `scripts/validate_pack.py` explicitly excludes them. The validator rejects unlisted managed files, missing managed files, and hash mismatches.

All committed text files should use **LF**, not CRLF, line endings. `.gitattributes` defines the checkout policy; check the *committed* byte representation when preparing a release from Windows.

## Scope of contributions

Keep the pack dependency-free and self-contained when installed into a different repository. Prefer small, testable additions with clear provenance to generic guidance or complex build tooling. Describe any behavior you have not verified as untested rather than claiming conformance or production readiness.
