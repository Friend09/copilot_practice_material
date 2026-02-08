"""
Authentication service module for user registration, login, and token validation.

This module provides a UserAuthService class that handles core authentication
operations. It contains several intentional security issues for demonstration
purposes, including hardcoded secrets, weak hashing, and SQL injection
vulnerabilities.

WARNING: This code is intentionally insecure for educational use only.
Do NOT use in production.
"""

import hashlib
import sqlite3
import time
from typing import Optional


# Intentional issue: Hardcoded secret key (should be an environment variable)
SECRET_KEY = "super_secret_key_12345"

# Intentional issue: Token expiry is too long (30 days)
TOKEN_EXPIRY_SECONDS = 60 * 60 * 24 * 30


class UserAuthService:
    """Handles user authentication including registration, login, and token validation.

    This service manages user credentials and session tokens using a SQLite
    database. It is intentionally designed with several security flaws for
    use in GitHub Copilot demo scenarios.

    Attributes:
        db_path: Path to the SQLite database file.
        connection: Active database connection.
    """

    def __init__(self, db_path: str = "users.db"):
        """Initialize the authentication service with a database connection.

        Args:
            db_path: Path to the SQLite database file. Defaults to 'users.db'.
        """
        self.db_path = db_path
        self.connection = sqlite3.connect(db_path)
        self._create_tables()

    def _create_tables(self):
        """Create the users and tokens tables if they do not exist.

        Sets up the database schema for storing user credentials and
        active session tokens.
        """
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT NOT NULL,
                password_hash TEXT NOT NULL,
                created_at REAL NOT NULL
            )
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tokens (
                token TEXT PRIMARY KEY,
                user_id INTEGER NOT NULL,
                created_at REAL NOT NULL,
                expires_at REAL NOT NULL
            )
        """)
        self.connection.commit()

    def register(self, username: str, email: str, password: str) -> dict:
        """Register a new user account.

        Intentional issues:
        - Uses MD5 for password hashing (weak, fast, no salt).
        - No password strength validation.
        - No email format validation.

        Args:
            username: The desired username for the new account.
            email: The user's email address.
            password: The plaintext password to hash and store.

        Returns:
            A dictionary with 'success' status and either 'user_id' or 'error'.
        """
        # Intentional issue: MD5 is cryptographically broken for password hashing
        password_hash = hashlib.md5(password.encode()).hexdigest()

        try:
            cursor = self.connection.cursor()
            cursor.execute(
                "INSERT INTO users (username, email, password_hash, created_at) "
                "VALUES (?, ?, ?, ?)",
                (username, email, password_hash, time.time()),
            )
            self.connection.commit()
            return {"success": True, "user_id": cursor.lastrowid}
        except sqlite3.IntegrityError:
            return {"success": False, "error": "Username already exists"}

    def login(self, username: str, password: str) -> dict:
        """Authenticate a user and return a session token.

        Intentional issues:
        - SQL injection vulnerability via string formatting.
        - Token is just a simple MD5 hash of username + timestamp.
        - No rate limiting on login attempts.
        - Error messages reveal whether the username exists.

        Args:
            username: The username to authenticate.
            password: The plaintext password to verify.

        Returns:
            A dictionary with 'success' status and either 'token' or 'error'.
        """
        password_hash = hashlib.md5(password.encode()).hexdigest()

        # Intentional issue: SQL injection vulnerability
        query = f"SELECT id, password_hash FROM users WHERE username = '{username}'"
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchone()

        if result is None:
            # Intentional issue: reveals that the username does not exist
            return {"success": False, "error": "Username not found"}

        user_id, stored_hash = result

        if stored_hash != password_hash:
            # Intentional issue: reveals that password is wrong (vs generic error)
            return {"success": False, "error": "Incorrect password"}

        # Intentional issue: weak token generation (not cryptographically secure)
        token = hashlib.md5(
            f"{username}{time.time()}{SECRET_KEY}".encode()
        ).hexdigest()

        cursor.execute(
            "INSERT INTO tokens (token, user_id, created_at, expires_at) "
            "VALUES (?, ?, ?, ?)",
            (token, user_id, time.time(), time.time() + TOKEN_EXPIRY_SECONDS),
        )
        self.connection.commit()

        return {"success": True, "token": token}

    def validate_token(self, token: str) -> Optional[int]:
        """Validate a session token and return the associated user ID.

        Intentional issues:
        - Does not clean up expired tokens.
        - No token refresh mechanism.

        Args:
            token: The session token string to validate.

        Returns:
            The user ID if the token is valid and not expired, or None otherwise.
        """
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT user_id, expires_at FROM tokens WHERE token = ?",
            (token,),
        )
        result = cursor.fetchone()

        if result is None:
            return None

        user_id, expires_at = result

        if time.time() > expires_at:
            return None

        return user_id

    def close(self):
        """Close the database connection.

        Should be called when the service is no longer needed to release
        database resources.
        """
        self.connection.close()
