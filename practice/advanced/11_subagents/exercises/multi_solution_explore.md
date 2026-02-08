# Exercise: Multi-Solution Exploration with Parallel Sub-Agents

## Objective

Use sub-agents to explore three different caching implementations simultaneously, then choose the best approach based on the findings.

---

## Scenario

Your task management API (in `parallel_analysis_scenario/`) needs caching to improve performance. There are three viable approaches:

1. **In-memory caching** (simple dict with TTL)
2. **File-based caching** (JSON files on disk)
3. **Redis caching** (external cache server)

Instead of researching each approach sequentially (which would bloat your context), use parallel sub-agents.

## Step 1: Launch Parallel Sub-Agents

Open VS Code Chat in Agent mode and enter:

```
I need to add caching to the task management API in this project.
Please explore three approaches in parallel using sub-agents:

Sub-agent 1: Research and design an in-memory caching solution
using Python dictionaries with TTL (time-to-live) support.
Consider thread safety, memory limits, and cache invalidation.

Sub-agent 2: Research and design a file-based caching solution
using JSON files. Consider file locking, disk I/O performance,
and cache cleanup strategies.

Sub-agent 3: Research and design a Redis-based caching solution.
Consider connection management, serialization, and deployment
requirements.

For each approach, provide:
- Implementation complexity (low/medium/high)
- Performance characteristics
- Scalability considerations
- Code skeleton showing the key classes/functions
- Pros and cons for our specific use case

Then synthesize the findings and recommend the best approach.
```

## Step 2: Observe Parallel Execution

Watch how:
- Three sub-agents are spawned simultaneously
- Each researches independently with its own context
- The main agent receives three summaries without context bloat
- The synthesis uses only the summaries, not the full research

## Step 3: Compare with Sequential Approach

Try the same task without sub-agents:

```
Research three caching approaches for this API:
1. In-memory with TTL
2. File-based with JSON
3. Redis-based

For each, analyze complexity, performance, scalability, and provide
a code skeleton. Then recommend the best approach.
```

Notice:
- The context window fills up quickly with all three analyses
- Later analyses may be influenced by earlier ones (context contamination)
- The final recommendation may be less objective

## What to Learn

| Aspect | Sequential | Parallel Sub-Agents |
|--------|-----------|-------------------|
| Context usage | High (all research in one context) | Low (each sub-agent isolated) |
| Objectivity | May be biased by earlier research | Each analysis is independent |
| Speed | Sequential (slower) | Parallel (faster) |
| Synthesis quality | Based on full context (may lose focus) | Based on clean summaries |

## Challenge

Extend this exercise: after choosing an approach, use a sub-agent to implement it while another sub-agent writes the tests. Use the prompt file from `subagent_prompt_file.prompt.md` to orchestrate this.
