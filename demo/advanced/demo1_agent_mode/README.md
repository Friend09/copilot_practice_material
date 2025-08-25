# Demo 1: Agent Mode & Multi-File Intelligence

## What This Demo Shows

- **Autonomous multi-file code generation**: Watch Copilot create an entire system from a single class
- **Context understanding**: AI maintains consistency across multiple files
- **Intelligent planning**: See how Copilot structures complex projects
- **Enterprise-ready code**: Generated code follows best practices

**Duration**: 15-20 minutes
**Complexity**: Intermediate
**Best For**: Showing autonomous development capabilities

---

## Prerequisites

1. **GitHub Copilot** subscription with access to Chat
2. **VS Code** with GitHub Copilot extensions
3. **Python 3.8+** installed
4. **Terminal access** for testing

---

## Quick Setup (2 minutes)

### 1. Navigate to Demo Folder

```bash
cd demo/advanced/demo1_agent_mode
```

### 2. Review Starting Point

Open `setup/product.py` - this simple class will become a complete system!

### 3. Install Dependencies (Optional - for testing results)

```bash
pip install -r setup/requirements.txt
```

### 4. Open Copilot Chat

- Press `Ctrl/Cmd + Shift + I` to open Copilot Chat
- Ensure you're in the demo1_agent_mode folder

---

## Demo Steps

### Step 1: Show the Starting Point (2 minutes)

1. Open `setup/product.py`
2. Explain this basic class will become a complete e-commerce system
3. Run the file to show it works: `python setup/product.py`

### Step 2: The Main Agent Mode Demo (10 minutes)

1. **Copy the primary prompt** from `prompts.md`
2. **Paste into Copilot Chat** and press Enter
3. **Watch Copilot work** - it should:
   - ✅ Plan the project structure
   - ✅ Create multiple related files
   - ✅ Handle imports and dependencies
   - ✅ Maintain consistent patterns

### Step 3: Show the Results (3 minutes)

1. **Explore generated files** - open them side by side
2. **Point out key features**:
   - Consistent naming conventions
   - Proper imports between files
   - Following FastAPI/SQLAlchemy patterns
   - Comprehensive error handling

### Step 4: Iterative Improvement (5 minutes)

Use the follow-up prompts from `prompts.md` to show:

- Adding authentication
- Implementing caching
- Adding comprehensive testing

---

## Expected Results

Copilot should generate a structure like:

```
ecommerce_system/
├── models/
│   ├── product.py       # Enhanced Product model
│   ├── inventory.py     # Inventory tracking
│   └── base.py         # Base model classes
├── api/
│   ├── main.py         # FastAPI application
│   └── routes/
│       └── products.py # Product endpoints
├── schemas/
│   └── product.py      # Pydantic models
├── database/
│   └── connection.py   # SQLAlchemy setup
└── requirements.txt
```

---

## Key Messages for Your Audience

1. **"This isn't autocomplete"** - It's autonomous system development
2. **"Quality is built-in"** - Best practices followed automatically
3. **"Speed without sacrifice"** - Fast development, high quality
4. **"Architecture matters"** - AI understands system design

---

## Troubleshooting

### If Agent Mode isn't working

- ✅ Check your GitHub Copilot subscription includes Chat
- ✅ Ensure you're using Copilot Chat, not just inline suggestions
- ✅ Try breaking the request into smaller parts
- ✅ Make sure you're in the correct folder context

### If file generation is incomplete

- ✅ Ask: "Please complete the remaining files"
- ✅ Be more specific: "Following Python PEP 8 standards"
- ✅ Use follow-up prompts to fill gaps

### If code quality is poor

- ✅ Request: "Include proper error handling and logging"
- ✅ Specify: "Use SQLAlchemy ORM patterns"
- ✅ Ask for: "Add comprehensive docstrings"

---

## Success Metrics

After this demo, your audience should understand:

- ✅ Agent Mode goes beyond completion - it's autonomous development
- ✅ Multi-file intelligence is real - Copilot understands entire projects
- ✅ Architecture is maintained automatically
- ✅ Development speed increases dramatically (50-70% faster)
- ✅ Quality is built-in through best practices

---

## Next Steps

- Try with their own simple classes
- Experiment with different domains (not just e-commerce)
- Use follow-up prompts to explore capabilities
- Apply to real projects starting with new features
