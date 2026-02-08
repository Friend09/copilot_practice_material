# Exercise 2: Creating GitHub Issues for Cloud Agents

> **Objective**: Learn to write GitHub issues that `@copilot` can execute effectively. Practice structuring issues with clear acceptance criteria so the cloud coding agent produces high-quality pull requests.

---

## Prerequisites

- GitHub repository with Copilot Coding Agent enabled
- Repository admin or write access (to assign issues)
- GitHub Copilot Pro, Business, or Enterprise subscription

---

## Issue Title Best Practices

The issue title is the first thing the coding agent reads. It should be:

| Guideline | Good Example | Poor Example |
|-----------|-------------|-------------|
| Specific and actionable | "Add rate limiting middleware to POST /api/users endpoint" | "Fix the API" |
| Scoped to one task | "Add input validation for email field in signup form" | "Improve the signup flow" |
| Indicates the type of change | "Bug: Login fails when password contains special characters" | "Login is broken" |
| Names the affected component | "Refactor UserService to use dependency injection" | "Clean up some code" |

---

## Description Structure

Structure your issue description with these sections to give the coding agent maximum clarity:

### The Four W's Framework

```markdown
### What
[What needs to change? Be specific about the expected behavior.]

### Where
[Which files, modules, or components are affected?]

### How
[Any constraints on the implementation approach?]

### Acceptance Criteria
[Checklist of conditions that must be true when the task is complete.]
```

---

## Template: Feature Request

Copy this template when creating feature request issues for `@copilot`:

```markdown
## Feature: [Short description]

### What
Add [specific feature] to [specific component/module].

**Expected behavior**: When a user [action], the system should [result].

### Where
- Primary file(s): `src/[path/to/file]`
- Related files: `src/[related/files]`
- Test file(s): `tests/[path/to/test]`

### How
- Use [specific library/pattern] for the implementation
- Follow the existing patterns in `src/[example/file]`
- Do NOT modify [files/APIs that should not change]

### Acceptance Criteria
- [ ] Feature works as described in "Expected behavior"
- [ ] Unit tests added with at least 80% coverage for new code
- [ ] No existing tests are broken
- [ ] Type annotations included (if TypeScript/Python with type hints)
- [ ] Error cases handled (invalid input, network failures, etc.)

### Additional Context
[Screenshots, links to documentation, or examples from other projects]
```

### Example: Feature Request (Filled In)

```markdown
## Feature: Add pagination to GET /api/tasks endpoint

### What
Add cursor-based pagination to the task listing endpoint. Currently, the
endpoint returns all tasks in a single response, which causes performance
issues when the task count exceeds 1,000.

**Expected behavior**: When a client calls `GET /api/tasks?limit=20&cursor=abc123`,
the response includes up to 20 tasks and a `next_cursor` field for fetching
the next page. When no cursor is provided, return the first page.

### Where
- Primary file(s): `src/api/tasks.py`
- Related files: `src/models/task.py`, `src/db/queries.py`
- Test file(s): `tests/api/test_tasks.py`

### How
- Use cursor-based pagination (not offset-based) for stable results
- Cursor should encode the task ID and creation timestamp
- Follow the pagination pattern already used in `src/api/users.py`
- Do NOT change the response format for individual task objects

### Acceptance Criteria
- [ ] `GET /api/tasks` returns paginated results with `limit` and `cursor` params
- [ ] Default limit is 20, maximum limit is 100
- [ ] Response includes `next_cursor` (null when no more results)
- [ ] Existing tests for GET /api/tasks still pass
- [ ] New tests cover: first page, middle page, last page, invalid cursor, limit bounds
- [ ] Performance: endpoint responds in under 200ms for 10,000 tasks
```

---

## Template: Bug Fix

Copy this template when creating bug fix issues for `@copilot`:

```markdown
## Bug: [Short description of the bug]

### Current Behavior
[What happens now? Include error messages, stack traces, or screenshots.]

### Expected Behavior
[What should happen instead?]

### Steps to Reproduce
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Where
- Likely cause: `src/[path/to/file]`, line [number] (if known)
- Related files: `src/[related/files]`
- Test file(s): `tests/[path/to/test]`

### Acceptance Criteria
- [ ] Bug no longer occurs when following the reproduction steps
- [ ] Root cause is addressed (not just the symptom)
- [ ] Regression test added to prevent recurrence
- [ ] No existing tests are broken

### Environment
- OS: [e.g., Ubuntu 22.04]
- Runtime: [e.g., Python 3.12, Node 20]
- Version: [e.g., commit hash or release version]
```

### Example: Bug Fix (Filled In)

```markdown
## Bug: delete_task returns 200 even when task does not exist

### Current Behavior
Calling `DELETE /api/tasks/nonexistent-id` returns HTTP 200 with
`{"status": "deleted"}` even though no task was actually deleted.

### Expected Behavior
Should return HTTP 404 with `{"error": "Task not found"}` when the
task ID does not exist.

### Steps to Reproduce
1. Start the application with `python app.py`
2. Call `DELETE /api/tasks/999` (an ID that does not exist)
3. Observe the 200 response instead of 404

### Where
- Likely cause: `exercises/worktree_scenario/app.py`, `delete_task()` function
- Test file(s): `exercises/worktree_scenario/tests/test_app.py`

### Acceptance Criteria
- [ ] `DELETE /api/tasks/<id>` returns 404 when task does not exist
- [ ] `DELETE /api/tasks/<id>` still returns 200 when task exists and is deleted
- [ ] Regression test added for the 404 case
- [ ] All existing tests pass
```

---

## How to Assign and Monitor

### Assigning `@copilot` to an Issue

1. Create the issue using one of the templates above
2. In the **Assignees** section (right sidebar), click **"Assign"**
3. Type `copilot` and select **@copilot** from the dropdown
4. Save the issue

Copilot begins working immediately. You will see:
- A comment on the issue indicating work has started
- A draft pull request linked to the issue within minutes
- Status updates as the agent progresses

### Monitoring Progress

- **GitHub Issues**: Watch for comments from `@copilot` on the issue
- **GitHub Pull Requests**: The linked draft PR shows commits as the agent works
- **VS Code**: Open the Chat view > Sessions list > filter by "Cloud" to see status
- **Email/Notifications**: GitHub sends notifications for PR creation and status changes

### Timeline Expectations

| Task Complexity | Typical Duration |
|----------------|-----------------|
| Small bug fix (single file) | 2-5 minutes |
| Feature addition (2-3 files) | 5-15 minutes |
| Multi-file refactor | 10-30 minutes |
| Complex feature with tests | 15-45 minutes |

---

## How to Provide Feedback via `@copilot` Mentions

After the agent creates a pull request, you can guide it with comments:

### On the PR Conversation Tab

```markdown
@copilot The pagination cursor should be base64-encoded, not plain text.
Please update the implementation.
```

### On Specific Lines (Code Review Comments)

1. Open the PR's **Files changed** tab
2. Click the `+` button next to a specific line
3. Write your feedback and mention `@copilot`:

```markdown
@copilot This query is missing an index hint. Add `.hint('idx_tasks_created_at')`
to the query on line 45.
```

### Requesting Additional Changes

```markdown
@copilot Please also:
1. Add a `previous_cursor` field for backward pagination
2. Add an integration test that tests pagination with 100 records
```

The agent reads your comments and pushes additional commits to the same PR.

---

## Practice Task

1. Open the repository containing `exercises/worktree_scenario/app.py`
2. Create a new GitHub issue using the **Bug Fix** template for one of the intentional bugs in `app.py`
3. Assign `@copilot` to the issue
4. Monitor the resulting pull request
5. Leave a review comment mentioning `@copilot` to request an improvement
6. Observe how the agent responds to your feedback

---

## What You Learned

- How to structure GitHub issues for optimal cloud agent performance
- Templates for feature requests and bug fixes
- The importance of acceptance criteria for autonomous agents
- How to monitor cloud agent progress
- How to provide iterative feedback via `@copilot` mentions on PRs

---

## Next Exercise

Proceed to [Exercise 3: Background Agent Worktree Task](worktree_scenario/) to work with the Python application that background agents can fix.
