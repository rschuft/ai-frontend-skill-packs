# Balance, visual weight and proportion playbook

## Diagnose
A layout with equal pixel areas can still feel lopsided because a large dark, sharp or saturated area appears visually heavier than a pale quiet region. Check whether visual imbalance is intentional or accidental, and whether it damages comprehension.

## Techniques
- Symmetrical balance works for calm/formal compositions; asymmetrical balance for a dynamic but controlled focal region; radial balance fits true center-oriented layouts, not ordinary forms.
- Check visual center at **every breakpoint**. An asymmetrical hero on a wide screen may turn into an awkward empty column on mobile.
- Use variable proportion tokens/`minmax()` rather than fixed golden-ratio columns. Golden ratio (~1.618) and rule of thirds can help exploration; neither has unique proof of superiority.
- Reduce weight of an overpowering image through crop, scale, brightness/saturation or moving it below supporting copy; don't simply add more copy to counterbalance it.
- Scale relative to task: information-dense product UIs need stable measures; editorial display typography can support larger steps.

## Example
```css
.hero { display: grid; gap: clamp(1.25rem, 3vw, 3rem); grid-template-columns: minmax(0, 1.1fr) minmax(0, .9fr); align-items: center; }
@media (max-width: 48rem) { .hero { grid-template-columns: 1fr; } }
.hero img { display: block; max-width: 100%; height: auto; }
```
Keep DOM order sensible before reflow. Avoid CSS `order` to disguise a broken reading sequence.

## Acceptance
Compare luminance-reduced views at narrow/mid/wide widths and with variable text. Intentional weight and primary message remain apparent, without clipping or loss of action affordance.

Sources: https://www.digitalpolo.com/balance-in-design/ · https://www.digitalpolo.com/proportion-in-design/ · https://www.digitalpolo.com/principles-of-design-explained/
