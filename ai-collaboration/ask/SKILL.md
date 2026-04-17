---
name: ask
description: Compatibility shim for the legacy async provider delegation skill from claude-ccb-skills. Use only when the user explicitly delegates to a provider with ask <provider> <message>.
metadata:
  compatibility: legacy-claude-ccb-skills
  canonical-skill: ccb-unified
---

# Ask Provider (Compatibility)

This compatibility skill preserves the legacy `ask` entrypoint from `claude-ccb-skills`.

Canonical CCB orchestration now lives in `../ccb-unified/SKILL.md`.

## Execution (MANDATORY)

```
Bash(ask <<'EOF'
$ARGUMENTS
EOF
, run_in_background=true)
```

## Rules

- Arguments must start with the provider name, for example `gemini ...`.
- After running `ask`, say "<Provider> processing..." and end your turn.
- Do not poll or use `pend` unless the user explicitly asks.
- Use this shim only when the user explicitly wants the legacy `ask` workflow.
