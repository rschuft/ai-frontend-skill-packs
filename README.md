# AI Frontend Skill Packs

**Agent skills for building interfaces that work well, are accessible, and look intentional.**

This MIT-licensed repository gives frontend coding agents three complementary bodies of guidance: **usability** (Laws of UX), **accessibility** (WCAG 2.2, with 2.1 compatibility and 3.0 draft research), and **visual/aesthetic design** (Digital Polo’s seven principles of design, color theory, and related articles). Rather than loading a long design manual for every prompt, the agents can select focused skills to **diagnose, review, implement and validate** real UI work.

The pack uses portable [`SKILL.md`](https://agentskills.io/specification) files and supports **Claude Code and Codex**. Skills have descriptive trigger metadata for model-driven discovery; selection remains host/model-dependent and is not guaranteed.

## What you can do

| Workflow | UX / usability | Accessibility | Visual design |
| --- | --- | --- | --- |
| **Diagnose** unclear or broken UI | [`ux-diagnose`](skills/ux-diagnose/SKILL.md) | [`wcag-diagnose`](skills/wcag-diagnose/SKILL.md) | [`design-diagnose`](skills/design-diagnose/SKILL.md) |
| **Review** existing screens, code and flows | [`ux-review`](skills/ux-review/SKILL.md) | [`wcag-review`](skills/wcag-review/SKILL.md) | [`design-review`](skills/design-review/SKILL.md) |
| **Build** screens, components and fixes | [`ux-build`](skills/ux-build/SKILL.md) | [`wcag-build`](skills/wcag-build/SKILL.md) | [`design-build`](skills/design-build/SKILL.md) |
| **Validate** changes with evidence | [`ux-validate`](skills/ux-validate/SKILL.md) | [`wcag-validate`](skills/wcag-validate/SKILL.md) | [`design-validate`](skills/design-validate/SKILL.md) |

Each family also has **10 specialist skills** for deeper, problem-specific remediation—42 skills total. A design review might find that a checkout CTA lacks visual emphasis, a form error is unclear, and a text label lacks sufficient contrast. Those findings should be investigated together but tested using different kinds of evidence, not collapsed into a vague “design quality” score.

### Areas of expertise

- **UX:** navigation and information architecture, cognitive load, forms/errors, feedback, onboarding, user journeys, trust, behavior, and interaction quality.
- **WCAG:** semantics, keyboard and pointer input, reflow/zoom, text/non-text contrast, assistive technologies, media, readable content, and explicit conformance criteria.
- **Visual design:** balance, contrast, emphasis, movement, pattern/repetition, proportion, unity; color harmonies and semantic palettes; typography; visual hierarchy; whitespace and Gestalt grouping; imagery, brand art direction and design tokens.

## Install in a frontend project

Clone this repository alongside the frontend application that will consume the skills:

```bash
git clone https://github.com/rschuft/ai-frontend-skill-packs.git
cd ai-frontend-skill-packs
python scripts/install.py --project ../my-frontend-app --host both --dry-run
python scripts/install.py --project ../my-frontend-app --host both
```

The installer copies complete skill folders into the **target project’s** `.claude/skills/` and/or `.agents/skills/`. It leaves unrelated skills intact, skips identical copies and refuses to replace a different same-named skill without an explicit reviewed `--replace`. Installation requires Python 3.11+ and no third-party packages.

Install one family with `--pack ux-laws`, `--pack wcag` or `--pack visual-design`; `--pack all` (the default) installs all three. The `--pack both` convenience alias also selects all three families. Use `--host claude` or `--host codex` to target just one agent.

For more deterministic routing, merge the short policy in [`integration/AGENTS.fragment.md`](integration/AGENTS.fragment.md) into your consuming project’s `AGENTS.md` or equivalent. Do not copy every catalog into permanent agent context—load the specialist reference when it becomes relevant.

### Example agent requests

> Review this dashboard for visual hierarchy, color consistency, reading density and WCAG 2.2 AA barriers. Distinguish observed visual problems from usability hypotheses, propose specific CSS/component changes and verification.

> Build a responsive settings screen using the existing brand palette and semantic tokens. Apply typography, spacing, focus and error states; explain how the visual design works at narrow widths and zoom.

> This landing page looks amateurish. Classify its visual problems using the seven design principles, identify the biggest cause and make one coherent improvement without damaging UX or accessibility.

> Validate these frontend changes with desktop/mobile and theme screenshots, task behavior, keyboard/AT checks, and any applicable WCAG criteria. Report what was not tested.

The agent’s available evidence limits its claims. A screenshot is useful for visual composition, but cannot prove keyboard behavior, dynamic UI usability or WCAG conformance.

## Knowledge architecture

| Family | Source coverage | Reusable assets |
| --- | --- | --- |
| [Laws of UX](https://lawsofux.com/) | 30 principles and 8 articles | 30 issue-remediation recipes, 13 conflict rules, classification tests |
| [WCAG 2.2](https://www.w3.org/TR/WCAG22/), 2.1 compatibility | 86 criteria in 2.2 (31 A / 24 AA / 31 AAA), plus the original 78 in 2.1; five conformance requirements | 40 remediation recipes, 26 cross-criterion rules, version-aware audit checker; [3.0 Working Draft](https://www.w3.org/TR/wcag3/) advisory research |
| [Digital Polo principles](https://www.digitalpolo.com/principles-of-design-explained/) | 7 design principles, 7 visual elements, 6 Gestalt concepts, 24 curated design articles | 30 remedies, 18 heuristic conflict rules, 40 classification examples, specialist playbooks |

The [machine-readable manifest](manifest.json) indexes skills and their descriptions. [`MANIFEST.sha256`](MANIFEST.sha256) records file hashes for repository integrity; it is not a skills catalog. Primary source catalogs live under [`knowledge/`](knowledge/). Diagnose skills include the necessary reference copies, so installed skills remain self-contained without a link back to this repository.

### Decision hierarchy

**Accessibility requirements and verified user outcomes override aesthetic heuristics.** A visually harmonious palette is not automatically readable. An intentional visual scan path is not necessarily the DOM/keyboard order. A beautiful minimalist layout may worsen an information-dense task. The golden ratio, 60/30/10 color distribution, emotional color associations and a single focal-point rule are optional starting points, not formal requirements.

When no target is supplied, the accessibility skills use **WCAG 2.2 AA**, a planning default rather than a declaration of legal applicability. WCAG 2.1 is selectable for legacy requirements; WCAG 3.0 is a dated Working Draft **research-only** lens, not a conformance target. The selected standard and level are recorded for each audit, and findings cannot silently migrate between versions. Canonical WCAG skill names and shared knowledge folders do not embed a standard version. Automated scanners and static reviews cannot certify conformance.

### How agents select an accessibility standard

1. **An explicit task or contractual requirement** wins—for example, “Audit against WCAG 2.1 AA.”
2. Otherwise, respect the **consuming project's accessibility policy**, using `.frontend-a11y.json` (shown below) or an unambiguous repository instruction. Conflicting policy sources must be resolved rather than guessed.
3. Otherwise, use **WCAG 2.2 AA**. The 14 **`wcag-*` skills are version-independent**; selected WCAG versions determine the normative catalog and conformance requirements.

```json
{ "standard": "WCAG 2.2", "level": "AA", "wcag3_advisory": false }
```

The policy file above is **optional** and belongs in the frontend project being evaluated, not in this distribution repository. `wcag3_advisory` may add a separate research appendix, but never modifies a 2.x conformance matrix. To verify resolution from this repository clone:

```bash
python scripts/resolve_wcag_target.py --project ../my-frontend-app --json
python scripts/resolve_wcag_target.py --project ../my-frontend-app --task-standard 'WCAG 2.1' --task-level AA --json
```

The resolver handles structured options, not natural-language interpretation or freeform `AGENTS.md` parsing: the agent must supply task overrides explicitly. Full precedence and criteria maps: [`standard-selection.md`](knowledge/wcag/standard-selection.md) and [`standards.json`](knowledge/wcag/standards.json).

For structured audits, the report must specify its **standard and level**. At AA, the coverage checker expects **55** WCAG 2.2 criteria or **50** WCAG 2.1 criteria; a 2.2 report containing removed 4.1.1, or a 2.1 report containing a 2.2-only criterion, is rejected:

```bash
python scripts/check_wcag_audit.py evaluation/wcag/sample-audit-22.json --json
```

The sample is intentionally incomplete and the checker validates report structure, not whether the application complies. WCAG 3.0 has no A/AA/AAA levels in this pack; no compliance claims may be based on its draft.


## Repository layout

```text
skills/                      42 canonical SKILL.md directories (14 per family)
knowledge/ux-laws/           UX laws, articles, taxonomy, recipes and schemas
knowledge/wcag/            Shared WCAG taxonomy and recipes, versioned 2.1/2.2 normative catalogs, 3.0 research
knowledge/visual-design/     Design principles, elements, articles, Gestalt, recipes, taxonomy
integration/                 Optional frontend agent-routing fragment
evaluation/                  Classification, activation and example-finding scenarios
scripts/install.py           Safe per-host, per-family skill installation
scripts/validate_pack.py     Source catalog, metadata, integrity and coverage checks
scripts/test_pack.py         Installer and audit-gate regression tests
scripts/check_wcag_audit.py  Version-specific WCAG 2.x report completeness (not certification)
scripts/resolve_wcag_target.py  Explicit task > project policy > 2.2 AA target resolver
manifest.json                Semantic skill index
MANIFEST.sha256              SHA-256 file integrity inventory
NOTICE.md                    Third-party attribution and license boundaries
.github/workflows/           Offline validation on GitHub
```

The original 2.1-only source-pack records retain their historical `wcag21` identifiers under `metadata/` and `licenses/`; these are attribution artifacts, not active agent skill directories.

`skills/` is the single source of truth; `.claude/skills/` and `.agents/skills/` in consuming projects are installed copies. The repository is not a hosted service and does not automatically modify an application’s design by itself.

## Verify and contribute

```bash
python scripts/validate_pack.py
python -m unittest discover -s scripts -p 'test_*.py' -v
```

If editing tracked source files, refresh the corresponding SHA-256 entries in [`MANIFEST.sha256`](MANIFEST.sha256) before committing. Validation checks the intended file inventory (excluding VCS, local caches and generated agent installs) as well as expected skill names and reference consistency.

Contribute a specific reproducible problem, source attribution, discriminating diagnostic check, implementation guidance, a counterexample, and an observable acceptance test. Prefer extending an existing specialist rather than adding an overlapping skill. Preserve the difference between aesthetic advice, usability evidence and normative accessibility requirements. Agent auto-selection, real browser behavior and accessibility must also be evaluated separately from structural tests.

## License and attribution

Original repository content is under [MIT](LICENSE). Laws of UX, WCAG 2.1/2.2, WCAG 3.0 draft and Digital Polo articles remain the works of their authors/rights holders; this repository provides independently authored operational synthesis and links, not wholesale reproductions. No source article text, branded assets or commercial font files are bundled. See [NOTICE.md](NOTICE.md) and the source-method documents under `knowledge/`.

Sources: [Laws of UX](https://lawsofux.com/) · [WCAG 2.2](https://www.w3.org/TR/WCAG22/) · [WCAG 2.1](https://www.w3.org/TR/WCAG21/) · [WCAG 3.0 draft](https://www.w3.org/TR/wcag3/) · [Digital Polo](https://www.digitalpolo.com/principles-of-design-explained/) · [Agent Skills specification](https://agentskills.io/specification)
