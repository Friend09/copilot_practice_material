#!/usr/bin/env python3
"""
CLI To‑Do List Manager.

Commands:
  add "task description"
  list
  done <number>     # optional
"""
from __future__ import annotations
import json
import sys
from pathlib import Path
from typing import List, Dict

DB_FILE = Path(__file__).with_suffix('.json')


def load_tasks() -> List[Dict]:
    """Load tasks from DB_FILE. Return [] if file missing."""
    # TODO: implement


def save_tasks(tasks: List[Dict]) -> None:
    """Write tasks list to DB_FILE."""
    # TODO: implement


def add_task(description: str) -> None:
    """Add new task with 'description'."""
    # TODO: implement


def list_tasks() -> None:
    """Print tasks with index and status."""
    # TODO: implement


def mark_done(index: int) -> None:
    """Set task at index (1‑based) as done."""
    # TODO: implement


def main(argv: List[str]) -> None:
    if len(argv) < 2:
        print("Usage: python todo.py [add|list|done] ...")
        return

    cmd = argv[1]
    if cmd == "add":
        add_task(" ".join(argv[2:]))
    elif cmd == "list":
        list_tasks()
    elif cmd == "done":
        if len(argv) < 3 or not argv[2].isdigit():
            print("Provide task number.")
            return
        mark_done(int(argv[2]))
    else:
        print(f"Unknown command: {cmd}")


if __name__ == "__main__":
    main(sys.argv)
