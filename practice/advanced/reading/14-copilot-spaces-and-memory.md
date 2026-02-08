# Copilot Spaces and Memory

## Overview

Even the most capable AI coding agent is only as good as the context it receives.
**Copilot Spaces** solves the context curation problem by letting you assemble
curated collections of code, documentation, issues, and discussions that ground
Copilot's responses in exactly the information that matters. **Copilot Memory**
complements this by persisting your coding preferences, conventions, and patterns
across sessions, so the agent learns and adapts over time. This guide covers both
features in depth.

---

## 1. Copilot Spaces

### What Are Spaces?

Copilot Spaces are curated context collections on GitHub.com. Rather than relying
on Copilot to search your entire codebase for relevant context (which can miss
important files or include irrelevant ones), Spaces let you explicitly define
**what information Copilot should know about** when answering questions or
generating code.

Think of a Space as a "reading list" for the AI -- a hand-picked set of files,
docs, and discussions that represent the knowledge needed for a specific task,
project area, or domain.

### Why Context Curation Matters

| Without Spaces | With Spaces |
|---------------|-------------|
| Copilot searches the entire repo (may miss relevant files) | Copilot focuses on your curated selection |
| Irrelevant files consume context window tokens | Every token is spent on relevant information |
| Responses may not reflect project-specific conventions | Responses are grounded in your chosen references |
| Onboarding a new developer means explaining everything | Share a Space to transfer domain knowledge instantly |
| Context varies between sessions | Consistent context across every session using the Space |

### Creating Spaces on GitHub.com

1. Navigate to **github.com** and open the Copilot Spaces interface (accessible
   from the Copilot menu or repository sidebar).
2. Click **"New Space"**.
3. Provide a **name** that clearly identifies the Space's purpose (e.g.,
   "Authentication System", "API Design Patterns", "Q4 Migration").
4. Add a **description** explaining what the Space covers and when to use it.
5. Begin adding content (see Content Types below).

### Content Types

Spaces can include several types of content, each serving a different purpose:

| Content Type | What It Provides | Example |
|-------------|-----------------|---------|
| **Code files** | Implementation details, patterns, conventions | `src/auth/jwt.ts`, `src/api/middleware/rate-limit.ts` |
| **Documentation** | Architecture decisions, API specs, design docs | `docs/architecture.md`, `docs/api-spec.yaml` |
| **Issues** | Requirements, bug reports, feature requests | Issue #142: "Implement OAuth2 PKCE flow" |
| **PR discussions** | Design decisions, review feedback, rationale | PR #87: "Refactor user service" |
| **Markdown notes** | Custom context you write directly in the Space | "Our team uses snake_case for database columns" |

### Adding Content to a Space

**Adding code files:**
- Browse your repository and select specific files or directories.
- Use search to find files by name or content.
- Pin specific file versions (commit SHA) for stability, or use HEAD for
  the latest version.

**Adding issues and PRs:**
- Search by issue number, title, or label.
- The full issue body, comments, and linked PRs are included.
- Closed issues and merged PRs are valid -- they contain valuable historical
  context and decisions.

**Adding documentation:**
- Select markdown files, wiki pages, or other documentation.
- External documentation can be added as markdown notes with links.

### Using Spaces

Once created, a Space can be activated when interacting with Copilot:

- **In Copilot Chat on GitHub.com:** Select the Space from the context picker
  before asking a question.
- **In VS Code:** Reference the Space by name in your prompt, or configure it
  as the default context for a workspace.
- **In Copilot CLI:** Use the `--space` flag to ground agent tasks in a
  specific Space.

**Example interaction with a Space:**

```
[Space: "Authentication System" active]

User: How should I implement the password reset flow?

Copilot: Based on the authentication patterns in your Space, I can see that
your project uses JWT tokens with short-lived reset tokens (15-minute expiry)
stored in Redis. Following the pattern in `src/auth/jwt.ts` and the
architecture decision in `docs/auth-architecture.md`, here's how to
implement the password reset flow...
```

Without the Space, Copilot might suggest a generic password reset implementation.
With the Space, it follows your project's established patterns.

---

## 2. Collaboration and Sharing

### Sharing Spaces with Team Members

Spaces can be shared at multiple levels:

| Sharing Level | Who Can Access | Use Case |
|--------------|---------------|----------|
| **Private** | Only you | Personal reference, exploratory work |
| **Team** | Specific GitHub team | Domain-specific knowledge for a team |
| **Repository** | All repo contributors | Project-wide context |
| **Organization** | All org members | Organization standards and conventions |

### Knowledge Bases

Spaces function as **living knowledge bases** for your team:

- **Onboarding.** Create a "Getting Started" Space with architecture docs,
  coding conventions, and key implementation files. New team members can
  activate it immediately.
- **Domain expertise.** Create Spaces per domain (auth, payments, search) so
  team members working in unfamiliar areas get grounded context.
- **Incident response.** Create Spaces with runbooks, monitoring configs, and
  past incident post-mortems for on-call engineers.

---

## 3. Available Plans

Copilot Spaces availability varies by subscription plan:

| Feature | Free | Pro | Team | Enterprise Cloud |
|---------|------|-----|------|-----------------|
| Create Spaces | Yes (limited) | Yes | Yes | Yes |
| Private Spaces | Yes | Yes | Yes | Yes |
| Shared Spaces | No | Yes | Yes | Yes |
| Organization Spaces | No | No | Yes | Yes |
| Space analytics | No | No | No | Yes |
| Max content items per Space | 10 | 50 | 100 | Unlimited |
| Max Spaces | 5 | 25 | Unlimited | Unlimited |
| Admin controls | No | No | Limited | Full |

---

## 4. Copilot Memory

### What Is Copilot Memory?

Copilot Memory is an **agentic memory system** that persists information across
chat sessions. Unlike Spaces (which you curate manually), Memory is built up
organically as you interact with Copilot. The agent learns your preferences,
project conventions, and patterns, then applies them automatically in future
sessions.

### What Gets Remembered

| Category | Examples |
|----------|---------|
| **Coding preferences** | "Prefers functional components over class components", "Uses 2-space indentation" |
| **Project conventions** | "Tests go in `__tests__/` directories", "API responses use camelCase" |
| **Architectural patterns** | "Uses repository pattern for data access", "Events go through the message bus" |
| **Tool preferences** | "Uses pytest for testing", "Prefers pnpm over npm" |
| **Communication style** | "Prefers concise responses", "Wants explanations with code examples" |

### How Memory Works

```
Session 1: "Always use TypeScript strict mode in this project."
    │
    ▼
Memory stored: { preference: "TypeScript strict mode", scope: "project" }
    │
    ▼
Session 2: (User asks to create a new component)
    │
    ▼
Copilot automatically applies strict mode without being reminded.
```

Memory is built through:
- **Explicit instructions.** "Remember that we use PostgreSQL, not MySQL."
- **Observed patterns.** After you correct Copilot's output multiple times,
  it learns the pattern.
- **Agent-initiated learning.** The agent may ask "Should I remember this
  preference for future sessions?" after noticing a consistent pattern.

### Privacy and Scoping

Memory is designed with privacy as a core concern:

| Property | Detail |
|----------|--------|
| **Scoped per user** | Your memories are never shared with other users |
| **Viewable** | You can view all stored memories at any time |
| **Manageable** | You can edit or delete individual memories |
| **No training data** | Memories are not used to train models |
| **Scope levels** | Global (all projects) or project-specific |

### Viewing and Managing Memory

**In VS Code:**
- Open the Copilot memory panel to see all stored memories.
- Filter by scope (global vs. project-specific).
- Delete individual memories or clear all memories.

**In Copilot CLI:**
```bash
# View all memories
gh copilot memory list

# View project-specific memories
gh copilot memory list --scope project

# Delete a specific memory
gh copilot memory delete <memory-id>

# Clear all memories
gh copilot memory clear
```

### Claude Agent /memory Command

When using Claude Agent as a partner agent, the `/memory` command provides
explicit memory management:

```
/memory list              -- Show all stored memories
/memory add "preference"  -- Explicitly add a memory
/memory remove <id>       -- Remove a specific memory
/memory clear             -- Clear all memories
/memory search "keyword"  -- Search memories by keyword
```

**Example usage:**

```
/memory add "This project uses Django 5.0 with PostgreSQL 16"
/memory add "Always include type hints in Python function signatures"
/memory add "Our CI pipeline runs on GitHub Actions with the ubuntu-latest runner"
```

These explicit memories are applied across all future Claude Agent sessions
for the current user.

---

## 5. Best Practices

### Organizing Spaces by Task

Create focused Spaces rather than all-encompassing ones:

| Approach | Space Name | Contents |
|----------|-----------|----------|
| Good | "Auth Module Development" | Auth code, auth tests, auth docs, auth-related issues |
| Bad | "Everything About Our App" | Entire codebase, all docs, all issues |
| Good | "Q4 Database Migration" | Migration scripts, schema docs, related PRs |
| Bad | "Database Stuff" | Every file that touches the database |

### Maintaining Currency

Spaces become stale if not maintained:

- **Review quarterly.** Remove files that are no longer relevant. Add new files
  that reflect current architecture.
- **Pin versions for stability.** When a Space references a design document,
  pin it to a specific commit so it does not change unexpectedly.
- **Use HEAD for active code.** For implementation files, use the latest version
  so the Space always reflects current state.
- **Archive completed Spaces.** After a migration or feature launch, archive
  the Space rather than deleting it -- it serves as historical context.

### Combining Spaces with Custom Instructions

Spaces and custom instructions (`.github/copilot-instructions.md`) are
complementary:

| Mechanism | Purpose | Scope |
|-----------|---------|-------|
| Custom instructions | "How to behave" -- coding style, conventions, rules | Always active |
| Spaces | "What to know about" -- specific files, docs, context | Activated per task |
| Memory | "What to remember" -- preferences learned over time | Persistent |

**Optimal combination:**
1. Custom instructions define your global coding standards.
2. Spaces provide task-specific context when needed.
3. Memory fills in personal preferences and project patterns automatically.

### When to Use Each

| Situation | Use |
|-----------|-----|
| "Copilot should always follow our style guide" | Custom instructions |
| "Copilot needs to understand our auth system for this task" | Space |
| "Copilot should remember I prefer verbose error messages" | Memory |
| "New team member needs to understand the payment module" | Shared Space |
| "Copilot keeps forgetting we use pnpm" | Memory (explicit add) |

---

## Summary

Copilot Spaces and Memory address two fundamental challenges in AI-assisted
development: context quality and continuity. Spaces give you explicit control
over what information grounds Copilot's responses, ensuring relevance and
consistency. Memory provides continuity across sessions, so Copilot gets
smarter and more aligned with your preferences over time. Used together with
custom instructions, they create a layered context system that makes Copilot
significantly more effective for real-world development workflows.

---

## Further Reading

- [GitHub Copilot Spaces Documentation](https://docs.github.com/en/copilot/using-github-copilot/using-copilot-spaces)
- [GitHub Copilot Memory Documentation](https://docs.github.com/en/copilot/customizing-copilot/managing-copilot-memory)
- Reading 01: Advanced Prompt Engineering (custom instructions)
- Reading 10: Modern Copilot Workflows (context management)
- Reading 13: Agent Skills and Custom Agents (complementary configuration)
