# week1_exercise4_models.py

# Data Models for Multi-File Context Exercise

class User:
    """Represents a user in the system."""
    
    def __init__(self, user_id, username, email, first_name, last_name, age):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.is_active = True
        self.created_at = None
        self.last_login = None
    
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def is_adult(self):
        return self.age >= 18


class Product:
    """Represents a product in an e-commerce system."""
    
    def __init__(self, product_id, name, description, price, category, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.stock_quantity = stock_quantity
        self.is_available = True
        self.rating = 0.0
        self.review_count = 0
    
    def is_in_stock(self):
        return self.stock_quantity > 0 and self.is_available
    
    def update_stock(self, quantity_sold):
        if quantity_sold <= self.stock_quantity:
            self.stock_quantity -= quantity_sold
            return True
        return False


class Order:
    """Represents an order in the system."""
    
    def __init__(self, order_id, user_id, order_date):
        self.order_id = order_id
        self.user_id = user_id
        self.order_date = order_date
        self.items = []  # List of OrderItem objects
        self.status = "pending"  # pending, confirmed, shipped, delivered, cancelled
        self.total_amount = 0.0
        self.shipping_address = None
        self.payment_method = None
    
    def add_item(self, product_id, quantity, unit_price):
        item = OrderItem(product_id, quantity, unit_price)
        self.items.append(item)
        self.calculate_total()
    
    def calculate_total(self):
        self.total_amount = sum(item.get_subtotal() for item in self.items)
        return self.total_amount


class OrderItem:
    """Represents an item within an order."""
    
    def __init__(self, product_id, quantity, unit_price):
        self.product_id = product_id
        self.quantity = quantity
        self.unit_price = unit_price
    
    def get_subtotal(self):
        return self.quantity * self.unit_price


class Category:
    """Represents a product category."""
    
    def __init__(self, category_id, name, description, parent_category_id=None):
        self.category_id = category_id
        self.name = name
        self.description = description
        self.parent_category_id = parent_category_id
        self.is_active = True
    
    def is_subcategory(self):
        return self.parent_category_id is not None

