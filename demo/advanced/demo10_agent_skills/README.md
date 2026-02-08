# Demo 10: Agent Skills

## What This Demo Shows

- **Agent Skills overview**: The next evolution beyond Copilot Extensions -- file-based, portable skills
- **SKILL.md authoring**: How to define a skill with YAML frontmatter and markdown instructions
- **Progressive disclosure**: How Copilot loads skill content in stages for efficiency
- **Portable skills**: Skills that work across VS Code, GitHub CLI, and coding agents

**Duration**: 15-20 minutes
**Complexity**: Intermediate
**Best For**: Teams building reusable AI-powered workflows

---

## Prerequisites

1. **GitHub Copilot** subscription with Agent Mode access
2. **VS Code** with GitHub Copilot extensions (v1.96+)
3. **Python 3.8+** installed (for the example skill script)
4. **Familiarity** with `.github/` repository conventions

---

## Quick Setup (2 minutes)

### 1. Navigate to Demo Folder

```bash
cd demo/advanced/demo10_agent_skills
```

### 2. Review the Example Skill

Browse `setup/example_skill/` to see the complete skill structure before the demo.

### 3. Open Copilot Chat

- Press `Ctrl/Cmd + Shift + I` to open Copilot Chat
- Ensure you are in Agent Mode (look for the agent icon)

---

## Demo Steps

### Step 1: Agent Skills vs Old Extensions (3 minutes)

**Explain the evolution to your audience:**

1. **Copilot Extensions (old approach)**:
   - Required an HTTP server to handle requests
   - Infrastructure overhead: hosting, monitoring, authentication
   - Tight coupling to GitHub's extension API surface

2. **Agent Skills (new approach)**:
   - Defined entirely as files in your repository (no server needed)
   - A `SKILL.md` file with YAML frontmatter and markdown instructions
   - Portable across VS Code, GitHub CLI, and any coding agent
   - Open standard defined at [agentskills.io](https://agentskills.io)

3. **Key advantages**:
   - Zero infrastructure -- just commit files to your repo
   - Version-controlled alongside your code
   - Shareable via `.github/skills/` directory convention
   - Works wherever Copilot runs

### Step 2: Create SKILL.md Live (5 minutes)

1. Open the example skill at `setup/example_skill/SKILL.md`
2. Walk through the **YAML frontmatter**:
   - `name`: a short, kebab-case identifier
   - `description`: one or two sentences explaining when to use the skill
3. Walk through the **body** (markdown below the frontmatter):
   - Step-by-step instructions Copilot should follow
   - References to scripts and resources via relative paths
4. Show where it lives in a real repository:

```
your-repo/
  .github/
    skills/
      python-lint-style/
        SKILL.md
        scripts/
          lint_check.py
        resources/
          style_guide.md
```

5. Emphasize: the description is the most important part -- it determines when Copilot selects this skill

### Step 3: Build Complete Skill Folder (5 minutes)

1. Show the full folder structure of `setup/example_skill/`:

```
example_skill/
  SKILL.md              # Skill definition and instructions
  scripts/
    lint_check.py       # Executable script for linting checks
  resources/
    style_guide.md      # Reference material for style decisions
```

2. Open `scripts/lint_check.py` and explain:
   - The script performs basic linting checks (docstrings, naming, imports)
   - SKILL.md references this script so Copilot can run it when needed
   - The script is self-contained and can also be used independently

3. Open `resources/style_guide.md` and explain:
   - This is reference material Copilot reads for context
   - It provides team-specific conventions beyond PEP 8
   - Copilot only loads this file when it needs style guidance

### Step 4: Test Progressive Disclosure (5 minutes)

Demonstrate the three levels of skill loading:

1. **Level 1 -- Metadata only**:
   - Copilot reads only the `name` and `description` from frontmatter
   - This happens for all skills in the repository to build a skill index
   - Ask a question unrelated to linting -- the skill is indexed but not loaded

2. **Level 2 -- Full SKILL.md body**:
   - When a request matches the description, Copilot reads the full SKILL.md
   - Ask: *"Check this Python file for style issues"*
   - Copilot now has the full set of instructions

3. **Level 3 -- Referenced files**:
   - When the instructions reference scripts or resources, Copilot accesses them
   - Copilot runs `lint_check.py` or reads `style_guide.md` only when needed
   - This keeps the context window lean and efficient

**Live test**: Use the prompts from `prompts.md` to trigger each level.

---

## Expected Results

After triggering the skill, Copilot should:

- Identify the `python-lint-style` skill as relevant
- Follow the instructions in SKILL.md to check Python code
- Reference the style guide for team-specific conventions
- Optionally run the lint_check.py script for automated checks
- Provide actionable feedback on docstrings, naming, imports, and complexity

---

## Key Messages for Your Audience

1. **"No servers, no infrastructure"** -- Skills are just files in your repo
2. **"Write once, run everywhere"** -- Same skill works in VS Code, CLI, and agents
3. **"Progressive disclosure is efficient"** -- Copilot only loads what it needs
4. **"Version control your AI workflows"** -- Skills evolve with your codebase
5. **"The description is everything"** -- A good description ensures proper skill matching

---

## Troubleshooting

### If the skill is not recognized

- Ensure the SKILL.md file is in `.github/skills/<skill-name>/SKILL.md`
- Verify the YAML frontmatter has valid `name` and `description` fields
- Check that the frontmatter delimiters (`---`) are on their own lines
- Reload VS Code to re-index skills

### If referenced files are not found

- Use relative paths from the SKILL.md location (e.g., `scripts/lint_check.py`)
- Ensure the files exist and are committed to the repository
- Check file permissions are readable

### If progressive disclosure seems off

- The skill description must clearly match the type of request
- Try rephrasing your question to include keywords from the description
- Check the Copilot output panel for skill matching logs

---

## Success Metrics

After this demo, your audience should understand:

- Agent Skills replace the need for hosted Copilot Extensions
- A SKILL.md file is all you need to teach Copilot a new capability
- Progressive disclosure keeps interactions fast and context-efficient
- Skills are portable, version-controlled, and team-shareable
- The description field is the primary mechanism for skill discovery

---

## Next Steps

- Create a skill for your team's most common workflow
- Add skills for code review checklists, deployment procedures, or onboarding
- Explore the open standard at [agentskills.io](https://agentskills.io)
- Combine multiple skills for complex, multi-step workflows
