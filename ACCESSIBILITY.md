# Accessibility

AI Frontend Skill Packs provides instructions and reference material for AI coding agents that diagnose, review, build, and validate user interfaces. This is a **documentation, skill, and command-line repository**, not a hosted frontend application.

Accessibility matters both to people using and contributing to this repository and to people affected by interfaces built with its guidance. We aim to make our materials clear, usable with assistive technology, and useful for producing more accessible interfaces. This statement describes our practices and limitations; it is **not a certification of accessibility or WCAG conformance**.

## Priorities

- Make documentation, examples, issue forms, and contribution guidance readable, structured, navigable, and understandable without relying on images or color alone.
- Make instructions usable with keyboard and assistive technology; provide text equivalents when information is presented visually.
- Prioritize meaningful labels, clear error and status information, logical reading order, contrast, zoom/reflow, and alternatives to pointer-only interactions when guidance addresses user interfaces.
- Preserve the distinction between an automated check, a manual test, and evidence of a user's actual task outcome.

The accessibility skills use **WCAG 2.2 Level AA as their default planning target**. They can also assess WCAG 2.1 requirements when specified, while WCAG 3.0 is tracked as draft research only. This default applies to the *advice the skills produce*, not as a claim that this repository—or any consuming application—has passed an accessibility audit. See the [README](README.md) for version selection.

## Contributor expectations

For documentation and skill changes, contributors should:

- Use descriptive headings and link text; keep tables simple and make code, commands, and examples available as selectable text.
- Avoid instructions that depend solely on sight, color, a screenshot, or a particular input method.
- Distinguish applicable WCAG requirements from UX or aesthetic recommendations, and link to authoritative sources.
- Include observable acceptance criteria, relevant test results, and limitations of testing for accessibility-related changes.
- Keep issue forms and contribution workflows short, labeled, and usable without uploading screenshots or disclosing a disability.

Our GitHub Actions checks validate skill catalogs, references, installation behavior, and release-file integrity. **They do not run a comprehensive accessibility audit**, simulate assistive technology, or prove WCAG conformance. See [CONTRIBUTING.md](CONTRIBUTING.md) for development checks.

## Reporting an accessibility barrier

[Open an accessibility issue](https://github.com/rschuft/ai-frontend-skill-packs/issues/new?template=accessibility.yml). You can also [open a regular issue](https://github.com/rschuft/ai-frontend-skill-packs/issues/new/choose) if the form does not fit your situation.

Describe the task you were trying to complete and what prevented or complicated it. If available, include the page or file, steps to reproduce, observed behavior, and relevant browser, operating system, input method, or assistive technology. **All of these details are optional except a description of the barrier.** Screenshots, recordings, personal information, and disability disclosures are never required. Do not post credentials or private data.

If the issue exposes a security vulnerability, [report it privately](SECURITY.md) instead of opening a public issue.

### Impact and severity

Reporters can describe the impact in their own words; maintainers will triage it. The issue form offers these optional descriptions:

| Impact | Example |
| --- | --- |
| Blocking | Unable to complete an essential task, with no known workable alternative |
| Significant difficulty | The task is possible only with major effort or an unreliable workaround |
| Minor barrier | A confusing, inefficient, or uncomfortable experience with a workable alternative |
| Unsure | Impact has not been determined |

These are triage descriptions, not automatic priority labels or guaranteed resolution times.

### What happens next

Maintainers will review reports on a **best-effort basis**. Where reproducible, we aim to identify the affected task, clarify impact, provide a workaround if one is available, document the proposed correction, and invite verification when a fix is available. We cannot guarantee response or fix deadlines. Reports may remain open when additional evidence or assistance is needed.

## Environments and limitations

The repository's primary delivery formats are Markdown, JSON, CSV, YAML, and optional Python command-line tools. GitHub hosts the documentation and issue forms; Claude Code and Codex consume installed skills. The accessibility of those third-party products is outside this repository's direct control.

**No comprehensive, independently verified assistive-technology/browser support matrix is published for this repository.** We do not claim that all combinations of browsers, screen readers, keyboard layouts, and hosts have been tested. The skills and report checker can support accessibility work but cannot themselves establish real application conformance. Any specific barriers or workarounds should be tracked in [accessibility issues](https://github.com/rschuft/ai-frontend-skill-packs/issues?q=is%3Aissue+accessibility) instead of assuming there are none.

## Ownership and feedback

Repository maintainers own the accessibility statement, triage, and changes to skill guidance. We will revisit this document when the supported workflows, standards, or reported limitations materially change. Suggestions to improve this policy can be submitted through [GitHub issues](https://github.com/rschuft/ai-frontend-skill-packs/issues/new/choose); use the accessibility issue form for an active barrier.
