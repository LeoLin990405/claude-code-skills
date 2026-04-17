# Multi-AI Orchestration Patterns

Common patterns for coordinating multiple AI providers. Each pattern describes when to use it, the workflow steps, and practical considerations.

---

## 1. Parallel Fan-Out

Send the same task to multiple providers simultaneously, then synthesize their outputs.

### When to Use

- You want diverse perspectives on the same problem
- Redundancy matters (code review, security audit)
- You want to identify areas of agreement and disagreement

### Workflow

```
                  +--> /gask "task" --> /pend gemini ---+
                  |                                     |
User task --------+--> /cask "task" --> /pend codex ----+--> Synthesize
                  |                                     |
                  +--> /dskask "task" --> /pend deepseek+
```

### Steps

1. Send the same prompt to 2-4 providers using their `/ask` commands
2. Continue working on other tasks (async)
3. Collect results with `/pend` for each provider
4. Synthesize: identify consensus, conflicts, and unique insights

### Considerations

- Use the exact same prompt for fair comparison
- 3 providers is usually the sweet spot (diverse enough, not too noisy)
- Best for: code review, design critique, bug hunting

### Template

See [parallel-review.md](../templates/parallel-review.md) for a ready-to-use version.

---

## 2. Sequential Pipeline

Chain providers so that each one builds on the previous output. The output of Provider A becomes input for Provider B.

### When to Use

- Tasks have natural stages (draft, refine, validate)
- You want iterative improvement across different model strengths
- The task benefits from multiple passes with different perspectives

### Workflow

```
User task --> /gask "research X"
          --> /pend gemini (get research)
          --> /dskask "given this research: [gemini output], design algorithm for..."
          --> /pend deepseek (get algorithm)
          --> /cask "implement this algorithm: [deepseek output]"
          --> /pend codex (get implementation)
```

### Steps

1. Send initial task to Provider A (the one best suited for the first stage)
2. Wait for result with `/pend`
3. Extract the relevant output and include it in the prompt for Provider B
4. Repeat until pipeline is complete

### Considerations

- Each stage should add clear value; do not chain just for the sake of it
- Context window limits: summarize intermediate outputs if they are too long
- Provider ordering matters: put the broadest thinker first, the most precise last
- Best for: research-to-implementation, draft-to-review, analysis-to-recommendation

### Example Pipeline Configurations

| Pipeline | Stage 1 | Stage 2 | Stage 3 |
|----------|---------|---------|---------|
| Research-to-Code | Gemini (research) | DeepSeek (algorithm design) | Codex (implementation) |
| Draft-Review-Polish | Qwen (draft) | Gemini (review) | Codex (finalize) |
| Analyze-Decide-Plan | Gemini (analysis) | DeepSeek (decision logic) | OpenCode (execution plan) |

---

## 3. Consensus Voting

Multiple providers independently answer the same question, then you tally votes and analyze reasoning.

### When to Use

- Binary or multi-option decisions ("A vs B vs C")
- You want to reduce single-model bias
- The stakes are high enough to warrant multiple opinions

### Workflow

```
                  +--> /gask "choose A or B, explain why" ---+
                  |                                          |
Decision frame ---+--> /cask "choose A or B, explain why" ---+--> Tally votes
                  |                                          |   + analyze reasoning
                  +--> /dskask "choose A or B, explain why" -+
                  |                                          |
                  +--> /oask "choose A or B, explain why" ---+
```

### Steps

1. Frame the decision with clear options and constraints
2. Send a structured prompt (same for all) asking for: recommendation, reasons, risks, reversal conditions
3. Collect with `/pend`
4. Tally votes, synthesize strongest arguments from each side

### Considerations

- Use an odd number of providers (3 or 5) to avoid ties
- Structured prompts produce comparable responses
- Unanimous agreement is worth scrutinizing -- it can mask shared blind spots
- Best for: technology choices, architecture decisions, trade-off analysis

### Template

See [consensus-decision.md](../templates/consensus-decision.md) for a ready-to-use version.

---

## 4. Specialist Routing

Decompose a complex task into sub-tasks and route each sub-task to the provider best suited for it.

### When to Use

- The task has distinct dimensions requiring different expertise
- You want depth from specialists rather than breadth from one generalist
- Sub-tasks are independent enough to run in parallel

### Workflow

```
                         +--> /dskask "algorithm sub-task" ---+
                         |                                    |
Complex task --[decompose]+--> /gask "research sub-task" -----+--> Consolidate
                         |                                    |
                         +--> /cask "implementation sub-task"-+
```

### Steps

1. Decompose the task into independent sub-tasks
2. Match each sub-task to the best-fit provider (see Provider Specialization below)
3. Delegate in parallel
4. Collect and consolidate results

### Provider Specialization

| Strength | Best Providers |
|----------|---------------|
| Formal reasoning, math, algorithms | DeepSeek |
| Long-context, research synthesis | Gemini, Kimi |
| Code generation, refactoring | Codex, OpenCode |
| Multilingual analysis | Qwen, Kimi |
| General-purpose analysis | Gemini, Qwen |
| Mobile/platform-specific | Droid |
| Workflow automation | iFlow |

### Considerations

- Decomposition quality determines result quality; spend time on step 1
- Add intentional overlap (assign one sub-task to two providers) for critical sections
- Results may use different formats; normalize before consolidating
- Best for: research projects, system design, complex analysis

### Template

See [research-delegation.md](../templates/research-delegation.md) for a ready-to-use version.

---

## Combining Patterns

Patterns can be composed. Common combinations:

| Combination | Example |
|-------------|---------|
| Specialist Routing + Consensus | Route sub-tasks to specialists, then use consensus voting on the final recommendation |
| Sequential Pipeline + Parallel Fan-Out | Pipeline stages where one stage fans out to multiple providers |
| Fan-Out + Sequential | Fan out for initial analysis, synthesize, then pipeline the synthesis through validation |

The key principle: start with the simplest pattern that meets your needs. Add complexity only when the task genuinely requires it.
