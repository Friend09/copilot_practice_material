"""
Task Management API -- A simple in-memory task management application.

This module provides functions for creating, reading, updating, and deleting
tasks. It is designed as a practice scenario for background agents: the code
contains several intentional bugs that a background agent should identify and
fix by running the accompanying test suite.

Intentional issues:
    - create_task does not validate required fields
    - get_task returns None instead of raising an error for missing tasks
    - update_task silently ignores updates to nonexistent tasks
    - delete_task does not check whether the task exists before deleting
    - list_tasks returns a direct reference to the internal store (mutation risk)
"""

from datetime import datetime
from typing import Optional


# ---------------------------------------------------------------------------
# In-memory task store
# ---------------------------------------------------------------------------

_tasks: dict[str, dict] = {}
_next_id: int = 1


def reset_store() -> None:
    """Reset the task store to its initial empty state.

    This function is intended for use in tests to ensure a clean state
    between test cases.
    """
    global _tasks, _next_id
    _tasks = {}
    _next_id = 1


# ---------------------------------------------------------------------------
# CRUD operations
# ---------------------------------------------------------------------------

def create_task(title: str, description: str = "", priority: str = "medium") -> dict:
    """Create a new task and add it to the store.

    Args:
        title: The title of the task. Must be a non-empty string.
        description: An optional longer description of the task.
        priority: The priority level. Must be one of 'low', 'medium', or 'high'.

    Returns:
        A dictionary representing the newly created task, including its
        generated ``id``, ``created_at`` timestamp, and ``status`` field
        set to ``'pending'``.

    Raises:
        ValueError: If *title* is empty or *priority* is not a valid level.

    Bug:
        This function does NOT validate that *title* is non-empty or that
        *priority* is one of the allowed values. A background agent should
        add validation logic.
    """
    global _next_id

    # BUG: No validation -- empty title and invalid priority are accepted
    task = {
        "id": str(_next_id),
        "title": title,
        "description": description,
        "priority": priority,
        "status": "pending",
        "created_at": datetime.now().isoformat(),
    }
    _tasks[task["id"]] = task
    _next_id += 1
    return task


def get_task(task_id: str) -> Optional[dict]:
    """Retrieve a single task by its ID.

    Args:
        task_id: The unique identifier of the task to retrieve.

    Returns:
        A dictionary representing the task.

    Raises:
        KeyError: If no task with the given *task_id* exists.

    Bug:
        This function returns ``None`` for missing tasks instead of raising
        a ``KeyError``. Callers that rely on a guaranteed return value will
        encounter unexpected ``None`` values.
    """
    # BUG: Returns None instead of raising KeyError for missing tasks
    return _tasks.get(task_id)


def list_tasks(status_filter: Optional[str] = None) -> list[dict]:
    """Return a list of all tasks, optionally filtered by status.

    Args:
        status_filter: If provided, only tasks with this status are returned.
            Valid values are ``'pending'``, ``'in_progress'``, and
            ``'completed'``.

    Returns:
        A list of task dictionaries matching the filter criteria. If no
        filter is provided, all tasks are returned.

    Bug:
        This function returns a direct reference to the internal task
        dictionaries. Callers that modify the returned list or its
        elements will corrupt the internal store.
    """
    # BUG: Returns direct references to internal dicts (mutation risk)
    if status_filter:
        return [t for t in _tasks.values() if t["status"] == status_filter]
    return list(_tasks.values())


def update_task(task_id: str, **kwargs) -> dict:
    """Update fields of an existing task.

    Args:
        task_id: The unique identifier of the task to update.
        **kwargs: Keyword arguments for the fields to update. Supported
            fields are ``title``, ``description``, ``priority``, and
            ``status``.

    Returns:
        A dictionary representing the updated task.

    Raises:
        KeyError: If no task with the given *task_id* exists.
        ValueError: If an unsupported field name is provided or if
            *priority* / *status* values are invalid.

    Bug:
        This function silently returns an empty dict when the task does
        not exist, instead of raising a ``KeyError``. It also does not
        validate field names or values.
    """
    # BUG: silently returns empty dict for nonexistent tasks
    task = _tasks.get(task_id)
    if not task:
        return {}

    # BUG: No validation of allowed fields or values
    for key, value in kwargs.items():
        task[key] = value

    task["updated_at"] = datetime.now().isoformat()
    return task


def delete_task(task_id: str) -> bool:
    """Delete a task from the store.

    Args:
        task_id: The unique identifier of the task to delete.

    Returns:
        ``True`` if the task was successfully deleted.

    Raises:
        KeyError: If no task with the given *task_id* exists.

    Bug:
        This function uses ``dict.pop`` with a default value, so it
        returns ``True`` even when no task was deleted. It should raise
        a ``KeyError`` for missing tasks.
    """
    # BUG: Returns True even when the task does not exist
    _tasks.pop(task_id, None)
    return True
