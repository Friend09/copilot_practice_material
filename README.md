# Copilot Practice Material

This repository contains a collection of practice materials and exercises designed to help you master GitHub Copilot and related AI coding tools. The content is organized into beginner and advanced sections, each with hands-on examples and guided tasks.

## Repository Structure

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
└── _copilot_practice_material.code-workspace
```

## Getting Started

### Prerequisites
- Python 3.8+
- [UV](https://github.com/astral-sh/uv) (for fast Python package management)
- Make (optional, for running tasks)
- OpenAI API key (for LLM-based exercises)

### Setup
1. **Clone the repository:**
   ```bash
   git clone <repo-url>
   cd copilot_practice_material
   ```
2. **Install dependencies (if any):**
   - Using UV:
     ```bash
     uv pip install -r requirements.txt
     ```
   - Or use provided Makefile targets if available:
     ```bash
     make install
     ```
3. **Set your OpenAI API key:**
   - Export your key as an environment variable:
     ```bash
     export OPENAI_API_KEY=your-key-here
     ```

## Contents

### Beginner
- **01_hello_copilot/**: Introduction to Copilot and basic usage.
- **02_function_completion/**: Practice with function completions.
- **03_loops_logic/**: Exercises on loops and logic.
- **04_tdd/**: Test-driven development basics.
- **05_documentation_refactor/**: Refactoring and documentation tasks.

### Advanced
- **01_custom_instructions/**: Customizing Copilot's behavior.
- **02_advanced_prompts/**: Advanced prompt engineering.
- **03_project_context/**: Using project context for better completions.
- **04_refactor_debug/**: Refactoring and debugging legacy code.
- **05_mcp_agent/**: Working with multi-agent Copilot (MCP) features.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for improvements or new exercises.

## License
This project is for educational purposes.
