---
description: Comprehensive code review with security and performance focus
mode: ask
tools: ['codebase', 'editFiles']
---

# Code Review Prompt

Please review the following code for:

- Security vulnerabilities
- Performance issues
- Code quality and best practices
- Documentation completeness

Focus on: ${input:language:programming language} specific patterns
Severity level: ${input:severity:high/medium/low}

Code to review:
${selection}
