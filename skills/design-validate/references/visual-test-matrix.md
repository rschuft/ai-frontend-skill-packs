# Visual verification matrix

| Property | Baseline | Focused method | Limits |
|---|---|---|---|
| Emphasis | Primary headline loses salience | Grayscale + thumbnail and quick recognition task | Human judgment; not a WCAG metric |
| Color roles | One-off accent and errors look alike | Compare semantic token usage and rendered state | WCAG must be tested separately |
| Typography | Long content clips | Browser render at widths, zoom, localized strings | CSS static read alone incomplete |
| Whitespace | Dense/airy regions obscure grouping | Screenshot pairs and grouping check | Depends on task, not maximum white space |
| Alignment | Cards drift with variable content | Multiple-content screenshot matrix | Fixed min-height may cause zoom clipping |
| Image quality | Cropped face/text, pixelation | DPR, crop, lazy-load fallback | Assets must be licensed |
| Theme | Dark mode inverts tone incorrectly | Light/dark comparison per semantic role | Inversion is not sufficient |
| Unity | Similar pages look unrelated | Side-by-side screenshots, token audit | Intentional page-type variation is allowed |
| Reading order | Eye flow differs from source order | Keyboard and DOM sequence, WCAG review | Static screenshot cannot establish semantics |

Statuses: passed (evidence observed), failed (reproducible defect), not-tested (evidence unavailable). Do not report compliance certification.
