---
name: oask
description: Compatibility shim for the legacy async OpenCode delegation skill from claude-ccb-skills. Use only when the user explicitly delegates to OpenCode.
metadata:
  compatibility: legacy-claude-ccb-skills
  canonical-skill: ccb-unified
---

# Ask OpenCode (Compatibility)

This compatibility skill preserves the legacy `oask` entrypoint from `claude-ccb-skills`.

Canonical CCB orchestration now lives in `../ccb-unified/SKILL.md`.

## Execution (MANDATORY)

```
Bash(oask <<'EOF'
$ARGUMENTS
EOF
, run_in_background=true)
```

## Rules

- After running `oask`, say "OpenCode processing..." and immediately end your turn.
- Do not wait for results or check status in the same turn.
- Use only when the user explicitly delegates to OpenCode, not for questions about OpenCode itself.

## Notes

- If it fails, check backend health with `oping`.
- For new orchestration flows, prefer `ccb-unified`.
