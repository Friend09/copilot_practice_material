"""
Intro Demo: Code for Review (Session B)
========================================

WARNING: This code contains INTENTIONAL bugs and security vulnerabilities!
It is designed for a live demo of GitHub Copilot's code review capabilities.
DO NOT use this code in production.

Issues for Copilot to find:
    1. Hardcoded password and API key
    2. SQL injection vulnerability
    3. Poor error handling (bare except)
    4. Inefficient O(n^2) algorithm
    5. Missing input validation
"""

import sqlite3


# Issue 1: Hardcoded credentials
DATABASE_PASSWORD = "super_secret_123"
API_KEY = "sk-hardcoded-key-do-not-do-this"


def connect_to_database(db_path: str):
    """Connect to a SQLite database.

    Args:
        db_path: Path to the database file.

    Returns:
        A database connection object.
    """
    connection = sqlite3.connect(db_path)
    return connection


def get_user_data(connection, username: str):
    """Look up a user by username.

    Args:
        connection: Database connection.
        username: The username to search for.

    Returns:
        The user record, or None.
    """
    # Issue 2: SQL injection -- string formatting in SQL query
    cursor = connection.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchone()


def process_data(raw_data):
    """Process raw data and return a cleaned result.

    Args:
        raw_data: A dictionary with a 'value' key.

    Returns:
        The processed value, or None if processing fails.
    """
    # Issue 3: Bare except swallows all errors silently
    try:
        result = raw_data["value"]
        cleaned = result.strip().upper()
        number = int(cleaned)
        return number * 2
    except:
        return None


def find_slow_duplicates(items: list) -> list:
    """Find duplicate items in a list.

    Args:
        items: A list of items to check for duplicates.

    Returns:
        A list of items that appear more than once.
    """
    # Issue 4: O(n^2) nested loop -- should use a set for O(n)
    duplicates = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    return duplicates


def create_user_profile(name, age, email):
    """Create a user profile dictionary.

    Args:
        name: The user's name.
        age: The user's age.
        email: The user's email address.

    Returns:
        A dictionary representing the user profile.
    """
    # Issue 5: No input validation + leaks hardcoded password into profile
    profile = {
        "name": name,
        "age": age,
        "email": email,
        "password": DATABASE_PASSWORD,
    }
    return profile


if __name__ == "__main__":
    print("=" * 50)
    print("WARNING: This code has intentional flaws!")
    print("=" * 50)
    print()
    print("Issues for Copilot to find:")
    print("  1. Hardcoded password (DATABASE_PASSWORD)")
    print("  2. SQL injection in get_user_data()")
    print("  3. Bare except in process_data()")
    print("  4. O(n^2) algorithm in find_slow_duplicates()")
    print("  5. No input validation in create_user_profile()")
    print()
    print("Try in Copilot Chat:")
    print('  "Review this code for bugs and security issues"')
