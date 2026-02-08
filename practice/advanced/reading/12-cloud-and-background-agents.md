# Cloud and Background Agents

## Overview

GitHub Copilot's agent capabilities now extend far beyond the editor. Agents can
run locally in VS Code, silently in the background via CLI, remotely in GitHub's
cloud infrastructure, or through partner platforms like Anthropic's Claude Agent
and OpenAI's Codex. This guide explores the full execution spectrum, comparing
capabilities, trust models, and integration patterns across every environment.

---

## 1. The Agent Execution Spectrum

Modern AI coding agents operate across a continuum of execution environments,
each with distinct trade-offs:

```
┌─────────────────────────────────────────────────────────────────────┐
│                    Agent Execution Spectrum                         │
│                                                                     │
│  Local          Background        Cloud            Partner          │
│  ──────         ──────────        ─────            ───────          │
│  VS Code        Copilot CLI       GitHub           Claude Agent     │
│  Interactive    Non-interactive   Remote infra     Anthropic        │
│  Full tools     Limited tools     Sandboxed        OpenAI Codex     │
│  Single session Parallel sessions Auto-PR          Slash commands   │
│                                                                     │
│  ◄── More control                      More autonomy ──►           │
│  ◄── More tool access                  More isolation ──►          │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2. Local Agents

### What They Are

Local agents run inside your editor (VS Code, JetBrains, etc.) with full access
to your development environment. This is the traditional Copilot Agent Mode
experience.

### Characteristics

- **Interactive.** The agent can ask clarifying questions, request confirmations,
  and present options for your review.
- **Full tool access.** Terminal commands, file system operations, browser preview,
  debugging, MCP servers -- everything available in your local environment.
- **Single session.** One agent session runs at a time within the editor.
- **Immediate feedback.** You see file edits, terminal output, and tool invocations
  in real time.

### Best Use Cases

| Use Case | Why Local Is Best |
|----------|-------------------|
| Exploratory coding | Interactive Q&A helps refine direction |
| Complex debugging | Full debugger and terminal access |
| Learning a new codebase | Real-time dialog about architecture |
| Prototyping | Rapid iteration with immediate feedback |
| Tasks requiring MCP tools | Full access to configured MCP servers |

### Limitations

- Blocks your editor while running.
- Context window limited to a single session's history.
- Cannot run multiple tasks in parallel.
- Requires your machine to remain on and connected.

---

## 3. Background Agents

### What They Are

Background agents run via the **Copilot CLI** (`gh copilot`) or through VS Code's
background task system. They operate non-interactively, executing tasks without
requiring continuous attention.

### Invocation via Copilot CLI

```bash
# Start a background coding session
gh copilot agent --task "Refactor the authentication module to use JWT tokens"

# Start with a specific branch
gh copilot agent --task "Add input validation to all API endpoints" --branch feature/validation

# Run in a git worktree for isolation
gh copilot agent --task "Migrate database schema" --worktree
```

### Git Worktrees for Isolation

Background agents can use **git worktrees** to operate on an isolated copy of
your repository, preventing interference with your active working directory:

```bash
# The agent creates a worktree automatically
gh copilot agent --task "Update all dependencies" --worktree

# Your main working directory remains untouched
# The agent works in .git/worktrees/copilot-agent-<id>/
```

Benefits of worktree isolation:
- No conflict with your current uncommitted changes.
- Multiple background agents can work on different worktrees simultaneously.
- Easy cleanup -- delete the worktree when done.

### Parallel Sessions

Unlike local agents, you can run **multiple background sessions concurrently**:

```bash
# Terminal 1
gh copilot agent --task "Add unit tests for user service" --worktree

# Terminal 2
gh copilot agent --task "Add unit tests for product service" --worktree

# Terminal 3
gh copilot agent --task "Update API documentation" --worktree
```

Each session operates independently with its own context window and worktree.

### Limited Tool Access

Background agents have a **restricted tool set** compared to local agents:

| Tool | Local Agent | Background Agent |
|------|-------------|------------------|
| File read/write | Yes | Yes |
| Terminal commands | Yes | Yes (sandboxed) |
| Browser preview | Yes | No |
| GUI interactions | Yes | No |
| MCP servers | Yes | Limited |
| User confirmation prompts | Yes | No (auto-proceeds) |
| Debugger | Yes | No |

### Best Use Cases

- Batch refactoring across many files.
- Running test suites and fixing failures iteratively.
- Dependency updates and migration scripts.
- Code generation from specifications.
- Tasks that take a long time and do not require interaction.

---

## 4. Cloud Coding Agents

### What They Are

Cloud coding agents run on **GitHub's remote infrastructure**. They are triggered
directly from GitHub.com -- on issues, pull requests, or via the `@copilot`
mention -- and execute in a sandboxed cloud environment.

### Invocation Methods

**From Issues:**
```
@copilot implement the feature described in this issue
```

**From Pull Requests:**
```
@copilot review this PR and suggest improvements
```

**From the GitHub UI:**
Navigate to an issue and select "Code with Copilot" to assign the task to the
cloud coding agent.

### Auto PR Creation

One of the most distinctive features of cloud coding agents is **automatic pull
request creation**. The agent:

1. Reads the issue or task description.
2. Clones the repository in a secure cloud environment.
3. Creates a new branch.
4. Implements the changes.
5. Runs available CI checks.
6. Opens a pull request with a detailed description.
7. Responds to review comments and iterates.

### Cloud Environment Specifications

| Property | Detail |
|----------|--------|
| Runtime | Secure container on GitHub infrastructure |
| Repository access | Full clone of the repository |
| Network access | Restricted (no arbitrary internet access) |
| Tool access | File operations, terminal (sandboxed), git |
| Duration limit | Configurable timeout (typically 30-60 minutes) |
| Secrets access | Repository secrets available via Actions |
| CI integration | Can trigger and monitor GitHub Actions |

### Best Use Cases

| Use Case | Why Cloud Is Best |
|----------|-------------------|
| Issue-driven development | Direct integration with GitHub Issues |
| Simple feature implementation | Self-contained tasks with clear specs |
| Bug fixes with reproduction steps | Agent can run tests autonomously |
| Documentation updates | Low-risk, high-volume changes |
| Dependency bumps | Automated with CI validation |

### Limitations

- No interactive dialog -- the agent works from the issue/PR description alone.
- Limited to tools available in the cloud sandbox.
- Cannot access local MCP servers or custom tool configurations.
- Network restrictions prevent accessing private APIs or services.
- Iteration happens through PR review comments, which is slower than local
  interaction.

---

## 5. Partner Agents

### Claude Agent (Anthropic)

Claude Agent integrates with VS Code as a partner agent, offering Anthropic's
Claude model with specialized slash commands:

```
/claude review this file for potential memory leaks
/claude refactor this function to use async/await
/claude explain the architecture of this module
```

**Key Features:**
- Direct access to Claude's extended context window (up to 200K tokens).
- Slash command interface for common tasks.
- Integration with VS Code's editor context.
- Support for the `/memory` command to persist preferences across sessions.

**Requirements:**
- Anthropic API key or compatible subscription.
- VS Code extension installed and configured.

### OpenAI Codex

OpenAI Codex operates as a partner agent that can be invoked for code generation
and analysis tasks:

**Key Features:**
- Specialized code generation capabilities.
- Support for multiple programming languages.
- Integration with the Copilot ecosystem.

**Requirements:**
- Requires **Pro+** subscription plan.
- Configured through VS Code settings or CLI.

### Partner Agent Comparison

| Feature | Claude Agent | OpenAI Codex |
|---------|-------------|--------------|
| Context window | Up to 200K tokens | Varies by model |
| Subscription | Anthropic API key | Pro+ required |
| Slash commands | Yes (`/claude`) | Limited |
| Memory persistence | Yes (`/memory`) | No |
| VS Code integration | Full | Full |
| CLI support | Yes | Yes |
| Custom instructions | Via CLAUDE.md | Via settings |

---

## 6. Comprehensive Comparison Table

| Capability | Local | Background | Cloud | Partner |
|------------|-------|------------|-------|---------|
| **Interactivity** | Full dialog | Non-interactive | Async (PR comments) | Varies |
| **Tool access** | All tools | Limited | Sandboxed | Platform-specific |
| **Parallel sessions** | No | Yes | Yes | Yes |
| **File system access** | Full local | Worktree-scoped | Cloud clone | Editor-scoped |
| **Terminal access** | Full | Sandboxed | Sandboxed | Limited |
| **MCP servers** | Yes | Limited | No | Platform-specific |
| **Network access** | Full | Full | Restricted | Varies |
| **Auto PR creation** | No | Optional | Yes | No |
| **CI integration** | Manual | Manual | Automatic | No |
| **Duration** | User-controlled | Hours | 30-60 min | User-controlled |
| **Best for** | Exploration, debug | Batch tasks | Issue-driven dev | Specialized models |
| **Cost model** | Subscription | Subscription | Subscription + compute | API key / Pro+ |

---

## 7. Security and Trust Model

### Trust Boundaries by Environment

```
┌─────────────────────────────────────────────────────┐
│  Trust Level                                         │
│                                                      │
│  HIGH ──── Local Agent                               │
│            │  Full access to your machine             │
│            │  You observe every action                │
│            │  Confirmations required for risky ops    │
│            │                                          │
│  MEDIUM ── Background Agent                          │
│            │  Worktree isolation                      │
│            │  No UI access                            │
│            │  Sandboxed terminal                      │
│            │                                          │
│  MEDIUM ── Partner Agent                             │
│            │  Platform-specific sandboxing             │
│            │  Data sent to third-party API             │
│            │  Governed by provider's privacy policy    │
│            │                                          │
│  LOWER ─── Cloud Agent                               │
│               Runs on GitHub infrastructure           │
│               Network-restricted sandbox              │
│               No local machine access                 │
│               Auditable via PR history                │
└─────────────────────────────────────────────────────┘
```

### Security Considerations

| Environment | Key Security Concern | Mitigation |
|-------------|---------------------|------------|
| Local | Agent runs arbitrary commands on your machine | Confirmation prompts, tool allowlists |
| Background | Non-interactive -- no confirmation prompts | Worktree isolation, sandboxed terminal |
| Cloud | Code executes on shared infrastructure | Container isolation, network restrictions |
| Partner | Data sent to third-party providers | Review provider privacy policies, API key scoping |

### Repository Permissions

- **Cloud agents** respect repository access controls. They can only operate on
  repositories the authenticated user has write access to.
- **Background agents** inherit the permissions of the user's git credentials.
- **Partner agents** are scoped to the files open in the editor unless explicitly
  granted broader access.

---

## 8. Integration with External Platforms

### Slack Integration

Cloud and background agents can post updates to Slack channels:

- Task completion notifications.
- PR creation alerts.
- Error reports requiring human intervention.

Configuration is managed through GitHub App settings and Slack webhook URLs.

### Teams Integration

Similar to Slack, Microsoft Teams integration provides:

- Notification cards for agent activity.
- Actionable messages (approve, reject, request changes).
- Thread-based discussion of agent outputs.

### Linear Integration

For teams using Linear for project management:

- Cloud agents can be triggered from Linear issues.
- Status updates flow back to Linear automatically.
- PR links are attached to the originating Linear issue.

---

## 9. Session Management

### Unified Session View

All agent sessions -- local, background, cloud, and partner -- can be viewed from
a unified interface:

- **VS Code:** The Copilot Sessions panel shows active and completed sessions.
- **GitHub.com:** The Copilot dashboard displays cloud agent activity.
- **CLI:** `gh copilot sessions list` shows background session status.

### Session Operations

| Operation | Command / Action |
|-----------|-----------------|
| List sessions | `gh copilot sessions list` |
| View session details | `gh copilot sessions view <id>` |
| Filter by status | `gh copilot sessions list --status active` |
| Filter by type | `gh copilot sessions list --type background` |
| Archive session | `gh copilot sessions archive <id>` |
| Delete session | `gh copilot sessions delete <id>` |
| Resume session | `gh copilot sessions resume <id>` (local only) |

### Session Lifecycle

```
Created ──► Running ──► Completed
                │            │
                ▼            ▼
             Failed      Archived
                │
                ▼
            Retryable
```

---

## 10. Hand-Off Patterns

### Local to Background

When a local session identifies a long-running task, delegate it to a background
agent:

```
# In VS Code chat:
"This migration will take a while. Run it as a background task."

# Equivalent CLI:
gh copilot agent --task "Complete the database migration started in session X" --worktree
```

### Local to Cloud

For tasks that benefit from GitHub's CI integration:

```
# In VS Code chat:
"Create an issue for this feature and assign it to Copilot."

# The cloud agent picks up the issue and creates a PR
```

### Background to Cloud with /delegate

The `/delegate` command transfers a background task to a cloud agent:

```bash
# Background agent encounters a task requiring CI validation
# It can delegate to a cloud agent:
gh copilot delegate --task "Run full integration test suite and fix failures" --to cloud
```

### Hand-Off Decision Matrix

| From | To | When |
|------|----|------|
| Local | Background | Task is well-defined, will take >10 minutes |
| Local | Cloud | Task benefits from CI, needs a PR |
| Background | Cloud | Task needs GitHub Actions or network resources |
| Cloud | Local | Task requires interactive debugging or MCP tools |
| Any | Partner | Task benefits from a specific model's strengths |

---

## Summary

The agent execution spectrum gives developers flexibility to match the right
execution environment to each task. Local agents excel at interactive exploration
and debugging. Background agents handle batch work without blocking your editor.
Cloud agents automate issue-to-PR workflows with CI integration. Partner agents
provide access to specialized models and capabilities. Understanding when and how
to use each type -- and how to hand off between them -- is key to maximizing
productivity with AI-assisted development.

---

## Further Reading

- [GitHub Copilot Coding Agent Documentation](https://docs.github.com/en/copilot/using-github-copilot/using-the-github-copilot-coding-agent)
- [Copilot CLI Reference](https://docs.github.com/en/copilot/github-copilot-in-the-cli)
- Reading 07: Agent Mode and Coding Agent (local agent fundamentals)
- Reading 11: Multi-Agent Architecture (sub-agent patterns)
- Reading 13: Agent Skills and Custom Agents (configuring agents)
