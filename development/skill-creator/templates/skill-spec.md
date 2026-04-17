# Skill Specification

> Fill in each section to define a new Claude Code skill. Remove sections that do not apply.

## Overview

| Field | Value |
|-------|-------|
| **Name** | `my-skill` |
| **Description** | _What this skill does in one sentence_ |
| **Version** | `1.0.0` |
| **Category** | Development / Knowledge / Communication / Testing / Research |

## Triggers

When should Claude activate this skill?

| Trigger Phrase | Example User Message |
|---------------|---------------------|
| `keyword1` | "Help me with keyword1" |
| `keyword2` | "I need to keyword2 something" |
| _pattern_ | _Example_ |

## Workflow

Step-by-step workflow this skill follows when activated.

### Step 1: _Gather Context_

- What information to collect from the user
- What files or resources to read
- What assumptions to validate

### Step 2: _Execute_

- Core actions the skill performs
- Decision points and branching logic
- Tools or commands to invoke

### Step 3: _Deliver Output_

- Output format and structure
- Where to write results (file, stdout, clipboard)
- Follow-up suggestions

## Resources

Files and knowledge this skill needs access to.

| Resource | Path / Location | Purpose |
|----------|----------------|---------|
| Knowledge base | `knowledge/` | Reference documents |
| Templates | `templates/` | Output templates |
| Examples | `examples/` | Sample inputs/outputs |

## SKILL.md Frontmatter

```yaml
---
name: my-skill
description: _One-sentence description_
version: 1.0.0
triggers:
  - keyword1
  - keyword2
  - phrase pattern
---
```

## Instructions Outline

Key sections for the SKILL.md body:

1. **Role** -- Who Claude becomes when using this skill
2. **Input Format** -- What the user provides
3. **Process** -- Step-by-step instructions
4. **Output Format** -- Structure and format of the result
5. **Constraints** -- Limits, anti-patterns, edge cases
6. **Examples** -- Input/output pairs

## File Structure

```
my-skill/
  SKILL.md          # Main skill definition
  knowledge/        # Reference documents (optional)
  templates/        # Output templates (optional)
  examples/         # Example inputs/outputs (optional)
```

## Testing Checklist

- [ ] Skill activates on each trigger phrase
- [ ] Skill does NOT activate on unrelated requests
- [ ] Output matches expected format
- [ ] Edge cases handled (empty input, very long input, ambiguous request)
- [ ] Knowledge base files are readable and up to date
- [ ] Skill works alongside other skills without conflicts
- [ ] Instructions are unambiguous (no room for misinterpretation)

## Anti-Patterns

| Avoid | Do Instead |
|-------|-----------|
| Overly broad triggers | Use specific, distinctive trigger phrases |
| Monolithic SKILL.md | Split large knowledge into `knowledge/` files |
| Hardcoded paths | Use relative paths from skill root |
| Vague instructions | Give concrete examples of expected behavior |
