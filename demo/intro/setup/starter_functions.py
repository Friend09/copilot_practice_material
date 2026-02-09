"""
Intro Demo: Starter Functions for Inline Completion
====================================================

These functions have signatures and docstrings but NO implementations.
During the live demo, place your cursor inside each function body and
let GitHub Copilot suggest the implementation via inline completions.

Usage:
    Open this file in VS Code with GitHub Copilot enabled.
    Place your cursor inside a function body and start typing or wait
    for Copilot's ghost text to appear. Press Tab to accept.
"""


def calculate_average(numbers: list) -> float:
    """Calculate the average of a list of numbers.

    Args:
        numbers: A list of numeric values.

    Returns:
        The arithmetic mean of the numbers.

    Raises:
        ValueError: If the list is empty.

    Example:
        >>> calculate_average([10, 20, 30])
        20.0
    """
    # TODO: Implement this function (let Copilot suggest!)
    pass


def find_duplicates(items: list) -> list:
    """Find and return duplicate items in a list.

    Args:
        items: A list of items that may contain duplicates.

    Returns:
        A list of items that appear more than once.

    Example:
        >>> find_duplicates([1, 2, 3, 2, 4, 3])
        [2, 3]
    """
    pass


def is_palindrome(text: str) -> bool:
    """Check if a given text is a palindrome.

    Ignores case and spaces when checking.

    Args:
        text: The string to check.

    Returns:
        True if the text is a palindrome, False otherwise.

    Example:
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("hello")
        False
    """
    pass


class Student:
    """A class representing a student with grades.

    Attributes:
        name: The student's full name.
        student_id: A unique identifier for the student.
        grades: A list of numeric grades.
    """

    def __init__(self, name: str, student_id: str):
        """Initialize a Student instance.

        Args:
            name: The student's full name.
            student_id: A unique identifier.
        """
        # TODO: Initialize attributes (let Copilot suggest!)
        pass

    def add_grade(self, grade: float) -> None:
        """Add a grade to the student's record.

        Args:
            grade: A numeric grade value (0-100).
        """
        pass

    def get_average(self) -> float:
        """Calculate and return the student's average grade.

        Returns:
            The average of all grades, or 0.0 if no grades exist.
        """
        pass

    def __str__(self) -> str:
        """Return a string representation of the student."""
        pass


if __name__ == "__main__":
    print("=" * 50)
    print("Starter Functions for Inline Completion Demo")
    print("=" * 50)
    print()
    print("Instructions:")
    print("  1. Open this file in VS Code with Copilot enabled")
    print("  2. Place cursor inside a function body")
    print("  3. Start typing or wait for Copilot's ghost text")
    print("  4. Press Tab to accept the suggestion")
    print()
    print("Functions to complete:")
    print("  - calculate_average(numbers)")
    print("  - find_duplicates(items)")
    print("  - is_palindrome(text)")
    print("  - Student class (init, add_grade, get_average)")
