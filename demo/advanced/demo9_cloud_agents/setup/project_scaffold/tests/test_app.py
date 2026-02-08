"""
Test suite for the task management application.

Contains unit tests for task CRUD operations. Some tests are intentionally
designed to fail in order to demonstrate cloud agent capabilities for
identifying and fixing issues.

WARNING: Some tests are intentionally failing for educational purposes.
"""

import pytest

from app import create_task, get_task, list_tasks, update_task, delete_task, reset_tasks


@pytest.fixture(autouse=True)
def clean_state():
    """Reset task storage before each test to ensure isolation.

    This fixture runs automatically before every test function,
    clearing all tasks and resetting the ID counter.
    """
    reset_tasks()


def test_create_task():
    """Test that creating a task returns a properly structured dictionary."""
    task = create_task("Test Task", "A test description")

    assert task["id"] == 1
    assert task["title"] == "Test Task"
    assert task["description"] == "A test description"
    assert task["status"] == "pending"
    assert "created_at" in task


def test_create_multiple_tasks():
    """Test that creating multiple tasks assigns sequential IDs."""
    task1 = create_task("Task 1")
    task2 = create_task("Task 2")

    assert task1["id"] == 1
    assert task2["id"] == 2


def test_get_task():
    """Test retrieving a task by its ID."""
    created = create_task("Fetch Me")
    fetched = get_task(created["id"])

    assert fetched is not None
    assert fetched["title"] == "Fetch Me"


def test_get_nonexistent_task():
    """Test that retrieving a non-existent task returns None."""
    result = get_task(999)
    assert result is None


def test_list_tasks():
    """Test listing all tasks returns the correct count."""
    create_task("Task A")
    create_task("Task B")
    create_task("Task C")

    tasks = list_tasks()
    assert len(tasks) == 3


def test_list_tasks_by_status():
    """Test filtering tasks by status."""
    create_task("Task A")
    task_b = create_task("Task B")
    update_task(task_b["id"], status="completed")

    pending = list_tasks(status="pending")
    completed = list_tasks(status="completed")

    assert len(pending) == 1
    assert len(completed) == 1


def test_update_task():
    """Test updating a task's title and status."""
    task = create_task("Original Title")
    updated = update_task(task["id"], title="Updated Title", status="in_progress")

    assert updated["title"] == "Updated Title"
    assert updated["status"] == "in_progress"


def test_delete_task():
    """Test that deleting a task removes it from storage.

    Intentional failure: This test expects delete_task to raise a
    ValueError for non-existent IDs, but the current implementation
    silently returns True.
    """
    task = create_task("Delete Me")
    result = delete_task(task["id"])
    assert result is True
    assert get_task(task["id"]) is None

    # This assertion will FAIL because delete_task does not raise ValueError
    with pytest.raises(ValueError):
        delete_task(999)
