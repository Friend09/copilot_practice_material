# Exercise 5: Handing Off from Local Agent to Cloud Agent

> **Objective**: Start a task in a local agent session where you can interactively research and plan, then delegate the implementation to a cloud agent that works autonomously and creates a pull request.

---

## Prerequisites

- VS Code with GitHub Copilot extension (latest version)
- GitHub Copilot Pro, Business, or Enterprise subscription
- GitHub Copilot Coding Agent enabled in your repository settings
- A GitHub repository cloned locally with push access

---

## Why Hand Off?

Local agents are ideal for **exploration and planning** because you can interact in real time, ask follow-up questions, and refine your approach. Cloud agents are ideal for **execution** because they work autonomously, create PRs, and do not consume your local resources.

The handoff workflow combines both strengths:

```
  LOCAL AGENT                          CLOUD AGENT
  +-----------------+                  +------------------+
  | 1. Explore code |                  | 4. Implement     |
  | 2. Ask questions|  -- handoff -->  | 5. Write tests   |
  | 3. Create plan  |   (full context) | 6. Create PR     |
  +-----------------+                  +------------------+
```

---

## Step 1: Start a Local Agent Session

1. Open the Chat view (`Ctrl+Shift+I` / `Cmd+Shift+I`)
2. Ensure the **Session Type** dropdown is set to **"Local"**
3. Begin exploring the task with an open-ended prompt:

```
I need to add error handling and input validation to the task management
API in exercises/worktree_scenario/app.py. First, help me understand the
current code structure and identify all the issues.
```

4. The local agent will:
   - Read the relevant files
   - Analyze the code
   - Present findings interactively

---

## Step 2: Research and Plan Interactively

Use the local agent's interactive capabilities to build a plan. Ask follow-up questions:

```
What validation patterns are commonly used in similar Python APIs?
Should we use custom exception classes or built-in ones?
```

```
Show me the test file. Which tests are currently failing and what do they
expect the fixed code to do?
```

```
Let's create an implementation plan. List each function that needs changes
and what specifically should change.
```

The local agent responds in real time. You can refine the plan until you are satisfied. This interactive research phase is where local agents excel.

### Example Plan Output

By the end of this step, your local agent session should contain a plan like:

```
Implementation Plan:
1. create_task: Add ValueError for empty title and invalid priority
2. get_task: Change from .get() to direct dict access for KeyError
3. list_tasks: Return deep copies of task dicts
4. update_task: Add KeyError for missing tasks; validate allowed fields
5. delete_task: Check existence before deleting; raise KeyError if missing
6. All changes must preserve existing type hints and docstrings
```

---

## Step 3: Delegate to a Cloud Agent

Once your plan is solid, hand off the implementation:

### Method 1: Session Type Dropdown

1. In the Chat view, click the **Session Type** dropdown
2. Change from **"Local"** to **"Cloud"**
3. The full conversation history (your research, the plan, all context) transfers to the cloud agent
4. Add a final instruction:

```
Implement the plan we discussed above. Make all changes to app.py and
ensure all tests in tests/test_app.py pass. Create a PR with a clear
description of what was fixed.
```

### Method 2: `/delegate` Command

Type `/delegate` in the chat input:

```
/delegate Implement the validation plan we discussed. Fix all bugs in
app.py so that every test in test_app.py passes.
```

The `/delegate` command:
- Transfers the full conversation history to the cloud agent
- Starts a cloud agent session on GitHub's infrastructure
- Creates a new session entry visible in the Sessions list

### What Transfers During Handoff

| Context Element | Transferred? |
|----------------|-------------|
| Full conversation history | Yes |
| File contents read during the session | Yes |
| Your plan and instructions | Yes |
| MCP server connections | No (cloud uses its own MCP config) |
| VS Code extension state | No |
| Local environment variables | No (use GitHub secrets instead) |

---

## Step 4: Observe the Conversation History Carry-Over

After the handoff:

1. Open the **Sessions list** in the Chat view
2. Find the new **Cloud** session
3. Click on it to see that the full conversation from the local session is included
4. The cloud agent has all the context from your research phase

You should see:
- Your initial exploration prompt
- The agent's analysis of the code
- Your follow-up questions and the agent's responses
- The final implementation plan
- Your delegation instructions

---

## Step 5: Monitor Cloud Agent Progress

While the cloud agent works:

1. **VS Code Chat view**: The session updates with each agent turn
2. **GitHub**: A draft PR appears in the repository
3. **Notifications**: GitHub sends notifications about PR creation

Track progress indicators:
- Number of agent turns completed
- Files modified so far
- Test results (if the agent runs tests)

You are free to:
- Continue working in your local workspace
- Start additional local or background sessions
- Close VS Code entirely (the cloud agent continues independently)

---

## Step 6: Review the Resulting Pull Request

When the cloud agent finishes:

1. Open the pull request on GitHub (linked from the session in Chat view)
2. Review the PR description -- it should reference the plan from your local session
3. Check the **Files changed** tab:
   - Verify each change matches the plan
   - Look for unexpected modifications
4. Check CI/test results:
   - All tests should pass
   - No new linting errors
5. If changes need refinement, comment on the PR mentioning `@copilot`:

```
@copilot The error message for invalid priority should list the allowed
values. Please update create_task to say:
"priority must be one of: low, medium, high"
```

6. When satisfied, approve and merge the PR

---

## Practice Scenario

Use the files in `exercises/worktree_scenario/` for this exercise:

1. **Start locally**: Open Chat in Local mode and explore `app.py` and `test_app.py`
2. **Research**: Ask the local agent to identify all bugs and create a fix plan
3. **Hand off**: Switch to Cloud mode or use `/delegate`
4. **Monitor**: Watch the cloud agent fix the bugs
5. **Review**: Check the resulting PR

### Success Criteria

- The cloud agent received the full context from your local session
- All 7 failing tests in `test_app.py` now pass
- The PR description references the plan you created locally
- Code style matches the existing codebase

---

## Troubleshooting

| Issue | Cause | Solution |
|-------|-------|----------|
| "Cloud session type not available" | Coding Agent not enabled for repo | Enable it in repository settings on GitHub |
| Handoff loses context | Session timeout | Complete the handoff promptly; do not let the local session expire |
| Cloud agent ignores the plan | Plan was too vague | Be explicit: list specific functions, specific changes, specific tests |
| PR has unrelated changes | Agent explored beyond scope | Add constraints: "Only modify app.py. Do not change test_app.py." |
| `/delegate` command not recognized | Extension version too old | Update the GitHub Copilot extension |

---

## What You Learned

- How to use local agents for interactive research and planning
- How to hand off a session to a cloud agent using the Session Type dropdown or `/delegate`
- That full conversation history transfers during handoff
- How to monitor cloud agent progress from VS Code
- How to review and refine the resulting pull request

---

## Next Exercise

Proceed to [Exercise 6: Parallel Background Tasks](parallel_background_tasks.md) to run multiple background agents simultaneously.
