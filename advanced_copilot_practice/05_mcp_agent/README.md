# Exercise 5 – Agent Mode with MCP

This exercise demonstrates Copilot's agent capabilities via the **Model Context Protocol**.

## Setup

1. Install the *GitHub Copilot Chat* extension (Insiders or 1.5+).
2. Open **.vscode/mcp.json**. This configuration registers the built‑in GitHub MCP server.
3. In VS Code, open the Copilot **Chat** panel and switch to **Agent** mode.
4. When prompted, grant permission for the GitHub tool.

## Task

There's an open issue described in **ISSUES.md**.  
Ask Copilot Agent to **fix the bug and create a pull request**:

```text
Fix issue #1 in bugfix/buggy_code.py and commit the changes.
```

Copilot will plan steps, ask for confirmation, run the edits, and create a branch.  
Review each step and approve when appropriate.

> You can also experiment with the "fetch" MCP server:  
> `Fetch https://api.github.com/repos/octocat/Hello-World`
