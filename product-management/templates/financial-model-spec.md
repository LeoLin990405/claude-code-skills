# Financial Model Spec: [Product/Company]

**Author**: [Name]
**Date**: [Date]
**Model type**: Unit Economics | Revenue Projection | Fundraising | Pricing Analysis

---

## 1. Model Structure

### Tabs / Sheets

| Tab | Purpose | Key Outputs |
|-----|---------|-------------|
| **Assumptions** | All inputs in one place (blue text) | Editable parameters |
| **Revenue** | Revenue build by segment/channel | MRR, ARR, revenue growth |
| **Costs** | COGS + OpEx breakdown | Gross margin, burn rate |
| **Unit Economics** | Per-customer metrics | CAC, LTV, payback, LTV/CAC |
| **Cohort Analysis** | Revenue/retention by signup cohort | Retention curves, net revenue retention |
| **Scenarios** | Best/base/worst case | Range of outcomes |
| **Dashboard** | Charts and summary | Visual overview |

---

## 2. Key Assumptions

### Revenue Assumptions

| Assumption | Base Case | Best Case | Worst Case | Source |
|-----------|-----------|-----------|------------|--------|
| Monthly new customers | [X] | [Y] | [Z] | [historical / benchmark] |
| ARPU | $[X] | $[Y] | $[Z] | [pricing plan] |
| Monthly churn rate | [X]% | [Y]% | [Z]% | [historical / benchmark] |
| Annual growth rate | [X]% | [Y]% | [Z]% | [plan / benchmark] |
| Expansion revenue rate | [X]% | [Y]% | [Z]% | [historical] |

### Cost Assumptions

| Assumption | Value | Notes |
|-----------|-------|-------|
| CAC (blended) | $[X] | [breakdown by channel] |
| COGS per customer | $[X] | [hosting, support, etc.] |
| Gross margin target | [X]% | [SaaS benchmark: 70-80%] |
| Monthly burn rate | $[X]K | [current] |
| Runway (months) | [X] | [cash / burn] |

---

## 3. Unit Economics

### Key Formulas

| Metric | Formula | Target | Current |
|--------|---------|--------|---------|
| **LTV** | ARPU × Gross Margin × (1 / Monthly Churn) | >$[X] | $[X] |
| **CAC** | Total S&M Spend / New Customers | <$[X] | $[X] |
| **LTV/CAC** | LTV / CAC | >3.0x | [X]x |
| **Payback** | CAC / (ARPU × Gross Margin) | <12 months | [X] months |
| **Magic Number** | Net New ARR / S&M Spend (prior Q) | >0.75 | [X] |

### Cohort Revenue Table

| Cohort | M0 | M1 | M2 | M3 | M6 | M12 | LTV |
|--------|----|----|----|----|----|----|-----|
| [Month 1] | $[X] | | | | | | |
| [Month 2] | $[X] | | | | | | |
| [Month 3] | $[X] | | | | | | |

---

## 4. Revenue Build

### Monthly Revenue Projection (12 months)

| Month | New Customers | Total Customers | MRR | Growth |
|-------|--------------|----------------|-----|--------|
| M1 | [X] | [X] | $[X] | - |
| M2 | [X] | [X] | $[X] | [X]% |
| ... | | | | |
| M12 | [X] | [X] | $[X] | [X]% |

### Revenue by Segment (if multi-product/tier)

| Segment | % of Revenue | ARPU | Growth Rate | Notes |
|---------|-------------|------|-------------|-------|
| [Tier 1] | [X]% | $[X] | [X]% | |
| [Tier 2] | [X]% | $[X] | [X]% | |
| [Enterprise] | [X]% | $[X] | [X]% | |

---

## 5. Scenario Analysis

### Variable Sensitivity

| If this changes... | Impact on LTV | Impact on Payback | Impact on ARR (M12) |
|-------------------|--------------|-------------------|---------------------|
| Churn +1% | -$[X] ([Y]%) | +[Z] months | -$[X] |
| ARPU +10% | +$[X] ([Y]%) | -[Z] months | +$[X] |
| CAC +20% | no change | +[Z] months | no change |

### Scenario Summary

| Metric | Worst | Base | Best |
|--------|-------|------|------|
| M12 ARR | $[X] | $[X] | $[X] |
| M12 Customers | [X] | [X] | [X] |
| LTV/CAC | [X]x | [X]x | [X]x |
| Runway | [X] mo | [X] mo | [X] mo |

---

## 6. Market Sizing

| Level | Size | Methodology |
|-------|------|-------------|
| **TAM** | $[X]B | [Top-down: total addressable market] |
| **SAM** | $[X]M | [Serviceable: your segment/geo] |
| **SOM** | $[X]M | [Bottom-up: realistic capture in 3 years] |

---

## 7. Benchmarks

| Metric | Your Product | Industry Median | Top Quartile |
|--------|-------------|----------------|--------------|
| Gross margin | [X]% | 70% | 80%+ |
| Net revenue retention | [X]% | 110% | 130%+ |
| LTV/CAC | [X]x | 3x | 5x+ |
| CAC payback | [X] months | 12 months | <6 months |
| Rule of 40 | [X] | 40 | 60+ |

---

## Spreadsheet Execution

For building the actual spreadsheet, use the xlsx skill:
- Color coding: Blue = inputs, Black = formulas, Green = internal links, Red = external links
- Zero formula errors tolerance
- Proper number formatting (currency, %, ratios)
- See: `../../documents/xlsx/SKILL.md`

---

## Model Checklist

- [ ] All assumptions in one tab (blue text, editable)
- [ ] No hardcoded numbers in formulas
- [ ] Scenario toggle works (best/base/worst)
- [ ] Unit economics calculated and benchmarked
- [ ] Cohort analysis included
- [ ] Charts created for key metrics
- [ ] Model reviewed by finance/advisor
