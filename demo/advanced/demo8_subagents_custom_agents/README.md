# Demo 8: Sub-Agents and Custom Agents

## What This Demo Shows

- **Sub-agent invocation**: How GitHub Copilot spawns isolated sub-agents to handle focused tasks
- **Context management**: Preventing context bloat by delegating work to sub-agents
- **Custom agent definitions**: Creating planning and implementation agents with handoff buttons
- **Parallel execution**: Running multiple sub-agents simultaneously for faster analysis

**Duration**: 20-25 minutes
**Complexity**: Advanced
**Best For**: Teams dealing with complex, multi-step workflows and context management
**Prerequisites**: GitHub Copilot subscription with Agent Mode, VS Code 1.102+

---

## Prerequisites

1. **GitHub Copilot** subscription with access to Agent Mode
2. **VS Code** with GitHub Copilot Chat extension (version 1.102 or later)
3. **Agent Mode** enabled in Copilot Chat settings
4. **Python 3.8+** installed (for the setup files)
5. Familiarity with prompt files and chat modes (see Demo 7)

---

## Quick Setup (2 minutes)

### 1. Navigate to Demo Folder

```bash
cd demo/advanced/demo8_subagents_custom_agents
```

### 2. Review Setup Files

Open the `setup/` folder and review the three Python files and the agent/prompt definitions:

- `setup/auth_service.py` - Authentication service with intentional issues
- `setup/user_model.py` - User data model
- `setup/config.py` - Application configuration
- `setup/research-implement.prompt.md` - Prompt file with sub-agent tooling
- `setup/plan.agent.md` - Planning agent definition
- `setup/implement.agent.md` - Implementation agent definition

### 3. Open Copilot Chat

- Press `Ctrl/Cmd + Shift + I` to open Copilot Chat
- Switch to **Agent Mode** from the chat mode dropdown
- Ensure you have the demo folder open as your workspace

---

## Demo Steps

### Step 1: The Context Bloat Problem (3 minutes)

**Goal**: Show why sub-agents matter by demonstrating context degradation.

1. **Open Copilot Chat** in Agent Mode
2. **Start a long conversation** -- ask Copilot to:
   - Explain the architecture of `auth_service.py`
   - Then ask about the user model
   - Then ask about the config
   - Then ask it to remember what security issues were in `auth_service.py`

3. **Point out to the audience**:
   - The agent's answers become less focused as the conversation grows
   - Earlier context gets diluted by later questions
   - The agent may forget or misremember details from earlier in the conversation

4. **Key message**: _"The more we add to a single conversation, the less effective the agent becomes. Sub-agents solve this by giving each task its own isolated context."_

---

### Step 2: Sub-Agent Invocation via Prompt Hinting (5 minutes)

**Goal**: Show how to hint at sub-agent usage in a prompt, causing Copilot to spawn an isolated research agent before implementing.

1. **Start a fresh chat session** (important -- clear the previous context)

2. **Open** `setup/auth_service.py` in the editor

3. **Copy and paste this prompt** (also available in `prompts.md`):

   ```
   First, use a sub-agent to research current authentication patterns
   in this project and best practices for JWT auth. Then implement the
   recommended approach in auth_service.py.
   ```

4. **Watch for sub-agent behavior**:
   - Copilot should spawn a sub-agent to research the codebase
   - The research sub-agent reads files and gathers patterns in its own context
   - Results are returned to the main agent
   - The main agent then implements changes using the research findings

5. **Point out to the audience**:
   - The research phase had its own isolated context
   - The main agent received a clean summary, not the full research context
   - This keeps the implementation context focused and effective

---

### Step 3: Prompt File with tools: ['agent'] (5 minutes)

**Goal**: Show how a prompt file can automatically spawn sub-agents using the `agent` tool.

1. **Open** `setup/research-implement.prompt.md` and walk through its structure:

   ```markdown
   ---
   description: Research a topic then implement changes using sub-agents
   mode: agent
   tools: ['agent', 'codebase', 'search', 'editFiles']
   ---
   ```

2. **Explain the key insight**: The `agent` tool in the tools array tells Copilot it can spawn sub-agents automatically

3. **Run the prompt file** by typing in Copilot Chat:

   ```
   /research-implement Add input validation to all API endpoints in this project
   ```

4. **Observe the behavior**:
   - A sub-agent spawns to research current validation patterns
   - Another sub-agent may analyze the API endpoints
   - The main agent synthesizes findings and implements validation

5. **Compare context usage**:
   - Show how the main agent's context stays clean
   - Sub-agent work is summarized, not dumped into the main context
   - The final implementation is more focused and accurate

---

### Step 4: Custom Agent with Handoffs (5 minutes)

**Goal**: Demonstrate pre-defined agents that hand off work to each other via buttons.

1. **Open** `setup/plan.agent.md` and explain:
   - This agent only has read-only tools (`readFile`, `search`, `listFiles`)
   - It cannot edit files -- it only plans
   - It defines a handoff to the `implement` agent

2. **Open** `setup/implement.agent.md` and explain:
   - This agent has write tools (`editFiles`, `runTerminalCommand`)
   - It follows plans created by the planning agent
   - It can hand back to `plan` for next steps

3. **Activate the planning agent** by pasting this prompt:

   ```
   Plan a refactoring of this authentication service to use bcrypt
   and proper JWT tokens
   ```

4. **Watch the planning agent work**:
   - It reads `auth_service.py`, `user_model.py`, and `config.py`
   - It produces a structured plan: Current State, Proposed Changes, Steps, Risks
   - It does NOT modify any files

5. **Show the handoff button**: After the plan completes, a button labeled **"Implement this plan"** should appear

6. **Click the handoff button**:
   - The implementation agent receives the plan
   - It begins making changes following the plan exactly
   - Point out the `autoSubmit: false` setting -- the user confirms before the handoff executes

---

### Step 5: Parallel Sub-Agent Execution (5 minutes)

**Goal**: Show multiple sub-agents running simultaneously for faster analysis.

1. **Start a fresh chat session**

2. **Paste this prompt** (also in `prompts.md`):

   ```
   Analyze this project in parallel using sub-agents:
   1) Review auth_service.py for security vulnerabilities
   2) Review user_model.py for data modeling best practices
   3) Review config.py for configuration issues
   Synthesize all findings into a single report.
   ```

3. **Observe parallel execution**:
   - Multiple sub-agents should spin up simultaneously
   - Each analyzes its assigned file independently
   - Progress indicators may show multiple agents working

4. **Show synthesized results**:
   - The main agent collects all sub-agent findings
   - It produces a unified report covering all three files
   - Cross-cutting concerns are identified (e.g., the hardcoded secret in config affects auth_service)

5. **Key message**: _"Parallel sub-agents turn a 3-minute sequential review into a faster parallel analysis, with each agent maintaining its own focused context."_

---

## Key Messages for Your Audience

1. **"Context is finite"** -- Every agent conversation has a limited context window. Sub-agents let you use that budget wisely.
2. **"Divide and conquer"** -- Complex tasks are better handled by specialized agents than one overloaded conversation.
3. **"Handoffs preserve intent"** -- Custom agents with handoff buttons create structured workflows that maintain quality.
4. **"Parallelism speeds analysis"** -- Multiple sub-agents working simultaneously can dramatically reduce review time.
5. **"You stay in control"** -- `autoSubmit: false` means the human always approves before handoffs execute.

---

## Expected Outcomes

After each step, you should observe:

| Step | What You Should See |
|------|-------------------|
| Step 1 | Context degradation in long conversations; agent forgets earlier details |
| Step 2 | Sub-agent spawns for research; main agent receives clean summary |
| Step 3 | Prompt file triggers automatic sub-agent spawning via `tools: ['agent']` |
| Step 4 | Plan agent produces read-only analysis; handoff button appears; implement agent follows the plan |
| Step 5 | Multiple sub-agents run in parallel; synthesized report covers all files |

---

## Troubleshooting

### Sub-agents not spawning

- Ensure you are in **Agent Mode** (not Ask or Edit mode)
- Check that your VS Code version is 1.102 or later
- Verify the prompt file has `tools: ['agent']` in its frontmatter
- Try being more explicit: "Use a sub-agent to research..."

### Handoff buttons not appearing

- Verify the `.agent.md` files are in the correct location
- Check the YAML frontmatter syntax in `plan.agent.md` and `implement.agent.md`
- Ensure the `target` field matches the `name` field of the target agent exactly
- Restart VS Code if agent files were just created

### Parallel execution not visible

- Not all Copilot versions support visible parallel sub-agents
- The behavior may appear sequential even if internally parallelized
- Focus on the synthesized output quality rather than visual parallelism

### Agent files not detected

- Agent files must use the `.agent.md` extension
- They should be in `.github/agents/` or the workspace root
- For this demo, the `setup/` folder files can be copied to `.github/agents/`

---

## Success Metrics

After this demo, your audience should understand:

- Sub-agents prevent context bloat by isolating tasks
- The `agent` tool in prompt files enables automatic sub-agent spawning
- Custom agents with handoffs create structured, repeatable workflows
- Parallel sub-agents accelerate multi-file analysis
- Human oversight is maintained through `autoSubmit: false`

---

## Next Steps

- Create custom agents for your team's specific workflows (e.g., security review, documentation generation)
- Define prompt files that leverage sub-agents for complex multi-step tasks
- Experiment with handoff chains: plan -> implement -> test -> review
- Combine with MCP servers (Demo 7) for agents that interact with external services
