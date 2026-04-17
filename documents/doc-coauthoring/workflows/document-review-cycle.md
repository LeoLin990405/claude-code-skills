# Workflow: Document Review Cycle

Manage the full lifecycle of a document from first draft through review, redlining, and final version.

**Skills used:** [docx](../../docx/SKILL.md) + [doc-coauthoring](../SKILL.md)

---

## Pipeline Overview

```
Request / Brief
  → Step 1: Draft Creation (docx)
  → Step 2: Self-Review Checklist
  → Step 3: Review Distribution
  → Step 4: Feedback Consolidation & Redlining (doc-coauthoring)
  → Step 5: Revision
  → Step 6: Final Approval & Publication
```

---

## Step 1: Draft Creation

**Skill:** docx

Tasks:
- Select appropriate template ([report](../templates/report-structure.md), [proposal](../templates/proposal-structure.md), or custom)
- Create initial draft with proper structure and formatting
- Apply heading styles for navigation and TOC generation
- Insert placeholder content for sections awaiting input
- Save as `[document-name]-v1-draft.docx`

Naming convention:
```
[document-name]-v[version]-[status].docx
Examples:
  q1-report-v1-draft.docx
  q1-report-v2-review.docx
  q1-report-v3-final.docx
```

---

## Step 2: Self-Review Checklist

Before sending for review, verify:

```
STRUCTURE
[ ] All required sections present
[ ] Logical flow from section to section
[ ] Executive summary written last and accurately reflects content
[ ] Table of contents matches actual headings

CONTENT
[ ] Key messages are clear and supported by evidence
[ ] Data is accurate and sourced
[ ] No placeholder text remaining
[ ] Recommendations are actionable with owners and timelines

FORMATTING
[ ] Consistent heading styles throughout
[ ] Tables properly formatted with headers
[ ] Charts labeled with titles, axes, and sources
[ ] Page numbers present
[ ] Headers/footers correct

QUALITY
[ ] Spelling and grammar checked
[ ] Jargon minimized or defined
[ ] Tone appropriate for audience
[ ] Length appropriate (not unnecessarily verbose)
```

---

## Step 3: Review Distribution

Tasks:
- Identify reviewers and their focus areas:
  - **Content reviewer**: Accuracy of information
  - **Subject matter expert**: Technical correctness
  - **Stakeholder**: Strategic alignment
  - **Editor**: Language, clarity, formatting
- Enable track changes in the document
- Send review copy with clear instructions:
  - What to review (specific sections or full document)
  - What kind of feedback you want
  - Deadline for feedback
- Save review copy as `[document-name]-v1-review.docx`

---

## Step 4: Feedback Consolidation & Redlining

**Skill:** doc-coauthoring

Tasks:
- Collect all reviewer copies
- Merge tracked changes from multiple reviewers into a single document
- For conflicting feedback:
  - Flag the conflict
  - Note both positions
  - Recommend resolution
- Create a redlined version showing all proposed changes
- Build a feedback summary:

```
REVIEWER: [Name]
SECTION: [Section name]
FEEDBACK: [Summary]
TYPE: [Content / Formatting / Factual / Structural]
ACTION: [Accept / Reject / Modify]
RATIONALE: [Why this action]
```

Output: Consolidated redlined .docx + feedback summary.

---

## Step 5: Revision

**Skill:** docx

Tasks:
- Accept/reject tracked changes based on feedback decisions
- Rewrite sections where substantive changes were requested
- Update cross-references, TOC, and page numbers
- Re-run self-review checklist (Step 2)
- If major changes: circulate for a second review (return to Step 3)
- If minor changes: proceed to final approval
- Save as `[document-name]-v2-revised.docx`

Decision guide:
```
Minor feedback only → Proceed to Step 6
Major structural changes → Return to Step 3 for re-review
New information needed → Pause, gather data, return to Step 1 for affected sections
```

---

## Step 6: Final Approval & Publication

Tasks:
- Accept all remaining tracked changes
- Remove all comments
- Final formatting pass:
  - Update TOC
  - Check page breaks
  - Verify headers/footers
  - Confirm page numbers
- Save final version as `[document-name]-v[N]-final.docx`
- Optionally convert to PDF for distribution using [pdf skill](../../pdf/SKILL.md)
- Archive all versions (draft, review, redline, final)

---

## Quick Start

```
"I have a draft report. Help me run it through a review cycle."

Claude will:
1. Review the draft against the self-review checklist
2. Identify areas that need reviewer attention
3. Help consolidate feedback once reviews come back
4. Generate a redlined version with tracked changes
5. Produce the final clean document
```

## Tips

- Never edit the original — always create a new version
- Keep a changelog noting what changed between versions
- Set clear review deadlines (reviewers expand to fill available time)
- Separate content feedback from formatting feedback
- Use comments for questions, track changes for edits
