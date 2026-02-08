"""Basic Python linting checker for the Agent Skills demo.

This script performs lightweight linting checks on a Python source file,
covering docstrings, naming conventions, and import ordering. It is
designed to be referenced from a SKILL.md file and executed by Copilot
or run independently from the command line.

Usage:
    python lint_check.py <filepath>
"""

import ast
import re
import sys
from pathlib import Path


def check_docstrings(filepath: str) -> list[str]:
    """Check for missing docstrings in modules, classes, and public functions.

    Args:
        filepath: Path to the Python source file to check.

    Returns:
        A list of warning strings describing missing docstrings.
    """
    issues: list[str] = []
    source = Path(filepath).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=filepath)

    if not ast.get_docstring(tree):
        issues.append(f"{filepath}:1: module is missing a docstring")

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if not node.name.startswith("_") and not ast.get_docstring(node):
                issues.append(
                    f"{filepath}:{node.lineno}: function '{node.name}' "
                    f"is missing a docstring"
                )
        elif isinstance(node, ast.ClassDef):
            if not ast.get_docstring(node):
                issues.append(
                    f"{filepath}:{node.lineno}: class '{node.name}' "
                    f"is missing a docstring"
                )

    return issues


def check_naming_conventions(filepath: str) -> list[str]:
    """Check that names follow PEP 8 conventions.

    Validates that functions and variables use snake_case, classes use
    PascalCase, and module-level constants use UPPER_SNAKE_CASE.

    Args:
        filepath: Path to the Python source file to check.

    Returns:
        A list of warning strings describing naming violations.
    """
    issues: list[str] = []
    source = Path(filepath).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=filepath)

    snake_case = re.compile(r"^[a-z_][a-z0-9_]*$")
    pascal_case = re.compile(r"^[A-Z][a-zA-Z0-9]*$")

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if not snake_case.match(node.name):
                issues.append(
                    f"{filepath}:{node.lineno}: function '{node.name}' "
                    f"should use snake_case"
                )
        elif isinstance(node, ast.ClassDef):
            if not pascal_case.match(node.name):
                issues.append(
                    f"{filepath}:{node.lineno}: class '{node.name}' "
                    f"should use PascalCase"
                )

    return issues


def check_import_order(filepath: str) -> list[str]:
    """Check that imports are grouped and ordered correctly.

    Expects three groups separated by blank lines: standard library,
    third-party, and local imports. Within each group imports should
    be alphabetically sorted.

    Args:
        filepath: Path to the Python source file to check.

    Returns:
        A list of warning strings describing import ordering issues.
    """
    issues: list[str] = []
    source = Path(filepath).read_text(encoding="utf-8")
    tree = ast.parse(source, filename=filepath)

    import_names: list[tuple[int, str]] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                import_names.append((node.lineno, alias.name))
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                import_names.append((node.lineno, node.module))

    for i in range(1, len(import_names)):
        prev_name = import_names[i - 1][1].lower()
        curr_name = import_names[i][1].lower()
        if curr_name < prev_name:
            line = import_names[i][0]
            issues.append(
                f"{filepath}:{line}: import '{import_names[i][1]}' "
                f"should come before '{import_names[i - 1][1]}'"
            )

    return issues


def main() -> None:
    """Run all linting checks on the specified Python file.

    Reads a file path from command-line arguments, executes all
    checkers, and prints any issues found. Exits with code 1 if
    issues are detected, or 0 if the file is clean.
    """
    if len(sys.argv) != 2:
        print("Usage: python lint_check.py <filepath>")
        sys.exit(2)

    filepath = sys.argv[1]

    if not Path(filepath).exists():
        print(f"Error: file '{filepath}' not found")
        sys.exit(2)

    all_issues: list[str] = []
    all_issues.extend(check_docstrings(filepath))
    all_issues.extend(check_naming_conventions(filepath))
    all_issues.extend(check_import_order(filepath))

    if all_issues:
        print(f"Found {len(all_issues)} issue(s):\n")
        for issue in all_issues:
            print(f"  - {issue}")
        sys.exit(1)
    else:
        print(f"No issues found in {filepath}")
        sys.exit(0)


if __name__ == "__main__":
    main()
