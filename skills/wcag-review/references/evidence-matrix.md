# Audit scope, evidence and priority contract

## Scope declaration

Document selected version (2.1 or 2.2), requested conformance level, product/app, route list, task map, domain/subdomains if applicable, authentication roles, localization, responsive breakpoints, browser/OS/input technologies, screen reader combinations, external dependencies, date and reviewer.

**Representative samples** help find defects efficiently but do not prove that every page in scope conforms. Where a claim is contemplated, require evidence that complete pages and every page in complete processes satisfy requirements; use an established evaluation method such as WCAG-EM and clearly state sampling limits.

## Per-criterion matrix

For each of the 50 criteria at AA (or 30 at A / 78 at AAA):

| Field | Required meaning |
| --- | --- |
| id, level | Exact selected-version SC; 2.2 additions only when 2.2 applies, and 4.1.1 only appears in 2.1 |
| applicability | Why this criterion applies, or evidence-backed N/A |
| status | pass / fail / not_applicable / not_tested / needs_manual_review |
| evidence | URLs, components, test states, direct observations |
| methods | static, browser automation, keyboard, visual, AT, content expert, process replay |
| result | Observable effect or repro; distinguish inference from verified behavior |
| risk | Task harm, severity, affected input/user experience, confidence |
| remediation | Exact implementation change, not “follow WCAG” |
| retest | Test owner and reproducible acceptance steps |

Treat incomplete/unknown outcomes as **coverage gaps**, not success. Never count all criteria as passing just because an axe run found no violations. Document exceptions individually; a generic “decorative” exemption cannot cover all images, and an essential 2D widget does not exempt a whole page from reflow.

## Priority rubric

Blocker: significant exclusion from core tasks, unrecoverable keyboard trap or photosensitivity hazard. High: core flow blocked for a modality, missing captions for essential information, serious erroneous submission. Medium: important usability/accessibility failure with workaround. Low: limited obstruction or minor but real barrier. Severity measures risk, not normative level.

## Core test journeys

- Enter route, bypass repeated content, orient by headings/title/landmarks, navigate and finish a goal via keyboard only.
- Use at least one suitable screen reader/browser pairing to check names, relationships, reading/focus sequence and dynamic status changes.
- Resize text to 200%; assess reflow at 320 CSS px (or the applicable horizontal case), test orientation and spacing overrides.
- Verify visible labels, contrast and non-color cues across light/dark/high-contrast states.
- Validate representative forms from invalid input through server error, correction, review and final submit.
- Test timeout/reauth, interrupted flow and retained entries where present.
- Test media alternatives, controls and potential dangerous flash/motion; enlist qualified assessment where warranted.
- Check touch, single pointer, pointer cancellation, voice label compatibility and AAA target size where requested.

## Conformance gates

Five requirements: level coverage, full pages, complete processes, accessibility-supported relied-upon technology, and non-interference. Claim itself is optional, but if issued it requires date, version+URI, level, page scope, and technology list relied upon. W3C conformance is not automatically a statement of compliance with ADA, Section 508, EN 301 549 or any other legal regime; version and legal context must be checked independently.
