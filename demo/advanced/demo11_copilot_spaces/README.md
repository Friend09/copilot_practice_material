# Demo 11: Copilot Spaces

## What This Demo Shows

- **Context curation**: How Spaces let you pre-load Copilot with project-specific knowledge
- **Persistent context**: Knowledge that survives across chat sessions
- **Dramatic quality improvement**: Side-by-side comparison of responses with and without context
- **Team collaboration**: Shareable Spaces that keep entire teams aligned

**Duration**: 10-15 minutes
**Complexity**: Beginner
**Best For**: Showing how curated context transforms Copilot's usefulness

---

## Prerequisites

1. **GitHub Copilot** subscription (Free, Pro, Team, or Enterprise)
2. **Access to github.com** Copilot Spaces (browser-based)
3. **Review** the project context files in `setup/project_context/` before the demo

---

## Quick Setup (2 minutes)

### 1. Navigate to Demo Folder

```bash
cd demo/advanced/demo11_copilot_spaces
```

### 2. Review the Context Files

Browse `setup/project_context/` to familiarize yourself with the sample project:

- `architecture.md` -- system architecture overview
- `api_spec.md` -- API v1/v2 specification
- `coding_standards.md` -- team coding standards

### 3. Open GitHub Copilot Spaces

Navigate to [github.com/copilot/spaces](https://github.com/copilot/spaces) in your browser.

---

## Demo Steps

### Step 1: Why Context Curation Matters (3 minutes)

**Explain the problem to your audience:**

1. **The fresh-start problem**:
   - Every Copilot Chat session starts with zero project knowledge
   - You end up re-explaining your architecture, conventions, and constraints
   - Responses are generic because Copilot lacks your project context

2. **The Spaces solution**:
   - Curate relevant documents, code, and references into a named Space
   - Copilot reads this context before answering your questions
   - Responses become project-aware, specific, and accurate

3. **Availability**:
   - Available on Free, Pro, Team, and Enterprise plans
   - Spaces can be private or shared with your team
   - Content can include markdown, code files, URLs, and repository references

### Step 2: Create a Space Live (5 minutes)

1. **Navigate** to GitHub Copilot Spaces in the browser
2. **Click** "Create a new Space"
3. **Name it**: `API Migration v1 to v2`
4. **Write a description**:

```text
Context for migrating our e-commerce platform API from v1 (session cookies,
monolithic endpoints) to v2 (JWT auth, RESTful microservices). Includes
system architecture, API specifications, and team coding standards.
```

5. **Add content** from `setup/project_context/`:
   - Upload or paste `architecture.md` -- explains the microservices layout
   - Upload or paste `api_spec.md` -- documents v1 endpoints and v2 plans
   - Upload or paste `coding_standards.md` -- team conventions and requirements

6. **Save** the Space

### Step 3: Compare Responses With/Without Context (5 minutes)

This is the most impactful part of the demo. Use the prompts from `prompts.md`.

1. **Without Space context** -- ask in a regular Copilot Chat:

```text
How should we handle authentication for the v2 API?
```

> **Expected**: A generic answer about JWT, OAuth, or API keys with no
> project-specific details.

2. **With Space context** -- ask the same question inside the Space:

```text
How should we handle authentication for the v2 API?
```

> **Expected**: A specific answer that references your architecture (API gateway,
> microservices), the migration from session cookies to JWT, your team's security
> requirements, and the coding standards for error handling.

3. **Highlight the differences**:
   - Generic vs. project-specific recommendations
   - Missing vs. accurate understanding of your current auth system
   - Vague vs. actionable migration steps
   - No awareness vs. full awareness of team coding standards

---

## Expected Results

| Aspect               | Without Space                     | With Space                                    |
|----------------------|-----------------------------------|-----------------------------------------------|
| Auth recommendation  | Generic JWT tutorial              | JWT migration plan from session cookies       |
| Architecture fit     | No awareness of microservices     | References API gateway and service boundaries |
| Migration path       | Vague "update your endpoints"     | Specific v1-to-v2 endpoint mapping            |
| Code standards       | Generic best practices            | Team-specific pytest, type hints, error format|

---

## Key Messages for Your Audience

1. **"Context is everything"** -- The same question yields dramatically different answers
2. **"Set it once, use it always"** -- Spaces persist across sessions
3. **"Share with your team"** -- Everyone benefits from curated project context
4. **"Quality scales"** -- Better context means fewer follow-up questions and corrections

---

## Troubleshooting

### If Spaces are not visible

- Ensure your GitHub Copilot subscription is active
- Check that you are signed in at github.com
- Spaces may require the latest Copilot plan -- verify at github.com/settings/copilot

### If responses do not reflect the context

- Verify the Space is selected/active when asking questions
- Check that the content files were uploaded completely
- Try refreshing the Space or re-adding the content
- Ensure the Space description clearly describes the project scope

### If content upload fails

- Keep individual files under the size limit (check GitHub docs for current limits)
- Use plain markdown for best results
- Avoid binary files -- convert to text or markdown first

---

## Success Metrics

After this demo, your audience should understand:

- Copilot Spaces solve the "fresh start" problem for every chat session
- Curated context transforms generic responses into project-specific guidance
- Spaces are easy to create, update, and share with a team
- The quality improvement is dramatic and immediately visible

---

## Next Steps

- Create Spaces for your current projects and active initiatives
- Share Spaces with team members for consistent AI-assisted development
- Update Spaces as your project evolves (new architecture decisions, updated specs)
- Combine Spaces with custom instructions for maximum context coverage
