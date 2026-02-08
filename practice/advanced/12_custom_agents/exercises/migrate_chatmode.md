# Exercise: Migrate .chatmode.md to .agent.md

## Objective

Convert a legacy `.chatmode.md` file to the new `.agent.md` format, adding handoffs and sub-agent control.

---

## Starting Material: Legacy Chat Mode

Here is a `.chatmode.md` file that was used for code reviews:

```yaml
---
name: reviewer
description: Reviews code for quality and best practices
tools: ['readFile', 'search']
---

You are a code reviewer. When asked to review code:
1. Read the specified files
2. Check for code quality issues
3. Look for potential bugs
4. Suggest improvements
5. Rate the overall code quality (1-10)
```

## Step 1: Rename the File

Rename from `reviewer.chatmode.md` to `reviewer.agent.md`

The file can stay in the same location, but the recommended location is now `.github/agents/`.

## Step 2: Enhance with Agent-Specific Properties

Add the new capabilities that `.agent.md` supports:

```yaml
---
name: reviewer
description: Reviews code for quality, performance, and best practices
tools: ['readFile', 'search', 'listFiles']
agents: []                    # NEW: don't spawn sub-agents
model: claude-sonnet-4        # NEW: specify preferred model
handoffs:                     # NEW: workflow transitions
  - target: implement
    label: "Fix these issues"
    prompt: "Address all the code quality issues identified in the review above."
    autoSubmit: false
  - target: plan
    label: "Plan the fixes"
    prompt: "Create a plan to address the issues found in this review."
    autoSubmit: false
---
```

## Step 3: Update the Instructions

Enhance the body to take advantage of the new format:

```markdown
You are a **Code Review Agent**. Review code for quality, performance, and best practices.

## Review Process

1. Use `search` to find all files related to the review target
2. Use `readFile` to examine each file thoroughly
3. Use `listFiles` to understand the project structure

## Review Categories

- **Code Quality**: Naming, structure, DRY principle, SOLID principles
- **Performance**: N+1 queries, unnecessary iterations, memory leaks
- **Error Handling**: Missing try/catch, unhandled promises, silent failures
- **Testing**: Missing tests, insufficient coverage, brittle tests
- **Documentation**: Missing docstrings, outdated comments, unclear README

## Output Format

For each finding:
- **Category**: Quality / Performance / Error Handling / Testing / Docs
- **Severity**: Critical / Warning / Suggestion
- **File:Line**: Specific location
- **Issue**: What's wrong
- **Recommendation**: How to fix it

End with an **Overall Score** (1-10) and **Summary**.
```

## Step 4: Test the Migration

1. Place the new `.agent.md` file in `.github/agents/`
2. Open the Chat view in VS Code
3. Select the **reviewer** agent from the dropdown
4. Ask it to review a file in your project
5. Verify the handoff buttons appear after the review

## What Changed

| Aspect | .chatmode.md | .agent.md |
|--------|-------------|-----------|
| Handoffs | Not supported | Sequential workflow transitions |
| Sub-agent control | Not supported | `agents` property |
| Model selection | Not supported | `model` property (single or array) |
| MCP servers | Not supported | `mcp-servers` property |
| Org sharing | Limited | Full support via policy |
| User-invokable control | Not supported | `user-invokable` property |

## Challenge

Create a second agent (`quick-check.agent.md`) that does a lightweight review (only critical issues) and has a handoff to the full `reviewer` agent for deeper analysis.
