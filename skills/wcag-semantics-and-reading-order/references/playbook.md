# Structure and reading order — diagnostic and repair playbook

**Primary criteria:** 1.3.1, 1.3.2, 1.3.3, 1.3.6. Nearby: 2.4.6, 4.1.2, 2.4.3. Reference: https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships

## Diagnose by three representations

Inspect **(a)** visual layout, **(b)** DOM order and **(c)** accessibility tree output. A screenshot reveals (a), not (b) and (c). Ask what a user needs to learn from the page: section nesting, associations, table header/data relationships, form groups, sequence for multi-column layouts, and which instructions only describe spatial appearance. Identify which representation loses that meaning.

## Semantic implementation

Use HTML's existing semantics before adding ARIA:

```html
<main id="main"><h1>Billing</h1>
  <section aria-labelledby="invoices-heading">
    <h2 id="invoices-heading">Invoices</h2>
    <table>
      <caption>Open invoices</caption>
      <thead><tr><th scope="col">Invoice</th><th scope="col">Amount</th></tr></thead>
      <tbody><tr><th scope="row">INV-12</th><td>$120</td></tr></tbody>
    </table>
  </section>
</main>
```

`<ul>` for collections, `<ol>` for ordered steps, `<fieldset><legend>` for related choices, labels tied to inputs, `<th scope>` or `headers/id` for complex tables. Use names that convey purpose. For chart and diagram information, include alternative semantic representation. For 1.3.6 AAA, verify *accessibility-supported* purpose metadata rather than adding arbitrary unsupported semantics.

## Order discipline

Keep DOM in meaningful reading and focus order. CSS Grid/Flex `order`, reversed columns, absolute positioning or portals may visually reorder content without updating screen-reader order. Prefer a DOM order that works on small screens and progressively enhance layout. Avoid forcing focus with positive `tabindex` to simulate a visual ordering. Check that table headers still associate after responsive transformation and that changing layout does not hide information.

Instructions: “Select the red circle at the right” fails if color/shape/position are the only means to know which target to use. “Select **Delete account**” with a properly named control survives color, zoom, reading order and localization.

## Distinguish failures

- **1.3.1:** visual heading or field group has no programmatic relation.
- **1.3.2:** essential content meaning changes when read linearly.
- **2.4.3:** keyboard focus moves in a sequence that harms meaning or use.
- **4.1.2:** an interactive component has missing name, role or state.
- **1.3.3:** instructions depend only on sensory characteristics.

One symptom can implicate several criteria, but create distinct findings only when each distinct requirement demonstrably fails.

## Validate

Navigate by headings, lists, landmarks and table cells in actual assistive technology. Inspect DOM in browser DevTools. Read a multi-column page with CSS disabled and at 320px-equivalent reflow. Record exact route, component state and assistive technology/browser. An automated tree audit is useful supporting evidence but cannot decide if the sequence is meaningful.
