# Exercise 1: Create a Copilot Space

## Scenario: API Migration Planning

You are leading a migration from API v1 to API v2. Multiple team members need context about the migration goals, breaking changes, and implementation strategy. You will create a Copilot Space that grounds Copilot's responses in all the relevant migration context.

---

## Steps

### Step 1: Navigate to Copilot Spaces

1. Open your browser and go to [github.com](https://github.com)
2. Click the **Copilot icon** in the top navigation bar
3. Select **Spaces** from the dropdown, or navigate directly to [github.com/copilot/spaces](https://github.com/copilot/spaces)
4. You should see the Spaces dashboard with any existing Spaces listed

### Step 2: Create a New Space

1. Click **"Create Space"**
2. Set the **name** to: `API Migration - v1 to v2`
3. Write a **description** that explains the migration goals:

   ```
   Context for migrating our REST API from v1 to v2. Includes route
   definitions, breaking changes, migration timeline, and architectural
   decisions. Use this Space when answering questions about the migration
   plan, backwards compatibility, or implementation priorities.
   ```

### Step 3: Add Context to the Space

Add the following types of content to your Space. Use your own repository, or create sample content for practice:

#### 3a. Repository Route Definitions

- Add your API route definition files (e.g., `src/routes/v1/`, `src/routes/v2/`)
- If you do not have route files, add any source files that represent the "before" and "after" of a migration

#### 3b. API Documentation

- Add your API documentation markdown files (e.g., `docs/api-v1.md`, `docs/api-v2.md`)
- Include endpoint descriptions, request/response schemas, and authentication details

#### 3c. Relevant Issue Threads

- Search your repository's issues for migration-related discussions
- Add 2-3 issue threads that capture design decisions, concerns, or requirements
- Example: "Issue #42: Plan breaking changes for v2 endpoints"

#### 3d. Architecture Decision Records

- Add any ADR (Architecture Decision Record) files from your repository
- If you do not have ADRs, add a freeform note summarizing key architectural decisions:

  ```
  Decision: Move from REST to REST + GraphQL hybrid for v2
  Rationale: Complex nested queries are inefficient with pure REST
  Status: Approved
  Date: 2026-01-15
  ```

#### 3e. Freeform Notes

- Add a note with migration priorities:

  ```
  Migration Priorities:
  1. Authentication endpoints (breaking change: OAuth2 replaces API keys)
  2. User management endpoints (additive changes only)
  3. Data export endpoints (new in v2)
  4. Deprecation notices for v1 endpoints (6-month sunset)
  ```

### Step 4: Write the Space Description

Review your Space and refine the description to accurately represent the content. A good description helps Copilot understand when and how to use the Space context. Consider including:

- The purpose of the Space
- What types of questions it can help answer
- Any important constraints or decisions already made

### Step 5: Test the Space with Copilot

Open the Space and ask Copilot the following questions. Note the quality of each response:

1. **"What are the breaking changes between v1 and v2?"**
   - Does the answer reference your actual route definitions?
   - Does it mention specific endpoints?

2. **"What is the migration timeline?"**
   - Does it reference the priorities from your notes?
   - Does it account for the deprecation schedule?

3. **"How should we handle backwards compatibility during the migration?"**
   - Does the response reference your architectural decisions?
   - Does it suggest strategies consistent with your existing patterns?

4. **"Write a migration guide for consumers of the v1 API."**
   - Is the guide specific to your actual API?
   - Does it reference real endpoints and schema changes?

### Step 6: Compare With and Without Space Context

1. **Without Space**: Open a regular Copilot chat (not in the Space) and ask the same questions from Step 5
2. **With Space**: Return to your Space and compare the answers
3. Note the differences in:
   - Specificity (generic vs. project-specific advice)
   - Accuracy (correct references to your actual codebase)
   - Actionability (can you directly use the suggestions?)

### Step 7: Refine the Space

Based on your testing:

1. **Add missing context**: If Copilot's answers were missing key information, add the relevant content to the Space
2. **Remove noise**: If the Space has too much content, remove files that are not contributing to answer quality
3. **Update notes**: Refine your freeform notes to better capture the most important context
4. **Re-test**: Ask the same questions again and observe improvements

---

## Tips for Effective Space Curation

- **Be selective**: A focused Space with 10 highly relevant files outperforms a Space with 100 loosely related files
- **Include decision context**: ADRs, issue discussions, and PR reviews often contain the "why" behind decisions -- this is exactly what Copilot needs
- **Update regularly**: Keep Space content current as your project evolves
- **Use descriptive names**: Name your Spaces clearly so team members can find the right one quickly
- **Layer your Spaces**: Create separate Spaces for different aspects of a project (architecture, testing strategy, deployment) rather than one massive Space

---

## Expected Outcome

After completing this exercise, you should have:

- A functional Copilot Space with curated context for a real project scenario
- First-hand experience of how context quality affects Copilot's response quality
- A mental model for what types of content are most valuable in a Space
- An understanding of the iterative process of Space curation
