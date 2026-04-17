---
name: ccb-launcher
description: Compatibility shim for the legacy CCB environment bootstrap workflow from claude-ccb-skills. Use when the user wants to start CCB, check CCB status, launch WezTerm, or troubleshoot the local CCB environment.
metadata:
  compatibility: legacy-claude-ccb-skills
  canonical-skill: ccb-unified
---

# CCB Launcher (Compatibility)

This compatibility skill preserves the legacy `ccb-launcher` entrypoint from `claude-ccb-skills`.

Canonical orchestration now lives in `../ccb-unified/SKILL.md`, but this shim keeps the legacy launch workflow available as an installed leaf skill.

## Core Workflow

1. Validate the environment with `ccb -v`, `python3 --version`, and `echo $TERM_PROGRAM`.
2. If the user is not already in WezTerm or tmux, launch WezTerm with `open -a WezTerm` and tell the user to run `ccb` there.
3. Check configuration with `cat ~/.ccb/ccb.config`.
4. Recommend launch commands such as `ccb`, `ccb codex gemini`, or `ccb -r`.
5. Use provider health checks like `cping`, `gping`, `oping`, `iping`, `kping`, `qping`, `dskping`, and `dping` when troubleshooting.

## Notes

- CCB must run interactively inside WezTerm or tmux.
- Keep this shim for legacy entrypoint compatibility.
- Prefer `ccb-unified` for new multi-provider orchestration flows.
