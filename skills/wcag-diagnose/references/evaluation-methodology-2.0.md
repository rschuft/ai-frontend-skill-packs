# WCAG Evaluation Methodology (WCAG-EM) 2.0

Source: [WCAG Evaluation Methodology (WCAG-EM) 2.0](https://www.w3.org/TR/WCAG-EM/), **W3C Group Note, 23 July 2026**.

WCAG-EM 2.0 is **informative evaluation guidance**, not a new WCAG success criterion, a replacement for the selected WCAG 2.1/2.2 Recommendation, or an automatic conformance certificate. It applies to web pages, apps, and other digital products. Use this methodology when a user requests a scoped WCAG review; don't impose a complete evaluation on a narrowly targeted bug fix.

## Evaluation sequence

1. **Define the scope:** Specify the product boundary, user tasks, content and features, evaluation target/version/level, assumptions, technologies relied upon, and accessibility support baseline (including relevant browser/assistive-technology combinations).
2. **Explore the product:** Identify common functions, templates, user roles, technologies, states, and complete processes. Inspect actual behavior rather than inferring it from screenshots.
3. **Select a representative sample:** Justify why pages, routes, screens, states, and complete journeys are included, including challenging or atypical cases. Record exclusions and what was not sampled. Sampling does not turn untested functionality into a pass.
4. **Evaluate the selected sample:** Test applicable success criteria using automated and manual methods, including keyboard, screen reader, zoom, touch, content/media, and relevant state/viewport combinations. Record observed results, methods, and evidence.
5. **Report results:** Record the exact scope, standard/level, sample rationale, accessibility support baseline, test environment and dates, findings, unresolved tests, and the limits of evaluation. Keep evidence traceable to screens and complete processes.

## Important boundaries

- A **representative evaluation** and an **entire-product conformance claim** are different. Do not infer unsampled or untested portions conform.
- This method does not add WCAG requirements or make automated checking sufficient. The selected WCAG Recommendation controls pass/fail interpretations.
- Treat accessibility support assumptions as explicit, and test third-party content and whole processes where relevant.
- A targeted remediation review can name the methodology as guidance while clearly marking that no full-product evaluation was conducted.

For authoritative methodology requirements and examples, consult the linked W3C Group Note directly. This file is an original operational summary, not a reproduction of that document.
