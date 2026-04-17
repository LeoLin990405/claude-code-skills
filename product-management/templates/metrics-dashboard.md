# Metrics Dashboard Spec: [Product/Team]

**Owner**: [Name]
**Date**: [Date]
**Review cadence**: Daily (anomaly) | Weekly (team) | Monthly (business)

---

## 1. North Star Metric

| Metric | Definition | Current | Target | Timeframe |
|--------|-----------|---------|--------|-----------|
| [North star] | [Exact definition - what counts, what doesn't] | [X] | [Y] | [quarterly] |

---

## 2. Input Metrics Tree

```
North Star: [metric]
├── [Input Metric 1] - owned by [team]
│   ├── [Leading Indicator 1a]
│   └── [Leading Indicator 1b]
├── [Input Metric 2] - owned by [team]
│   ├── [Leading Indicator 2a]
│   └── [Leading Indicator 2b]
└── [Input Metric 3] - owned by [team]
    ├── [Leading Indicator 3a]
    └── [Leading Indicator 3b]
```

---

## 3. Metric Definitions

| Metric | Definition | Calculation | Data Source | Owner |
|--------|-----------|-------------|-------------|-------|
| [Metric 1] | [Plain English definition] | [Formula: numerator / denominator] | [Table/event] | [Team] |
| [Metric 2] | [Plain English definition] | [Formula] | [Table/event] | [Team] |
| [Metric 3] | [Plain English definition] | [Formula] | [Table/event] | [Team] |

---

## 4. Health Metrics (guardrails)

These should NOT degrade while we optimize the north star:

| Metric | Acceptable Range | Alert Threshold | Action if Breached |
|--------|-----------------|----------------|-------------------|
| [Error rate] | <1% | >2% | [Pause experiments, investigate] |
| [Page load time] | <2s | >3s | [Performance review] |
| [Support ticket volume] | <[X]/week | >[Y]/week | [UX review] |
| [Customer satisfaction] | >[X] NPS | <[Y] NPS | [User research sprint] |

---

## 5. Dashboard Layout

### Section A: Executive Summary (top of dashboard)
- North star metric with trend (7d, 30d, 90d)
- 3-5 input metrics with sparklines
- Red/yellow/green status for each

### Section B: Acquisition
- New users (daily/weekly)
- Signup conversion rate
- Channel breakdown (organic, paid, referral)
- CAC by channel

### Section C: Activation
- Signup-to-aha-moment conversion
- Time to value (median)
- Onboarding completion rate by step

### Section D: Engagement
- DAU / WAU / MAU
- DAU/MAU ratio (stickiness)
- Core action frequency
- Feature adoption rates

### Section E: Retention
- Retention curve by cohort (D1, D7, D30, D90)
- Churn rate (monthly)
- Resurrection rate

### Section F: Revenue (if applicable)
- MRR / ARR
- ARPU
- LTV
- LTV/CAC ratio
- Net revenue retention

---

## 6. Review Cadence

| Review | Frequency | Attendees | Focus | Duration |
|--------|-----------|-----------|-------|----------|
| Anomaly check | Daily | On-call PM | Are metrics within normal range? | 5 min |
| Team metrics | Weekly | Product team | Progress against OKRs, experiment results | 30 min |
| Business review | Monthly | Leadership + cross-functional | Revenue, growth, retention cohorts | 60 min |
| Strategy review | Quarterly | Exec team | Are we working on the right things? | 2 hours |

---

## 7. Alerting Rules

| Condition | Severity | Notify | Channel |
|-----------|----------|--------|---------|
| North star drops >10% day-over-day | Critical | PM + Eng Lead | Slack + PagerDuty |
| Health metric breaches threshold | High | PM | Slack |
| Input metric flat for 2+ weeks | Medium | PM | Weekly review |

---

## Setup Checklist

- [ ] Event tracking implemented for all metrics
- [ ] Dashboard built in [tool: Amplitude / Mixpanel / Looker / etc.]
- [ ] Alert rules configured
- [ ] Review cadence on calendar
- [ ] Team aligned on metric definitions (no ambiguity)
