# Exercise: Build a 3-Agent Handoff Chain

## Objective

Create a workflow where three specialized agents work in sequence:
**Research Agent** -> **Implement Agent** -> **Test Agent**

Each agent hands off to the next, carrying full context.

---

## Step 1: Create the Research Agent

Create `.github/agents/research.agent.md`:

```yaml
---
name: research
description: Researches best practices and patterns before implementation
tools: ['readFile', 'search', 'listFiles']
agents: []
handoffs:
  - target: implement
    label: "Implement the recommendation"
    prompt: "Implement the approach recommended above."
    autoSubmit: false
---

You are a Research Agent. When given a task:
1. Search the codebase for existing patterns
2. Identify relevant files and dependencies
3. Research best practices for the approach
4. Recommend a specific implementation strategy
5. List the files that will need changes

Output a structured recommendation with:
- **Approach**: What to do and why
- **Files to modify**: Specific paths
- **New files to create**: If any
- **Dependencies**: New packages or imports needed
- **Risks**: Potential issues to watch for
```

## Step 2: Create the Implementation Agent

Create `.github/agents/implement.agent.md`:

```yaml
---
name: implement
description: Implements code changes based on research recommendations
tools: ['readFile', 'search', 'editFiles', 'runTerminalCommand']
agents: []
handoffs:
  - target: test-verify
    label: "Test these changes"
    prompt: "Run tests and verify the changes made above work correctly."
    autoSubmit: true
---

You are an Implementation Agent. Follow research recommendations exactly.
1. Read the recommended approach
2. Make changes file by file
3. Add docstrings to all new functions
4. Keep changes minimal and focused
```

## Step 3: Create the Test Agent

Create `.github/agents/test-verify.agent.md`:

```yaml
---
name: test-verify
description: Runs tests and verifies code changes work correctly
tools: ['readFile', 'search', 'runTerminalCommand']
agents: []
handoffs:
  - target: implement
    label: "Fix the failures"
    prompt: "Fix the test failures identified above."
    autoSubmit: false
---

You are a Test & Verification Agent.
1. Run the project's test suite
2. Check for lint errors
3. Verify the changes match the original requirements
4. Report any failures with specific details

If all tests pass, confirm the implementation is complete.
If tests fail, provide details for the handoff back to the implementation agent.
```

## Step 4: Test the Chain

1. Select the **research** agent from the Chat dropdown
2. Ask: "Research the best approach to add input validation to our API endpoints"
3. When research is done, click **"Implement the recommendation"**
4. The implement agent makes changes, then auto-submits to the test agent
5. If tests fail, click **"Fix the failures"** to loop back to implement

## What to Observe

- Each agent has access to only the tools it needs
- Context flows through the entire chain via handoffs
- The `autoSubmit: true` on the implement -> test handoff means automatic progression
- The test -> implement handoff is manual (`autoSubmit: false`) so you can review failures first

## Challenge

Modify the chain to add a fourth agent: a **documentation agent** that runs after tests pass and updates README/docstrings based on the changes made.
