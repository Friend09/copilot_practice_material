# Speaker Notes -- Intro to GitHub Copilot

Quick-reference talking points, engagement tips, and backup plans for both sessions.

---

## "What is Copilot?" Talking Points (3 minutes)

Use these verbatim or adapt to your style. No slides needed -- just talk while VS Code is visible.

### Opening Hook (30 seconds)

> "How many of you have used autocomplete on your phone? GitHub Copilot is like that, but for code -- and it actually understands what you're building."

### What It Is (1 minute)

- AI pair programmer built into VS Code
- Trained on billions of lines of public code
- Three modes you'll see today:
  1. **Inline completions** -- suggests code as you type (like autocomplete on steroids)
  2. **Chat** -- ask questions, explain code, generate tests
  3. **Agent Mode** -- describe a feature, Copilot builds it autonomously
- Works with Python, JavaScript, TypeScript, Java, C#, Go, and 20+ languages

### What It Is NOT (30 seconds)

- Not a replacement for understanding code -- you're still the pilot
- Not always 100% correct -- review before committing
- Not reading your private code unless you opt in (Business/Enterprise have stronger guarantees)

### Why It Matters (1 minute)

- GitHub's research: 55% faster task completion, 46% of code written by Copilot
- Developers stay in flow -- fewer context switches to Stack Overflow / documentation
- Great for learning -- ask it to explain code you don't understand
- Available: Individual ($10/mo), Business ($19/user/mo), Enterprise ($39/user/mo), free for students

---

## Audience Engagement Tips

### Before Starting

- Ask: "Who has heard of GitHub Copilot?" (gauge awareness)
- Ask: "Who has tried it?" (adjust depth accordingly)
- If >50% have used it: skip some inline basics, spend more time on Chat and Agent Mode

### During Inline Completions (Segment 2)

- **Pause** after typing to let the audience see the ghost text appear
- Verbalize: "Notice I only typed the function name and docstring -- Copilot figured out the rest"
- Delete the suggestion and retype to show it's not a recording
- Show that changing the docstring changes the suggestion

### During Chat Demos (Segment 3)

- Read the Chat response aloud (important for remote audiences)
- Zoom in on the Chat panel if needed (Cmd/Ctrl + = while focused)
- Ask audience: "What would you want to ask Copilot next?"
- Point out how Chat references the open file for context

### During Agent Mode (Segment 4)

- Build anticipation: "Now watch -- I'm going to describe what I want, and Copilot will build the whole thing."
- Point out the planning step: "See how it plans before writing code?"
- After generation: "This took about a minute. How long would this take you?"
- Highlight file creation: "It created multiple files with correct imports between them"

---

## Backup Plans

### If Copilot is slow or not responding

- Show the setup files as static examples: "Here's what Copilot typically generates"
- Switch to Chat if inline completions fail
- Have a phone hotspot ready if wifi is unreliable
- Restart VS Code: sometimes extensions need a refresh

### If Agent Mode is not available

- Explain what it would do, show the prompt from prompts.md
- Use regular Chat with the same prompt -- it works, just doesn't create files automatically
- Say: "Agent Mode requires the latest VS Code and Copilot Chat extension"

### If audience is more advanced than expected

- Skip straight to Chat (Segment 3)
- Spend more time on Agent Mode
- Mention the `demo/advanced/` demos for deeper exploration
- Show follow-up prompts that refactor or enhance generated code

### If running short on time

- **Session A**: Skip the "Add history feature" prompt (3d)
- **Session B**: Skip the "Fix error handling" prompt (3e)
- Shorten Q&A to 2-3 minutes
- Agent Mode can be trimmed to just showing the prompt and first minute of generation

---

## Common Q&A Questions and Answers

### "Is it free?"

Individual plan is $10/month or $100/year. Free for verified students, teachers, and popular open source maintainers. Business plan is $19/user/month. Enterprise is $39/user/month.

### "Does it work with [language X]?"

Yes for all major languages. Best quality for Python, JavaScript/TypeScript, Java, C#, Go, Ruby, and Rust. Quality varies for less common languages but it still helps.

### "Does it learn from my private code?"

No, unless you explicitly opt in via telemetry settings. Business and Enterprise plans have stronger data privacy guarantees -- your code is never used for model training on those plans.

### "What about code quality -- can I trust it?"

Treat it like a junior developer's code: always review before committing. It follows patterns in your codebase, so good code begets good suggestions. It's not always right, but it's a great starting point.

### "How is this different from ChatGPT?"

Copilot is integrated directly into your editor. It sees your open files, project structure, and cursor position. ChatGPT is a general chatbot you copy-paste to/from. Copilot is purpose-built for coding workflows.

### "Will AI replace developers?"

No. It handles boilerplate, repetitive tasks, and pattern recognition so you can focus on architecture, design decisions, and complex logic. Think of it as a force multiplier -- the developers who use AI tools will be more productive than those who don't.

### "What model does it use?"

Copilot uses multiple models depending on the task -- GPT-4o for complex tasks, faster models for completions. You can also choose Claude or Gemini models if you prefer.

---

## Session-Specific Notes

### Session A: Productivity Edition

- The `calculator.py` demo works best if you build up gradually: explain -> error handling -> tests -> features
- For the Agent Mode teaser, the Student/GradeBook prompt is deliberately simple so beginners can follow what gets generated
- If short on time, skip the "Add history feature" prompt
- The `calculator.py` deliberately has no type hints -- if asked, mention Copilot can add those too

### Session B: Code Quality Edition

- Let the audience try to spot bugs before Copilot does -- scroll through the file slowly first
- The hardcoded password `"super_secret_123"` usually gets a laugh -- lean into it
- For Agent Mode, the "fix ALL issues" prompt is dramatic because it applies 5+ fixes in one pass
- If short on time, skip the error handling fix (prompt 3e)
- Point out that `find_slow_duplicates` mirrors `find_duplicates` from `starter_functions.py` -- "right way vs wrong way"
