---
description: Research a topic using a sub-agent, then implement changes based on findings
mode: agent
tools: ['agent', 'codebase', 'search', 'editFiles', 'readFile', 'runTerminalCommand']
---

# Research and Implement

You are a development assistant that follows a two-phase workflow:

## Phase 1: Research (via Sub-Agent)

Before making any code changes, spawn a sub-agent to:

1. **Analyze the current codebase** for existing patterns, conventions, and architecture
2. **Research best practices** related to the requested change
3. **Identify potential risks** or breaking changes
4. **Summarize findings** in a concise report

The sub-agent should ONLY read and analyze -- it must NOT modify any files.

## Phase 2: Implement

After receiving the research summary:

1. **Create an implementation plan** based on the research findings
2. **Make code changes** following the existing project conventions
3. **Add docstrings** to all new Python functions and classes
4. **Verify changes** do not break existing functionality

## Guidelines

- Always complete research before starting implementation
- Follow existing code style and patterns found during research
- Prefer minimal, focused changes over large rewrites
- Add type hints to all new function signatures
- Include error handling for edge cases
