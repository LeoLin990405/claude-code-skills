---
name: agent-teams
description: Orchestrate teams of Claude Code sessions with shared tasks, inter-agent messaging, and centralized management
version: 1.0.0
triggers:
  - agent team
  - agent teams
  - spawn team
  - create team
  - teammates
  - team lead
  - parallel agents
  - coordinate agents
  - multi-agent
---

# Agent Teams Skill

Coordinate multiple Claude Code instances working together as a team, with shared tasks, inter-agent messaging, and centralized management.

## Prerequisites

Agent teams are **experimental and disabled by default**. Enable them first:

```json
// In settings.json
{
  "env": {
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
  }
}
```

Or set environment variable: `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`

## When to Use Agent Teams

### Best Use Cases
- **Research and review**: Multiple teammates investigate different aspects simultaneously
- **New modules or features**: Teammates each own a separate piece without conflicts
- **Debugging with competing hypotheses**: Test different theories in parallel
- **Cross-layer coordination**: Changes spanning frontend, backend, and tests

### When NOT to Use
- Sequential tasks with dependencies
- Same-file edits (causes conflicts)
- Simple tasks (coordination overhead exceeds benefit)
- Routine work (single session is more cost-effective)

## Agent Teams vs Subagents

| Aspect | Subagents | Agent Teams |
|--------|-----------|-------------|
| **Context** | Own context; results return to caller | Own context; fully independent |
| **Communication** | Report back to main agent only | Teammates message each other directly |
| **Coordination** | Main agent manages all work | Shared task list with self-coordination |
| **Best for** | Focused tasks where only result matters | Complex work requiring discussion |
| **Token cost** | Lower | Higher (each teammate = separate instance) |

**Rule of thumb**: Use subagents for quick focused workers. Use agent teams when teammates need to share findings and coordinate.

## Quick Start

Tell Claude to create a team in natural language:

```
Create an agent team to explore this CLI tool design from different angles:
one teammate on UX, one on technical architecture, one playing devil's advocate.
```

Claude will:
1. Create a team with shared task list
2. Spawn teammates for each role
3. Have them explore the problem
4. Synthesize findings
5. Clean up when finished

## Display Modes

### In-Process Mode (Default)
All teammates run inside your main terminal.
- **Shift+Up/Down**: Select a teammate
- **Type**: Send message to selected teammate
- **Enter**: View teammate's session
- **Escape**: Interrupt teammate's current turn
- **Ctrl+T**: Toggle task list

### Split-Pane Mode
Each teammate gets its own pane (requires tmux or iTerm2).

```json
// settings.json
{
  "teammateMode": "tmux"  // or "in-process" or "auto"
}
```

Or per-session: `claude --teammate-mode in-process`

## Team Control Commands

### Spawn Teammates with Specific Models
```
Create a team with 4 teammates to refactor these modules in parallel.
Use Sonnet for each teammate.
```

### Require Plan Approval
```
Spawn an architect teammate to refactor the authentication module.
Require plan approval before they make any changes.
```

### Enable Delegate Mode
Press **Shift+Tab** to cycle into delegate mode. The lead focuses only on coordination (spawning, messaging, task management) without implementing tasks itself.

### Assign Tasks
```
Assign the security review task to the researcher teammate
```

### Shut Down Teammates
```
Ask the researcher teammate to shut down
```

### Clean Up Team
```
Clean up the team
```

**Important**: Always use the lead to clean up. Shut down all teammates first.

## Architecture

| Component | Role |
|-----------|------|
| **Team lead** | Main session that creates team, spawns teammates, coordinates |
| **Teammates** | Separate Claude instances working on assigned tasks |
| **Task list** | Shared work items that teammates claim and complete |
| **Mailbox** | Messaging system for inter-agent communication |

### Storage Locations
- Team config: `~/.claude/teams/{team-name}/config.json`
- Task list: `~/.claude/tasks/{team-name}/`

### Task States
- **Pending**: Not started
- **In Progress**: Being worked on
- **Completed**: Done

Tasks can have dependencies - blocked tasks auto-unblock when dependencies complete.

## Best Practices

### 1. Give Teammates Enough Context
Teammates don't inherit lead's conversation history. Include details in spawn prompt:

```
Spawn a security reviewer teammate with the prompt: "Review the authentication
module at src/auth/ for security vulnerabilities. Focus on token handling,
session management, and input validation. The app uses JWT tokens stored in
httpOnly cookies. Report any issues with severity ratings."
```

### 2. Size Tasks Appropriately
- **Too small**: Coordination overhead exceeds benefit
- **Too large**: Risk of wasted effort
- **Just right**: Self-contained units with clear deliverables

Aim for 5-6 tasks per teammate.

### 3. Avoid File Conflicts
Break work so each teammate owns different files. Two teammates editing the same file leads to overwrites.

### 4. Monitor and Steer
Check in on progress, redirect approaches that aren't working, synthesize findings as they come in.

### 5. Wait for Teammates
If lead starts implementing instead of waiting:
```
Wait for your teammates to complete their tasks before proceeding
```

## Example Prompts

### Parallel Code Review
```
Create an agent team to review PR #142. Spawn three reviewers:
- One focused on security implications
- One checking performance impact
- One validating test coverage
Have them each review and report findings.
```

### Competing Hypotheses Investigation
```
Users report the app exits after one message instead of staying connected.
Spawn 5 agent teammates to investigate different hypotheses. Have them talk to
each other to try to disprove each other's theories, like a scientific
debate. Update the findings doc with whatever consensus emerges.
```

### Feature Development
```
Create an agent team to implement the new notification system:
- One teammate for the backend API
- One for the frontend components
- One for writing tests
Each should own their own files to avoid conflicts.
```

## Troubleshooting

### Teammates Not Appearing
- In-process mode: Press Shift+Down to cycle through active teammates
- Check if task warrants a team (Claude decides based on complexity)
- For split panes: Verify `which tmux` returns a path

### Too Many Permission Prompts
Pre-approve common operations in permission settings before spawning teammates.

### Teammates Stopping on Errors
Check output with Shift+Up/Down, then:
- Give additional instructions directly
- Spawn a replacement teammate

### Lead Shuts Down Early
Tell it to keep going or wait for teammates to finish.

### Orphaned tmux Sessions
```bash
tmux ls
tmux kill-session -t <session-name>
```

## Limitations

- **No session resumption**: `/resume` and `/rewind` don't restore in-process teammates
- **Task status can lag**: Manually update if tasks appear stuck
- **Shutdown can be slow**: Teammates finish current work first
- **One team per session**: Clean up before starting new team
- **No nested teams**: Only lead can manage the team
- **Lead is fixed**: Can't transfer leadership
- **Permissions set at spawn**: All teammates start with lead's permissions
- **Split panes require tmux/iTerm2**: Not supported in VS Code terminal, Windows Terminal, or Ghostty

## Token Usage Warning

Agent teams use **significantly more tokens** than single sessions. Each teammate has its own context window. Use for:
- Research and review tasks
- New feature development
- Complex debugging

Avoid for routine tasks where single session suffices.
