"""
Intro Demo: Basic Calculator for Chat Demos (Session A)
=======================================================

A simple calculator class with basic arithmetic operations.
This code works but is intentionally basic -- no error handling,
no input validation, no history tracking.

Use Copilot Chat to:
    1. Explain this code
    2. Add error handling to the divide method
    3. Generate unit tests
    4. Add a calculation history feature
"""


class Calculator:
    """A basic calculator that performs arithmetic operations.

    Supports addition, subtraction, multiplication, division,
    exponentiation, and modulo. Does not include error handling
    or history tracking -- those will be added during the demo.
    """

    def add(self, a, b):
        """Add two numbers and return the result."""
        return a + b

    def subtract(self, a, b):
        """Subtract b from a and return the result."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers and return the result."""
        return a * b

    def divide(self, a, b):
        """Divide a by b and return the result."""
        return a / b

    def power(self, base, exponent):
        """Raise base to the power of exponent."""
        return base ** exponent

    def modulo(self, a, b):
        """Return the remainder of a divided by b."""
        return a % b


if __name__ == "__main__":
    calc = Calculator()

    print("Basic Calculator Demo")
    print("=" * 30)
    print(f"5 + 3   = {calc.add(5, 3)}")
    print(f"10 - 4  = {calc.subtract(10, 4)}")
    print(f"6 * 7   = {calc.multiply(6, 7)}")
    print(f"15 / 4  = {calc.divide(15, 4)}")
    print(f"2 ^ 8   = {calc.power(2, 8)}")
    print(f"17 % 5  = {calc.modulo(17, 5)}")
    print()
    print("Try in Copilot Chat:")
    print('  "Explain this code"')
    print('  "Add error handling to the divide method"')
    print('  "Generate unit tests for this Calculator class"')
    print('  "Add a calculation history feature"')
