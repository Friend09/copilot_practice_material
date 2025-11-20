---
title: Comprehensive Code Review
description: Thorough code review focusing on security, performance, and best practices
tags: [code-review, security, performance, quality]
---

# Code Review Prompt

Review the selected code thoroughly and provide detailed feedback.

## Review Areas

### 1. Security
- Input validation and sanitization
- SQL injection vulnerabilities
- XSS and CSRF protection
- Authentication and authorization
- Sensitive data handling
- Dependency vulnerabilities

### 2. Performance
- Algorithm efficiency (Big O analysis)
- Database query optimization
- Caching opportunities
- Memory usage
- Network request optimization
- Lazy loading possibilities

### 3. Code Quality
- Readability and maintainability
- DRY principle (Don't Repeat Yourself)
- SOLID principles adherence
- Proper naming conventions
- Code organization
- Comment quality

### 4. Error Handling
- Appropriate exception handling
- Meaningful error messages
- Logging completeness
- Graceful degradation
- Recovery mechanisms

### 5. Testing
- Test coverage gaps
- Edge cases handling
- Integration test needs
- Mock usage appropriateness

### 6. Best Practices
- Language-specific idioms
- Framework conventions
- Design patterns usage
- Code smells

## Output Format

Provide structured feedback:

**🔴 Critical Issues** (must fix before merge)
- List critical problems with line numbers

**🟡 Important Issues** (should fix soon)
- List important improvements needed

**🟢 Suggestions** (nice to have)
- List optional enhancements

**✅ Positive Observations**
- Highlight what was done well

**📊 Overall Assessment**
- Summary recommendation (Approve/Request Changes/Comment)

## Example Usage

Select code and run:
```
@workspace Use code-review prompt to review this function
```
