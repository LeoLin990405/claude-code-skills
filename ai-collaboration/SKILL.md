---
name: coordination-toolkit
description: Multi-AI coordination toolkit router for provider delegation, orchestration patterns, compatibility wrappers, and unified collaboration workflows.
version: 2.1.0
triggers:
  - multi-ai
  - coordination
  - delegate
  - ask provider
  - all-plan
  - ccb
  - pend
  - ping
  - consensus
  - parallel review
---

# Coordination Toolkit

This toolkit restores the umbrella-level coordination router that previously lived in `claude-skills/ccb`.

## Routing Guide

| User Intent | Skill | Supporting Assets |
|---|---|---|
| Use the unified CCB orchestration platform | [ccb-unified](ccb-unified/SKILL.md) | `ccb-unified/references/`, `ccb-unified/templates/` |
| Delegate to one provider by explicit name | [ask](ask/SKILL.md) or provider-specific wrappers | - |
| Delegate to Codex, Gemini, OpenCode, Kimi, Qwen, DeepSeek, iFlow, Droid | [cask](cask/SKILL.md), [gask](gask/SKILL.md), [oask](oask/SKILL.md), [kask](kask/SKILL.md), [qask](qask/SKILL.md), [dskask](dskask/SKILL.md), [iask](iask/SKILL.md), [dask](dask/SKILL.md) | - |
| Check replies or provider health | [pend](pend/SKILL.md), [ping](ping/SKILL.md) | - |
| Plan with multiple providers in parallel | [all-plan](all-plan/SKILL.md) | [flow.md](all-plan/references/flow.md) |
| Specialist collaboration inside Claude Code | [agent-teams](agent-teams/SKILL.md), [find-skills](find-skills/SKILL.md) | - |

## Quick Actions

- **"Ask Codex to review this"** -> [cask](cask/SKILL.md)
- **"Ask Gemini to analyze this"** -> [gask](gask/SKILL.md)
- **"Get multiple model opinions"** -> [all-plan](all-plan/SKILL.md)
- **"Use the unified CCB flow"** -> [ccb-unified](ccb-unified/SKILL.md)
- **"Check if a provider replied"** -> [pend](pend/SKILL.md)
- **"Check provider connectivity"** -> [ping](ping/SKILL.md)

## Compatibility Notes

- Legacy top-level provider wrappers from the old `claude-skills/ccb` layout are preserved here as first-class skills.
- Reusable orchestration references now live under [ccb-unified](ccb-unified/SKILL.md) and [all-plan](all-plan/SKILL.md).
- New installs can skip these legacy wrappers with `./install.sh --canonical-only`.
