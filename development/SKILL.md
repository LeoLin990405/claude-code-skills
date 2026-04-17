---
name: developer-toolkit
description: Cross-category developer toolkit router for skill creation, MCP servers, documentation lookup, testing, internal comms, and note processing.
version: 2.1.0
triggers:
  - developer toolkit
  - dev tools
  - create skill
  - MCP server
  - anthropic docs
  - webapp testing
  - test plan
  - internal comms
  - history notes
---

# Developer Toolkit

This toolkit restores the workflow router that previously lived in `claude-skills/utility`. The underlying skills now span `development/`, `ai-collaboration/`, `system/`, and `research/`.

## Routing Guide

| User Intent | Skill | Templates |
|---|---|---|
| Create a new skill, update SKILL.md structure, package a skill | [skill-creator](skill-creator/SKILL.md) | [skill-spec](skill-creator/templates/skill-spec.md) |
| Build an MCP server, define tools/resources, FastMCP or TypeScript SDK | [mcp-builder](mcp-builder/SKILL.md) | [mcp-server-spec](mcp-builder/templates/mcp-server-spec.md) |
| Anthropic docs, Claude API, model selection, Claude Code features | [anthropic-docs](../ai-collaboration/anthropic-docs/SKILL.md) | - |
| Write status reports, leadership updates, newsletters, incident reports | [internal-comms](../system/internal-comms/SKILL.md) | - |
| Test web apps, Playwright, screenshots, browser debugging | [webapp-testing](webapp-testing/SKILL.md) | [test-plan](webapp-testing/templates/test-plan.md) |
| Process history notes, exports, academic research notes | [history-note-processor](../research/history-note-processor/SKILL.md) | - |
| Repository structure, README, CI/CD, release hygiene | [github-repo-design](github-repo-design/SKILL.md) | - |

## Quick Actions

- **"Create a new skill"** -> [skill-creator](skill-creator/SKILL.md) + [skill-spec](skill-creator/templates/skill-spec.md)
- **"Build an MCP server"** -> [mcp-builder](mcp-builder/SKILL.md) + [mcp-server-spec](mcp-builder/templates/mcp-server-spec.md)
- **"Test my web app"** -> [webapp-testing](webapp-testing/SKILL.md) + [test-plan](webapp-testing/templates/test-plan.md)
- **"Write a status report"** -> [internal-comms](../system/internal-comms/SKILL.md)
- **"Look up Anthropic docs"** -> [anthropic-docs](../ai-collaboration/anthropic-docs/SKILL.md)
- **"Process history notes"** -> [history-note-processor](../research/history-note-processor/SKILL.md)
