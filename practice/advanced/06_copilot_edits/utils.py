"""
Utility functions for e-commerce application
Practice file for Copilot Edits exercises
"""

def format_price(price):
    """Format price as currency"""
    return f"${price:.2f}"


def calculate_discount(price, discount_percentage):
    """Calculate discounted price"""
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100")

    discount_amount = price * (discount_percentage / 100)
    return price - discount_amount


def validate_email(email):
    """Basic email validation"""
    if '@' not in email:
        return False

    parts = email.split('@')
    if len(parts) != 2:
        return False

    if len(parts[0]) == 0 or len(parts[1]) == 0:
        return False

    if '.' not in parts[1]:
        return False

    return True


def generate_order_number(order_id):
    """Generate a formatted order number"""
    return f"ORD-{order_id:06d}"


def calculate_shipping(weight, distance):
    """Calculate shipping cost based on weight and distance"""
    base_rate = 5.0
    weight_rate = 0.5  # per kg
    distance_rate = 0.1  # per km

    shipping_cost = base_rate + (weight * weight_rate) + (distance * distance_rate)
    return shipping_cost


def calculate_tax(amount, tax_rate=0.1):
    """Calculate tax amount"""
    if tax_rate < 0 or tax_rate > 1:
        raise ValueError("Tax rate must be between 0 and 1")
    return amount * tax_rate


def generate_invoice_data(order):
    """Generate invoice data from order"""
    subtotal = order.calculate_total()
    tax = calculate_tax(subtotal)
    total = subtotal + tax

    return {
        'order_number': generate_order_number(order.id),
        'customer_name': order.customer_name,
        'items': order.items,
        'subtotal': format_price(subtotal),
        'tax': format_price(tax),
        'total': format_price(total)
    }


def search_products(products, query):
    """Search products by name"""
    query = query.lower()
    results = []

    for product in products:
        if query in product.name.lower():
            results.append(product)

    return results


def sort_products_by_price(products, descending=False):
    """Sort products by price"""
    return sorted(products, key=lambda p: p.price, reverse=descending)
