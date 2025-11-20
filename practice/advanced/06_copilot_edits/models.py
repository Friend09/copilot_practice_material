"""
E-commerce data models
Practice file for Copilot Edits exercises
"""

class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def is_available(self):
        return self.stock > 0

    def update_stock(self, quantity):
        if self.stock + quantity < 0:
            raise ValueError("Insufficient stock")
        self.stock += quantity

    def get_price_with_tax(self, tax_rate=0.1):
        return self.price * (1 + tax_rate)


class Order:
    def __init__(self, id, customer_name, items):
        self.id = id
        self.customer_name = customer_name
        self.items = items
        self.status = "pending"

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['price'] * item['quantity']
        return total

    def add_item(self, product, quantity):
        if not product.is_available():
            raise ValueError("Product not available")

        self.items.append({
            'product_id': product.id,
            'name': product.name,
            'price': product.price,
            'quantity': quantity
        })
        product.update_stock(-quantity)

    def complete_order(self):
        self.status = "completed"
        return True


class Customer:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)

    def get_order_history(self):
        return [order for order in self.orders]

    def get_total_spent(self):
        total = 0
        for order in self.orders:
            if order.status == "completed":
                total += order.calculate_total()
        return total
