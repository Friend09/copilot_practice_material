# Copilot Practice Material (Python + VS Code)

This repository contains hands‑on exercises—beginner *and* advanced—that will help you master **GitHub Copilot**, **Copilot Chat**, and the new **Copilot agent (MCP)** capabilities.
All examples are in **Python 3.8+** and assume you work in **VS Code**.

---

## 1  Repository Structure

```
.
├── advanced_copilot_practice/
│   ├── 01_custom_instructions/
│   ├── 02_advanced_prompts/
│   ├── 03_project_context/
│   ├── 04_refactor_debug/
│   └── 05_mcp_agent/
├── beginner_copilot_practice/
│   ├── 01_hello_copilot/
│   ├── 02_function_completion/
│   ├── 03_loops_logic/
│   ├── 04_tdd/
│   └── 05_documentation_refactor/
└── _copilot_practice_material.code-workspace   # optional VS Code workspace
```

Each numbered folder is a self‑contained lab with its own **README.md** and starter code.
Work through them in ascending order.

---

## 2  Prerequisites

| Tool / Account | Purpose | Minimum Version |
|----------------|---------|-----------------|
| **GitHub account** with Copilot seat | Enables Copilot suggestions & chat | any paid Copilot plan |
| **VS Code** | Editor & Copilot extensions | 1.85 or later |
| **GitHub Copilot** extension | Inline code completions | latest |
| **GitHub Copilot Chat** extension | Chat & agent mode | v ≥ 0.10 |
| **Python** | Run examples | 3.8+ |
| **uv** (optional) | Fast `pip` alternative | 0.1.30+ |
| **make** (optional) | Convenience tasks | any |

> **Note** – The advanced MCP exercise also requires enabling the **“GitHub MCP Agent”** feature flag in your organization or on your GitHub account.

---

## 3  Quick Setup

1. **Clone the repo**

   ```bash
   git clone https://github.com/your-org/copilot_practice_material.git
   cd copilot_practice_material
   ```

2. **Install Python deps**

   ```bash
   # fast path with uv
   uv pip install -r requirements.txt

   # or classic pip / virtualenv
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Open in VS Code**

   ```bash
   code _copilot_practice_material.code-workspace
   # or simply
   code .
   ```

4. **Sign in to GitHub inside VS Code**
   Verify that the Copilot status icon (bottom‑right) reads **“Copilot: ON”**.

5. **(Advanced) Enable agent mode**

   * Ensure the **GitHub Copilot Chat** extension is installed.
   * Command Palette → **GitHub Copilot: Toggle Agent Mode**.
   * When prompted, approve access to the “github” MCP server.

---

## 4  Project Contents

### 🟢 Beginner Track (`beginner_copilot_practice/`)

| Lab | Skill Focus |
|-----|-------------|
| `01_hello_copilot` | Accept your first suggestion (“Hello World”). |
| `02_function_completion` | Fill in function bodies from docstrings/comments. |
| `03_loops_logic` | Generate algorithms (Fibonacci, prime filter). |
| `04_tdd` | Use Copilot to satisfy failing `pytest` tests. |
| `05_documentation_refactor` | Document & refactor verbose code with Chat. |

### 🔵 Advanced Track (`advanced_copilot_practice/`)

| Lab | Skill Focus |
|-----|-------------|
| `01_custom_instructions` | Steer Copilot via `.github/copilot-instructions.md`. |
| `02_advanced_prompts` | Generate a Flask API via multi‑line prompts. |
| `03_project_context` | Use your own API (`utils/speech_api.py`) in completions. |
| `04_refactor_debug` | Refactor & debug legacy code with Chat. |
| `05_mcp_agent` | Let a Copilot **agent** fix an issue & open a PR (MCP). |

Each folder’s README walks you through the steps and suggested prompts.

---

## 5  Running the Exercises

* **Inline Suggestions** – Type, accept with `Tab`, cycle variants with `Alt` + `[` / `Alt` + `]`.
* **Copilot Chat** – `Ctrl` + `Shift` + `I` (or chat icon) to open a panel; ask questions.
* **Agent Tasks** – Switch the chat panel to **Agent**; issue commands, e.g.:

  > *Fix issue #1 in `bugfix/buggy_code.py` and commit the changes.*

  Review the plan and confirm each step.

* **Run Tests** – Inside TDD labs, execute `python -m pytest -q`.

---

## 6  Best Practices

1. Write **clear, goal‑oriented prompts**—context matters.
2. **Iterate.** Refine the prompt or ask Chat for alternatives if the first answer isn’t right.
3. **Review & test** every suggestion—you own correctness.
4. **Guard secrets & IP.** Never paste credentials into prompts.
5. **Limit agent scope.** Give explicit tasks and approve cautiously.

---

## 7  Contributing

Spotted an issue or have a new exercise idea?
Open an **Issue** or submit a **Pull Request**—follow the existing `NN_topic/` convention.

---

## 8  License

For educational and internal-training use. See [LICENSE](LICENSE) for details.
