---
name: gask
description: Compatibility shim for the legacy async Gemini delegation skill from claude-ccb-skills. Use only when the user explicitly delegates to Gemini.
metadata:
  compatibility: legacy-claude-ccb-skills
  canonical-skill: ccb-unified
---

# Ask Gemini (Compatibility)

This compatibility skill preserves the legacy `gask` entrypoint from `claude-ccb-skills`.

Canonical CCB orchestration now lives in `../ccb-unified/SKILL.md`.

## Execution (MANDATORY)

```
Bash(gask <<'EOF'
$ARGUMENTS
EOF
, run_in_background=true)
```

## Rules

- After running `gask`, say "Gemini processing..." and immediately end your turn.
- Do not wait for results or check status in the same turn.
- Use only when the user explicitly delegates to Gemini, not for questions about Gemini itself.

## Notes

- If it fails, check backend health with `gping`.
- For new orchestration flows, prefer `ccb-unified`.
