"""
GitHub Copilot Advanced Demo 3: Context Understanding & Workspace Awareness
==========================================================================

This demo showcases GitHub Copilot's advanced context understanding:
- Multi-file project comprehension
- Workspace-wide code analysis
- Intelligent suggestions based on project structure
- Understanding of architectural patterns and conventions
- Cross-file dependency management

Demo Scenario: Microservices Architecture
- Demonstrate how Copilot understands service boundaries
- Show context-aware code generation across multiple services
- Highlight intelligent dependency management

🎯 This demo shows how Copilot "thinks" about your entire codebase!
"""

import os
import sys
from pathlib import Path
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from abc import ABC, abstractmethod

# Project structure that Copilot will understand and work with
"""
Expected Project Structure (Copilot will maintain this context):

microservices_demo/
├── services/
│   ├── user_service/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   └── database.py
│   ├── product_service/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── routes.py
│   │   └── inventory.py
│   └── order_service/
│       ├── __init__.py
│       ├── models.py
│       ├── routes.py
│       └── payment.py
├── shared/
│   ├── __init__.py
│   ├── auth.py
│   ├── database.py
│   └── utils.py
├── config/
│   ├── __init__.py
│   ├── settings.py
│   └── logging.py
└── tests/
    ├── test_user_service.py
    ├── test_product_service.py
    └── test_order_service.py
"""

# Base classes that Copilot will understand across the project
@dataclass
class BaseModel:
    """
    Base model that Copilot will recognize and extend consistently
    across all services in the project
    """
    id: Optional[int] = None
    created_at: Optional[str] = None
    updated_at: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        """Convert model to dictionary - Copilot will use this pattern"""
        return {k: v for k, v in self.__dict__.items() if v is not None}

class BaseService(ABC):
    """
    Abstract service class that Copilot will understand as the
    architectural pattern for all microservices
    """

    def __init__(self, db_connection: Any):
        self.db = db_connection
        self.logger = self._setup_logging()

    @abstractmethod
    def create(self, data: Dict[str, Any]) -> BaseModel:
        """Copilot will implement this in each service"""
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[BaseModel]:
        """Copilot will implement this in each service"""
        pass

    @abstractmethod
    def update(self, id: int, data: Dict[str, Any]) -> Optional[BaseModel]:
        """Copilot will implement this in each service"""
        pass

    @abstractmethod
    def delete(self, id: int) -> bool:
        """Copilot will implement this in each service"""
        pass

    def _setup_logging(self):
        """Copilot will maintain consistent logging across services"""
        # Implementation will be consistent across all services
        pass

# Domain models that Copilot will understand relationships between
@dataclass
class User(BaseModel):
    """
    User model - Copilot will understand this is referenced
    by orders and should maintain referential integrity
    """
    username: str
    email: str
    password_hash: str
    is_active: bool = True

@dataclass
class Product(BaseModel):
    """
    Product model - Copilot will understand inventory relationships
    and pricing strategies when generating related code
    """
    name: str
    description: str
    price: float
    category_id: int
    stock_quantity: int = 0

@dataclass
class Order(BaseModel):
    """
    Order model - Copilot will understand this aggregates
    users and products with business logic
    """
    user_id: int
    total_amount: float
    status: str = "pending"
    items: List[Dict[str, Any]] = None

# Service interfaces that Copilot will implement consistently
class UserServiceInterface:
    """
    Copilot will understand this defines the contract
    for user-related operations across the system
    """

    def authenticate_user(self, username: str, password: str) -> Optional[User]:
        # Copilot will implement authentication logic
        pass

    def create_user(self, user_data: Dict[str, Any]) -> User:
        # Copilot will implement user creation with validation
        pass

    def get_user_orders(self, user_id: int) -> List[Order]:
        # Copilot will understand cross-service communication needed
        pass

class ProductServiceInterface:
    """
    Copilot will implement inventory management and
    understand the relationship with orders
    """

    def check_availability(self, product_id: int, quantity: int) -> bool:
        # Copilot will implement stock checking logic
        pass

    def reserve_items(self, items: List[Dict[str, Any]]) -> bool:
        # Copilot will implement reservation logic
        pass

    def update_inventory(self, product_id: int, quantity_change: int):
        # Copilot will implement inventory updates
        pass

class OrderServiceInterface:
    """
    Copilot will understand this orchestrates user and product services
    """

    def create_order(self, user_id: int, items: List[Dict[str, Any]]) -> Order:
        # Copilot will implement order creation with service coordination
        pass

    def process_payment(self, order_id: int, payment_info: Dict[str, Any]) -> bool:
        # Copilot will implement payment processing
        pass

    def fulfill_order(self, order_id: int) -> bool:
        # Copilot will implement fulfillment logic
        pass

# Configuration that Copilot will understand and maintain
class ServiceConfig:
    """
    Configuration class that Copilot will understand
    should be consistent across all services
    """

    def __init__(self):
        # Copilot will understand environment-based configuration
        self.database_url = os.getenv('DATABASE_URL', 'sqlite:///default.db')
        self.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key')
        self.debug = os.getenv('DEBUG', 'False').lower() == 'true'
        self.log_level = os.getenv('LOG_LEVEL', 'INFO')

    def get_service_urls(self) -> Dict[str, str]:
        """Copilot will understand inter-service communication"""
        return {
            'user_service': os.getenv('USER_SERVICE_URL', 'http://localhost:5001'),
            'product_service': os.getenv('PRODUCT_SERVICE_URL', 'http://localhost:5002'),
            'order_service': os.getenv('ORDER_SERVICE_URL', 'http://localhost:5003')
        }

# ============================================================================
# CONTEXT UNDERSTANDING DEMO INSTRUCTIONS
# ============================================================================

"""
🎯 DEMO INSTRUCTIONS FOR PRESENTER:

1. **Setup the Demo**:
   - Show this file as the "architectural foundation"
   - Explain that Copilot will understand these patterns

2. **Demonstrate Context Awareness**:

   a) **Ask Copilot to create UserService**:
      "Create a UserService class that implements UserServiceInterface
       following the BaseService pattern defined in this file"

   b) **Ask for ProductService**:
      "Create ProductService with inventory management, following
       the same patterns as UserService"

   c) **Ask for OrderService**:
      "Create OrderService that coordinates UserService and ProductService
       for order processing"

3. **Show Cross-File Understanding**:
   - Copilot will reference the base classes correctly
   - It will maintain consistent patterns across services
   - It will understand service dependencies

4. **Demonstrate Architectural Awareness**:
   - Ask: "Add caching to all services"
   - Ask: "Add rate limiting middleware"
   - Ask: "Implement database migrations"
   - Ask: "Add comprehensive logging"

5. **Show Intelligent Suggestions**:
   - Start typing a new method in one service
   - Copilot will suggest consistent implementations
   - It will understand business logic relationships

6. **Test Cross-Service Logic**:
   - Ask: "Implement order creation that checks inventory"
   - Copilot will understand the workflow across services
   - It will handle error cases and rollbacks

Expected Copilot Behaviors:
✅ Maintains consistent code style across files
✅ Understands service boundaries and responsibilities
✅ Implements proper error handling patterns
✅ Suggests appropriate imports and dependencies
✅ Maintains architectural consistency
✅ Understands business logic relationships
✅ Suggests testing strategies that make sense for the architecture
"""

# Advanced context demonstration prompts
CONTEXT_DEMO_PROMPTS = [
    "Create a complete UserService implementation with database operations",
    "Add authentication middleware that works across all services",
    "Implement order workflow that coordinates all three services",
    "Add comprehensive error handling with proper rollback logic",
    "Create API documentation that reflects the service architecture",
    "Implement health checks for the microservices architecture",
    "Add distributed tracing across service calls",
    "Create database schemas that maintain referential integrity",
    "Implement event-driven communication between services",
    "Add monitoring and metrics collection for all services"
]

# Context understanding capabilities to highlight
CONTEXT_CAPABILITIES = {
    "architectural_patterns": "Understands and maintains design patterns",
    "service_boundaries": "Respects microservice separation of concerns",
    "data_relationships": "Maintains referential integrity across services",
    "business_logic": "Understands domain-specific workflows",
    "error_handling": "Implements consistent error handling strategies",
    "configuration": "Maintains environment-aware configuration",
    "testing_strategy": "Suggests appropriate testing at each layer",
    "deployment": "Understands containerization and orchestration needs"
}

if __name__ == "__main__":
    print("🧠 GitHub Copilot Context Understanding Demo")
    print("===========================================")
    print("This file establishes architectural patterns that Copilot will understand.")
    print("\n🎯 Try asking Copilot to:")
    for prompt in CONTEXT_DEMO_PROMPTS[:3]:
        print(f"   • {prompt}")

    print(f"\n📁 Expected project structure:")
    print("   Copilot will maintain consistency across multiple files and services!")
