---
name: qask
description: Compatibility shim for the legacy async Qwen delegation skill from claude-ccb-skills. Use only when the user explicitly delegates to Qwen.
metadata:
  compatibility: legacy-claude-ccb-skills
  canonical-skill: ccb-unified
---

# Ask Qwen (Compatibility)

This compatibility skill preserves the legacy `qask` entrypoint from `claude-ccb-skills`.

Canonical CCB orchestration now lives in `../ccb-unified/SKILL.md`.

## Execution (MANDATORY)

```
Bash(qask <<'EOF'
$ARGUMENTS
EOF
, run_in_background=true)
```

## Rules

- After running `qask`, say "Qwen processing..." and immediately end your turn.
- Do not wait for results or check status in the same turn.
- Use only when the user explicitly delegates to Qwen, not for questions about Qwen itself.

## Notes

- If it fails, check backend health with `qping`.
- For new orchestration flows, prefer `ccb-unified`.
