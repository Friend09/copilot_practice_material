# GitHub Copilot Tips and Tricks

## Quick Reference Guide

### Essential Keyboard Shortcuts

| Action              | Windows/Linux | macOS        | Description                    |
| ------------------- | ------------- | ------------ | ------------------------------ |
| Accept suggestion   | `Tab`         | `Tab`        | Accept the current suggestion  |
| Dismiss suggestion  | `Esc`         | `Esc`        | Dismiss the current suggestion |
| Next suggestion     | `Alt + ]`     | `Option + ]` | Cycle to next suggestion       |
| Previous suggestion | `Alt + [`     | `Option + [` | Cycle to previous suggestion   |
| Trigger suggestion  | `Alt + \`     | `Option + \` | Manually trigger suggestions   |
| Open Copilot Chat   | `Ctrl + I`    | `Cmd + I`    | Open conversational interface  |

### Effective Prompting Patterns

#### 1. The Function Template Pattern

```python
# Create a function that [action] [object] and returns [result]
# Parameters: [list parameters with types]
# Example: [provide usage example]
```

#### 2. The Step-by-Step Pattern

```python
# Function to process user data:
# 1. Validate input format
# 2. Clean and normalize data
# 3. Apply business rules
# 4. Return processed result
```

#### 3. The Example-Driven Pattern

```python
# Convert temperature units
# Example: celsius_to_fahrenheit(0) -> 32
# Example: celsius_to_fahrenheit(100) -> 212
```

### Language-Specific Tips

#### Python

- Use type hints for better suggestions
- Write docstrings to get better function implementations
- Use descriptive variable names
- Leverage Python's built-in functions in comments

#### JavaScript/TypeScript

- Define interfaces/types first
- Use JSDoc comments for better context
- Mention framework (React, Vue, Angular) in comments
- Be specific about async/await patterns

#### HTML/CSS

- Describe the layout structure in comments
- Mention responsive design requirements
- Specify browser compatibility needs
- Include accessibility considerations

### Troubleshooting Common Issues

#### No Suggestions Appearing

1. Check internet connection
2. Verify Copilot subscription is active
3. Ensure extension is enabled for file type
4. Try manual trigger with `Alt + \`
5. Restart VS Code if needed

#### Poor Quality Suggestions

1. Add more context in comments
2. Provide examples of expected output
3. Break complex tasks into smaller parts
4. Use more specific language in prompts
5. Include relevant imports and dependencies

#### Performance Issues

1. Close unnecessary files
2. Use `.copilotignore` for large directories
3. Increase suggestion delay in settings
4. Disable for very large files
5. Clear VS Code cache if needed

### Advanced Techniques

#### Multi-File Context

- Keep related files open in workspace
- Use consistent naming conventions
- Reference other files in comments
- Organize code logically across files

#### Testing with Copilot

```python
# Generate unit tests for the above function
# Include edge cases and error conditions
# Use pytest framework
```

#### Documentation Generation

```python
def complex_function(param1, param2):
    """
    # Copilot will generate comprehensive docstring here
    """
    pass
```

#### Refactoring Assistance

```python
# Refactor this function to use dependency injection
# Extract configuration into separate class
# Improve error handling and logging
```

### Best Practices Checklist

- [ ] Always review generated code before using
- [ ] Test AI-generated functions thoroughly
- [ ] Use version control to track changes
- [ ] Follow your team's coding standards
- [ ] Consider security implications
- [ ] Document your prompting strategies
- [ ] Share effective patterns with team
- [ ] Keep learning and experimenting

### Common Pitfalls to Avoid

1. **Blindly accepting suggestions** - Always review and understand the code
2. **Over-relying on Copilot** - Maintain your coding skills
3. **Ignoring security** - AI code may have vulnerabilities
4. **Poor prompt writing** - Vague prompts lead to poor results
5. **Not testing thoroughly** - AI code needs the same testing as human code
6. **Inconsistent style** - Ensure generated code matches your standards

### Productivity Hacks

#### Quick Function Generation

```python
# [function_name]: [brief description]
# Input: [parameter description]
# Output: [return value description]
```

#### Rapid Prototyping

```python
# Create a simple [type] class with basic CRUD operations
# Include validation and error handling
```

#### API Integration

```python
# Function to call [API_NAME] API
# Handle authentication and rate limiting
# Return parsed JSON response
```

### Measuring Your Progress

Track these metrics to see improvement:

- Time saved on routine coding tasks
- Quality of first-attempt code generation
- Reduction in syntax errors
- Faster completion of complex functions
- Improved code documentation

### Community Resources

- GitHub Copilot Community Forum
- VS Code Extension Marketplace reviews
- Developer blogs and tutorials
- YouTube channels focused on AI-assisted coding
- Stack Overflow discussions

Remember: GitHub Copilot is a tool to enhance your productivity, not replace your thinking. The best results come from combining AI assistance with solid programming fundamentals and critical thinking.
