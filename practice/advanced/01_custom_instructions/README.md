# Exercise 1 – Repository Custom Instructions

1. Open `.github/copilot-instructions.md`.
2. Add at least **one project overview sentence** and **three coding standards** specific to this repository.
3. Save the file and start typing code in `style_demo.py` to see if Copilot follows your conventions.

> Tip: Keep instructions short, broadly applicable, and not overly specific.
> See GitHub Docs for best practices.

---

## 2025 Updates

### File-Specific Instructions with `.instructions.md`

You can now create `.instructions.md` files with `applyTo` glob patterns to target instructions to specific file types:

```markdown
---
applyTo: "**/*.py"
---
Always use Google-style docstrings. Type-hint all function parameters and return values.
Use dataclasses instead of plain dicts for structured data.
```

```markdown
---
applyTo: "**/tests/**"
---
Use pytest with fixtures. Name tests as test_<function>_<scenario>_<expected>.
Mock external dependencies. Target 80% coverage minimum.
```

Place these files in `.github/instructions/` and they will automatically apply to matching files.

### Organization-Level Instructions

Enterprise and Business subscribers can set instructions at the **organization level** that apply to all repositories. These are configured by org admins and cannot be overridden by individual repos.

### Instruction Priority

When multiple instruction sources exist, they combine in this order:
1. Organization-level instructions (highest priority)
2. Repository-level `.github/copilot-instructions.md`
3. File-specific `.instructions.md` files matching the current file
4. Personal instructions in VS Code settings

> **See also**: Module 12 (Custom Agents) for agent-specific instructions via `.agent.md` files
