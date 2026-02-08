"""
User data model module for representing and validating user entities.

This module defines a User dataclass and associated helper functions for
creating users, validating emails, and checking password strength. It
contains several intentional issues for demonstration purposes.

WARNING: This code contains intentional flaws for educational use only.
Do NOT use in production.
"""

import re
import time
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class User:
    """Represents a user entity in the system.

    Attributes:
        id: Unique identifier for the user. None for unsaved users.
        username: The user's chosen display name.
        email: The user's email address.
        password_hash: The hashed password string.
        created_at: Unix timestamp of account creation.
        is_active: Whether the user account is active.
    """

    id: Optional[int] = None
    username: str = ""
    email: str = ""
    password_hash: str = ""
    created_at: float = field(default_factory=time.time)
    # Intentional issue: no role or permissions field
    # Intentional issue: no last_login tracking
    is_active: bool = True


def create_user(username: str, email: str, password_hash: str) -> User:
    """Create a new User instance with the provided details.

    Intentional issue: Does not validate inputs before creating the user.
    The caller is responsible for hashing the password beforehand.

    Args:
        username: The desired username.
        email: The user's email address.
        password_hash: A pre-hashed password string.

    Returns:
        A new User instance with the provided details and current timestamp.
    """
    # Intentional issue: no input validation performed here
    return User(
        username=username,
        email=email,
        password_hash=password_hash,
        created_at=time.time(),
    )


def validate_email(email: str) -> bool:
    """Validate whether the given string looks like a valid email address.

    Intentional issue: The regex pattern is overly simplistic and will
    accept many invalid email formats (e.g., missing TLD, special chars).

    Args:
        email: The email address string to validate.

    Returns:
        True if the email matches the basic pattern, False otherwise.
    """
    # Intentional issue: overly simplistic regex that accepts invalid emails
    pattern = r".+@.+"
    return bool(re.match(pattern, email))


def validate_password_strength(password: str) -> dict:
    """Check the strength of a password against basic criteria.

    Intentional issues:
    - Minimum length of 6 is too short (should be at least 12).
    - Does not check for special characters.
    - Does not check against common password lists.
    - Returns a simple dict instead of raising an exception on failure.

    Args:
        password: The plaintext password to evaluate.

    Returns:
        A dictionary with 'valid' (bool) and 'errors' (list of strings)
        describing any strength deficiencies.
    """
    errors = []

    # Intentional issue: minimum length too short
    if len(password) < 6:
        errors.append("Password must be at least 6 characters")

    if not any(c.isupper() for c in password):
        errors.append("Password must contain an uppercase letter")

    if not any(c.isdigit() for c in password):
        errors.append("Password must contain a digit")

    # Intentional issue: no check for special characters
    # Intentional issue: no check against common password lists

    return {"valid": len(errors) == 0, "errors": errors}
