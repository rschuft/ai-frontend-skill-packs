# Time, moving content, motion safety — diagnostic and repair playbook

**Primary criteria:** 1.4.2, 2.2.1–2.2.6, 2.3.1–2.3.3. Timing and flashing demand different evidence; do not merge into a single animation test. Reference: https://www.w3.org/TR/WCAG21/#enough-time

## Triage timer behavior

Record who starts a timer, its duration, user control, warning timing, extension count, session persistence and data-loss risk. WCAG 2.1 A **2.2.1** allows at least one path: user can turn off before encountering; set at least 10x duration; warning with >=20 seconds and at least ten extensions; or valid real-time, essential or >20-hour exception. For AAA **2.2.3**, timing cannot be an essential part except for narrow real-time/noninteractive media cases; do not misapply A-level flexibility at AAA. AAA **2.2.6** concerns informing users about potential inactivity-related data loss, and **2.2.5** concerns continuation after reauthentication.

Recommended architecture: persist unsent drafts safely (subject to sensitivity and policy), surface session-warning dialog before expiry, permit meaningful extension where permitted, then restore workflow after reauth without resurrecting the old authenticated session. Treat security risks separately rather than disabling all timeout features.

## Moving and auto-updating content

2.2.2 distinguishes moving/blinking/scrolling content (automatic, presented in parallel and lasting >5 seconds) from auto-updating information (automatic, parallel). Provide pause/stop/hide or control of update frequency where required; consider essential activity exceptions. For autoplay audio lasting >3 seconds (1.4.2), expose pause/stop or independent volume control. A moving stock ticker and a time-critical live status feed deserve different treatment.

## Flash and interaction motion

- **2.3.1 A:** avoid more than three flashes per second or have proof that any flashes stay below general/red flash thresholds. A frequent saturated red flash can be especially risky. Evaluate across GIF, video, canvas, transitions and third-party content.
- **2.3.2 AAA:** no greater-than-three-flashes alternative; remove offending flashes altogether.
- **2.3.3 AAA:** allow disabling **nonessential** motion triggered by interaction; respect `prefers-reduced-motion` including JS animation engines.

```css
@media (prefers-reduced-motion: reduce) {
  .nonessential-motion { animation: none !important; transition: none !important; }
}
```

This CSS does **not** establish 2.3.1 compliance: unsafe flashing must not be allowed in the first place. Avoid flashing effects for untested content. When video may be seizure-inducing, use specialist measurement tools and qualified review rather than visual judgment alone.

## Test evidence

Reproduce each timer with a controllable test clock, capture expiry/extend behavior, round-trip data restoration, and check warning display for keyboard and screen reader. Observe moving content with controls and when hidden behind dialogs. Test reduced-motion preference with CSS and script animation. Report safety-critical flashing conservatively: if measurements are unavailable, mark not tested or needs manual review; do not mark pass.
