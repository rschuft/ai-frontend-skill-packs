# Security Policy

AI Frontend Skill Packs is an open-source collection of agent instructions, reference data, and optional Python utilities for UX, accessibility, and visual design. It is **not a hosted service**. Its primary security boundary is the consuming developer's environment: installed skills may influence an AI coding agent that has access to project files, tools, and credentials.

## Report a vulnerability privately

**Use [GitHub's private vulnerability reporting](https://github.com/rschuft/ai-frontend-skill-packs/security/advisories/new).** Private reporting is enabled for this repository. Do not open a public issue or pull request containing an exploitable vulnerability, working exploit, or sensitive information.

A useful report includes:

- The affected skill, script, data file, revision, or installation workflow.
- The security impact and the trust boundary being crossed (for example, untrusted reference content causing an agent to execute an unauthorized command).
- Minimal reproduction steps, expected versus observed behavior, and relevant environment details (agent host, operating system, invocation, permissions).
- A proof of concept using **synthetic data and credentials**, plus any practical mitigations. Redact real secrets, tokens, and personal information.

Reports about harassment or contributor conduct belong under [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), not in security advisories.

## What we consider in scope

Vulnerabilities in this repository's published content or tooling that can plausibly compromise a consuming project or its development environment, including:

- **Agent instruction and prompt-injection attacks:** malicious or improperly trusted `SKILL.md` content, bundled references, or routing rules that demonstrably cause unauthorized tool use, data disclosure, policy bypass, or unsafe file changes.
- **Installer and filesystem safety:** path traversal, symlink manipulation, unapproved overwrites, deletion or modification outside the target skill directories, and unsafe rollback/recovery.
- **Supply-chain and publication integrity:** tampering with published skills, evaluation data, scripts, routing metadata, or integrity checks in a way that hides malicious changes or defeats intended validation safeguards.
- **Credential or sensitive-data exposure:** repository tooling that exposes secrets or sensitive project material without authorization.

A convincing report should identify an exploitable behavior and its impact, not only a suspicious phrase or an abstract model failure.

Generally **not security vulnerabilities**: subjective design disagreements, incorrect UX/WCAG guidance without a security consequence, incomplete accessibility testing, harmless prompt variations, and vulnerabilities entirely within third-party agent hosts or downstream applications unless this repository creates or materially enables the exploit. Those can be reported as normal issues to the appropriate project.

## Supported code

| Source | Security maintenance |
| --- | --- |
| Current `main` branch | Best-effort investigation and fixes |
| Older commits, unmaintained copies, and downstream-modified skill installations | No separate maintenance or backport commitment |

This repository does not currently promise a long-term-support release series. Users who copy skills into another project must review changes and update their installed copies deliberately. A fix committed here does not automatically update downstream installations.

## Handling and disclosure

We aim to acknowledge private reports within **seven calendar days** and share an initial assessment or progress update within **30 days**. These are best-effort targets, not guaranteed response or remediation deadlines. Complex issues may take longer.

We will assess reproducibility and impact, coordinate a fix or mitigation when warranted, and communicate through the private advisory. We prefer coordinated public disclosure after a fix or practical mitigation is available, with a reasonable timeline discussed with the reporter. When appropriate, we may publish a GitHub security advisory and credit the reporter with their consent. Not every report will require an advisory or a CVE.

## Responsible testing

Test only on repositories, agents, accounts, and environments you own or are expressly authorized to assess. Use local or synthetic fixtures; avoid collecting real data, interrupting others' services, or accessing third-party credentials. Do not submit malicious skill content as a public pull request to demonstrate an exploit.

No bug bounty, compensation, or formal safe-harbor agreement is offered by this policy.

## Advice for consumers

Treat agent skills as **executable-in-effect instructions**, even though a `SKILL.md` file is text. Inspect additions and updates before giving an agent access to sensitive files or powerful tools. Prefer least-privilege agent permissions, review proposed commands and diffs, and do not assume that repository checksums prove source authenticity: hashes primarily detect unintended changes relative to the checked-in manifest. Use a trusted repository origin and review the corresponding Git history.
