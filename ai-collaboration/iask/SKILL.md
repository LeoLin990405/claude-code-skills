---
name: iask
description: Compatibility shim for the legacy async iFlow delegation skill from claude-ccb-skills. Use only when the user explicitly delegates to iFlow.
metadata:
  compatibility: legacy-claude-ccb-skills
  canonical-skill: ccb-unified
---

# Ask iFlow (Compatibility)

This compatibility skill preserves the legacy `iask` entrypoint from `claude-ccb-skills`.

Canonical CCB orchestration now lives in `../ccb-unified/SKILL.md`.

## Execution (MANDATORY)

```
Bash(iask <<'EOF'
$ARGUMENTS
EOF
, run_in_background=true)
```

## Rules

- After running `iask`, say "iFlow processing..." and immediately end your turn.
- Do not wait for results or check status in the same turn.
- Use only when the user explicitly delegates to iFlow, not for questions about iFlow itself.

## Notes

- If it fails, check backend health with `iping`.
- For new orchestration flows, prefer `ccb-unified`.
