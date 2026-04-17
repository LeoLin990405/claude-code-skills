# Meeting Notes Template

A structured template for capturing meeting notes. Use with the [docx skill](../../docx/SKILL.md) to generate formatted Word documents.

---

## Meeting Notes Structure

### Header

```
MEETING TITLE: [Descriptive title]
DATE: [YYYY-MM-DD]
TIME: [Start time] - [End time] ([Duration])
LOCATION: [Room / Video link]
TYPE: [Status update / Decision / Brainstorm / Planning / Review / 1:1]
```

### Attendees

```
PRESENT
- [Name] — [Role/Title] — [Owner / Participant / Observer]
- [Name] — [Role/Title] — [Owner / Participant / Observer]

ABSENT
- [Name] — [Role/Title]

NOTES TAKEN BY: [Name]
```

### Agenda

Number items with time allocations. Mark the owner of each item.

```
1. [Topic] — [Time allocation] — [Owner]
2. [Topic] — [Time allocation] — [Owner]
3. [Topic] — [Time allocation] — [Owner]
4. Open discussion — [Remaining time]
```

### Discussion Notes

One section per agenda item. Capture key points, not transcripts.

```
ITEM 1: [Topic]
- [Key point discussed]
- [Key point discussed]
- [Data or fact referenced]
- Open question: [Unresolved question]

ITEM 2: [Topic]
- [Key point discussed]
- [Key point discussed]
- Concern raised: [Who raised it + summary]
```

### Decisions Made

Every decision needs: what was decided, who approved it, and any conditions.

```
DECISION 1: [Clear statement of what was decided]
- Decided by: [Who]
- Rationale: [Brief reason]
- Conditions: [If any]

DECISION 2: [Clear statement of what was decided]
- Decided by: [Who]
- Rationale: [Brief reason]
```

### Action Items

Every action needs: what, who, and when. This is the most important section.

```
| # | Action | Owner | Due Date | Status |
|---|--------|-------|----------|--------|
| 1 | [Specific action] | [Name] | [Date] | Pending |
| 2 | [Specific action] | [Name] | [Date] | Pending |
| 3 | [Specific action] | [Name] | [Date] | Pending |
```

### Parking Lot

Items raised but deferred to a future meeting.

```
- [Topic] — To be discussed: [When / which meeting]
- [Topic] — Needs: [What's needed before discussing]
```

### Next Meeting

```
DATE: [Next meeting date]
TIME: [Time]
PRELIMINARY AGENDA:
1. Review action items from this meeting
2. [Carried-over topic]
3. [New topic]
```

---

## Meeting Type Variants

### Status Update Meeting
Focus on: progress against milestones, blockers, timeline changes.
Key sections: Discussion (by workstream), Action Items.

### Decision Meeting
Focus on: options presented, criteria used, decision reached.
Key sections: Discussion (options + pros/cons), Decisions Made.

### Brainstorm / Workshop
Focus on: ideas generated, themes identified, next steps.
Key sections: Discussion (ideas grouped by theme), Action Items.

### Project Kickoff
Focus on: objectives, roles, timeline, communication plan.
Key sections: All sections, emphasize Attendees and Action Items.

### 1:1 Meeting
Focus on: priorities, blockers, feedback, development.
Key sections: Discussion, Action Items. Keep informal.

---

## Formatting Guidelines

| Element | Style |
|---------|-------|
| Title | Heading 1, bold |
| Section headers | Heading 2, bold |
| Body text | Normal, 11pt |
| Action items table | Bordered, header shaded |
| Decisions | Bold decision statement, normal rationale |

## Usage

```
"Create meeting notes for today's project review using the meeting notes template"
→ Claude loads docx skill + this template, generates structured .docx file
```
