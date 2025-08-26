# Demo 7: VS Code GitHub Copilot Advanced Features

## What This Demo Covers

This demo provides hands-on practice with the advanced GitHub Copilot features available through the VS Code chat interface. You'll learn to configure and use each feature accessed through the settings menu (⚙️) in the Copilot chat window.

**Duration**: 30-45 minutes
**Complexity**: Advanced
**Prerequisites**: GitHub Copilot subscription, VS Code with GitHub Copilot extension
**Copilot Documentation**: [GitHub Copilot Docs](https://code.visualstudio.com/docs/copilot/customization/prompt-files#copilot-articles)

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

### Setup Instructions

1. **Create a new practice folder:**

   ```bash
   mkdir copilot-advanced-features-demo
   cd copilot-advanced-features-demo
   ```

2. **Create a VS Code workspace file (optional but recommended):**

   Create a file named `copilot-demo.code-workspace` with the following content:

   ```json
   {
     "folders": [
       {
         "path": "."
       }
     ],
     "settings": {}
   }
   ```

3. **Initialize a Git repository:**

   ```bash
   git init
   git add .
   git commit -m "Initial commit for Copilot advanced features demo"
   ```

4. **Open in VS Code:**

   ```bash
   code copilot-demo.code-workspace
   ```

Now you're all set to get started with the advanced GitHub Copilot features!

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

### Prompt File Format

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

### Available Variables

| Category         | Variables                                                                    | Description                                                    |
| ---------------- | ---------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Workspace**    | `${workspaceFolder}`, `${workspaceFolderBasename}`                           | Current workspace folder path and name                         |
| **Selection**    | `${selection}`, `${selectedText}`                                            | Currently selected text in editor                              |
| **File Context** | `${file}`, `${fileBasename}`, `${fileDirname}`, `${fileBasenameNoExtension}` | Current file path, name, directory, and name without extension |
| **Input**        | `${input:variableName}`, `${input:variableName:placeholder}`                 | Custom input variables with optional placeholder text          |

### How to Create Prompt Files

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
   mode: "agent"
   model: GPT-4o
   tools: ["githubRepo", "codebase"]
   description: "Generate a new React form component"
   ---

   Your goal is to generate a new React form component based on the templates in #githubRepo contoso/react-templates.

   Ask for the form name and fields if not provided.

   Requirements for the form:

   - Use form design system components: [design-system/Form.md](../docs/design-system/Form.md)
   - Use `react-hook-form` for form state management:
   - Always define TypeScript types for your form data
   - Prefer _uncontrolled_ components using register
   - Use `defaultValues` to prevent unnecessary rerenders
   - Use `yup` for validation:
   - Create reusable validation schemas in separate files
   - Use TypeScript types to ensure type safety
   - Customize UX-friendly validation rules
   ```

### Using Prompt Files

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

### Managing Prompt Files

- **Workspace prompts**: Stored in `.github/prompts/` by default
- **Additional locations**: Configure with `chat.promptFilesLocations` setting
- **User prompts**: Stored in VS Code profile folder
- **Sync across devices**: Enable Settings Sync for "Prompts and Instructions"

### Tips for Effective Prompt Files

- Clearly describe what the prompt should accomplish
- Provide examples of expected input and output
- Use Markdown links to reference custom instructions
- Take advantage of built-in variables like `${selection}`
- Use input variables for flexible, reusable prompts
- Test prompts using the editor play button

---

## 2. ⚙️ Instructions

Instructions define custom behavior and guidelines for GitHub Copilot across your workspace. VS Code supports two types of custom instructions files that automatically influence how AI generates code and handles development tasks.

### Types of Instructions Files

#### A. Single Workspace Instructions (`.github/copilot-instructions.md`)

A single `.github/copilot-instructions.md` file that automatically applies to all chat requests in the workspace.
[cursor rules link](https://cursor.directory/fastapi-python-cursor-rules)

```markdown
# Project Copilot Instructions

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

## Architecture Patterns

- Follow MVC pattern
- Use dependency injection
- Implement proper error handling
- Use middleware for common functionality
```

#### B. Specific Instructions Files (`.instructions.md`)

Multiple `.instructions.md` files for specific tasks or file types with YAML frontmatter to define scope.

**Example: Python-specific instructions** (`python-guidelines.instructions.md`):

```markdown
---
description: Python coding standards and best practices
applyTo: "**/*.py"
---

# Python Coding Standards

## PEP 8 Compliance

- Follow PEP 8 style guide for Python
- Use 4 spaces for indentation
- Maximum line length of 88 characters (Black formatter)
- Use descriptive variable and function names

## Type Hints

- Always include type hints for function parameters and return values
- Use `from typing import` for complex types
- Use `Optional[Type]` for nullable parameters

## Documentation

- Include docstrings for all functions and classes
- Use Google-style docstring format
- Document parameters, return values, and exceptions

## Error Handling

- Use specific exception types
- Include meaningful error messages
- Use try-except blocks appropriately
```

**Example: React component instructions** (`react-components.instructions.md`):

```markdown
---
description: React component development guidelines
applyTo: "**/*.tsx,**/*.jsx"
---

# React Component Guidelines

## Component Structure

- Use functional components with hooks
- Follow the single responsibility principle
- Keep components under 200 lines

## TypeScript Usage

- Define proper interfaces for props
- Use strict typing for state and handlers
- Export types for reusable components

## Performance

- Use React.memo for expensive components
- Implement proper dependency arrays in useEffect
- Use useCallback for expensive computations

## Testing

- Include unit tests for all components
- Test user interactions and edge cases
- Use React Testing Library
```

### Setting Up Instructions

#### Method 1: Using VS Code Interface

1. **Enable instruction files:**

   - Enable the `github.copilot.chat.codeGeneration.useInstructionFiles` setting

2. **Create instruction files:**

   - In Chat view: Configure Chat → Instructions → New instruction file
   - Or use Command Palette: `Chat: New Instructions File`

3. **Choose storage location:**
   - **Workspace**: `.github/instructions/` folder (team-wide access)
   - **User Profile**: Personal instructions synced across devices

#### Method 2: Manual Creation

1. **Create single workspace instructions:**

   ```bash
   mkdir -p .github
   touch .github/copilot-instructions.md
   ```

2. **Create specific instruction files:**

   ```bash
   mkdir -p .github/instructions
   touch .github/instructions/python-guidelines.instructions.md
   touch .github/instructions/react-components.instructions.md
   ```

3. **Edit the files with your guidelines and proper frontmatter**

### Instructions File Locations

- **Workspace instructions**: `.github/instructions/` (default)
- **Additional locations**: Configure with `chat.instructionsFilesLocations` setting
- **User instructions**: Stored in VS Code profile folder
- **Sync across devices**: Enable Settings Sync for "Prompts and Instructions"

### Advanced Configuration

#### Using Settings for Specialized Scenarios

```json
{
  "github.copilot.chat.reviewSelection.instructions": [
    { "file": "guidance/code-review-guidelines.md" },
    {
      "text": "Always check for security vulnerabilities and performance issues."
    }
  ],
  "github.copilot.chat.commitMessageGeneration.instructions": [
    { "text": "Use conventional commit format: type(scope): description" }
  ],
  "github.copilot.chat.pullRequestDescriptionGeneration.instructions": [
    { "text": "Include a list of key changes and testing notes." }
  ]
}
```

### Generate Instructions Automatically

VS Code can analyze your workspace and generate matching instructions:

1. In Chat view: Configure Chat → Generate Instructions
2. Review and customize the generated instructions
3. Save to `.github/copilot-instructions.md`

### Testing Instructions

1. Open Copilot Chat
2. Ask: "Generate a new API endpoint following our project guidelines"
3. Observe how Copilot follows your instructions
4. For specific files, instructions with matching `applyTo` patterns will be applied automatically

### Best Practices

- Keep instructions short and self-contained
- Use multiple `.instructions.md` files for different topics
- Store project-specific instructions in workspace for team sharing
- Use glob patterns in `applyTo` for targeted application
- Reference instructions files in prompt files and chat modes to avoid duplication

---

## 3. 🔧 Tool Sets

Tool Sets are collections of tools that you can use together in chat, particularly in agent mode. They enable you to group related tools together, making them easier to select and reference in chat prompts and other Copilot features.

### What are Tool Sets?

Tool Sets allow you to:

- Group related tools together for easier management
- Quickly select multiple tools at once in agent mode
- Reference tool sets directly in prompts using `#toolSetName`
- Create reusable tool configurations for different workflows
- Organize tools when you have many installed from MCP servers or extensions

### Types of Tools Available

| Tool Type           | Examples                                                                                      | Source                         |
| ------------------- | --------------------------------------------------------------------------------------------- | ------------------------------ |
| **Built-in Tools**  | `changes`, `codebase`, `fetch`, `findTestFiles`, `githubRepo`, `problems`, `search`, `usages` | VS Code Copilot                |
| **MCP Tools**       | Database operations, API integrations, web scraping, analytics                                | Model Context Protocol servers |
| **Extension Tools** | Language-specific tools, testing frameworks, deployment tools                                 | VS Code extensions             |

### Creating Tool Sets

1. **Access Tool Sets Configuration:**

   - In Chat view, select Configure Chat → Tool Sets
   - Choose "New tool sets file"
   - Or use Command Palette: `Chat: Configure Tool Sets`

2. **Tool Set File Structure:**
   Tool sets are defined in `.jsonc` files with this structure:

   ```json
   {
     "toolSetName": {
       "tools": ["tool1", "tool2", "tool3"],
       "description": "Brief description of the tool set",
       "icon": "iconName"
     }
   }
   ```

3. **Example Tool Set Configuration:**

   ```json
   {
     "reader": {
       "tools": [
         "changes",
         "codebase",
         "fetch",
         "findTestFiles",
         "githubRepo",
         "problems",
         "usages"
       ],
       "description": "Tools for reading and analyzing code",
       "icon": "tag"
     },
     "webDev": {
       "tools": ["codebase", "search", "githubRepo", "fetch"],
       "description": "Web development tools",
       "icon": "globe"
     }
   }
   ```

### Using Tool Sets

1. **In Agent Mode:**

   - Select the Tools icon in Chat view
   - Choose tool sets from the tools picker
   - Tool sets appear alongside individual tools

2. **Direct Reference:**

   - Use `#toolSetName` in chat prompts
   - Example: "Create a new feature #webDev"

3. **In Chat Modes and Prompt Files:**
   - Reference tool sets in `tools` array
   - Example: `tools: ['reader', 'webDev']`

### Tool Set Storage

- **User Profile**: Personal tool sets synced across devices
- **Workspace**: Team-shared tool sets (recommended location)
- **Icon Options**: Use icons from [Product Icon Reference](https://code.visualstudio.com/api/references/icons-in-labels)

### Limitations

- Maximum of 128 tools per chat request (including tools from tool sets)
- If you exceed this limit, reduce selected tools or enable virtual tools setting

---

## 4. 🎭 Modes

Modes change how Copilot interacts with you and processes your requests.

### Available Modes

| Mode                         | Focus                                                                        | Best For                                               |
| ---------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------ |
| **Assistant Mode** (Default) | General programming assistance, code completion, explanations, debugging     | General development questions and code assistance      |
| **Agent Mode**               | Autonomous task execution, multi-step problem solving, proactive suggestions | Complex tasks requiring exploration and multiple tools |
| **Review Mode**              | Code review focus, security and quality analysis, best practices enforcement | Code quality assessment and security reviews           |

### Switching Modes

1. Click settings (⚙️) → Modes
2. Select appropriate mode for your task
3. Mode affects Copilot's response style and focus

---

## 5. 💬 Chat Modes

Chat modes are predefined configurations that enable you to tailor the chat behavior in Visual Studio Code for specific workflows or have chat assume a specific persona. VS Code comes with three built-in chat modes: Ask, Edit, and Agent. You can create custom chat modes for specialized workflows like planning features, conducting code reviews, or researching implementation options.

**Note**: Custom chat modes are available as of VS Code release 1.101 and are currently in preview.

### Switching Between Chat Modes

To switch between chat modes:

1. Open the Chat view (⌃⌘I / Ctrl+Shift+I)
2. Select the desired mode from the chat mode dropdown list
3. The mode affects how Copilot processes your requests and responds

### Built-in Chat Modes

VS Code provides three built-in chat modes, each optimized for specific use cases:

| Mode           | Description                                                                                                                                                         | Best Use Cases                                                                                          |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Ask Mode**   | Optimized for answering questions about your codebase, coding, and general technology concepts.                                                                     | Understanding how code works, brainstorming software design ideas, exploring new technologies           |
| **Edit Mode**  | Optimized for making code edits across multiple files in your project. VS Code directly applies the code changes in the editor, where you can review them in-place. | Coding tasks when you have a good understanding of the changes you want to make and which files to edit |
| **Agent Mode** | Optimized for making autonomous edits across multiple files in your project. Can run terminal commands and use tools.                                               | Less well-defined tasks that might require exploration, running commands, and using multiple tools      |

### Custom Chat Modes

The built-in chat modes provide general-purpose configurations for chat in VS Code. For a more tailored chat experience, you can create your own chat modes.

Custom chat modes consist of a set of instructions and tools that are applied when you switch to that mode. For example, a "Plan" chat mode could include instructions for generating an implementation plan and only use read-only tools. By creating a custom chat mode, you can quickly switch to that specific configuration without having to manually select relevant tools and instructions each time.

Custom chat modes are defined in a `.chatmode.md` Markdown file, and can be stored in your workspace for others to use, or in your user profile, where you can reuse them across different workspaces.

#### Chat Mode File Structure

Chat mode files are Markdown files and use the `.chatmode.md` extension with this structure:

##### Header (optional): YAML frontmatter

- `description`: A brief description of the chat mode. This description is displayed as placeholder text in the chat input field and when you hover the mode in the chat mode dropdown list.
- `tools`: A list of tool or tool set names that are available for this chat mode. This can include built-in tools, tool sets, MCP tools, or tools contributed by extensions. Use the Configure Tools action to select the tools from the list of available tools in your workspace.
- `model`: The AI model to use when running the prompt. If not specified, the currently selected model in model picker is used.

##### Body: Chat mode details and instructions in Markdown format

This is where you provide specific prompts, guidelines, or any other relevant information that you want the AI to follow when in this chat mode.

You can reference instructions files by using Markdown links. The chat mode instructions will complement whatever is specified in the chat prompt.

```markdown
---
description: Brief description of the chat mode
tools: ["codebase", "search", "findTestFiles"]
model: Claude Sonnet 4
---

# Custom Mode Instructions

Your specific instructions and guidelines for this chat mode.
Include prompts, workflows, and any relevant information.

You can reference [custom instructions](../instructions/coding-standards.md) files.
```

#### Example: Planning Chat Mode

The following example shows a "Plan" chat mode file that generates an implementation plan and doesn't make any code edits:

**File**: `.github/chatmodes/plan.chatmode.md`

```markdown
---
description: Generate an implementation plan for new features or refactoring existing code.
tools: ["codebase", "fetch", "findTestFiles", "githubRepo", "search", "usages"]
model: Claude Sonnet 4
---

# Planning mode instructions

You are in planning mode. Your task is to generate an implementation plan for a new feature or for refactoring existing code.

Don't make any code edits, just generate a plan.

The plan consists of a Markdown document that describes the implementation plan, including the following sections:

- **Overview**: A brief description of the feature or refactoring task.
- **Requirements**: A list of requirements for the feature or refactoring task.
- **Implementation Steps**: A detailed list of steps to implement the feature or refactoring task.
- **Testing**: A list of tests that need to be implemented to verify the feature or refactoring task.
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

#### Creating a Custom Chat Mode

1. **Access Chat Mode Configuration:**

   - In the Chat view, select Configure Chat > Modes, and then select "Create new custom chat mode file"
   - Alternatively, use the `Chat: New Mode File` command in the Command Palette (⇧⌘P / Ctrl+Shift+P)

2. **Choose Storage Location:**

   - **Workspace**: By default, workspace chat mode files are stored in the `.github/chatmodes` folder of your workspace. Add more prompt folders for your workspace with the `chat.modeFilesLocations` setting.
   - **User Profile**: User chat mode files are stored in the current profile folder. You can sync your user chat mode files across multiple devices by using Settings Sync.

3. **Enter a Name**: This name is used in the chat mode dropdown list in the Chat view.

4. **Configure the Chat Mode:**
   - Provide the description and configure the list of available tools or tool sets in the Front Matter metadata
   - Add instructions for the chat mode in the body of the file

#### Managing Chat Modes

**Edit Existing Modes:**

- In the Chat view, select Configure Chat > Modes, and then select an existing chat mode from the list to modify it
- Alternatively, use the `Chat: Configure Chat Modes` command from the Command Palette (⇧⌘P / Ctrl+Shift+P)

**Share Team Modes:**

- Store chat modes in `.github/chatmodes/`
- Commit to version control
- Team members get consistent experience across the workspace

---

## 6. 🌐 MCP Servers

Model Context Protocol (MCP) is an open standard that lets AI models use external tools and services through a unified interface. In VS Code, MCP servers add tools for tasks like file operations, databases, or interacting with external APIs.

**Note**: MCP support in VS Code is generally available starting from VS Code 1.102.

### What are MCP Servers?

MCP servers provide additional capabilities and context to GitHub Copilot through:

- **Tools**: Executable functions for specific tasks (file operations, API calls, database queries)
- **Resources**: Contextual information (documentation, files, database schemas)
- **Prompts**: Preconfigured prompts for common tasks
- **Elicitations**: Dynamic requests for additional user input

MCP servers can be:

- **Local servers**: Running on your machine (stdio communication)
- **Remote servers**: Accessible via HTTP/HTTPS (HTTP/SSE communication)
- **Extension-provided**: Installed as part of VS Code extensions

### Prerequisites

- Latest version of Visual Studio Code
- Access to GitHub Copilot
- MCP support enabled with `chat.mcp.enabled` setting (enabled by default)

### Adding MCP Servers

⚠️ **Security Warning**: MCP servers can run arbitrary code on your machine. Only add servers from trusted sources, and review the publisher and server configuration before starting it.

#### Method 1: Install from VS Code Web Catalog

1. Visit the [VS Code curated list of MCP servers](https://code.visualstudio.com/mcp)
2. Browse available servers by category
3. Click "Install in VS Code" for your desired server
4. VS Code will prompt you to confirm installation

#### Method 2: Manual Configuration

1. **Open MCP Configuration:**

   - Run `MCP: Open User Configuration` or `MCP: Open Workspace Folder Configuration` from Command Palette
   - This creates/opens the `mcp.json` file

2. **Add Server Configuration:**

**Standard I/O (stdio) Server Example:**

```json
{
  "servers": {
    "github": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@github/github-mcp-server"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${input:github-token}"
      }
    }
  },
  "inputs": [
    {
      "type": "promptString",
      "id": "github-token",
      "description": "GitHub Personal Access Token",
      "password": true
    }
  ]
}
```

**HTTP Server Example:**

```json
{
  "servers": {
    "api-server": {
      "type": "http",
      "url": "https://api.example.com/mcp",
      "headers": {
        "Authorization": "Bearer ${input:api-token}"
      }
    }
  },
  "inputs": [
    {
      "type": "promptString",
      "id": "api-token",
      "description": "API Access Token",
      "password": true
    }
  ]
}
```

#### Method 3: Command Line Installation

```bash
# Install to user profile
code --add-mcp '{"name":"github","command":"npx","args":["-y","@github/github-mcp-server"]}'

# For VS Code Insiders
code-insiders --add-mcp '{"name":"github","command":"npx","args":["-y","@github/github-mcp-server"]}'
```

### Using MCP Tools in Agent Mode

Once you have MCP servers installed:

1. **Enable Agent Mode:**

   - Open Chat view (⌃⌘I / Ctrl+Shift+I)
   - Select "Agent" from the chat mode dropdown

2. **Select Tools:**

   - Click the Tools button in the chat input
   - Select MCP tools alongside built-in tools
   - Search for specific tools by typing

3. **Use Tools in Prompts:**

   - Tools are automatically invoked based on your requests
   - Directly reference tools with `#toolName`
   - Example: "List my GitHub issues" (automatically uses GitHub MCP tools)

4. **Tool Confirmation:**
   - VS Code prompts for confirmation before running MCP tools
   - Review tool parameters before execution
   - Use "Continue" dropdown to auto-approve tools for session/workspace

**Tool Limit**: Maximum of 128 tools per chat request. Use the `github.copilot.chat.virtualTools.threshold` setting to enable virtual tools if you exceed this limit.

### Using MCP Resources

MCP servers can provide contextual resources (files, documentation, data):

1. **Add Resources to Chat:**

   - In Chat view, select "Add Context" > "MCP Resources"
   - Choose resource type and provide parameters
   - Resources appear as context in your chat

2. **Browse Available Resources:**

   - Run `MCP: Browse Resources` from Command Palette
   - Or use `MCP: List Servers` > Browse Resources for specific server

3. **Save Resources:**
   - Tools can return resources in their responses
   - Save resources to workspace by selecting "Save" or drag-and-drop to Explorer

### Using MCP Prompts

MCP servers can provide preconfigured prompts for common tasks:

- **Invoke MCP Prompts:**

  - Type `/` in chat followed by prompt name: `/mcp.servername.promptname`
  - VS Code shows available prompts as you type
  - Provide additional parameters when prompted

- **Example:**

  ```text
  /mcp.github.create-issue
  ```

### MCP Server Management

#### View Installed Servers

1. **Extensions View:**

   - Open Extensions view (⇧⌘X / Ctrl+Shift+X)
   - Navigate to "MCP SERVERS - INSTALLED" section

2. **Command Palette:**
   - Run `MCP: Show Installed Servers`
   - Run `MCP: List Servers` for detailed view

#### Server Actions

| Action                 | Method                              | Purpose                        |
| ---------------------- | ----------------------------------- | ------------------------------ |
| **Start/Stop/Restart** | Right-click server → Control state  | Control server state           |
| **Show Output**        | Right-click server → Show Output    | View server logs for debugging |
| **Uninstall**          | Right-click server → Uninstall      | Remove server configuration    |
| **Trust/Untrust**      | Right-click server → Trust settings | Manage server trust settings   |

Access these actions by right-clicking on server in Extensions view or using `MCP: List Servers`.

#### Auto-start Configuration

Enable automatic server restart on configuration changes:

```json
{
  "chat.mcp.autostart": true
}
```

### Popular MCP Servers

The [VS Code MCP catalog](https://code.visualstudio.com/mcp) provides a curated list of MCP servers organized by category. Here are some of the most useful servers available:

| Category                   | Server                                                                                                  | Description                                                    |
| -------------------------- | ------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **Developer Tools**        | [GitHub](https://github.com/github/github-mcp-server)                                                   | Access GitHub repositories, issues, and pull requests          |
|                            | [Figma](https://help.figma.com/hc/en-us/articles/32132100833559-Guide-to-the-Dev-Mode-MCP-Server)       | Extract UI content and generate code from Figma designs        |
|                            | [Playwright](https://github.com/microsoft/playwright-mcp)                                               | Automate web browsers using accessibility trees                |
|                            | [Sentry](https://github.com/getsentry/sentry-mcp)                                                       | Retrieve and analyze application errors and performance issues |
|                            | [Hugging Face](https://hf.co/mcp)                                                                       | Access models, datasets, and Spaces on the Hugging Face Hub    |
|                            | [MarkItDown](https://github.com/microsoft/markitdown/tree/main/packages/markitdown-mcp)                 | Convert various file formats to Markdown                       |
|                            | [Microsoft Docs](https://github.com/microsoftdocs/mcp)                                                  | Search Microsoft Learn and Azure documentation                 |
|                            | [Context7](https://github.com/upstash/context7)                                                         | Get up-to-date documentation and code examples                 |
|                            | [Codacy](https://github.com/codacy/codacy-mcp-server)                                                   | Code quality and security analysis with SAST                   |
| **Productivity**           | [Notion](https://github.com/makenotion/notion-mcp-server)                                               | View, search, create, and update Notion pages                  |
|                            | [Linear](https://linear.app/docs/mcp)                                                                   | Create, update, and track issues in Linear                     |
|                            | [Asana](https://developers.asana.com/docs/using-asanas-model-control-protocol-mcp-server)               | Manage tasks, projects, and comments                           |
|                            | [Atlassian](https://www.atlassian.com/platform/remote-mcp-server)                                       | Connect to Jira and Confluence                                 |
|                            | [Zapier](https://zapier.com/mcp)                                                                        | Create workflows across 30,000+ apps                           |
|                            | [Monday.com](https://github.com/mondaycom/monday-ai/tree/master/packages/monday-api-mcp)                | Project management with boards and teams                       |
|                            | [Sequential Thinking](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking) | Break down complex tasks into steps                            |
|                            | [Memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory)                          | Store contextual information across sessions                   |
| **Data & Analytics**       | [DuckDB](https://github.com/ktanaka101/mcp-server-duckdb)                                               | Query and analyze DuckDB databases                             |
|                            | [MongoDB](https://github.com/mongodb-js/mongodb-mcp-server)                                             | Database operations and aggregation pipelines                  |
|                            | [Neon](https://github.com/neondatabase-labs/mcp-server-neon)                                            | Manage Neon Postgres databases with natural language           |
|                            | [PostHog](https://github.com/PostHog/mcp)                                                               | Access analytics and product usage insights                    |
|                            | [Microsoft Clarity](https://github.com/microsoft/clarity-mcp-server)                                    | Access analytics data and session recordings                   |
|                            | [Apify](https://docs.apify.com/platform/integrations/mcp)                                               | Extract data and automate workflows                            |
|                            | [Firecrawl](https://github.com/mendableai/firecrawl-mcp-server)                                         | Advanced web scraping and data extraction                      |
|                            | [Prisma Postgres](https://mcp.prisma.io/mcp)                                                            | Database operations with Prisma ORM                            |
| **Business Services**      | [Stripe](https://docs.stripe.com/mcp)                                                                   | Create customers, manage subscriptions                         |
|                            | [PayPal](https://developer.paypal.com/tools/mcp-server/)                                                | Create invoices and process payments                           |
|                            | [Square](https://developer.squareup.com/docs/mcp)                                                       | Process payments and manage customers                          |
|                            | [Intercom](https://developers.intercom.com/docs/guides/mcp)                                             | Access customer conversations and support tickets              |
|                            | [Wix](https://www.wix.com/studio/developers/mcp-server)                                                 | Build and manage Wix sites                                     |
|                            | [Webflow](https://github.com/webflow/mcp-server)                                                        | Create and manage websites and content                         |
| **Cloud & Infrastructure** | [Azure](https://github.com/azure/azure-mcp)                                                             | Manage Azure resources and services                            |
|                            | [Azure DevOps](https://github.com/microsoft/azure-devops-mcp)                                           | Manage projects, work items, and repositories                  |
|                            | [Convex](https://stack.convex.dev/convex-mcp-server)                                                    | Access backend databases and functions                         |
|                            | [Terraform](https://terraform-mcp-server.com)                                                           | Infrastructure as Code management                              |

#### Installation Examples

Most servers can be installed directly from the catalog with one click, or manually configured. Here are some examples:

**GitHub Server (Manual Configuration):**

```json
{
  "servers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@github/github-mcp-server"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "${input:github-token}"
      }
    }
  }
}
```

**Notion Server (One-Click Install):**
Visit [VS Code MCP catalog](https://code.visualstudio.com/mcp) → Productivity → Notion → "Install Notion"

**Browse Complete Catalog:**
Visit the [VS Code MCP catalog](https://code.visualstudio.com/mcp) for the most up-to-date list of available servers, organized by category with direct installation links.

### Configuration Format

#### Server Configuration Properties

| Server Type              | Required Properties         | Optional Properties      |
| ------------------------ | --------------------------- | ------------------------ |
| **Standard I/O (stdio)** | `type: "stdio"`, `command`  | `args`, `env`, `envFile` |
| **HTTP/SSE**             | `type: "http"/"sse"`, `url` | `headers`                |

**Property Details:**

- `command`: Executable command (must be in PATH or full path)
- `args`: Array of command arguments
- `env`: Environment variables object
- `envFile`: Path to environment file
- `url`: Server URL
- `headers`: HTTP headers object

#### Input Variables for Sensitive Data

Use input variables to avoid hardcoding sensitive information:

```json
{
  "inputs": [
    {
      "type": "promptString",
      "id": "api-key",
      "description": "Your API Key",
      "password": true
    }
  ]
}
```

Reference in server config: `"${input:api-key}"`

#### Server Naming Conventions

| Convention  | Examples                              | Avoid                                   |
| ----------- | ------------------------------------- | --------------------------------------- |
| **Format**  | `githubIntegration`, `databaseHelper` | `github integration`, `database-helper` |
| **Style**   | camelCase, descriptive, unique names  | whitespace, special characters          |
| **Purpose** | Reflect functionality or brand        | Generic names like `server1`            |

### Synchronization Across Devices

Enable MCP server synchronization with Settings Sync:

1. Run `Settings Sync: Configure` from Command Palette
2. Ensure "MCP Servers" is included in synchronized configurations
3. Your MCP server configurations will sync across devices

### Development and Debugging

#### Debug Mode Configuration

Add development configuration to server definition:

```json
{
  "servers": {
    "my-server": {
      "command": "node",
      "args": ["build/index.js"],
      "dev": {
        "watch": "build/**/*.js",
        "debug": { "type": "node" }
      }
    }
  }
}
```

Supports debugging for Node.js and Python servers.

### Troubleshooting

#### MCP Troubleshooting Issues

| Issue                          | Symptoms                                  | Primary Solution                                                      |
| ------------------------------ | ----------------------------------------- | --------------------------------------------------------------------- |
| **Server not starting**        | Server fails to launch                    | Check server logs: `MCP: List Servers` > Show Output                  |
| **Docker servers not working** | Container-based servers fail              | Don't use detached mode (`-d` option) - server must run in foreground |
| **Tools not appearing**        | MCP tools missing from agent mode         | Restart server: Right-click server > Restart                          |
| **128 tools limit error**      | "Cannot have more than 128 tools" message | Deselect unnecessary tools in tools picker                            |

**Additional troubleshooting steps:**

- **Server issues**: Verify command/path is correct, check environment variables and permissions
- **Tool visibility**: Clear cached tools (`MCP: Reset Cached Tools`), check server trust (`MCP: Reset Trust`)
- **Tool limits**: Enable virtual tools (`github.copilot.chat.virtualTools.threshold`), use tool sets for organization

---

## 7. 🤖 Generate Instructions

Automatically generate custom instructions based on your codebase.

### How it Works

1. Analyzes your project structure
2. Identifies patterns and conventions
3. Generates appropriate instructions
4. Suggests team guidelines

### Using Generate Instructions

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

### Exercise 1: Set Up Custom Instructions

1. Enable the `github.copilot.chat.codeGeneration.useInstructionFiles` setting
2. Create `.github/copilot-instructions.md` with general coding standards
3. Create a language-specific instruction file (e.g., `python-standards.instructions.md`) with `applyTo: "**/*.py"`
4. Test both instruction types with code generation requests

### Exercise 2: Create Prompt Files

1. Enable the `chat.promptFiles` setting in VS Code
2. Create a code review prompt file (`code-review.prompt.md`) in `.github/prompts/`
3. Create a documentation prompt file (`generate-docs.prompt.md`) with input variables
4. Test both prompts using `/` command in chat and the editor play button

### Exercise 3: Create and Use Tool Sets

1. **Create a Custom Tool Set:**

   - Open Chat view and select Configure Chat → Tool Sets
   - Create a new tool sets file
   - Define a "reader" tool set with: `changes`, `codebase`, `fetch`, `findTestFiles`, `githubRepo`, `problems`, `usages`
   - Define a "webDev" tool set with: `codebase`, `search`, `githubRepo`, `fetch`

2. **Test Tool Sets:**

   - Enable agent mode in Chat view
   - Select Tools icon and choose your custom tool sets
   - Try using `#reader` in a prompt: "Analyze the codebase structure #reader"
   - Try using `#webDev` in a prompt: "Create a modern web page #webDev"

3. **Reference in Chat Modes:**
   - Create a custom chat mode that uses your tool sets in the `tools` array
   - Test how the tool set affects the chat behavior

### Exercise 4: Test Different Modes

1. Try the same request in different modes
2. Compare the responses
3. Identify best mode for different tasks

### Exercise 5: Create Custom Chat Modes

1. **Create a Planning Chat Mode:**

   - Open Chat view and select Configure Chat → Modes
   - Choose "Create new custom chat mode file"
   - Create a "plan.chatmode.md" file in `.github/chatmodes/`
   - Configure with planning-specific tools: `['codebase', 'fetch', 'findTestFiles', 'githubRepo', 'search', 'usages']`
   - Add instructions that focus on generating implementation plans without making code changes

2. **Create a Code Review Chat Mode:**

   - Create "code-review.chatmode.md" with tools: `["codebase", "search", "usages", "findTestFiles"]`
   - Include instructions for security analysis, performance review, and code quality checks
   - Test the mode by asking it to review a code file

3. **Test Different Chat Modes:**

   - Try the same development task in different modes (Ask, Edit, Agent, and your custom modes)
   - Compare the responses and behavior
   - Document which mode works best for different types of tasks

4. **Share Team Chat Modes:**

   - Commit your `.github/chatmodes/` folder to version control
   - Test that team members can access the custom modes
   - Gather feedback and iterate on the mode instructions

### Exercise 6: Set Up and Use MCP Servers

1. **Install MCP Server from Catalog:**

   - Visit [VS Code MCP catalog](https://code.visualstudio.com/mcp)
   - Choose a server based on your interests:
     - **Developer Tools**: GitHub, Playwright, or Microsoft Docs
     - **Productivity**: Notion, Linear, or Sequential Thinking
     - **Data & Analytics**: DuckDB, MongoDB, or Firecrawl
   - Click "Install in VS Code" and follow setup prompts
   - Configure any required API keys or credentials

2. **Manual MCP Server Setup:**

   - Run `MCP: Open User Configuration` from Command Palette
   - Add the GitHub MCP server configuration (see Popular MCP Servers section)
   - Set up input variables for your GitHub token
   - Test server installation using `MCP: List Servers`

3. **Use MCP Tools in Agent Mode:**

   - Enable Agent mode in Chat view
   - Select Tools and choose your installed MCP tools
   - Try specific prompts based on your server:
     - GitHub: "List my recent repositories" or "Create a new issue"
     - Notion: "Show my recent Notion pages"
     - Sequential Thinking: "Break down this complex feature into steps"
   - Observe tool confirmations and parameter editing

4. **Explore MCP Resources and Prompts:**

   - Use "Add Context" > "MCP Resources" in chat
   - Try MCP prompts using `/mcp.servername.promptname` format
   - Browse available resources with `MCP: Browse Resources`
   - Save returned resources to your workspace

### Exercise 7: Configure Tool Sets with MCP Tools

1. **Create MCP-Enhanced Tool Set:**

   - Open Configure Chat → Tool Sets
   - Create a tool set that combines built-in tools with MCP tools
   - Test the tool set in different chat modes

### Exercise 8: Generate Instructions Automatically

1. **Use Auto-Generation Feature:**

   - Open Chat view and select Configure Chat → Generate Instructions
   - Choose analysis scope (workspace or repository)
   - Review the automatically generated instructions

2. **Customize Generated Instructions:**

   - Edit the generated instructions to match your team's needs
   - Save to `.github/copilot-instructions.md`
   - Test how the instructions affect code generation

3. **Compare Manual vs Auto-Generated:**

   - Create manual instructions for comparison
   - Test both sets with similar code generation tasks
   - Identify strengths and gaps in auto-generation

---

## 🎯 Expected Outcomes

After completing this demo, you should be able to:

- ✅ Configure both workspace-wide and file-specific custom instructions
- ✅ Create and use reusable prompt files with variables and YAML frontmatter
- ✅ Select appropriate tool sets for your development stack
- ✅ Switch between Ask, Edit, and Agent modes effectively
- ✅ Create and manage custom chat modes with proper YAML frontmatter
- ✅ Configure chat modes with specific tools and AI models
- ✅ Use chat mode dropdown to switch between different configurations
- ✅ Store custom chat modes for team sharing in workspace
- ✅ Reference instruction files within chat modes for complementary behavior
- ✅ Set up and configure MCP servers using multiple methods (catalog, manual, command-line)
- ✅ Use MCP tools, resources, and prompts effectively in agent mode
- ✅ Manage MCP server lifecycle (start, stop, restart, debug)
- ✅ Configure server security and trust settings appropriately
- ✅ Create tool sets that combine built-in and MCP tools
- ✅ Troubleshoot common MCP server issues and debug problems
- ✅ Generate custom instructions automatically from codebase analysis
- ✅ Sync MCP configurations and custom settings across devices
- ✅ Apply instructions using glob patterns for targeted file types
- ✅ Sync custom instructions and prompt files across devices

---

## 🔍 Troubleshooting

### Common Issues Summary

| Issue Category   | Problem            | Quick Fix                                                               |
| ---------------- | ------------------ | ----------------------------------------------------------------------- |
| **Instructions** | Not being followed | Enable `github.copilot.chat.codeGeneration.useInstructionFiles` setting |
| **Prompt Files** | Not appearing      | Check file extension (`.prompt.md`) and location                        |
| **Tool Sets**    | Not working        | Ensure `.jsonc` extension and enable agent mode                         |
| **Chat Modes**   | Not appearing      | Verify `.chatmode.md` extension and YAML frontmatter                    |
| **MCP Servers**  | Not starting       | Check server logs and command/path                                      |

### Detailed Troubleshooting

#### Instructions Issues

| Problem                       | Primary Solution                            | Additional Steps                                   |
| ----------------------------- | ------------------------------------------- | -------------------------------------------------- |
| **Instructions not followed** | Enable `useInstructionFiles` setting        | Check file location, syntax, restart VS Code       |
| **Files not detected**        | Verify file extensions (`.instructions.md`) | Check YAML frontmatter, confirm `applyTo` patterns |

#### Prompt & Chat Mode Issues

| Problem                   | Primary Solution                             | Additional Steps                                   |
| ------------------------- | -------------------------------------------- | -------------------------------------------------- |
| **Prompt files missing**  | Check `.prompt.md` extension                 | Enable `chat.promptFiles` setting, verify location |
| **Variables not working** | Use correct syntax: `${name}` not `{{name}}` | Check YAML frontmatter format                      |
| **Chat modes missing**    | Verify `.chatmode.md` extension              | Check YAML frontmatter syntax, restart VS Code     |

#### Tool & MCP Issues

| Problem                   | Primary Solution         | Additional Steps                                    |
| ------------------------- | ------------------------ | --------------------------------------------------- |
| **Tool sets not working** | Check `.jsonc` extension | Enable agent mode, verify JSON syntax               |
| **128 tools limit**       | Deselect unused tools    | Enable virtual tools setting, use smaller tool sets |
| **MCP servers failing**   | Check server logs        | Verify configuration, reset cached tools            |

---

## 📚 Additional Resources

- **[VS Code MCP Catalog](https://code.visualstudio.com/mcp)** - Curated list of MCP servers with one-click installation
- [GitHub Copilot Documentation](https://docs.github.com/en/copilot)
- [VS Code Copilot Extension Guide](https://code.visualstudio.com/docs/copilot/overview)
- [VS Code Copilot Customization Overview](https://code.visualstudio.com/docs/copilot/customization/overview)
- [Custom Instructions Documentation](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [Prompt Files Documentation](https://code.visualstudio.com/docs/copilot/customization/prompt-files)
- [Custom Chat Modes Documentation](https://code.visualstudio.com/docs/copilot/customization/custom-chat-modes)
- [Agent Mode and Tool Sets](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode#_agent-mode-tools)
- [Language Models Documentation](https://code.visualstudio.com/docs/copilot/customization/language-models)
- [MCP Servers Documentation](https://code.visualstudio.com/docs/copilot/customization/mcp-servers)
- [MCP Protocol Specification](https://modelcontextprotocol.io/)
- [Official MCP Server Repository](https://github.com/modelcontextprotocol/servers)
- [Prompt Engineering Best Practices](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
- [Awesome Copilot Community Examples](https://github.com/github/awesome-copilot)

---

## 🎓 Next Steps

1. **Implement in your projects**: Apply these configurations to real projects
2. **Share with your team**: Distribute instructions and prompt files
3. **Iterate and improve**: Refine based on team feedback
4. **Explore enterprise features**: If available, explore additional enterprise capabilities
