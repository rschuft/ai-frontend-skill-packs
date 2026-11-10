# Typography and type-system playbook

**Discriminate:** Problems might arise from font personality, weak typographic hierarchy, cramped reading, bad measure, poor glyph coverage, or font-loading shifts. Fix the cause, not all typography at once.

## Audit
- Inspect body, caption, label, heading and display roles across real screens; check family, weight, line height, letter spacing, optical size and text measure.
- Long-form body text often benefits from a reasonable line measure (roughly 55–75 characters where feasible) and comfortable line-height (~1.5–1.7 as a starting point), but font metrics, language and density determine the final design.
- Distinguish kerning (pair adjustment), tracking (uniform letter spacing), and leading (line spacing). Prefer default kerning/tracking for UI body copy; tune large branding/display type carefully.
- Serif versus sans conveys brand tone; do not treat either as universally faster to read. Prefer robust script coverage and fallback behavior over idealized mood.

## Implementation sketch
```css
:root { --font-ui: system-ui, 'Segoe UI', sans-serif; --font-body-size: 1rem; }
body { font-family: var(--font-ui); font-size: var(--font-body-size); line-height: 1.6; }
.prose { max-width: 68ch; }
.page-heading { font-size: clamp(1.9rem, 1.2rem + 2vw, 3.2rem); line-height: 1.12; letter-spacing: -0.015em; }
```
Avoid forbidding user-controlled text spacing; WCAG 1.4.12 and reflow constraints require stress tests. Use licensed web fonts only, with appropriate `font-display` and system fallback. Do not package commercial font files.

## Acceptance
Test long headings, lists, diacritics/non-Latin script, browser zoom, delayed font load and translated UI strings. No clipping or loss of controls; type roles visually distinct and documented.

Sources: https://www.digitalpolo.com/serif-vs-sans-serif-fonts/ · https://www.digitalpolo.com/kerning-leading-tracking-explained/ · https://www.digitalpolo.com/proportion-in-design/
