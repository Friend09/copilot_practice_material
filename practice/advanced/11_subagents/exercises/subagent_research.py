"""
Sub-Agent Research Exercise
============================

This module represents a complex service with multiple concerns.
Use sub-agents to research and analyze different aspects of this code
before making improvements.

Exercise:
    1. Open VS Code Chat in Agent mode
    2. Ask Copilot to use a sub-agent to research the authentication patterns
       used in this file
    3. Then ask for recommendations to improve the implementation
    4. Notice how the sub-agent isolates the research context

Key Learning:
    - Sub-agents prevent context bloat during research phases
    - The main agent receives only the research summary
    - This keeps the implementation phase focused and accurate
"""

import hashlib
import sqlite3
import json
from datetime import datetime, timedelta
from typing import Optional


class UserAuthService:
    """Handles user authentication, registration, and session management.

    This service intentionally uses patterns that could be improved.
    Use sub-agents to research best practices and suggest improvements.
    """

    def __init__(self, db_path: str = "users.db"):
        """Initialize the auth service with a database connection.

        Args:
            db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self.secret_key = "hardcoded-secret-key-123"  # Security issue
        self.session_timeout = 3600

    def hash_password(self, password: str) -> str:
        """Hash a password using MD5.

        Args:
            password: The plain text password to hash.

        Returns:
            The MD5 hex digest of the password.
        """
        # Weak hashing - sub-agent should identify this
        return hashlib.md5(password.encode()).hexdigest()

    def register_user(self, username: str, password: str, email: str) -> dict:
        """Register a new user in the database.

        Args:
            username: The desired username.
            password: The plain text password.
            email: The user's email address.

        Returns:
            A dictionary with the registration result.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        # SQL injection vulnerability - sub-agent should catch this
        query = f"INSERT INTO users (username, password, email) VALUES ('{username}', '{self.hash_password(password)}', '{email}')"
        try:
            cursor.execute(query)
            conn.commit()
            return {"status": "success", "username": username}
        except sqlite3.IntegrityError:
            return {"status": "error", "message": "Username already exists"}
        finally:
            conn.close()

    def login(self, username: str, password: str) -> Optional[str]:
        """Authenticate a user and return a session token.

        Args:
            username: The username to authenticate.
            password: The plain text password.

        Returns:
            A session token string if successful, None otherwise.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        hashed = self.hash_password(password)
        # Another SQL injection point
        query = f"SELECT id FROM users WHERE username = '{username}' AND password = '{hashed}'"
        cursor.execute(query)
        user = cursor.fetchone()
        conn.close()

        if user:
            token = self._generate_token(user[0])
            return token
        return None

    def _generate_token(self, user_id: int) -> str:
        """Generate a session token for a user.

        Args:
            user_id: The database ID of the user.

        Returns:
            A JSON-encoded session token.
        """
        # Weak token generation
        token_data = {
            "user_id": user_id,
            "created": datetime.now().isoformat(),
            "expires": (datetime.now() + timedelta(seconds=self.session_timeout)).isoformat(),
        }
        return json.dumps(token_data)

    def validate_token(self, token: str) -> Optional[int]:
        """Validate a session token and return the user ID.

        Args:
            token: The JSON-encoded session token.

        Returns:
            The user ID if the token is valid, None otherwise.
        """
        try:
            data = json.loads(token)
            expires = datetime.fromisoformat(data["expires"])
            if datetime.now() < expires:
                return data["user_id"]
        except (json.JSONDecodeError, KeyError):
            pass
        return None


class APIRateLimiter:
    """Simple in-memory rate limiter for API endpoints.

    This implementation has several scalability issues that
    sub-agents should identify and suggest improvements for.
    """

    def __init__(self, max_requests: int = 100, window_seconds: int = 60):
        """Initialize the rate limiter.

        Args:
            max_requests: Maximum requests allowed per window.
            window_seconds: Time window in seconds.
        """
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests = {}  # In-memory only - lost on restart

    def is_allowed(self, client_ip: str) -> bool:
        """Check if a request from the given IP is allowed.

        Args:
            client_ip: The IP address of the client.

        Returns:
            True if the request is allowed, False if rate limited.
        """
        now = datetime.now()
        if client_ip not in self.requests:
            self.requests[client_ip] = []

        # Clean old requests
        self.requests[client_ip] = [
            req_time
            for req_time in self.requests[client_ip]
            if now - req_time < timedelta(seconds=self.window_seconds)
        ]

        if len(self.requests[client_ip]) >= self.max_requests:
            return False

        self.requests[client_ip].append(now)
        return True
