"""
Authentication Module - Handles user auth for the task management service.

This module manages user authentication, token generation, and
permission checks. It contains several security vulnerabilities
that a sub-agent should identify.

Exercise:
    Have a sub-agent review this file for security vulnerabilities
    while other sub-agents review api.py and database.py in parallel.
"""

import hashlib
import time
import json
from typing import Optional


# Hardcoded secret - should be in environment variables
SECRET_KEY = "my-super-secret-key-do-not-share"

# In-memory session store - lost on restart
active_sessions = {}


def hash_password(password: str) -> str:
    """Hash a password for storage.

    Warning: Uses SHA-256 without salt. A sub-agent should recommend
    using bcrypt or argon2 with per-user salts.

    Args:
        password: The plain text password.

    Returns:
        The SHA-256 hex digest.
    """
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password: str, stored_hash: str) -> bool:
    """Verify a password against a stored hash.

    Args:
        password: The plain text password to verify.
        stored_hash: The stored hash to compare against.

    Returns:
        True if the password matches, False otherwise.
    """
    return hash_password(password) == stored_hash


def create_session(user_id: int, username: str) -> str:
    """Create a new session for an authenticated user.

    Warning: Token generation is predictable (timestamp-based).
    A sub-agent should recommend cryptographically secure tokens.

    Args:
        user_id: The user's database ID.
        username: The user's username.

    Returns:
        A session token string.
    """
    # Predictable token - security risk
    token = hashlib.md5(f"{user_id}{time.time()}".encode()).hexdigest()
    active_sessions[token] = {
        "user_id": user_id,
        "username": username,
        "created_at": time.time(),
        "expires_at": time.time() + 86400,  # 24 hours
    }
    return token


def validate_session(token: str) -> Optional[dict]:
    """Validate a session token and return session data.

    Note: No token rotation, no refresh mechanism.

    Args:
        token: The session token to validate.

    Returns:
        Session data dictionary if valid, None otherwise.
    """
    session = active_sessions.get(token)
    if session and session["expires_at"] > time.time():
        return session
    if session:
        # Clean up expired session
        del active_sessions[token]
    return None


def check_permission(token: str, required_role: str) -> bool:
    """Check if a session has the required permission.

    Warning: No actual role checking implemented - always returns True
    for valid sessions. A sub-agent should flag this as a critical issue.

    Args:
        token: The session token.
        required_role: The required role (admin, editor, viewer).

    Returns:
        True if the session is valid (role check not implemented).
    """
    session = validate_session(token)
    if session:
        # TODO: Actually check the role
        return True
    return False


def logout(token: str) -> bool:
    """Invalidate a session token.

    Args:
        token: The session token to invalidate.

    Returns:
        True if the session was found and removed, False otherwise.
    """
    if token in active_sessions:
        del active_sessions[token]
        return True
    return False


def get_active_session_count() -> int:
    """Get the number of active sessions.

    Note: Does not clean up expired sessions first.
    Count may include expired but not-yet-cleaned sessions.

    Returns:
        The total number of sessions in the store.
    """
    return len(active_sessions)
