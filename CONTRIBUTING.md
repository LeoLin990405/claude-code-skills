# Contributing to Claude Code Skills

Thank you for your interest in contributing! This guide covers how to add skills, suggest community skills, and report issues.

## Adding a New Skill

### 1. Create the Skill Directory

```bash
mkdir -p <category>/<skill-name>
```

Choose the appropriate category: `productivity`, `development`, `documents`, `research`, `ai-collaboration`, `product-management`, `security`, `design`, or `system`.

### 2. Create `SKILL.md`

Every skill **must** have a `SKILL.md` file with YAML frontmatter and instructions:

```yaml
---
name: my-skill
description: One-line description of what this skill does
triggers:
  - keyword1
  - keyword2
---

# My Skill

## Instructions

Detailed instructions that Claude Code will follow when this skill is activated.

## Examples

Show example usage and expected behavior.
```

### 3. Add Supporting Files (Optional)

Include any additional files the skill needs (templates, scripts, configs). Keep them inside the skill directory.

### 4. Submit a Pull Request

- Fork the repository
- Create a feature branch: `git checkout -b add-my-skill`
- Add your skill directory and files
- Commit with a clear message: `git commit -m "Add my-skill to development category"`
- Push and open a PR

## Suggesting a Community Skill

If you know of an existing GitHub repo that would make a good skill:

1. Open an issue using the **Skill Request** template
2. Include the repo URL, a description, and which category it fits
3. We will evaluate it for inclusion as a submodule

## Reporting Bugs

Use the **Bug Report** issue template. Include:

- Which skill is affected
- What you expected to happen
- What actually happened
- Your Claude Code version

## Skill Quality Guidelines

- **`SKILL.md` is required** -- it is the entry point Claude Code reads
- **Keep instructions clear and actionable** -- Claude Code follows them literally
- **Include examples** when possible
- **One concern per skill** -- don't bundle unrelated functionality
- **Test your skill** by installing it locally before submitting

## Code of Conduct

Be respectful, constructive, and welcoming. We are building tools to help everyone be more productive with Claude Code.
