# Layout, whitespace, alignment and grouping playbook

## Diagnose with Gestalt and content task
- **Proximity:** related labels/data/actions should have smaller internal than external gaps.
- **Similarity:** same-role cards look alike; do not visually group items that behave differently.
- **Continuity:** align major baselines and edges; avoid misleading nested grids.
- **Figure/ground:** separate content from backgrounds with readable contrast and restrained texture.
- **White space:** use deliberate space for hierarchy, but do not turn comparison tables, dashboards or technical docs into unnecessarily long scroll journeys.

## Responsive repair sequence
1. Build semantic content order. Choose containers and grids based on minimum useful content width, not device labels.
2. Start with flexible width `min()` and CSS Grid `repeat(auto-fit, minmax(min(100%, 18rem), 1fr))` for repeatable cards; use `minmax(0, 1fr)` for content that otherwise overflows.
3. Use 4/8-based spacing tokens where consistent with existing system. Increase gaps *between* groups more than within them.
4. Remove fixed height and decorative `position:absolute` that causes overlapping text under zoom/translation.
5. Recheck at narrow width, 200% zoom and dense data; check the accessible reading and focus sequence separately.

## Example
```css
.container { width: min(100% - 2rem, 74rem); margin-inline: auto; }
.cards { display: grid; grid-template-columns: repeat(auto-fit, minmax(min(100%, 17rem), 1fr)); gap: var(--space-6, 1.5rem); }
.card { min-width: 0; padding: var(--space-6, 1.5rem); }
```

## Acceptance
No accidental horizontal scrolling, meaningful groups remain clear without ornamental borders, headings and controls never overlap, and no information disappears because of visual density choices.

Sources: https://www.digitalpolo.com/white-space-in-design/ · https://www.digitalpolo.com/gestalt-principles-of-design/ · https://www.digitalpolo.com/proportion-in-design/
