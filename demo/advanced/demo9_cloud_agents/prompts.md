# Demo 9: Cloud Agents - Prompts and Templates

Copy-paste these prompts and issue templates during the live demo. Each section corresponds to a step in the README.

---

## Step 2: GitHub Issue Templates for @copilot

### Template A: Feature Request Issue

Use this template when creating a feature request issue to assign to `@copilot`:

```markdown
## Description

Add input validation to all task management endpoints in `app.py`. Currently,
the application accepts any input without checking for required fields, valid
data types, or reasonable value ranges.

## Acceptance Criteria

- [ ] `create_task` validates that `title` is a non-empty string (max 200 characters)
- [ ] `create_task` validates that `description` is a string (max 2000 characters)
- [ ] `update_task` validates that the task ID exists before updating
- [ ] `update_task` validates that `status` is one of: "pending", "in_progress", "completed"
- [ ] All validation errors return descriptive error messages
- [ ] Add docstrings to all new and modified functions
- [ ] Existing tests continue to pass
- [ ] New tests added for validation logic

## Files to Modify

- `setup/project_scaffold/app.py` - Add validation logic
- `setup/project_scaffold/tests/test_app.py` - Add validation tests

## Constraints

- Do not add external dependencies for validation
- Keep the existing function signatures compatible
- Follow the existing code style and patterns
```

### Template B: Bug Fix Issue

Use this template when creating a bug fix issue to assign to `@copilot`:

```markdown
## Bug Description

The `delete_task` function in `app.py` does not verify that the task exists
before attempting deletion. It silently succeeds even when given an invalid
task ID, and the corresponding test `test_delete_task` is currently failing.

## Steps to Reproduce

1. Call `delete_task` with a non-existent task ID (e.g., `999`)
2. Observe that no error is raised
3. Run `pytest tests/test_app.py::test_delete_task` to see the failing test

## Expected Behavior

- `delete_task` should raise a `ValueError` when the task ID does not exist
- The function should return a confirmation message on successful deletion
- The `test_delete_task` test should pass

## Files to Modify

- `setup/project_scaffold/app.py` - Fix `delete_task` function
- `setup/project_scaffold/tests/test_app.py` - Fix or update test

## Constraints

- Do not change the function signature
- Add a docstring if one is missing
- Ensure all other tests continue to pass
```

---

## Step 2: Creating Issues via CLI

### Create feature request issue and assign to @copilot

```bash
gh issue create \
  --title "Add input validation to task management endpoints" \
  --body "$(cat setup/sample_issue.md)" \
  --assignee @copilot \
  --label "enhancement"
```

### Create bug fix issue and assign to @copilot

```bash
gh issue create \
  --title "Fix delete_task not validating task existence" \
  --body "The delete_task function silently succeeds for non-existent IDs. See test_delete_task for the expected behavior." \
  --assignee @copilot \
  --label "bug"
```

---

## Step 3: Session Tracking Prompts

### Monitor cloud agent session from VS Code chat

```
Show me the status of my active Copilot cloud sessions
```

### Add guidance to a running cloud agent

```
For the current task, make sure to add docstrings to all Python functions
and include type hints for all parameters and return values.
```

---

## Step 4: Partner Agent Prompts

### Using background agent via CLI (Copilot CLI integration)

```bash
gh copilot agent run "Review setup/project_scaffold/app.py for bugs and create a fix"
```

### Delegate a task to a cloud agent from VS Code

```
/delegate Review the project_scaffold application, fix all failing tests,
and add input validation to all public functions.
```

---

## Bonus Prompts

### Bonus 1: Multi-issue workflow

Create multiple related issues and assign them all to `@copilot`:

```bash
# Issue 1: Validation
gh issue create \
  --title "Add input validation to app.py" \
  --body "Add validation for all input parameters in create_task, update_task, and delete_task." \
  --assignee @copilot

# Issue 2: Error handling
gh issue create \
  --title "Improve error handling in app.py" \
  --body "Replace generic exceptions with specific error types. Add proper error messages." \
  --assignee @copilot

# Issue 3: Testing
gh issue create \
  --title "Increase test coverage for app.py" \
  --body "Add tests for edge cases: empty inputs, very long strings, special characters, concurrent access." \
  --assignee @copilot
```

### Bonus 2: Issue template with architecture context

```markdown
## Description

Refactor the task storage from an in-memory dictionary to a SQLite database.

## Architecture Context

The current application uses a simple dictionary (`_tasks`) for storage.
This should be migrated to SQLite while maintaining the same public API.

## Implementation Notes

- Use Python's built-in `sqlite3` module (no external dependencies)
- Create a `TaskDatabase` class to encapsulate database operations
- Maintain backward compatibility with existing function signatures
- Add connection pooling or context manager for proper resource cleanup

## Acceptance Criteria

- [ ] All existing tests pass without modification
- [ ] Data persists across application restarts
- [ ] Thread-safe database access
- [ ] Proper connection cleanup on application shutdown
- [ ] Docstrings on all new functions and classes
```
