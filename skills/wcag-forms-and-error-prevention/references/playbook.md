# Forms, input purpose, validation and error recovery — playbook

**Primary criteria:** 1.3.5; 3.3.1–3.3.6. Related: 1.3.1, 2.2.5, 4.1.3 and 3.2.2. References: https://www.w3.org/TR/WCAG21/#input-assistance and https://www.w3.org/TR/WCAG21/#input-purposes

## Task-centric diagnosis

Trace a form through empty, focused, typing, invalid, submitting, server-error, corrected, confirmation and resumed session states. Distinguish **field lacks a persistent label** (3.3.2 A), **known invalid value not identified textually** (3.3.1 A), **known correction not suggested** (3.3.3 AA), and **risky submission not protected** (3.3.4 AA or 3.3.6 AAA). `autocomplete` purpose (1.3.5 AA) has a specific taxonomy: use tokens only for fields collecting eligible personal information about the user, not indiscriminately for every form input.

Consult `../wcag-diagnose/references/input-purposes.json` for the complete W3C Section 7 inventory of 53 user-personal-data purposes. The source specification lists purposes, not an instruction to attach unrelated tokens to every field.

## Semantic implementation

```html
<form novalidate>
 <label for="email">Email address <span>(required)</span></label>
 <input id="email" type="email" name="email" autocomplete="email"
        required aria-describedby="email-help email-error" />
 <p id="email-help">We send your receipt here.</p>
 <p id="email-error">Enter an email address, for example name@example.com.</p>
 <button type="submit">Review order</button>
</form>
```

In production, render error text only when appropriate or manage its visibility accessibly; synchronize `aria-invalid="true"` when the field is invalid. Maintain a usable error summary for long forms, focus it deliberately after failed submit where appropriate, and link errors to corresponding fields. Do not assign `role=alert` to every keystroke: repeated assertive announcements can make a form unusable.

## Error prevention requirements

For **3.3.4 AA**, legal commitments, financial transactions, modification/deletion of user-controllable stored data and user test responses need at least one of: reversible, checked for errors, or confirmation/review and correction before finalization. **3.3.6 AAA** extends one of these safeguards to all user submissions. An irreversible Delete Account button is not repaired merely by putting it behind a decorative dialog; actual review, reversible operation, or validated corrections must be possible as required.

## Common pitfalls

Placeholder substituted for label; error conveyed only by red border; input masked in a way that prevents review; “invalid” without correction suggestion; generic `<input autocomplete="on">` where expected user-specific purpose could be identified; validation clearing all completed fields; hidden server errors with no live notification; submit button disabled with no explanation; focus jumping unexpectedly after each keystroke.

## Validation contract

Submit deliberately invalid data in every representative form type, including server-rejected submissions; navigate with keyboard and screen reader. Confirm label, instruction timing, text errors, linked description, next fix, data retention, required confirmation and successful recovery. Capture the submitted data type to judge whether 3.3.4 applies. Security restrictions are relevant to the content of suggestions but are not blanket excuses to omit feedback.

## WCAG 2.2 forms and authentication extension

- **3.3.7 A Redundant Entry:** Trace full multistep checkout/onboarding process and note where data is requested again. Populate or allow selecting previous process values. Evaluate whether re-entry is essential, invalid data, or legitimately security-related before calling a failure.
- **3.3.8 AA Accessible Authentication (Minimum):** Exercise every login, registration, recovery and MFA path. Check paste/autofill/password managers and supported alternatives. Do not claim an inaccessible CAPTCHA is acceptable because a text box exists. The AA requirement has exceptions for object recognition and identifying personal content, but they are not generally available at AAA.
- **3.3.9 AAA Enhanced:** Re-test the paths without relying on those AA object/personal-content exceptions; use a genuine noncognitive or supported assistance route. Never weaken authentication security solely to satisfy a superficial check.
Sources: https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry and https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum
