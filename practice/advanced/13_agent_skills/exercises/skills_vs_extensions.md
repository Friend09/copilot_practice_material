# Exercise: Agent Skills vs Copilot Extensions

This guide compares Agent Skills (SKILL.md) with Copilot Extensions (Module 08) and walks you through migrating from the deprecated Skillsets format to the new Agent Skills standard.

---

## When to Use Each

### Agent Skills (SKILL.md)

Use Agent Skills when you need to:

- Provide **domain-specific instructions** that Copilot should follow for certain tasks
- Include **scripts and resource files** alongside instructions
- Share expertise **portably** across VS Code, Copilot CLI, and Copilot Coding Agent
- Customize behavior **without writing server-side code**
- Contribute to the **open standard** ecosystem at agentskills.io

**Examples:**
- A Python code quality checklist with an automated linting script
- API design conventions with an OpenAPI template
- A database migration guide with SQL schema templates

### Copilot Extensions (Module 08)

Use Copilot Extensions when you need to:

- Access **external APIs or services** (databases, monitoring, CI/CD)
- Perform **real-time data retrieval** from third-party systems
- Implement **complex logic** that goes beyond static instructions
- Build **interactive tools** with custom UI or response formatting
- Provide capabilities that require **authentication** with external services

**Examples:**
- A Sentry extension that fetches real error data from your monitoring system
- A database extension that queries production schema information
- A deployment extension that triggers and monitors CI/CD pipelines

---

## Feature Comparison

| Feature | Agent Skills (SKILL.md) | Copilot Extensions |
|---------|------------------------|--------------------|
| **Format** | Markdown files with YAML frontmatter | GitHub App / API endpoint |
| **Hosting** | Local files (no server needed) | Requires a server or serverless function |
| **Activation** | Automatic (semantic matching) | Explicit (`@extension-name`) |
| **Portability** | Open standard (VS Code, CLI, Coding Agent) | GitHub Copilot Chat only |
| **Content** | Instructions, scripts, resources | Dynamic responses from external systems |
| **Setup effort** | Create a folder with SKILL.md | Build, deploy, and register an app |
| **Data access** | Static files only | Real-time API calls |
| **Authentication** | None needed | OAuth, API keys, tokens |
| **Sharing** | Copy a directory | Publish to GitHub Marketplace |
| **Customization** | Edit the Markdown directly | Fork/configure the app |
| **Context cost** | Progressive disclosure (efficient) | Response-based (varies) |
| **Maintenance** | Update text files | Maintain running service |
| **Open standard** | Yes (agentskills.io) | No (GitHub-specific) |

---

## Decision Matrix

Use this matrix to decide which approach fits your use case:

| Scenario | Recommended Approach |
|----------|---------------------|
| "I want Copilot to follow our coding standards" | **Agent Skill** |
| "I need Copilot to query our Jira board" | **Copilot Extension** |
| "I want to share our API design guidelines" | **Agent Skill** |
| "I need Copilot to run our test suite and report results" | **Agent Skill** (with script) |
| "I need Copilot to access live production metrics" | **Copilot Extension** |
| "I want to enforce our PR review checklist" | **Agent Skill** |
| "I need Copilot to interact with our internal documentation wiki" | **Copilot Extension** |
| "I want to distribute linting rules with example scripts" | **Agent Skill** |
| "I need real-time stock data in my Copilot chat" | **Copilot Extension** |
| "I want portable instructions that work in CLI and VS Code" | **Agent Skill** |

---

## Migration: Skillsets to Agent Skills

The older "Skillsets" feature (defined in Copilot Extension configuration) has been superseded by Agent Skills. If you have existing Skillset definitions, here is how to migrate them.

### What Changed

| Aspect | Old Skillsets | New Agent Skills |
|--------|--------------|-----------------|
| **Definition** | JSON in Copilot Extension config | SKILL.md file with YAML frontmatter |
| **Location** | Part of a Copilot Extension app | `.github/skills/` directory |
| **Format** | JSON schema | Markdown with YAML frontmatter |
| **Dependencies** | Required a GitHub App | Standalone (no app needed) |
| **Portability** | Copilot Chat only | Open standard (VS Code, CLI, Coding Agent) |
| **Activation** | Via `@extension-name` | Automatic semantic matching |

### Migration Steps

1. **Identify your existing Skillset definitions**

   Old Skillsets were defined in your Copilot Extension's configuration, often as a JSON file:

   ```json
   {
     "skillsets": [
       {
         "name": "code-review",
         "description": "Reviews code for quality and security issues",
         "instructions": "When reviewing code, check for...",
         "tools": ["readFile", "search"]
       }
     ]
   }
   ```

2. **Create the skill directory**

   ```bash
   mkdir -p .github/skills/code-review
   ```

3. **Convert the JSON definition to SKILL.md**

   Map the JSON fields to the SKILL.md format:

   ```yaml
   ---
   name: code-review
   description: Reviews code for quality and security issues. Use this skill when asked to review code, check for bugs, or evaluate code quality.
   ---

   # Code Review Skill

   When reviewing code, check for:

   ## Security
   - SQL injection vulnerabilities
   - Cross-site scripting (XSS)
   - Authentication bypass risks

   ## Quality
   - Missing error handling
   - Unused variables and imports
   - Code duplication

   ## Performance
   - N+1 query patterns
   - Unnecessary memory allocations
   - Missing caching opportunities
   ```

   **Key differences in the conversion:**
   - The `instructions` string becomes the Markdown body (expand it with proper formatting)
   - The `tools` array is no longer specified in the skill (tool access is managed at the agent level via `.agent.md`)
   - The `description` should be more detailed to improve semantic matching

4. **Move any associated resources**

   If your Skillset referenced external files, templates, or scripts, move them into the skill directory:

   ```
   .github/skills/code-review/
     SKILL.md
     resources/
       checklist.md
       security_patterns.md
     scripts/
       lint_check.sh
   ```

   Update the SKILL.md body to reference these files with relative paths.

5. **Test the migrated skill**

   - Open VS Code Chat in Agent mode
   - Ask a question that should trigger the skill
   - Verify that the response follows your skill's instructions
   - Compare the behavior with the old Skillset-based Extension

6. **Remove the old Skillset definition**

   Once confirmed working, remove the old Skillset configuration from your Copilot Extension app.

---

## Hands-On Exercise: Convert a Skillset to SKILL.md

### Starting Material

Here is a sample Skillset definition from an old Copilot Extension configuration:

```json
{
  "skillsets": [
    {
      "name": "testing-standards",
      "description": "Enforces project testing standards and generates tests",
      "instructions": "When writing tests: use pytest framework, follow AAA pattern (Arrange-Act-Assert), mock external dependencies, aim for 80% coverage, use descriptive test names following test_<function>_<scenario>_<expected> format, group tests by module in test_ prefixed files.",
      "tools": ["readFile", "editFiles", "runTerminalCommand"]
    }
  ]
}
```

### Your Task

1. Create the directory `.github/skills/testing-standards/`

2. Create a `SKILL.md` file that converts the above JSON into the Agent Skills format

3. Expand the single `instructions` string into a well-structured Markdown body with:
   - Clear section headings
   - Specific examples for each guideline
   - A sample test file demonstrating the conventions

4. Add a `resources/` directory with a `test_template.py` file that serves as a starter template

5. Test the skill by asking Copilot: "Write tests for this function following our standards"

### Expected SKILL.md Structure

Your converted file should look something like this:

```yaml
---
name: testing-standards
description: Enforces project testing standards and generates test files. Use this skill when writing tests, reviewing test code, or setting up test infrastructure. Follows pytest conventions with AAA pattern.
---

# Testing Standards Skill

Follow these standards when writing or reviewing tests.

## Framework

Use **pytest** for all test files. Do not use unittest directly.

## Test File Organization

- Place test files alongside source files or in a `tests/` directory
- Name test files with a `test_` prefix: `test_user_service.py`
- Group related tests in classes: `class TestUserCreation:`

## Naming Convention

Follow the pattern: `test_<function>_<scenario>_<expected>`

Examples:
- `test_create_user_valid_input_returns_user_dict`
- `test_create_user_duplicate_email_raises_error`
- `test_calculate_total_empty_cart_returns_zero`

## AAA Pattern

Structure every test with Arrange-Act-Assert:

(include a code example here)

## Mocking

- Mock all external dependencies (databases, APIs, file system)
- Use `pytest-mock` or `unittest.mock`
- Prefer `mocker.patch` over `@mock.patch` decorators

## Coverage

- Target 80% code coverage minimum
- Run with: `pytest --cov=src --cov-report=term-missing`
```

### Verification

After creating your skill, verify it works:

1. Open a Python file in your project
2. Open Copilot Chat in Agent mode
3. Ask: "Write tests for the functions in this file"
4. Confirm that Copilot follows the testing standards from your skill (pytest, AAA pattern, naming convention)

---

## Summary

- **Agent Skills** are best for portable, static instructions with optional scripts and resources
- **Copilot Extensions** are best for dynamic, API-connected capabilities requiring a running service
- The two approaches are **complementary**, not competing -- use both when appropriate
- Migrating from old Skillsets to Agent Skills involves converting JSON to SKILL.md format, expanding instructions into structured Markdown, and moving resources into the skill directory
- Agent Skills follow an open standard, making them future-proof and portable across tools
