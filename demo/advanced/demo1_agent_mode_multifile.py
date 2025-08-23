"""
GitHub Copilot Advanced Demo 1: Agent Mode & Multi-File Context
============================================================

This demo showcases GitHub Copilot's Agent Mode capabilities:
- Autonomous multi-file code changes
- Context understanding across project structure
- Intelligent code iteration and validation
- Complex refactoring with dependency management

Demo Scenario: E-commerce Product Management System
- Start with a simple product class
- Ask Copilot to add inventory management
- Extend with database integration
- Add API endpoints with validation
- Demonstrate how Copilot understands relationships between files

🎯 Prompt to use with Copilot:
"Create a complete e-commerce product management system with:
1. Product model with inventory tracking
2. Database operations with SQLAlchemy
3. REST API with FastAPI
4. Input validation with Pydantic
5. Error handling and logging
Please create multiple files and ensure they work together."
"""

# Initial Product Class - Copilot will expand this into a full system
class Product:
    """
    Basic product model that Copilot will enhance with:
    - Inventory management
    - Price history tracking
    - Category management
    - Search and filtering capabilities
    """

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name} - ${self.price}"

# Demo Instructions for Presenter:
"""
1. Start with the basic Product class above
2. Open Copilot Chat and ask:
   "Convert this into a complete e-commerce system with multiple files"
3. Let Copilot create:
   - models/ directory with enhanced Product model
   - database/ directory with SQLAlchemy setup
   - api/ directory with FastAPI endpoints
   - schemas/ directory with Pydantic models
   - utils/ directory with helper functions
4. Show how Copilot understands file relationships and imports
5. Demonstrate the autonomous iteration process
"""

# Expected Agent Mode Behaviors to Highlight:
"""
✨ AGENT MODE FEATURES TO DEMONSTRATE:

1. **Multi-File Planning**:
   - Copilot creates a project structure plan
   - Identifies dependencies between files
   - Plans the order of file creation

2. **Autonomous Code Generation**:
   - Creates multiple related files automatically
   - Handles imports and dependencies
   - Ensures consistent naming conventions

3. **Context Awareness**:
   - References other files in the project
   - Maintains consistency across the codebase
   - Understands architectural patterns

4. **Error Detection & Fixing**:
   - Identifies missing imports
   - Fixes circular dependencies
   - Validates code syntax automatically

5. **Iterative Improvement**:
   - Refines code based on context
   - Adds missing functionality
   - Optimizes performance bottlenecks
"""

# Sample follow-up prompts for the demo:
DEMO_PROMPTS = [
    "Add authentication middleware to the API",
    "Implement caching for product queries",
    "Add comprehensive error handling",
    "Create database migration scripts",
    "Add unit tests for all components",
    "Implement search functionality with filtering",
    "Add rate limiting to API endpoints",
    "Create Docker configuration for deployment"
]

if __name__ == "__main__":
    # Simple test to show the starting point
    product = Product("Demo Widget", 29.99)
    print(product)
    print("\n🚀 Ready for Copilot Agent Mode demonstration!")
    print("Use the prompts above to showcase advanced capabilities.")
