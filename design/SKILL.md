---
name: design-toolkit
description: Complete design toolkit - 7 specialized skills, 3 templates, and a workflow router for visual design, frontend design, theming, and design-system work.
version: 2.1.0
triggers:
  - design
  - visual design
  - generative art
  - design system
  - style guide
  - frontend design
  - theme
  - brand
  - poster
  - GIF
---

# Design Toolkit

This toolkit restores the workflow-level entry point that previously lived in `claude-skills/design`. Use it when the user needs design intent routing rather than jumping straight to one leaf skill.

## Routing Guide

| User Intent | Primary Skills | Templates |
|---|---|---|
| Generative visuals, procedural art, animated assets | [algorithmic-art](../development/algorithmic-art/SKILL.md), [slack-gif-creator](slack-gif-creator/SKILL.md) | [design-brief](templates/design-brief.md) |
| Posters, brand-aligned visuals, canvas compositions | [canvas-design](canvas-design/SKILL.md), [brand-guidelines](brand-guidelines/SKILL.md) | [design-brief](templates/design-brief.md), [style-guide](templates/style-guide.md) |
| UI systems, themed interfaces, React artifacts | [frontend-design](../development/frontend-design/SKILL.md), [web-artifacts-builder](../development/web-artifacts-builder/SKILL.md), [theme-factory](theme-factory/SKILL.md) | [design-brief](templates/design-brief.md), [design-review-checklist](templates/design-review-checklist.md) |
| Design standards, consistency, review, accessibility | Use this router with [style-guide](templates/style-guide.md) and [design-review-checklist](templates/design-review-checklist.md) | [style-guide](templates/style-guide.md), [design-review-checklist](templates/design-review-checklist.md) |

## Quick Actions

- **"Create generative art"** -> [algorithmic-art](../development/algorithmic-art/SKILL.md)
- **"Design a poster"** -> [canvas-design](canvas-design/SKILL.md)
- **"Apply brand constraints"** -> [brand-guidelines](brand-guidelines/SKILL.md)
- **"Build a themed UI"** -> [frontend-design](../development/frontend-design/SKILL.md) + [theme-factory](theme-factory/SKILL.md)
- **"Create a React artifact"** -> [web-artifacts-builder](../development/web-artifacts-builder/SKILL.md)
- **"Review design quality"** -> [design-review-checklist](templates/design-review-checklist.md)
- **"Define tokens and standards"** -> [style-guide](templates/style-guide.md)

## Templates

| Template | Use Case |
|---|---|
| [design-brief](templates/design-brief.md) | Scope a visual, UI, or motion design project |
| [style-guide](templates/style-guide.md) | Define tokens, typography, spacing, and component rules |
| [design-review-checklist](templates/design-review-checklist.md) | Review hierarchy, consistency, accessibility, and performance |

## Related Skills

- [cli-demo-gif](cli-demo-gif/SKILL.md) for terminal demos rendered as GIFs
- [asciinema-recorder](asciinema-recorder/SKILL.md) for terminal capture workflows
- `design/web-asset-generator` remains available as a submodule-backed asset utility
