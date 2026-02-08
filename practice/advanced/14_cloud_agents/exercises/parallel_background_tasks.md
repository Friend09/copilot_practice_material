# Exercise 6: Parallel Background Tasks

> **Objective**: Run three background agent sessions simultaneously on independent tasks, monitor all sessions, merge the results from each worktree, and resolve any conflicts.

---

## Prerequisites

- VS Code with GitHub Copilot extension (latest version)
- GitHub Copilot Pro, Business, or Enterprise subscription
- Copilot CLI installed (VS Code auto-installs it)
- The `exercises/worktree_scenario/` project files (`app.py` and `tests/test_app.py`)
- Git 2.20+ (required for worktree support)

---

## Overview

Background agents run in isolated git worktrees, which means you can start **multiple sessions at the same time** without them interfering with each other or your main workspace:

```
Main workspace (your active editing)
  |
  +-- Worktree 1: Background Agent Session A (validation task)
  +-- Worktree 2: Background Agent Session B (documentation task)
  +-- Worktree 3: Background Agent Session C (testing task)
```

Each agent works independently, commits to its own branch, and reports results separately.

---

## Step 1: Identify Three Independent Tasks

For the `exercises/worktree_scenario/` project, here are three tasks that can be done in parallel because they touch different aspects of the code:

### Task A: Input Validation

```
Add input validation to create_task in exercises/worktree_scenario/app.py:
- Raise ValueError if title is an empty string
- Raise ValueError if priority is not one of 'low', 'medium', 'high'
- Include descriptive error messages
Only modify the create_task function. Do not touch other functions.
```

### Task B: Docstring and Type Hint Improvements

```
Improve the documentation in exercises/worktree_scenario/app.py:
- Remove the "Bug:" sections from all docstrings (these are development
  notes, not user-facing documentation)
- Add a module-level constant VALID_PRIORITIES = ('low', 'medium', 'high')
  and VALID_STATUSES = ('pending', 'in_progress', 'completed')
- Add Return type annotations to all functions that are missing them
Only modify docstrings, constants, and type annotations. Do not change
function logic.
```

### Task C: Additional Test Cases

```
Add new test cases to exercises/worktree_scenario/tests/test_app.py:
- test_create_task_assigns_sequential_ids: create 3 tasks, verify IDs
  are '1', '2', '3'
- test_create_task_sets_created_at: verify the created_at field is set
- test_list_tasks_empty_store: verify list_tasks returns [] when no
  tasks exist
- test_update_task_sets_updated_at: verify updated_at is added after update
- test_delete_task_removes_from_list: create 2 tasks, delete 1, verify
  list_tasks returns 1
Only add new test functions. Do not modify existing tests.
```

---

## Step 2: Start Three Background Agent Sessions

Start all three sessions within a short time window:

### Session A: Validation

1. Open the Chat view (`Ctrl+Shift+I` / `Cmd+Shift+I`)
2. Set **Session Type** to **Background**
3. Paste the Task A prompt above
4. Press Enter to start

### Session B: Documentation

1. Open a **new chat session** (click the `+` button in the Chat view)
2. Set **Session Type** to **Background**
3. Paste the Task B prompt above
4. Press Enter to start

### Session C: Testing

1. Open another **new chat session**
2. Set **Session Type** to **Background**
3. Paste the Task C prompt above
4. Press Enter to start

All three sessions should now be running simultaneously, each in its own git worktree.

---

## Step 3: Verify Worktree Isolation

Confirm that three separate worktrees exist:

```bash
git worktree list
```

Expected output (paths and hashes will vary):

```
/path/to/your-project                          abc1234 [main]
/path/to/your-project-worktrees/bg-session-001  def5678 [bg-session-001]
/path/to/your-project-worktrees/bg-session-002  ghi9012 [bg-session-002]
/path/to/your-project-worktrees/bg-session-003  jkl3456 [bg-session-003]
```

Each worktree is a full checkout of the repository. The agents can read and modify files without affecting each other or your main workspace.

---

## Step 4: Monitor All Sessions in Chat View

While the agents work:

1. Open the **Sessions list** in the Chat view (sidebar or panel header)
2. You should see three active background sessions
3. Each session shows:
   - **Session name** or task summary
   - **Status**: Running / Completed / Failed
   - **Turn count**: Number of agent actions taken
   - **Duration**: How long the session has been running

### What to Observe

| Observation | What It Tells You |
|-------------|------------------|
| All three running simultaneously | Parallel execution is working |
| Different completion times | Tasks vary in complexity |
| One fails while others succeed | Independent failure isolation |
| Turn counts differ | Agents take different approaches |

### While You Wait

You can continue working in your main workspace. Background agents do not block your editor, terminal, or other Copilot features. Consider:

- Writing code in your main workspace
- Starting a local agent session for a different task
- Reviewing documentation

---

## Step 5: Merge Changes from Each Worktree

As each session completes, merge its changes into your main branch.

### Recommended Merge Order

Merge in this order to minimize conflicts:

1. **Task C (tests)** first -- new test functions are least likely to conflict
2. **Task B (documentation)** second -- docstring changes are isolated
3. **Task A (validation)** last -- logic changes may interact with updated docstrings

### Merging via VS Code

1. Click on a completed session in the Sessions list
2. Review the summary of changes
3. Click **"Apply Changes"** or **"Merge to Workspace"**
4. Repeat for each session

### Merging via Git CLI

```bash
# Check which branches were created
git branch --list 'bg-session-*'

# Merge Task C (tests) first
git merge bg-session-003 --no-ff -m "Add additional test cases for task management API"

# Merge Task B (documentation) second
git merge bg-session-002 --no-ff -m "Improve docstrings and type annotations"

# Merge Task A (validation) last
git merge bg-session-001 --no-ff -m "Add input validation to create_task"
```

---

## Step 6: Resolve Any Conflicts

When merging changes from multiple agents that touched the same file, git may report conflicts.

### Common Conflict Scenarios

| Conflict | Cause | Resolution |
|----------|-------|-----------|
| Both agents modified the same docstring | Task A added validation notes; Task B cleaned docstrings | Keep both changes: updated docstring with validation info |
| Both agents added imports | Task A added `copy`; Task C added `pytest` | Keep both import lines |
| Adjacent line changes | Task A modified a function; Task B changed the docstring above it | Git marks as conflict, but changes are compatible -- keep both |

### Resolving Conflicts in VS Code

1. When a merge conflict occurs, VS Code highlights the conflicting sections
2. Click **"Accept Both Changes"** if both modifications are compatible
3. Click **"Accept Current"** or **"Accept Incoming"** if one should take priority
4. After resolving all conflicts, stage the files and commit:

```bash
git add .
git commit -m "Resolve merge conflicts from parallel background agent tasks"
```

### Verify After Merging

```bash
# Run the full test suite
cd exercises/worktree_scenario
python -m pytest tests/ -v
```

All tests (original passing tests + new tests from Task C) should pass. If Task A's validation was merged, the previously-failing validation tests should now pass too.

---

## Step 7: Clean Up Worktrees

After merging all changes:

```bash
# Remove worktrees
git worktree remove /path/to/your-project-worktrees/bg-session-001
git worktree remove /path/to/your-project-worktrees/bg-session-002
git worktree remove /path/to/your-project-worktrees/bg-session-003

# Prune any stale references
git worktree prune

# Optionally delete the worktree branches
git branch -d bg-session-001 bg-session-002 bg-session-003
```

---

## Reflection Questions

1. Did all three sessions complete successfully? If not, which failed and why?
2. How long did each session take? Was there significant variation?
3. Were there any merge conflicts? How did you resolve them?
4. Could you have accomplished all three tasks faster with a single agent session? Why or why not?
5. What is the maximum number of parallel background sessions you would run before it becomes hard to manage?

---

## Bonus: Scaling Parallel Tasks

For larger projects, consider these strategies:

| Strategy | When to Use |
|----------|------------|
| **2-3 parallel sessions** | Standard workflow; easy to monitor and merge |
| **5-10 parallel sessions** | Large refactors (e.g., updating every module's error handling) |
| **Sequential with dependencies** | Task B depends on Task A's output -- run A first, then B |
| **Mixed local + background** | Use local for complex tasks, background for routine ones |

---

## What You Learned

- How to start multiple background agent sessions simultaneously
- How git worktrees provide isolation between parallel sessions
- How to monitor multiple sessions in the Chat view
- How to merge results from multiple worktrees in the right order
- How to resolve conflicts when agents modify overlapping code
- When parallel background tasks are more effective than sequential work

---

## Congratulations

You have completed all six exercises in Module 14. You now understand how to use local, background, and cloud agents effectively, and when to choose each type for different tasks. Return to the [Module README](../README.md) for key takeaways and next steps.
