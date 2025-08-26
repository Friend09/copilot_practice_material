# Demo 7: VS Code GitHub Copilot Advanced Features

## What This Demo Covers

This demo provides hands-on practice with the advanced GitHub Copilot features available through the VS Code chat interface. You'll learn to configure and use each feature accessed through the settings menu (⚙️) in the Copilot chat window.

**Duration**: 30-45 minutes
**Complexity**: Advanced
**Prerequisites**: GitHub Copilot subscription, VS Code with GitHub Copilot extension

---

## 🎯 Features Covered

Based on the GitHub Copilot chat settings menu, this demo covers:

1. **Prompt Files** - Custom prompt templates
2. **Instructions** - Custom AI behavior configuration
3. **Tool Sets** - Extended capabilities and integrations
4. **Modes** - Different AI interaction modes
5. **MCP Servers** - Model Context Protocol servers
6. **Generate Instructions** - Auto-generated custom instructions

---

## 📋 Prerequisites

Before starting, ensure you have:

- VS Code with GitHub Copilot extension installed
- GitHub Copilot subscription (Individual, Business, or Enterprise)
- Access to VS Code settings and workspace configuration
- Basic understanding of VS Code and GitHub Copilot

---

## 🚀 Getting Started

### Step 1: Access Copilot Chat Settings

1. Open VS Code
2. Open GitHub Copilot Chat (Ctrl/Cmd + Shift + I or click the chat icon)
3. Click the settings icon (⚙️) in the chat window
4. You'll see the dropdown menu with the features we'll explore

---

## 1. 📝 Prompt Files

Prompt Files allow you to create reusable prompt templates for common development tasks.

### What are Prompt Files?

- Reusable prompt templates stored as `.md` files
- Can include variables and placeholders
- Shareable across team members
- Located in `.vscode/` or workspace root

### How to Create Prompt Files:

1. **Create a prompt file:**

   ```bash
   mkdir -p .vscode/prompts
   ```

2. **Example: Code Review Prompt (`code-review.md`):**

   ```markdown
   # Code Review Prompt

   Please review the following code for:

   - Security vulnerabilities
   - Performance issues
   - Code quality and best practices
   - Documentation completeness

   Focus on: {{language}} specific patterns
   Severity level: {{severity}}

   Code to review:
   {{selection}}
   ```

3. **Example: API Documentation Prompt (`api-docs.md`):**

   ```markdown
   # API Documentation Generator

   Generate comprehensive API documentation for:
   {{selection}}

   Include:

   - Endpoint descriptions
   - Request/response examples
   - Error codes
   - Authentication requirements
   ```

### Using Prompt Files:

1. Select code in your editor
2. Open Copilot Chat
3. Click settings (⚙️) → Prompt Files
4. Choose your template
5. Fill in any variables
6. Execute the prompt

---

## 2. ⚙️ Instructions

Instructions define custom behavior and guidelines for GitHub Copilot across your workspace.

### Types of Instructions:

#### A. Workspace Instructions (`.vscode/copilot-instructions.md`)

```markdown
# Workspace Copilot Instructions

## Code Style Guidelines

- Use TypeScript for all new files
- Follow ESLint configuration
- Use async/await instead of Promises
- Include JSDoc comments for all functions

## Security Requirements

- Never hardcode secrets or API keys
- Use environment variables for configuration
- Validate all user inputs
- Follow OWASP security guidelines

## Testing Standards

- Write unit tests for all new functions
- Use Jest as testing framework
- Aim for 80%+ code coverage
- Include integration tests for APIs
```

#### B. Repository Instructions (`.github/copilot-instructions.md`)

```markdown
# Repository Copilot Instructions

## Project-Specific Guidelines

- This is a Node.js Express API
- Use MongoDB for data persistence
- Follow RESTful API conventions
- Use Swagger for API documentation

## Architecture Patterns

- Follow MVC pattern
- Use dependency injection
- Implement proper error handling
- Use middleware for common functionality
```

### Setting Up Instructions:

1. **Create workspace instructions:**

   ```bash
   mkdir -p .vscode
   touch .vscode/copilot-instructions.md
   ```

2. **Create repository instructions:**

   ```bash
   mkdir -p .github
   touch .github/copilot-instructions.md
   ```

3. **Edit the files with your team's guidelines**

### Testing Instructions:

1. Open Copilot Chat
2. Ask: "Generate a new API endpoint following our project guidelines"
3. Observe how Copilot follows your instructions

---

## 3. 🔧 Tool Sets

Tool Sets extend Copilot's capabilities with additional tools and integrations.

### Available Tool Sets:

- **Web Development**: HTML, CSS, JavaScript frameworks
- **Backend Development**: API development, database tools
- **DevOps**: Docker, Kubernetes, CI/CD tools
- **Testing**: Unit testing, integration testing frameworks
- **Documentation**: API docs, README generators

### Configuring Tool Sets:

1. **Access Tool Sets:**

   - Click settings (⚙️) → Tool Sets
   - Browse available tool collections

2. **Example Tool Set Configuration:**
   ```json
   {
     "copilot.toolSets": {
       "webDev": {
         "enabled": true,
         "tools": ["react", "next.js", "tailwind"]
       },
       "backend": {
         "enabled": true,
         "tools": ["express", "mongodb", "prisma"]
       }
     }
   }
   ```

### Using Tool Sets:

1. Select relevant tool set for your project
2. Copilot will provide framework-specific suggestions
3. Access specialized commands and snippets

---

## 4. 🎭 Modes

Modes change how Copilot interacts with you and processes your requests.

### Available Modes:

#### A. **Assistant Mode** (Default)

- General programming assistance
- Code completion and generation
- Explanations and debugging

#### B. **Agent Mode**

- Autonomous task execution
- Multi-step problem solving
- Proactive suggestions

#### C. **Review Mode**

- Code review focus
- Security and quality analysis
- Best practices enforcement

### Switching Modes:

1. Click settings (⚙️) → Modes
2. Select appropriate mode for your task
3. Mode affects Copilot's response style and focus

---

## 5. 🌐 MCP Servers

Model Context Protocol (MCP) servers provide additional context and capabilities.

### What are MCP Servers?

- External services that provide context to Copilot
- Can include documentation, APIs, databases
- Extend Copilot's knowledge beyond training data

### Common MCP Servers:

- **Documentation servers**: Access to latest library docs
- **API servers**: Real-time API information
- **Database servers**: Schema and data context
- **Custom servers**: Team-specific knowledge bases

### Setting Up MCP Servers:

1. **Configure in VS Code settings:**

   ```json
   {
     "copilot.mcpServers": [
       {
         "name": "docs-server",
         "url": "https://api.example.com/docs",
         "enabled": true
       }
     ]
   }
   ```

2. **Access through settings:**
   - Click settings (⚙️) → MCP Servers
   - Enable/disable servers as needed

---

## 6. 🤖 Generate Instructions

Automatically generate custom instructions based on your codebase.

### How it Works:

1. Analyzes your project structure
2. Identifies patterns and conventions
3. Generates appropriate instructions
4. Suggests team guidelines

### Using Generate Instructions:

1. **Access the feature:**

   - Click settings (⚙️) → Generate Instructions
   - Choose analysis scope (workspace/repository)

2. **Review generated instructions:**

   - Copilot will analyze your code
   - Suggest coding standards
   - Identify architectural patterns

3. **Customize and save:**
   - Edit generated instructions
   - Save to appropriate location
   - Share with team members

---

## 🏃‍♂️ Hands-on Exercises

### Exercise 1: Set Up Workspace Instructions

1. Create `.vscode/copilot-instructions.md`
2. Add coding standards for your preferred language
3. Test with a code generation request

### Exercise 2: Create Prompt Files

1. Create a prompt file for code reviews
2. Create a prompt file for documentation
3. Use both with sample code

### Exercise 3: Configure Tool Sets

1. Enable tool sets for your tech stack
2. Generate code using framework-specific tools
3. Compare results with/without tool sets

### Exercise 4: Test Different Modes

1. Try the same request in different modes
2. Compare the responses
3. Identify best mode for different tasks

### Exercise 5: Generate Instructions

1. Use the generate instructions feature
2. Review and customize the output
3. Apply to a sample project

---

## 🎯 Expected Outcomes

After completing this demo, you should be able to:

- ✅ Configure custom instructions for consistent AI behavior
- ✅ Create and use reusable prompt files
- ✅ Select appropriate tool sets for your projects
- ✅ Switch between different Copilot modes effectively
- ✅ Set up and use MCP servers for additional context
- ✅ Generate custom instructions automatically

---

## 🔍 Troubleshooting

### Common Issues:

1. **Instructions not being followed:**

   - Check file location and syntax
   - Ensure instructions are clear and specific
   - Restart VS Code to reload instructions

2. **Prompt files not appearing:**

   - Verify file extension (.md)
   - Check file location (.vscode/prompts or workspace root)
   - Refresh Copilot chat

3. **Tool sets not working:**
   - Ensure tool set is enabled
   - Check VS Code settings
   - Update GitHub Copilot extension

---

## 📚 Additional Resources

- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [VS Code Copilot Extension Guide](https://code.visualstudio.com/docs/copilot/overview)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)
- [Prompt Engineering Best Practices](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)

---

## 🎓 Next Steps

1. **Implement in your projects**: Apply these configurations to real projects
2. **Share with your team**: Distribute instructions and prompt files
3. **Iterate and improve**: Refine based on team feedback
4. **Explore enterprise features**: If available, explore additional enterprise capabilities
