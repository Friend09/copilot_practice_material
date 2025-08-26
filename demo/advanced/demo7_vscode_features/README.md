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
5. **Chat Modes** - Custom and built-in chat mode configurations
6. **MCP Servers** - Model Context Protocol servers
7. **Generate Instructions** - Auto-generated custom instructions

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

Prompt Files are Markdown files that define reusable prompts for common development tasks like generating code, performing code reviews, or scaffolding project components. They are standalone prompts that you can run directly in chat, enabling the creation of a library of standardized development workflows.

### What are Prompt Files?

- Reusable prompt templates stored as `.prompt.md` files
- Can include variables and placeholders using `${variableName}` syntax
- Shareable across team members
- Available in two scopes: workspace and user profile
- Support YAML frontmatter for configuration

### Prompt File Format:

Prompt files use the `.prompt.md` extension and have this structure:

```markdown
---
description: Short description of the prompt
mode: ask | edit | agent (default)
model: Specific language model to use
tools: ["codebase", "search", "findTestFiles"]
---

# Prompt content in Markdown format

Use variables like ${selection}, ${file}, ${workspaceFolder}
Reference other files with [link](../path/to/file.md)
```

### Available Variables:

- **Workspace variables**: `${workspaceFolder}`, `${workspaceFolderBasename}`
- **Selection variables**: `${selection}`, `${selectedText}`
- **File context variables**: `${file}`, `${fileBasename}`, `${fileDirname}`, `${fileBasenameNoExtension}`
- **Input variables**: `${input:variableName}`, `${input:variableName:placeholder}`

### How to Create Prompt Files:

1. **Enable prompt files:**

   - Enable the `chat.promptFiles` setting in VS Code

2. **Create a new prompt file:**

   - In Chat view: Configure Chat → Prompt Files → New prompt file
   - Or use Command Palette: `Chat: New Prompt File`

3. **Choose storage location:**

   - **Workspace**: `.github/prompts/` folder (team-wide access)
   - **User profile**: Personal prompts synced across devices

4. **Example: Code Review Prompt (`code-review.prompt.md`):**

   ```markdown
   ---
   description: Comprehensive code review with security and performance focus
   mode: ask
   tools: ["codebase", "search"]
   ---

   # Code Review Prompt

   Please review the following code for:

   - Security vulnerabilities
   - Performance issues
   - Code quality and best practices
   - Documentation completeness

   Focus on: ${input:language:programming language} specific patterns
   Severity level: ${input:severity:high/medium/low}

   Code to review:
   ${selection}
   ```

5. **Example: React Component Generator (`create-react-form.prompt.md`):**

   ```markdown
   ---
   description: Generate a React form component with validation
   mode: edit
   tools: ["codebase"]
   ---

   # React Form Component Generator

   Create a React form component in ${file} with the following requirements:

   - Form name: ${input:formName:MyForm}
   - Fields: ${input:fields:name, email, message}
   - Include form validation
   - Use TypeScript if the project uses it
   - Follow the project's existing component patterns

   Reference existing components: [Button](../components/Button.tsx)
   ```

### Using Prompt Files:

1. **In Chat view:**

   - Type `/` followed by the prompt file name: `/code-review`
   - Pass additional parameters: `/create-react-form: formName=ContactForm`

2. **From Command Palette:**

   - Run `Chat: Run Prompt` command
   - Select prompt file from Quick Pick

3. **From Editor:**
   - Open the `.prompt.md` file
   - Click the play button in the editor title
   - Choose to run in current or new chat session

### Managing Prompt Files:

- **Workspace prompts**: Stored in `.github/prompts/` by default
- **Additional locations**: Configure with `chat.promptFilesLocations` setting
- **User prompts**: Stored in VS Code profile folder
- **Sync across devices**: Enable Settings Sync for "Prompts and Instructions"

### Tips for Effective Prompt Files:

- Clearly describe what the prompt should accomplish
- Provide examples of expected input and output
- Use Markdown links to reference custom instructions
- Take advantage of built-in variables like `${selection}`
- Use input variables for flexible, reusable prompts
- Test prompts using the editor play button

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

## 5. 💬 Chat Modes

Chat Modes are predefined configurations that enable you to tailor chat behavior for specific workflows or personas. VS Code comes with built-in modes and supports custom chat modes.

### Built-in Chat Modes:

#### A. **Ask Mode**

- Optimized for answering questions about your codebase
- Best for understanding code and exploring technologies
- General coding and technology concept discussions

#### B. **Edit Mode**

- Optimized for making code edits across multiple files
- VS Code directly applies changes in the editor
- Use when you have well-defined changes to make

#### C. **Agent Mode**

- Autonomous edits across multiple files
- Can run terminal commands and use tools
- Best for less well-defined tasks requiring exploration

### Custom Chat Modes:

Create specialized chat modes for your workflow needs.

#### Creating Custom Chat Modes:

1. **Access Chat Mode Configuration:**

   - In Chat view, select Configure Chat → Modes
   - Choose "Create new custom chat mode file"
   - Or use Command Palette: `Chat: New Mode File`

2. **Choose Storage Location:**

   - **Workspace**: `.github/chatmodes/` folder (team-wide)
   - **User Profile**: Personal modes synced across devices

3. **Chat Mode File Structure (.chatmode.md):**

```markdown
---
description: Brief description of the chat mode
tools: ["codebase", "search", "findTestFiles"]
model: Claude Sonnet 4
---

# Custom Mode Instructions

Your specific instructions and guidelines for this chat mode.
Include prompts, workflows, and any relevant information.
```

#### Example: Code Review Chat Mode

**File**: `.github/chatmodes/code-review.chatmode.md`

```markdown
---
description: Comprehensive code review with security and performance focus
tools: ["codebase", "search", "usages", "findTestFiles"]
model: Claude Sonnet 4
---

# Code Review Mode

You are in code review mode. Focus on:

## Security Analysis

- Look for security vulnerabilities
- Check for hardcoded secrets
- Validate input sanitization
- Review authentication/authorization

## Performance Review

- Identify performance bottlenecks
- Check for memory leaks
- Review algorithm efficiency
- Analyze database queries

## Code Quality

- Check coding standards compliance
- Review documentation completeness
- Validate error handling
- Assess test coverage

## Best Practices

- Framework-specific patterns
- SOLID principles adherence
- Code maintainability
- Architectural consistency

Provide specific, actionable feedback with code examples.
```

#### Example: Planning Chat Mode

**File**: `.github/chatmodes/planning.chatmode.md`

```markdown
---
description: Generate implementation plans without making code changes
tools: ["codebase", "search", "githubRepo", "usages"]
model: Claude Sonnet 4
---

# Planning Mode

You are in planning mode. Generate detailed implementation plans.

## Planning Structure

### Overview

- Brief feature description
- Goals and objectives
- Success criteria

### Requirements Analysis

- Functional requirements
- Non-functional requirements
- Dependencies and constraints

### Technical Design

- Architecture overview
- Component breakdown
- Data flow diagrams
- API specifications

### Implementation Steps

1. Detailed step-by-step plan
2. File creation/modification list
3. Testing strategy
4. Deployment considerations

### Risk Assessment

- Potential challenges
- Mitigation strategies
- Alternative approaches

Do NOT make any code changes - only generate plans.
```

### Using Chat Modes:

1. **Switch Modes:**

   - Open Chat view (Ctrl/Cmd + Shift + I)
   - Use the chat mode dropdown
   - Select your desired mode

2. **Mode-Specific Behavior:**
   - Each mode follows its configured instructions
   - Uses specified tools and model
   - Maintains consistent persona/workflow

### Managing Chat Modes:

1. **Edit Existing Modes:**

   - Configure Chat → Modes
   - Select mode to modify
   - Edit `.chatmode.md` file

2. **Share Team Modes:**
   - Store in `.github/chatmodes/`
   - Commit to version control
   - Team members get consistent experience

---

## 6. 🌐 MCP Servers

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

## 7. 🤖 Generate Instructions

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

1. Enable the `chat.promptFiles` setting in VS Code
2. Create a code review prompt file (`code-review.prompt.md`) in `.github/prompts/`
3. Create a documentation prompt file (`generate-docs.prompt.md`) with input variables
4. Test both prompts using `/` command in chat and the editor play button

### Exercise 3: Configure Tool Sets

1. Enable tool sets for your tech stack
2. Generate code using framework-specific tools
3. Compare results with/without tool sets

### Exercise 4: Test Different Modes

1. Try the same request in different modes
2. Compare the responses
3. Identify best mode for different tasks

### Exercise 5: Create Custom Chat Modes

1. Create a code review chat mode
2. Create a planning chat mode
3. Test both modes with sample tasks
4. Compare with built-in modes

### Exercise 6: Configure MCP Servers

1. Set up an MCP server (if available)
2. Test enhanced context capabilities
3. Compare responses with/without MCP

### Exercise 7: Generate Instructions

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
- ✅ Create and manage custom chat modes for specialized workflows
- ✅ Set up and use MCP servers for additional context
- ✅ Generate custom instructions automatically

---

## 🔍 Troubleshooting

### Common Issues

1. **Instructions not being followed:**

   - Check file location and syntax
   - Ensure instructions are clear and specific
   - Restart VS Code to reload instructions

2. **Prompt files not appearing:**

   - Verify file extension (`.prompt.md`)
   - Check `chat.promptFiles` setting is enabled
   - Ensure file is in correct location (`.github/prompts/` or user profile)
   - Refresh Copilot chat

3. **Prompt file variables not working:**

   - Use correct syntax: `${variableName}` not `{{variableName}}`
   - Check YAML frontmatter format
   - Verify variable names match available options

4. **Tool sets not working:**

   - Ensure tool set is enabled
   - Check VS Code settings
   - Update GitHub Copilot extension

5. **Custom chat modes not appearing:**

   - Verify file extension (`.chatmode.md`)
   - Check file location (`.github/chatmodes` or user profile)
   - Ensure proper YAML frontmatter format
   - Restart VS Code if needed

6. **Chat mode instructions ignored:**
   - Check YAML frontmatter syntax
   - Ensure description and tools are properly formatted
   - Verify model specification is valid

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
