# AI Frontend Skill Packs

A dependency-free, MIT-licensed collection of **28 agent skills** for diagnosing, reviewing, building and validating user-facing interfaces, combining the **Laws of UX** and **WCAG 2.1** operational reference packs.

Designed to be committed at the **root of [`rschuft/ai-frontend-skill-packs`](https://github.com/rschuft/ai-frontend-skill-packs)**. `skills/` is the canonical source directory; the installer copies selected skills into consuming projects for Claude Code and/or Codex automatic discovery.

## Contents

| Pack | Diagnose | Review | Build | Validate | Specialists | Source coverage |
|---|---|---|---|---|---|---|
| Laws of UX (`ux-*`) | `ux-diagnose` | `ux-review` | `ux-build` | `ux-validate` | 10 | 30 principles, 8 articles |
| WCAG 2.1 (`wcag21-*`) | `wcag21-diagnose` | `wcag21-review` | `wcag21-build` | `wcag21-validate` | 10 | 78 success criteria, five conformance requirements |

The packs retain **61 remediation recipes**, **31 conflict/misclassification rules**, **66 diagnostic test cases**, independent schemas, and selective specialist playbooks. All 28 skill folders carry their own `SKILL.md` with descriptive frontmatter and local references.

## Extract into this repository

The distribution ZIP is a **repository-root overlay**, without a top-level wrapper directory. Extract it **into the existing clone**, not into a new nested folder:

```bash
cd ai-frontend-skill-packs
unzip /path/to/ai-frontend-skill-packs-v1.0.0-repo-root.zip
python scripts/validate_pack.py
python -m unittest discover -s scripts -p 'test_*.py' -v
```

On Windows, use File Explorer **Extract All** into the clone, or `Expand-Archive` in PowerShell. Review overwrite prompts if the clone already contains `README.md` or other files; this package deliberately **does not** include a root `LICENSE` or `AGENTS.md`, so it will not overwrite the existing repository's MIT copyright terms or agent instructions. The included `NOTICE.md` identifies the external sources. The archive itself **does not** modify GitHub; review and commit normally. If your repository does not already ignore Python-generated caches, add `__pycache__/` and `*.pyc` to its existing `.gitignore`.

## Install from the clone into a frontend project

```bash
python scripts/install.py --project /path/to/your-frontend-repo --host both --dry-run
python scripts/install.py --project /path/to/your-frontend-repo --host both
```

Or specify `--host claude` or `--host codex`; `--pack ux-laws` or `--pack wcag21` installs one family instead of both. The installer copies complete skill folders into `.claude/skills/` and/or `.agents/skills/` in the target project; unrelated skills are retained. It is offline, supports repeated runs, preflights collisions and refuses overwrites without `--replace`. `--replace` is for replacing **only the same-named skill directories** after reviewing the differences.

The installation roots are **inside the project being modified**, not necessarily this distribution repository. `skills/` remains the publication source of truth; generated host directories should not be committed back to this distribution repository as duplicate copies.

## Automatic activation and evidence priority

Skills are **discoverable**, not guaranteed to run on every request: Claude Code and Codex select relevant `SKILL.md` files from installed project skill directories. For consistent frontend routing, copy the minimal policy in [`integration/AGENTS.fragment.md`](integration/AGENTS.fragment.md) into the consuming project's existing `AGENTS.md` (or equivalent host instruction); do not load every specialist or all reference catalogs into all contexts.

- **Ambiguous UX complaint:** `ux-diagnose` → matching `ux-*` specialist.
- **Accessibility barrier:** `wcag21-diagnose` → matching `wcag21-*` specialist.
- **Broad interface review:** `ux-review` + `wcag21-review`; distinguish user experience heuristics from normative accessibility criteria.
- **Implementation:** `ux-build` + `wcag21-build` as applicable, then load focused specialist playbooks.
- **Validation:** `ux-validate` + `wcag21-validate`; run appropriate focused automated and manual tests.

**Authority rule:** WCAG 2.1 success criteria and conformance requirements outrank competing UX heuristics. WCAG **2.1 AA** is a *planning default* only when no target was specified; it is not legal advice. The UX pack also discusses WCAG 2.2 as a separate supplementary source. Never silently mix WCAG 2.2-only criteria into a WCAG 2.1 assessment. An automated accessibility scan alone does not demonstrate conformance.

## Repository layout

```text
skills/                         # 28 canonical host-installable SKILL.md folders
knowledge/ux-laws/             # principle, article, recipe, taxonomy, schema catalogs
knowledge/wcag21/              # 78 criteria, conformance, recipe, taxonomy, schema catalogs
evaluation/ux-laws/            # classification and auto-activation prompt cases
evaluation/wcag21/             # classification prompts and sample coverage audit
integration/AGENTS.fragment.md # lightweight, optional agent routing policy
scripts/install.py             # safe, dependency-free Claude/Codex installer
scripts/validate_pack.py       # full inventory/reference/metadata validation
scripts/check_wcag_audit.py    # WCAG audit completeness check (never certification)
scripts/test_pack.py           # focused installer and report-gate tests
metadata/                      # preserved source pack manifests and provenance
NOTICE.md                      # copyright, third-party boundaries and attribution
manifest.json                  # machine-readable index of all 28 skills
MANIFEST.sha256                # SHA-256 inventory of release files
.github/workflows/validate.yml # offline validations in GitHub Actions
```

The reusable knowledge is namespaced to avoid filename collisions; each classifier also contains its corresponding reference copy, so installed skills work without repository-wide knowledge paths.

## WCAG report gate

```bash
python scripts/check_wcag_audit.py evaluation/wcag21/sample-audit.json --json
```

This checks **scope, criterion coverage and required evidence fields**, not whether observations are true. It never certifies compliance and the included sample is intentionally incomplete.

## Validation boundaries

The included tests confirm catalog completeness, frontmatter/routing metadata, source/reference consistency, safe installer behavior, and WCAG audit-report structure. They do **not** confirm live model auto-invocation, UI behavior in a browser, screen-reader support, task outcomes, or WCAG/legal compliance.

See [`NOTICE.md`](NOTICE.md), [`knowledge/ux-laws/source-and-method.md`](knowledge/ux-laws/source-and-method.md), and [`knowledge/wcag21/source-and-method.md`](knowledge/wcag21/source-and-method.md) for provenance and scope. Source references: [Laws of UX](https://lawsofux.com/) · [WCAG 2.1](https://www.w3.org/TR/WCAG21/) · [Agent Skills specification](https://agentskills.io/specification).
