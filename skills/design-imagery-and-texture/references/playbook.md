# Art assets, image hierarchy, iconography and texture playbook

## Discriminators
- Pixelated illustration/logo -> likely a raster scaling or asset-resolution issue, not CSS "sharpness".
- Mismatched photo color grades/icons -> visual unity / art direction.
- Text on image unreadable -> foreground/background contrast and backing; refer to `wcag21-*` for applicable criteria.
- Decorative clutter -> lower ornament, not merely higher z-index.

## Asset decisions
Use SVG for licensed simple vector illustrations, logos and icons where appropriate; use responsive raster/WebP/AVIF/JPEG/PNG for photos as supported. Preserve intrinsic aspect ratio and use `object-fit: cover` only where cropping doesn't hide critical information. Keep `object-position` or focal metadata for art-directed crops. Use `srcset`/`sizes` for realistic rendered sizes; inspect high-DPI sharpness and loading fallbacks.

Keep consistent icon stroke, fill, corner radius and implied lighting. Photography and imagery can share a palette and crop style, but do not edit informational charts/images in ways that misrepresent data. Never package or assume rights to a third-party logo, stock image or commercial font.

## Practical CSS
```css
.media { aspect-ratio: 4 / 3; overflow: hidden; background: var(--color-surface-muted); }
.media img { width: 100%; height: 100%; object-fit: cover; object-position: center 40%; }
/* Important imagery should not be cropped without checking the subject at each width. */
```

For overlaid text, prefer a solid/semi-opaque region with actual WCAG-checked contrast rather than relying on unknown photo tones. Appropriate alt text / decorative decisions belong to the WCAG skills.

## Acceptance
Crops preserve the intended content and brand mood, assets render crisply at expected DPR, fallback is safe, and text is legible on worst-case crops and themes.

Sources: https://www.digitalpolo.com/vector-vs-raster-explained/ · https://www.digitalpolo.com/aesthetic-branding-guide/ · https://www.digitalpolo.com/white-space-in-design/
