# Navigation, information architecture and mental models

## Diagnose

Identify the failed *prediction*: destination, label meaning, object hierarchy, action effect, or return path. A visually neat sidebar may still be organized by the vendor's architecture instead of users' mental models. Distinguish failure to **find** an action from failure to **operate** it. Capture the starting screen, task request, expected path, actual path, and where the user first hesitates.

## Remediation ladder

1. **Task-to-label mapping:** Gather representative task phrases and ensure destination labels use user terms. Prefer clear nouns for objects and verbs for actions. Avoid internal organization labels as primary navigation.
2. **Information scent:** Show enough context in navigation labels, search results and breadcrumbs that a destination is predictable. Provide stateful back and place in the hierarchy.
3. **Conventions and novelty:** Adopt established patterns for search, account, settings, modal dismissal, navigation and selection. Novelty requires a specific benefit and an evidence-backed introduction. Preserve transition paths when redesigning a high-use product.
4. **Group according to meaning:** Use proximity, common region and distinct hierarchy where tasks belong together; avoid deep nesting unless domain distinctions warrant it.
5. **Persist context:** Maintain filters, selection, location and search query across detail views. Deep links should load in meaningful state; browser Back should be coherent.
6. **Information-dense expert workflows:** Offer search, recent items, favorites, keyboard navigation and stable landmarks rather than burying features in a simplified mobile-inspired view.

## Build notes

Use semantic navigation landmarks, correct links for navigation and buttons for actions. Do not simulate client navigation with unlabeled click targets. Highlight current location beyond color alone. Ensure keyboard focus arrives at the newly loaded context and that route changes are announced through accessible document title/heading patterns. For nested app navigation, preserve parent-child meaning and indicate scope.

## Validation

- Tree test: can users find a feature from labels without full UI treatment?
- First-click test: does first navigation choice point to the correct region?
- Predict-then-click: ask what a label or control will do; compare with observed outcome.
- Regression: deep linking, browser back, mobile menu, screen reader landmarks, newly introduced feature discoverability.
- Avoid moving familiar locations for aesthetic novelty without proving a measurable benefit.

Sources: https://lawsofux.com/jakobs-law/ ; https://lawsofux.com/mental-model/ ; https://lawsofux.com/articles/2024/familiar-vs-novel/ ; https://lawsofux.com/articles/2020/ux-psychology-google-search/
