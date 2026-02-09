# Intro to GitHub Copilot -- 30-Minute Beginner Presentations

## Overview

Two independent 30-minute sessions designed for audiences with **no prior Copilot experience**. Pick one per day, or run both on separate days for different groups.

| Session | Theme | Core Message | Key Demo |
|---------|-------|-------------|----------|
| **A: Productivity Edition** | Generate code faster | "Copilot makes you faster" | Chat: explain, test, enhance |
| **B: Code Quality Edition** | Write better code | "Copilot makes you better" | Chat: review, fix, secure |

Both sessions share the same opening (talking points + inline completions) and close with an Agent Mode teaser.

**Duration**: 30 minutes each
**Complexity**: Beginner
**Best For**: First-time Copilot audiences, team onboarding, lunch-and-learn sessions

---

## Prerequisites

- GitHub Copilot subscription (Individual, Business, or Enterprise)
- VS Code with **GitHub Copilot** and **Copilot Chat** extensions installed
- Python 3.8+ installed
- Internet connection

---

## Quick Setup (2 minutes before either session)

1. Open VS Code in the `demo/intro/` folder
2. Open `setup/starter_functions.py` in a tab
3. Open `setup/calculator.py` (Session A) or `setup/code_for_review.py` (Session B) in a second tab
4. Open `prompts.md` in a third tab (for copy-paste during the demo)
5. Open Copilot Chat: `Ctrl/Cmd + Shift + I`
6. Test: type "Hello" in Chat to verify Copilot is responding
7. Increase font size: `Ctrl/Cmd + =` a few times for visibility

---

## Session A: "Productivity Edition" (30 minutes)

### Segment 1: What is Copilot? (0:00 - 3:00)

**No slides needed** -- talk while VS Code is visible.

Use the talking points from [speaker_notes.md](speaker_notes.md):

- **Opening hook**: "Autocomplete on your phone, but for code"
- **Three modes**: Inline completions, Chat, Agent Mode
- **What it's NOT**: Not a replacement, not always right, not reading your private code
- **Why it matters**: 55% faster, fewer context switches, great for learning

### Segment 2: Live -- Inline Completions (3:00 - 9:00)

1. **Open** `setup/starter_functions.py`
2. **Show the file**: "These functions have signatures and docstrings but no code"
3. **calculate_average**: Place cursor after `pass`, delete `pass`, start typing `total = ` -- pause and let ghost text appear. Press Tab.
   - Say: "I only wrote the function name and docstring. Copilot figured out the implementation."
4. **find_duplicates**: Place cursor after `pass`, delete `pass`, just wait -- Copilot should suggest without any typing.
   - Say: "It reads the docstring and examples to understand what we want."
5. **is_palindrome**: Same approach. Start with `cleaned =` and let Copilot complete.
6. **Student class**: Type `self.name` in `__init__` and let Copilot fill the rest, then move to `add_grade` and `get_average`.
   - Say: "It understands the class attributes from the docstring and fills in all the methods."

**Key takeaway**: "Copilot reads your intent from names, docstrings, and comments."

### Segment 3: Live -- Copilot Chat (9:00 - 17:00)

1. **Open** `setup/calculator.py`
2. **Run it**: `python setup/calculator.py` in terminal to show it works
3. **Select all code**, open Chat

#### 3a. Explain Code (2 min)

Paste from [prompts.md](prompts.md):
> "Explain what this Calculator class does, including each method."

- Read the response aloud. Point out how clear and structured it is.

#### 3b. Add Error Handling (3 min)

Paste:
> "Add error handling to the divide method to handle division by zero gracefully, and add input validation to all methods to ensure arguments are numbers."

- Show the diff. Accept the changes. Run the code again.

#### 3c. Generate Tests (3 min)

Paste:
> "Generate comprehensive unit tests for this Calculator class using pytest."

- Show the generated test file. Run: `python -m pytest` (if pytest is installed) or just review the tests.

#### 3d. Add History Feature (optional, if time permits)

Paste:
> "Add a calculation history feature..."

- Accept and show the enhanced class.

**Key takeaway**: "Chat understands the entire file. You can explain, improve, test, and enhance -- all through conversation."

### Segment 4: Live -- Agent Mode Teaser (17:00 - 25:00)

1. **Switch** to Agent mode using the mode dropdown in Copilot Chat
2. **Build anticipation**: "Everything so far worked on one file. Now watch what Agent Mode can do."
3. **Paste** the Agent Mode prompt from [prompts.md](prompts.md):
   > "Create a complete student grade management system with..."
4. **Watch Copilot work**:
   - Point out the planning step: "See how it plans the structure first?"
   - Point out file creation: "It's creating multiple files with correct imports"
   - Point out consistency: "All files follow the same patterns"
5. **Walk through results** briefly -- open 2-3 generated files
6. **Run the code** if time permits

**Key takeaway**: "Agent Mode goes beyond completion -- it builds entire systems from a description."

### Segment 5: Q&A (25:00 - 30:00)

- See [speaker_notes.md](speaker_notes.md) for common questions and prepared answers
- Ask: "What would you want to try first with Copilot?"

---

## Session B: "Code Quality Edition" (30 minutes)

### Segment 1: What is Copilot? (0:00 - 3:00)

Same as Session A. Use talking points from [speaker_notes.md](speaker_notes.md).

### Segment 2: Live -- Inline Completions (3:00 - 8:00)

Same as Session A but slightly shorter. Do:

1. **calculate_average** -- full walkthrough with `total =` hint
2. **is_palindrome** -- show Copilot suggesting without any typing
3. **Skip** find_duplicates and Student class to save time

Optionally show: delete a docstring, then undo -- point out how the suggestion changes without the docstring context.

**Key takeaway**: Same as Session A.

### Segment 3: Live -- Code Review with Chat (8:00 - 18:00)

1. **Open** `setup/code_for_review.py`
2. **Scroll through slowly**: "This code has problems. Can you spot any?"
   - Give the audience 30 seconds to look. Some will notice the hardcoded password.
3. **Select all code**, open Chat

#### 3a. Initial Review (3 min)

Paste from [prompts.md](prompts.md):
> "Review this code for bugs, security issues, and code quality problems. List every issue you find with its severity."

- Read through the findings. Point out: "It found the SQL injection, the hardcoded password, the O(n^2) loop, the bare except, AND the missing validation. That's five issues in seconds."

#### 3b. Fix SQL Injection (2 min)

Paste:
> "Fix the SQL injection vulnerability in the get_user_data function. Use parameterized queries."

- Show the diff: f-string replaced with `?` placeholder. Accept.

#### 3c. Fix Hardcoded Password (2 min)

Paste:
> "Fix the hardcoded password issue. Use environment variables with a fallback, and add proper password hashing."

- Show the diff. Point out `os.environ.get()` pattern.

#### 3d. Fix Performance (2 min)

Paste:
> "The find_slow_duplicates function is O(n^2). Rewrite it to be O(n) using a more efficient approach."

- Show the diff: nested loop replaced with a set-based approach. Say: "From O(n^2) to O(n) -- that matters when you have a million items."

#### 3e. Fix Error Handling (optional, if time permits)

Paste:
> "Replace the bare except clause in process_data with specific exception handling and proper logging."

**Key takeaway**: "Copilot is a code reviewer that never gets tired and catches everything from security vulnerabilities to performance issues."

### Segment 4: Live -- Agent Mode Teaser (18:00 - 25:00)

1. **Switch** to Agent mode using the mode dropdown
2. **Set the scene**: "We just fixed issues one by one. What if we could fix everything at once?"
3. **Paste** the Agent Mode prompt from [prompts.md](prompts.md):
   > "Fix ALL the issues in this file..."
4. **Watch Copilot work**:
   - Point out: "It's applying all seven fixes in a single pass"
   - Show the diff when done: every flaw addressed
5. **Run the fixed code** if time permits

**Key takeaway**: "Agent Mode can remediate entire files autonomously -- from security fixes to performance improvements."

### Segment 5: Q&A (25:00 - 30:00)

Same as Session A. See [speaker_notes.md](speaker_notes.md).

---

## Troubleshooting

### If Copilot isn't responding

- Check status icon (bottom-right) shows "Copilot: ON"
- Restart VS Code
- Check internet connection
- Sign out and back in to GitHub

### If inline completions don't appear

- Ensure you're inside a function body with good context (docstring above)
- Try typing a few characters to trigger suggestions
- Check Settings: `"github.copilot.enable": { "python": true }`

### If Agent Mode isn't available

- Requires latest VS Code and Copilot Chat extension
- Fallback: use regular Chat with the same prompt (works, just doesn't create files)
- Explain the concept and show the prompt

### If running short on time

- **Session A**: Skip prompt 3d (history feature), trim Agent Mode to 5 minutes
- **Session B**: Skip prompt 3e (error handling), trim Agent Mode to 5 minutes
- Q&A can always be shortened to 2-3 minutes

---

## Success Metrics

After either session, your audience should understand:

- Copilot suggests code from function names, docstrings, and context
- Copilot Chat can explain, improve, test, and review code
- Agent Mode can build or fix entire systems from a description
- Copilot is an intelligent development partner, not just autocomplete

---

## Files in This Folder

| File | Purpose |
|------|---------|
| [README.md](README.md) | This file -- master guide for both sessions |
| [prompts.md](prompts.md) | All copy-paste prompts, labeled by session |
| [speaker_notes.md](speaker_notes.md) | Talking points, engagement tips, backup plans, Q&A |
| [setup/starter_functions.py](setup/starter_functions.py) | Partial functions for inline completion demo (both sessions) |
| [setup/calculator.py](setup/calculator.py) | Working calculator for Chat demos (Session A) |
| [setup/code_for_review.py](setup/code_for_review.py) | Intentionally flawed code for review demo (Session B) |
