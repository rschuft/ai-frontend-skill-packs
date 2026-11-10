# AI Frontend Skill Packs

**Agent skills for building interfaces that are easier to use and more accessible.**

This repository turns established UX principles and accessibility requirements into actionable guidance for coding agents. Instead of delivering a generic design checklist, the skills help an agent **diagnose a user-facing problem, review a UI or workflow, implement a targeted fix, and validate the result**.

The collection combines two complementary sources:

- **[Laws of UX](https://lawsofux.com/)** — usability heuristics for understanding friction, choosing interaction patterns, and checking design tradeoffs.
- **[WCAG 2.1](https://www.w3.org/TR/WCAG21/)** — testable accessibility success criteria, techniques, exceptions, and conformance requirements.

The repository is MIT-licensed, and the skills are designed for **Claude Code and Codex** using the standard [`SKILL.md` format](https://agentskills.io/specification). The agents discover relevant installed skills from their descriptions; detailed references are loaded only when needed. Automatic selection is model-dependent, not guaranteed.

## What the skills help you do

| Task | Entry-point skills | Expected result |
| --- | --- | --- |
| **Diagnose** a confusing or inaccessible interaction | [`ux-diagnose`](skills/ux-diagnose/SKILL.md), [`wcag21-diagnose`](skills/wcag21-diagnose/SKILL.md) | Evidence-based issue classification, likely cause, applicable law or success criterion, and a way to distinguish competing explanations |
| **Review** an existing screen, codebase, or user journey | [`ux-review`](skills/ux-review/SKILL.md), [`wcag21-review`](skills/wcag21-review/SKILL.md) | Prioritized findings tied to observable behavior, impact, remediation, and gaps in the evidence |
| **Build** or repair interface components and flows | [`ux-build`](skills/ux-build/SKILL.md), [`wcag21-build`](skills/wcag21-build/SKILL.md) | Implementation guidance, state and interaction contracts, accessible patterns, and focused acceptance checks |
| **Validate** a change or accessibility audit | [`ux-validate`](skills/ux-validate/SKILL.md), [`wcag21-validate`](skills/wcag21-validate/SKILL.md) | Task-oriented tests, regression evidence, and explicit passed, failed, or untested outcomes |

Each family also has **10 specialist skills** for deeper work. UX specialists cover areas such as cognitive load, navigation, visual hierarchy, forms, feedback, onboarding, and user journeys. WCAG specialists cover areas such as semantic structure, keyboard interaction, responsive presentation, media, timing, forms, and assistive technology. See [`skills/`](skills/) or the machine-readable [`manifest.json`](manifest.json) for the full inventory.

The skills are intended to work together. For example, a checkout flow may have a usability problem (unclear error recovery) *and* an accessibility failure (errors not programmatically associated with fields). The same observed problem can be investigated through both lenses without confusing a UX heuristic with a WCAG requirement.

## Get started

Clone this repository alongside the frontend project that will use the skills:

```bash
git clone https://github.com/rschuft/ai-frontend-skill-packs.git
cd ai-frontend-skill-packs
```

Install the skills into that project's agent-specific directories (the project must already exist):

```bash
# Preview changes first
python scripts/install.py --project ../my-frontend-app --host both --dry-run

# Install for both Claude Code and Codex
python scripts/install.py --project ../my-frontend-app --host both
```

`--host both` installs skills into `.claude/skills/` and `.agents/skills/` **in the target project**, not in this source repository. You can use `--host claude` or `--host codex` to target only one agent. Use `--pack ux-laws` or `--pack wcag21` to install one family; the default is both.

Installation requires Python (the repository's CI uses Python 3.11) and no third-party packages. Existing unrelated skills are preserved; identical copies are left unchanged. If a same-named skill differs, the installer stops rather than overwriting it. After reviewing the differences, `--replace` allows that specific replacement.

For more consistent skill routing, add the small policy from [`integration/AGENTS.fragment.md`](integration/AGENTS.fragment.md) to the **consuming project's** `AGENTS.md` or equivalent agent instructions. This is optional, but useful when a request spans both usability and accessibility. Avoid loading every specialist and reference catalog into every conversation.

### Ask your agent to use the skills

After installation, examples of useful requests include:

> Review the onboarding flow for usability and WCAG 2.1 AA barriers. Classify the issues by observed user impact, identify applicable principles or success criteria, and propose testable fixes. Distinguish confirmed problems from hypotheses.

> Implement this dialog with correct keyboard behavior, focus management, loading/error states, and responsive layout. Use the relevant frontend skills and include focused tests.

> Validate the checkout changes against the reported findings. Check task completion, error recovery, keyboard interaction, zoom/reflow, and relevant screen-reader behavior. Report what you could and could not test.

An agent can use the skills for code, browser-observed behavior, screenshots, design artifacts, or written problem descriptions. The evidence available determines how confidently it can diagnose and validate an issue; a screenshot alone cannot establish dynamic behavior or accessibility conformance.

## How the knowledge is organized

The repository contains **28 skills**: four workflow entry points and ten specialists in each family. Their reference material is structured for *progressive disclosure*: select a workflow, classify the issue, consult only the matching specialist, apply a remediation pattern, and verify against an explicit outcome.

| Source knowledge | What is included | How it is used |
| --- | --- | --- |
| Laws of UX | 30 principles, 8 supporting articles, issue taxonomy, 30 remediation recipes, and 13 tradeoff/conflict rules | Classify usability failures, choose patterns, identify counterexamples, and define user-outcome checks |
| WCAG 2.1 | All 78 success criteria (30 A, 20 AA, 28 AAA), five conformance requirements, operational glossary, 31 remediation recipes, and 18 cross-criterion rules | Map accessibility barriers to specific criteria, choose repairs, track applicability, and test evidence |
| Evaluations | 66 classification scenarios, skill-invocation examples, and example reports | Check routing coverage and structure; they are not a substitute for live usability or accessibility testing |

Reference catalogs live in [`knowledge/ux-laws/`](knowledge/ux-laws/) and [`knowledge/wcag21/`](knowledge/wcag21/); installed skill folders contain the relevant copies they need, so consuming projects do not depend on paths back into this repository.

### Decision and evidence rules

**WCAG criteria are requirements; UX laws are heuristics.** A design heuristic must not override an applicable accessibility criterion, user consent, or truthful system behavior. WCAG **2.1 AA** is the default *planning target* when none is provided, not a declaration of legal obligation or achieved conformance. WCAG 2.2 has additional criteria and must not be silently conflated with an assessment explicitly scoped to 2.1.

Automated accessibility tools catch only a subset of barriers. A meaningful assessment also needs appropriate keyboard, zoom/reflow, media, content, process, and assistive-technology checks. The skills report missing evidence explicitly and **do not certify compliance**.

For structured WCAG audits, this repository includes a completeness checker:

```bash
python scripts/check_wcag_audit.py evaluation/wcag21/sample-audit.json --json
```

It checks report coverage and required evidence fields; it does *not* decide whether the observations are true or certify a product. The included sample audit is intentionally incomplete.

## Repository map

```text
skills/                  Canonical, installable SKILL.md directories (28)
knowledge/               Laws of UX and WCAG 2.1 reference catalogs and schemas
evaluation/              Classification cases, routing prompts, example findings/audits
integration/             Optional agent-routing instructions for consuming projects
scripts/install.py       Install selected skill families into another repository
scripts/validate_pack.py Validate skill metadata, catalogs, references, and integrity
scripts/check_wcag_audit.py
                         Check WCAG audit-report completeness
scripts/test_pack.py     Unit tests for installation and reporting safeguards
manifest.json            Searchable, machine-readable skill inventory
MANIFEST.sha256          Repository file-integrity inventory
NOTICE.md                Third-party provenance and attribution
licenses/                Additional license/reference material
.github/workflows/       Continuous validation
```

`skills/` is the **source of truth**. The `.claude/skills/` and `.agents/skills/` directories in consuming repositories are installed copies; do not add duplicates of them here.

## Contributing and maintaining the pack

Contributions should make an agent **more accurate or more effective at a real UI task**, not merely add more prose. Prefer a concrete symptom, discriminating diagnostic checks, a repair pattern, a counterexample, and a repeatable validation step. Preserve source attribution, distinguish standards requirements from recommended techniques, and keep specialist skills narrowly scoped to avoid unnecessary context loading.

Run the offline checks before publishing:

```bash
python scripts/validate_pack.py
python -m unittest discover -s scripts -p 'test_*.py' -v
```

When editing repository files, refresh the relevant SHA-256 entries in [`MANIFEST.sha256`](MANIFEST.sha256), which is checked by validation. GitHub Actions runs these checks on pushes and pull requests. Catalog validation and unit tests do **not** demonstrate live agent auto-selection, usable runtime behavior, or WCAG conformance; those require separate evidence.

## License and sources

The original material in this repository is licensed under [MIT](LICENSE). The external UX and WCAG publications remain the work of their respective authors and standards bodies; this repository provides independently structured operational summaries and links rather than republishing those sources in full. See [NOTICE.md](NOTICE.md), [Laws of UX source notes](knowledge/ux-laws/source-and-method.md), and [WCAG 2.1 source notes](knowledge/wcag21/source-and-method.md) for provenance and boundaries.

Sources: [Laws of UX](https://lawsofux.com/) · [WCAG 2.1](https://www.w3.org/TR/WCAG21/) · [Agent Skills specification](https://agentskills.io/specification)
