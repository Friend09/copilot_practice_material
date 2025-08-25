"""
Demo 3: Service Interfaces
=========================

Service interfaces that define contracts for the microservices.
Copilot will understand these patterns and implement them consistently.
"""

from typing import Dict, List, Optional, Any
from abc import ABC, abstractmethod
from base_models import User, Product, Order


class UserServiceInterface(ABC):
    """
    Copilot will understand this defines the contract
    for user-related operations across the system
    """

    @abstractmethod
    def authenticate_user(self, username: str, password: str) -> Optional[User]:
        """Authenticate user and return user object if successful"""
        pass

    @abstractmethod
    def create_user(self, user_data: Dict[str, Any]) -> User:
        """Create a new user with validation"""
        pass

    @abstractmethod
    def get_user_orders(self, user_id: int) -> List[Order]:
        """Get all orders for a specific user - requires cross-service communication"""
        pass

    @abstractmethod
    def update_user_profile(self, user_id: int, profile_data: Dict[str, Any]) -> Optional[User]:
        """Update user profile information"""
        pass


class ProductServiceInterface(ABC):
    """
    Copilot will implement inventory management and
    understand the relationship with orders
    """

    @abstractmethod
    def check_availability(self, product_id: int, quantity: int) -> bool:
        """Check if requested quantity is available"""
        pass

    @abstractmethod
    def reserve_items(self, items: List[Dict[str, Any]]) -> bool:
        """Reserve items for order processing"""
        pass

    @abstractmethod
    def update_inventory(self, product_id: int, quantity_change: int) -> bool:
        """Update inventory levels (positive or negative change)"""
        pass

    @abstractmethod
    def get_products_by_category(self, category_id: int) -> List[Product]:
        """Get all products in a specific category"""
        pass

    @abstractmethod
    def search_products(self, query: str, filters: Dict[str, Any]) -> List[Product]:
        """Search products with filtering capabilities"""
        pass


class OrderServiceInterface(ABC):
    """
    Copilot will understand this orchestrates user and product services
    """

    @abstractmethod
    def create_order(self, user_id: int, items: List[Dict[str, Any]]) -> Order:
        """Create order with validation and inventory checking"""
        pass

    @abstractmethod
    def process_payment(self, order_id: int, payment_info: Dict[str, Any]) -> bool:
        """Process payment for an order"""
        pass

    @abstractmethod
    def fulfill_order(self, order_id: int) -> bool:
        """Mark order as fulfilled and update inventory"""
        pass

    @abstractmethod
    def cancel_order(self, order_id: int, reason: str) -> bool:
        """Cancel order and return inventory to stock"""
        pass

    @abstractmethod
    def get_order_status(self, order_id: int) -> Dict[str, Any]:
        """Get detailed order status and tracking information"""
        pass


# Configuration for expected project structure
EXPECTED_PROJECT_STRUCTURE = """
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


if __name__ == "__main__":
    print("🎯 Service interfaces ready for implementation!")
    print("📝 Available interfaces:")
    print("   - UserServiceInterface")
    print("   - ProductServiceInterface")
    print("   - OrderServiceInterface")
    print("\n🚀 Ask Copilot to implement these interfaces following the BaseService pattern!")
    print("\nExpected project structure:")
    print(EXPECTED_PROJECT_STRUCTURE)
