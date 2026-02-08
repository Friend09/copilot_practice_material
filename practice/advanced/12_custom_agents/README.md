# Module 12: Custom Agents (.agent.md Format)

> **Last verified**: February 2026 | [Official Docs](https://code.visualstudio.com/docs/copilot/customization/custom-agents)

## Prerequisites and Access

- **VS Code**: Latest version (1.100+)
- **GitHub Copilot**: Pro, Business, or Enterprise subscription
- **Agent mode**: Enabled in settings (`chat.agent.enabled: true`)
- **Organization agents** (optional): `github.copilot.chat.organizationCustomAgents.enabled`

---

## Overview

Custom agents let you define specialized AI personas for specific tasks. Instead of re-explaining your requirements every time you start a chat, you configure agents with tailored instructions, tool access, and workflow transitions (handoffs).

**Key change**: The `.chatmode.md` format has been replaced by `.agent.md`. If you have existing chat modes, they should be migrated to the new format.

---

## Core Concepts

### 1. The .agent.md File Format

Each custom agent is a single Markdown file with a `.agent.md` extension containing two sections:

```yaml
---
# YAML Frontmatter (configuration)
name: my-agent
description: Brief description shown as placeholder text
tools: ['readFile', 'search', 'editFiles']
model: claude-sonnet-4
---

# Body (instructions)
You are a specialized agent that...
```

### 2. Frontmatter Properties

| Property | Type | Description |
|----------|------|-------------|
| `name` | string | Agent identifier (defaults to filename) |
| `description` | string | Shown as placeholder in chat input |
| `tools` | array | Available tools and tool sets. Use `<server>/*` for all MCP server tools |
| `agents` | array | Which sub-agents this agent can invoke. `*` = all, `[]` = none |
| `model` | string or array | Model to use. Array = prioritized fallback list |
| `user-invokable` | boolean | Whether agent appears in the dropdown (default: true) |
| `disable-model-invocation` | boolean | Prevents other agents from invoking this as a sub-agent |
| `handoffs` | array | Workflow transitions to other agents |
| `mcp-servers` | object | MCP server configurations for this agent |

### 3. Handoffs

Handoffs enable sequential workflows that transition between agents:

```yaml
---
name: plan
description: Creates implementation plans
tools: ['readFile', 'search']
handoffs:
  - target: implement
    label: "Implement this plan"
    prompt: "Implement the plan above. Follow the architecture exactly."
    autoSubmit: true
  - target: review
    label: "Review this plan"
---
```

When the planning agent finishes, the user sees buttons for "Implement this plan" and "Review this plan" that transition to the respective agents with full context carried over.

### 4. Storage Locations

| Location | Scope | Sharing |
|----------|-------|---------|
| `.github/agents/` | Workspace | Shared with team via git |
| User profile (VS Code) | Personal | Synced via Settings Sync |
| Organization (via policy) | Org-wide | Requires admin opt-in |

### 5. Tool Priority Chain

When multiple sources define tools, this priority applies:
1. Tools specified in the active prompt file
2. Tools from the referenced custom agent
3. Default agent tools

### 6. Migration from .chatmode.md

The old `.chatmode.md` format is deprecated. To migrate:
1. Rename the file extension from `.chatmode.md` to `.agent.md`
2. Review and update frontmatter properties (same format, new capabilities)
3. Add `handoffs` if you want workflow transitions
4. Add `agents` to control sub-agent access

---

## Exercises

### Exercise 1: Create a Planning Agent

Create a read-only planning agent that analyzes code but never edits it.

**Steps:**
1. Create `.github/agents/plan.agent.md` in your workspace
2. Set `tools` to read-only tools: `['readFile', 'search', 'listFiles']`
3. Write instructions that focus on analysis and planning
4. Test by selecting the agent from the Chat dropdown and asking it to plan a refactoring

**Reference**: See `exercises/sample_agents/plan.agent.md`

### Exercise 2: Create a Security Review Agent with Handoff

Build an agent that reviews code for security issues and hands off to a fix agent.

**Steps:**
1. Create `.github/agents/security-review.agent.md`
2. Add a handoff to an `implement` agent with a "Fix these issues" label
3. Create `.github/agents/implement.agent.md` with write tools
4. Test the full workflow: review finds issues, handoff button transitions to implementation

**Reference**: See `exercises/sample_agents/review.agent.md`

### Exercise 3: Build a Multi-Model Agent

Create an agent that uses a prioritized model fallback list.

**Steps:**
1. Create `.github/agents/smart-coder.agent.md`
2. Set `model` to an array: `['claude-sonnet-4', 'gpt-4o', 'gemini-2.5-pro']`
3. The system will try each model in order until one is available
4. Test with different models enabled/disabled in your settings

### Exercise 4: Create an MCP-Powered Agent

Build an agent that uses specific MCP server tools.

**Steps:**
1. Ensure you have at least one MCP server configured in `.vscode/mcp.json`
2. Create `.github/agents/data-agent.agent.md`
3. Set `tools` to include your MCP server tools: `['myMcpServer/*']`
4. Write instructions that leverage the MCP tools for data access
5. Test by asking the agent to perform tasks using MCP capabilities

### Exercise 5: Migrate a Chat Mode

Convert an existing `.chatmode.md` file to the new `.agent.md` format.

**Steps:**
1. Open `exercises/migrate_chatmode.md` for the starting material
2. Rename the file extension
3. Add `handoffs` for workflow transitions
4. Add `agents` to control sub-agent access
5. Test that the migrated agent works identically plus has new capabilities

---

## Key Takeaways

- Custom agents replace the old chat modes with more powerful configuration
- Handoffs create guided multi-step workflows between specialized agents
- The `agents` property controls sub-agent delegation
- Store agents in `.github/agents/` for team sharing
- Tool priority: prompt file > custom agent > defaults
- Migration from `.chatmode.md` is straightforward (rename + enhance)

---

## Next Steps

- **Module 11**: Learn how sub-agents work with custom agents
- **Module 13**: Create Agent Skills that complement your custom agents
- **Module 14**: Use custom agents with cloud and background agent sessions
