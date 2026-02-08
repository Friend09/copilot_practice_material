# Exercise 1: Background Agent Setup and First Task

> **Objective**: Set up a background agent session, observe how git worktrees provide isolation, monitor progress, and merge results back into your workspace.

---

## Prerequisites

- VS Code with GitHub Copilot extension (latest version)
- GitHub Copilot Pro, Business, or Enterprise subscription
- A GitHub repository cloned locally
- Git 2.20+ (required for worktree support)

---

## Step 1: Verify Copilot CLI Is Installed

VS Code automatically installs the Copilot CLI when you have the GitHub Copilot extension. Verify it is available:

1. Open VS Code
2. Open the Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
3. Search for **"Copilot: Show CLI Version"**
4. Confirm the version is displayed in the output

If the CLI is not installed, try:
- Restarting VS Code
- Updating the GitHub Copilot extension to the latest version
- Checking the Output panel (select "GitHub Copilot" from the dropdown) for error messages

---

## Step 2: Open Chat View and Select Background Session Type

1. Open the Chat view using one of these methods:
   - Keyboard shortcut: `Ctrl+Shift+I` / `Cmd+Shift+I`
   - Click the Copilot icon in the Activity Bar
   - Command Palette: **"Copilot: Open Chat"**

2. At the top of the Chat panel, locate the **Session Type** dropdown
   - It defaults to "Local"
   - Click the dropdown and select **"Background"**

3. You should see a visual indicator confirming you are in Background mode (the chat header or input area changes to reflect the session type)

---

## Step 3: Enter a Task Description

Type a clear, well-defined task in the chat input. Background agents work best with specific instructions:

**Good task descriptions:**
```
Fix the type errors in src/utils/validation.ts and ensure all
existing tests pass.
```

```
Add JSDoc comments to all exported functions in the api/ directory.
```

**Poor task descriptions (too vague for background agents):**
```
Make the code better.
```

```
I think something is wrong with the app, can you help?
```

For this exercise, try:
```
Review the files in the exercises/worktree_scenario/ directory.
Fix any bugs in app.py so that all tests in tests/test_app.py pass.
```

Press Enter to start the background agent session.

---

## Step 4: Observe Worktree Creation

Once the session starts:

1. Open the **Source Control** view (`Ctrl+Shift+G` / `Cmd+Shift+G`)
2. Look for a new section labeled with the worktree path (something like `your-project-worktrees/bg-session-<id>`)
3. The background agent created a separate checkout of your repository in this folder
4. Your main workspace files remain completely untouched

To verify isolation from the terminal:
```bash
# List active worktrees for your repository
git worktree list
```

You should see your main workspace and the background agent's worktree:
```
/path/to/your-project           abc1234 [main]
/path/to/your-project-worktrees/bg-session-xyz  def5678 [bg-session-xyz]
```

---

## Step 5: Monitor Progress in Chat View

While the background agent works:

1. Return to the **Chat view**
2. In the **Sessions list** (sidebar or dropdown), find your background session
3. The session shows:
   - **Status**: Running, Completed, or Failed
   - **Turn count**: How many agent turns have been executed
   - **Latest action**: What the agent is currently doing (reading files, editing, running tests)
4. You can continue working in your main workspace while the agent runs
5. Optionally, start a new local or background session for a different task

---

## Step 6: Review Changes and Merge

When the background agent completes:

1. The session status changes to **Completed**
2. Click on the session to see a summary of all changes
3. Open the **Source Control** view to see the diff between the worktree and your main branch
4. Review each changed file:
   - Click on a file to see the diff
   - Verify the changes are correct
5. To merge changes into your main workspace:
   - Click **"Apply Changes"** or **"Merge to Workspace"** in the session summary
   - Alternatively, use git commands:
     ```bash
     # From your main workspace
     git merge bg-session-xyz
     ```
6. After merging, the worktree can be cleaned up:
   ```bash
   git worktree remove /path/to/worktree
   ```

---

## Step 7: Troubleshooting Common Issues

### Background agent session does not start

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| "CLI not found" error | Copilot CLI not installed | Restart VS Code; update the Copilot extension |
| Session hangs on "Starting..." | Network connectivity issue | Check internet connection; check the Output panel for errors |
| "Repository not found" | Git repo not initialized | Run `git init` or clone a repository |

### Worktree creation fails

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| "Cannot create worktree" | Uncommitted changes on target branch | Commit or stash your changes first |
| "Lock file exists" | Previous session did not clean up | Run `git worktree prune` to remove stale entries |
| Permission errors | File system permissions | Check write permissions on parent directory |

### Agent produces incorrect results

| Symptom | Possible Cause | Solution |
|---------|---------------|----------|
| Agent says "task complete" but tests fail | Task description was too vague | Provide more specific instructions with acceptance criteria |
| Agent modifies wrong files | Ambiguous file references | Specify exact file paths in the task description |
| Agent loops without progress | Task is too complex for background mode | Switch to a local agent session for interactive guidance |

### Cleaning up after issues

```bash
# List all worktrees
git worktree list

# Remove a specific worktree
git worktree remove /path/to/worktree --force

# Prune stale worktree references
git worktree prune

# Delete orphaned worktree branches
git branch -d bg-session-xyz
```

---

## What You Learned

- How to start a background agent session from the Chat view
- How git worktrees provide isolation from your main workspace
- How to monitor background agent progress
- How to review and merge changes back to your workspace
- Common troubleshooting steps for background agent issues

---

## Next Exercise

Proceed to [Exercise 2: Creating GitHub Issues for Cloud Agents](cloud_agent_issue_template.md) to learn how to write issues that `@copilot` can execute autonomously in the cloud.
