# Style Guide: [Project/Brand Name]

**Version**: 1.0
**Last Updated**: [Date]
**Owner**: [Name]

---

## 1. Color Palette

### Primary Colors

| Name | Hex | RGB | Usage |
|------|-----|-----|-------|
| [Primary] | `#______` | `rgb(_, _, _)` | Main brand color, CTAs, key accents |
| [Secondary] | `#______` | `rgb(_, _, _)` | Supporting elements, secondary actions |
| [Accent] | `#______` | `rgb(_, _, _)` | Highlights, notifications, emphasis |

### Neutral Colors

| Name | Hex | Usage |
|------|-----|-------|
| [Background] | `#______` | Page background |
| [Surface] | `#______` | Card/panel backgrounds |
| [Border] | `#______` | Dividers, borders |
| [Text Primary] | `#______` | Body text, headings |
| [Text Secondary] | `#______` | Captions, placeholders |
| [Text Muted] | `#______` | Disabled states |

### Semantic Colors

| Name | Hex | Usage |
|------|-----|-------|
| [Success] | `#______` | Positive actions, confirmations |
| [Warning] | `#______` | Caution states |
| [Error] | `#______` | Error states, destructive actions |
| [Info] | `#______` | Informational messages |

### Color Rules
- Minimum contrast ratio: **4.5:1** for normal text, **3:1** for large text (WCAG AA)
- Never use color alone to convey meaning - pair with icons or text
- [Additional project-specific color rules]

---

## 2. Typography

### Font Stack

| Role | Font | Fallback | Weight |
|------|------|----------|--------|
| **Headings** | [Font name] | [system fallback] | Bold (700) |
| **Body** | [Font name] | [system fallback] | Regular (400) |
| **Code/Mono** | [Font name] | `monospace` | Regular (400) |

### Type Scale

| Level | Size | Line Height | Weight | Usage |
|-------|------|-------------|--------|-------|
| **Display** | 48px / 3rem | 1.1 | 700 | Hero headlines |
| **H1** | 36px / 2.25rem | 1.2 | 700 | Page titles |
| **H2** | 28px / 1.75rem | 1.25 | 600 | Section headers |
| **H3** | 22px / 1.375rem | 1.3 | 600 | Subsections |
| **H4** | 18px / 1.125rem | 1.4 | 600 | Card titles |
| **Body** | 16px / 1rem | 1.5 | 400 | Paragraphs |
| **Small** | 14px / 0.875rem | 1.5 | 400 | Captions, labels |
| **Tiny** | 12px / 0.75rem | 1.5 | 400 | Footnotes, legal |

### Typography Rules
- Maximum line length: **65-75 characters** for readability
- Paragraph spacing: **1em** between paragraphs
- [Additional project-specific typography rules]

---

## 3. Spacing

### Spacing Scale

| Token | Value | Usage |
|-------|-------|-------|
| `space-xs` | 4px | Tight gaps, icon padding |
| `space-sm` | 8px | Inline element spacing |
| `space-md` | 16px | Default gap, form fields |
| `space-lg` | 24px | Section padding, card padding |
| `space-xl` | 32px | Between sections |
| `space-2xl` | 48px | Major section breaks |
| `space-3xl` | 64px | Page-level spacing |

### Layout Grid
- **Columns**: [12]
- **Gutter**: [16px / 24px]
- **Margin**: [16px mobile, 24px tablet, auto desktop]
- **Max width**: [1200px / 1440px]

---

## 4. Border Radius

| Token | Value | Usage |
|-------|-------|-------|
| `radius-sm` | 4px | Badges, tags, small buttons |
| `radius-md` | 8px | Cards, inputs, buttons |
| `radius-lg` | 16px | Modals, large containers |
| `radius-full` | 9999px | Avatars, pills |

---

## 5. Shadows

| Token | Value | Usage |
|-------|-------|-------|
| `shadow-sm` | `0 1px 2px rgba(0,0,0,0.05)` | Subtle elevation |
| `shadow-md` | `0 4px 6px rgba(0,0,0,0.07)` | Cards, dropdowns |
| `shadow-lg` | `0 10px 15px rgba(0,0,0,0.1)` | Modals, floating elements |

---

## 6. Components

### Buttons

| Variant | Background | Text | Border | Usage |
|---------|-----------|------|--------|-------|
| **Primary** | [Primary color] | White | None | Main actions |
| **Secondary** | Transparent | [Primary color] | [Primary color] | Secondary actions |
| **Ghost** | Transparent | [Text color] | None | Tertiary actions |
| **Destructive** | [Error color] | White | None | Delete, remove |

### States
- **Hover**: [description - e.g., darken 10%, scale 1.02]
- **Active/Pressed**: [description - e.g., darken 15%, scale 0.98]
- **Focus**: [description - e.g., 2px ring offset with primary color]
- **Disabled**: [description - e.g., 50% opacity, no pointer events]

### Form Inputs
- Border: [1px solid border-color]
- Focus border: [Primary color]
- Error border: [Error color]
- Placeholder color: [Text muted]
- Padding: [space-sm space-md]

---

## 7. Iconography

- **Style**: [Outlined / Filled / Duotone]
- **Size**: [16px / 20px / 24px standard sizes]
- **Stroke width**: [1.5px / 2px]
- **Source**: [Lucide / Heroicons / Phosphor / custom]
- **Color**: Inherit from text color unless semantic

---

## 8. Motion

| Property | Duration | Easing | Usage |
|----------|----------|--------|-------|
| **Micro** | 100-150ms | ease-out | Button press, toggle |
| **Standard** | 200-300ms | ease-in-out | Expand, collapse, fade |
| **Emphasis** | 300-500ms | cubic-bezier(0.4, 0, 0.2, 1) | Page transitions, modals |

### Motion Rules
- Respect `prefers-reduced-motion` - disable non-essential animations
- Entrances: fade + slight translate (8-16px)
- Exits: fade only (faster than entrances)
