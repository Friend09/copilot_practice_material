"""
Demo 5: Code Review - Problematic Code for Review
================================================

This code contains various quality and security issues that demonstrate
how Copilot assists in comprehensive code reviews.

WARNING: This code is intentionally problematic for demonstration purposes!
"""

import hashlib
import sqlite3
from datetime import datetime
from typing import Dict, List, Optional


# ❌ Multiple code quality issues for review demonstration
class UserManager:
    """User management with various code quality issues"""

    def __init__(self):
        self.users = {}  # ❌ Using dict instead of proper data structure
        self.db_connection = None  # ❌ No dependency injection

    def createUser(self, name, email, password):  # ❌ Naming convention, no type hints
        """❌ Missing type hints and proper validation"""
        if not name:  # ❌ Insufficient validation
            return False

        # ❌ Direct password storage (security issue)
        user_id = len(self.users) + 1  # ❌ Poor ID generation
        self.users[user_id] = {
            'name': name,
            'email': email,
            'password': password,  # ❌ Plain text password
            'created': datetime.now()
        }

        return user_id

    def get_user(self, user_id):  # ❌ Inconsistent naming, no error handling
        return self.users[user_id]  # ❌ KeyError potential

    def deleteUser(self, user_id):  # ❌ No soft delete, no cascading
        del self.users[user_id]  # ❌ Hard delete, no backup
        return True

    # ❌ Method doing too many things
    def authenticateAndGetProfile(self, email, password):
        for user_id, user in self.users.items():
            if user['email'] == email and user['password'] == password:  # ❌ Plain text comparison
                # ❌ Returning sensitive data
                return {
                    'id': user_id,
                    'name': user['name'],
                    'email': user['email'],
                    'password': user['password']  # ❌ Exposing password
                }
        return None


# ❌ Performance issues and poor patterns
def find_users_by_criteria(users, criteria):  # ❌ No type hints
    """❌ Inefficient algorithm and no optimization"""
    results = []

    # ❌ O(n²) complexity when could be O(n)
    for user_id, user in users.items():
        match = True
        for key, value in criteria.items():
            if key not in user or user[key] != value:
                match = False
                break
        if match:
            results.append(user)

    return results


# ❌ SQL injection and database issues
class DatabaseManager:
    def __init__(self):
        self.connection = None

    def get_user_by_email(self, email):
        """❌ SQL injection vulnerability"""
        cursor = self.connection.cursor()
        # Vulnerable query construction
        query = f"SELECT * FROM users WHERE email = '{email}'"  # ❌ SQL injection risk
        cursor.execute(query)
        return cursor.fetchone()

    def update_user_balance(self, user_id, amount):
        """❌ No transaction handling for financial operations"""
        cursor = self.connection.cursor()
        query = f"UPDATE users SET balance = balance + {amount} WHERE id = {user_id}"
        cursor.execute(query)  # ❌ No commit, no error handling


# ❌ Payment processing with security issues
def process_payment(amount, card_number, cvv):  # ❌ Missing type hints, logging
    """❌ Security issues and poor error handling"""

    # ❌ No input validation
    if amount <= 0:
        return False

    # ❌ Hardcoded payment gateway details
    api_key = "sk_test_12345"  # ❌ Hardcoded secret

    # ❌ No encryption for sensitive data
    payment_data = {
        'amount': amount,
        'card': card_number,  # ❌ Storing card number
        'cvv': cvv,  # ❌ Storing CVV
        'api_key': api_key
    }

    # ❌ No try-catch, no logging
    # response = make_payment_request(payment_data)  # ❌ Undefined function

    return True  # ❌ Always returns success


# ❌ Error handling and logging issues
def risky_operation(data):
    """❌ Poor error handling demonstrates issues for review"""
    try:
        result = data['required_field']  # ❌ No validation that field exists
        processed = result.upper()  # ❌ Assumes string type
        return processed
    except:  # ❌ Bare except clause
        return None  # ❌ Silent failure, no logging


# ❌ Configuration and environment issues
class AppConfig:
    """❌ Configuration management issues"""
    DATABASE_URL = "postgresql://admin:password123@localhost/myapp"  # ❌ Hardcoded credentials
    SECRET_KEY = "super-secret-key-12345"  # ❌ Hardcoded secret
    DEBUG = True  # ❌ Always in debug mode

    def get_api_key(self):
        return "sk-1234567890abcdef"  # ❌ Hardcoded API key


if __name__ == "__main__":
    print("📋 Code ready for comprehensive review demonstration!")
    print("🔍 Issues to be identified by Copilot:")
    print("   - Security vulnerabilities (SQL injection, hardcoded secrets)")
    print("   - Performance bottlenecks (O(n²) algorithms)")
    print("   - Code quality issues (naming, type hints, error handling)")
    print("   - Architecture problems (tight coupling, SRP violations)")
    print("\n🚀 Ask Copilot: 'Review this code for quality issues and suggest improvements'")
