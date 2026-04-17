# Workflow: Data to Presentation

Transform raw data in Excel into a polished PowerPoint presentation.

**Skills used:** [xlsx](../../xlsx/SKILL.md) → [pptx](../../pptx/SKILL.md)

---

## Pipeline Overview

```
Raw Data (CSV/XLSX)
  → Step 1: Data Cleanup & Structuring (xlsx)
  → Step 2: Analysis & Chart Generation (xlsx)
  → Step 3: Insight Extraction
  → Step 4: Slide Deck Creation (pptx)
  → Step 5: Review & Polish
```

---

## Step 1: Data Cleanup & Structuring

**Skill:** xlsx

Tasks:
- Import raw data into a clean worksheet
- Remove duplicates, fix formatting inconsistencies
- Standardize column headers and data types
- Handle missing values (fill, interpolate, or flag)
- Create a "Clean Data" sheet separate from raw data

Output: Clean, structured .xlsx file with raw and clean sheets.

---

## Step 2: Analysis & Chart Generation

**Skill:** xlsx

Tasks:
- Create summary tables (totals, averages, counts by category)
- Build pivot tables for multi-dimensional analysis
- Generate charts appropriate to the data:
  - **Trends over time** → Line chart
  - **Comparisons** → Bar/column chart
  - **Composition** → Pie/stacked bar chart
  - **Distribution** → Histogram/box plot
  - **Correlation** → Scatter plot
- Apply conditional formatting to highlight key values
- Create a "Dashboard" sheet with key metrics

Output: Analysis .xlsx with summary tables, pivot tables, and charts.

---

## Step 3: Insight Extraction

Tasks:
- Identify the 3-5 key findings from the analysis
- For each finding, note:
  - The data point or trend
  - Why it matters (business impact)
  - Recommended action
- Determine the narrative arc: What story does the data tell?
- Draft headline for each slide

Output: Outline of key insights with supporting data points.

---

## Step 4: Slide Deck Creation

**Skill:** pptx

Recommended slide structure:

```
Slide 1: Title Slide
  - Presentation title, date, author

Slide 2: Executive Summary
  - 3-5 bullet points of key findings
  - One headline metric

Slide 3: Methodology / Data Source
  - Where the data came from
  - Time period, sample size
  - Any caveats

Slides 4-8: Key Findings (one per slide)
  - Headline: Insight statement (not "Sales Data")
  - Chart or visual from Step 2
  - 2-3 supporting bullet points
  - Source note at bottom

Slide 9: Summary & Recommendations
  - Recap of findings
  - Recommended actions
  - Next steps

Slide 10: Appendix (optional)
  - Detailed data tables
  - Additional charts
```

Tasks:
- Export charts from xlsx as images or recreate in pptx
- Use consistent slide layout and color scheme
- Write insight-driven headlines (e.g., "Revenue grew 23% YoY" not "Revenue Chart")
- Add speaker notes for each slide
- Include source citations on data slides

Output: Polished .pptx presentation.

---

## Step 5: Review & Polish

Tasks:
- Check all charts are readable and properly labeled
- Verify data consistency between xlsx and pptx
- Ensure slide-to-slide flow tells a coherent story
- Check formatting: fonts, alignment, spacing
- Add slide numbers and footer

---

## Quick Start

```
"I have sales data in sales-q1.xlsx. Create a presentation with key insights."

Claude will:
1. Read and clean the data using xlsx skill
2. Generate analysis and charts
3. Extract key insights
4. Build a presentation using pptx skill
5. Deliver both the analysis .xlsx and presentation .pptx
```

## Tips

- Keep one key message per slide
- Use the chart type that best matches your data relationship
- Headlines should state the insight, not describe the chart
- Limit text on slides — details go in speaker notes
- Include an appendix for stakeholders who want raw data
