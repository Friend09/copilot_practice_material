# Agent Skills and Custom Agents

## Overview

As the GitHub Copilot ecosystem evolves, two powerful configuration mechanisms
have emerged for extending agent behavior: **Agent Skills** (SKILL.md files
following the agentskills.io open standard) and **Custom Agents** (.agent.md
files, the evolution of .chatmode.md). Together, they enable developers to
package domain expertise, define specialized workflows, and share reusable
agent configurations across teams, organizations, and platforms. This guide
covers both systems in depth, including formats, storage, progressive disclosure,
handoff patterns, and migration from legacy approaches.

---

## 1. Agent Skills (SKILL.md)

### What Are Agent Skills?

Agent Skills are portable, declarative instruction sets that teach an AI coding
agent how to perform a specific task or operate within a specific domain. They
follow the **agentskills.io** open standard, making them interoperable across
platforms: VS Code, Copilot CLI, the Copilot coding agent, and compatible
third-party tools.

A SKILL.md file is analogous to a README for humans, but written for AI agents.
It tells the agent what the skill does, how to use it, and where to find
additional resources.

### SKILL.md Format

Every SKILL.md file has two parts: **YAML frontmatter** and a **markdown body**.

```markdown
---
name: "django-rest-api"
description: "Build and maintain Django REST Framework APIs following team conventions"
---

# Django REST API Skill

## Instructions

When creating or modifying Django REST Framework APIs:

1. Always use `ModelSerializer` unless custom field handling is required.
2. Use `ViewSet` classes with explicit `queryset` and `serializer_class`.
3. Apply `IsAuthenticated` permission by default; override per-view when needed.
4. Write OpenAPI-compatible docstrings on all view methods.
5. Register routes in `urls.py` using `DefaultRouter`.

## File References

- `src/api/serializers/base.py` -- Base serializer with common validation logic
- `src/api/views/mixins.py` -- Shared view mixins for pagination and filtering
- `src/api/permissions.py` -- Custom permission classes
- `docs/api-conventions.md` -- Team API design conventions
```

### Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique identifier for the skill (kebab-case recommended) |
| `description` | Yes | One-line description of what the skill does |
| `version` | No | Semantic version (e.g., "1.2.0") |
| `author` | No | Creator or maintaining team |
| `tags` | No | List of tags for discovery (e.g., ["python", "django", "api"]) |
| `platforms` | No | List of supported platforms (e.g., ["vscode", "cli", "cloud"]) |

### Storage Locations

SKILL.md files can be stored at three levels, each with a different scope:

| Location | Scope | Discovery |
|----------|-------|-----------|
| `.github/skills/` | Repository-level | Automatically discovered by Copilot in this repo |
| `~/.copilot/skills/` | User-level | Available across all repositories for this user |
| `chat.agentSkillsLocations` setting | Custom paths | VS Code setting pointing to additional skill directories |

**Repository-level example:**
```
my-project/
├── .github/
│   └── skills/
│       ├── django-rest-api/
│       │   └── SKILL.md
│       ├── react-components/
│       │   └── SKILL.md
│       └── database-migrations/
│           └── SKILL.md
```

**User-level example:**
```
~/.copilot/
└── skills/
    ├── my-coding-style/
    │   └── SKILL.md
    └── git-workflow/
        └── SKILL.md
```

### Three-Level Progressive Disclosure

Agent Skills follow a **progressive disclosure** model to optimize context usage:

```
Level 1: Metadata Only
┌──────────────────────────────┐
│ name: "django-rest-api"      │
│ description: "Build Django   │
│   REST Framework APIs..."    │
└──────────────────────────────┘
   Agent sees this in skill index.
   Decides whether to load more.

Level 2: Instructions
┌──────────────────────────────┐
│ Full markdown body with      │
│ instructions, conventions,   │
│ and guidelines.              │
└──────────────────────────────┘
   Loaded when the skill is
   activated for a task.

Level 3: Referenced Resources
┌──────────────────────────────┐
│ Actual file contents from    │
│ referenced paths:            │
│ - base.py                    │
│ - mixins.py                  │
│ - api-conventions.md         │
└──────────────────────────────┘
   Loaded on-demand when the
   agent needs specific details.
```

This three-level approach prevents unnecessary context consumption. The agent
only loads what it needs, when it needs it.

### Cross-Platform Compatibility

The same SKILL.md file works across all Copilot surfaces:

| Platform | How Skills Are Used |
|----------|-------------------|
| **VS Code** | Automatically discovered and offered in Agent Mode chat |
| **Copilot CLI** | Available via `gh copilot agent --skill <name>` |
| **Copilot coding agent** | Discovered from `.github/skills/` in the repository |
| **Third-party tools** | Any tool supporting agentskills.io can consume SKILL.md |

---

## 2. Custom Agents (.agent.md)

### What Are Custom Agents?

Custom Agents are fully configured AI personas defined in `.agent.md` files. They
go beyond skills by specifying not just instructions but also **tools, sub-agents,
model preferences, handoff patterns, and MCP server connections**. They represent
the evolution of the earlier `.chatmode.md` format.

Where a Skill says "here's how to do X," a Custom Agent says "I am an agent that
does X, using these tools, with these capabilities, following these workflows."

### .agent.md Format

```markdown
---
name: "fullstack-developer"
description: "Full-stack development agent for React + Node.js projects"
tools:
  - codebase
  - terminal
  - browser
  - agent
agents:
  - "test-runner"
  - "code-reviewer"
model: "gpt-4o"
mcp-servers:
  - "database-explorer"
  - "api-tester"
handoffs:
  - target: "code-reviewer"
    trigger: "implementation complete"
    auto-submit: true
  - target: "test-runner"
    trigger: "code review passed"
    auto-submit: false
---

# Full-Stack Developer Agent

You are a senior full-stack developer specializing in React frontends and
Node.js backends. Follow these principles:

## Frontend (React)
- Use functional components with hooks exclusively.
- Apply TypeScript strict mode for all new components.
- Follow the component structure in `src/components/README.md`.

## Backend (Node.js)
- Use Express.js with middleware-based architecture.
- Apply input validation with Zod schemas on all endpoints.
- Write integration tests for every new route.

## Workflow
1. Understand the requirement fully before writing code.
2. Implement the backend API first.
3. Build the frontend component to consume the API.
4. Write tests for both layers.
5. Hand off to @code-reviewer for review.
6. After review approval, hand off to @test-runner for full test suite.
```

### Frontmatter Fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Display name for the agent |
| `description` | Yes | Brief description shown in agent picker |
| `tools` | No | List of tools the agent can use |
| `agents` | No | List of sub-agents this agent can invoke |
| `model` | No | Preferred model (e.g., "gpt-4o", "claude-sonnet-4", "o3-mini") |
| `mcp-servers` | No | List of MCP servers to connect |
| `handoffs` | No | Workflow transitions to other agents |
| `user-invokable` | No | Whether users can select this agent directly (default: true) |
| `disable-model-invocation` | No | Prevent other agents from spawning this agent (default: false) |

### Handoff Patterns

Handoffs define how agents transition work between each other, enabling
**sequential workflows**.

#### Sequential Workflow

```yaml
handoffs:
  - target: "code-reviewer"
    trigger: "implementation complete"
    auto-submit: true
  - target: "deployer"
    trigger: "review approved"
    auto-submit: false
```

#### Auto-Submit vs. Manual Transitions

| Mode | Behavior |
|------|----------|
| `auto-submit: true` | The agent automatically hands off to the target when the trigger condition is met. No user interaction required. |
| `auto-submit: false` | The agent notifies the user that handoff is ready and waits for explicit confirmation before transitioning. |

#### Handoff Workflow Visualization

```
┌──────────────┐    auto-submit    ┌──────────────┐    manual     ┌──────────────┐
│  Full-Stack  │ ──────────────►   │    Code      │ ──────────►   │   Deployer   │
│  Developer   │  "impl complete"  │   Reviewer   │  "approved"   │              │
└──────────────┘                   └──────────────┘               └──────────────┘
```

### Storage Locations

| Location | Scope | Discovery |
|----------|-------|-----------|
| `.github/agents/` | Repository-level | Available to all contributors |
| `~/.copilot/agents/` | User-level | Available across all repos for this user |
| Organization settings | Org-level | Available to all org members |

**Repository-level example:**
```
my-project/
├── .github/
│   └── agents/
│       ├── fullstack-developer.agent.md
│       ├── code-reviewer.agent.md
│       ├── test-runner.agent.md
│       └── deployer.agent.md
```

---

## 3. Tool Priority Chain

When multiple configuration sources specify tool access, they are resolved in
a strict priority order:

```
Highest priority
      │
      ▼
┌─────────────────────┐
│   Prompt File        │  tools: specified in .prompt.md frontmatter
│   (.prompt.md)       │  Overrides everything below
├─────────────────────┤
│   Custom Agent       │  tools: specified in .agent.md frontmatter
│   (.agent.md)        │  Overrides default tool set
├─────────────────────┤
│   Default Tools      │  Platform default tool set
│                      │  (codebase, terminal, file, etc.)
└─────────────────────┘
      │
      ▼
Lowest priority
```

**Implication:** If a prompt file specifies `tools: [codebase]`, the agent will
ONLY have access to the codebase tool for that prompt, even if the custom agent
it runs within has `tools: [codebase, terminal, browser]` configured.

---

## 4. Migration Guide

### From Extensions/Skillsets to Agent Skills

The older Copilot Extensions and Skillsets system is being superseded by Agent
Skills. Here is how to migrate:

| Old System | New System | Migration Steps |
|------------|------------|-----------------|
| Copilot Extension (GitHub App) | Agent Skill (SKILL.md) | Extract instructions into SKILL.md, move referenced files into skill directory |
| Skillset (API-based) | Agent Skill (SKILL.md) | Convert API endpoint descriptions into markdown instructions, reference API specs as files |
| Custom tool integration | MCP Server + Agent Skill | Implement tool as MCP server, create SKILL.md with usage instructions |

**Example migration -- Skillset to SKILL.md:**

Before (Skillset API definition):
```json
{
  "name": "code-quality",
  "description": "Analyze code quality metrics",
  "endpoints": [
    {
      "path": "/analyze",
      "method": "POST",
      "description": "Analyze a file for code quality"
    }
  ]
}
```

After (SKILL.md):
```markdown
---
name: "code-quality"
description: "Analyze code quality metrics using team standards"
---

# Code Quality Analysis

## Instructions

When analyzing code quality:

1. Check cyclomatic complexity (threshold: 10 per function).
2. Verify test coverage meets minimum (80% line coverage).
3. Ensure no functions exceed 50 lines.
4. Validate naming conventions per `docs/naming-conventions.md`.

## File References

- `config/quality-rules.json` -- Quality rule definitions
- `docs/naming-conventions.md` -- Naming convention guide
```

### From .chatmode.md to .agent.md

The `.chatmode.md` format has been replaced by `.agent.md`. The migration is
straightforward:

| .chatmode.md Field | .agent.md Equivalent | Notes |
|-------------------|---------------------|-------|
| `name` | `name` | No change |
| `description` | `description` | No change |
| `tools` | `tools` | No change |
| (not available) | `agents` | New: sub-agent declarations |
| (not available) | `model` | New: model preference |
| (not available) | `handoffs` | New: workflow transitions |
| (not available) | `mcp-servers` | New: MCP server connections |
| (not available) | `disable-model-invocation` | New: invocation control |

**Steps to migrate:**

1. Rename `.chatmode.md` files to `.agent.md`.
2. Move files from `.github/chatmodes/` (if applicable) to `.github/agents/`.
3. Review and add new frontmatter fields (`agents`, `model`, `handoffs`, etc.)
   to take advantage of the expanded capabilities.
4. Update any references in documentation or team guides.

---

## 5. Community Ecosystem

### Discovering Skills and Agents

The community has created repositories for sharing reusable skills and agents:

| Repository | Description |
|------------|-------------|
| `github/awesome-copilot` | Curated list of Copilot skills, agents, and configurations |
| `anthropics/skills` | Agent Skills from Anthropic for Claude-based workflows |
| `agentskills-io/registry` | Community registry of agentskills.io-compatible skills |

### Contributing Skills

To share a skill with the community:

1. Create a well-documented SKILL.md following the agentskills.io standard.
2. Include example usage scenarios.
3. Test across multiple platforms (VS Code, CLI, cloud).
4. Submit to the relevant community repository.

### Organization-Level Sharing

Organizations can share skills and agents across all repositories:

**Organization Skills:**
```
my-org/.github/
├── skills/
│   ├── org-coding-standards/
│   │   └── SKILL.md
│   ├── org-security-review/
│   │   └── SKILL.md
│   └── org-deployment/
│       └── SKILL.md
```

**Organization Agents:**
```
my-org/.github/
├── agents/
│   ├── senior-developer.agent.md
│   ├── security-auditor.agent.md
│   └── release-manager.agent.md
```

These are automatically available to all repositories within the organization,
providing consistent workflows and standards.

### Organization Configuration

Admins can manage agent and skill availability at the organization level:

| Setting | Description |
|---------|-------------|
| Allowed skills | Whitelist of skills that can be used in org repos |
| Blocked skills | Skills prohibited for security or compliance reasons |
| Required skills | Skills automatically applied to all agent sessions |
| Agent approval | Whether custom agents require admin approval |

---

## 6. Advanced Patterns

### Composing Skills with Agents

A custom agent can reference multiple skills to build a comprehensive workflow:

```markdown
---
name: "senior-fullstack"
description: "Senior full-stack developer with all team skills"
tools:
  - codebase
  - terminal
  - agent
---

# Senior Full-Stack Developer

You are a senior developer. Use the following skills based on the task:

- For API work, follow the `django-rest-api` skill.
- For frontend work, follow the `react-components` skill.
- For database changes, follow the `database-migrations` skill.
- For deployments, follow the `org-deployment` skill.

Always run tests before considering any task complete.
```

### Conditional Tool Access

Agents can describe conditional tool usage in their instructions:

```markdown
---
name: "cautious-developer"
description: "Developer agent with safety-first approach"
tools:
  - codebase
  - terminal
  - agent
---

# Cautious Developer

## Tool Usage Rules

- **Terminal:** Only use for running tests, linting, and build commands.
  Never use for `rm`, `mv`, or destructive operations without explicit
  user confirmation.
- **Agent:** Only spawn sub-agents for read-only analysis tasks. Never
  delegate file modifications to sub-agents.
- **Codebase:** Full access for reading and writing code files.
```

### Skill Versioning

When skills evolve, use versioning to manage transitions:

```markdown
---
name: "api-conventions"
description: "Team API design conventions"
version: "2.0.0"
---

# API Conventions v2.0

> **Breaking change from v1.x:** All endpoints now require pagination.
> See migration notes below.

## Current Standards (v2.0)
...

## Migration from v1.x
...
```

---

## Summary

Agent Skills and Custom Agents represent a significant maturation of the
Copilot ecosystem. Skills provide portable, platform-agnostic instruction
sets following the agentskills.io open standard, while Custom Agents define
fully configured personas with tools, models, handoffs, and sub-agents.
Together, they enable teams to encode their expertise, share workflows,
and build sophisticated multi-agent systems that operate consistently across
VS Code, CLI, and cloud environments.

---

## Further Reading

- [agentskills.io Specification](https://agentskills.io)
- [GitHub Copilot Custom Agents Documentation](https://docs.github.com/en/copilot/customizing-copilot)
- [GitHub Copilot Extensions Documentation](https://docs.github.com/en/copilot/using-github-copilot/using-extensions-to-integrate-external-tools)
- Reading 08: Copilot Extensions Ecosystem (legacy extension system)
- Reading 11: Multi-Agent Architecture (sub-agent patterns)
- Reading 12: Cloud and Background Agents (execution environments)
