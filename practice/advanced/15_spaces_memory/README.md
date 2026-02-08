# Module 15: Copilot Spaces and Memory

> **Last verified**: February 2026 | [Official Docs - Spaces](https://docs.github.com/en/copilot/using-github-copilot/using-copilot-spaces) | [Official Docs - Memory](https://docs.github.com/en/copilot/using-github-copilot/using-copilot-memory)

## Prerequisites and Access

- **GitHub Account**: With Copilot enabled (Free, Pro, Team, or Enterprise)
- **Access to GitHub.com**: Spaces are managed through the GitHub web interface
- **VS Code** (for Memory): Latest version with GitHub Copilot extension
- **Recommended**: At least one repository with documentation, issues, and pull requests for meaningful Space content

---

## Overview

This module covers two complementary GitHub Copilot features that bring **persistent context** to your AI-assisted development workflow:

1. **Copilot Spaces** -- Curated collections of content that ground Copilot's responses in the right context for specific tasks
2. **Copilot Memory** -- Agentic memory that persists your preferences and patterns across sessions

Together, these features solve one of the biggest limitations of AI assistants: starting from scratch every time you open a new conversation. With Spaces and Memory, Copilot has curated context from day one and learns your preferences over time.

---

## Section A: Copilot Spaces

### What Are Copilot Spaces?

Copilot Spaces are organized collections of relevant content that you curate to ground Copilot's responses in the right context for specific tasks. Think of a Space as a knowledge bundle -- a focused set of files, documentation, discussions, and notes that give Copilot the background it needs to provide accurate, project-specific answers.

### Why Spaces Matter

Without Spaces, every Copilot conversation starts fresh. You must re-explain your architecture, point to relevant files, and provide context before getting useful answers. With Spaces:

- Copilot has **curated context from day one** for any topic
- Responses are **grounded in your actual codebase** and documentation
- Team members share the **same foundational knowledge**
- Complex topics get **accurate, specific answers** instead of generic ones

### Creating a Space on GitHub.com

1. **Navigate to Spaces**: Go to [github.com/copilot/spaces](https://github.com/copilot/spaces), or click the Copilot icon in the GitHub navigation bar and select "Spaces"
2. **Create a new Space**: Click the "Create Space" button
3. **Name and describe the Space**: Give it a clear, descriptive name (e.g., "Payment Service Architecture") and a description that outlines what context it provides
4. **Add content** from multiple sources:
   - **Repository files**: Source code, configuration files, schema definitions
   - **Markdown documentation**: README files, architecture docs, API specs
   - **Issue threads**: Relevant discussions about design decisions or bugs
   - **Pull request discussions**: Code review threads with important context
   - **Freeform notes**: Your own written context, decisions, or guidelines
   - **External links**: References to relevant external documentation
5. **Save and refine**: Review the Space content and iterate as needed

### Content Types You Can Add

| Content Type | Use Case | Example |
|---|---|---|
| Code files | Ground answers in actual implementation | `src/auth/middleware.ts` |
| Markdown docs | Provide architectural context | `docs/architecture.md` |
| Issue threads | Include design decision discussions | `#142: Auth redesign proposal` |
| PR discussions | Reference code review context | `PR #89: OAuth2 implementation` |
| Freeform notes | Add personal context and guidelines | "We chose JWT over sessions because..." |
| External links | Reference third-party docs | API provider documentation |

### Using Spaces

- **Open a Space** before asking Copilot questions about that topic -- the Space content is automatically included as context
- Copilot uses the Space content to **ground its responses**, leading to more specific and accurate answers
- Works especially well for questions about **specific projects, APIs, or architectural decisions**
- You can switch between Spaces as you shift between different tasks or projects

### Collaboration with Spaces

Spaces become powerful when shared across teams:

- **Share Spaces with team members** to create a common knowledge base
- **Onboarding**: Create a "Getting Started" Space with everything a new team member needs
- **Cross-team projects**: Share Spaces to align context across different teams working on the same system
- **Knowledge preservation**: Capture institutional knowledge that persists even as team members rotate

### Available Plans

Copilot Spaces are available on:

- **Copilot Free**
- **Copilot Pro**
- **Copilot Team** (previously Copilot Business)
- **Copilot Enterprise Cloud**

---

## Section B: Copilot Memory

### What Is Copilot Memory?

Copilot Memory is an agentic feature that allows Copilot to **persist context across sessions**. Instead of forgetting everything when you close a conversation, Copilot remembers your preferences, patterns, and previously discussed context.

### How It Works

- Copilot stores **memories** based on your interactions -- things you explicitly tell it and patterns it observes
- When you start a new session, Copilot retrieves relevant memories to inform its responses
- Memory is **agentic**: Copilot decides what is worth remembering based on significance and relevance
- You can also **explicitly tell Copilot to remember something** (e.g., "Remember that I always use pytest for testing")

### What Copilot Remembers

| Category | Examples |
|---|---|
| Coding preferences | "I prefer functional style over class-based components" |
| Project conventions | "Our API routes follow RESTful naming with `/api/v2/` prefix" |
| Tool choices | "I use pytest with fixtures, not unittest" |
| Style preferences | "I prefer Google-style docstrings" |
| Previously discussed patterns | Architectural decisions from prior sessions |
| Project-specific context | Framework versions, deployment targets, team norms |

### Privacy and Control

- Memory is **scoped per user** -- your memories are never shared with other users
- You can **view all stored memories** and delete any you want removed
- Memory is **transparent**: you can see what Copilot has remembered about you
- Organization admins can enable or disable Memory at the policy level

### VS Code Integration

In VS Code with the Claude Agent (Copilot chat using Claude):

- Use the **`/memory`** slash command for explicit memory management
- `/memory` lets you view, add, or remove specific memories
- Useful for seeding Copilot with your preferences at the start of a project

### Limitations

- Memory is **probabilistic, not guaranteed recall** -- Copilot may not always surface every relevant memory
- Memory works best for **frequently reinforced patterns** rather than one-off mentions
- The feature is still evolving -- memory retrieval will improve over time
- Not all Copilot surfaces support memory equally; VS Code agent mode has the strongest support

---

## Exercises

### Exercise 1: Create a Copilot Space

Build a Space for a real-world scenario and test how it improves Copilot's responses.

**File**: `exercises/create_space.md`

### Exercise 2: Space Collaboration

Share a Space with your team and use it for onboarding and cross-team alignment.

**File**: `exercises/space_collaboration.md`

### Exercise 3: Memory Exploration

Work across multiple Copilot sessions to test how memory persists your coding preferences.

**File**: `exercises/memory_exploration.py`

### Exercise 4: Context Comparison

Systematically compare Copilot's responses with and without Space context to measure the impact.

**File**: `exercises/context_comparison.md`

---

## Key Takeaways

- **Spaces** solve the cold-start problem by giving Copilot curated, project-specific context from the beginning of every conversation
- **Memory** solves the continuity problem by persisting your preferences and patterns across sessions
- Both features are complementary: Spaces provide **project context**, Memory provides **personal context**
- Effective Spaces require intentional curation -- add the content that will most improve response quality
- Memory is probabilistic, so reinforce important preferences when needed
- Team collaboration through shared Spaces creates a multiplier effect on Copilot's usefulness
- Both features respect privacy boundaries: Spaces are shared intentionally, Memory is per-user

---

## Next Steps

- **Module 05**: Learn about MCP servers that can extend the tools available within Spaces
- **Module 09**: Use prompt files alongside Spaces for even more targeted context
- **Module 11**: Explore how sub-agents can leverage Space context for multi-step workflows
- **Module 12**: Create custom agents that work alongside your curated Spaces
