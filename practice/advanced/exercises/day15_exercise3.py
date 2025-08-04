# day15_exercise3.py

# Exercise 3: Context Managers

import time
import contextlib
from typing import Optional

# 1. Create a context manager for file handling



# 2. Create a context manager to time a code block



# 3. Create a context manager for database connection
# Simulate database connection
class MockDatabase:
    def __init__(self):
        self.connected = False
    
    def connect(self):
        print("Connecting to database...")
        self.connected = True
    
    def close(self):
        print("Closing database connection...")
        self.connected = False
    
    def query(self, sql):
        if not self.connected:
            raise Exception("Not connected to database")
        return f"Result for: {sql}"



# 4. Create a context manager to suppress exceptions



# 5. Use contextlib.contextmanager to create a context manager



# Challenge: Data Stream Processor
# Combine decorators, generators, and context managers

# Test the context managers
if __name__ == "__main__":
    # Test file context manager
    print("Testing file context manager:")
    with FileManager('test_file.txt', 'w') as f:
        f.write("Hello, World!")
    
    # Test timer context manager
    print("\nTesting timer context manager:")
    with Timer():
        time.sleep(1)
    
    # Test database context manager
    print("\nTesting database context manager:")
    with DatabaseConnection() as db:
        result = db.query("SELECT * FROM users")
        print(result)
    
    # Test exception suppressor
    print("\nTesting exception suppressor:")
    with SuppressExceptions(ValueError):
        raise ValueError("This error will be suppressed")
    print("Code continues after suppressed exception")
    
    # Test contextlib context manager
    print("\nTesting contextlib context manager:")
    with temporary_setting("debug", True):
        print("Debug mode is on")

