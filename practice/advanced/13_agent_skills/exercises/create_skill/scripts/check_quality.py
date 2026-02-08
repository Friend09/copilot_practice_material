"""Python Code Quality Checker.

A basic static analysis tool that checks Python source files for common
quality issues including missing docstrings, missing type hints, and
naming convention violations. Designed to be referenced from the
python-code-quality Agent Skill (SKILL.md).

Usage:
    python check_quality.py <file_or_directory>
    python check_quality.py src/
    python check_quality.py my_module.py
"""

import ast
import os
import re
import sys
from dataclasses import dataclass, field
from enum import Enum
from typing import Optional


class Severity(Enum):
    """Severity levels for quality findings."""

    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"


@dataclass
class Finding:
    """Represents a single quality issue found during analysis.

    Attributes:
        file_path: Path to the file containing the issue.
        line: Line number where the issue occurs.
        severity: Severity level of the finding.
        category: Category of the check (e.g., 'docstring', 'type-hint').
        message: Human-readable description of the issue.
    """

    file_path: str
    line: int
    severity: Severity
    category: str
    message: str

    def __str__(self) -> str:
        """Return a formatted string representation of the finding."""
        return (
            f"  [{self.severity.value}] {self.file_path}:{self.line} "
            f"({self.category}) {self.message}"
        )


@dataclass
class Report:
    """Aggregated quality report for one or more files.

    Attributes:
        findings: List of all findings discovered during analysis.
        files_checked: Total number of files analyzed.
    """

    findings: list[Finding] = field(default_factory=list)
    files_checked: int = 0

    def add(self, finding: Finding) -> None:
        """Add a finding to the report.

        Args:
            finding: The Finding instance to add.
        """
        self.findings.append(finding)

    def summary(self) -> str:
        """Generate a human-readable summary of all findings.

        Returns:
            A formatted string summarizing the report.
        """
        errors = sum(1 for f in self.findings if f.severity == Severity.ERROR)
        warnings = sum(1 for f in self.findings if f.severity == Severity.WARNING)
        infos = sum(1 for f in self.findings if f.severity == Severity.INFO)

        lines = [
            "=" * 60,
            "Python Code Quality Report",
            "=" * 60,
            f"Files checked: {self.files_checked}",
            f"Total findings: {len(self.findings)}",
            f"  Errors:   {errors}",
            f"  Warnings: {warnings}",
            f"  Info:     {infos}",
            "-" * 60,
        ]

        if not self.findings:
            lines.append("No issues found. Code quality looks good!")
        else:
            # Group findings by file
            by_file: dict[str, list[Finding]] = {}
            for finding in self.findings:
                by_file.setdefault(finding.file_path, []).append(finding)

            for file_path, file_findings in sorted(by_file.items()):
                lines.append(f"\n{file_path}:")
                for finding in sorted(file_findings, key=lambda f: f.line):
                    lines.append(str(finding))

        lines.append("\n" + "=" * 60)
        return "\n".join(lines)


def check_docstrings(tree: ast.AST, file_path: str, report: Report) -> None:
    """Check for missing docstrings on public functions, classes, and the module.

    Examines the AST for function definitions, class definitions, and the
    module itself. Reports a warning for any public entity (name not starting
    with underscore) that lacks a docstring.

    Args:
        tree: The parsed AST of the Python source file.
        file_path: Path to the source file (for reporting).
        report: The Report instance to add findings to.
    """
    # Check module-level docstring
    if not ast.get_docstring(tree):
        report.add(Finding(
            file_path=file_path,
            line=1,
            severity=Severity.WARNING,
            category="docstring",
            message="Module is missing a docstring.",
        ))

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            if not node.name.startswith("_") and not ast.get_docstring(node):
                report.add(Finding(
                    file_path=file_path,
                    line=node.lineno,
                    severity=Severity.WARNING,
                    category="docstring",
                    message=f"Public function '{node.name}' is missing a docstring.",
                ))
        elif isinstance(node, ast.ClassDef):
            if not node.name.startswith("_") and not ast.get_docstring(node):
                report.add(Finding(
                    file_path=file_path,
                    line=node.lineno,
                    severity=Severity.WARNING,
                    category="docstring",
                    message=f"Class '{node.name}' is missing a docstring.",
                ))


def check_type_hints(tree: ast.AST, file_path: str, report: Report) -> None:
    """Check for missing type annotations on function parameters and return values.

    Inspects each function definition in the AST. Reports an info-level finding
    for any parameter (except 'self' and 'cls') lacking a type annotation, and
    for any function missing a return type annotation.

    Args:
        tree: The parsed AST of the Python source file.
        file_path: Path to the source file (for reporting).
        report: The Report instance to add findings to.
    """
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            # Check parameter annotations
            for arg in node.args.args:
                if arg.arg in ("self", "cls"):
                    continue
                if arg.annotation is None:
                    report.add(Finding(
                        file_path=file_path,
                        line=node.lineno,
                        severity=Severity.INFO,
                        category="type-hint",
                        message=(
                            f"Parameter '{arg.arg}' in function "
                            f"'{node.name}' is missing a type annotation."
                        ),
                    ))

            # Check return annotation
            if node.returns is None and not node.name.startswith("_"):
                report.add(Finding(
                    file_path=file_path,
                    line=node.lineno,
                    severity=Severity.INFO,
                    category="type-hint",
                    message=(
                        f"Function '{node.name}' is missing a "
                        f"return type annotation."
                    ),
                ))


def check_naming_conventions(
    tree: ast.AST, file_path: str, report: Report
) -> None:
    """Check that names follow Python naming conventions.

    Validates:
    - Functions and variables use snake_case
    - Classes use PascalCase
    - Module-level constants (UPPER_CASE assignments) are acceptable

    Args:
        tree: The parsed AST of the Python source file.
        file_path: Path to the source file (for reporting).
        report: The Report instance to add findings to.
    """
    snake_case_pattern = re.compile(r"^_?_?[a-z][a-z0-9_]*_?_?$")
    pascal_case_pattern = re.compile(r"^_?[A-Z][a-zA-Z0-9]*$")

    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            # Dunder methods are fine
            if node.name.startswith("__") and node.name.endswith("__"):
                continue
            if not snake_case_pattern.match(node.name):
                report.add(Finding(
                    file_path=file_path,
                    line=node.lineno,
                    severity=Severity.WARNING,
                    category="naming",
                    message=(
                        f"Function '{node.name}' should use snake_case."
                    ),
                ))
        elif isinstance(node, ast.ClassDef):
            if not pascal_case_pattern.match(node.name):
                report.add(Finding(
                    file_path=file_path,
                    line=node.lineno,
                    severity=Severity.WARNING,
                    category="naming",
                    message=(
                        f"Class '{node.name}' should use PascalCase."
                    ),
                ))


def check_anti_patterns(tree: ast.AST, file_path: str, report: Report) -> None:
    """Check for common Python anti-patterns.

    Detects:
    - Mutable default arguments (list, dict, set literals as defaults)
    - Bare except clauses (except without a specific exception type)

    Args:
        tree: The parsed AST of the Python source file.
        file_path: Path to the source file (for reporting).
        report: The Report instance to add findings to.
    """
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            # Check mutable default arguments
            for default in node.args.defaults + node.args.kw_defaults:
                if default is None:
                    continue
                if isinstance(default, (ast.List, ast.Dict, ast.Set)):
                    report.add(Finding(
                        file_path=file_path,
                        line=node.lineno,
                        severity=Severity.ERROR,
                        category="anti-pattern",
                        message=(
                            f"Function '{node.name}' uses a mutable default "
                            f"argument. Use None and assign inside the function."
                        ),
                    ))

        # Check bare except
        if isinstance(node, ast.ExceptHandler):
            if node.type is None:
                report.add(Finding(
                    file_path=file_path,
                    line=node.lineno,
                    severity=Severity.ERROR,
                    category="anti-pattern",
                    message="Bare 'except:' clause. Catch specific exceptions.",
                ))


def analyze_file(file_path: str, report: Report) -> None:
    """Analyze a single Python file for quality issues.

    Parses the file into an AST and runs all quality checks against it.
    If the file cannot be parsed, a syntax error finding is recorded instead.

    Args:
        file_path: Path to the Python file to analyze.
        report: The Report instance to add findings to.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            source = f.read()
    except (OSError, IOError) as e:
        report.add(Finding(
            file_path=file_path,
            line=0,
            severity=Severity.ERROR,
            category="file",
            message=f"Could not read file: {e}",
        ))
        return

    try:
        tree = ast.parse(source, filename=file_path)
    except SyntaxError as e:
        report.add(Finding(
            file_path=file_path,
            line=e.lineno or 0,
            severity=Severity.ERROR,
            category="syntax",
            message=f"Syntax error: {e.msg}",
        ))
        return

    report.files_checked += 1

    check_docstrings(tree, file_path, report)
    check_type_hints(tree, file_path, report)
    check_naming_conventions(tree, file_path, report)
    check_anti_patterns(tree, file_path, report)


def collect_python_files(path: str) -> list[str]:
    """Recursively collect all Python files from a path.

    If the path is a single .py file, returns it in a list.
    If the path is a directory, walks it recursively and collects
    all .py files, skipping hidden directories and __pycache__.

    Args:
        path: A file path or directory path to search.

    Returns:
        A sorted list of absolute paths to Python files.
    """
    if os.path.isfile(path):
        if path.endswith(".py"):
            return [path]
        return []

    python_files: list[str] = []
    for root, dirs, files in os.walk(path):
        # Skip hidden directories and __pycache__
        dirs[:] = [
            d for d in dirs
            if not d.startswith(".") and d != "__pycache__"
        ]
        for filename in sorted(files):
            if filename.endswith(".py"):
                python_files.append(os.path.join(root, filename))

    return sorted(python_files)


def main(target: Optional[str] = None) -> int:
    """Entry point for the quality checker.

    Parses command-line arguments (or uses the provided target), collects
    Python files, runs all quality checks, and prints a summary report.

    Args:
        target: Optional path to check. If None, reads from sys.argv.

    Returns:
        Exit code: 0 if no errors found, 1 if errors exist.
    """
    if target is None:
        if len(sys.argv) < 2:
            print("Usage: python check_quality.py <file_or_directory>")
            print("Example: python check_quality.py src/")
            return 1
        target = sys.argv[1]

    if not os.path.exists(target):
        print(f"Error: '{target}' does not exist.")
        return 1

    python_files = collect_python_files(target)
    if not python_files:
        print(f"No Python files found in '{target}'.")
        return 0

    report = Report()
    for file_path in python_files:
        analyze_file(file_path, report)

    print(report.summary())

    # Return non-zero if any errors were found
    error_count = sum(
        1 for f in report.findings if f.severity == Severity.ERROR
    )
    return 1 if error_count > 0 else 0


if __name__ == "__main__":
    sys.exit(main())
