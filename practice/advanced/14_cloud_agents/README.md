# Module 14: Cloud Coding Agents and Background Agents

> **Last verified**: February 2026 | [Official Docs](https://code.visualstudio.com/docs/copilot/agents/cloud-agents)

## Prerequisites and Access

- **VS Code**: Latest version (1.100+)
- **GitHub Copilot**: Pro, Business, or Enterprise subscription
- **GitHub Repository Access**: Push access to at least one GitHub repository
- **Agent mode**: Enabled (`chat.agent.enabled: true`)
- **Background agents**: Copilot CLI installed (VS Code auto-installs it)
- **Cloud agents**: GitHub Copilot Coding Agent enabled in repository settings

---

## Overview

GitHub Copilot offers **four distinct execution environments** for AI-powered coding assistance. Each environment trades off interactivity, tool access, and isolation differently. Understanding when to use each is essential for maximizing productivity:

1. **Local Agent** -- Runs interactively in your VS Code workspace with full tool access (MCP, extensions, terminal). You guide the conversation in real time.
2. **Background Agent** -- Runs non-interactively on your local machine via the Copilot CLI. Works in an isolated git worktree so it cannot interfere with your active workspace.
3. **Cloud Coding Agent (GitHub)** -- Runs on remote GitHub infrastructure. Can autonomously create pull requests, respond to issues, and work at scale across repositories.
4. **Partner Agents** -- Third-party agents (Claude Agent by Anthropic, OpenAI Codex) that run on their own cloud infrastructure and integrate with GitHub workflows.

This module covers Background Agents (Section A), Cloud Coding Agents (Section B), and guidance on choosing the right agent type (Section C).

---

## Section A: Background Agents

### What Are Background Agents?

Background agents are **CLI-based tools that run non-interactively on your local machine**. The primary implementation is the Copilot CLI, which VS Code manages automatically. When you start a background agent session, it:

- Launches a headless Copilot CLI process
- Creates an isolated git worktree for the task
- Works autonomously without requiring your input
- Commits changes at the end of each turn
- Reports results back to the VS Code Chat view

### Git Worktrees: Automatic Isolation

Background agents use **git worktrees** to prevent conflicts with your main workspace. A worktree is a separate checkout of the same repository in a different folder on disk.

```
your-project/                  <-- Your main workspace (untouched)
your-project-worktrees/
  bg-session-abc123/           <-- Background agent's isolated workspace
  bg-session-def456/           <-- Another background agent's workspace
```

Key behaviors:
- Worktrees are created automatically when the session starts
- Each background agent session gets its own worktree
- Changes are committed at the end of each agent turn
- You can review changes in the Source Control view before merging
- Worktrees are cleaned up when you dismiss the session

### Starting a Background Agent Session

There are four ways to start a background agent:

**Method 1: Chat View Session Type Dropdown**
1. Open the Chat view (`Ctrl+Shift+I` / `Cmd+Shift+I`)
2. Click the **Session Type** dropdown at the top of the Chat panel
3. Select **Background**
4. Enter your task description and press Enter

**Method 2: `@cli` Command**
```
@cli Refactor the authentication module to use async/await
```

**Method 3: Command Palette**
1. Open Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
2. Search for **"Copilot: Start Background Agent Session"**
3. Enter your task description

**Method 4: Hand Off from Local Session**
While working in a local agent session, you can delegate the remaining work to a background agent by changing the session type dropdown from "Local" to "Background." The full conversation history carries over.

### Limited Tool Access

Background agents have **restricted tool access** compared to local agents:

| Capability | Local Agent | Background Agent |
|-----------|-------------|-----------------|
| File read/write | Yes | Yes |
| Terminal commands | Yes | Yes |
| MCP servers | Yes | **No** |
| VS Code extension tools | Yes | **No** |
| Browser/web access | Via MCP | **No** |
| Model selection | Full | CLI models only |

This means background agents are best suited for **well-defined tasks** where the agent does not need to query external services or use specialized VS Code extensions.

### Parallel Sessions

You can run **multiple background agent sessions simultaneously**. Each operates in its own worktree with its own context:

```
Session 1: "Add input validation to all API endpoints"     --> worktree-1/
Session 2: "Write unit tests for the user service"          --> worktree-2/
Session 3: "Update all deprecated dependency imports"       --> worktree-3/
```

Monitor all active sessions in the Chat view's session list. Each session shows its status (running, completed, or failed) and a summary of changes.

### Multi-Repo Workspaces

When your VS Code workspace contains **multiple repositories** (e.g., a monorepo with submodules or a multi-root workspace), you can choose which repository the background agent targets. The **repository picker** appears in the session configuration when multiple repos are detected.

### Settings

Key settings for background agents:

| Setting | Description | Default |
|---------|-------------|---------|
| `github.copilot.chat.cli.customAgents.enabled` | Enable custom agents (`.agent.md`) in background CLI sessions | `false` |
| `github.copilot.chat.backgroundAgent.enabled` | Enable background agent sessions | `true` |

To enable custom agents in background sessions:

```json
{
  "github.copilot.chat.cli.customAgents.enabled": true
}
```

---

## Section B: Cloud Coding Agents

### What Are Cloud Coding Agents?

Cloud coding agents **execute on remote infrastructure**, not on your machine. They can work autonomously on issues, create pull requests, and respond to feedback -- all without occupying your local resources.

### GitHub Copilot Coding Agent

The **GitHub Copilot Coding Agent** is GitHub's native cloud agent. It works directly with GitHub issues and pull requests:

- Analyzes issue descriptions to understand the task
- Clones the repository in a cloud environment
- Makes code changes autonomously
- Creates a pull request with the changes
- Responds to review comments and feedback

**Starting a Cloud Agent Session:**

**Option 1: Assign `@copilot` to a GitHub Issue**
1. Navigate to a GitHub issue
2. In the Assignees section, assign `@copilot`
3. Copilot begins working on the issue and creates a draft PR

**Option 2: Chat View Cloud Option**
1. Open the Chat view in VS Code
2. Set the Session Type dropdown to **Cloud**
3. Enter your task description
4. Copilot works on GitHub's infrastructure and creates a PR

**Option 3: `/delegate` from a Background Agent**
While a background agent is running, use `/delegate` to escalate the task to a cloud agent. The conversation history and context transfer automatically.

### Partner Agents

GitHub supports **third-party cloud agents** that integrate with its ecosystem:

#### Claude Agent (Anthropic)

Available with GitHub Copilot Pro, Business, or Enterprise subscriptions. Claude Agent provides specialized slash commands:

| Command | Description |
|---------|-------------|
| `/agents` | List available agents |
| `/hooks` | Configure lifecycle hooks for agent sessions |
| `/memory` | Manage agent memory and context persistence |
| `/init` | Initialize a new project or workspace |
| `/pr-comments` | Review and respond to PR comments |
| `/review` | Perform a code review |
| `/security-review` | Run a security-focused code review |

To enable Claude Agent:
1. Go to your GitHub account settings
2. Navigate to Copilot settings
3. Under "Partner agents," enable **Claude Agent (Anthropic)**

#### OpenAI Codex

Available with **GitHub Copilot Pro+** subscription tier. OpenAI Codex provides autonomous coding capabilities on OpenAI's infrastructure.

To enable:
1. Go to your GitHub account settings
2. Navigate to Copilot settings
3. Under "Partner agents," enable **OpenAI Codex**
4. Requires a Pro+ subscription (Pro tier is not sufficient)

### MCP in Cloud Environments

Cloud agents **can access MCP servers** configured in the remote environment. This differs from background agents, which cannot use MCP:

- Configure MCP servers in `.vscode/mcp.json` or `.github/copilot/mcp.json`
- Cloud agents read these configurations when they clone your repository
- Useful for database access, API integrations, or custom tooling in CI/CD pipelines

```json
// .github/copilot/mcp.json
{
  "servers": {
    "project-db": {
      "type": "stdio",
      "command": "npx",
      "args": ["@my-org/db-mcp-server"],
      "env": {
        "DATABASE_URL": "${secrets.DATABASE_URL}"
      }
    }
  }
}
```

### Integration with External Tools

Cloud agents integrate with collaboration platforms:

- **Slack**: Receive notifications about agent progress; start agent sessions from Slack
- **Microsoft Teams**: Similar notification and trigger capabilities
- **Linear**: Assign issues to Copilot directly from Linear; agent creates PRs in the linked GitHub repo

### Firewall and Environment Customization

For enterprise environments:

- **Firewall rules**: Cloud agents run on GitHub's IP ranges; ensure your firewall allows outbound connections from your repository's CI/CD runners
- **Custom Docker images**: Specify a custom development container (`devcontainer.json`) for the cloud agent's execution environment
- **Secrets**: Use GitHub Actions secrets or Copilot-specific secret storage for sensitive values

### Custom Model Selection

You can configure which model the cloud coding agent uses:

1. Navigate to your repository settings on GitHub
2. Go to **Copilot > Coding Agent**
3. Under **Model**, select your preferred model
4. The selected model applies to all coding agent sessions for that repository

### Session Tracking

Monitor cloud agent sessions from multiple clients:

| Client | How to Track |
|--------|-------------|
| **VS Code** | Chat view > Sessions list > Filter by "Cloud" |
| **JetBrains** | Copilot tool window > Agent Sessions |
| **GitHub CLI** | `gh copilot sessions list --type cloud` |
| **Raycast** | Copilot extension > Active Sessions |

---

## Section C: Choosing the Right Agent Type

### Comparison Table

| Feature | Local Agent | Background Agent | Cloud Agent |
|---------|------------|-----------------|-------------|
| **Runs on** | Your machine | Your machine (CLI) | GitHub cloud |
| **Interactive** | Yes | No | No |
| **Tool access** | Full (MCP, extensions) | Limited (CLI only) | MCP in remote env |
| **Best for** | Exploratory, ambiguous tasks | Well-defined, parallel tasks | Large-scale, team PRs |
| **Git isolation** | No (same workspace) | Yes (worktrees) | Yes (branches) |
| **Requires internet** | For Copilot API only | For Copilot API only | Yes (fully remote) |
| **Resource usage** | Your CPU/RAM | Your CPU/RAM (lighter) | Zero local resources |
| **Session persistence** | Until VS Code closes | Until task completes | Until PR is merged |
| **Custom agents** | Full support | Opt-in via setting | Limited |

### Decision Flowchart

```
Is the task well-defined with clear acceptance criteria?
  |
  +-- No --> Use LOCAL AGENT (interactive exploration)
  |
  +-- Yes --> Do you need MCP or extension tools?
               |
               +-- Yes --> Use LOCAL AGENT
               |
               +-- No --> Should it run without using your machine's resources?
                           |
                           +-- Yes --> Use CLOUD AGENT
                           |
                           +-- No --> Do you have other tasks to do simultaneously?
                                       |
                                       +-- Yes --> Use BACKGROUND AGENT
                                       |
                                       +-- No --> Use LOCAL or BACKGROUND AGENT
```

---

## Exercises

### Exercise 1: Background Agent Setup and First Task

**File**: [`exercises/background_agent_setup.md`](exercises/background_agent_setup.md)

Set up a background agent session, observe worktree creation, monitor progress, and merge results back to your workspace.

### Exercise 2: Creating GitHub Issues for Cloud Agents

**File**: [`exercises/cloud_agent_issue_template.md`](exercises/cloud_agent_issue_template.md)

Learn to write GitHub issues that `@copilot` can execute effectively, with templates for feature requests and bug fixes.

### Exercise 3: Background Agent Worktree Task

**Files**: [`exercises/worktree_scenario/app.py`](exercises/worktree_scenario/app.py), [`exercises/worktree_scenario/tests/test_app.py`](exercises/worktree_scenario/tests/test_app.py)

A Python Flask-style task management API with intentional bugs and failing tests. Start a background agent to fix the issues while you continue working in your main workspace.

### Exercise 4: Partner Agents Comparison

**File**: [`exercises/partner_agents_comparison.md`](exercises/partner_agents_comparison.md)

Run the same coding task through Claude Agent and OpenAI Codex, then compare their approaches, code quality, and speed.

### Exercise 5: Handing Off from Local to Cloud

**File**: [`exercises/handoff_local_to_cloud.md`](exercises/handoff_local_to_cloud.md)

Start a task locally, research and plan interactively, then delegate the implementation to a cloud agent.

### Exercise 6: Parallel Background Tasks

**File**: [`exercises/parallel_background_tasks.md`](exercises/parallel_background_tasks.md)

Run three background agent sessions simultaneously on independent tasks, monitor all of them, and merge the results.

---

## Key Takeaways

- **Background agents** run locally via the Copilot CLI in isolated git worktrees, ideal for well-defined parallel tasks
- **Cloud agents** run on GitHub's infrastructure and can autonomously create PRs from issues
- **Partner agents** (Claude Agent, OpenAI Codex) extend cloud capabilities with specialized features
- **Worktrees** provide automatic git isolation so background agents never interfere with your active workspace
- **MCP servers** are available in cloud environments but not in background agent sessions
- Use the **Session Type dropdown** in Chat view to switch between Local, Background, and Cloud
- **Parallel sessions** let you delegate multiple tasks simultaneously while you continue working
- Write **clear, structured issues** with acceptance criteria for the best cloud agent results

---

## Next Steps

- **Module 11**: [Sub-Agents and Multi-Agent Architecture](../11_subagents/README.md) -- learn how agents delegate to sub-agents within a single session
- **Module 12**: [Custom Agents](../12_custom_agents/README.md) -- create `.agent.md` files that background agents can use (when `cli.customAgents.enabled` is set)
- **Module 15**: Advanced Agent Orchestration -- combine local, background, and cloud agents in complex workflows
