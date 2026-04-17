# Research Delegation Template

Delegate research tasks to specialized AI providers based on their strengths, then consolidate findings.

## When to Use

- You need to research a broad topic with multiple dimensions
- Different aspects of the research map to different provider strengths
- You want depth from specialists rather than breadth from one generalist

## Provider Specialization Guide

| Research Type | Best Provider | Why |
|---------------|---------------|-----|
| Algorithm analysis, math proofs, formal reasoning | DeepSeek (`/dskask`) | Strong at step-by-step reasoning |
| Long document analysis, literature review | Gemini (`/gask`) or Kimi (`/kask`) | Large context windows |
| Code-related research (libraries, APIs, patterns) | Codex (`/cask`) or OpenCode (`/oask`) | Code-native models |
| Multilingual sources, cross-language research | Qwen (`/qask`) or Kimi (`/kask`) | Strong multilingual capabilities |
| General technology survey, trend analysis | Gemini (`/gask`) | Broad training data |
| Mobile/platform-specific research | Droid (`/dask`) | Platform specialization |

## Steps

### 1. Decompose the Research Question

Break the research topic into sub-questions that can be independently investigated:

```
Main question: [your research topic]

Sub-questions:
  1. [sub-question suited for Provider X]
  2. [sub-question suited for Provider Y]
  3. [sub-question suited for Provider Z]
```

### 2. Assign and Delegate

Route each sub-question to the best-fit provider:

```bash
# Example: Researching "best database for real-time analytics"
/dskask "Compare the theoretical performance characteristics of ClickHouse vs TimescaleDB vs Apache Druid for real-time OLAP queries. Focus on query complexity, ingestion rates, and storage efficiency."
/gask "Survey recent (2024-2025) production case studies of companies using ClickHouse, TimescaleDB, or Apache Druid for real-time analytics. What scale did they operate at and what problems did they encounter?"
/cask "Compare the developer experience of ClickHouse, TimescaleDB, and Apache Druid: client libraries, ORM support, migration tooling, and integration with common frameworks (Python, Node.js, Go)."
```

### 3. Collect Results

```bash
/pend deepseek
/pend gemini
/pend codex
```

### 4. Consolidate Research

```markdown
## Research Report: [Topic]

### Executive Summary
[2-3 sentences synthesizing the key finding across all sub-questions]

### Findings by Dimension

#### [Dimension 1: e.g., Performance Characteristics]
Source: [Provider]
- [key findings]

#### [Dimension 2: e.g., Production Experience]
Source: [Provider]
- [key findings]

#### [Dimension 3: e.g., Developer Experience]
Source: [Provider]
- [key findings]

### Cross-Cutting Themes
- [patterns that appeared across multiple providers' research]

### Gaps and Follow-Up Questions
- [areas where research was insufficient or contradictory]
- [questions that emerged from the initial findings]

### Recommendation
[synthesized recommendation based on all dimensions]
```

## Tips

- **Prompt specificity**: Give each provider a narrow, well-defined sub-question. Broad prompts produce shallow results.
- **Overlap intentionally**: Assign one sub-question to two providers for cross-validation on critical topics.
- **Iterative deepening**: After the first round, use findings to formulate follow-up questions and delegate again.
- **Source skepticism**: AI providers may generate plausible-sounding but incorrect details. Cross-reference critical claims across providers.
