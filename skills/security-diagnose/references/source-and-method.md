# Source authority and assessment method

- **Requirement authority:** [OWASP ASVS 5.0.0](https://github.com/OWASP/ASVS/tree/v5.0.0_release/5.0) and its machine-readable source. Our `asvs/5.0.0/index.json` covers all requirement identifiers, chapters and levels but deliberately does **not** reproduce or summarize every requirement. Read the official source for exact applicability, conditions and exceptions.
- **Risk awareness:** [OWASP Top 10:2025](https://top10.owasp.org/2025/), mapping only broad vulnerability classes.
- **Test technique:** [OWASP WSTG 4.2](https://owasp.org/www-project-web-security-testing-guide/v42/); reference version-pinned scenarios, but test only authorized targets and avoid active exploitation or destructive operations by default.
- **Development process:** [NIST SP 800-218 SSDF 1.1](https://csrc.nist.gov/pubs/sp/800/218/final), final. Version 1.2 is a draft and advisory only.
- **Organization risk governance:** [NIST CSF 2.0](https://www.nist.gov/cyberframework), an optional alignment, not an application test suite.

Separate an observation from an inferred weakness, a reproduced exploit, a verified remediation and a system-wide assurance claim. Record authorization, target boundaries, selected assessment baseline/level, versions, date, inspected artifacts, exact testing methods, evidence, impact and owner. Distinguish **confirmed**, **suspected**, **not tested**, and **not applicable**. Security severity depends on likelihood, impact and environment, not a single heuristic or ASVS level. Describe proof without leaking credentials, personal information or production data.

Prefer existing open-source SAST, SCA, IaC scanning, secret scanning, DAST (authorized), and manual review; pin tools and capture outputs as evidence. Do not trust an LLM to be the sole security gate. Require a separate independent CI policy where enforcement is needed.
