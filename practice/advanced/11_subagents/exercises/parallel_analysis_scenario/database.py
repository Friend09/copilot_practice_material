"""
Database Module - Data access layer for the task management service.

This module handles all database operations including connection management,
queries, and migrations. It contains several performance and design issues
that a sub-agent should identify.

Exercise:
    Have a sub-agent review this file for database best practices and
    query optimization while other sub-agents review api.py and auth.py.
"""

import sqlite3
from typing import Optional


DB_PATH = "tasks.db"


def get_connection() -> sqlite3.Connection:
    """Get a new database connection.

    Note: Creates a new connection every time - no connection pooling.
    A sub-agent should identify this as a scalability issue.

    Returns:
        A new SQLite connection object.
    """
    return sqlite3.connect(DB_PATH)


def initialize_database() -> None:
    """Create the database tables if they don't exist.

    Creates users and tasks tables with basic schema.
    No indexes defined - sub-agent should flag this for
    frequently queried columns.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            assigned_to TEXT,
            status TEXT DEFAULT 'open',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def get_user_tasks(username: str) -> list:
    """Get all tasks assigned to a user.

    Warning: Uses string formatting for SQL - injection risk.

    Args:
        username: The username to look up tasks for.

    Returns:
        A list of task tuples from the database.
    """
    conn = get_connection()
    cursor = conn.cursor()
    # SQL injection vulnerability
    query = f"SELECT * FROM tasks WHERE assigned_to = '{username}'"
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results


def get_tasks_by_status(status: str) -> list:
    """Get all tasks with a given status.

    Args:
        status: The status to filter by.

    Returns:
        A list of task tuples matching the status.
    """
    conn = get_connection()
    cursor = conn.cursor()
    # No index on status column - slow for large datasets
    cursor.execute("SELECT * FROM tasks WHERE status = ?", (status,))
    results = cursor.fetchall()
    conn.close()
    return results


def get_overdue_tasks() -> list:
    """Get all tasks that are overdue.

    Note: Fetches ALL tasks and filters in Python instead of SQL.
    A sub-agent should recommend moving this logic to the query.

    Returns:
        A list of all open task tuples (filtering should be in SQL).
    """
    conn = get_connection()
    cursor = conn.cursor()
    # N+1 problem: fetches everything, filters in Python
    cursor.execute("SELECT * FROM tasks")
    all_tasks = cursor.fetchall()
    conn.close()

    # This filtering should happen in SQL
    overdue = [task for task in all_tasks if task[5] == "open"]
    return overdue


def update_task_status(task_id: int, new_status: str) -> bool:
    """Update a task's status.

    Note: No validation on status values. No updated_at timestamp update.

    Args:
        task_id: The ID of the task to update.
        new_status: The new status value.

    Returns:
        True if a row was updated, False otherwise.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tasks SET status = ? WHERE id = ?",
        (new_status, task_id),
    )
    updated = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return updated


def bulk_insert_tasks(tasks: list) -> int:
    """Insert multiple tasks at once.

    Note: Uses a loop instead of executemany - slow for large batches.

    Args:
        tasks: A list of task dictionaries to insert.

    Returns:
        The number of tasks successfully inserted.
    """
    conn = get_connection()
    cursor = conn.cursor()
    count = 0
    for task in tasks:
        try:
            cursor.execute(
                "INSERT INTO tasks (title, description, assigned_to, status) VALUES (?, ?, ?, ?)",
                (task["title"], task.get("description", ""), task.get("assigned_to"), "open"),
            )
            count += 1
        except sqlite3.Error:
            continue  # Silently swallows errors
    conn.commit()
    conn.close()
    return count
