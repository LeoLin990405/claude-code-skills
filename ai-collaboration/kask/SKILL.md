---
name: kask
description: Compatibility shim for the legacy async Kimi delegation skill from claude-ccb-skills. Use only when the user explicitly delegates to Kimi.
metadata:
  compatibility: legacy-claude-ccb-skills
  canonical-skill: ccb-unified
---

# Ask Kimi (Compatibility)

This compatibility skill preserves the legacy `kask` entrypoint from `claude-ccb-skills`.

Canonical CCB orchestration now lives in `../ccb-unified/SKILL.md`.

## Execution (MANDATORY)

```
Bash(kask <<'EOF'
$ARGUMENTS
EOF
, run_in_background=true)
```

## Rules

- After running `kask`, say "Kimi processing..." and immediately end your turn.
- Do not wait for results or check status in the same turn.
- Use only when the user explicitly delegates to Kimi, not for questions about Kimi itself.

## Notes

- If it fails, check backend health with `kping`.
- For new orchestration flows, prefer `ccb-unified`.
