"""
Demo 1: Agent Mode Starting Point
=================================

This is the simple starting point for the Agent Mode demo.
Copilot will expand this into a complete e-commerce system.
"""

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


if __name__ == "__main__":
    # Simple test to show the starting point
    product = Product("Demo Widget", 29.99)
    print(product)
    print("\n🚀 Ready for Copilot Agent Mode demonstration!")
