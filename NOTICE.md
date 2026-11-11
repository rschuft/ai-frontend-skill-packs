# Copyright, license, and attribution

This repository contains independently authored agent instructions, operational summaries, catalogs, scripts, examples, and evaluation cases across four skill families. These original portions (excluding the separately attributed OWASP-derived ASVS index) are intended for redistribution under the existing **MIT License** at the root of `rschuft/ai-frontend-skill-packs`. When publishing, retain that repository license and the appropriate copyright notices.

## Third-party source material

- **Laws of UX**: https://lawsofux.com/ — Jon Yablonski. External website, article content, imagery, and source publications remain with their owners. This pack summarizes the site's listed principles and indexed articles in independently authored terms; it does not redistribute their full text or illustrations.
- **WCAG 2.1 / 2.2**: https://www.w3.org/TR/WCAG21/ and https://www.w3.org/TR/WCAG22/ — World Wide Web Consortium (W3C). The normative Recommendations, Understanding documents and Techniques remain W3C publications. This pack provides its own summaries and links, not a W3C-authorized standard copy or a certification tool. W3C copyright terms: https://www.w3.org/copyright/ .
- **Additional references**: W3C WAI-ARIA Authoring Practices, the non-final WCAG 3.0 Working Draft (https://www.w3.org/TR/2026/WD-wcag-3.0-20260910/), and usability-research references are linked in source-method files. External licenses are **not** replaced by this repository's MIT License.

No claim of third-party endorsement or conformance is made.

## Visual-design sources (Digital Polo)

This repository’s visual-design skills are original operational synthesis of public articles by Digital Polo / Aditya Kathotia, beginning with [The 7 Principles of Design Explained](https://www.digitalpolo.com/principles-of-design-explained/) and the curated source inventory in [`knowledge/visual-design/articles.json`](knowledge/visual-design/articles.json). The third-party articles, text, imagery, and branding remain the property of their respective rights holders; these materials are not bundled under this repository’s MIT license. Source title/URL attribution is not endorsement or relicensing. No third-party imagery or font binaries are redistributed.

## Application security sources and licensing

- **OWASP Application Security Verification Standard 5.0.0:** https://github.com/OWASP/ASVS/tree/v5.0.0_release/5.0 — © OWASP Foundation and contributors. The reduced requirement ID/level/chapter index in `knowledge/security/asvs/5.0.0/index.json` and its installed copy under `skills/security-diagnose/references/` are derived from OWASP ASVS 5.0.0 and distributed separately under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). This adaptation removes the normative requirement descriptions and retains version-pinned identifiers and metadata. The complete original standard is linked, not included.
- **OWASP Top 10:2025:** https://top10.owasp.org/2025/ — original risk categories, linked for orientation; this pack contains an independently authored mapping to skills, not a reproduced risk document.
- **OWASP Web Security Testing Guide 4.2:** https://owasp.org/www-project-web-security-testing-guide/v42/ — CC BY-SA 4.0, external test methodology only. Its full text is not included.
- **NIST SP 800-218 SSDF 1.1:** https://csrc.nist.gov/pubs/sp/800/218/final — external final secure-development practices; the bundled process-category mapping is original operational guidance. NIST CSF 2.0 is an optional external governance reference. Draft SSDF 1.2 is not the stable target.

This repository is not affiliated with OWASP or NIST, and its skill outputs, static checks and assessment-report validation are not certifications of application security.
