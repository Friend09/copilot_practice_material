# Exercise: Install a Community Agent Skill

This walkthrough guides you through finding, evaluating, installing, and testing a community-contributed Agent Skill.

---

## Step 1: Browse Available Skills

Community skills are published in open repositories. Start by exploring these sources:

1. **GitHub Awesome Copilot**: [github.com/github/awesome-copilot](https://github.com/github/awesome-copilot)
   - Curated list of skills, extensions, and resources
   - Look for the "Agent Skills" section

2. **Anthropics Skills Repository**: [github.com/anthropics/skills](https://github.com/anthropics/skills)
   - Collection of skills compatible with the SKILL.md open standard

3. **GitHub Search**: Search for repositories containing `SKILL.md` files:
   ```
   filename:SKILL.md path:.github/skills
   ```

**Task:** Browse at least one of the repositories above and identify a skill that is relevant to your current project or interests.

---

## Step 2: Choose a Skill to Install

When evaluating a skill, check the following before installing:

| Criteria | What to Look For |
|----------|-----------------|
| **Relevance** | Does the `description` in the YAML frontmatter match tasks you perform regularly? |
| **Quality** | Are the instructions clear, specific, and well-structured? |
| **Scope** | Is the skill focused on a single concern, or does it try to do too much? |
| **Resources** | Does it include useful scripts or reference files? Are they well-documented? |
| **Maintenance** | When was the skill last updated? Does it have open issues? |
| **Security** | Do any scripts perform file modifications, network requests, or shell commands? |

**Task:** Select one skill to install. Note the repository URL and skill directory name.

---

## Step 3: Copy the Skill to Your Workspace

Install the skill by copying its directory into your project's `.github/skills/` folder.

### Option A: Clone and Copy

```bash
# Clone the repository containing the skill
git clone https://github.com/<owner>/<repo>.git /tmp/skill-repo

# Copy the skill directory to your project
cp -r /tmp/skill-repo/.github/skills/<skill-name> \
      .github/skills/<skill-name>

# Clean up
rm -rf /tmp/skill-repo
```

### Option B: Download Directly

If the skill is a standalone directory in a repository:

```bash
# Create the target directory
mkdir -p .github/skills/<skill-name>

# Download the SKILL.md file
curl -o .github/skills/<skill-name>/SKILL.md \
  https://raw.githubusercontent.com/<owner>/<repo>/main/.github/skills/<skill-name>/SKILL.md
```

Download any additional resource files referenced in the SKILL.md.

### Option C: Git Submodule (for frequently updated skills)

```bash
# Add as a submodule for automatic updates
git submodule add \
  https://github.com/<owner>/<repo>.git \
  .github/skills/<skill-name>
```

**Task:** Copy your chosen skill into `.github/skills/` in your workspace.

---

## Step 4: Review and Customize the SKILL.md

Before using the skill, review its contents thoroughly:

1. **Open the SKILL.md** file and read the full body
2. **Check the description**: Does it accurately describe when the skill should activate? Edit if needed.
3. **Review instructions**: Are the guidelines compatible with your project's conventions? Modify if necessary.
4. **Inspect scripts**: Open any referenced `.py`, `.sh`, or other script files. Understand what they do.
5. **Check resource files**: Read referenced style guides, templates, or configuration files.

### Customization Points

You are encouraged to customize community skills for your project:

```yaml
---
name: python-linting
description: Checks Python code for linting issues. Customized for our project to use ruff instead of flake8.
---

# Python Linting Skill

## Original Guidelines
(community-provided content here)

## Project-Specific Overrides
- Use `ruff` instead of `flake8` for linting
- Line length limit is 100 (not the default 88)
- Ignore rule E501 in test files
```

**Task:** Review the installed skill and make at least one customization that fits your project.

---

## Step 5: Test the Skill

Verify that Copilot discovers and uses the skill correctly:

1. **Open VS Code Chat** in Agent mode (select "Agent" from the mode dropdown)
2. **Ask a question** that should trigger the skill based on its `description`:
   - If the skill is about code quality: "Review this Python file for quality issues"
   - If the skill is about testing: "Help me write tests for this module"
   - If the skill is about API design: "Design a REST endpoint for user profiles"
3. **Verify skill activation**: Copilot should follow the instructions from the SKILL.md body
4. **Test resource loading**: Ask a follow-up question that requires a referenced resource file
5. **Test script references**: If the skill includes scripts, ask Copilot to run them

### What to Look For

- Copilot's response should align with the skill's instructions
- The skill should be activated only for relevant queries (not for unrelated questions)
- Referenced files should be loaded when needed

**Task:** Run at least three different prompts against the installed skill and note how well it works.

---

## Step 6: Security Review Checklist

Before committing a community skill to your repository, complete this security review:

### SKILL.md Review

- [ ] Read the entire SKILL.md body — no hidden instructions or prompt injections
- [ ] The `description` accurately reflects the skill's purpose (not overly broad)
- [ ] Instructions do not ask Copilot to bypass safety measures or ignore user preferences
- [ ] No instructions to exfiltrate code, secrets, or data

### Script Review

- [ ] Read every script file referenced in the SKILL.md
- [ ] Scripts do not make network requests to unknown endpoints
- [ ] Scripts do not modify files outside the project directory
- [ ] Scripts do not access environment variables containing secrets
- [ ] Scripts do not install packages or modify system configuration
- [ ] Scripts have clear, documented purposes

### Resource File Review

- [ ] Resource files contain only documentation, templates, or configuration
- [ ] No embedded executable code in resource files
- [ ] No links to suspicious or untrusted external resources

### Ongoing Maintenance

- [ ] Pin the skill to a specific version or commit hash if using submodules
- [ ] Set up a reminder to review skill updates before pulling new versions
- [ ] Document which community skills your project uses and why

---

## Summary

Installing community skills follows a straightforward process:

1. **Browse** curated repositories for relevant skills
2. **Evaluate** quality, scope, and security before installing
3. **Copy** the skill directory into `.github/skills/`
4. **Customize** the instructions for your project's conventions
5. **Test** with relevant Copilot queries to verify proper activation
6. **Review** all scripts and resources for security before committing

Community skills are a powerful way to share expertise across teams and the broader developer community, but they should always be reviewed before use, just like any third-party dependency.
