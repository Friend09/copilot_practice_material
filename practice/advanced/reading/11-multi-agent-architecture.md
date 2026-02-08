# Multi-Agent Architecture in GitHub Copilot

## Overview

As AI-assisted development matures, single-agent sessions increasingly struggle with
complex, large-scale tasks. Multi-agent architecture addresses this by spawning
specialized sub-agents that operate with isolated context windows, enabling parallel
execution and cleaner task decomposition. This guide covers the architectural
foundations, invocation methods, configuration options, and real-world strategies for
leveraging multi-agent workflows in GitHub Copilot.

---

## 1. The Context Bloat Problem

### Why Single-Agent Sessions Degrade Over Time

Every interaction with an AI agent appends tokens to the conversation's context window.
Over the course of a long session, this accumulation leads to **context bloat** -- a
state where the agent's effective reasoning degrades because:

- **Token limits are finite.** Models operate within a fixed context window (e.g.,
  128K or 200K tokens). Once the window fills, older context is evicted or summarized
  losilly.
- **Signal-to-noise ratio drops.** Early instructions, file contents from abandoned
  approaches, and resolved error messages clutter the context alongside current,
  relevant information.
- **Attention diffusion.** Transformer-based models distribute attention across all
  tokens. As context grows, the model's ability to focus on the most relevant
  information weakens.
- **Latency increases.** Larger context windows require more computation per
  inference call, slowing response times.
- **Contradictory state.** A session that refactored a function three times retains
  all three versions in context, creating ambiguity about which version is current.

### Symptoms of Context Bloat

| Symptom | Description |
|---------|-------------|
| Hallucinated references | Agent refers to files or functions discussed earlier but since removed |
| Instruction amnesia | Agent forgets constraints stated at the beginning of the session |
| Repetitive suggestions | Agent re-proposes solutions already attempted and rejected |
| Slower responses | Inference time grows noticeably as the session lengthens |
| Inconsistent code style | Agent loses track of established patterns and conventions |

### The Fundamental Insight

Rather than fighting context bloat within a single session, multi-agent architecture
sidesteps it entirely: each sub-agent starts with a **fresh, focused context window**
containing only the information relevant to its specific task.

---

## 2. Sub-Agent Architecture

### How Sub-Agents Work

A sub-agent is an independent AI session spawned by a parent agent. Each sub-agent
receives:

1. **A task description** -- a focused prompt describing exactly what to accomplish.
2. **Relevant context** -- only the files, instructions, and constraints pertinent to
   the task, not the entire parent conversation.
3. **An isolated context window** -- the sub-agent has no access to the parent's
   accumulated conversation history.
4. **Scoped tool access** -- the sub-agent may have access to a subset of available
   tools, determined by configuration.

### Parent-Child Communication

```
┌──────────────────────────────┐
│        Parent Agent          │
│  (orchestrates, delegates)   │
├──────────────────────────────┤
│                              │
│  ┌────────┐  ┌────────┐     │
│  │ Sub-   │  │ Sub-   │     │
│  │Agent A │  │Agent B │     │
│  │(auth)  │  │(API)   │     │
│  └───┬────┘  └───┬────┘     │
│      │           │           │
│      ▼           ▼           │
│  Result A    Result B        │
│      │           │           │
│      └─────┬─────┘           │
│            ▼                 │
│     Synthesized Result       │
└──────────────────────────────┘
```

The parent agent:
- Decomposes the task into discrete units of work.
- Spawns sub-agents with targeted prompts.
- Receives structured results from each sub-agent.
- Synthesizes the results into a cohesive outcome.

### Context Isolation Benefits

- **No cross-contamination.** A sub-agent analyzing authentication code never sees
  unrelated database migration discussions.
- **Maximum context budget.** Each sub-agent can use its full context window for its
  specific task.
- **Deterministic behavior.** With less noise, sub-agents produce more consistent
  and predictable outputs.

---

## 3. Invocation Methods

### Method 1: Prompt Hinting

The simplest approach is to instruct the agent to delegate within your prompt:

```
Analyze the authentication module in src/auth/ for security vulnerabilities.
Spawn a separate agent to review the API rate limiting in src/api/middleware/.
Combine findings into a unified security report.
```

The agent interprets these instructions and decides whether to spawn sub-agents based
on its capabilities and configuration.

### Method 2: Tools Declaration in Prompt Files

In `.prompt.md` files, you can explicitly declare the `agent` tool:

```yaml
---
tools:
  - agent
  - codebase
  - file
---

# Refactoring Coordinator

Review the codebase and identify modules that need refactoring.
For each module, delegate the detailed refactoring to a sub-agent.
Ensure all changes maintain backward compatibility.
```

By listing `agent` in the tools array, you explicitly grant the prompt the ability
to spawn sub-agents.

### Method 3: Agents Property in Custom Agents

Custom agent definitions (`.agent.md` files) support an `agents` property that
declares which other agents can be invoked as sub-agents:

```yaml
---
name: "refactoring-coordinator"
description: "Coordinates large-scale refactoring across services"
tools:
  - agent
  - codebase
agents:
  - "code-reviewer"
  - "test-writer"
  - "documentation-updater"
---

# Refactoring Coordinator

When given a refactoring task:
1. Use @code-reviewer to analyze the current implementation.
2. Apply the refactoring changes.
3. Use @test-writer to generate tests for the new implementation.
4. Use @documentation-updater to update relevant documentation.
```

---

## 4. Parallel Execution

### Running Multiple Sub-Agents Simultaneously

One of the most powerful aspects of multi-agent architecture is parallel execution.
Rather than sequentially analyzing each part of a codebase, multiple sub-agents can
work concurrently:

```
Parent Agent
    ├── Sub-Agent 1: Analyze src/auth/        ──┐
    ├── Sub-Agent 2: Analyze src/api/         ──┤── All run in parallel
    ├── Sub-Agent 3: Analyze src/database/    ──┤
    └── Sub-Agent 4: Analyze src/frontend/    ──┘
                                                 │
                                          Results merged
```

### When Parallel Execution Helps

- **Independent modules.** Services with clear boundaries can be analyzed
  simultaneously.
- **Read-only tasks.** Code review, documentation generation, and analysis
  tasks that do not modify files are ideal candidates.
- **Time-sensitive work.** Parallel execution reduces wall-clock time for
  large-scale analysis.

### When to Avoid Parallel Execution

- **Write conflicts.** If sub-agents modify overlapping files, merge conflicts
  arise.
- **Sequential dependencies.** When Sub-Agent B needs the output of Sub-Agent A,
  parallelism is not possible.
- **Resource constraints.** Each sub-agent consumes API quota and compute resources.

---

## 5. Configuration

### User-Invokable Agents

Agents can be configured as user-invokable, meaning they appear in the agent
selection UI and can be directly triggered by the user:

```yaml
---
name: "security-auditor"
description: "Performs comprehensive security audits"
user-invokable: true
---
```

### Disabling Model-Initiated Invocation

To prevent a parent agent from automatically spawning a sub-agent without user
consent, use the `disable-model-invocation` property:

```yaml
---
name: "production-deployer"
description: "Deploys to production environments"
disable-model-invocation: true
---
```

This ensures the agent can only be invoked explicitly by the user, never
autonomously by another agent -- critical for high-risk operations like deployments.

### Agents List Configuration

The `agents` property in a custom agent's frontmatter defines which sub-agents
are available:

```yaml
---
agents:
  - name: "code-reviewer"
    description: "Reviews code for quality and best practices"
  - name: "test-generator"
    description: "Generates unit and integration tests"
  - name: "doc-writer"
    description: "Writes and updates documentation"
---
```

---

## 6. Best Practices

### When to Use Sub-Agents

| Scenario | Use Sub-Agents? | Rationale |
|----------|----------------|-----------|
| Analyzing a single file | No | Context window is sufficient |
| Refactoring across 10+ files | Yes | Prevents context bloat |
| Writing tests for one module | No | Focused task, single agent works well |
| Comprehensive code review of a monorepo | Yes | Parallel analysis of independent services |
| Quick bug fix | No | Overhead of sub-agent setup exceeds benefit |
| Security audit across microservices | Yes | Each service analyzed independently |

### Task Decomposition Strategies

1. **Decompose by module boundary.** Align sub-agent tasks with existing code
   module boundaries (packages, services, domains).
2. **Decompose by concern.** Separate security analysis, performance analysis,
   and code quality analysis into distinct sub-agent tasks.
3. **Decompose by phase.** Analysis phase (read-only sub-agents), implementation
   phase (write sub-agents), verification phase (test sub-agents).
4. **Keep tasks atomic.** Each sub-agent should have a single, clearly defined
   objective with unambiguous success criteria.
5. **Provide explicit output formats.** Tell each sub-agent exactly how to
   structure its response so the parent can easily synthesize results.

### Anti-Patterns to Avoid

- **Over-delegation.** Spawning a sub-agent for a task that takes 10 lines of
  code adds unnecessary overhead.
- **Vague task descriptions.** "Review this code" is too broad. "Identify SQL
  injection vulnerabilities in the query builder module" is actionable.
- **Missing context.** Failing to provide the sub-agent with necessary files,
  schemas, or constraints leads to hallucinated assumptions.
- **Ignoring results.** The parent agent must actually process and validate
  sub-agent outputs, not blindly concatenate them.

---

## 7. Real-World Case Study: Refactoring a Monolith

### Scenario

A team needs to refactor a monolithic e-commerce application into a modular
architecture. The monolith has five major domains:

- **User Management** (`src/users/`)
- **Product Catalog** (`src/products/`)
- **Order Processing** (`src/orders/`)
- **Payment Gateway** (`src/payments/`)
- **Notification Service** (`src/notifications/`)

### Multi-Agent Approach

**Step 1: Parent Agent -- Analysis Coordination**

The parent agent reads the top-level project structure and spawns five parallel
sub-agents, one per domain:

```
Parent prompt:
"Analyze the monolithic e-commerce application. For each domain module,
 spawn a sub-agent to:
 1. Map all internal dependencies (imports within the module).
 2. Map all external dependencies (imports from other modules).
 3. Identify shared state and tight coupling points.
 4. Propose an interface boundary for extraction."
```

**Step 2: Parallel Sub-Agents -- Domain Analysis**

Each sub-agent operates in isolation:

- **Sub-Agent (Users):** Discovers that `src/users/auth.py` is imported by 14
  files across all other domains. Proposes an `AuthService` interface.
- **Sub-Agent (Products):** Finds that product pricing logic is duplicated in
  `src/orders/pricing.py`. Recommends consolidation.
- **Sub-Agent (Orders):** Identifies direct database queries against the `users`
  and `products` tables. Recommends API-based access.
- **Sub-Agent (Payments):** Notes PCI compliance concerns with how card data
  flows through the order module. Proposes isolation.
- **Sub-Agent (Notifications):** Finds it is already loosely coupled. Recommends
  event-driven extraction with minimal changes.

**Step 3: Parent Agent -- Synthesis**

The parent agent receives all five reports and:
- Identifies cross-cutting concerns (auth is used everywhere).
- Prioritizes extraction order (notifications first, payments last due to
  compliance complexity).
- Generates a phased refactoring plan with dependency ordering.

**Step 4: Implementation Sub-Agents**

The parent spawns sequential sub-agents for implementation, starting with the
lowest-risk extraction:

1. Sub-Agent: Extract `NotificationService` with event bus.
2. Sub-Agent: Define `AuthService` interface and adapter.
3. Sub-Agent: Consolidate pricing logic into `ProductCatalog`.
4. Sub-Agent: Replace direct DB queries in `Orders` with service calls.
5. Sub-Agent: Isolate `PaymentGateway` with compliance boundaries.

### Outcome

- **Total context used per sub-agent:** ~15K tokens (vs. ~180K+ for a single agent
  attempting the entire analysis).
- **Wall-clock time:** Analysis phase completed in parallel, reducing time by ~4x.
- **Quality:** Each sub-agent produced focused, high-quality analysis without
  interference from unrelated domain knowledge.

---

## Summary

Multi-agent architecture transforms how developers tackle large-scale AI-assisted
tasks. By understanding the context bloat problem and leveraging sub-agents with
isolated context windows, you can achieve higher quality results, faster execution,
and more predictable behavior. The key is thoughtful task decomposition -- matching
the granularity of sub-agent tasks to the natural boundaries in your codebase.

---

## Further Reading

- [GitHub Copilot Agent Mode Documentation](https://docs.github.com/en/copilot)
- [Prompt Engineering for Multi-Agent Systems](https://docs.github.com/en/copilot/using-github-copilot/prompt-engineering-for-github-copilot)
- Reading 07: Agent Mode and Coding Agent (foundational concepts)
- Reading 13: Agent Skills and Custom Agents (custom agent configuration)
