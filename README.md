# AI Frontend Skill Packs

**Agent skills for building interfaces that work well, are accessible, and look intentional.**

This MIT-licensed repository gives frontend coding agents three complementary bodies of guidance: **usability** (Laws of UX), **accessibility** (WCAG 2.1), and **visual/aesthetic design** (Digital Polo’s seven principles of design, color theory, and related articles). Rather than loading a long design manual for every prompt, the agents can select focused skills to **diagnose, review, implement and validate** real UI work.

The pack uses portable [`SKILL.md`](https://agentskills.io/specification) files and supports **Claude Code and Codex**. Skills have descriptive trigger metadata for model-driven discovery; selection remains host/model-dependent and is not guaranteed.

## What you can do

| Workflow | UX / usability | Accessibility | Visual design |
| --- | --- | --- | --- |
| **Diagnose** unclear or broken UI | [`ux-diagnose`](skills/ux-diagnose/SKILL.md) | [`wcag21-diagnose`](skills/wcag21-diagnose/SKILL.md) | [`design-diagnose`](skills/design-diagnose/SKILL.md) |
| **Review** existing screens, code and flows | [`ux-review`](skills/ux-review/SKILL.md) | [`wcag21-review`](skills/wcag21-review/SKILL.md) | [`design-review`](skills/design-review/SKILL.md) |
| **Build** screens, components and fixes | [`ux-build`](skills/ux-build/SKILL.md) | [`wcag21-build`](skills/wcag21-build/SKILL.md) | [`design-build`](skills/design-build/SKILL.md) |
| **Validate** changes with evidence | [`ux-validate`](skills/ux-validate/SKILL.md) | [`wcag21-validate`](skills/wcag21-validate/SKILL.md) | [`design-validate`](skills/design-validate/SKILL.md) |

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

Install one family with `--pack ux-laws`, `--pack wcag21` or `--pack visual-design`; `--pack all` (the default) installs all three. The old `--pack both` remains a compatibility alias for all. Use `--host claude` or `--host codex` to target just one agent.

For more deterministic routing, merge the short policy in [`integration/AGENTS.fragment.md`](integration/AGENTS.fragment.md) into your consuming project’s `AGENTS.md` or equivalent. Do not copy every catalog into permanent agent context—load the specialist reference when it becomes relevant.

### Example agent requests

> Review this dashboard for visual hierarchy, color consistency, reading density and WCAG 2.1 AA barriers. Distinguish observed visual problems from usability hypotheses, propose specific CSS/component changes and verification.

> Build a responsive settings screen using the existing brand palette and semantic tokens. Apply typography, spacing, focus and error states; explain how the visual design works at narrow widths and zoom.

> This landing page looks amateurish. Classify its visual problems using the seven design principles, identify the biggest cause and make one coherent improvement without damaging UX or accessibility.

> Validate these frontend changes with desktop/mobile and theme screenshots, task behavior, keyboard/AT checks, and any applicable WCAG criteria. Report what was not tested.

The agent’s available evidence limits its claims. A screenshot is useful for visual composition, but cannot prove keyboard behavior, dynamic UI usability or WCAG conformance.

## Knowledge architecture

| Family | Source coverage | Reusable assets |
| --- | --- | --- |
| [Laws of UX](https://lawsofux.com/) | 30 principles and 8 articles | 30 issue-remediation recipes, 13 conflict rules, classification tests |
| [WCAG 2.1](https://www.w3.org/TR/WCAG21/) | All 78 success criteria (30 A / 20 AA / 28 AAA), 5 conformance requirements | 31 remediation recipes, 18 cross-criterion rules, coverage checker |
| [Digital Polo principles](https://www.digitalpolo.com/principles-of-design-explained/) | 7 design principles, 7 visual elements, 6 Gestalt concepts, 24 curated design articles | 30 remedies, 18 heuristic conflict rules, 40 classification examples, specialist playbooks |

The [machine-readable manifest](manifest.json) indexes skills and their descriptions. [`MANIFEST.sha256`](MANIFEST.sha256) records file hashes for repository integrity; it is not a skills catalog. Primary source catalogs live under [`knowledge/`](knowledge/). Diagnose skills include the necessary reference copies, so installed skills remain self-contained without a link back to this repository.

### Decision hierarchy

**Accessibility requirements and verified user outcomes override aesthetic heuristics.** A visually harmonious palette is not automatically readable. An intentional visual scan path is not necessarily the DOM/keyboard order. A beautiful minimalist layout may worsen an information-dense task. The golden ratio, 60/30/10 color distribution, emotional color associations and a single focal-point rule are optional starting points, not formal requirements.

When no target is supplied, the WCAG family uses **2.1 AA** as a planning default, not a declaration of legal applicability. Automated scanners and static reviews cannot certify conformance. WCAG 2.2-only requirements must not be silently substituted into a WCAG 2.1 audit.

## Repository layout

```text
skills/                      42 canonical SKILL.md directories (14 per family)
knowledge/ux-laws/           UX laws, articles, taxonomy, recipes and schemas
knowledge/wcag21/            WCAG criteria, evidence requirements, recipes and schemas
knowledge/visual-design/     Design principles, elements, articles, Gestalt, recipes, taxonomy
integration/                 Optional frontend agent-routing fragment
evaluation/                  Classification, activation and example-finding scenarios
scripts/install.py           Safe per-host, per-family skill installation
scripts/validate_pack.py     Source catalog, metadata, integrity and coverage checks
scripts/test_pack.py         Installer and audit-gate regression tests
scripts/check_wcag_audit.py  WCAG audit completeness (not certification)
manifest.json                Semantic skill index
MANIFEST.sha256              SHA-256 file integrity inventory
NOTICE.md                    Third-party attribution and license boundaries
.github/workflows/           Offline validation on GitHub
```

`skills/` is the single source of truth; `.claude/skills/` and `.agents/skills/` in consuming projects are installed copies. The repository is not a hosted service and does not automatically modify an application’s design by itself.

## Verify and contribute

```bash
python scripts/validate_pack.py
python -m unittest discover -s scripts -p 'test_*.py' -v
```

If editing tracked source files, refresh the corresponding SHA-256 entries in [`MANIFEST.sha256`](MANIFEST.sha256) before committing. Validation checks the intended file inventory (excluding VCS, local caches and generated agent installs) as well as expected skill names and reference consistency.

Contribute a specific reproducible problem, source attribution, discriminating diagnostic check, implementation guidance, a counterexample, and an observable acceptance test. Prefer extending an existing specialist rather than adding an overlapping skill. Preserve the difference between aesthetic advice, usability evidence and normative accessibility requirements. Agent auto-selection, real browser behavior and accessibility must also be evaluated separately from structural tests.

## License and attribution

Original repository content is under [MIT](LICENSE). Laws of UX, WCAG 2.1, and Digital Polo articles remain the works of their authors/rights holders; this repository provides independently authored operational synthesis and links, not wholesale reproductions. No source article text, branded assets or commercial font files are bundled. See [NOTICE.md](NOTICE.md) and the source-method documents under `knowledge/`.

Sources: [Laws of UX](https://lawsofux.com/) · [WCAG 2.1](https://www.w3.org/TR/WCAG21/) · [Digital Polo](https://www.digitalpolo.com/principles-of-design-explained/) · [Agent Skills specification](https://agentskills.io/specification)
