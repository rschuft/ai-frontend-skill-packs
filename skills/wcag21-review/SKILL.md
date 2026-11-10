---
name: wcag21-review
description: Perform an evidence-based WCAG 2.1 accessibility audit of web pages, applications, components and end-to-end flows. Use for A/AA/AAA reviews, PR audits, acceptance criteria, accessibility checklists and compliance gap analyses.
---

# Review page(s) or workflows against WCAG 2.1

**Before starting**, define target version **WCAG 2.1** and target level (default **AA**, i.e. A + AA), evaluated routes, representative page templates, task flows, device/browser/AT support matrix and review depth. If unspecified, use AA as an explicit planning default, not as an implied claim of compliance.

1. Consult `../wcag21-diagnose/references/criteria.json`, taxonomy and `conformance.json`. At AA cover 50 SCs, including 30 A; mark every SC `pass`, `fail`, `not_applicable`, `not_tested` or `needs_manual_review`. Do not silently exclude SCs because a scanner cannot automate them.
2. Review **complete page** and **every step of each covered process**: navigation, content, embeds, overlays, error and success states, session expiry, dynamic updates, responsive behavior, touch and keyboard.
3. Combine static analysis, automated rules and manual keyboard/zoom/media/visual checks; include screen reader interaction and expert content judgment. Check devices, states and AT support relevant to actual users. Read `references/evidence-matrix.md` for repeatable scope and evidence rules.
4. Diagnose barriers via `wcag21-diagnose` and load specialist playbooks only for relevant classes. Cite exact SC and canonical W3C link. Record counterevidence, exception tests and remediation ownership.
5. Summarize coverage, unresolved fail findings, incomplete manual work, re-test obligations and process risks. **Never mark fully conforming from a partial sample or a passing axe scan.**

## Severity

Blocker: task inaccessible or dangerous (e.g. keyboard trap, unmitigated seizure risk). High: major access barrier to core process. Medium: meaningful access friction or functional restriction. Low: limited impact with workaround. Evidence and task harm—not levels A/AA/AAA alone—determine priority.

## Output

Audit scope and support matrix; criterion coverage by status and level; ordered findings with evidence, links, fix, owner and test; untested gaps; conformance-claim caveat. Use a machine-readable findings list adhering to the schema if user requests JSON/CSV.
