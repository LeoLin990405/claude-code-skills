# Design Review Checklist: [Project Name]

**Reviewer**: [Name]
**Date**: [Date]
**Design Version**: [v1.0 / v1.1 / ...]
**Status**: Pass | Pass with Notes | Needs Revision

---

## 1. Visual Hierarchy

- [ ] Most important element is immediately obvious (< 3 seconds)
- [ ] Clear reading order - eye flows from primary to secondary to tertiary
- [ ] Headings, subheadings, and body text have distinct visual weight
- [ ] CTAs stand out from surrounding content
- [ ] Whitespace is used intentionally to group related elements
- [ ] No competing focal points - one primary action per view

**Notes**: [Any observations]

---

## 2. Consistency

- [ ] Colors match the defined style guide / palette
- [ ] Typography uses only approved fonts and sizes from the type scale
- [ ] Spacing follows the spacing scale (no magic numbers)
- [ ] Border radius is consistent across similar elements
- [ ] Icon style is uniform (all outlined OR all filled, not mixed)
- [ ] Button styles match defined variants (primary, secondary, ghost)
- [ ] Component patterns are reused, not reinvented per page/section

**Notes**: [Any observations]

---

## 3. Brand Alignment

- [ ] Design reflects brand personality and tone
- [ ] Logo usage follows brand guidelines (clear space, minimum size)
- [ ] Color usage stays within brand palette
- [ ] Typography aligns with brand fonts
- [ ] Imagery style is consistent with brand direction
- [ ] No elements contradict brand guidelines

**Notes**: [Any observations]

---

## 4. Accessibility

### Color and Contrast
- [ ] Text contrast ratio meets WCAG AA (4.5:1 normal, 3:1 large text)
- [ ] Color is not the sole indicator of meaning (error = red + icon + text)
- [ ] Interactive elements have visible focus indicators
- [ ] Links are distinguishable from surrounding text (underline or distinct color)

### Readability
- [ ] Body text is 16px or larger
- [ ] Line length is 65-75 characters maximum
- [ ] Line height is at least 1.5 for body text
- [ ] Sufficient spacing between interactive targets (44px minimum touch target)

### Motion
- [ ] Animations respect `prefers-reduced-motion`
- [ ] No content relies solely on animation to convey information
- [ ] No flashing content (3 flashes per second max)

**Notes**: [Any observations]

---

## 5. Responsiveness

- [ ] Layout works at mobile (375px), tablet (768px), and desktop (1440px)
- [ ] Text remains readable at all breakpoints (no overflow, no tiny text)
- [ ] Images scale appropriately (no stretching, no cropping of key content)
- [ ] Navigation adapts for touch vs. pointer input
- [ ] No horizontal scroll at any breakpoint
- [ ] Touch targets are at least 44x44px on mobile

**Notes**: [Any observations]

---

## 6. Performance

- [ ] Images are optimized (WebP/AVIF preferred, appropriate dimensions)
- [ ] SVGs are used for icons and simple graphics (not raster)
- [ ] No unnecessary decorative elements that add load time
- [ ] Fonts are subsetted to required characters (if custom)
- [ ] Critical CSS is minimal; no large unused stylesheets
- [ ] Animations use transform/opacity only (GPU-accelerated, no layout thrash)
- [ ] GIFs are under 1MB for web use; under 500KB for Slack

**Notes**: [Any observations]

---

## 7. Content and Copy

- [ ] Placeholder text has been replaced with real content
- [ ] Text is free of typos and grammatical errors
- [ ] Microcopy is clear and actionable (button labels, error messages)
- [ ] Empty states have helpful guidance (not just "No data")
- [ ] Error messages explain what went wrong and how to fix it

**Notes**: [Any observations]

---

## 8. Edge Cases

- [ ] Long text content is handled gracefully (truncation, wrapping)
- [ ] Empty states are designed (no data, first use, error)
- [ ] Loading states are designed (skeleton, spinner, progress)
- [ ] Extreme data is handled (0 items, 1000+ items)
- [ ] Missing images have fallback (placeholder, alt text)

**Notes**: [Any observations]

---

## Summary

| Category | Status | Priority Issues |
|----------|--------|-----------------|
| Visual Hierarchy | Pass / Needs Work | [issues] |
| Consistency | Pass / Needs Work | [issues] |
| Brand Alignment | Pass / Needs Work | [issues] |
| Accessibility | Pass / Needs Work | [issues] |
| Responsiveness | Pass / Needs Work | [issues] |
| Performance | Pass / Needs Work | [issues] |
| Content | Pass / Needs Work | [issues] |
| Edge Cases | Pass / Needs Work | [issues] |

### Overall Verdict
- [ ] **Approved** - Ready to ship
- [ ] **Approved with notes** - Ship after addressing minor items
- [ ] **Revision needed** - Address priority issues and re-review

### Action Items

| # | Issue | Severity | Owner | Status |
|---|-------|----------|-------|--------|
| 1 | [description] | High / Med / Low | [name] | [pending] |
| 2 | [description] | High / Med / Low | [name] | [pending] |
