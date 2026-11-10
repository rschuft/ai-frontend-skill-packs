# Visual movement and scan-flow playbook

**Important distinction:** Visual *movement* is the eye's perceived path through a static composition; it is not necessarily animation. Z/F patterns describe some reading contexts, not universal user behavior or scripts.

## Procedure
1. Describe the expected entry point, secondary evidence, decision moment and exit/action.
2. Inspect landmarks, alignments, image gaze, directional edges, relative scale and whitespace that create or break that path.
3. Compare scanning hypotheses with real tasks or a short exposure test. If screenshots are the only evidence, do not state observed eye tracking.
4. Preserve logical DOM order and visible keyboard focus. CSS grid reflow should support, not contradict, assistive-technology reading order.
5. For RTL and localized pages, review actual direction and meaning rather than mechanically mirroring every icon/image.

## Repair options
- Reorder content blocks semantically, demote decorative imagery, align action with relevant evidence.
- Use stepped type hierarchy and section spacing so reading continues through the intended sequence.
- Avoid arbitrary arrows, carousels or autoplay as substitutes for a clear information sequence.
- If genuine animation is added, honor prefers-reduced-motion and applicable WCAG criteria; keep all information available without motion.

## Acceptance
Participants can locate the next action at each state; keyboard/AT order does not contradict visual sequence. Test in mobile and RTL where applicable.

Sources: https://www.digitalpolo.com/movement-in-design/ · https://www.digitalpolo.com/visual-hierarchy-in-design/ · https://www.digitalpolo.com/gestalt-principles-of-design/
