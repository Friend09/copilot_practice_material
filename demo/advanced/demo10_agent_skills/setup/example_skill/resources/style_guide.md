# Python Style Guide

This style guide defines the team conventions for Python code. It supplements PEP 8
with project-specific requirements.

## Naming Conventions

| Element          | Convention          | Example                  |
|------------------|---------------------|--------------------------|
| Variables        | `snake_case`        | `user_count`             |
| Functions        | `snake_case`        | `get_active_users()`     |
| Classes          | `PascalCase`        | `UserAccount`            |
| Constants        | `UPPER_SNAKE_CASE`  | `MAX_RETRY_COUNT`        |
| Private members  | `_leading_underscore`| `_internal_cache`       |
| Module files     | `snake_case.py`     | `data_loader.py`         |

## Import Ordering

Imports must appear in three groups, separated by a blank line:

1. **Standard library** -- `os`, `sys`, `pathlib`, `typing`, etc.
2. **Third-party packages** -- `requests`, `flask`, `sqlalchemy`, etc.
3. **Local application** -- `from myapp.models import User`, etc.

Within each group, sort imports alphabetically. Prefer `import x` over
`from x import *`.

## Docstring Format (Google Style)

```python
def fetch_user(user_id: int, include_inactive: bool = False) -> User:
    """Fetch a user record from the database.

    Args:
        user_id: The unique identifier of the user.
        include_inactive: Whether to include deactivated accounts.

    Returns:
        The User object matching the given ID.

    Raises:
        UserNotFoundError: If no user matches the given ID.
    """
```

Every module, class, and public function must have a docstring.

## Error Handling Patterns

- Catch specific exceptions, never bare `except:` or `except Exception:`
- Use custom exception classes for domain errors
- Always include context in error messages
- Log exceptions before re-raising when appropriate

## Type Hints Requirements

- All function parameters must have type annotations
- All functions must declare a return type (use `-> None` for procedures)
- Use `Optional[T]` when a value can be `None`
- For Python 3.9+, prefer built-in generics (`list[str]`) over `typing` imports
- Use `TypeAlias` for complex or reused type expressions
