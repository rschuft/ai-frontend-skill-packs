# Hierarchy, contrast and emphasis playbook

**Discriminate:** Is the problem weak hierarchy (no clear rank), wrong emphasis (wrong item wins), or inaccessible legibility (normative WCAG concern)? Do not conflate these. Work from the page's actual goal.

## Diagnostic checks
1. Reduce a screenshot to a thumbnail and grayscale. What survives? Is the actual primary proposition first, followed by task-relevant evidence and action?
2. Compare H1, H2, body and supporting copy by size, weight, alignment, tone and separation. Is each rank meaningfully distinguishable without using hue alone?
3. Count visually primary buttons. Ask whether the task actually permits ranking them. Cancellation and consent cannot be buried just to manufacture a hero.
4. Validate at narrow widths: an oversized hero can consume the viewport and push the actual message away; typography must reflow.

## Repair sequence
- Restate the primary user question as a single concise heading or status. Reduce competition before increasing its scale.
- Allocate space and consistent alignments to establish a readable order; apply scale and weight steps with design tokens.
- Use one conspicuous accent role when appropriate, not a saturated rainbow. Keep links and secondary actions readable and identifiable.
- Apply semantic headings and correct DOM order; CSS visual position is no substitute for logical navigation.

## Implementation sketch
```css
.hero-title { font-size: clamp(2rem, 1.1rem + 2.8vw, 3.5rem); line-height: 1.08; max-width: 18ch; }
.lead { max-width: 58ch; line-height: 1.55; }
.actions { display: flex; flex-wrap: wrap; gap: .75rem; }
/* Use existing primary/secondary component variants, don't invent semantic hierarchy via color alone. */
```

## Prove the change
Conduct quick first-glance recall and grayscale checks with real content. Verify tab order, focus visibility and legibility via `wcag-*`. Record when a focal-point hierarchy is an untested design hypothesis.

Source links: https://www.digitalpolo.com/visual-hierarchy-in-design/ · https://www.digitalpolo.com/emphasis-in-design/ · https://www.digitalpolo.com/contrast-in-design/
