"""
Demo 3: Context Understanding - Foundation Code
==============================================

This file provides the architectural foundation that Copilot will understand
and extend consistently across all services in the microservices demo.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from abc import ABC, abstractmethod
from datetime import datetime


@dataclass
class BaseModel:
    """
    Base model that Copilot will recognize and extend consistently
    across all services in the project
    """
    id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

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
        import logging
        return logging.getLogger(self.__class__.__name__)


# Domain Models
@dataclass
class User(BaseModel):
    """
    User model - Copilot will understand this is referenced
    by orders and should maintain referential integrity
    """
    username: str = ""
    email: str = ""
    password_hash: str = ""
    is_active: bool = True


@dataclass
class Product(BaseModel):
    """
    Product model - Copilot will understand inventory relationships
    and pricing strategies when generating related code
    """
    name: str = ""
    description: str = ""
    price: float = 0.0
    category_id: int = 0
    stock_quantity: int = 0


@dataclass
class Order(BaseModel):
    """
    Order model - Copilot will understand this aggregates
    users and products with business logic
    """
    user_id: int = 0
    total_amount: float = 0.0
    status: str = "pending"
    items: List[Dict[str, Any]] = None

    def __post_init__(self):
        if self.items is None:
            self.items = []


if __name__ == "__main__":
    print("🏗️  Foundation models ready for Copilot context understanding demo!")
    print("📋 Available models: User, Product, Order")
    print("🔧 Available patterns: BaseModel, BaseService")
    print("\n🚀 Ask Copilot to create services using these patterns!")
