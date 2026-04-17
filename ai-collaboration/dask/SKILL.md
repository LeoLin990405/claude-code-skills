---
name: dask
description: Compatibility shim for the legacy async Droid delegation skill from claude-ccb-skills. Use only when the user explicitly delegates to Droid.
metadata:
  compatibility: legacy-claude-ccb-skills
  canonical-skill: ccb-unified
---

# Ask Droid (Compatibility)

This compatibility skill preserves the legacy `dask` entrypoint from `claude-ccb-skills`.

Canonical CCB orchestration now lives in `../ccb-unified/SKILL.md`.

## Execution (MANDATORY)

```
Bash(dask <<'EOF'
$ARGUMENTS
EOF
, run_in_background=true)
```

## Rules

- After running `dask`, say "Droid processing..." and immediately end your turn.
- Do not wait for results or check status in the same turn.
- Use only when the user explicitly delegates to Droid, not for questions about Droid itself.

## Notes

- If it fails, check backend health with `dping`.
- For new orchestration flows, prefer `ccb-unified`.
