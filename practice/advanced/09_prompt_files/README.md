# Module 09 – Prompt Files: Reusable Prompt Templates and Blueprints

## 🎯 Overview

**Prompt Files** are a powerful 2024 feature that allows you to save, organize, and share reusable prompt instructions within your VS Code workspace. Think of them as "blueprints" for common development tasks that you and your team can use repeatedly.

## What are Prompt Files?

Prompt Files are self-contained markdown files that combine:
- Natural language instructions
- File references
- Code snippets
- Context and examples
- Step-by-step procedures

They transform complex, multi-step prompts into shareable, version-controlled templates.

## Why Use Prompt Files?

### Benefits

✅ **Consistency**: Standardize how tasks are performed across your team
✅ **Efficiency**: Reuse complex prompts without rewriting
✅ **Knowledge Sharing**: Share expertise through well-crafted prompts
✅ **Onboarding**: Help new team members learn best practices
✅ **Version Control**: Track prompt evolution in Git
✅ **Documentation**: Self-documenting development processes

## Structure of a Prompt File

```markdown
---
title: Prompt Title
description: Brief description of what this prompt does
tags: [tag1, tag2, tag3]
---

# Main Instructions

Clear, detailed instructions for Copilot.

## Context

Background information and requirements.

## Steps

1. First step
2. Second step
3. Third step

## Examples

Show examples of expected inputs/outputs.

## References

Link to related files or documentation.
```

## Exercise 1: Basic Prompt File

### Task: Create a Code Review Prompt

Create `.github/copilot/prompts/code-review.md`:

```markdown
---
title: Comprehensive Code Review
description: Perform a thorough code review with focus on security, performance, and maintainability
tags: [code-review, quality, security]
---

# Code Review Instructions

Review the selected code for:

## Security
- SQL injection vulnerabilities
- XSS vulnerabilities
- Authentication/authorization issues
- Sensitive data exposure
- Input validation

## Performance
- Inefficient algorithms (time complexity)
- Memory leaks
- Database query optimization
- Unnecessary computations
- Caching opportunities

## Maintainability
- Code clarity and readability
- DRY principle violations
- Proper error handling
- Comprehensive logging
- Documentation quality

## Testing
- Test coverage gaps
- Edge cases not handled
- Integration test needs

## Output Format

Provide:
1. Overall assessment (Green/Yellow/Red)
2. Critical issues (must fix)
3. Important issues (should fix)
4. Suggestions (nice to have)
5. Positive observations

## Example Response

**Overall**: 🟡 Yellow - Some issues need attention

**Critical Issues:**
- SQL injection risk in line 45

**Important Issues:**
- Missing error handling in API calls
- No input validation for user data

**Suggestions:**
- Consider adding caching for frequently accessed data
- Extract magic numbers into constants

**Positive:**
- Well-structured code
- Good use of type hints
```

### Usage

1. Save the file in your workspace
2. In Copilot Chat, type: `@workspace /code-review`
3. Or reference it: `Use the code-review prompt to review this function`

## Exercise 2: Feature Implementation Template

### Task: Create a Full-Stack Feature Prompt

Create `.github/copilot/prompts/fullstack-feature.md`:

```markdown
---
title: Full-Stack Feature Implementation
description: Complete workflow for implementing a full-stack feature
tags: [fullstack, api, database, frontend]
---

# Full-Stack Feature Implementation

Implement a complete feature following these steps:

## Phase 1: Backend - Database

1. **Design the schema**
   - Create migration file
   - Define tables, columns, constraints
   - Add indexes for performance
   - Include foreign keys

2. **Create models**
   - Define ORM models
   - Add validation rules
   - Include relationships
   - Add class methods for business logic

## Phase 2: Backend - API

3. **Create API endpoints**
   - POST /api/resource (create)
   - GET /api/resource (list)
   - GET /api/resource/:id (retrieve)
   - PUT /api/resource/:id (update)
   - DELETE /api/resource/:id (delete)

4. **Add validation**
   - Input validation
   - Business rule validation
   - Authorization checks

5. **Error handling**
   - Proper HTTP status codes
   - Meaningful error messages
   - Logging

## Phase 3: Frontend

6. **Create components**
   - List view component
   - Detail view component
   - Create/Edit form component
   - Delete confirmation modal

7. **State management**
   - API integration
   - Loading states
   - Error handling
   - Optimistic updates

8. **Styling**
   - Responsive design
   - Accessibility (ARIA labels)
   - Loading indicators
   - Error messages

## Phase 4: Testing

9. **Backend tests**
   - Unit tests for models
   - Integration tests for API
   - Test error conditions

10. **Frontend tests**
    - Component rendering tests
    - User interaction tests
    - API integration tests

## Phase 5: Documentation

11. **API documentation**
    - Endpoint descriptions
    - Request/response examples
    - Error codes

12. **Component documentation**
    - Props documentation
    - Usage examples
    - Storybook stories (if applicable)

## Quality Checklist

Before completing, ensure:
- [ ] All tests pass
- [ ] Code is properly formatted
- [ ] No linter errors
- [ ] Documentation is complete
- [ ] Security best practices followed
- [ ] Performance considerations addressed
- [ ] Accessibility requirements met
```

### Usage

```
@workspace Use fullstack-feature prompt to implement a user notification system
```

## Exercise 3: Bug Fix Protocol

Create `.github/copilot/prompts/bug-fix-protocol.md`:

```markdown
---
title: Systematic Bug Fix Protocol
description: Methodical approach to identifying and fixing bugs
tags: [debugging, bug-fix, troubleshooting]
---

# Bug Fix Protocol

Follow this systematic approach to fix bugs:

## Step 1: Reproduce

1. Identify the exact steps to reproduce
2. Note the expected vs actual behavior
3. Check if it's environment-specific
4. Verify it's not already fixed

## Step 2: Isolate

1. Use debugger or logging to trace execution
2. Identify the exact line/function causing the issue
3. Check recent changes (git blame)
4. Review related code paths

## Step 3: Understand

1. Understand why the code behaves this way
2. Identify root cause (not just symptoms)
3. Check for similar issues elsewhere
4. Review error logs and stack traces

## Step 4: Fix

1. Implement the minimal fix required
2. Don't introduce unnecessary changes
3. Follow existing code patterns
4. Add error handling if missing

## Step 5: Test

1. Verify the original issue is fixed
2. Test edge cases
3. Run existing test suite
4. Add regression test

## Step 6: Document

1. Update comments if behavior changed
2. Add/update documentation
3. Write clear commit message
4. Update CHANGELOG if applicable

## Template for Fix

```python
# Before (buggy code)
def problematic_function():
    # Explain what was wrong
    pass

# After (fixed code)
def fixed_function():
    # Explain what was changed and why
    # Reference issue number if applicable
    pass
```

## Commit Message Format

```
Fix: [Component] Brief description

- Detailed explanation of the bug
- Root cause identified
- How the fix addresses it
- Any side effects or considerations

Closes #[issue-number]
```
```

## Exercise 4: Code Refactoring Template

Create `.github/copilot/prompts/refactor.md`:

```markdown
---
title: Code Refactoring Guidelines
description: Safe and systematic code refactoring approach
tags: [refactoring, clean-code, optimization]
---

# Refactoring Guidelines

## Before You Start

1. Ensure tests exist and pass
2. Understand the current behavior completely
3. Have a clear goal for the refactoring
4. Make sure you have a clean git state

## Refactoring Patterns

### Extract Function
When: Function is too long or does multiple things
```python
# Before
def complex_function():
    # 50 lines of mixed logic
    pass

# After
def main_function():
    step1()
    step2()
    step3()

def step1():
    # Focused logic
    pass
```

### Extract Class
When: Related functions and data should be grouped
```python
# Before
def process_user_data(user_dict):
    # Multiple functions operating on user_dict
    pass

# After
class User:
    def __init__(self, data):
        self.data = data

    def process(self):
        pass
```

### Replace Magic Numbers
```python
# Before
if age > 18:
    pass

# After
LEGAL_ADULT_AGE = 18
if age > LEGAL_ADULT_AGE:
    pass
```

### Simplify Conditional
```python
# Before
if user.is_active and not user.is_banned and user.age >= 18:
    pass

# After
if user.can_access_content():
    pass
```

## Process

1. **Make small changes**
   - One refactoring at a time
   - Commit after each successful change

2. **Run tests frequently**
   - After every small change
   - Ensure behavior unchanged

3. **Refactor incrementally**
   - Don't try to perfect everything at once
   - Stop when good enough

4. **Keep original behavior**
   - Refactoring changes structure, not behavior
   - Add new features separately

## Checklist

- [ ] All tests still pass
- [ ] No new functionality added
- [ ] Code is more readable
- [ ] Performance not degraded
- [ ] No new bugs introduced
- [ ] Documentation updated
```

## Exercise 5: Team-Specific Prompts

### Task: Create Company Coding Standards Prompt

Create `.github/copilot/prompts/company-standards.md`:

```markdown
---
title: Acme Corp Coding Standards
description: Company-specific coding standards and conventions
tags: [standards, style-guide, conventions]
---

# Acme Corp Development Standards

When generating or reviewing code, ensure compliance with:

## Python Standards

### Naming Conventions
- Classes: `PascalCase`
- Functions/variables: `snake_case`
- Constants: `SCREAMING_SNAKE_CASE`
- Private methods: `_leading_underscore`

### Code Structure
- Maximum line length: 100 characters
- Imports: stdlib, third-party, local (separated by blank line)
- Docstrings: Google style
- Type hints: Required for all functions

### Error Handling
- Use specific exceptions, not generic `Exception`
- Always log errors with context
- Include error codes for API responses

### Testing
- Minimum 80% code coverage
- Use pytest fixtures for setup
- Mock external dependencies
- Name tests: `test_<function>_<scenario>_<expected>`

## API Standards

### Endpoints
- REST conventions: GET, POST, PUT, PATCH, DELETE
- Version in URL: `/api/v1/resource`
- Plural resource names: `/users` not `/user`
- Use hyphens: `/user-profiles` not `/user_profiles`

### Responses
```json
{
  "success": true,
  "data": {},
  "error": null,
  "timestamp": "ISO 8601 format"
}
```

### Status Codes
- 200: Success
- 201: Created
- 400: Bad Request (client error)
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 500: Internal Server Error

## Database Standards

- Use migrations for all schema changes
- Index foreign keys
- Add created_at and updated_at timestamps
- Use UUIDs for primary keys
- Soft delete with deleted_at column

## Security Requirements

- Never commit secrets
- Use environment variables for config
- Validate all user inputs
- Sanitize data before database queries
- Use prepared statements (no string concatenation)
- Hash passwords with bcrypt (cost factor 12)

## Documentation

- README for each major module
- API documentation with examples
- Inline comments for complex logic
- Update CHANGELOG for notable changes
```

## Organizing Prompt Files

### Directory Structure

```
.github/
└── copilot/
    └── prompts/
        ├── development/
        │   ├── code-review.md
        │   ├── refactor.md
        │   ├── bug-fix.md
        │   └── feature-implementation.md
        ├── testing/
        │   ├── unit-tests.md
        │   ├── integration-tests.md
        │   └── e2e-tests.md
        ├── documentation/
        │   ├── api-docs.md
        │   ├── readme.md
        │   └── inline-comments.md
        └── standards/
            ├── python-style.md
            ├── javascript-style.md
            └── api-conventions.md
```

## Best Practices

### 1. Be Specific
```markdown
✅ Good: "Review for SQL injection, XSS, and CSRF vulnerabilities"
❌ Vague: "Check security"
```

### 2. Include Examples
```markdown
✅ Good: Show example input/output
❌ Bad: Only describe abstractly
```

### 3. Use Clear Structure
```markdown
✅ Good: Numbered steps, clear sections
❌ Bad: Wall of text
```

### 4. Make Them Discoverable
```markdown
✅ Good: Use descriptive titles and tags
❌ Bad: Generic names like "prompt1.md"
```

### 5. Version Control
- Commit prompt files to Git
- Review changes in PRs
- Update as standards evolve

## Advanced: Composable Prompts

Reference one prompt from another:

```markdown
# API Endpoint Implementation

First, follow the steps in `feature-implementation.md` for the backend.

Then, specifically for the API layer:

1. Apply standards from `api-conventions.md`
2. Add tests following `integration-tests.md`
3. Document using `api-docs.md` template
```

## Integration with Workflow

### 1. Pull Request Template
```markdown
## Checklist

- [ ] Ran code-review prompt
- [ ] Applied company-standards prompt
- [ ] Generated tests with unit-tests prompt
- [ ] Updated docs using api-docs prompt
```

### 2. Pre-Commit Hook
```bash
#!/bin/bash
# Run standard prompts before commit
copilot run code-review
copilot run lint-check
```

### 3. CI/CD Integration
```yaml
# .github/workflows/copilot-checks.yml
name: Copilot Quality Checks
on: [pull_request]
jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run Copilot Review
        run: copilot-cli review --prompt .github/copilot/prompts/code-review.md
```

## Sharing Prompt Files

### 1. Within Team
- Commit to shared repository
- Create a prompts library repo
- Share via internal documentation

### 2. Publicly
- Create GitHub repository
- Add to GitHub Marketplace
- Share on community forums

### 3. Packaging
```
my-prompts/
├── README.md
├── LICENSE
├── prompts/
│   ├── backend/
│   ├── frontend/
│   └── devops/
└── examples/
    └── usage.md
```

## Key Takeaways

1. **Prompt Files capture expertise** in reusable form
2. **Standardize workflows** across your team
3. **Version control prompts** like code
4. **Organize systematically** for easy discovery
5. **Iterate and improve** based on results
6. **Share knowledge** through well-crafted prompts

## Next Steps

- Try **Vision for Copilot** (Module 10) to combine images with prompt files
- Review **Agent Mode** (Module 05) to use prompts in autonomous workflows
- Explore **Multi-Model Support** (Module 07) to optimize prompt effectiveness

## Resources

- [GitHub Copilot Prompt Files Documentation](https://docs.github.com/en/copilot)
- [Prompt Engineering Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)
- [Example Prompt Library](https://github.com/copilot-prompts)
