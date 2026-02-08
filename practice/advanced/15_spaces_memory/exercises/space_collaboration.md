# Exercise 2: Space Collaboration

## Objective

Learn how to use Copilot Spaces as a shared knowledge base for your team. You will create a Space, share it with team members, test consistency of responses, and build an onboarding Space for new hires.

---

## Part 1: Create a Team Project Space

### Step 1: Choose a Team Project

Select a project that your team actively works on. The best candidate is a project where:

- Multiple people contribute code
- There are established conventions and patterns
- New team members need ramp-up time
- Architectural decisions have been made that are not obvious from the code alone

### Step 2: Create the Space

1. Navigate to [github.com/copilot/spaces](https://github.com/copilot/spaces)
2. Create a new Space named after your project (e.g., "Payment Service - Team Context")
3. Write a description that explains what the Space covers and who it is for

### Step 3: Add Shared Knowledge Content

Add content that represents your team's collective knowledge:

| Content Category | What to Add | Why It Matters |
|---|---|---|
| Architecture overview | `docs/architecture.md` or equivalent | Grounds answers in your actual system design |
| Coding standards | `.eslintrc`, style guides, convention docs | Ensures suggestions follow team norms |
| Key design decisions | ADRs, design docs, relevant PR discussions | Provides the "why" behind patterns |
| Common patterns | Example implementations of recurring patterns | Helps Copilot suggest consistent solutions |
| Known gotchas | Notes about pitfalls, workarounds, tech debt | Prevents Copilot from suggesting approaches that will not work |
| Testing strategy | Test configuration, testing guidelines | Ensures test suggestions match your approach |

---

## Part 2: Share and Test Consistency

### Step 4: Share the Space with Team Members

1. Open your Space and find the sharing settings
2. Share the Space with 2-3 team members
3. Ensure each person can access and open the Space

### Step 5: Run a Consistency Test

Have each team member perform the following test independently:

1. **Open the shared Space** in Copilot
2. **Ask the exact same question**: Choose a question relevant to your project, for example:
   - "How should I add a new API endpoint to this service?"
   - "What is the testing strategy for database interactions?"
   - "How does authentication work in this system?"
3. **Record the response** -- copy it to a shared document

### Step 6: Compare Responses

Create a comparison document with columns for each team member's response. Evaluate:

- **Consistency**: Are the responses aligned on key points?
- **Accuracy**: Do all responses correctly reference project patterns?
- **Completeness**: Does each response cover the important aspects?
- **Specificity**: Are responses grounded in your actual codebase?

If responses diverge significantly, identify what context is missing from the Space and add it.

---

## Part 3: Iterate on Space Content

### Step 7: Refine Based on Results

1. **Identify gaps**: Where did responses lack accuracy or specificity?
2. **Add missing context**: Include the files, notes, or discussions that would fill those gaps
3. **Remove irrelevant content**: If some files are adding noise, remove them
4. **Re-test**: Have team members ask the same questions again and compare improvement

### Step 8: Establish a Space Maintenance Process

Decide as a team:

- **Who owns the Space?** Assign a maintainer (or rotate responsibility)
- **When to update?** After major architectural changes, new conventions, or quarterly reviews
- **How to suggest changes?** Create a channel (Slack, Teams, or GitHub Discussion) for Space update requests
- **What triggers a review?** Poor Copilot responses, new team members, major releases

---

## Part 4: Onboarding Space

### Step 9: Create a "Getting Started" Space for New Team Members

1. Create a new Space named "[Project Name] - Getting Started"
2. Add content specifically curated for onboarding:

   **Essential content to include:**

   - **Repository README** -- high-level overview
   - **Setup guide** -- local development environment instructions
   - **Architecture diagram or description** -- how the system fits together
   - **Key terminology** -- glossary of project-specific terms
   - **Common workflows** -- how to run tests, deploy, create PRs
   - **Who to ask** -- team member roles and areas of expertise
   - **First tasks guide** -- suggestions for good first contributions

3. Write a Space description targeted at new hires:

   ```
   Welcome to [Project Name]! This Space contains everything you need to
   get started as a new team member. Open this Space before asking Copilot
   any questions about the project -- it will give you accurate,
   project-specific answers instead of generic ones.

   Start by asking: "Give me an overview of this project and how to set up
   my local development environment."
   ```

### Step 10: Test the Onboarding Space

Simulate the onboarding experience:

1. Have someone unfamiliar with the project (or pretend you are new) open the Space
2. Ask common onboarding questions:
   - "How do I set up my local development environment?"
   - "What is the architecture of this system?"
   - "How do I run the test suite?"
   - "What are the coding conventions for this project?"
   - "Where should I start if I want to fix a bug?"
3. Evaluate whether the answers would genuinely help a new team member
4. Refine the Space based on gaps

---

## Part 5: Best Practices for Maintaining Spaces Over Time

### Content Freshness

- **Schedule quarterly reviews** of Space content
- **Update after major changes**: new services, framework upgrades, convention changes
- **Archive stale Spaces** that are no longer relevant
- **Version your notes**: include dates in freeform notes so readers know how current they are

### Organization

- **One Space per concern**: Prefer multiple focused Spaces over one giant Space
  - Good: "Auth Service", "Payment Processing", "Onboarding Guide"
  - Avoid: "Everything About Our Project"
- **Consistent naming**: Use a team convention for Space names (e.g., "[Service] - [Purpose]")
- **Clear descriptions**: Write descriptions that help people choose the right Space

### Team Habits

- **Reference Spaces in code reviews**: "Check the Auth Space for context on this pattern"
- **Link Spaces in issue descriptions**: "Open the Migration Space before working on this issue"
- **Onboard with Spaces**: Make opening the Getting Started Space the first step for new hires
- **Celebrate good curation**: Recognize team members who keep Spaces useful and current

---

## Expected Outcome

After completing this exercise, you should have:

- A shared team Space that provides consistent, accurate context to all team members
- An onboarding Space that accelerates new team member ramp-up
- A maintenance process for keeping Spaces current and useful
- First-hand experience of how shared context improves team-wide Copilot quality
