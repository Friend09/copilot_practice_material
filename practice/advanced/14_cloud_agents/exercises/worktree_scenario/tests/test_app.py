"""
Test suite for the Task Management API (app.py).

This module contains pytest tests for all CRUD operations in app.py.
Several tests are designed to FAIL against the current (buggy) implementation,
giving a background agent clear signals about what needs to be fixed.

Tests that should PASS with the current code:
    - test_create_task_basic
    - test_list_tasks_returns_all
    - test_update_task_existing

Tests that should FAIL with the current code (bugs to fix):
    - test_create_task_empty_title_raises
    - test_create_task_invalid_priority_raises
    - test_get_task_missing_raises
    - test_update_task_missing_raises
    - test_update_task_invalid_field_raises
    - test_delete_task_missing_raises
    - test_list_tasks_returns_copies
"""

import sys
import os
import pytest

# ---------------------------------------------------------------------------
# Ensure the parent directory is on sys.path so we can import app
# ---------------------------------------------------------------------------
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app import create_task, get_task, list_tasks, update_task, delete_task, reset_store


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture(autouse=True)
def clean_store():
    """Reset the task store before every test to ensure isolation."""
    reset_store()
    yield
    reset_store()


# ---------------------------------------------------------------------------
# create_task tests
# ---------------------------------------------------------------------------

class TestCreateTask:
    """Tests for the create_task function."""

    def test_create_task_basic(self):
        """Creating a task with valid inputs should return a dict with all expected fields."""
        task = create_task("Buy groceries", description="Milk, eggs, bread", priority="high")

        assert task["title"] == "Buy groceries"
        assert task["description"] == "Milk, eggs, bread"
        assert task["priority"] == "high"
        assert task["status"] == "pending"
        assert "id" in task
        assert "created_at" in task

    def test_create_task_default_values(self):
        """Creating a task with only a title should use default description and priority."""
        task = create_task("Simple task")

        assert task["title"] == "Simple task"
        assert task["description"] == ""
        assert task["priority"] == "medium"

    def test_create_task_empty_title_raises(self):
        """Creating a task with an empty title should raise ValueError.

        BUG: The current implementation does NOT validate the title,
        so this test FAILS. A background agent should add validation
        to create_task.
        """
        with pytest.raises(ValueError, match="title"):
            create_task("")

    def test_create_task_invalid_priority_raises(self):
        """Creating a task with an invalid priority should raise ValueError.

        BUG: The current implementation accepts any string as priority,
        so this test FAILS. A background agent should add validation
        to create_task.
        """
        with pytest.raises(ValueError, match="priority"):
            create_task("Valid title", priority="ultra-critical")


# ---------------------------------------------------------------------------
# get_task tests
# ---------------------------------------------------------------------------

class TestGetTask:
    """Tests for the get_task function."""

    def test_get_task_existing(self):
        """Getting an existing task should return the correct task dict."""
        created = create_task("Test task")
        retrieved = get_task(created["id"])

        assert retrieved is not None
        assert retrieved["id"] == created["id"]
        assert retrieved["title"] == "Test task"

    def test_get_task_missing_raises(self):
        """Getting a nonexistent task should raise KeyError.

        BUG: The current implementation returns None instead of raising
        KeyError, so this test FAILS. A background agent should fix
        get_task to raise KeyError.
        """
        with pytest.raises(KeyError):
            get_task("nonexistent-id")


# ---------------------------------------------------------------------------
# list_tasks tests
# ---------------------------------------------------------------------------

class TestListTasks:
    """Tests for the list_tasks function."""

    def test_list_tasks_returns_all(self):
        """Listing tasks without a filter should return all tasks."""
        create_task("Task 1")
        create_task("Task 2")
        create_task("Task 3")

        tasks = list_tasks()
        assert len(tasks) == 3

    def test_list_tasks_filter_by_status(self):
        """Listing tasks with a status filter should return only matching tasks."""
        create_task("Task 1")
        task2 = create_task("Task 2")
        update_task(task2["id"], status="completed")

        pending = list_tasks(status_filter="pending")
        completed = list_tasks(status_filter="completed")

        assert len(pending) == 1
        assert len(completed) == 1
        assert pending[0]["title"] == "Task 1"
        assert completed[0]["title"] == "Task 2"

    def test_list_tasks_returns_copies(self):
        """Modifying returned task dicts should NOT affect the internal store.

        BUG: The current implementation returns direct references to
        internal dicts, so mutations leak into the store. This test
        FAILS. A background agent should return deep copies.
        """
        create_task("Original title")

        tasks = list_tasks()
        tasks[0]["title"] = "Mutated title"

        # The internal store should be unchanged
        fresh_tasks = list_tasks()
        assert fresh_tasks[0]["title"] == "Original title"


# ---------------------------------------------------------------------------
# update_task tests
# ---------------------------------------------------------------------------

class TestUpdateTask:
    """Tests for the update_task function."""

    def test_update_task_existing(self):
        """Updating an existing task should modify the specified fields."""
        task = create_task("Old title")
        updated = update_task(task["id"], title="New title", priority="high")

        assert updated["title"] == "New title"
        assert updated["priority"] == "high"
        assert "updated_at" in updated

    def test_update_task_missing_raises(self):
        """Updating a nonexistent task should raise KeyError.

        BUG: The current implementation returns an empty dict instead of
        raising KeyError, so this test FAILS. A background agent should
        fix update_task to raise KeyError.
        """
        with pytest.raises(KeyError):
            update_task("nonexistent-id", title="Doesn't matter")

    def test_update_task_invalid_field_raises(self):
        """Updating with an invalid field name should raise ValueError.

        BUG: The current implementation accepts any keyword argument
        and blindly sets it on the task dict, so this test FAILS.
        A background agent should add field validation.
        """
        task = create_task("Test task")
        with pytest.raises(ValueError, match="field"):
            update_task(task["id"], nonexistent_field="bad value")


# ---------------------------------------------------------------------------
# delete_task tests
# ---------------------------------------------------------------------------

class TestDeleteTask:
    """Tests for the delete_task function."""

    def test_delete_task_existing(self):
        """Deleting an existing task should remove it from the store."""
        task = create_task("To be deleted")
        result = delete_task(task["id"])

        assert result is True
        assert list_tasks() == []

    def test_delete_task_missing_raises(self):
        """Deleting a nonexistent task should raise KeyError.

        BUG: The current implementation returns True even when no task
        was deleted, so this test FAILS. A background agent should fix
        delete_task to raise KeyError.
        """
        with pytest.raises(KeyError):
            delete_task("nonexistent-id")
