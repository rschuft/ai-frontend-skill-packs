# Alternatives and timed media — diagnostic and repair playbook

**Primary criteria:** 1.1.1, 1.2.1–1.2.9, 1.4.7. Normative: https://www.w3.org/TR/WCAG21/#text-alternatives and https://www.w3.org/TR/WCAG21/#time-based-media. Read criterion-specific W3C Understanding page before relying on exceptions.

## Differential diagnosis

1. **Static non-text content (1.1.1):** Is the image functional, informative, complex, decorative or a CAPTCHA? Its accessible alternative depends on purpose. A magnifying-glass *button* needs an action name; a decorative swirl needs `alt=""`; a graph needs both a short identification and equivalent relationships and values in text/table.
2. **Audio-only vs video-only (1.2.1):** Prerecorded speech-only audio needs complete text alternative; silent instructional video needs text or corresponding audio; neither should be misclassified as prerecorded synchronized media.
3. **Synchronized prerecorded audio+video (1.2.2, 1.2.3, 1.2.5):** Captions convey speech and meaningful audio; description conveys visual information absent from ordinary audio. A transcript is not an AA substitute for required audio description; Level A 1.2.3 permits description **or** complete media alternative.
4. **Live synchronized media (1.2.4):** Check caption availability during event. Post-event transcripts cannot repair the live barrier.
5. **AAA extras:** Sign language (1.2.6), extended description where ordinary gaps cannot fit (1.2.7), comprehensive time-based media alternative (1.2.8), live audio-only alternative (1.2.9), and controlled background speech interference (1.4.7).

## Repair patterns

**Informative / decorative / functional images**

```html
<img src="logo-symbol.svg" alt="" /> <!-- decorative when neighboring text already names brand -->
<a href="/invoices" aria-label="View invoices"><svg aria-hidden="true" focusable="false">...</svg></a>
<img src="sales-trend.svg" alt="Sales increased each month; detailed data follows" />
<table><caption>Monthly sales</caption><!-- full values and row/column headers --></table>
```

Where image is the only content of a link, it must convey the link's function; if contextual adjacent text already labels a control, avoid a competing name. Don't use `aria-label` redundantly on real text links. Chart equivalents should preserve axes, scale, exceptional changes and information needed for the task, not merely describe colors.

**Synchronized media:** Use selectable caption track, editorially reviewed timing and speakers, and a described version or selectable audio-description track at AA. Distinguish true closed captions from subtitles containing only spoken words. Verify caption quality using actual media, not the presence of `<track>` alone. For live events, test the service *live* including latency and gaps. Provide transcript as an additional benefit when practical, not as a substitute for all SCs.

## Negative cases

- `alt="image of chart"` is not equivalent information.
- CSS background image carrying instructions without textual equivalent.
- Captions missing alarms, laughter or change of speaker.
- Auto-generated subtitles published without checking names, timing or accuracy.
- Silent video wrongly given speech captions while important actions remain undocumented.
- CAPTCHA with only an audio alternative that is itself inaccessible to other groups.

## Validation contract

Collect representative assets **including every unique media type**, not just a homepage sample. For each: modality, purpose, supplied alternative, authoring source, media duration, reviewer, target SC, manual equivalence assessment and result. Check keyboard access to all alternative tracks; capture that the alternative is perceivable with screen reader, text-only view and user-selected captions. A scanning tool can detect a missing `alt` attribute but cannot establish that the alternative is accurate or sufficient.
