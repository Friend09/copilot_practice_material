# Demo 5: AI-Powered Code Review

## What This Demo Shows

- **Comprehensive code analysis**: Security, performance, and quality issues
- **Automated PR summaries**: Professional documentation generation
- **Best practices enforcement**: Consistent quality standards
- **Educational code review**: Learning while reviewing

**Duration**: 10-12 minutes
**Complexity**: Intermediate
**Best For**: Development teams, QA engineers, tech leads

---

## Quick Setup (30 seconds)

### 1. Navigate to Demo Folder

```bash
cd demo/advanced/demo5_code_review
```

### 2. Review Problematic Code

Open `setup/problematic_code.py` - intentionally flawed code for review!

---

## Demo Steps

### Step 1: Show Problematic Code (2 minutes)

1. Open the problematic code file
2. Point out visible issues while scrolling:
   - Security vulnerabilities (hardcoded secrets, SQL injection)
   - Performance problems (O(n²) algorithms)
   - Code quality issues (naming, error handling)

### Step 2: Comprehensive Review (6 minutes)

1. Open Copilot Chat
2. Copy primary prompt from `prompts.md`:
   ```text
   Please review this code for quality issues, security problems,
   and best practices violations. Provide specific suggestions
   for improvement.
   ```
3. Watch Copilot identify and categorize issues

### Step 3: Get Improved Code (4 minutes)

Use follow-up prompts to get:

- Secure implementations
- Performance optimizations
- Quality improvements
- PR summary generation

---

## Expected Results

Copilot should identify:

- ✅ **Security Issues**: SQL injection, hardcoded secrets, weak auth
- ✅ **Performance Problems**: Inefficient algorithms, missing indexes
- ✅ **Quality Issues**: Missing type hints, poor error handling
- ✅ **Architecture Problems**: Tight coupling, SRP violations

---

## Success Metrics

After this demo, your audience should understand:

- ✅ **AI review is comprehensive** - Catches multiple issue types
- ✅ **Quality is enterprise-grade** - Professional analysis level
- ✅ **Speed improves dramatically** - Faster, more thorough reviews
- ✅ **Learning happens automatically** - Educational for developers
