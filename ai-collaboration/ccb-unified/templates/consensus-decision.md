# Consensus Decision Template

Get multiple AI providers to weigh in on a design or architecture decision, then tally votes and synthesize reasoning.

## When to Use

- You face a binary or multi-option technical decision (e.g., "SQL vs NoSQL", "monolith vs microservices")
- You want to reduce single-model bias on an important choice
- You need structured arguments for and against each option

## Steps

### 1. Frame the Decision

Define the decision clearly with options and constraints:

```
Decision: [clear question with 2-4 options]
Options:
  A) [option A description]
  B) [option B description]
  C) [option C description, if applicable]
Constraints: [budget, timeline, team size, tech stack, etc.]
Context: [what problem this solves, current state, relevant history]
```

### 2. Craft the Prompt

Use a structured prompt so all providers respond in a comparable format:

```
Given this decision:
[paste decision frame from step 1]

Please:
1. State your recommendation (Option A, B, or C)
2. Give your top 3 reasons for this choice
3. Identify the biggest risk of your recommended option
4. State what would change your mind (what condition would make another option better)
```

### 3. Fan Out to Providers

Send to 3-5 providers for a meaningful vote:

```bash
/gask "[structured prompt]"
/cask "[structured prompt]"
/dskask "[structured prompt]"
/oask "[structured prompt]"
/kask "[structured prompt]"
```

### 4. Collect and Tally

```bash
/pend gemini
/pend codex
/pend deepseek
/pend opencode
/pend kimi
```

### 5. Synthesize Decision

```markdown
## Consensus Decision Report

### The Question
[restate the decision]

### Vote Tally
| Provider | Recommendation | Confidence |
|----------|---------------|------------|
| Gemini   | Option A      | [high/medium/low based on strength of reasoning] |
| Codex    | Option A      | ... |
| DeepSeek | Option B      | ... |
| OpenCode | Option A      | ... |
| Kimi     | Option B      | ... |

**Result**: Option A wins 3-2

### Strongest Arguments For Winner
1. [best argument from any provider supporting Option A]
2. [second best argument]
3. [third best argument]

### Strongest Arguments Against (from dissenters)
1. [best counterargument from providers who chose differently]
2. [second counterargument]

### Key Risks Identified
- [risks mentioned by multiple providers]

### Conditions That Would Reverse the Decision
- [conditions identified by providers that would flip the answer]

### Recommendation
[Final recommendation with reasoning, incorporating insights from all providers]
```

## Tips

- **Odd number of providers**: Use 3 or 5 providers to avoid ties
- **Weighted votes**: If one provider has domain expertise (e.g., DeepSeek for algorithms), weight its vote higher
- **Unanimous agreement**: If all providers agree, pay extra attention to the risks they each identified -- unanimous agreement can mask blind spots
- **Split votes**: A close split (3-2) suggests the decision is genuinely hard. Document the dissenting arguments carefully -- they may become relevant as conditions change.
