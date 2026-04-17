# Workflow: PDF Form Processing

Extract data from PDF forms, process it, and produce structured output.

**Skills used:** [pdf](../../pdf/SKILL.md) → [xlsx](../../xlsx/SKILL.md) (optional) → [docx](../../docx/SKILL.md) (optional)

---

## Pipeline Overview

```
PDF Form(s)
  → Step 1: Form Field Discovery (pdf)
  → Step 2: Data Extraction (pdf)
  → Step 3: Data Validation & Cleaning
  → Step 4: Data Processing & Analysis (xlsx)
  → Step 5: Output Generation (xlsx / docx / pdf)
```

---

## Step 1: Form Field Discovery

**Skill:** pdf

Tasks:
- Open the PDF and enumerate all form fields
- Catalog each field:
  - Field name / ID
  - Field type (text, checkbox, radio, dropdown, signature, date)
  - Required vs. optional
  - Validation rules (if embedded)
- Map the form layout to understand logical groupings
- Handle both AcroForm (traditional) and XFA (XML-based) forms

Output: Field inventory listing all extractable fields.

```
FORM: [filename.pdf]
TOTAL FIELDS: [count]

FIELD INVENTORY:
| # | Field Name | Type | Required | Section |
|---|------------|------|----------|---------|
| 1 | first_name | text | Yes | Personal Info |
| 2 | last_name | text | Yes | Personal Info |
| 3 | agree_terms | checkbox | Yes | Legal |
```

---

## Step 2: Data Extraction

**Skill:** pdf

Tasks:
- Extract field values from each PDF form
- For batch processing (multiple forms):
  - Process each form sequentially
  - Compile results into a single dataset
- Handle edge cases:
  - Empty/unfilled fields → mark as null
  - Handwritten text (if OCR available) → flag confidence level
  - Scanned forms without form fields → use text extraction with position mapping
  - Multi-page forms → track page numbers

Output: Structured data (JSON or tabular format) with all extracted values.

```json
{
  "source": "application-001.pdf",
  "extracted_at": "2026-03-10",
  "fields": {
    "first_name": "John",
    "last_name": "Smith",
    "agree_terms": true
  },
  "warnings": []
}
```

---

## Step 3: Data Validation & Cleaning

Tasks:
- Validate extracted data against expected formats:
  - Dates in correct format
  - Numeric fields contain numbers
  - Required fields are populated
  - Email/phone match expected patterns
- Flag issues:

```
VALIDATION REPORT:
| Form | Field | Issue | Severity |
|------|-------|-------|----------|
| app-003.pdf | email | Invalid format | Error |
| app-007.pdf | phone | Missing value (required) | Error |
| app-012.pdf | date | Ambiguous format (01/02/03) | Warning |
```

- Clean data:
  - Standardize date formats
  - Trim whitespace
  - Normalize capitalization
  - Deduplicate entries if applicable

Output: Validated, cleaned dataset + validation report.

---

## Step 4: Data Processing & Analysis

**Skill:** xlsx (optional — skip if output is simple)

Tasks:
- Import cleaned data into Excel workbook
- Create summary statistics:
  - Total forms processed
  - Completion rate by field
  - Common values / distributions
- Build pivot tables for categorical data
- Generate charts for reporting
- Apply conditional formatting to highlight anomalies

Output: Analysis .xlsx workbook.

---

## Step 5: Output Generation

Choose one or more output formats based on the use case:

### Option A: Spreadsheet Output (xlsx)
**Skill:** xlsx

- One row per form, one column per field
- Summary sheet with statistics
- Best for: Data analysis, record-keeping, further processing

### Option B: Report Output (docx)
**Skill:** docx

- Summary report of all forms processed
- Aggregated findings and statistics
- Individual form details in appendix
- Best for: Management reporting, audit documentation

### Option C: Filled PDF Output (pdf)
**Skill:** pdf

- Pre-fill blank forms with data from another source
- Batch-fill multiple forms from a spreadsheet
- Best for: Form generation, auto-population from database

### Option D: Merged PDF Output (pdf)
**Skill:** pdf

- Merge processed forms into a single PDF
- Add cover page with summary
- Best for: Archiving, submission packages

---

## Quick Start

```
"Extract data from these 20 application forms and create a summary spreadsheet."

Claude will:
1. Discover form fields in the first PDF
2. Batch-extract data from all 20 forms
3. Validate and clean the extracted data
4. Create an xlsx with all data + summary statistics
5. Flag any forms with missing or invalid data
```

## Common Use Cases

| Use Case | Pipeline |
|----------|----------|
| Application processing | PDF extract → validate → xlsx summary |
| Survey aggregation | PDF extract → xlsx analysis → pptx report |
| Compliance audit | PDF extract → validate → docx audit report |
| Form pre-filling | xlsx source data → PDF fill → batch output |
| Archive creation | Multiple PDFs → merge → single indexed PDF |

## Tips

- Always discover fields first — form structures vary between versions
- Process a single form before batching to verify extraction accuracy
- Keep the validation report — it documents data quality
- For scanned (non-fillable) PDFs, extraction relies on OCR and is less reliable
- Back up original PDFs before any processing
