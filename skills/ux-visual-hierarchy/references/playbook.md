# Visual perception, grouping, attention and hierarchy

## Diagnose perceptual confusion

Classify the signal: **related content appears unrelated** (proximity, common region), **unrelated content appears equivalent** (similarity), **sequence lacks a visible relationship** (connectedness), **primary action is lost** (Von Restorff/selective attention), **icons are ambiguous** (Prägnanz and mental models), or **good looks hide failure** (aesthetic-usability effect).

## Design grammar

- **Hierarchy:** Give each screen one clear task focus with headings, labels and meaningful content order. Use size, weight, whitespace, alignment and limited accent—not color alone—to distinguish levels.
- **Proximity:** Within-group spacing should be consistently tighter than between-group spacing. Associate labels/help/errors with the controls they describe; retest after responsive wrapping.
- **Regions and connection:** Borders and surfaces signal a genuine group, but cards around every atom add unnecessary noise. A connector or stepper implies a real relationship and should not be decorative.
- **Similarity:** Same role -> same visual behavior. Do not make static text look tappable or links appear identical to body text. Ensure state distinctions are observable.
- **Selective attention:** Key information should be in the user's task context. Avoid making warnings look like ads or positioning status updates where change blindness is likely.
- **Von Restorff:** Reserve distinct emphasis for a key action/state; don't highlight all CTAs. Treat danger, status and hierarchy semantics consistently.
- **Aesthetic-usability:** Distinguish attractiveness from task usability; test with actions, not screenshots alone.

## Practical implementation

Derive reusable layout tokens and component states from semantics rather than per-screen decoration. Keep source order aligned with visual reading order. Use text labels for non-standard icons. Add clear keyboard focus, hover/pressed/selected/disabled/error states, and ensure contrast in every state. On small screens, do not scatter a label, control and validation message into separate scrolling regions.

## Validation

Five-second test: identify the goal and primary action; brief-scan test: identify which items belong together; role-prediction test: distinguish clickable versus informational items. Repeat in grayscale, high zoom, narrow viewport, reduced motion and keyboard mode. Visual polish may earn preference while task completion remains poor—check both.

Sources: https://lawsofux.com/law-of-proximity/ ; https://lawsofux.com/law-of-similarity/ ; https://lawsofux.com/law-of-common-region/ ; https://lawsofux.com/law-of-uniform-connectedness/ ; https://lawsofux.com/selective-attention/
