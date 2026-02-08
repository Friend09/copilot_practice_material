# Exercise 4: Context Comparison

## Objective

Systematically measure the impact of Copilot Space context on response quality. You will ask the same complex question with and without Space context, then document the differences in a structured comparison.

---

## Step 1: Choose a Complex Question

Select a question about your codebase that requires deep, project-specific knowledge to answer well. The question should be one where a generic answer would be noticeably inferior to a context-aware answer.

**Good example questions:**

- "How should I handle authentication for the new microservice?"
- "What is the best way to add caching to our data access layer?"
- "How should I structure the database schema for the notifications feature?"
- "What patterns should I follow when adding a new API endpoint?"
- "How do I write integration tests for our event-driven architecture?"

**Why these work:** Each question has a "generic" answer (how authentication works in general) and a "specific" answer (how authentication works in *your* system with *your* constraints).

Write down your chosen question:

```
My question: _______________________________________________
```

---

## Step 2: Ask WITHOUT Space Context

1. Open a **regular Copilot chat** (no Space selected)
2. Ask your chosen question exactly as written
3. **Copy the full response** and paste it below or into a separate document
4. Rate the response on these dimensions (1-5 scale):

| Dimension | Score (1-5) | Notes |
|---|---|---|
| **Specificity**: Does it reference your actual project? | | |
| **Accuracy**: Are the recommendations correct for your system? | | |
| **Architecture alignment**: Does it match your existing patterns? | | |
| **Actionability**: Could you implement the suggestion directly? | | |
| **Completeness**: Does it cover all relevant concerns? | | |

---

## Step 3: Create a Space with Relevant Context

Build a Space specifically designed to provide the context needed for your question.

### Context Selection Guide

For an **authentication question**, add:

- Existing auth middleware or service code
- Auth configuration files
- Security policy documents or ADRs
- Relevant issue threads about auth decisions
- API gateway configuration
- Notes about compliance requirements (SOC2, HIPAA, etc.)

For a **caching question**, add:

- Current data access layer code
- Database schema or ORM models
- Performance requirements documentation
- Existing caching patterns (if any)
- Infrastructure notes (Redis, Memcached, etc.)

For an **API endpoint question**, add:

- Existing route definitions and controllers
- API documentation or OpenAPI specs
- Middleware pipeline configuration
- Testing patterns for existing endpoints
- Naming conventions and style guides

For a **testing question**, add:

- Existing test files (unit and integration)
- Test configuration (jest.config, pytest.ini, etc.)
- CI/CD pipeline configuration
- Test coverage reports or requirements
- Notes about testing philosophy and priorities

### General Tips

- **Include 5-10 highly relevant files** rather than everything
- **Add at least one freeform note** explaining constraints or decisions
- **Include a design document or ADR** if one exists for the topic

---

## Step 4: Ask WITH Space Context

1. **Open your newly created Space** in Copilot
2. Ask the **exact same question** you asked in Step 2
3. **Copy the full response** and paste it alongside the first response
4. Rate the response on the same dimensions:

| Dimension | Score (1-5) | Notes |
|---|---|---|
| **Specificity**: Does it reference your actual project? | | |
| **Accuracy**: Are the recommendations correct for your system? | | |
| **Architecture alignment**: Does it match your existing patterns? | | |
| **Actionability**: Could you implement the suggestion directly? | | |
| **Completeness**: Does it cover all relevant concerns? | | |

---

## Step 5: Document the Differences

### Comparison Table

Fill in this table with your observations:

| Aspect | Without Space | With Space | Improvement |
|---|---|---|---|
| **Specificity of answer** | Generic advice about the topic | References actual project files and patterns | Significant / Moderate / Minimal |
| **Accuracy of recommendations** | May contradict existing patterns | Aligned with established architecture | Significant / Moderate / Minimal |
| **References to project patterns** | None -- uses general best practices | Cites specific files, functions, or conventions | Significant / Moderate / Minimal |
| **Actionability of suggestions** | Requires substantial adaptation | Can be implemented with minimal changes | Significant / Moderate / Minimal |
| **Awareness of constraints** | Ignores project-specific limitations | Accounts for known constraints and trade-offs | Significant / Moderate / Minimal |
| **Code examples** | Generic examples in isolation | Examples that fit your existing codebase | Significant / Moderate / Minimal |

### Score Summary

| Dimension | Without Space | With Space | Delta |
|---|---|---|---|
| Specificity | /5 | /5 | |
| Accuracy | /5 | /5 | |
| Architecture alignment | /5 | /5 | |
| Actionability | /5 | /5 | |
| Completeness | /5 | /5 | |
| **Total** | **/25** | **/25** | |

---

## Step 6: Lessons Learned

Reflect on the comparison and document your takeaways:

### What types of context made the biggest difference?

```
_______________________________________________
```

### What content was missing from the Space that would have helped further?

```
_______________________________________________
```

### When is Space context essential vs. nice-to-have?

Consider these scenarios:

- **Essential**: Questions about project-specific architecture, conventions, or constraints
- **Nice-to-have**: Questions about general programming concepts or language syntax
- **Not needed**: Simple code completions or well-known patterns

### What is the minimum viable Space?

Based on your experience, what is the smallest amount of context that still provides a meaningful improvement?

```
_______________________________________________
```

---

## Bonus: Repeat with a Different Question

For a more thorough evaluation, repeat Steps 2-5 with a different type of question:

1. If your first question was about architecture, try one about testing
2. If your first question was about a specific feature, try one about cross-cutting concerns
3. Compare whether certain question types benefit more from Space context than others

---

## Expected Outcome

After completing this exercise, you should have:

- Quantified evidence of how Space context improves Copilot responses
- A clear understanding of which types of context matter most
- A framework for deciding when to create a Space vs. relying on default context
- Practical experience curating Space content for maximum impact
