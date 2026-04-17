---
name: all-plan
description: Compatibility shim for the legacy multi-provider collaborative planning workflow from claude-ccb-skills. Use when the user explicitly asks for all-plan or wants broad cross-provider planning.
metadata:
  compatibility: legacy-claude-ccb-skills
  canonical-skill: ccb-unified
---

# All Plan (Compatibility)

This compatibility skill preserves the legacy `all-plan` entrypoint from `claude-ccb-skills`.

The canonical implementation now lives in `../ccb-unified/SKILL.md`, especially the unified discussion and planning workflow.

## How To Use

- Use when the user explicitly asks for `all-plan`.
- Gather planning input across the mounted providers.
- Synthesize the outputs into one concrete execution plan.

## Notes

- Prefer `ccb-unified` for new work.
- Keep this shim to preserve the installed legacy skill name.
