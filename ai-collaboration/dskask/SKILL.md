---
name: dskask
description: Compatibility shim for the legacy async DeepSeek delegation skill from claude-ccb-skills. Use only when the user explicitly delegates to DeepSeek.
metadata:
  compatibility: legacy-claude-ccb-skills
  canonical-skill: ccb-unified
---

# Ask DeepSeek (Compatibility)

This compatibility skill preserves the legacy `dskask` entrypoint from `claude-ccb-skills`.

Canonical CCB orchestration now lives in `../ccb-unified/SKILL.md`.

## Execution (MANDATORY)

```
Bash(dskask <<'EOF'
$ARGUMENTS
EOF
, run_in_background=true)
```

## Rules

- After running `dskask`, say "DeepSeek processing..." and immediately end your turn.
- Do not wait for results or check status in the same turn.
- Use only when the user explicitly delegates to DeepSeek, not for questions about DeepSeek itself.

## Notes

- If it fails, check backend health with `dskping`.
- For new orchestration flows, prefer `ccb-unified`.
