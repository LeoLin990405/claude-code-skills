---
name: knowledge-toolkit
description: Obsidian-centered knowledge management toolkit - 3 format skills, 4 templates, and adjacent productivity skills for knowledge capture, organization, and visualization.
version: 2.1.0
triggers:
  - knowledge management
  - obsidian
  - daily note
  - meeting note
  - project tracker
  - canvas
  - markdown
  - bases
  - PKM
  - second brain
---

# Knowledge Toolkit

This toolkit restores the Obsidian workflow router that previously lived in `claude-skills/obsidian`.

## Routing Guide

| User Intent | Skill | Quick Templates |
|---|---|---|
| Note-taking, markdown, wikilinks, callouts, embeds, properties | [obsidian-markdown](obsidian-markdown/SKILL.md) | [daily-note](obsidian-markdown/templates/daily-note.md), [meeting-note](obsidian-markdown/templates/meeting-note.md) |
| Databases, tracking, tables, filters, formulas, status views | [obsidian-bases](obsidian-bases/SKILL.md) | [project-tracker](obsidian-bases/templates/project-tracker.base) |
| Visual mapping, spatial layout, node connections, brainstorming | [json-canvas](json-canvas/SKILL.md) | [research-canvas](json-canvas/templates/research-canvas.canvas) |

## Quick Actions

- **"Create a daily note"** -> [obsidian-markdown](obsidian-markdown/SKILL.md) + [daily-note](obsidian-markdown/templates/daily-note.md)
- **"Set up a project tracker"** -> [obsidian-bases](obsidian-bases/SKILL.md) + [project-tracker](obsidian-bases/templates/project-tracker.base)
- **"Map out a research topic"** -> [json-canvas](json-canvas/SKILL.md) + [research-canvas](json-canvas/templates/research-canvas.canvas)
- **"Take meeting notes"** -> [obsidian-markdown](obsidian-markdown/SKILL.md) + [meeting-note](obsidian-markdown/templates/meeting-note.md)

## Adjacent Productivity Skills

- [knowledge-hub](knowledge-hub/SKILL.md) for Knowledge-Hub workflows and note operations
- [notebooklm](notebooklm/SKILL.md) for NotebookLM notebook orchestration
- `productivity/obsidian-cli` remains available as a submodule-backed CLI skill
