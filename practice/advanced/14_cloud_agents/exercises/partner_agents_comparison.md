# Exercise 4: Partner Agents Comparison -- Claude Agent vs OpenAI Codex

> **Objective**: Run the same coding task through both Claude Agent (Anthropic) and OpenAI Codex, then compare their approaches, code quality, tool usage, and speed.

---

## Prerequisites

### Claude Agent (Anthropic)

- **Subscription**: GitHub Copilot Pro, Business, or Enterprise
- **Enable**: GitHub account settings > Copilot > Partner agents > enable **Claude Agent (Anthropic)**
- **Access**: Available for repositories where Copilot is enabled

### OpenAI Codex

- **Subscription**: GitHub Copilot **Pro+** (Pro tier is not sufficient)
- **Enable**: GitHub account settings > Copilot > Partner agents > enable **OpenAI Codex**
- **Access**: Available for repositories where Copilot is enabled

### Verification

Confirm both agents are enabled:

1. Go to [github.com/settings/copilot](https://github.com/settings/copilot)
2. Scroll to **Partner agents**
3. Both Claude Agent and OpenAI Codex should show as "Enabled"

---

## How to Enable Each Agent

### Enabling Claude Agent

1. Navigate to your GitHub account settings
2. Select **Copilot** from the left sidebar
3. Under **Partner agents**, locate **Claude Agent (Anthropic)**
4. Toggle it to **Enabled**
5. Accept any terms of service prompts

Claude Agent provides specialized slash commands:

| Command | Purpose |
|---------|---------|
| `/agents` | List all available agents |
| `/hooks` | Configure lifecycle hooks |
| `/memory` | Manage persistent memory |
| `/init` | Initialize a project workspace |
| `/pr-comments` | Review and respond to PR comments |
| `/review` | Perform a code review |
| `/security-review` | Security-focused code review |

### Enabling OpenAI Codex

1. Navigate to your GitHub account settings
2. Select **Copilot** from the left sidebar
3. Ensure you have a **Pro+** subscription (upgrade if needed)
4. Under **Partner agents**, locate **OpenAI Codex**
5. Toggle it to **Enabled**
6. Accept any terms of service prompts

---

## The Comparison Task

Use the same well-defined task for both agents to enable a fair comparison. Create two identical GitHub issues, one assigned to each agent.

### Task: Add Input Validation to the Task Management API

```markdown
## Feature: Add comprehensive input validation to app.py

### What
Add input validation to all CRUD functions in `exercises/worktree_scenario/app.py`:
1. `create_task`: Validate that title is non-empty and priority is one of
   'low', 'medium', 'high'
2. `get_task`: Raise KeyError when task_id does not exist
3. `update_task`: Raise KeyError for missing tasks; raise ValueError for
   invalid field names (only allow title, description, priority, status)
4. `delete_task`: Raise KeyError when task_id does not exist

### Where
- Primary: `exercises/worktree_scenario/app.py`
- Tests: `exercises/worktree_scenario/tests/test_app.py`

### Acceptance Criteria
- [ ] All existing passing tests continue to pass
- [ ] All currently failing tests now pass
- [ ] No new dependencies added
- [ ] Code follows existing style (type hints, docstrings)
```

---

## Running the Comparison

### Step 1: Create Issue for Claude Agent

1. Create a new issue in your repository with the task above
2. Title: `[Claude] Add input validation to Task Management API`
3. Assign `@copilot` and select Claude Agent as the partner agent
4. Note the **start time**

### Step 2: Create Issue for OpenAI Codex

1. Create a second identical issue
2. Title: `[Codex] Add input validation to Task Management API`
3. Assign `@copilot` and select OpenAI Codex as the partner agent
4. Note the **start time**

### Step 3: Wait for Both to Complete

Monitor both issues and their resulting PRs. Record the completion time for each.

---

## What to Compare

Fill in this comparison table after both agents complete:

### Evaluation Criteria

| Criterion | Claude Agent | OpenAI Codex | Notes |
|-----------|-------------|-------------|-------|
| **Time to first commit** | ___ min | ___ min | |
| **Time to completion** | ___ min | ___ min | |
| **Number of commits** | ___ | ___ | |
| **Tests passing** | ___/total | ___/total | |
| **Lines changed** | ___ | ___ | |
| **Files modified** | ___ | ___ | |

### Approach Comparison

| Aspect | Claude Agent | OpenAI Codex |
|--------|-------------|-------------|
| **Planning** | Did it explain its approach first? | Did it explain its approach first? |
| **Order of changes** | Which functions did it fix first? | Which functions did it fix first? |
| **Validation style** | How did it implement validation? (if/raise, decorators, etc.) | How did it implement validation? |
| **Error messages** | Quality and specificity of error messages | Quality and specificity of error messages |
| **Edge cases** | Did it handle edge cases beyond the spec? | Did it handle edge cases beyond the spec? |

### Code Quality Comparison

| Quality Metric | Claude Agent | OpenAI Codex |
|---------------|-------------|-------------|
| **Docstrings updated** | Yes / No / Partially | Yes / No / Partially |
| **Type hints preserved** | Yes / No | Yes / No |
| **Consistent style** | Matches existing code? | Matches existing code? |
| **Unnecessary changes** | Any unrelated modifications? | Any unrelated modifications? |
| **Copy safety** | Did it fix the list_tasks copy issue? | Did it fix the list_tasks copy issue? |

### Tool Usage Comparison

| Tool Behavior | Claude Agent | OpenAI Codex |
|--------------|-------------|-------------|
| **File reading** | How many files read? | How many files read? |
| **Test execution** | Did it run tests? How many times? | Did it run tests? How many times? |
| **Iterative fixing** | Did it fix issues found by tests? | Did it fix issues found by tests? |
| **Terminal usage** | What commands did it run? | What commands did it run? |

---

## Limitations of Each Agent

### Claude Agent Limitations

- Requires Copilot Pro, Business, or Enterprise (not available on free tier)
- Slash commands (`/review`, `/security-review`, etc.) are specific to Claude Agent and not available in other agent types
- Memory persistence (`/memory`) scope is limited to the repository
- May approach tasks differently than other agents due to Anthropic's model training
- Session history is not transferable to other partner agents

### OpenAI Codex Limitations

- Requires **Pro+** subscription (higher cost than Pro)
- Not available to all GitHub users (regional and subscription restrictions)
- Fewer specialized commands compared to Claude Agent
- May have different context window limits than Claude Agent
- Response style and verbosity may differ from Claude Agent

### General Partner Agent Limitations

- Neither partner agent has access to VS Code extension tools
- MCP server access depends on remote environment configuration
- Both are subject to GitHub's rate limits for Copilot API calls
- Neither can access private resources outside the repository (databases, internal APIs) unless configured via MCP or environment secrets
- Partner agent availability may change as GitHub updates its Copilot offerings

---

## Reflection Questions

After completing the comparison, consider:

1. Which agent produced code that better matched the existing codebase style?
2. Which agent was faster to complete the task?
3. Did either agent handle edge cases that the other missed?
4. Which agent's PR was easier to review?
5. Would you choose different agents for different types of tasks? If so, what criteria would you use?

---

## What You Learned

- How to enable and use both Claude Agent and OpenAI Codex
- How to set up a controlled comparison between partner agents
- The strengths and limitations of each partner agent
- How to evaluate agent output for code quality, speed, and correctness

---

## Next Exercise

Proceed to [Exercise 5: Handing Off from Local to Cloud](handoff_local_to_cloud.md) to learn how to start a task locally and delegate it to a cloud agent.
