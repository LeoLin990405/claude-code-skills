# Business Report Template

A structured template for creating professional business reports. Use with the [docx skill](../../docx/SKILL.md) to generate formatted Word documents.

---

## Report Structure

### 1. Title Page

```
[Company Name / Logo]
[Report Title]
[Subtitle / Project Name]

Prepared by: [Author Name]
Date: [Date]
Version: [X.X]
Classification: [Confidential / Internal / Public]
```

### 2. Executive Summary

Write this section LAST, after all other sections are complete. Keep to 1 page maximum.

```
PURPOSE
- What this report covers and why it was created
- Key question or problem being addressed

KEY FINDINGS
- Finding 1: [One-sentence summary with key metric]
- Finding 2: [One-sentence summary with key metric]
- Finding 3: [One-sentence summary with key metric]

RECOMMENDATIONS
- Recommendation 1: [Action + expected impact]
- Recommendation 2: [Action + expected impact]

NEXT STEPS
- [Immediate action with owner and deadline]
```

### 3. Table of Contents

Auto-generated from heading styles. Include page numbers.

### 4. Introduction / Background

```
CONTEXT
- Business context and background
- Why this report was commissioned
- Scope and boundaries

METHODOLOGY
- Data sources used
- Analysis approach
- Time period covered
- Any limitations or caveats
```

### 5. Analysis

Structure depends on report type. Choose one:

**Option A: Thematic Analysis**
```
THEME 1: [Topic]
- Data / evidence
- Interpretation
- Implications

THEME 2: [Topic]
- Data / evidence
- Interpretation
- Implications
```

**Option B: Comparative Analysis**
```
CURRENT STATE
- Metrics and performance data
- Process description

GAP ANALYSIS
- Where we are vs. where we need to be
- Root causes

FUTURE STATE
- Target metrics
- Required changes
```

**Option C: Financial Analysis**
```
REVENUE ANALYSIS
- Trends, breakdown by segment
- Year-over-year comparison

COST ANALYSIS
- Fixed vs. variable
- Cost drivers

PROFITABILITY
- Margins by product/segment
- Sensitivity analysis
```

### 6. Findings

```
FINDING 1: [Clear statement]
- Supporting data / evidence
- Impact assessment (quantified where possible)
- Confidence level: [High / Medium / Low]

FINDING 2: [Clear statement]
- Supporting data / evidence
- Impact assessment
- Confidence level: [High / Medium / Low]
```

### 7. Recommendations

```
RECOMMENDATION 1: [Action statement]
- Rationale: Why this action
- Expected impact: [Quantified benefit]
- Cost / effort: [Estimated resources]
- Timeline: [Implementation timeframe]
- Risk: [Key risk and mitigation]
- Priority: [Critical / High / Medium / Low]
- Owner: [Responsible person/team]

RECOMMENDATION 2: [Action statement]
- [Same structure]
```

### 8. Implementation Plan

```
PHASE 1: [Name] — [Timeframe]
- Action items with owners
- Key milestones
- Dependencies

PHASE 2: [Name] — [Timeframe]
- Action items with owners
- Key milestones
- Dependencies

SUCCESS METRICS
- KPI 1: [Metric] — Target: [Value] — Measured: [Frequency]
- KPI 2: [Metric] — Target: [Value] — Measured: [Frequency]
```

### 9. Appendix

```
APPENDIX A: [Detailed Data Tables]
APPENDIX B: [Methodology Details]
APPENDIX C: [Glossary of Terms]
APPENDIX D: [References and Sources]
```

---

## Formatting Guidelines

| Element | Style |
|---------|-------|
| Title | Heading 1, bold, 18pt |
| Section headers | Heading 2, bold, 14pt |
| Subsection headers | Heading 3, bold, 12pt |
| Body text | Normal, 11pt, 1.15 line spacing |
| Tables | Bordered, header row shaded |
| Charts | Titled, labeled axes, source noted |
| Page numbers | Bottom center or bottom right |

## Usage

```
"Create a business report about Q1 sales performance using the report template"
→ Claude loads docx skill + this template, generates structured .docx file
```
