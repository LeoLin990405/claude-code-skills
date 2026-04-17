# Parallel Code Review Template

Delegate code review to multiple AI providers in parallel, then synthesize their findings into a unified review.

## When to Use

- You want diverse perspectives on code quality, bugs, or architecture
- A critical PR needs thorough review before merging
- You want to compare how different AI models evaluate the same code

## Steps

### 1. Define the Review Scope

Identify what to review and what reviewers should focus on:

```
Review target: [file path, PR number, or code block]
Focus areas: [security, performance, readability, architecture, correctness]
Context: [brief description of what this code does and why]
```

### 2. Fan Out to Providers

Send the review task to multiple providers in parallel. Choose 2-4 providers for best results.

```bash
# Option A: Broad review (same prompt to all)
/gask "Review this code for bugs, security issues, and design problems: [paste code or file path]"
/cask "Review this code for bugs, security issues, and design problems: [paste code or file path]"
/dskask "Review this code for bugs, security issues, and design problems: [paste code or file path]"

# Option B: Specialist review (different focus per provider)
/dskask "Analyze this algorithm for correctness and edge cases: [code]"
/gask "Review this code for security vulnerabilities and injection risks: [code]"
/cask "Review this code for readability, naming, and idiomatic patterns: [code]"
```

### 3. Collect Results

Wait for all providers, then collect:

```bash
/pend gemini
/pend codex
/pend deepseek
```

### 4. Synthesize

After collecting all reviews, synthesize using this structure:

```markdown
## Parallel Review Summary

### Issues Found by Multiple Reviewers (High Confidence)
- [Issues flagged by 2+ providers — these are almost certainly real]

### Issues Found by One Reviewer (Medium Confidence)
- [Unique findings from individual providers — worth investigating]

### Conflicting Opinions
- [Areas where providers disagree — requires human judgment]

### Consensus Recommendations
- [Changes all or most reviewers agree on]

### Provider-Specific Insights
- **Gemini**: [unique perspective or finding]
- **Codex**: [unique perspective or finding]
- **DeepSeek**: [unique perspective or finding]
```

## Tips

- **Provider selection**: Use DeepSeek for algorithm/logic-heavy code, Gemini for broad architectural review, Codex for idiomatic code style
- **Prompt consistency**: When doing broad review, use the exact same prompt for all providers so results are comparable
- **Conflict resolution**: When providers disagree, the issue that is flagged by the most providers is usually correct. For genuine ties, escalate to human judgment.
- **Cost control**: 2-3 providers usually suffice. Using all 9 is rarely necessary.
