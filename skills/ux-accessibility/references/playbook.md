# Accessibility and inclusive usability verification

Accessibility requirements are not optional consequences of a psychology law. Treat explicit standards, user needs and product obligations as primary; use Laws of UX as an additional explanatory lens, never as a conformance substitute.

## Review surfaces and repairs

1. **Keyboard operation:** Native elements where possible; tab and arrow-key behavior per component type; visible focus; no traps; logical focus on dialogs and after route changes; Escape and return focus when appropriate.
2. **Name, role and state:** Ensure controls have meaningful accessible names, correct semantics, states and descriptions. Associate labels and field errors programmatically. Verify hidden content does not receive focus.
3. **Perception:** Check text/non-text contrast by applicable WCAG criterion, non-color state cues, meaningful heading structure, zoom/reflow, high contrast, text resizing, meaningful alt text and readable labels.
4. **Target acquisition:** Measure actual interactive target size/spacing and drag alternatives. WCAG 2.2 SC 2.5.8 has a 24×24 CSS px minimum with enumerated exceptions; the 44×44 enhanced criterion is AAA. Do not misreport the stronger target as universally mandatory AA.
5. **Time and motion:** Respect reduced motion, avoid surprise focus shifts, make time constraints manageable and notify users of important async updates without live-region noise.
6. **Forms and errors:** Preserve entries, announce relevant issues, identify fields and suggestions in text, ensure recovery without relying on color or pointing alone.
7. **Responsiveness:** Test narrow screens, 200%+ zoom, touch and desktop input, varied text lengths and localization, with semantic grouping intact.

## Validation sequence

Static code/DOM inspection and automated checks can detect some failures; they do not prove usability or full conformance. Manually run keyboard-only and a representative screen reader, check pointer and viewport behavior, and involve users with disabilities when practical. Capture reproducible conditions and WCAG criterion where relevant. Audit components and end-to-end journeys, not just isolated screenshots.

## References

- https://www.w3.org/TR/WCAG22/
- https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum
- https://www.w3.org/WAI/ARIA/apg/patterns/
- https://lawsofux.com/fittss-law/
- https://lawsofux.com/von-restorff-effect/
