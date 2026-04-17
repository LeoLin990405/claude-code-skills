---
name: pend
description: Compatibility shim for the legacy provider-reply fetch skill from claude-ccb-skills. Use only when the user explicitly asks to fetch provider replies.
metadata:
  compatibility: legacy-claude-ccb-skills
  canonical-skill: ccb-unified
---

# Pend Provider (Compatibility)

This compatibility skill preserves the legacy `pend` entrypoint from `claude-ccb-skills`.

Canonical CCB orchestration now lives in `../ccb-unified/SKILL.md`.

## Execution (MANDATORY)

```
Bash(pend $ARGUMENTS)
```

## Rules

- Arguments must start with the provider name, for example `gemini`.
- Only use when the user explicitly requests results.
- Keep this shim to preserve the legacy installed skill name.
