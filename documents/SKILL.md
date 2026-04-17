---
name: document-toolkit
description: Complete document processing toolkit - 5 format skills, 3 workflow guides, and 3 templates for PDF, Word, Excel, PowerPoint, and collaborative review.
version: 2.1.0
triggers:
  - document
  - office
  - pdf
  - docx
  - xlsx
  - pptx
  - proposal
  - report
  - meeting notes
  - document review
---

# Document Toolkit

This toolkit restores the format-and-workflow router that previously lived in `claude-skills/office`.

## Routing Guide

| User Intent | Skill | Quick Templates |
|---|---|---|
| PDF extract, create, merge, split, fill forms | [pdf](pdf/SKILL.md) | - |
| Word documents: create, edit, format, styles, tables | [docx](docx/SKILL.md) | [report-structure](doc-coauthoring/templates/report-structure.md), [proposal-structure](doc-coauthoring/templates/proposal-structure.md), [meeting-notes](doc-coauthoring/templates/meeting-notes.md) |
| Excel: formulas, charts, pivot tables, data analysis | [xlsx](xlsx/SKILL.md) | - |
| PowerPoint: slides, layouts, charts, animations | [pptx](pptx/SKILL.md) | - |
| Collaborative editing, track changes, review cycles | [doc-coauthoring](doc-coauthoring/SKILL.md) | - |
| Data analysis to presentation pipeline | - | [data-to-presentation](doc-coauthoring/workflows/data-to-presentation.md) |
| Document draft/review/finalize cycle | - | [document-review-cycle](doc-coauthoring/workflows/document-review-cycle.md) |
| PDF form extraction and processing | - | [pdf-form-processing](doc-coauthoring/workflows/pdf-form-processing.md) |

## Quick Actions

- **"Create a business report"** -> [docx](docx/SKILL.md) + [report-structure](doc-coauthoring/templates/report-structure.md)
- **"Write a proposal"** -> [docx](docx/SKILL.md) + [proposal-structure](doc-coauthoring/templates/proposal-structure.md)
- **"Take meeting notes"** -> [docx](docx/SKILL.md) + [meeting-notes](doc-coauthoring/templates/meeting-notes.md)
- **"Merge these PDFs"** -> [pdf](pdf/SKILL.md)
- **"Build slides from this data"** -> [data-to-presentation](doc-coauthoring/workflows/data-to-presentation.md)
- **"Review and redline this document"** -> [document-review-cycle](doc-coauthoring/workflows/document-review-cycle.md)

## Skills

| Skill | Scope |
|---|---|
| [pdf](pdf/SKILL.md) | Extract text/tables/images, create, merge, split, fill forms |
| [docx](docx/SKILL.md) | Create, edit, format with styles, tables, images, comments |
| [xlsx](xlsx/SKILL.md) | Formulas, charts, pivot tables, validation, recalculation |
| [pptx](pptx/SKILL.md) | Slides, layouts, charts, animations, notes |
| [doc-coauthoring](doc-coauthoring/SKILL.md) | Collaborative review workflows, templates, and redline structure |
