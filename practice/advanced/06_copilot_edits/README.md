# Module 06 – Copilot Edits: Multi-File Editing with Natural Language

## 🎯 Overview

**Copilot Edits** is a revolutionary feature introduced in 2024 that allows you to edit multiple files simultaneously using natural language instructions. Unlike traditional inline suggestions or chat-based coding, Copilot Edits provides a dedicated interface for making coordinated changes across your entire codebase.

## What is Copilot Edits?

Copilot Edits transforms how you perform large-scale code changes:

- **Multi-File Editing**: Make changes across multiple files in one go
- **Natural Language Instructions**: Describe what you want in plain English
- **Inline Changes**: Edits appear directly in your workspace
- **Fast Iteration**: Optimized UI for rapid development cycles
- **Context-Aware**: Understands relationships between files

### When to Use Copilot Edits

✅ **Perfect for:**
- Refactoring across multiple files
- Implementing features that span components
- Renaming functions/classes with all references
- Adding consistent patterns (logging, error handling)
- Migration tasks (API updates, library upgrades)
- Architectural changes

❌ **Not ideal for:**
- Single-line quick fixes (use inline suggestions)
- Exploratory questions (use Copilot Chat)
- Learning how something works (use Chat)
- Tasks requiring external knowledge only

## Setup

1. **Prerequisites**:
   - VS Code or VS Code Insiders
   - GitHub Copilot Chat extension (latest version)
   - Active GitHub Copilot subscription

2. **Accessing Copilot Edits**:
   - Open Copilot Chat panel (`Ctrl+Shift+I` / `Cmd+Shift+I`)
   - Look for "Edits" tab or "Start Editing Session"
   - Alternative: Use command palette (`Ctrl+Shift+P`) → "GitHub Copilot: Open Edits"

3. **Selecting Files**:
   - Click "Add Files" in the Edits interface
   - Select files you want Copilot to modify
   - Or use `@workspace` to give broader context

## Exercise 1: Basic Multi-File Refactoring

### Scenario
You have a simple e-commerce application with separate files for models, views, and utilities. You need to add logging throughout the application.

### Files to Work With
- `models.py` - Product and Order models
- `views.py` - API endpoint handlers
- `utils.py` - Utility functions

### Task
Use Copilot Edits to add logging to all three files:

```
Add Python logging to all functions in models.py, views.py, and utils.py.
- Import logging at the top of each file
- Add a logger instance using __name__
- Log entry and exit of each function at DEBUG level
- Log any exceptions at ERROR level
```

### Expected Result
- All three files will have logging imports
- Each function will log its execution
- Consistent logging pattern across all files

## Exercise 2: Feature Implementation Across Components

### Scenario
Add pagination support to your API, which requires changes to models, views, and a new utility module.

### Task
```
Implement pagination for the product listing API:
1. Add pagination parameters (page, page_size) to the get_products view
2. Create pagination utility functions in utils.py
3. Update the Product model to support pagination queries
4. Add pagination metadata to API responses (total, page, pages)
```

### Advanced Version
```
Implement pagination with these requirements:
- Default page size: 20 items
- Maximum page size: 100 items
- Return pagination metadata in response headers
- Add input validation for page parameters
- Handle edge cases (empty results, invalid page numbers)
```

## Exercise 3: API Migration

### Scenario
Your API is moving from v1 to v2 with breaking changes. Update all endpoints and their references.

### Task
```
Migrate API from v1 to v2:
- Change all endpoint routes from /api/v1/* to /api/v2/*
- Update function names to include v2 prefix
- Add deprecation warnings to old v1 endpoints
- Update import statements in all files
- Add API version to response headers
```

## Exercise 4: Error Handling Standardization

### Scenario
Implement consistent error handling across your application.

### Task
```
Standardize error handling across all files:
1. Create a custom exception hierarchy in utils.py
2. Wrap all database operations in try-except blocks
3. Convert generic exceptions to custom exceptions
4. Add appropriate HTTP status codes to API errors
5. Log all exceptions with stack traces
```

## Exercise 5: Adding TypeScript Types

### Scenario
Convert Python code to TypeScript (or add type hints to Python).

### Files
- `models.ts` / `models.py`
- `views.ts` / `views.py`
- `utils.ts` / `utils.py`

### Task (Python)
```
Add comprehensive type hints to all Python files:
- Import typing module types
- Add type hints to function parameters
- Add return type annotations
- Add type hints for class attributes
- Use Optional, List, Dict where appropriate
```

### Task (TypeScript Alternative)
```
Create TypeScript interfaces and types:
- Define interfaces for all data models
- Add type annotations to all functions
- Create union types for status codes
- Use generics for utility functions
```

## Best Practices for Copilot Edits

### 1. Be Explicit About Files
```
✅ Good: "Update models.py and views.py to use async/await"
❌ Vague: "Make things async"
```

### 2. Break Down Large Tasks
```
✅ Good:
"Step 1: Add async imports to all files
 Step 2: Convert database calls to async
 Step 3: Update view functions to async handlers"

❌ Too broad: "Make entire application asynchronous"
```

### 3. Specify Patterns and Constraints
```
✅ Good: "Add error handling using try-except blocks,
         log errors with logger.error(),
         return appropriate HTTP status codes"

❌ Vague: "Add error handling"
```

### 4. Review Changes Before Accepting
- Copilot Edits shows diffs for all files
- Review each change carefully
- Accept/reject changes per file or in bulk
- You can request modifications if something isn't right

### 5. Use Context Effectively
```
✅ Include context: "Following the pattern in auth.py,
                      add token validation to all API endpoints"
❌ No context: "Add token validation everywhere"
```

## Advanced Techniques

### 1. Conditional Changes
```
Only add logging to functions that make database calls.
Skip getter/setter methods.
```

### 2. Pattern Matching
```
Find all functions that return None and update them to return
Result[T, Error] types instead, handling errors appropriately.
```

### 3. Architectural Changes
```
Refactor the application to use dependency injection:
- Create container.py with dependency registrations
- Update all classes to accept dependencies via __init__
- Modify views.py to inject dependencies
- Add type hints for injected dependencies
```

### 4. Code Style Consistency
```
Ensure all files follow these conventions:
- PEP 8 style guide
- Docstrings in Google format
- Maximum line length: 100 characters
- Imports organized: stdlib, third-party, local
```

## Troubleshooting

### Issue: Copilot makes unexpected changes
**Solution**: Be more specific in your instructions, specify exact files, or break down the task into smaller steps.

### Issue: Edits don't appear in some files
**Solution**: Ensure files are added to the editing session. Check if files are ignored in `.copilotignore`.

### Issue: Changes conflict with each other
**Solution**: Review the diff carefully. You can partially accept changes and manually resolve conflicts.

### Issue: Copilot Edits not available
**Solution**: Update GitHub Copilot Chat extension. Feature may be in gradual rollout.

## Comparison: Edits vs Chat vs Inline

| Feature | Inline Suggestions | Copilot Chat | Copilot Edits |
|---------|-------------------|--------------|---------------|
| Single-line completion | ✅ Best | ❌ | ❌ |
| Multi-line function | ✅ Good | ✅ Good | ✅ Good |
| Multi-file changes | ❌ | ⚠️ Manual | ✅ Best |
| Learning/Questions | ❌ | ✅ Best | ❌ |
| Refactoring | ⚠️ Limited | ⚠️ Manual | ✅ Best |
| Speed | ⚡ Instant | 🚀 Fast | 🚀 Fast |

## Practice Project: Complete Application Enhancement

Use Copilot Edits to enhance the provided e-commerce application:

### Phase 1: Foundation
```
Add comprehensive error handling and logging to all files.
```

### Phase 2: Features
```
Implement user authentication:
- Add User model
- Create authentication utilities
- Protect API endpoints
- Add authorization checks
```

### Phase 3: Optimization
```
Add caching layer:
- Create cache utility wrapper
- Add caching to expensive queries
- Implement cache invalidation
- Add cache statistics endpoint
```

### Phase 4: Testing
```
Generate comprehensive tests:
- Unit tests for all models
- Integration tests for API endpoints
- Mock external dependencies
- Achieve >80% code coverage
```

## Key Takeaways

1. **Copilot Edits excels at coordinated multi-file changes**
2. **Clear, specific instructions yield better results**
3. **Always review changes before accepting**
4. **Break complex tasks into manageable steps**
5. **Use it for refactoring, migrations, and feature implementation**

## Next Steps

- Try **Multi-Model Support** (Module 07) to optimize your editing sessions
- Explore **Prompt Files** (Module 09) to save complex editing instructions
- Learn **Vision for Copilot** (Module 10) to generate code from designs

## Resources

- [GitHub Copilot Edits Documentation](https://docs.github.com/en/copilot)
- [Multi-File Editing Best Practices](https://github.blog)
- [Copilot Edits Video Tutorial](https://youtube.com)
