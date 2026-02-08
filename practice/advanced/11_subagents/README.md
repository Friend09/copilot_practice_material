# Module 11: Sub-Agents and Multi-Agent Architecture

> **Last verified**: February 2026 | [Official Docs](https://code.visualstudio.com/docs/copilot/agents/subagents)

## Prerequisites and Access

- **VS Code**: Latest version (1.100+)
- **GitHub Copilot**: Pro, Business, or Enterprise subscription
- **Agent mode**: Enabled (`chat.agent.enabled: true`)
- **Sub-agents**: Currently supported in local agent sessions only

---

## Overview

As your agent sessions grow longer, the context window fills up with information from every prompt and response. This **context bloat** makes the agent less effective — it loses focus, gives contradictory answers, and wastes tokens on irrelevant history.

**Sub-agents** solve this by spawning autonomous agents with their own isolated context windows. The main agent delegates a task, the sub-agent works independently, and only the final result flows back. Think of it as the agent's ability to "go research something and come back with the answer."

---

## Core Concepts

### 1. What is a Sub-Agent?

A sub-agent is an autonomous agent started as part of an agent session but operating independently with its own context window. Key properties:

- **Isolated context**: Sub-agent conversation history does NOT accumulate in the main agent's context
- **Parallel execution**: Multiple sub-agents can run simultaneously
- **Result summary**: Only the final output returns to the main agent
- **Inherited defaults**: Sub-agents inherit the main session's agent and model by default

### 2. Why Use Sub-Agents?

| Problem | Without Sub-Agents | With Sub-Agents |
|---------|-------------------|-----------------|
| Research before coding | Main agent reads 20 files, context bloats | Sub-agent researches, returns 1-paragraph summary |
| Comparing approaches | Sequential exploration, everything in one context | 3 parallel sub-agents, each exploring one approach |
| Code review | Long context with all review findings | Separate sub-agents for security, performance, style |
| Multi-file analysis | Agent gets confused with too much context | Each sub-agent analyzes one area |

### 3. How to Invoke Sub-Agents

**Method 1: Prompt hinting** — Simply describe a task that implies delegation:

```
"First, use a sub-agent to research best practices for JWT authentication
in Python. Then implement the recommended approach."
```

The main agent recognizes this as a sub-agent task and delegates automatically.

**Method 2: Prompt file with `tools: ['agent']`** — Explicitly enable sub-agent spawning:

```yaml
---
name: research-and-implement
tools: ['agent', 'readFile', 'search', 'editFiles']
---
Research the topic first using a sub-agent, then implement based on findings.
```

**Method 3: Custom agent with `agents` property** — Control which sub-agents are available:

```yaml
---
name: architect
agents: ['researcher', 'security-review']
tools: ['readFile', 'search']
---
You can delegate research to the researcher agent and
security checks to the security-review agent.
```

### 4. Configuration Options

**Control sub-agent availability in custom agents:**

```yaml
# Allow all sub-agents
agents: ['*']

# Allow specific sub-agents only
agents: ['researcher', 'tester']

# Disable all sub-agents
agents: []
```

**Prevent an agent from being used as a sub-agent:**

```yaml
---
name: main-orchestrator
disable-model-invocation: true
---
```

**Create sub-agent-only agents (not shown in dropdown):**

```yaml
---
name: internal-helper
user-invokable: false
---
This agent can only be invoked as a sub-agent by other agents.
```

### 5. Parallel Sub-Agent Execution

Sub-agents can run in parallel when tasks are independent:

```
"In parallel:
1. Use a sub-agent to analyze the database module for performance issues
2. Use a sub-agent to review the auth module for security vulnerabilities
3. Use a sub-agent to check the API module for missing error handling

Then synthesize all findings into a prioritized action plan."
```

---

## Exercises

### Exercise 1: Trigger a Sub-Agent by Prompt Hinting

Use the Python project in `exercises/parallel_analysis_scenario/` as your workspace.

1. Open VS Code Chat in Agent mode
2. Enter this prompt:
   ```
   First, use a sub-agent to research how the authentication is
   currently implemented across this project. Then, based on the
   findings, suggest improvements to the auth flow.
   ```
3. Observe: the agent should spawn a sub-agent for research, receive a summary, then provide recommendations
4. Compare this to asking the same question without sub-agents — notice how context stays cleaner

### Exercise 2: Create a Prompt File with Sub-Agent Support

Use the template in `exercises/subagent_prompt_file.prompt.md`.

1. Copy the file to `.github/prompts/research-implement.prompt.md`
2. Open the Chat view and use the prompt via `/research-implement`
3. Provide a task like: "Add rate limiting to the API endpoints"
4. Observe the sub-agent research phase followed by implementation

### Exercise 3: Parallel Sub-Agent Analysis

Using the files in `exercises/parallel_analysis_scenario/`:

1. Open Chat in Agent mode
2. Enter:
   ```
   Analyze this project in parallel using sub-agents:
   - Sub-agent 1: Review api.py for REST API best practices
   - Sub-agent 2: Review database.py for query optimization
   - Sub-agent 3: Review auth.py for security vulnerabilities
   Synthesize all findings into a single prioritized report.
   ```
3. Observe parallel execution and the synthesized output

### Exercise 4: Configure Custom Agent with Sub-Agent Access

1. Create `.github/agents/architect.agent.md`:
   ```yaml
   ---
   name: architect
   description: Designs solutions using specialized sub-agents
   tools: ['readFile', 'search', 'listFiles']
   agents: ['researcher', 'security-review']
   ---
   You are a software architect. Delegate research to the
   researcher sub-agent and security checks to security-review.
   ```
2. Create the `researcher` and `security-review` agents (or use samples from Module 12)
3. Set `user-invokable: false` on the sub-agents so they only appear as sub-agents
4. Test the architect agent — it should automatically delegate to its sub-agents

### Exercise 5: Compare Single-Agent vs Multi-Agent

Run the same complex task both ways and compare:

1. **Single agent**: Ask the default agent to "Review this entire project for security issues, performance problems, and code quality, then fix everything"
2. **Multi-agent**: Use the architect agent from Exercise 4 that delegates to specialized sub-agents
3. Compare: context usage, response quality, specificity of findings

---

## Key Takeaways

- Sub-agents prevent context bloat by isolating research and analysis tasks
- Invoke via prompt hints, `tools: ['agent']` in prompt files, or `agents` in custom agents
- Parallel sub-agents handle independent tasks simultaneously
- Use `user-invokable: false` for sub-agent-only agents
- Use `disable-model-invocation: true` to prevent an agent from being used as a sub-agent
- Only the final result from sub-agents enters the main context

---

## Next Steps

- **Module 12**: Create custom agents with `.agent.md` format (prerequisite for advanced sub-agent configuration)
- **Module 13**: Build Agent Skills that sub-agents can leverage
- **Module 14**: Learn about background and cloud agents (different execution environments)
