# Demo 10: Agent Skills Prompts

## Step 2 Prompts -- Creating a Skill from Scratch

### Prompt: Ask Copilot to scaffold a skill

```text
Create a new Agent Skill for Python linting and style checking. The skill should:
1. Have a SKILL.md with proper YAML frontmatter (name, description)
2. Include instructions for checking docstrings, type hints, naming conventions, and import order
3. Reference a lint_check.py script and a style_guide.md resource
4. Follow the .github/skills/ directory convention
```

### Prompt: Refine the skill description

```text
Improve the description field in this SKILL.md so Copilot matches it for questions about
Python code quality, style violations, lint errors, missing docstrings, or naming issues.
```

---

## Step 3 Prompts -- Testing the Skill with Relevant Questions

### Prompt: Trigger skill matching (should activate the lint skill)

```text
Check this Python file for linting issues and style violations. Look for missing docstrings,
bad naming conventions, and incorrect import ordering.
```

### Prompt: Ask a style-specific question

```text
Does this Python code follow our team's style guide? Check naming conventions,
docstring format, and type hint usage.
```

### Prompt: Request a lint script run

```text
Run the linting checks on setup/example_skill/scripts/lint_check.py and report any issues
with docstrings, naming, or import order.
```

---

## Step 4 Prompts -- Verifying Progressive Disclosure Behavior

### Level 1 -- Metadata only (should NOT fully load the skill)

```text
What is the capital of France?
```

> **Expected**: Copilot answers the question normally. The python-lint-style skill is
> indexed but not loaded because the question is unrelated to linting.

### Level 2 -- Full SKILL.md loaded (should load instructions)

```text
I have a Python file with several style issues. Can you review it for compliance
with our linting standards?
```

> **Expected**: Copilot matches the skill description, loads the full SKILL.md body,
> and follows the instructions to check the file.

### Level 3 -- Referenced files accessed (should load scripts/resources)

```text
Run the lint checker script on my Python file and use the team style guide to
evaluate naming conventions and docstring format.
```

> **Expected**: Copilot loads the lint_check.py script and style_guide.md resource
> in addition to the SKILL.md instructions.

---

## Bonus Prompts -- Extending Skills

### Create a second skill

```text
Create an Agent Skill for "Database Migration Review" that checks SQL migration files
for common issues like missing rollback steps, unsafe ALTER TABLE operations,
and missing indexes on foreign keys. Include a SKILL.md and a checklist resource.
```

### Ask Copilot about skill structure

```text
What is the recommended folder structure for an Agent Skill? What fields are
required in the SKILL.md frontmatter?
```
