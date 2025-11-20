# Exercise 5 – Agent Mode, Copilot Coding Agent & MCP

This exercise demonstrates Copilot's autonomous agent capabilities, including Agent Mode in VS Code and the Copilot Coding Agent for GitHub issues.

## 🆕 What's New in 2024/2025

GitHub Copilot now offers multiple agent capabilities:

1. **Agent Mode** (VS Code): Autonomous iteration, error fixing, and multi-step task completion
2. **Copilot Coding Agent** (GitHub): Assign entire issues to Copilot for autonomous resolution
3. **Model Context Protocol (MCP)**: Secure integration with repositories and external services
4. **Self-Healing**: Copilot recognizes and fixes its own errors
5. **Next Edit Suggestions**: Context-aware predictions for your next code change

## Setup

### For Agent Mode (VS Code)

1. Install **VS Code Insiders** (required for latest Agent Mode features)
2. Install the **GitHub Copilot Chat** extension (version 1.5+)
3. Enable Agent Mode in settings:
   - Open Settings (`Ctrl+,` or `Cmd+,`)
   - Search for "GitHub Copilot Agent"
   - Enable "GitHub Copilot > Agent: Enabled"
4. Open the Copilot **Chat** panel (`Ctrl+Shift+I` or `Cmd+Shift+I`)
5. Look for the Agent Mode toggle in the Chat interface

### For Copilot Coding Agent (GitHub)

1. Ensure your repository has a **GitHub Copilot Pro, Business, or Enterprise** subscription
2. Navigate to any GitHub issue in your repository
3. Look for the "Assign to Copilot" option in the issue interface

### MCP Configuration (Optional)

1. Create or open `.vscode/mcp.json` in your workspace
2. This configuration registers the built‑in GitHub MCP server
3. When prompted in Agent Mode, grant permission for the GitHub tool

## Task 1: Agent Mode in VS Code

There's an open issue described in **ISSUES.md**.
Ask Copilot Agent to **fix the bug autonomously**:

```text
Fix issue #1 in bugfix/buggy_code.py. Analyze the code, identify the problem,
implement a fix, and verify it works correctly.
```

**What to observe:**
- Copilot will plan multiple steps
- It will iterate on its own solution if the first attempt has issues
- It can run terminal commands and check results
- It will ask for confirmation at key decision points

**Advanced prompt:**
```text
Review bugfix/buggy_code.py, identify all bugs, fix them, add error handling,
and write unit tests to prevent regression. Create a commit with a descriptive message.
```

## Task 2: Copilot Coding Agent (GitHub Issues)

If you have access to GitHub Copilot Coding Agent:

1. Create a GitHub issue with a clear description:
   ```
   Title: Add input validation to user registration

   Description:
   The user registration function needs validation for:
   - Email format validation
   - Password strength requirements (min 8 chars, uppercase, number)
   - Username uniqueness check

   File: bugfix/buggy_code.py
   ```

2. Assign the issue to Copilot:
   - Click "Assign to Copilot" in the issue
   - Copilot will analyze the request and create a work plan
   - Review the plan and approve

3. Copilot will:
   - Create a new branch
   - Make the necessary code changes
   - Run tests (if configured)
   - Open a pull request with detailed description
   - Request your review

4. Review the PR, provide feedback, and merge when satisfied

## Task 3: Multi-Step Autonomous Development

Test Agent Mode's ability to handle complex, multi-step tasks:

```text
Create a new feature in bugfix/buggy_code.py:
1. Add a password reset function that generates a secure token
2. Add an email notification function (mock implementation)
3. Add appropriate error handling
4. Write comprehensive unit tests
5. Update any relevant documentation
```

Watch how Copilot:
- Breaks down the task into subtasks
- Implements each subtask sequentially
- Tests its own work
- Fixes errors it encounters
- Iterates to improve the solution

## Task 4: Error Recovery and Self-Healing

Introduce an intentional error and see Agent Mode recover:

```text
Refactor bugfix/buggy_code.py to use a new database connection class.
Use the class 'DatabaseConnector' even though it doesn't exist yet.
```

**Expected behavior:**
- Copilot will attempt the refactoring
- Encounter an error about the missing class
- Recognize the error
- Create the DatabaseConnector class
- Complete the refactoring successfully

## Task 5: MCP Integration

If you have MCP configured, test external integrations:

```text
Fetch the latest issue from GitHub repository and analyze its complexity.
Then, estimate how many lines of code would be needed to resolve it.
```

This demonstrates MCP's ability to:
- Connect to external services (GitHub)
- Retrieve real-time data
- Process and analyze information
- Provide informed responses

## Best Practices for Agent Mode

1. **Be Specific**: Clear, detailed prompts get better results
2. **Review Plans**: Always review Copilot's work plan before approving
3. **Iterate**: If the result isn't perfect, provide feedback and let it try again
4. **Set Boundaries**: Specify files to modify or avoid
5. **Monitor Progress**: Watch the agent's actions and intervene if needed
6. **Test Thoroughly**: Always test agent-generated code before deploying

## Troubleshooting

**Agent Mode not available?**
- Ensure you're using VS Code Insiders
- Update GitHub Copilot Chat extension to latest version
- Check your subscription includes Agent Mode access

**Copilot Coding Agent not showing?**
- Verify repository has appropriate Copilot subscription
- Check you have write access to the repository
- Feature may be in gradual rollout - check GitHub's feature status

**Agent making unexpected changes?**
- Be more explicit in your instructions
- Specify which files can/cannot be modified
- Review and reject plans that don't align with your intent

## Learning Outcomes

After completing these exercises, you should understand:
- How to leverage Agent Mode for autonomous development
- When to use Copilot Coding Agent vs. manual development
- How to provide effective prompts for complex tasks
- How agents handle errors and iterate on solutions
- The power and limitations of autonomous AI coding

## Next Steps

- Explore **Copilot Edits** for multi-file refactoring (Module 06)
- Learn about **Multi-Model Support** for task optimization (Module 07)
- Try building your own **Copilot Extensions** (Module 08)
