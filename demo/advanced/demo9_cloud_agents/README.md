# Demo 9: Cloud Agents

## What This Demo Shows

- **Agent types comparison**: Understanding Local, Background, and Cloud agents
- **GitHub Issue assignment to @copilot**: Assigning issues for autonomous resolution
- **Session tracking**: Monitoring cloud agent progress from VS Code
- **Partner agents**: Using alternative AI backends (Claude, Codex) with GitHub Copilot

**Duration**: 15-20 minutes
**Complexity**: Advanced
**Best For**: Teams adopting asynchronous AI-assisted development workflows
**Prerequisites**: GitHub Copilot Business or Enterprise subscription, GitHub repository with write access

---

## Prerequisites

1. **GitHub Copilot Business or Enterprise** subscription (cloud agents require this tier)
2. **VS Code** with GitHub Copilot Chat extension (version 1.102 or later)
3. **GitHub repository** with write access (for issue assignment)
4. **GitHub CLI** (`gh`) installed and authenticated (optional, for command-line workflows)
5. Familiarity with GitHub Issues and pull requests

---

## Quick Setup (2 minutes)

### 1. Navigate to Demo Folder

```bash
cd demo/advanced/demo9_cloud_agents
```

### 2. Review Setup Files

- `setup/sample_issue.md` - Issue template optimized for @copilot
- `setup/project_scaffold/app.py` - Sample application with issues to fix
- `setup/project_scaffold/tests/test_app.py` - Test suite with some failures
- `setup/project_scaffold/requirements.txt` - Project dependencies

### 3. Verify GitHub Access

```bash
# Check GitHub CLI authentication
gh auth status

# Verify repository access
gh repo view
```

---

## Demo Steps

### Step 1: Agent Types Overview (3 minutes)

**Goal**: Establish the landscape of agent types before diving into cloud agents.

Present this comparison to your audience:

| Feature | Local Agent | Background Agent | Cloud Agent |
|---------|-------------|-----------------|-------------|
| **Where it runs** | VS Code (your machine) | VS Code (your machine, background) | GitHub cloud infrastructure |
| **Context** | Current editor/workspace | Workspace files | Full repository |
| **Session lifetime** | While chat is open | Persists across sessions | Persists until task completes |
| **Interaction** | Real-time chat | Async notifications | Async via GitHub |
| **Trigger** | Chat prompt | CLI or chat command | Issue assignment or API |
| **Best for** | Interactive development | Long-running local tasks | Autonomous issue resolution |
| **Cost** | Included in Copilot | Included in Copilot | Copilot Business/Enterprise |

**Key message**: _"Local agents are your pair programmer. Background agents handle long tasks while you keep working. Cloud agents are your autonomous teammates -- they work on issues even when your laptop is closed."_

---

### Step 2: Assign GitHub Issue to @copilot (5 minutes)

**Goal**: Show the end-to-end flow of creating an issue and having Copilot resolve it autonomously.

1. **Open** `setup/sample_issue.md` and review the issue template structure

2. **Create the issue on GitHub** using one of these methods:

   **Method A: Via GitHub CLI**
   ```bash
   gh issue create \
     --title "Add input validation to task management endpoints" \
     --body "$(cat setup/sample_issue.md)" \
     --assignee @copilot
   ```

   **Method B: Via GitHub Web UI**
   - Navigate to your repository on GitHub.com
   - Click **Issues** > **New Issue**
   - Paste the content from `setup/sample_issue.md`
   - In the **Assignees** section, type `@copilot` and select it

3. **Observe the auto-created work plan**:
   - Copilot will comment on the issue with its understanding of the task
   - It creates a work plan outlining the steps it will take
   - A draft pull request may be created automatically

4. **Point out to the audience**:
   - The issue description quality directly affects the agent's output
   - Acceptance criteria help the agent know when it is done
   - File references guide the agent to the right parts of the codebase

---

### Step 3: Session Tracking from VS Code (5 minutes)

**Goal**: Show how to monitor and interact with cloud agent sessions without leaving VS Code.

1. **Open VS Code** and navigate to the Chat view (`Ctrl/Cmd + Shift + I`)

2. **Access cloud sessions**:
   - Look for the **Copilot Sessions** panel or the cloud icon in the chat view
   - Filter to show **Cloud Agent** sessions
   - You should see the session created by the issue assignment in Step 2

3. **Monitor progress**:
   - Click on the active session to see real-time status updates
   - View the files the cloud agent is reading and modifying
   - See the agent's reasoning and decision-making process

4. **Interact with the session**:
   - You can add comments or constraints while the agent is working
   - Example: "Make sure to add docstrings to all new functions"
   - The agent will incorporate your feedback into its work

5. **Review the result**:
   - When the agent completes, it creates a pull request
   - Review the PR directly from VS Code using the GitHub Pull Requests extension
   - Check the changes against the original issue requirements

---

### Step 4: Partner Agents (5 minutes)

**Goal**: Show that GitHub Copilot supports multiple AI model backends for cloud agents.

1. **Explain partner agents**:
   - GitHub Copilot can use different AI models as backend engines
   - Current partner options include Claude (Anthropic) and Codex (OpenAI)
   - Each partner brings different strengths to different tasks

2. **Show configuration** (if available in your subscription):

   - Navigate to GitHub.com > Settings > Copilot
   - Look for the **Agent Model** or **Partner Agent** settings
   - Show the available options and their descriptions

3. **Subscription requirements**:

   | Partner Agent | Subscription Required | Strengths |
   |--------------|----------------------|-----------|
   | GitHub Copilot (default) | Copilot Business/Enterprise | General-purpose, fast |
   | Claude Agent | Copilot Enterprise | Detailed analysis, long-context tasks |
   | OpenAI Codex | Copilot Enterprise | Code generation, multi-file changes |

4. **Demo the selection** (if available):
   - Assign an issue to `@copilot` with a specific model preference
   - Or use the VS Code settings to select a preferred partner agent
   - Show how the same issue might be handled differently by different agents

5. **If partner agents are not available**:
   - Show the configuration page and explain what each option provides
   - Discuss the roadmap for partner agent availability
   - Emphasize that the workflow is the same regardless of the backend model

---

## Key Messages for Your Audience

1. **"Copilot works while you sleep"** -- Cloud agents resolve issues autonomously, even when your laptop is off.
2. **"Issue quality equals output quality"** -- Well-written issues with acceptance criteria produce better results.
3. **"You stay in the loop"** -- Session tracking lets you monitor, guide, and course-correct cloud agents.
4. **"Choose the right tool"** -- Different agent types (local, background, cloud) suit different workflows.
5. **"Enterprise-ready"** -- Cloud agents operate within your repository's permissions and security boundaries.

---

## Expected Outcomes

| Step | What You Should See |
|------|-------------------|
| Step 1 | Clear understanding of when to use each agent type |
| Step 2 | Issue created, @copilot assigned, work plan auto-generated |
| Step 3 | Cloud session visible in VS Code, progress updates streaming |
| Step 4 | Partner agent options shown, strengths and requirements explained |

---

## Troubleshooting

### @copilot assignment not working

- Verify your repository has GitHub Copilot enabled at the organization level
- Check that your subscription tier supports cloud agents (Business or Enterprise)
- Ensure the repository is not archived or read-only
- Try refreshing the issue page after assignment

### Cloud sessions not appearing in VS Code

- Update VS Code and the GitHub Copilot extension to the latest version
- Check that you are signed into the same GitHub account in VS Code
- Try reloading VS Code (`Ctrl/Cmd + Shift + P` > "Developer: Reload Window")
- Verify your network allows connections to GitHub's cloud services

### Partner agents not available

- Partner agents require Copilot Enterprise subscription
- Availability may vary by region and organization settings
- Check GitHub's documentation for the latest partner agent availability
- Use the default Copilot agent as a fallback -- the workflow is identical

### Issue not generating a pull request

- Ensure the issue description includes clear, actionable requirements
- Add file references to help the agent locate relevant code
- Check that the repository has a default branch configured
- Review the agent's work plan comment for any blockers it identified

---

## Success Metrics

After this demo, your audience should understand:

- The differences between local, background, and cloud agents
- How to write issues optimized for @copilot assignment
- How to monitor cloud agent sessions from VS Code
- The partner agent ecosystem and subscription requirements
- When to use cloud agents versus local or background agents

---

## Next Steps

- Create a library of issue templates optimized for @copilot
- Establish team guidelines for when to assign issues to @copilot vs. a human
- Experiment with different partner agents for different task types
- Integrate cloud agent workflows into your team's CI/CD pipeline
- Combine with custom agents (Demo 8) for multi-phase cloud workflows
