# GitHub Copilot Troubleshooting Guide

## Common Issues and Solutions

### 1. Installation and Setup Issues

#### Problem: Copilot extension not installing

**Symptoms**: Extension fails to install or shows error messages
**Solutions**:

- Ensure you have the latest version of VS Code
- Check your internet connection
- Try installing from the command line: `code --install-extension GitHub.copilot`
- Clear VS Code extension cache
- Restart VS Code as administrator (Windows)

#### Problem: Authentication failures

**Symptoms**: "Sign in to GitHub" prompts repeatedly appear
**Solutions**:

- Clear browser cache and cookies
- Use incognito/private browsing mode for authentication
- Check if your organization has restrictions on GitHub Apps
- Try signing out and back in: `Ctrl+Shift+P` → "GitHub Copilot: Sign Out"
- Verify your GitHub account has an active Copilot subscription

### 2. Suggestion Issues

#### Problem: No suggestions appearing

**Symptoms**: Copilot doesn't show any code suggestions
**Diagnostic Steps**:

1. Check the Copilot status in VS Code status bar
2. Verify internet connectivity
3. Ensure the file type is supported
4. Check if Copilot is enabled for the current language

**Solutions**:

- Manually trigger suggestions: `Alt + \` (Windows/Linux) or `Option + \` (macOS)
- Check settings: `github.copilot.enable` should be `true`
- Restart the Copilot service: `Ctrl+Shift+P` → "Developer: Reload Window"
- Update the Copilot extension to the latest version

#### Problem: Poor quality or irrelevant suggestions

**Symptoms**: Suggestions don't match your intent or are low quality
**Solutions**:

- Improve your prompts with more specific comments
- Provide examples of expected input/output
- Add more context to your code
- Break complex tasks into smaller, more specific requests
- Use the persona pattern: "You are an expert Python developer..."

#### Problem: Suggestions are too slow

**Symptoms**: Long delays before suggestions appear
**Solutions**:

- Check your internet connection speed
- Close unnecessary files in VS Code
- Increase the suggestion delay: `github.copilot.inlineSuggest.delay`
- Use `.copilotignore` to exclude large directories
- Consider upgrading your internet plan

### 3. Performance Issues

#### Problem: VS Code becomes slow with Copilot enabled

**Symptoms**: Editor lag, high CPU usage, memory consumption
**Solutions**:

- Close unused tabs and files
- Disable Copilot for large files (>1000 lines)
- Exclude node_modules and other large directories with `.copilotignore`
- Increase hardware resources (RAM, CPU)
- Adjust suggestion settings to reduce frequency

#### Problem: High network usage

**Symptoms**: Excessive data consumption, slow internet for other applications
**Solutions**:

- Monitor network usage in Task Manager/Activity Monitor
- Reduce suggestion frequency
- Work offline when possible (Copilot won't work, but you can code)
- Use a wired connection instead of Wi-Fi

### 4. Language and Framework Issues

#### Problem: Poor suggestions for specific languages

**Symptoms**: Copilot works well for Python but poorly for other languages
**Solutions**:

- Ensure the language is officially supported by Copilot
- Add language-specific context in comments
- Include relevant imports and dependencies
- Use language-specific naming conventions
- Provide framework-specific context (e.g., "using React hooks")

#### Problem: Framework-specific code not recognized

**Symptoms**: Copilot doesn't understand your framework patterns
**Solutions**:

- Mention the framework explicitly in comments
- Keep framework documentation files open
- Use standard framework patterns and naming
- Provide examples of the framework's syntax in comments

### 5. Workspace and Context Issues

#### Problem: Copilot ignores related files

**Symptoms**: Suggestions don't consider code in other open files
**Solutions**:

- Ensure related files are open in the same workspace
- Use consistent naming conventions across files
- Keep the workspace size manageable
- Reference other files explicitly in comments

#### Problem: Sensitive data in suggestions

**Symptoms**: Copilot suggests code containing API keys or personal data
**Solutions**:

- Use `.copilotignore` to exclude sensitive files
- Remove sensitive data from your codebase
- Use environment variables for secrets
- Review all suggestions before accepting

### 6. Subscription and Billing Issues

#### Problem: Subscription not recognized

**Symptoms**: "Copilot subscription required" messages
**Solutions**:

- Verify your subscription status on GitHub
- Check if you're signed in with the correct GitHub account
- Contact GitHub support for billing issues
- Ensure your payment method is valid

#### Problem: Organization restrictions

**Symptoms**: Copilot disabled by organization policy
**Solutions**:

- Contact your organization's IT administrator
- Request approval for Copilot usage
- Use a personal GitHub account for learning (if allowed)
- Check organization settings on GitHub

### 7. Enterprise Features Issues

#### Problem: Custom instructions not working

**Symptoms**: AI doesn't follow instructions in `.github/copilot-instructions.md`
**Solutions**:

- Verify the `github.copilot.chat.codeGeneration.useInstructionFiles` setting is enabled
- Check file location: `.github/copilot-instructions.md` or `.github/instructions/`
- Ensure the file has proper Markdown format
- Test with simple, clear instructions first
- Verify file permissions and VS Code can read the file

#### Problem: Prompt files not appearing

**Symptoms**: Prompt files don't show up in chat
**Solutions**:

- Enable the `chat.promptFiles` setting in VS Code
- Check file extension is `.prompt.md`
- Verify file location: `.github/prompts/` or configured location
- Test YAML frontmatter syntax is valid
- Use Command Palette: `Chat: Refresh Prompt Files`

#### Problem: Tool sets not available

**Symptoms**: Custom tool sets don't appear in agent mode
**Solutions**:

- Verify tool set file has `.json` or `.jsonc` extension
- Check JSON syntax is valid
- Ensure tools referenced in set actually exist
- Refresh chat view or restart VS Code
- Check tool set storage location configuration

#### Problem: Chat modes not working

**Symptoms**: Custom chat modes don't appear or function correctly
**Solutions**:

- Verify file extension is `.chatmode.md`
- Check YAML frontmatter syntax
- Ensure referenced tools and instructions exist
- Test with built-in modes first
- Use Command Palette: `Chat: Refresh Chat Modes`

#### Problem: MCP servers not connecting

**Symptoms**: MCP tools unavailable or connection errors
**Solutions**:

- Check `mcp.json` configuration syntax
- Verify server executable exists and has permissions
- Test server standalone outside VS Code
- Check VS Code logs for MCP-specific errors
- Ensure `chat.mcp.enabled` setting is true
- Only use trusted MCP servers (security risk)

### 8. Advanced Troubleshooting

#### Collecting Diagnostic Information

1. Check VS Code version: `Help` → `About`
2. Check Copilot extension version in Extensions panel
3. View Copilot logs: `Ctrl+Shift+P` → "Developer: Show Logs" → "Extension Host"
4. Check network connectivity to GitHub services

#### Resetting Copilot Configuration

1. Sign out of GitHub Copilot
2. Close VS Code completely
3. Clear VS Code settings (backup first):
   - Windows: `%APPDATA%\Code\User\settings.json`
   - macOS: `~/Library/Application Support/Code/User/settings.json`
   - Linux: `~/.config/Code/User/settings.json`
4. Restart VS Code and reconfigure Copilot

#### Network Configuration Issues

If you're behind a corporate firewall:

- Configure proxy settings in VS Code
- Whitelist GitHub domains: `*.github.com`, `api.github.com`
- Contact your network administrator for assistance

### 8. Getting Help

#### Official Support Channels

- GitHub Copilot Documentation: [https://docs.github.com/en/copilot](https://docs.github.com/en/copilot)
- GitHub Support: [https://support.github.com/](https://support.github.com/)
- VS Code Issues: [https://github.com/microsoft/vscode/issues](https://github.com/microsoft/vscode/issues)

#### Community Resources

- GitHub Community Forum
- Stack Overflow (tag: github-copilot)
- Reddit: r/github, r/vscode
- Discord servers for developers

#### Reporting Bugs

When reporting issues, include:

- VS Code version
- Copilot extension version
- Operating system
- Steps to reproduce the issue
- Screenshots or error messages
- Relevant code snippets (without sensitive data)

### 9. Prevention Tips

#### Regular Maintenance

- Keep VS Code and extensions updated
- Regularly clear cache and temporary files
- Monitor system resources
- Review and update `.copilotignore` files
- Validate custom instructions and prompt files regularly
- Back up enterprise feature configurations

#### Best Practices

- Use version control to track changes
- Test Copilot suggestions thoroughly
- Maintain good coding practices
- Keep learning about new Copilot features
- Document team standards in custom instructions
- Share prompt files and tool sets across team
- Review and update chat modes based on workflow changes
- Test MCP servers in isolated environments first

#### Enterprise Configuration Management

- Store `.github/copilot-instructions.md` in version control
- Organize prompt files in `.github/prompts/` directory
- Document tool set configurations for team consistency
- Create standardized chat modes for common workflows
- Maintain MCP server configurations centrally
- Regular training on new enterprise features

Remember: Most Copilot issues are related to configuration, network connectivity, or prompt quality. Start with the basics before moving to advanced troubleshooting steps.
