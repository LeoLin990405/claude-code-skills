---
name: ping
description: Compatibility shim for the legacy provider-connectivity skill from claude-ccb-skills. Use only when the user explicitly asks for a provider health check.
metadata:
  compatibility: legacy-claude-ccb-skills
  canonical-skill: ccb-unified
---

# Ping Provider (Compatibility)

This compatibility skill preserves the legacy `ping` entrypoint from `claude-ccb-skills`.

Canonical CCB orchestration now lives in `../ccb-unified/SKILL.md`.

## Execution (MANDATORY)

```
Bash(ping $ARGUMENTS)
```

## Rules

- Arguments must start with the provider name, for example `gemini`.
- Only use when the user explicitly asks for a health check.
- Keep this shim to preserve the legacy installed skill name.
