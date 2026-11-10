# Forms, validation, error prevention and recovery

## Error taxonomy

Identify (a) benign format variation, (b) missing required information, (c) invalid business value, (d) expired/failed network state, (e) inconsistent or dangerous input, (f) user misprediction of outcome, or (g) repeated entry demanded by product internals. These cases require different responses. Never apply Postel's Law to silently accept security-sensitive ambiguity.

## Remediation

- **Inputs:** Visible persistent labels, expected formats only where useful, examples for ambiguous fields, correct input modes and autocomplete hints. Preserve user input after validation failure.
- **Normalization:** Trim benign whitespace, handle case where meaning is unaffected, accept common harmless separators. Keep canonical stored values consistent and show transformed values if consequential.
- **Validation:** Validate near the moment correction is possible, without flashing errors before user input. Clearly associate messages with the field; describe the issue and how to fix it. Validate at server boundary independently of UX convenience.
- **Complexity transfer:** Prepopulate known data, reuse addresses with explicit user correction, show calculated values and explain assumptions. Do not silently make financial, legal or identity choices.
- **Multi-step:** Explicit current step, saved draft, skip/back when safe, review before irreversible submission, coherent focus on errors and after completion.
- **Failures:** Preserve values; explain whether action succeeded, failed or is uncertain. Offer retry/undo only when idempotent or safely supported. Do not encourage repeated payment submissions.

## Build details

Use `<label for>`, native input types, semantic fieldset/legend for related choices, descriptions bound via `aria-describedby`, and errors that identify the field. Use appropriate `aria-invalid`; do not use ARIA to replace native semantics. For asynchronous validation, announce relevant failures without flooding live regions. Don't rely on placeholder as the label.

## Tests

Submit with blank, malformed, alternate-but-valid, Unicode, pasted, very long, and hostile values; verify preservation, specific recovery and server-side rejection where needed. Test keyboard entry, screen reader error association, slow networks and page reload. Measure first-pass success and successful correction, not simply fewer validation messages.

Sources: https://lawsofux.com/postels-law/ ; https://lawsofux.com/teslers-law/ ; https://lawsofux.com/parkinsons-law/ ; https://lawsofux.com/articles/2024/teslers-law/
