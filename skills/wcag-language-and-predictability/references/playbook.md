# Language, comprehension and predictable interaction — playbook

**Primary criteria:** 3.1.1–3.1.6, 3.2.1–3.2.5. References: https://www.w3.org/TR/WCAG21/#readable and https://www.w3.org/TR/WCAG21/#predictable

## Language is semantic metadata

Use `<html lang="en">` or the correct BCP 47 language tag for primary human language (3.1.1 A); wrap genuine embedded passages using `lang` (3.1.2 AA) so assistive technology can pronounce correctly. Do not mark proper names or technical words as whole-language changes unless justified. Detect languages from authoring context, not guessing from a single word or visitor region.

For AAA comprehension: explain unusual words/idioms (3.1.3), provide discoverable abbreviation expansion (3.1.4), offer supporting explanation for content beyond lower-secondary reading level where required (3.1.5), and provide pronunciation guidance if pronunciation is essential to meaning (3.1.6). Domain complexity is not proof that every technical term must disappear. Preserve accurate vocabulary while giving accessible explanations.

## Context-change classification

- **3.2.1 A:** receiving focus should not by itself unexpectedly change context.
- **3.2.2 A:** changing setting should not unexpectedly change context without advance advice.
- **3.2.3 AA:** repeated navigation appears in same relative order across pages.
- **3.2.4 AA:** same-function controls use consistent identification.
- **3.2.5 AAA:** context changes occur only at user request or via a mechanism that can disable them.

Changing a chart based on a selector may be an appropriate content update; changing route, opening a new window or moving focus unexpectedly can be a change of context. Understand the W3C glossary definition instead of failing every reactive update.

## Implementation decision patterns

Avoid `<select onchange="location = this.value">` unless consequences are clearly described before use. Prefer a Submit/Go button, preserving keyboard behavior and maintaining focus when validation fails. For reactive filters, keep input focus steady, report result count in a status region if appropriate, and provide an accessible state label. Share consistent navigation/configuration in common components. Do not force uniform terminology for truly different operations.

```html
<label for="region">Region</label>
<select id="region"><option>North</option><option>South</option></select>
<button type="button">Apply region</button>
```

## Validation

Verify language metadata and spoken pronunciation in actual AT. Test Tab alone, change values without submitting, then explicitly submit. Monitor route, window, scroll, focus and form state. Cross-compare at least three related pages for repeated navigation/labels. Have representative readers assess ambiguity, jargon and location of definitions. A linter cannot reliably decide whether a phrase is idiomatic or a context change is surprising.
