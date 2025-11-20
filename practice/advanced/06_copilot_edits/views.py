"""
API endpoint handlers for e-commerce application
Practice file for Copilot Edits exercises
"""

from models import Product, Order, Customer

# In-memory storage (replace with database in production)
products = {}
orders = {}
customers = {}

def get_products():
    """Get all products"""
    return list(products.values())


def get_product(product_id):
    """Get a specific product by ID"""
    if product_id not in products:
        return None
    return products[product_id]


def create_product(data):
    """Create a new product"""
    product_id = len(products) + 1
    product = Product(
        id=product_id,
        name=data['name'],
        price=data['price'],
        stock=data['stock']
    )
    products[product_id] = product
    return product


def update_product(product_id, data):
    """Update an existing product"""
    if product_id not in products:
        return None

    product = products[product_id]
    if 'name' in data:
        product.name = data['name']
    if 'price' in data:
        product.price = data['price']
    if 'stock' in data:
        product.stock = data['stock']

    return product


def delete_product(product_id):
    """Delete a product"""
    if product_id not in products:
        return False
    del products[product_id]
    return True


def create_order(data):
    """Create a new order"""
    order_id = len(orders) + 1
    order = Order(
        id=order_id,
        customer_name=data['customer_name'],
        items=[]
    )

    for item in data['items']:
        product = get_product(item['product_id'])
        if product:
            order.add_item(product, item['quantity'])

    orders[order_id] = order
    return order


def get_order(order_id):
    """Get a specific order by ID"""
    if order_id not in orders:
        return None
    return orders[order_id]


def get_customer_orders(customer_id):
    """Get all orders for a customer"""
    if customer_id not in customers:
        return []

    customer = customers[customer_id]
    return customer.get_order_history()


def complete_order(order_id):
    """Mark an order as completed"""
    if order_id not in orders:
        return False

    order = orders[order_id]
    return order.complete_order()
