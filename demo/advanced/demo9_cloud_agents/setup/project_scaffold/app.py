"""
Task management application module.

Provides functions for creating, reading, updating, and deleting tasks.
Tasks are stored in an in-memory dictionary for simplicity. This module
contains several intentional issues for demonstration with GitHub Copilot
cloud agents.

WARNING: This code contains intentional flaws for educational use only.
Do NOT use in production.
"""

from datetime import datetime
from typing import Optional


# In-memory task storage
_tasks: dict = {}
_next_id: int = 1


def create_task(title: str, description: str = "") -> dict:
    """Create a new task and store it in memory.

    Intentional issues:
    - No validation on title (could be empty or None).
    - No length limits on title or description.
    - No duplicate title checking.

    Args:
        title: The title of the task.
        description: An optional description of the task.

    Returns:
        A dictionary representing the newly created task.
    """
    global _next_id

    task = {
        "id": _next_id,
        "title": title,
        "description": description,
        "status": "pending",
        "created_at": datetime.now().isoformat(),
        "updated_at": datetime.now().isoformat(),
    }

    _tasks[_next_id] = task
    _next_id += 1

    return task


def get_task(task_id: int) -> Optional[dict]:
    """Retrieve a single task by its ID.

    Args:
        task_id: The unique identifier of the task to retrieve.

    Returns:
        The task dictionary if found, or None if the task does not exist.
    """
    return _tasks.get(task_id)


def list_tasks(status: Optional[str] = None) -> list:
    """List all tasks, optionally filtered by status.

    Intentional issue: Does not validate the status parameter against
    allowed values, so filtering by a misspelled status silently returns
    an empty list.

    Args:
        status: Optional status string to filter tasks. If None, returns
                all tasks.

    Returns:
        A list of task dictionaries matching the filter criteria.
    """
    if status is None:
        return list(_tasks.values())

    return [task for task in _tasks.values() if task["status"] == status]


def update_task(task_id: int, title: Optional[str] = None,
                description: Optional[str] = None,
                status: Optional[str] = None) -> Optional[dict]:
    """Update an existing task's fields.

    Intentional issues:
    - Does not validate that task_id exists (returns None silently).
    - Does not validate status against allowed values.
    - Does not validate title or description length.

    Args:
        task_id: The unique identifier of the task to update.
        title: New title for the task, or None to keep current.
        description: New description, or None to keep current.
        status: New status, or None to keep current.

    Returns:
        The updated task dictionary, or None if the task was not found.
    """
    task = _tasks.get(task_id)

    if task is None:
        return None

    if title is not None:
        task["title"] = title

    if description is not None:
        task["description"] = description

    if status is not None:
        # Intentional issue: accepts any string as status
        task["status"] = status

    task["updated_at"] = datetime.now().isoformat()

    return task


def delete_task(task_id: int) -> bool:
    """Delete a task by its ID.

    Intentional issue: Does not verify that the task exists before
    attempting deletion. Returns True even if the task did not exist,
    which masks errors.

    Args:
        task_id: The unique identifier of the task to delete.

    Returns:
        True regardless of whether the task existed.
    """
    # Intentional issue: pop with default means no error on missing key
    _tasks.pop(task_id, None)
    return True


def reset_tasks() -> None:
    """Reset the task store to its initial empty state.

    Clears all tasks and resets the ID counter. Useful for testing.
    """
    global _next_id
    _tasks.clear()
    _next_id = 1
