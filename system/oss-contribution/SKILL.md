---
name: oss-contribution
description: Open source contribution etiquette — mandatory workflow for PRs to external repos
triggers:
  - fork
  - pull request
  - contribute
  - upstream
  - open source
  - PR to
  - submit PR
  - propose change
---

# Open Source Contribution Etiquette

**MANDATORY**: This skill MUST be followed whenever contributing to repositories that are NOT owned by the user. This includes forking, submitting PRs, commenting on issues, or proposing changes to any external open source project.

## Core Principles

1. **Communicate before coding** — Never submit a PR without prior discussion
2. **Respect maintainer authority** — They decide the direction, not us
3. **Keep PRs small and focused** — One PR, one purpose
4. **Use polite, positive language** — Affirm others' work before suggesting changes
5. **Language-aware communication** — Determine maintainer language before commenting (see Language Strategy below)
6. **Never modify main branch directly** — Always work on a feature/fix branch

## Mandatory Pre-PR Workflow

### Step 1: Study the Project

Before any contribution, understand:

- [ ] README and contributing guidelines (CONTRIBUTING.md)
- [ ] Code style and conventions
- [ ] Existing issues and PR discussions
- [ ] PR template (if any)
- [ ] License
- [ ] Branch structure (which branch to target: main, dev, feature branches)

### Step 2: Engage on the Issue First

**NEVER skip this step.**

If an issue already exists:
- Comment expressing interest: "I'd like to help with this"
- Propose your approach with enough detail
- Use question form: "Would this approach work?" not "I will implement this"
- Wait for maintainer confirmation before writing code

If no issue exists:
- Create one first, describing the problem/feature
- For bugs: describe the symptom, reproduction steps, and expected behavior
- For features: describe the goal, design approach, and possible implementation
- Wait for maintainer feedback on direction
- Only then offer to implement

### Step 3: Wait for Maintainer Response

- **Do NOT submit a PR before the maintainer responds**
- If no response after 1-2 weeks, a polite ping is acceptable
- If the maintainer suggests a different approach, follow their direction

### Step 4: Fork and Branch

After maintainer confirms the direction:

```bash
# 1. Fork the repo on GitHub (click Fork button, or use gh repo fork)
gh repo fork <owner>/<repo> --clone

# 2. Add upstream remote (gh repo fork does this automatically)
git remote add upstream https://github.com/<owner>/<repo>.git

# 3. Switch to the correct target branch (e.g. dev, not always main)
git checkout <target-branch>
git pull upstream <target-branch>

# 4. Create a descriptive feature branch — NEVER work on main directly
git checkout -b fix/issue-123-description
# or: feat/add-xxx, docs/update-xxx, refactor/xxx
```

**Branch naming conventions:**
| Prefix | Usage |
|--------|-------|
| `fix/` | Bug fixes |
| `feat/` | New features |
| `docs/` | Documentation changes |
| `refactor/` | Code refactoring |
| `test/` | Test additions |

### Step 5: Make Changes and Commit

- Keep changes minimal and focused (no unrelated refactoring)
- Follow the project's code style and conventions
- Write clear commit messages explaining the "why"
- Each commit should be a logical unit of change

```bash
# Stage specific files, not everything
git add <specific-files>

# Write clear commit messages
git commit -m "fix: correct filter chain in HCM when MergeGateway enabled

The Chinese specialization branch re-added clap features but the code
was not properly reverted, causing training errors in v2.3.

Closes #123"
```

### Step 6: Submit the PR

```bash
# Push to your fork
git push origin fix/issue-123-description

# Create PR targeting the correct branch (not always main!)
gh pr create --repo <owner>/<repo> \
  --base <target-branch> \
  --title "fix: correct filter chain when MergeGateway enabled" \
  --body "..."
```

**PR description MUST include:**
- [ ] Reference the issue: `Closes #xxx` or `Fixes #xxx`
- [ ] What the PR does and why
- [ ] How the bug was caused / what the feature achieves
- [ ] Summary of code changes
- [ ] Test plan or verification steps
- [ ] Credit the original issue author if applicable
- [ ] Follow the project's PR template if one exists

**PR description examples:**

Bad (too vague):
> This PR fixes a bug in the HTTP Listeners.

Good (clear cause and fix):
> This PR fixes #123 in the HTTP Listeners.
> The bug is caused by missing HTTP filters in the filter chain of the HCM
> when the MergeGateway option is enabled.
> To fix it, the missing filters have been patched to the existing HCM
> when translating ir.HTTPRoute to the xDS.

### Step 7: Respond to Review

- Thank reviewers for their time
- Address all feedback, don't ignore comments
- If you disagree, explain politely with reasoning
- Push fixes as new commits (don't force-push during review unless asked)
- After all feedback is addressed, the maintainer will merge

### Step 8: Post-Merge Cleanup

```bash
# Sync your fork after merge
git checkout main
git pull upstream main
git push origin main

# Delete the feature branch
git branch -d fix/issue-123-description
git push origin --delete fix/issue-123-description
```

## Language Guidelines

### Use Positive Framing

| Avoid | Prefer |
|-------|--------|
| "There's a bug in the current implementation" | "We could improve this by adding..." |
| "This is wrong" | "This is a good start, but we might improve it by..." |
| "I don't think this is the best way" | "This might not be the best way — what do you think?" |
| "There's a memory leaking problem" | "We can improve memory consumption by adding a cleanup function" |

### Use Modal Verbs for Uncertainty

| Avoid | Prefer |
|-------|--------|
| "We need to do X" | "Should we do X?" |
| "This should be changed to..." | "This could be changed to... what do you think?" |
| "I will implement..." | "I was thinking of going with..." |
| "We also need to expose the foo field" | "Should we expose the foo field? It's widely used in client code." |

### Affirm Before Suggesting

Always acknowledge others' work before proposing changes:

- "Great write-up — the analysis is very thorough"
- "Thanks for the detailed proposal"
- "This is a good idea, just have a few suggestions on..."
- "This is a good start, but I think we could improve it by..."

Never just say "This is wrong" — reframe as "This is a good start, but..."

### Language Strategy

**Step 1: Determine maintainer/community language**

Check these signals:
- Maintainer's GitHub profile location and bio
- README language (Chinese README = likely Chinese developer)
- Issue/PR discussion language used by maintainers
- Repo description and docs language

**Step 2: Choose format**

| Maintainer Background | Comment Format |
|----------------------|----------------|
| Chinese-speaking (confirmed) | English first, `---` separator, Chinese below |
| Non-Chinese / Unknown | English only |
| Mixed community | English only (safe default) |

**Bilingual format (Chinese maintainers only):**

```markdown
Hi @maintainer, great analysis by @author — very thorough.

I'd like to help with this. Would Approach A work?

---

你好 @maintainer，@author 的分析写得非常详尽。

我想参与实现这个功能。方案 A 可以吗？
```

**English-only format (default):**

```markdown
Hi @maintainer, great analysis by @author — very thorough.

I'd like to help with this. Would Approach A work?
```

**Tip**: If unsure about your English tone, mentally apply: "Please rewrite my sentence and make it polite." Use modal verbs (might, could, may) and question forms to soften tone.

## Anti-Patterns (NEVER do these)

- Submit a PR without any prior discussion on the issue
- Assume the maintainer agrees with a proposed approach
- Submit a "giant PR" touching many unrelated files
- Modify the main/master branch directly in your fork
- Mix unrelated changes (bug fix + refactoring + new feature) in one PR
- Use imperative/commanding tone
- Ignore the project's PR template
- Force-push without warning during review
- Close and reopen PRs repeatedly
- @mention maintainers excessively to rush review
- Submit PR to wrong branch (e.g. main when project uses dev)

## When Private Communication is Appropriate

- If a discussion needs >3 rounds of comments, move to Slack/email/Discord
- If a PR has been pending review for >2 weeks, politely ping
- After private resolution, summarize the outcome publicly on the PR/issue
- Complex issues are resolved faster in real-time chat than async PR comments

## PR Size Guidelines

| Size | Files | Recommendation |
|------|-------|----------------|
| Small | 1-5 | Ideal, submit as-is |
| Medium | 5-15 | Acceptable if focused |
| Large | 15-30 | Consider splitting |
| Giant | 30+ | Must split into multiple PRs |

Split strategies:
- **By function**: One feature per PR, separate refactoring into its own PR. Don't "fix a typo while you're at it" in a feature PR.
- **By module**: API changes first (get consensus), then implementation, then tests/docs. API PR should always be separate — implementing before API consensus risks wasted work.

## Branch Protection Awareness

Many projects use branch protection rules:
- PRs must pass CI checks before merge
- PRs may require reviewer approval
- Force-push to protected branches is blocked
- Linear commit history may be required

Always check if the project has these rules and comply with them.

## Reference

Based on:
- Zhao Huabing's open source PR best practices (Envoy Gateway maintainer)
- 刘悦's GitHub PR contribution guide (Bert-vits2 example)

Key takeaways:
- Communicate before coding
- Clear PR descriptions with cause and fix
- Avoid giant PRs
- Community etiquette in language
- Know when to communicate privately
- Always work on feature branches, never main
- Target the correct branch (dev vs main)
- Post-merge: sync fork and clean up branches
