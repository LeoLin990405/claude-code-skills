---
name: pm-toolkit
description: Product management toolkit router with workflow guidance, Lenny-derived PM skills, and reusable PM templates for discovery, strategy, execution, growth, and team leadership.
version: 2.1.0
triggers:
  - product management
  - PM toolkit
  - PRD
  - OKR
  - roadmap
  - user research
  - launch checklist
  - retro
  - product strategy
  - growth loops
---

# PM Toolkit

This toolkit restores the workflow-level PM entry point that previously lived in `claude-skills/lenny`.

## Routing Guide

| User Intent | Skill | Quick Templates |
|---|---|---|
| Discovery, interviews, customer understanding, competitive research | [lenny-research](lenny-research/SKILL.md) | [user-interview-script](templates/user-interview-script.md), [competitive-analysis](templates/competitive-analysis.md) |
| Vision, roadmap, PRD, OKRs, prioritization | [lenny-strategy](lenny-strategy/SKILL.md) | [prd-template](templates/prd-template.md), [okr-template](templates/okr-template.md) |
| Execution, launches, retros, decision-making | [lenny-execution](lenny-execution/SKILL.md), [lenny-decision](lenny-decision/SKILL.md) | [launch-checklist](templates/launch-checklist.md), [retro-template](templates/retro-template.md), [decision-doc-template](templates/decision-doc-template.md) |
| Growth, pricing, retention, metrics | [lenny-growth](lenny-growth/SKILL.md) | [metrics-dashboard](templates/metrics-dashboard.md) |
| Hiring, 1:1s, org health, stakeholder communication | [lenny-hiring](lenny-hiring/SKILL.md), [lenny-communication](lenny-communication/SKILL.md) | [one-on-one-template](templates/one-on-one-template.md) |
| PM breadth, category lookup, role-based sequencing | [lenny-skills](lenny-skills/SKILL.md), [lenny-playbooks](lenny-playbooks/SKILL.md) | [financial-model-spec](templates/financial-model-spec.md) |

## Quick Actions

- **"Write a PRD"** -> [lenny-strategy](lenny-strategy/SKILL.md) + [prd-template](templates/prd-template.md)
- **"Set OKRs"** -> [lenny-strategy](lenny-strategy/SKILL.md) + [okr-template](templates/okr-template.md)
- **"Prepare user interviews"** -> [lenny-research](lenny-research/SKILL.md) + [user-interview-script](templates/user-interview-script.md)
- **"Run a retro"** -> [lenny-execution](lenny-execution/SKILL.md) + [retro-template](templates/retro-template.md)
- **"Build a metrics dashboard"** -> [lenny-growth](lenny-growth/SKILL.md) + [metrics-dashboard](templates/metrics-dashboard.md)
- **"Write a decision doc"** -> [lenny-decision](lenny-decision/SKILL.md) + [decision-doc-template](templates/decision-doc-template.md)

## Templates

| Template | Use Case |
|---|---|
| [prd-template](templates/prd-template.md) | Product requirements document |
| [okr-template](templates/okr-template.md) | Quarterly OKRs |
| [user-interview-script](templates/user-interview-script.md) | Interview guide and synthesis sheet |
| [competitive-analysis](templates/competitive-analysis.md) | Market and competitor analysis |
| [decision-doc-template](templates/decision-doc-template.md) | Structured product/technical decision making |
| [financial-model-spec](templates/financial-model-spec.md) | Revenue and unit economics model spec |
| [launch-checklist](templates/launch-checklist.md) | Cross-functional launch readiness |
| [metrics-dashboard](templates/metrics-dashboard.md) | North-star and guardrail dashboard spec |
| [one-on-one-template](templates/one-on-one-template.md) | Manager-report 1:1 template |
| [retro-template](templates/retro-template.md) | Sprint, project, or incident retro |

## Compatibility Wrappers

Legacy `pm-*` entry points from `claude-skills/lenny` are preserved here:

- [pm-discovery](pm-discovery/SKILL.md)
- [pm-strategy](pm-strategy/SKILL.md)
- [pm-execution](pm-execution/SKILL.md)
- [pm-growth](pm-growth/SKILL.md)
- [pm-analytics](pm-analytics/SKILL.md)
- [pm-communication](pm-communication/SKILL.md)
- [pm-team](pm-team/SKILL.md)
- [pm-leadership](pm-leadership/SKILL.md)
- [pm-playbooks](pm-playbooks/SKILL.md)

If you want a smaller canonical install surface, use `./install.sh --canonical-only` to skip these compatibility wrappers.
