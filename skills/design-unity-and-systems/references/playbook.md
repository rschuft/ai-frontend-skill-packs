# Design tokens, unity and visual-system playbook

## Architecture
Separate **brand guidelines** (intent and identity), **style guidance** (visual decisions) and a **software design system** (tokens, components, patterns and states). They overlap but should not become one giant document.

Use three levels of design tokens as *appropriate*: primitive (`blue.600`), semantic (`action.primary`), and component (`button.primary.background`). Semantic roles allow independent light and dark theme mappings. Do not create the whole infrastructure for a one-off page; start with repeating decisions.

## Build sequence
1. Audit current color, font, spacing, radius, shadow, icon and animation patterns; identify exceptions that are real semantic differences.
2. Define token ownership, canonical naming and mapping; avoid raw hex/gap literals throughout new components.
3. Consolidate common component variants (buttons, fields, dialogs, cards) but preserve accessible and task-specific states.
4. Document reference examples with dimensions, copy, empty/error/loading and focus states. A screenshot-only style guide is not a functioning design system.
5. Wire visual regression tests and token-level checks to shared component changes; update the smallest affected slice.

## Token example
```json
{"primitive": {"blue600": "#2455aa"}, "semantic": {"actionPrimary": "{primitive.blue600}"}, "component": {"buttonPrimaryBackground": "{semantic.actionPrimary}"}}
```
This is illustrative JSON, not a fully specified token interchange standard.

## Acceptance
Across several product surfaces, semantic roles use consistent tokens, the component API explains variants, and light/dark accessibility and hover/focus/error states are tested. Divergence is documented rather than silently flattened.

Sources: https://www.digitalpolo.com/design-tokens-explained/ · https://www.digitalpolo.com/design-system-vs-style-guide-vs-brand-guidelines/ · https://www.digitalpolo.com/unity-in-design/
