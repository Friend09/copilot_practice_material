## Add Input Validation to Task Management Endpoints

### Description

The task management application in `setup/project_scaffold/app.py` currently
accepts any input without validation. This creates potential issues with data
integrity, unexpected errors, and poor user experience. All public functions
need input validation with clear, descriptive error messages.

### Current Behavior

- `create_task` accepts empty strings, None values, and excessively long inputs
- `update_task` does not verify that the task ID exists before attempting updates
- `update_task` accepts arbitrary status values instead of a defined set
- `delete_task` silently succeeds even when given a non-existent task ID
- No input length limits are enforced anywhere

### Expected Behavior

- All functions validate their inputs before processing
- Invalid inputs raise `ValueError` with a descriptive message
- Task IDs are verified to exist before update and delete operations
- Status values are restricted to: `"pending"`, `"in_progress"`, `"completed"`
- Title length is capped at 200 characters
- Description length is capped at 2000 characters

### Acceptance Criteria

- [ ] `create_task` validates `title` is a non-empty string (max 200 chars)
- [ ] `create_task` validates `description` is a string (max 2000 chars)
- [ ] `update_task` raises `ValueError` for non-existent task IDs
- [ ] `update_task` validates `status` is one of the allowed values
- [ ] `delete_task` raises `ValueError` for non-existent task IDs
- [ ] All validation errors include descriptive messages
- [ ] All functions have complete docstrings
- [ ] Existing passing tests continue to pass
- [ ] New tests cover all validation scenarios

### Files to Modify

- `setup/project_scaffold/app.py` -- Add validation logic to all public functions
- `setup/project_scaffold/tests/test_app.py` -- Add tests for validation behavior

### Constraints

- Do not add external dependencies (use only Python standard library)
- Maintain existing function signatures for backward compatibility
- Follow the existing code style and naming conventions
- Add type hints to all function parameters and return values
