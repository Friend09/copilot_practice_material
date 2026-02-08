# Demo 11: Copilot Spaces Prompts

## Without Space Context (Regular Copilot Chat)

Ask these questions in a regular Copilot Chat session (no Space selected)
to establish the baseline response quality.

### Question 1: Authentication

```text
How should we handle authentication for the v2 API?
```

> **Expected without context**: A generic answer about JWT, OAuth2, or API keys.
> No awareness of your current session-cookie auth or microservices architecture.

### Question 2: Migration strategy

```text
What is the best approach to migrate our API from v1 to v2 without breaking
existing clients?
```

> **Expected without context**: General versioning advice (URL versioning, header
> versioning). No knowledge of your specific endpoints or breaking changes.

### Question 3: Error handling

```text
How should we structure error responses in our API?
```

> **Expected without context**: Generic REST error response patterns. No reference
> to your team's coding standards or existing error format.

---

## With Space Context (Inside the Space)

Ask the same questions inside the "API Migration v1 to v2" Space to show
the dramatic improvement.

### Question 1: Authentication (with context)

```text
How should we handle authentication for the v2 API?
```

> **Expected with context**: References the migration from session cookies to JWT,
> mentions the API gateway as the auth enforcement point, suggests token-based auth
> compatible with your microservices architecture, and follows the team security
> requirements (no hardcoded secrets, input validation).

### Question 2: Migration strategy (with context)

```text
What is the best approach to migrate our API from v1 to v2 without breaking
existing clients?
```

> **Expected with context**: References specific v1 endpoints (`/api/v1/products`,
> `/api/v1/orders`) and their v2 counterparts, identifies the breaking changes
> (auth method, response format), suggests a parallel-run migration with the API
> gateway routing, and recommends the 80% test coverage requirement.

### Question 3: Error handling (with context)

```text
How should we structure error responses in our API?
```

> **Expected with context**: References your coding standards for REST error
> responses (standard error envelope, HTTP status codes, error codes), mentions
> pytest requirements for error path testing, and aligns with the team's input
> validation and security requirements.

---

## Follow-Up Questions (Demonstrate Depth of Context)

These follow-ups show that the Space maintains context across multiple questions.

### Follow-up 1: Service boundaries

```text
Which microservice should own the authentication logic, and how should other
services validate tokens?
```

### Follow-up 2: Database migration

```text
Given our database-per-service architecture, how should we handle data migration
for the user service when switching from session-based to JWT-based auth?
```

### Follow-up 3: Testing the migration

```text
Write a pytest test plan for verifying that v1 clients can still authenticate
during the migration period while v2 clients use JWT.
```

### Follow-up 4: Event-driven considerations

```text
How should our event-driven communication layer handle auth tokens when services
communicate asynchronously?
```

---

## Bonus: Creating Additional Spaces

### Prompt: Ask Copilot to suggest Space content

```text
Based on our project architecture and API spec, what additional documents should
we add to this Space to improve Copilot's understanding of our migration project?
```
