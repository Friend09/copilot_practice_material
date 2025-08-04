# Copilot Practice Material (Python + VS Code)

This comprehensive repository contains:

- **Hands-on exercises** (beginner and advanced tracks)
- **Hackathon challenges** (guided and minimal formats for different skill levels)
- **Learning resources** including a 30-day roadmap and troubleshooting guides

All materials help you master **GitHub Copilot**, **Copilot Chat**, and the new **Copilot agent (MCP)** capabilities.
Examples are in **Python 3.8+** and designed for **VS Code**.

---

## 1 Repository Structure

```
copilot_practice_material/
├── README.md                          # This file
├── _copilot_practice_material.code-workspace
├── practice/                          # Structured learning exercises
│   ├── beginner/                      # Beginner track (01-05 modules + daily exercises)
│   └── advanced/                      # Advanced track (01-05 modules + daily exercises)
├── demo/                              # Example implementations and demos
│   ├── basic/                         # Basic Copilot usage examples
│   └── advanced/                      # Advanced patterns and techniques
├── hackathon/                         # Hackathon challenges
│   ├── guided/                        # Structured challenges with detailed guidance
│   └── minimal/                       # Open-ended challenges with minimal scaffolding
├── projects/                          # Project-based learning
│   ├── 30-day-program/                # Weekly projects for the 30-day program
│   └── independent/                   # Standalone projects for skill development
└── docs/                              # Documentation and learning resources
    ├── guides/                        # Learning guides and structured programs
    ├── reference/                     # Tips, tricks, and troubleshooting
    └── sessions/                      # Workshop materials and session notes
```

Each directory contains self-contained materials with clear README files and starter code.
Work through `practice/` exercises in order for the best learning experience.

> **💡 Tip**: Complete the practice exercises before attempting hackathon challenges for the best learning experience.

---

## 2 Prerequisites

| Tool / Account                       | Purpose                            | Minimum Version       |
| ------------------------------------ | ---------------------------------- | --------------------- |
| **GitHub account** with Copilot seat | Enables Copilot suggestions & chat | any paid Copilot plan |
| **VS Code**                          | Editor & Copilot extensions        | 1.85 or later         |
| **GitHub Copilot** extension         | Inline code completions            | latest                |
| **GitHub Copilot Chat** extension    | Chat & agent mode                  | v ≥ 0.10              |
| **Python**                           | Run examples                       | 3.8+                  |
| **uv** (optional)                    | Fast `pip` alternative             | 0.1.30+               |
| **make** (optional)                  | Convenience tasks                  | any                   |

> **Note** – The advanced MCP exercise also requires enabling the **"GitHub MCP Agent"** feature flag in your organization or on your GitHub account.

---

## 3 Quick Setup

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-org/copilot_practice_material.git
   cd copilot_practice_material
   ```

2. **Open in VS Code**

   ```bash
   code _copilot_practice_material.code-workspace
   # or simply
   code .
   ```

3. **Install Python deps**

   ```bash
   # fast path with uv
   uv pip install -r requirements.txt

   # or classic pip / virtualenv
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Sign in to GitHub inside VS Code**
   Verify that the Copilot status icon (bottom‑right) reads **"Copilot: ON"**.

5. **(Advanced) Enable agent mode**

   - Ensure the **GitHub Copilot Chat** extension is installed.
   - Command Palette → **GitHub Copilot: Toggle Agent Mode**.
   - When prompted, approve access to the "github" MCP server.

---

## 4 Learning Paths

### 🟢 Beginner Track (`practice/beginner/`)

Perfect for those new to GitHub Copilot:

| Module                    | Topic                      | Goal                                              |
| ------------------------- | -------------------------- | ------------------------------------------------- |
| 01_hello_copilot          | Installation & Hello World | Accept your first Copilot suggestion              |
| 02_function_completion    | Function bodies            | Use comments/docstrings to drive completions      |
| 03_loops_logic            | Loops & algorithms         | Generate multi‑line code for Fibonacci & primes   |
| 04_tdd                    | Test‑driven development    | Implement code to satisfy provided tests          |
| 05_documentation_refactor | Docs & refactor            | Use Copilot to document and improve existing code |

**Daily Exercises**: days 01-14 with progressive skill building

### 🔵 Advanced Track (`practice/advanced/`)

For experienced developers exploring sophisticated features:

| Module                 | Topic                   | Goal                                          |
| ---------------------- | ----------------------- | --------------------------------------------- |
| 01_custom_instructions | Repository instructions | Steer Copilot via project-specific guidelines |
| 02_advanced_prompts    | Multi‑line prompts      | Generate complete features and applications   |
| 03_project_context     | Custom APIs & context   | Use your own APIs in Copilot completions      |
| 04_refactor_debug      | Refactoring & debugging | Refactor & debug legacy code with Chat        |
| 05_mcp_agent           | Agent mode (MCP)        | Let Copilot agent fix issues & open PRs       |

**Daily Exercises**: days 15-30 with complex scenarios and real-world applications

### 🎯 Hands-On Challenges (`hackathon/`)

Two formats for different learning styles:

#### `guided/` - Structured Experience

- **Duration**: 1-2 hours per challenge
- **Style**: Detailed briefs with comprehensive guidance
- **Best for**: Educational settings, Copilot newcomers

#### `minimal/` - Open-Ended Space

- **Duration**: 2-4 hours (flexible)
- **Style**: Minimal scaffolding with creative freedom
- **Best for**: Experienced developers, creative exploration

### 📚 Supporting Materials

- **`demo/`** - Live examples and reference implementations
- **`projects/`** - Extended project-based learning (30-day program + independent projects)
- **`docs/`** - Comprehensive guides, tips, and troubleshooting resources

---

## 5 Getting Started

1. **Choose Your Learning Path**

   - **New to Copilot?** Start with `practice/beginner/01_hello_copilot/`
   - **Have experience?** Jump to `practice/advanced/` or try `hackathon/` challenges
   - **Want structured learning?** Follow the 30-day program in `docs/guides/`

2. **Set Up Your Environment**

   ```bash
   # Clone and open in VS Code
   git clone https://github.com/your-org/copilot_practice_material.git
   cd copilot_practice_material
   code _copilot_practice_material.code-workspace
   ```

3. **Install Dependencies**

   ```bash
   # Fast path with uv
   uv pip install -r requirements.txt

   # Or classic pip/virtualenv
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Verify Copilot Setup**
   - Ensure the Copilot status icon (bottom‑right) reads **"Copilot: ON"**
   - For agent mode: Command Palette → **GitHub Copilot: Toggle Agent Mode**

## 6 Usage Patterns

- **Inline Suggestions** – Type, accept with `Tab`, cycle variants with `Alt` + `[` / `Alt` + `]`
- **Copilot Chat** – `Ctrl` + `Shift` + `I` (or chat icon) to open panel; ask questions
- **Agent Tasks** – Switch chat panel to **Agent** mode; issue commands like:
  > _Fix issue #1 in `bugfix/buggy_code.py` and commit the changes._
- **Daily Practice** – Spend 30-45 minutes daily with exercises and challenges

---

## 7 Best Practices

1. Write **clear, goal‑oriented prompts**—context matters.
2. **Iterate.** Refine the prompt or ask Chat for alternatives if the first answer isn't right.
3. **Review & test** every suggestion—you own correctness.
4. **Guard secrets & IP.** Never paste credentials into prompts.
5. **Limit agent scope.** Give explicit tasks and approve cautiously.

---

## 8 Contributing

Spotted an issue or have a new exercise idea?
Open an **Issue** or submit a **Pull Request**—follow the existing folder conventions and include comprehensive README files.

---

## 9 License

For educational and internal-training use. See [LICENSE](LICENSE) for details.
