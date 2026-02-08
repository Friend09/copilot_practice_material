# Module 13: Agent Skills (SKILL.md Open Standard)

> **Last verified**: February 2026 | [Official Docs](https://code.visualstudio.com/docs/copilot/customization/agent-skills)

## Prerequisites and Access

- **VS Code**: Latest version (1.100+)
- **GitHub Copilot**: Pro, Business, or Enterprise subscription
- **Agent mode**: Enabled in settings (`chat.agent.enabled: true`)
- **Open standard specification**: [agentskills.io](https://agentskills.io)

---

## Overview

**Agent Skills** are portable, self-contained folders of instructions, scripts, and resources that GitHub Copilot automatically loads when they are relevant to a user's request. Unlike custom instructions (which apply globally) or prompt files (which are invoked explicitly), skills are **discovered dynamically** based on the semantic match between the user's question and the skill's metadata.

Agent Skills are built on an **open standard** defined at [agentskills.io](https://agentskills.io). This means skills are portable across multiple tools and environments:

- **VS Code** (Copilot Chat in Agent mode)
- **Copilot CLI** (terminal-based coding assistant)
- **Copilot Coding Agent** (GitHub Actions-powered autonomous agent)

Because skills follow a standard format, you can share them across teams, publish them for the community, and import skills authored by others with confidence that they will work in any compatible tool.

---

## Core Concepts

### 1. The SKILL.md File Format

Each skill is defined by a `SKILL.md` file placed in a skill directory. The file consists of two parts:

**YAML Frontmatter** (metadata for discovery):

```yaml
---
name: my-skill-name
description: A concise description of what this skill does and when to use it.
---
```

**Body** (instructions loaded when the skill is activated):

```markdown
# My Skill Name

Detailed instructions, guidelines, examples, and references to
additional resource files.

## Guidelines

1. Do this
2. Avoid that

## Resources

See [config reference](resources/config.md) for details.
Run [setup script](scripts/setup.sh) to initialize.
```

**Frontmatter rules:**

| Property | Constraints | Purpose |
|----------|-------------|---------|
| `name` | Lowercase with hyphens, max 64 characters | Unique identifier for the skill |
| `description` | Max 1024 characters | Tells Copilot when this skill is relevant; used for semantic matching |

**Body conventions:**

- Write clear, actionable instructions that Copilot should follow
- Use standard Markdown formatting (headings, lists, code blocks, tables)
- Reference additional files using **relative paths** (e.g., `[guide](resources/guide.md)`)
- Include examples of correct and incorrect patterns where applicable

### 2. Storage Locations

Skills can be stored in multiple locations depending on scope and sharing needs:

| Location | Scope | Sharing | Use Case |
|----------|-------|---------|----------|
| `.github/skills/<skill-name>/` | Workspace | Shared with team via git | **Recommended** for project-specific skills |
| `~/.copilot/skills/<skill-name>/` | Personal | Available in all your workspaces | Personal productivity skills |
| Custom paths via settings | Configurable | Varies | Organization-wide skill libraries |

**Directory structure example:**

```
.github/
  skills/
    python-code-quality/
      SKILL.md
      scripts/
        check_quality.py
      resources/
        style_guide.md
    api-design/
      SKILL.md
      resources/
        rest_conventions.md
        openapi_template.yaml
```

**Custom skill locations** can be added via the VS Code setting:

```json
{
  "chat.agentSkillsLocations": [
    "/path/to/shared/skills",
    "/another/skills/directory"
  ]
}
```

### 3. Three-Level Progressive Disclosure

Copilot does not load all skill content at once. Instead, it uses a three-level system that balances context efficiency with depth of information:

| Level | What Happens | When It Occurs | Context Cost |
|-------|-------------|----------------|--------------|
| **1. Discovery** | Copilot reads only the YAML frontmatter (`name` + `description`) from all available skills | Every request | Minimal |
| **2. Instructions** | Copilot loads the full SKILL.md body (instructions, guidelines, examples) | When the user's request semantically matches a skill's description | Moderate |
| **3. Resources** | Copilot reads additional files referenced in the body (scripts, configs, guides) | Only when the instructions explicitly reference them and the agent needs them | Variable |

**Why this matters:**

- You can have dozens of skills installed without bloating Copilot's context window
- Only the relevant skill's instructions are loaded for any given request
- Large reference files (style guides, templates) are loaded on-demand, not upfront
- This is fundamentally different from custom instructions, which are always loaded

### 4. Skills vs Custom Instructions

Understanding when to use skills versus custom instructions is critical for effective Copilot configuration:

| Aspect | Agent Skills (SKILL.md) | Custom Instructions (.github/copilot-instructions.md) |
|--------|------------------------|------------------------------------------------------|
| **Purpose** | Task-specific expertise and tools | Global project-wide guidelines |
| **Activation** | Automatic, based on semantic relevance | Always active for every request |
| **Portability** | Open standard; works across VS Code, CLI, Coding Agent | VS Code specific |
| **Content types** | Instructions + scripts + resource files | Instructions only (single file) |
| **Context cost** | Progressive disclosure (loaded only when relevant) | Always in context |
| **Standard** | Open standard at agentskills.io | GitHub/VS Code convention |
| **Sharing** | Shareable as standalone directories | Part of repo configuration |
| **Granularity** | One skill per concern (testing, linting, deployment, etc.) | One file covers everything |

**Rule of thumb:** Use custom instructions for things that should _always_ apply (coding style, language preferences). Use skills for specialized capabilities that are only needed for certain tasks (code quality checks, deployment procedures, API design patterns).

### 5. Community Skills

The open standard has enabled a growing ecosystem of community-contributed skills:

- **[github/awesome-copilot](https://github.com/github/awesome-copilot)**: Curated list of skills, extensions, and resources for GitHub Copilot
- **[anthropics/skills](https://github.com/anthropics/skills)**: Collection of agent skills compatible with the SKILL.md standard

Community skills cover common use cases such as:

- Language-specific linting and code quality
- Framework-specific patterns (React, Django, Rails, etc.)
- DevOps and CI/CD workflows
- Security review checklists
- Documentation generation
- Database design and migration patterns

### 6. Security Considerations

Because skills can contain scripts and instructions that Copilot will follow, security review is essential:

- **Review all shared skills** before adding them to your project: read the SKILL.md body and inspect any scripts
- **Terminal tool controls**: Scripts referenced by skills that require terminal execution are subject to VS Code's terminal tool approval. Copilot will ask for confirmation before running commands
- **Limit skill locations**: Only add trusted directories to `chat.agentSkillsLocations`
- **Git review**: When skills are committed to `.github/skills/`, they go through your normal PR review process
- **No network access**: Skills themselves do not have network access; they are local files and instructions
- **Least privilege**: Write skill instructions that request only the minimum tools and access needed

---

## Exercises

### Exercise 1: Create Your First Agent Skill

Build a Python code quality skill from scratch and test it with Copilot.

**Steps:**
1. Study the sample SKILL.md in `exercises/create_skill/SKILL.md`
2. Copy the entire `exercises/create_skill/` directory to `.github/skills/python-code-quality/` in your workspace
3. Open VS Code Chat in Agent mode
4. Ask: "Review this Python file for code quality issues"
5. Observe that Copilot discovers and loads the skill automatically
6. Ask: "Run the quality check script on my project" to test script referencing

**Reference**: See `exercises/create_skill/SKILL.md`

### Exercise 2: Install a Community Skill

Find, evaluate, and install a community skill from public repositories.

**Steps:**
1. Follow the walkthrough in `exercises/install_community_skill.md`
2. Browse available skills at the community repositories
3. Install a skill to your workspace
4. Test it with relevant Copilot queries

**Reference**: See `exercises/install_community_skill.md`

### Exercise 3: Skills vs Extensions Decision Making

Understand when to use Agent Skills versus Copilot Extensions.

**Steps:**
1. Read the comparison guide in `exercises/skills_vs_extensions.md`
2. Complete the migration exercise: convert a skillset definition to SKILL.md
3. Evaluate your existing Copilot configuration for skill opportunities

**Reference**: See `exercises/skills_vs_extensions.md`

### Exercise 4: Build a Multi-File Skill with Resources

Create a more complex skill that leverages scripts and resource files.

**Steps:**
1. Create a new directory: `.github/skills/api-design/`
2. Write a `SKILL.md` with frontmatter:
   ```yaml
   ---
   name: api-design
   description: Guides RESTful API design following company conventions. Use when designing, reviewing, or implementing API endpoints.
   ---
   ```
3. Create `resources/rest_conventions.md` with your API naming and versioning rules
4. Create `resources/openapi_template.yaml` with a starter OpenAPI spec
5. Reference both files in the SKILL.md body
6. Test by asking Copilot: "Design a REST API for user management"
7. Verify that Copilot follows your conventions and references your template

### Exercise 5: Organize a Skill Library

Set up a shared skill library for a team using custom skill locations.

**Steps:**
1. Create a directory outside your workspace (e.g., `~/copilot-team-skills/`)
2. Add at least two skills to it (e.g., `security-review/` and `testing-standards/`)
3. Configure VS Code to include this path:
   ```json
   {
     "chat.agentSkillsLocations": [
       "~/copilot-team-skills"
     ]
   }
   ```
4. Open a project and verify that both skills are discoverable
5. Ask Copilot questions that should trigger each skill
6. Discuss with your team: which skills should be project-level (`.github/skills/`) vs shared library?

---

## Key Takeaways

- Agent Skills are portable, self-contained packages of instructions, scripts, and resources
- The SKILL.md format uses YAML frontmatter (`name` + `description`) for discovery and a Markdown body for instructions
- Skills follow an open standard at [agentskills.io](https://agentskills.io), making them portable across VS Code, Copilot CLI, and Copilot Coding Agent
- Three-level progressive disclosure (discovery, instructions, resources) keeps context usage efficient
- Store project skills in `.github/skills/`, personal skills in `~/.copilot/skills/`
- Community skills are available from repositories like `github/awesome-copilot`
- Always review shared skills for security before adding them to your project
- Use skills for task-specific expertise; use custom instructions for global project guidelines

---

## Next Steps

- **Module 12**: Create custom agents with `.agent.md` that leverage your skills
- **Module 14**: Use skills with cloud and background agent sessions for autonomous workflows
