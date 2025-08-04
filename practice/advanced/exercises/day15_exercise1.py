# day15_exercise1.py

# Exercise 1: Decorators

import time
import functools

# 1. Create a decorator to time function execution



# 2. Create a decorator to log function calls



# 3. Create an authentication decorator
# Simulate a global user state
current_user = None  # Set to "admin" to simulate authenticated user



# 4. Create a retry decorator that takes max_retries as argument



# 5. Create a class decorator to add a method



# Test the decorators
if __name__ == "__main__":
    # Test timer decorator
    @timer
    def slow_function():
        time.sleep(1)
        return "Done"
    
    # Test logger decorator
    @logger
    def add_numbers(a, b):
        return a + b
    
    # Test authentication decorator
    @requires_auth
    def sensitive_operation():
        return "Secret data"
    
    # Test retry decorator
    @retry(max_retries=3)
    def unreliable_function():
        import random
        if random.random() < 0.7:  # 70% chance of failure
            raise Exception("Random failure")
        return "Success"
    
    # Test class decorator
    @add_method
    class MyClass:
        pass

