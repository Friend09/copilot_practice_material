"""
API Module - REST API endpoints for the task management service.

This module provides HTTP endpoints for creating, reading, updating,
and deleting tasks. It is part of the parallel analysis scenario where
sub-agents analyze each module independently.

Exercise:
    Have a sub-agent review this file specifically for REST API best practices
    while other sub-agents review database.py and auth.py in parallel.
"""

from typing import Optional


# Simulated in-memory storage (would use database in production)
tasks_db = {}
next_id = 1


def create_task(title: str, description: str, assigned_to: Optional[str] = None) -> dict:
    """Create a new task and store it.

    Args:
        title: The task title.
        description: The task description.
        assigned_to: Optional username to assign the task to.

    Returns:
        The created task dictionary with an assigned ID.
    """
    global next_id
    task = {
        "id": next_id,
        "title": title,
        "description": description,
        "assigned_to": assigned_to,
        "status": "open",
        "created_at": "2026-01-01T00:00:00",  # Hardcoded - should use datetime
    }
    tasks_db[next_id] = task
    next_id += 1
    return task


def get_task(task_id: int) -> Optional[dict]:
    """Retrieve a task by its ID.

    Args:
        task_id: The ID of the task to retrieve.

    Returns:
        The task dictionary if found, None otherwise.
    """
    return tasks_db.get(task_id)


def list_tasks(status: Optional[str] = None, assigned_to: Optional[str] = None) -> list:
    """List tasks with optional filtering.

    Args:
        status: Filter by task status (open, in_progress, closed).
        assigned_to: Filter by assigned username.

    Returns:
        A list of task dictionaries matching the filters.
    """
    results = list(tasks_db.values())
    if status:
        results = [t for t in results if t["status"] == status]
    if assigned_to:
        results = [t for t in results if t["assigned_to"] == assigned_to]
    return results


def update_task(task_id: int, updates: dict) -> Optional[dict]:
    """Update a task's fields.

    Note: No validation on which fields can be updated.
    A sub-agent should identify this as a concern.

    Args:
        task_id: The ID of the task to update.
        updates: Dictionary of fields to update.

    Returns:
        The updated task dictionary if found, None otherwise.
    """
    if task_id not in tasks_db:
        return None
    tasks_db[task_id].update(updates)  # Allows updating any field including 'id'
    return tasks_db[task_id]


def delete_task(task_id: int) -> bool:
    """Delete a task by its ID.

    Note: No authorization check - any caller can delete any task.
    A sub-agent should flag this.

    Args:
        task_id: The ID of the task to delete.

    Returns:
        True if the task was deleted, False if not found.
    """
    if task_id in tasks_db:
        del tasks_db[task_id]
        return True
    return False


def search_tasks(query: str) -> list:
    """Search tasks by title or description.

    Warning: Simple string matching - no sanitization.

    Args:
        query: The search string to match against title and description.

    Returns:
        A list of matching task dictionaries.
    """
    results = []
    for task in tasks_db.values():
        if query.lower() in task["title"].lower() or query.lower() in task["description"].lower():
            results.append(task)
    return results
