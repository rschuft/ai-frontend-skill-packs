# Visual review checklist (not a compliance certificate)

| Audit area | Observable checks | Typical tests | Related specialist |
|---|---|---|---|
| Primary emphasis | First focal point agrees with task | 3–5-second exposure, squint/thumbnail | design-hierarchy-and-emphasis |
| Contrast | Tonal/size/weight differentiation and readability | Grayscale; WCAG contrast pairing in wcag21-* | design-color-theory |
| Composition | Visual weight and ratios intentionally distributed | Narrow/wide screenshot pair | design-balance-and-proportion |
| Visual movement | Scan direction and CTA placement coherent | Trace entry → detail → action; compare DOM order | design-movement-and-flow |
| Type | Hierarchy, measure, line-height, fallbacks | Long content, locale, 200% zoom | design-typography |
| Grouping | Proximity and whitespace match semantic relationships | Blur / grouping check, compare data-dense and editorial | design-layout-and-grid |
| Rhythm | Component treatments consistently repeat | Visual regression across screens | design-rhythm-and-pattern |
| Unity | Tokens, iconography, image tone match art direction | Side-by-side cross-surface grid | design-unity-and-systems |
| Imagery | Crops, sharpness, licensing, content | DPR, object-position, fallback, captions | design-imagery-and-texture |
| Brand | Mood and hierarchy meet documented target | Brief-to-screen matrix, blind style review | design-brand-and-art-direction |

## Evidence fields
- Observed from: browser / code / screenshot / user report / inferred.
- Verified at: viewport and device pixel ratio; theme; component state; content variation; language.
- Required outcome: visual task, not just subjective "looks better".
- Cross-lens checks: WCAG requires its own SC and evidence; UX needs actual task behavior or a clearly labeled hypothesis.
