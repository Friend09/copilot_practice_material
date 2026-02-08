# Python Style Guide

A concise reference for Python coding standards used by the `python-code-quality` skill.

---

## Naming Conventions

| Element | Convention | Example |
|---------|-----------|---------|
| Functions | `snake_case` | `calculate_total()` |
| Variables | `snake_case` | `user_count = 0` |
| Classes | `PascalCase` | `class UserAccount:` |
| Constants | `SCREAMING_SNAKE_CASE` | `MAX_RETRY_COUNT = 3` |
| Private methods | Leading underscore | `_validate_input()` |
| Dunder methods | Double underscore | `__init__()`, `__str__()` |
| Modules | `snake_case` | `user_manager.py` |
| Packages | `lowercase` (no underscores preferred) | `utilities/` |

---

## Import Ordering

Imports should be grouped in the following order, separated by a blank line between each group:

```python
# 1. Standard library imports
import os
import sys
from collections import defaultdict
from typing import Optional

# 2. Third-party imports
import requests
from flask import Flask, jsonify
from sqlalchemy import Column, Integer, String

# 3. Local application imports
from myapp.models import User
from myapp.utils.validators import validate_email
```

**Rules:**

- Use absolute imports over relative imports
- Avoid wildcard imports (`from module import *`)
- Sort imports alphabetically within each group
- One import per line for `import` statements; multiple names allowed for `from ... import`

---

## Docstring Format (Google Style)

### Module Docstring

```python
"""User account management module.

Provides classes and functions for creating, updating, and
deactivating user accounts in the system.
"""
```

### Function Docstring

```python
def create_user(name: str, email: str, role: str = "viewer") -> dict:
    """Create a new user account in the system.

    Validates the provided information, checks for duplicate emails,
    and persists the new user record to the database.

    Args:
        name: Full name of the user.
        email: Email address (must be unique).
        role: User role. Defaults to "viewer".
            Must be one of "viewer", "editor", or "admin".

    Returns:
        A dictionary containing the created user's ID and profile data.
        Example::

            {
                "id": "usr_abc123",
                "name": "Jane Doe",
                "email": "jane@example.com",
                "role": "viewer"
            }

    Raises:
        ValueError: If the email format is invalid.
        DuplicateEmailError: If the email is already registered.
    """
```

### Class Docstring

```python
class UserAccount:
    """Represents a user account in the system.

    Manages user state including authentication status, profile
    information, and role-based permissions.

    Attributes:
        user_id: Unique identifier for the user.
        email: User's email address.
        is_active: Whether the account is currently active.
    """

    def __init__(self, user_id: str, email: str) -> None:
        """Initialize a UserAccount instance.

        Args:
            user_id: Unique identifier for the user.
            email: User's email address.
        """
        self.user_id = user_id
        self.email = email
        self.is_active = True
```

---

## Type Hints

### Basic Annotations

```python
# Simple types
name: str = "Alice"
count: int = 0
ratio: float = 0.5
is_valid: bool = True

# Container types (Python 3.9+)
names: list[str] = ["Alice", "Bob"]
scores: dict[str, int] = {"Alice": 95}
unique_ids: set[int] = {1, 2, 3}
coordinates: tuple[float, float] = (1.0, 2.0)

# Optional values
middle_name: str | None = None  # Python 3.10+
```

### Function Signatures

```python
def process_items(
    items: list[str],
    max_count: int = 100,
    filter_fn: Callable[[str], bool] | None = None,
) -> dict[str, int]:
    """Process a list of items and return frequency counts."""
    ...
```

---

## Error Handling Patterns

### Preferred

```python
# Catch specific exceptions
try:
    result = parse_config(file_path)
except FileNotFoundError:
    logger.error("Config file not found: %s", file_path)
    raise
except json.JSONDecodeError as e:
    logger.error("Invalid JSON in config: %s", e)
    raise ConfigError(f"Malformed config file: {file_path}") from e
```

### Avoid

```python
# Bare except - catches SystemExit, KeyboardInterrupt, etc.
try:
    result = parse_config(file_path)
except:
    print("Something went wrong")

# Catching Exception too broadly
try:
    result = parse_config(file_path)
except Exception:
    pass  # Silently swallowing errors
```

### Custom Exceptions

```python
class AppError(Exception):
    """Base exception for application errors."""


class ConfigError(AppError):
    """Raised when configuration is invalid or missing."""


class ValidationError(AppError):
    """Raised when input data fails validation.

    Attributes:
        field: The field name that failed validation.
        reason: Explanation of why validation failed.
    """

    def __init__(self, field: str, reason: str) -> None:
        self.field = field
        self.reason = reason
        super().__init__(f"Validation failed for '{field}': {reason}")
```

---

## Common Anti-Patterns

### Mutable Default Arguments

```python
# BAD: list is shared across all calls
def add_item(item: str, items: list[str] = []) -> list[str]:
    items.append(item)
    return items

# GOOD: use None and create inside the function
def add_item(item: str, items: list[str] | None = None) -> list[str]:
    if items is None:
        items = []
    items.append(item)
    return items
```

### String Concatenation in Loops

```python
# BAD: creates new string object each iteration
result = ""
for word in words:
    result += word + " "

# GOOD: use join()
result = " ".join(words)
```

### Nested Functions Beyond 2 Levels

```python
# BAD: deeply nested and hard to test
def process():
    def validate():
        def check_field():
            ...
        check_field()
    validate()

# GOOD: extract to module-level functions
def _check_field() -> bool:
    ...

def _validate(data: dict) -> bool:
    return _check_field()

def process() -> None:
    _validate(data)
```
