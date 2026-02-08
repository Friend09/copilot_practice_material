# Demo 8: Sub-Agents and Custom Agents - Prompts

Copy-paste these prompts during the live demo. Each prompt corresponds to a step in the README.

---

## Step 1: The Context Bloat Problem

Use these prompts sequentially in a single chat session to demonstrate context degradation:

### Prompt 1a: Initial analysis

```
Explain the architecture and design patterns used in setup/auth_service.py. What are its main components?
```

### Prompt 1b: Shift to user model

```
Now analyze setup/user_model.py. What data modeling patterns does it use? How does it relate to the auth service?
```

### Prompt 1c: Shift to config

```
Review setup/config.py. What configuration patterns are used? Are there any issues with how settings are managed?
```

### Prompt 1d: Test context retention

```
Based on everything we've discussed, what were the top 3 security vulnerabilities in auth_service.py? Be specific about line numbers and code patterns.
```

> **Presenter note**: The agent will likely struggle with specifics from the earlier auth_service.py analysis because the context has been diluted by subsequent questions. This is the problem sub-agents solve.

---

## Step 2: Sub-Agent Invocation via Prompt Hinting

> **Important**: Start a **fresh chat session** before using this prompt.

```
First, use a sub-agent to research current authentication patterns in this project and best practices for JWT auth. Then implement the recommended approach in auth_service.py.
```

> **Presenter note**: Watch for the sub-agent spawning. The research phase runs in its own context, and the main agent receives a clean summary before implementing changes.

---

## Step 3: Prompt File with tools: ['agent']

> **Important**: This uses the prompt file at `setup/research-implement.prompt.md`.

```
/research-implement Add input validation to all API endpoints in this project
```

> **Presenter note**: The `/research-implement` slash command triggers the prompt file, which has `tools: ['agent']` in its frontmatter, enabling automatic sub-agent spawning.

---

## Step 4: Custom Agent with Handoffs

> **Important**: Ensure `setup/plan.agent.md` and `setup/implement.agent.md` are recognized by VS Code (may need to copy to `.github/agents/`).

### Prompt 4a: Activate the planning agent

```
Plan a refactoring of this authentication service to use bcrypt and proper JWT tokens
```

> **Presenter note**: The planning agent will read all files but NOT modify anything. After it completes, look for the **"Implement this plan"** handoff button.

### Prompt 4b: (Alternative) Manual implementation request after plan

If the handoff button does not appear, you can manually transition:

```
Now implement the plan above. Follow the architecture exactly. Use bcrypt for password hashing and PyJWT for token generation. Add docstrings to all new functions.
```

---

## Step 5: Parallel Sub-Agent Execution

> **Important**: Start a **fresh chat session** before using this prompt.

```
Analyze this project in parallel using sub-agents:
1) Review auth_service.py for security vulnerabilities
2) Review user_model.py for data modeling best practices
3) Review config.py for configuration issues
Synthesize all findings into a single report.
```

> **Presenter note**: Watch for multiple sub-agents spinning up. The main agent should produce a unified report that identifies cross-cutting concerns (e.g., the hardcoded secret key in config.py is used by auth_service.py).

---

## Bonus Prompts

### Bonus 1: Chain multiple agent handoffs

```
First plan the security improvements for this project, then implement them, then write tests for all the changes.
```

### Bonus 2: Focused sub-agent with specific constraints

```
Use a sub-agent to analyze auth_service.py ONLY for OWASP Top 10 vulnerabilities. Do not look at other files. Report findings in a table format with severity ratings.
```

### Bonus 3: Compare approaches with sub-agents

```
Use two sub-agents in parallel:
1) Research the bcrypt approach for password hashing in Python
2) Research the argon2 approach for password hashing in Python
Then compare both approaches and recommend the best one for this project.
```
