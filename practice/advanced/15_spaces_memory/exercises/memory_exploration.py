"""
Module 15 - Exercise 3: Memory Exploration

This file is a scaffold for testing Copilot Memory across multiple sessions.
The code below contains intentional style inconsistencies that you will ask
Copilot to review and fix according to your personal preferences.

=== EXERCISE INSTRUCTIONS ===

This exercise spans multiple VS Code sessions. Follow these steps in order:

SESSION 1 - Establish Preferences:
    1. Open this file in VS Code with Copilot agent mode enabled.
    2. Ask Copilot to review the code. It will likely point out the style
       inconsistencies (mixed naming conventions, inconsistent docstrings,
       mixed test framework references).
    3. Explicitly tell Copilot your preferences. For example:
       - "I prefer pytest over unittest for all testing"
       - "I use Google-style docstrings for all Python code"
       - "I prefer snake_case for functions and UPPER_CASE for constants"
       - "I always type-hint function signatures"
    4. Ask Copilot to refactor this file according to your stated preferences.
    5. Close VS Code completely.

SESSION 2 - Test Memory Persistence:
    1. Reopen VS Code and this file.
    2. Ask Copilot: "Add a new method to ProjectPreferences called
       get_documentation_style() that returns the preferred documentation
       format."
    3. Observe: Does the new method follow the preferences you stated in
       Session 1? Check for:
       - Correct docstring style (Google-style if that is what you chose)
       - Correct naming convention
       - Type hints present or absent (matching your preference)
       - Test framework references (pytest vs unittest)
    4. Note what Copilot remembered and what it forgot.

SESSION 3 - Direct Memory Query:
    1. Open a new Copilot chat (do not open this file first).
    2. Ask: "What are my coding preferences for Python projects?"
    3. Observe: Does Copilot recall the preferences from Session 1?
    4. Try: "What test framework do I prefer?" and "What docstring style
       do I use?"
    5. Document what was remembered accurately vs. what was lost.

BONUS - Explicit Memory Management (Claude Agent):
    If you are using the Claude agent in Copilot:
    1. Use the /memory slash command to view stored memories
    2. Use /memory to explicitly add: "For Python projects, I always use
       pytest, Google-style docstrings, and type hints on all functions"
    3. Start a new session and test recall

=== END EXERCISE INSTRUCTIONS ===
"""

from typing import Any


# NOTE: Intentional style inconsistency below -- mixed naming conventions,
# inconsistent docstrings, and mixed test references. This is deliberate
# for the exercise.


DEFAULT_STYLE = "pep8"
defaultNamingConvention = "snake_case"  # Intentional: camelCase variable name
DEFAULT_TEST_FRAMEWORK = "unittest"  # Intentional: you may prefer pytest


class ProjectPreferences:
    """Stores coding preferences for a project.

    This class is intentionally written with mixed styles to give learners
    something concrete to discuss with Copilot and establish their preferences.

    Attributes:
        project_name: The name of the project.
        language: The programming language (default: Python).
        preferences: A dictionary of preference key-value pairs.
    """

    def __init__(self, project_name: str, language: str = "Python"):
        """Initialize ProjectPreferences.

        Args:
            project_name: The name of the project.
            language: The programming language for this project.
        """
        self.project_name = project_name
        self.language = language
        self.preferences: dict[str, Any] = {}

    def set_preference(self, key, value):
        """Set a preference value.

        Parameters:
            key: The preference key.
            value: The preference value.
        """
        # NOTE: Intentional inconsistency -- this docstring uses "Parameters"
        # (NumPy style) instead of "Args" (Google style). Discuss with Copilot
        # which style you prefer.
        self.preferences[key] = value

    def getPreference(self, key: str) -> Any:
        """Get a preference value by key.

        Args:
            key: The preference key to look up.

        Returns:
            The preference value, or None if not found.
        """
        # NOTE: Intentional inconsistency -- this method uses camelCase naming
        # instead of snake_case. Discuss with Copilot which convention to use.
        return self.preferences.get(key)


def get_preferred_style() -> str:
    """Return the preferred coding style for the project.

    Returns:
        A string representing the preferred style guide name.
    """
    return DEFAULT_STYLE


def get_naming_convention():
    # NOTE: Intentional -- missing docstring and missing type hint.
    # Ask Copilot to fix this based on your preferences.
    return defaultNamingConvention


def GetTestFramework() -> str:
    """Return the preferred test framework.

    Returns:
        str: The name of the preferred test framework.
    """
    # NOTE: Intentional inconsistency -- PascalCase function name.
    # This should be snake_case if that is your preference.
    return DEFAULT_TEST_FRAMEWORK


def validate_preferences(prefs: ProjectPreferences) -> list[str]:
    """Validate that all required preferences are set.

    Args:
        prefs: The ProjectPreferences instance to validate.

    Returns:
        A list of warning messages for missing or inconsistent preferences.
    """
    warnings = []

    if not prefs.project_name:
        warnings.append("Project name is required")

    style = prefs.getPreference("style")
    if style is None:
        warnings.append("No coding style preference set")

    naming = prefs.getPreference("naming_convention")
    if naming is None:
        warnings.append("No naming convention preference set")

    testFramework = prefs.getPreference("test_framework")
    if testFramework is None:
        warnings.append("No test framework preference set")

    return warnings


# --- Example usage (for testing) ---

if __name__ == "__main__":
    # Create preferences for a sample project
    prefs = ProjectPreferences("my-api-service")
    prefs.set_preference("style", get_preferred_style())
    prefs.set_preference("naming_convention", get_naming_convention())
    prefs.set_preference("test_framework", GetTestFramework())

    # Validate and print results
    issues = validate_preferences(prefs)
    if issues:
        print("Preference warnings:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("All preferences are set.")
        print(f"  Style: {prefs.getPreference('style')}")
        print(f"  Naming: {prefs.getPreference('naming_convention')}")
        print(f"  Testing: {prefs.getPreference('test_framework')}")
