# Module 07 – Multi-Model Support: Choosing the Right AI Model

## 🎯 Overview

As of 2024, GitHub Copilot supports multiple AI models from different providers, giving you the flexibility to choose the best model for your specific task. This module teaches you how to select and optimize models for different coding scenarios.

## Available Models

GitHub Copilot now offers access to models from three major AI providers:

### OpenAI Models
- **GPT-4o** - Latest GPT-4 optimized version
  - Best for: Complex reasoning, architectural decisions
  - Strengths: Deep understanding, nuanced code generation
  - Context window: Large (128K tokens)
  - Speed: Moderate

- **GPT-4 Turbo** - Faster variant of GPT-4
  - Best for: General-purpose coding
  - Strengths: Balanced performance and quality
  - Context window: Large (128K tokens)
  - Speed: Fast

- **o1-preview / o3-mini / o4-mini** - Reasoning models
  - Best for: Complex algorithmic problems, optimization
  - Strengths: Step-by-step reasoning, mathematical problems
  - Context window: Medium
  - Speed: Slower (more thinking time)

### Anthropic Models (Claude)
- **Claude 3.5 Sonnet** - Current flagship
  - Best for: Long contexts, detailed analysis
  - Strengths: Excellent instruction following, safety
  - Context window: Very large (200K tokens)
  - Speed: Fast

- **Claude Opus 4** - Most capable Claude model
  - Best for: Most complex tasks requiring deep reasoning
  - Strengths: Exceptional quality, thorough responses
  - Context window: Very large (200K tokens)
  - Speed: Moderate

- **Claude 3.7 Thinking** - Reasoning variant
  - Best for: Problems requiring explicit reasoning chains
  - Strengths: Transparent thought process
  - Context window: Large
  - Speed: Moderate

### Google Models (Gemini)
- **Gemini 2.0 Flash** - Fast general model
  - Best for: Quick iterations, rapid prototyping
  - Strengths: Speed, efficiency, multimodal
  - Context window: Very large (1M tokens)
  - Speed: Very fast

- **Gemini 2.5 Pro** - Advanced reasoning
  - Best for: Complex tasks, large codebases
  - Strengths: Long context, multimodal understanding
  - Context window: Massive (2M tokens)
  - Speed: Fast

## Model Selection Guide

### By Task Type

| Task Type | Recommended Model | Why |
|-----------|------------------|-----|
| Quick completions | Gemini 2.0 Flash | Speed matters most |
| Code refactoring | GPT-4 Turbo | Good balance |
| Complex algorithms | o3-mini / Claude Opus | Deep reasoning needed |
| Large codebase understanding | Gemini 2.5 Pro / Claude 3.5 | Huge context windows |
| Documentation | Claude 3.5 Sonnet | Excellent at clear writing |
| Security review | Claude Opus 4 | Careful, thorough analysis |
| API design | GPT-4o | Strong at system design |
| Mathematical problems | o3-mini | Specialized reasoning |
| UI/Frontend | GPT-4 Turbo | Good at modern frameworks |
| Performance optimization | o3-mini | Algorithmic thinking |

### By Context Size Needs

| Context Needed | Recommended Models |
|----------------|-------------------|
| Small (< 10K tokens) | Any model works well |
| Medium (10-50K tokens) | GPT-4, Claude, Gemini Flash |
| Large (50-100K tokens) | GPT-4o, Claude 3.5, Gemini Pro |
| Very Large (100K+ tokens) | Claude 3.5, Gemini 2.5 Pro |
| Massive (1M+ tokens) | Gemini 2.5 Pro |

### By Speed Requirements

| Priority | Recommended Models |
|----------|-------------------|
| Need instant response | Gemini 2.0 Flash |
| Fast iteration | GPT-4 Turbo, Gemini Flash |
| Balanced | Claude 3.5 Sonnet, GPT-4o |
| Quality over speed | Claude Opus 4, o3-mini |

## How to Switch Models

### In VS Code

1. **Open Copilot Chat**
   - `Ctrl+Shift+I` (Windows/Linux) or `Cmd+Shift+I` (Mac)

2. **Access Model Picker**
   - Look for model dropdown in Chat interface
   - Or use settings: `GitHub Copilot > Chat: Model`

3. **Select Your Model**
   - Click dropdown
   - Choose from available models
   - Selection persists for your session

### Via Settings

```json
{
  "github.copilot.chat.model": "gpt-4o",
  // or "claude-3-5-sonnet"
  // or "gemini-2-0-flash"
}
```

## Exercise 1: Model Comparison - Code Generation

Test the same prompt with different models and compare results.

### Task
Generate a Python function for this prompt:

```
Create a function that implements a binary search tree with insert, search,
and delete operations. Include proper error handling and docstrings.
```

### Process
1. Select **GPT-4 Turbo** → Generate code → Note the result
2. Select **Claude 3.5 Sonnet** → Same prompt → Compare
3. Select **Gemini 2.0 Flash** → Same prompt → Compare
4. Select **o3-mini** → Same prompt → Compare

### Questions to Consider
- Which model provided the most complete solution?
- Which was fastest?
- Which had the best documentation?
- Which handled edge cases best?
- Which would you choose for this task? Why?

## Exercise 2: Model Comparison - Code Review

Ask each model to review the same code:

```python
def process_orders(orders):
    result = []
    for o in orders:
        if o['status'] == 'pending':
            result.append(o)
    return result
```

### Prompt
```
Review this code for improvements in performance, readability,
and Pythonic style. Suggest refactorings.
```

### Compare
- **GPT-4o**: What improvements does it suggest?
- **Claude 3.5**: How detailed is the review?
- **Gemini Flash**: How quickly does it respond?

## Exercise 3: Complex Problem Solving

Test models on algorithmic challenges:

### Task
```
Implement Dijkstra's shortest path algorithm with these requirements:
- Support weighted directed graphs
- Handle negative weights gracefully (detect and warn)
- Optimize for sparse graphs
- Include comprehensive unit tests
- Time complexity: O((V + E) log V)
```

### Recommended Models to Try
1. **o3-mini** - Should show explicit reasoning
2. **Claude Opus 4** - Should be thorough
3. **GPT-4o** - Good baseline
4. **Gemini 2.5 Pro** - Fast with good quality

### Evaluation Criteria
- Correctness of implementation
- Efficiency of algorithm
- Quality of error handling
- Completeness of tests
- Clarity of explanation

## Exercise 4: Large Codebase Understanding

Test models with large context:

### Setup
1. Open multiple related files (10-15 files)
2. Ask a question that requires understanding relationships

### Example Prompt
```
Analyze the architecture of this application. Identify:
- Design patterns used
- Potential bottlenecks
- Security concerns
- Opportunities for optimization
- Breaking changes if we upgrade to Python 3.12
```

### Models to Test
- **Gemini 2.5 Pro** - Largest context window
- **Claude 3.5 Sonnet** - Excellent at analysis
- **GPT-4o** - Strong reasoning

### Compare
- Which model provided the most insightful analysis?
- Which caught the most issues?
- Which gave the most actionable recommendations?

## Exercise 5: Real-World Scenario - Feature Implementation

Implement a complete feature and note which models you prefer for each step:

### Feature: User Authentication System

1. **Architecture Design**
   - Which model did you use? Why?
   - Prompt: "Design an authentication system with JWT tokens..."

2. **Implementation**
   - Which model for writing the code?
   - Did you switch models during implementation?

3. **Testing**
   - Which model for generating tests?
   - Were the tests comprehensive?

4. **Documentation**
   - Which model wrote the best docs?

5. **Security Review**
   - Which model for security analysis?
   - Did it catch potential vulnerabilities?

### Reflect
- Did you use different models for different steps?
- What was your strategy?
- What did you learn about each model's strengths?

## Best Practices

### 1. Match Model to Task
```
✅ Use Gemini Flash for quick iterations
✅ Use Claude Opus for critical security code
✅ Use o3-mini for complex algorithms
❌ Don't use slow models for simple tasks
❌ Don't use fast models for critical decisions
```

### 2. Start Fast, Refine Later
```
1. Use fast model (Gemini Flash) for initial draft
2. Use reasoning model (o3-mini) to optimize
3. Use thorough model (Claude Opus) for final review
```

### 3. Consider Cost
- Faster/smaller models are typically cheaper
- Use them for routine tasks
- Save premium models for complex problems

### 4. Experiment and Learn
- Each model has unique characteristics
- Your preference may differ from others
- Build intuition through practice

### 5. Context Management
- Larger context = better understanding BUT slower response
- Close irrelevant files before asking questions
- Be explicit about what context matters

## Advanced: Model-Specific Prompting

Different models respond better to different prompting styles:

### For Claude
```
✅ Step-by-step instructions work well
✅ Appreciates explicit constraints
✅ Good with "thinking out loud" requests
```

### For GPT
```
✅ Concise, direct prompts
✅ Good with examples (few-shot)
✅ Responds well to role-playing ("You are an expert...")
```

### For Gemini
```
✅ Works well with multimodal inputs
✅ Efficient with concise prompts
✅ Good at handling very long contexts
```

### For Reasoning Models (o1/o3)
```
✅ Give complex problems that need thinking
✅ Don't rush - they take time to reason
✅ Ask for step-by-step explanations
```

## Troubleshooting

### Model not available?
- Check your Copilot subscription tier
- Some models require Business/Enterprise
- Feature may be in gradual rollout

### Different results each time?
- AI models have inherent randomness
- Temperature settings affect variation
- Multiple attempts can yield different solutions

### Model seems worse than expected?
- Check your prompt quality
- Ensure sufficient context
- Try rephrasing your question

## Comparison Matrix

| Feature | GPT-4o | Claude 3.5 | Gemini 2.0 | o3-mini |
|---------|--------|------------|------------|---------|
| Speed | ⚡⚡⚡ | ⚡⚡⚡ | ⚡⚡⚡⚡ | ⚡⚡ |
| Quality | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| Context | 128K | 200K | 1M | 64K |
| Reasoning | Good | Excellent | Good | Exceptional |
| Code Gen | Excellent | Excellent | Very Good | Excellent |
| Cost | $$$ | $$$$ | $$ | $$$$ |

## Key Takeaways

1. **Different models excel at different tasks**
2. **Speed vs. quality is a real tradeoff**
3. **Context window size matters for large projects**
4. **Experiment to find your preferences**
5. **Consider switching models during development**
6. **Reasoning models are worth the wait for hard problems**

## Next Steps

- Try **Copilot Extensions** (Module 08) to integrate external models
- Explore **Prompt Files** (Module 09) to save model-specific prompts
- Learn **Vision for Copilot** (Module 10) which leverages multimodal models

## Resources

- [GitHub Copilot Model Documentation](https://docs.github.com/en/copilot)
- [OpenAI Model Comparison](https://platform.openai.com/docs/models)
- [Anthropic Claude Models](https://www.anthropic.com/claude)
- [Google Gemini Documentation](https://deepmind.google/technologies/gemini/)
