# Intro to GitHub Copilot -- Prompts

All prompts for both sessions. Copy-paste these exactly during your live demo.

---

## Session A: "Productivity Edition"

### Segment 3: Copilot Chat (9:00 - 17:00)

#### 3a. Explain Code

Open `setup/calculator.py`, select all code, then paste in Chat:

```text
Explain what this Calculator class does, including each method.
```

#### 3b. Add Error Handling

```text
Add error handling to the divide method to handle division by zero gracefully, and add input validation to all methods to ensure arguments are numbers.
```

#### 3c. Generate Tests

```text
Generate comprehensive unit tests for this Calculator class using pytest. Cover normal cases, edge cases, and error cases.
```

#### 3d. Add History Feature

> Skip this prompt if running short on time.

```text
Add a calculation history feature to this Calculator class. It should store the last 10 operations and their results, with a method to view the history.
```

### Segment 4: Agent Mode Teaser (17:00 - 25:00)

Switch to **Agent** mode in the Copilot Chat dropdown, then paste:

```text
Create a complete student grade management system with:
1. A Student class with name, student_id, and a list of grades
2. A GradeBook class that manages multiple students
3. Methods to add grades, calculate averages, find top students, and generate a report
4. A main.py that demonstrates the system with sample data
5. Unit tests in a separate test file

Create all files in a new student_grades/ folder.
```

---

## Session B: "Code Quality Edition"

### Segment 3: Code Review with Chat (8:00 - 18:00)

#### 3a. Initial Review

Open `setup/code_for_review.py`, select all code, then paste in Chat:

```text
Review this code for bugs, security issues, and code quality problems. List every issue you find with its severity (critical, high, medium, low).
```

#### 3b. Fix SQL Injection

```text
Fix the SQL injection vulnerability in the get_user_data function. Use parameterized queries.
```

#### 3c. Fix Hardcoded Password

```text
Fix the hardcoded password issue. Use environment variables with a fallback, and add proper password hashing.
```

#### 3d. Fix Performance

```text
The find_slow_duplicates function is O(n^2). Rewrite it to be O(n) using a more efficient approach.
```

#### 3e. Fix Error Handling

> Skip this prompt if running short on time.

```text
Replace the bare except clause in process_data with specific exception handling and proper logging.
```

### Segment 4: Agent Mode Teaser (18:00 - 25:00)

Switch to **Agent** mode in the Copilot Chat dropdown, then paste:

```text
Fix ALL the issues in this file:
1. Fix the SQL injection vulnerability with parameterized queries
2. Remove the hardcoded password and use environment variables
3. Replace the bare except with proper exception handling and logging
4. Optimize the O(n^2) function to O(n)
5. Add input validation to all functions
6. Add proper type hints throughout
7. Add comprehensive docstrings

Apply all fixes and explain each change you made.
```

---

## Backup Prompts

Use these if the primary prompts produce unexpected results.

### Simpler Chat Prompt

```text
What does this function do? Explain it line by line.
```

### Simpler Review Prompt

```text
What security issues do you see in this code?
```

### Simpler Agent Prompt

```text
Create a simple Student class with name and grades, and a method to calculate the average grade. Put it in a new file called student.py.
```
