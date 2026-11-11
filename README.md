# AI Frontend Skill Packs

**Agent skills for frontend usability, accessibility, visual design, and application security.**

This repository gives frontend coding agents four complementary bodies of guidance: **usability** (Laws of UX), **accessibility** (WCAG 2.1 and 2.2, plus WCAG 3.0 draft research), **visual design** (principles, typography, color and composition), and **application security** (OWASP ASVS 5.0.0, OWASP Top 10:2025, and NIST SSDF 1.1 process guidance). Original skill guidance is MIT-licensed; the derived ASVS reference index has separate CC BY-SA 4.0 attribution. Rather than loading a long design manual for every prompt, the agents can select focused skills to **diagnose, review, implement and validate** real UI work.

The pack uses portable [`SKILL.md`](https://agentskills.io/specification) files and supports **Claude Code and Codex**. Skills have descriptive trigger metadata for model-driven discovery; selection remains host/model-dependent and is not guaranteed.

## What you can do

| Workflow | UX / usability | Accessibility | Visual design | Application security |
| --- | --- | --- | --- | --- |
| **Diagnose** unclear or broken UI | [`ux-diagnose`](skills/ux-diagnose/SKILL.md) | [`wcag-diagnose`](skills/wcag-diagnose/SKILL.md) | [`design-diagnose`](skills/design-diagnose/SKILL.md) | [`security-diagnose`](skills/security-diagnose/SKILL.md) |
| **Review** existing screens, code and flows | [`ux-review`](skills/ux-review/SKILL.md) | [`wcag-review`](skills/wcag-review/SKILL.md) | [`design-review`](skills/design-review/SKILL.md) | [`security-review`](skills/security-review/SKILL.md) |
| **Build** screens, components and fixes | [`ux-build`](skills/ux-build/SKILL.md) | [`wcag-build`](skills/wcag-build/SKILL.md) | [`design-build`](skills/design-build/SKILL.md) | [`security-build`](skills/security-build/SKILL.md) |
| **Validate** changes with evidence | [`ux-validate`](skills/ux-validate/SKILL.md) | [`wcag-validate`](skills/wcag-validate/SKILL.md) | [`design-validate`](skills/design-validate/SKILL.md) | [`security-validate`](skills/security-validate/SKILL.md) |

Each family has **10 specialist skills** alongside the four workflow skills, for **56 skills total**. A design review might find that a checkout CTA lacks visual emphasis, a form error is unclear, and a text label lacks sufficient contrast. Those findings should be investigated together but tested using different kinds of evidence, not collapsed into a vague “design quality” score.

### Areas of expertise

- **UX:** navigation and information architecture, cognitive load, forms/errors, feedback, onboarding, user journeys, trust, behavior, and interaction quality.
- **WCAG:** semantics, keyboard and pointer input, reflow/zoom, text/non-text contrast, assistive technologies, media, readable content, and explicit conformance criteria.
- **Visual design:** balance, contrast, emphasis, movement, pattern/repetition, proportion, unity; color harmonies and semantic palettes; typography; visual hierarchy; whitespace and Gestalt grouping; imagery, brand art direction and design tokens.
- **Security:** authentication and sessions, authorization, injection, browser/origin protections, APIs and uploads, cryptography and sensitive data, configuration and secrets, supply chain, logging and threat modeling.

## Install in a frontend project

Clone this repository alongside the frontend application that will consume the skills:

```bash
git clone https://github.com/rschuft/ai-frontend-skill-packs.git
cd ai-frontend-skill-packs
python scripts/install.py --project ../my-frontend-app --host both --dry-run
python scripts/install.py --project ../my-frontend-app --host both
```

The installer copies complete skill folders into the **target project’s** `.claude/skills/` and/or `.agents/skills/`. It leaves unrelated skills intact, skips identical copies and refuses to replace a different same-named skill without an explicit reviewed `--replace`. Installation requires Python 3.11+ and no third-party packages.

Install one family with `--pack ux-laws`, `--pack wcag`, `--pack visual-design` or `--pack security`; `--pack all` (the default) installs all four. The legacy `--pack both` alias also selects all four families. Use `--host claude` or `--host codex` to target just one agent.

For more deterministic routing, merge the short policy in [`integration/AGENTS.fragment.md`](integration/AGENTS.fragment.md) into your consuming project’s `AGENTS.md` or equivalent. Do not copy every catalog into permanent agent context—load the specialist reference when it becomes relevant.

### Example agent requests

> Review this dashboard for visual hierarchy, color consistency, reading density and WCAG 2.2 AA barriers. Distinguish observed visual problems from usability hypotheses, propose specific CSS/component changes and verification.

> Build a responsive settings screen using the existing brand palette and semantic tokens. Apply typography, spacing, focus and error states; explain how the visual design works at narrow widths and zoom.

> This landing page looks amateurish. Classify its visual problems using the seven design principles, identify the biggest cause and make one coherent improvement without damaging UX or accessibility.

> Validate these frontend changes with desktop/mobile and theme screenshots, task behavior, keyboard/AT checks, and any applicable WCAG criteria. Report what was not tested.

> Review this React app and its API for broken authorization and browser token exposure against OWASP ASVS 5.0.0 Level 2. Identify the application boundaries, map exact requirements, and report uninspected services as not tested.

The agent’s available evidence limits its claims. A screenshot cannot prove keyboard behavior or security; a code scan cannot verify an application’s ASVS requirements end to end or establish security certification.

## Knowledge architecture

| Family | Source coverage | Reusable assets |
| --- | --- | --- |
| **Usability and UX** | [Laws of UX](https://lawsofux.com/): 30 principles and 8 articles | 30 issue-remediation recipes, 13 conflict rules, classification tests |
| **Accessibility** | [WCAG 2.1](https://www.w3.org/TR/WCAG21/): 78 criteria (compatibility); [WCAG 2.2](https://www.w3.org/TR/WCAG22/): 86 criteria (default); [WCAG 3.0 Working Draft](https://www.w3.org/TR/wcag3/): advisory research only. Includes five WCAG 2.x conformance requirements. | 40 remediation recipes, 26 cross-criterion rules, version-aware standard resolver and audit checker |
| **Visual design** | [Digital Polo design principles](https://www.digitalpolo.com/principles-of-design-explained/): 7 design principles, 7 visual elements, 6 Gestalt concepts, 24 curated articles | 30 remediation recipes, 18 heuristic conflict rules, 40 classification examples, specialist playbooks |
| **Application security** | [OWASP ASVS 5.0.0](https://github.com/OWASP/ASVS/tree/v5.0.0_release/5.0): full 345 ID/level index across 17 chapters, including 70 L1 / 183 L2 / 92 L3 requirements. Exact requirement text is linked upstream. | 40 remediation recipes, 10 specialists, [OWASP Top 10:2025](https://top10.owasp.org/2025/) awareness map, NIST SSDF 1.1 process mapping, target resolver, audit-ledger checker |

The [skill catalog](manifest.json) lists the available skills and their descriptions. The underlying [knowledge](knowledge/) includes reusable issue classifications, remediation recipes, and source references. Installed skills carry their own required references, so they work independently of this repository.

### Decision hierarchy

**Security, accessibility requirements and verified user outcomes override aesthetic heuristics.** A visually harmonious palette is not automatically readable. An intentional visual scan path is not necessarily the DOM/keyboard order. A beautiful minimalist layout may worsen an information-dense task. The golden ratio, 60/30/10 color distribution, emotional color associations and a single focal-point rule are optional starting points, not formal requirements.

WCAG 2.1 is selectable for legacy requirements. When no target is supplied, the accessibility skills use **WCAG 2.2 AA**, a planning default rather than a declaration of legal applicability. WCAG 3.0 is a dated Working Draft **research-only** lens, not a conformance target. The selected standard and level are recorded for each audit, and findings cannot silently migrate between versions. Canonical WCAG skill names and shared knowledge folders do not embed a standard version. Automated scanners and static reviews cannot certify conformance.

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

For structured audits, the report must specify its **standard and level**. At AA, the coverage checker expects **50** WCAG 2.1 criteria or **55** WCAG 2.2 criteria; a 2.1 report containing a 2.2-only criterion, or a 2.2 report containing removed 4.1.1, is rejected:

```bash
python scripts/check_wcag_audit.py evaluation/wcag/sample-audit-22.json --json
```

The sample is intentionally incomplete and the checker validates report structure, not whether the application complies. WCAG 3.0 has no A/AA/AAA levels in this pack; no compliance claims may be based on its draft.

### How agents select an application security baseline

Security skills prioritize the **explicit requirement** in the task, then an optional consuming-project `.frontend-security.json` policy, then **OWASP ASVS 5.0.0 Level 2** as a **review-planning fallback**, not a universal compliance mandate. ASVS levels are cumulative: 70 L1, 253 through L2, and all 345 through L3. NIST SSDF 1.1 provides development-process alignment; NIST CSF 2.0 is optional governance context. OWASP Top 10 is not a verification checklist.

```json
{ "standard": "OWASP ASVS", "version": "5.0.0", "level": 2 }
```

Place this optional file in the **consuming application**, not the skill repository. You can resolve the target and check a structured assessment ledger from the distribution checkout:

```bash
python scripts/resolve_security_target.py --project ../my-frontend-app --json
python scripts/check_security_audit.py evaluation/security/sample-audit.json --json
```

The sample is deliberately **not tested**. The checker verifies requirement coverage and that evidence fields are present; it does not verify their truth, conduct testing, or certify security. A frontend-only review cannot substantiate server-side authorization, authentication or deployment controls. The bundled ID/level index does not reproduce ASVS requirement text. Read the [official version-pinned ASVS release](https://github.com/OWASP/ASVS/tree/v5.0.0_release/5.0) for actual requirements and exceptions. See [security sources and method](knowledge/security/source-and-method.md).

## Contributing

For repository structure, development checks, source attribution requirements, and how to add or revise skills, see [CONTRIBUTING.md](CONTRIBUTING.md).

## License and attribution

Original repository content is under [MIT](LICENSE), except the identified [OWASP ASVS-derived index](knowledge/security/asvs/5.0.0/README.md) under CC BY-SA 4.0. Laws of UX, WCAG 2.1, WCAG 2.2, WCAG 3.0 draft, Digital Polo, OWASP and NIST materials remain the works of their respective rights holders; this repository provides independently authored operational synthesis and links, not wholesale reproductions. No source article text, branded assets or commercial font files are bundled. See [NOTICE.md](NOTICE.md) and the source-method documents under `knowledge/`.

Sources: [Laws of UX](https://lawsofux.com/) · [WCAG 2.1](https://www.w3.org/TR/WCAG21/) · [WCAG 2.2](https://www.w3.org/TR/WCAG22/) · [WCAG 3.0 draft](https://www.w3.org/TR/wcag3/) · [Digital Polo](https://www.digitalpolo.com/principles-of-design-explained/) · [OWASP ASVS 5.0.0](https://github.com/OWASP/ASVS/tree/v5.0.0_release/5.0) · [NIST SSDF 1.1](https://csrc.nist.gov/pubs/sp/800/218/final) · [Agent Skills specification](https://agentskills.io/specification)
