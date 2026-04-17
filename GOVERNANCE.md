# Repository Governance

This document defines the repository-level rules for skill packaging, install surface, submodule decisions, and source-repo retirement.

## Canonical Surface

The canonical public surface of this repository is:

- category toolkit routers such as `productivity/SKILL.md` and `ai-collaboration/SKILL.md`
- bundled skill directories that contain `SKILL.md`
- selected upstream submodules that remain independently maintained

Legacy compatibility wrappers may remain in-repo, but they are not the preferred canonical entry points for new installs.

## Install Profiles

Two install profiles are supported:

| Profile | Command | Purpose |
|---|---|---|
| Default | `./install.sh` | Preserve backward compatibility and install the full repo surface |
| Canonical only | `./install.sh --canonical-only` | Install the smallest supported canonical surface for new setups |

`--canonical-only` skips legacy compatibility wrappers, but still installs toolkit routers and canonical skills.

## Installable Unit Rules

A directory counts as an installable skill only if it contains `SKILL.md`.

Implications:

- directories like `templates/`, `references/`, `scripts/`, and `examples/` are support assets, not installable skills
- `install.sh` should only count and link directories that contain `SKILL.md`
- repo-level skill counts should follow the same rule as the installer

## Skill Packaging Types

This repository uses four packaging types:

| Type | Description | Preferred Use |
|---|---|---|
| Bundled canonical skill | Lives directly in this repo | Default for thin skills and unified repo-owned skills |
| External submodule | Upstream maintained outside this repo | Keep as submodule unless there is a strong reason to vendor |
| Self-owned submodule | Owned by this account but still independently maintained | Keep only when independent release surface is still valuable |
| Compatibility wrapper | Legacy entrypoint preserved for backward compatibility | Keep in-repo when needed, but avoid surfacing as the primary path for new installs |

## Self-Owned Submodule Policy

Self-owned submodules should be retained only when they still have meaningful independent value outside this monorepo.

Strong reasons to keep a self-owned submodule:

- it has its own release or version history
- it has standalone scripts or executable helpers
- it includes examples, onboarding docs, or contributor workflow that are useful outside the monorepo
- it is treated as an independent canonical repo by existing users or links

Strong reasons to vendor instead:

- it is only a thin skill package with little or no independent tooling surface
- the monorepo is already the clear canonical home
- keeping it as a submodule adds coordination cost without preserving real independent value

## Current Decisions

Current self-owned submodule decisions are:

| Path | Source Repo | Decision | Reason |
|---|---|---|---|
| `development/r-analytics` | `LeoLin990405/r-analytics-skill` | Keep independent | Still treated as its own canonical repo |
| `documents/mineru` | `LeoLin990405/mineru-skill` | Keep independent | Still has standalone script, examples, changelog, and contributor surface |

Previously vendored self-owned submodules:

| Path | Former Source Repo | Outcome |
|---|---|---|
| `productivity/obsidian-cli` | `LeoLin990405/obsidian-cli-skill` | Vendored, source repo archived |
| `development/github-repo-design` | `LeoLin990405/github-repo-design-skill` | Vendored, source repo archived |

## Compatibility Wrapper Policy

Compatibility wrappers may remain in-repo when they protect existing entrypoints, installs, or user habits.

Rules:

- do not remove compatibility wrappers just to reduce directory count
- do not present compatibility wrappers as the primary install surface for new users
- prefer `--canonical-only` for clean new installs
- prefer toolkit routers and canonical skills in docs and examples

## Source Repo Retirement Checklist

Before retiring a source repo, verify all of the following:

1. The canonical target already exists in this repo.
2. The source repo is not preserving a meaningful independent release surface.
3. README and root `SKILL.md` can be replaced with redirect text without breaking the canonical path.
4. Install and docs references in this repo no longer depend on the source repo as a live submodule.

Only after that should the source repo be redirected and archived.
