
# 02 - Setup and Configuration

Setting up GitHub Copilot correctly is crucial for maximizing its effectiveness. This comprehensive guide will walk you through the installation process, configuration options, and initial setup to ensure you get the most out of your AI pair programming experience.

## Prerequisites

Before installing GitHub Copilot, ensure you have the following:

### GitHub Account and Subscription

GitHub Copilot requires an active subscription. As of 2024, GitHub offers several subscription tiers:

- **GitHub Copilot Individual**: $10/month or $100/year for individual developers
- **GitHub Copilot Business**: $19/month per user for organizations
- **GitHub Copilot Enterprise**: $39/month per user with additional enterprise features

Students, teachers, and maintainers of popular open-source projects may be eligible for free access through GitHub's education and open-source programs [1].

### Supported Editors

GitHub Copilot is available for multiple editors:

- **Visual Studio Code** (Primary focus of this guide)
- **Visual Studio**
- **Neovim**
- **JetBrains IDEs** (IntelliJ IDEA, PyCharm, WebStorm, etc.)

## Installing GitHub Copilot in VS Code

### Step 1: Install Visual Studio Code

If you haven't already, download and install VS Code from the official website [2]. VS Code is free and available for Windows, macOS, and Linux.

### Step 2: Install the GitHub Copilot Extension

1. Open VS Code
2. Click on the Extensions icon in the Activity Bar (or press `Ctrl+Shift+X`)
3. Search for "GitHub Copilot"
4. Click "Install" on the official GitHub Copilot extension by GitHub
5. You may also want to install "GitHub Copilot Chat" for conversational AI assistance

### Step 3: Sign in to GitHub

After installation, you'll need to authenticate:

1. VS Code will prompt you to sign in to GitHub
2. Click "Sign in to GitHub" 
3. This will open your browser to complete the authentication
4. Authorize the GitHub Copilot extension
5. Return to VS Code to complete the setup

## Configuration Options

### Basic Settings

Access Copilot settings through:
- **Command Palette**: `Ctrl+Shift+P` → "Preferences: Open Settings"
- **Menu**: File → Preferences → Settings
- Search for "copilot" to find all related settings

Key configuration options include:

#### Enable/Disable Copilot
```json
{
    "github.copilot.enable": {
        "*": true,
        "yaml": false,
        "plaintext": false
    }
}
```

This setting allows you to enable or disable Copilot globally or for specific file types.

#### Inline Suggestions
```json
{
    "github.copilot.inlineSuggest.enable": true
}
```

Controls whether Copilot shows inline suggestions as you type.

#### Tab Completion
```json
{
    "editor.tabCompletion": "on"
}
```

Enables tab completion for better integration with Copilot suggestions.

### Advanced Configuration

#### Suggestion Delay
```json
{
    "github.copilot.inlineSuggest.delay": 10
}
```

Adjusts the delay (in milliseconds) before Copilot shows suggestions. Lower values provide faster suggestions but may be more distracting.

#### Language-Specific Settings

You can configure Copilot differently for different programming languages:

```json
{
    "[python]": {
        "github.copilot.enable": true
    },
    "[javascript]": {
        "github.copilot.enable": true
    },
    "[markdown]": {
        "github.copilot.enable": false
    }
}
```

## Keyboard Shortcuts

Familiarize yourself with these essential keyboard shortcuts:

| Action | Windows/Linux | macOS |
|--------|---------------|-------|
| Accept suggestion | `Tab` | `Tab` |
| Dismiss suggestion | `Esc` | `Esc` |
| Next suggestion | `Alt + ]` | `Option + ]` |
| Previous suggestion | `Alt + [` | `Option + [` |
| Open Copilot | `Ctrl + I` | `Cmd + I` |
| Trigger suggestion | `Alt + \` | `Option + \` |

### Customizing Shortcuts

You can customize these shortcuts through:
1. `Ctrl+Shift+P` → "Preferences: Open Keyboard Shortcuts"
2. Search for "copilot"
3. Click the pencil icon next to any command to change its shortcut

## Workspace Configuration

### .vscode/settings.json

For project-specific settings, create a `.vscode/settings.json` file in your project root:

```json
{
    "github.copilot.enable": {
        "*": true,
        "yaml": false
    },
    "github.copilot.inlineSuggest.enable": true,
    "editor.suggestSelection": "first",
    "editor.tabCompletion": "on"
}
```

### .copilotignore File

Create a `.copilotignore` file in your project root to exclude certain files or directories from Copilot's context:

```
# Ignore sensitive files
.env
config/secrets.py

# Ignore large data files
data/
*.csv
*.json

# Ignore generated files
build/
dist/
```

## Optimizing Performance

### Memory and CPU Usage

Copilot can be resource-intensive. To optimize performance:

1. **Close unnecessary files**: Copilot considers open files for context
2. **Limit workspace size**: Large workspaces can slow down suggestions
3. **Adjust suggestion frequency**: Increase the delay for suggestions if needed

### Network Considerations

Copilot requires an internet connection to function. For optimal performance:

- Ensure stable internet connectivity
- Consider network latency when working remotely
- Be aware that suggestions are sent to GitHub's servers

## Troubleshooting Common Issues

### Authentication Problems

If you're having trouble signing in:

1. Check your GitHub Copilot subscription status
2. Try signing out and back in: `Ctrl+Shift+P` → "GitHub Copilot: Sign Out"
3. Clear VS Code's authentication cache
4. Restart VS Code

### No Suggestions Appearing

If Copilot isn't showing suggestions:

1. Verify the extension is enabled
2. Check if Copilot is enabled for the current file type
3. Ensure you're connected to the internet
4. Try triggering suggestions manually with `Alt + \`

### Performance Issues

If Copilot is running slowly:

1. Close unnecessary files and folders
2. Increase the suggestion delay
3. Disable Copilot for large files
4. Restart VS Code

## Privacy and Security Considerations

### Data Handling

Understanding how your code is processed:

- Code snippets are sent to GitHub's servers for processing
- GitHub states that your code is not stored or used to train models
- Telemetry data may be collected for service improvement

### Enterprise Considerations

For enterprise users:

- Review your organization's policies on AI tools
- Consider using GitHub Copilot Business for additional controls
- Implement code review processes for AI-generated code
- Be aware of intellectual property implications

## Best Practices for Setup

### Development Environment

1. **Keep VS Code updated**: Ensure you're using the latest version
2. **Regular extension updates**: Keep the Copilot extension current
3. **Backup settings**: Export your VS Code settings for consistency across machines

### Team Collaboration

When working in teams:

1. **Standardize settings**: Share workspace configurations
2. **Document Copilot usage**: Include guidelines in your team's coding standards
3. **Code review processes**: Establish practices for reviewing AI-generated code

## Conclusion

Proper setup and configuration of GitHub Copilot is essential for a productive development experience. Take time to customize the settings according to your preferences and workflow. Remember that configuration is an iterative process – adjust settings as you become more familiar with Copilot's capabilities and your own usage patterns.

In the next section, we'll explore basic usage patterns and start with hands-on exercises to help you become comfortable with GitHub Copilot's core features.

## References

[1] GitHub Copilot Pricing. GitHub. [https://github.com/features/copilot](https://github.com/features/copilot)
[2] Visual Studio Code. Microsoft. [https://code.visualstudio.com/](https://code.visualstudio.com/)

