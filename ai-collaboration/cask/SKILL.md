---
name: cask
description: Compatibility shim for the legacy async Codex delegation skill from claude-ccb-skills. Use only when the user explicitly delegates to Codex.
metadata:
  compatibility: legacy-claude-ccb-skills
  canonical-skill: ccb-unified
---

# Ask Codex (Compatibility)

This compatibility skill preserves the legacy `cask` entrypoint from `claude-ccb-skills`.

Canonical CCB orchestration now lives in `../ccb-unified/SKILL.md`.

## Execution (MANDATORY)

```
Bash(cask <<'EOF'
$ARGUMENTS
EOF
, run_in_background=true)
```

## Rules

- After running `cask`, say "Codex processing..." and immediately end your turn.
- Do not wait for results or check status in the same turn.
- Use only when the user explicitly delegates to Codex, not for questions about Codex itself.

## Notes

- If it fails, check backend health with `cping`.
- For new orchestration flows, prefer `ccb-unified`.
