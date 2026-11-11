# Accessing the authoritative OWASP ASVS 5.0.0 requirements

The installed [`index.json`](index.json) intentionally contains identifiers, levels, and chapter metadata, not the normative requirement wording. An ID-only or scanner-only review cannot demonstrate ASVS compliance.

## Source of truth

- **Stable version:** [OWASP ASVS 5.0.0 release](https://github.com/OWASP/ASVS/tree/v5.0.0_release/5.0).
- **Official machine-readable requirements:** [ASVS 5.0.0 English flat JSON](https://github.com/OWASP/ASVS/blob/v5.0.0_release/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.flat.json).
- **Direct raw JSON:** `https://raw.githubusercontent.com/OWASP/ASVS/v5.0.0_release/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.flat.json`.
- **License:** OWASP ASVS content is [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Consult the official terms before redistributing its text.

The upstream flat JSON has a `requirements` array with `req_id` (for example `V3.4.1`), `req_description`, `L`, and chapter/section fields. The local ID `v5.0.0-3.4.1` maps to upstream `V3.4.1`. Levels are cumulative, so Level 2 includes requirements from L1 and L2.

## Source-resolution procedure

1. Select explicit task or project ASVS version and level, or label Level 2 as a *planning fallback*.
2. Filter the installed index by the applicable level and requested scope, without implying unsampled controls are compliant.
3. Fetch the **pinned 5.0.0 official flat JSON** from the authoritative GitHub release when network access is available; when offline, use a previously downloaded copy from that same release. Do not bundle, alter, or commit the upstream text under the project's MIT license.
4. Match the exact `req_id` and level, then read the complete `req_description`, including qualifiers, exceptions, and relevant chapter guidance. Record which upstream release/source was consulted.
5. If the full requirement text is unavailable, mark that requirement `not_tested` or `needs_manual_verification`. Do not infer the requirement from its ID or treat the local index as normative text.
6. Use OWASP WSTG and the relevant [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) for testing and implementation guidance, but do not substitute either for the ASVS requirement being assessed.

A narrowly scoped PR review can assess selected relevant requirements and label the remaining baseline **out of scope**; a complete ASVS assessment must retain a ledger for the entire selected level and require appropriate evidence.
