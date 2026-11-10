# Navigation, page discovery and orientation — playbook

**Primary criteria:** 2.4.1, 2.4.2, 2.4.4–2.4.6, 2.4.8–2.4.10. Shared with keyboard: 2.4.3 and 2.4.7. Reference: https://www.w3.org/TR/WCAG21/#navigable

## Diagnose navigation versus semantics

Determine whether user cannot **skip**, **find**, **identify**, **locate** or **understand** a page. A skip link (2.4.1) solves repeated blocks, not necessarily heading semantics (1.3.1). A page title (2.4.2) helps tabs and history; an `h1` alone does not establish a descriptive document title. Link purpose (2.4.4) may be obtainable from programmatic context at A; for 2.4.9 AAA purpose must be determinable from link text alone except generic ambiguity. Multiple ways (2.4.5 AA) generally applies to pages in a set, except steps in a process.

## Recommended patterns

```html
<a class="skip-link" href="#main">Skip to main content</a>
<header>... site navigation ...</header>
<main id="main" tabindex="-1">
  <h1>Manage subscriptions</h1>
  <nav aria-label="Breadcrumb"><ol>... current page ...</ol></nav>
</main>
```

Make the skip link visible on focus and verify that activation positions sequential navigation and actual focus appropriately. Be cautious with `tabindex="-1"`: it can accept programmatic focus, but does not make all content part of Tab order. In single-page apps, update `document.title`, identify active page and manage focus/announcements on route changes. Do not announce route updates twice.

Use descriptive link labels: “View invoice INV-1034” instead of “Click here”; a table-cell context may be sufficient for A if programmatically determinable, but link-only AAA benefits from self-contained labels. A link should navigate; a button should perform an action. Use consistent headings and genuine section headings for long documents.

## Audit matrix

Review multiple routes from same site, nested sections, states after route transitions and full user processes. For each: document title, heading outline, working bypass, link list context, alternate discovery mechanism, breadcrumb/location information where AAA applies. Check with browser keyboard, screen reader landmarks/headings/links lists and direct deep links. Explicitly record 2.4.5 process-step exceptions; do not turn them into blanket exemptions for all multi-step apps.

## Common misses

Hidden skip links that never become visible; links to missing IDs; same title on every route; icon-only link named “button”; visually grouped links with no programmatically associated context; heading hierarchy used only to achieve desired font size; breadcrumbs missing current-page indication; search that can only find content already shown in a menu and does not constitute a meaningful second way.
