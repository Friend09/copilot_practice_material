"""
Demo 2: Security Vulnerability Detection - Intentionally Vulnerable Code
======================================================================

WARNING: This code contains intentional security vulnerabilities for demonstration purposes.
DO NOT use this code in production! It's designed to show how Copilot detects security issues.
"""

import hashlib
import sqlite3
import jwt
import requests
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# ❌ SECURITY ISSUE 1: Hardcoded secrets (Copilot will detect and suggest environment variables)
SECRET_KEY = "hardcoded-secret-key-12345"  # Copilot will flag this
DATABASE_PASSWORD = "admin123"  # Copilot will suggest env vars
API_KEY = "sk-1234567890abcdef"  # Copilot will warn about exposed keys


class UserManager:
    """User management with multiple security vulnerabilities"""

    def __init__(self):
        self.users = {}  # ❌ Using dict instead of proper data structure
        self.db_connection = None  # ❌ No dependency injection

    def createUser(self, name, email, password):  # ❌ Naming convention
        """❌ Missing type hints and proper validation"""
        if not name:  # ❌ Insufficient validation
            return False

        # ❌ SECURITY ISSUE 2: Direct password storage (security issue)
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

    # ❌ SECURITY ISSUE 3: SQL Injection vulnerability
    def get_user_by_id_vulnerable(self, user_id):
        """SQL Injection vulnerability - Copilot will suggest parameterized queries"""
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()

        # Vulnerable: Direct string concatenation
        query = f"SELECT * FROM users WHERE id = {user_id}"  # Copilot will flag this
        cursor.execute(query)

        result = cursor.fetchone()
        conn.close()
        return result

    # ❌ SECURITY ISSUE 4: Method doing too many things and exposing sensitive data
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


# ❌ SECURITY ISSUE 5: Weak password hashing
def hash_password_weak(password):
    """Weak hashing algorithm - Copilot will suggest bcrypt or similar"""
    return hashlib.md5(password.encode()).hexdigest()  # Copilot will flag this


# ❌ SECURITY ISSUE 6: Insecure HTTP requests
def make_api_request_insecure(url, data):
    """Insecure HTTP request - Copilot will suggest SSL verification"""
    response = requests.post(url, data=data, verify=False)  # Copilot will flag this
    return response.json()


# ❌ SECURITY ISSUE 7: JWT without proper validation
def decode_jwt_insecure(token):
    """JWT decoded without verification - Copilot will suggest proper validation"""
    decoded = jwt.decode(token, options={"verify_signature": False})  # Copilot will flag this
    return decoded


# ❌ SECURITY ISSUE 8: Path traversal vulnerability
@app.route('/download/<filename>')
def download_file_vulnerable(filename):
    """Path traversal vulnerability - Copilot will suggest path validation"""
    file_path = f"./uploads/{filename}"  # Copilot will flag potential path traversal
    with open(file_path, 'r') as file:  # No validation - Copilot will warn
        return file.read()


# ❌ SECURITY ISSUE 9: Insufficient input validation
@app.route('/api/user', methods=['POST'])
def create_user_vulnerable():
    """No input validation - Copilot will suggest validation and sanitization"""
    data = request.get_json()
    # No validation - Copilot will suggest validation
    username = data['username']  # Potential KeyError - Copilot will flag
    email = data['email']        # No email validation - Copilot will suggest regex/validator

    return jsonify({"status": "User created", "username": username})


# ❌ SECURITY ISSUE 10: Information disclosure
@app.route('/api/debug')
def debug_info_vulnerable():
    """Information disclosure - Copilot will suggest removing debug info in production"""
    try:
        # Simulated database operation that might fail
        result = 1 / 0  # This will cause an exception
    except Exception as e:
        # Exposes internal details - Copilot will flag this
        return jsonify({
            "error": str(e),
            "traceback": str(e.__traceback__),
            "secret_key": SECRET_KEY  # ❌ Exposing secrets in error response
        })


# ❌ SECURITY ISSUE 11: Payment processing vulnerabilities
def process_payment(amount, card_number, cvv):  # ❌ Missing type hints, logging
    """Security issues and poor error handling"""

    # ❌ No input validation
    if amount <= 0:
        return False

    # ❌ No encryption for sensitive data
    payment_data = {
        'amount': amount,
        'card': card_number,  # ❌ Storing card number
        'cvv': cvv,  # ❌ Storing CVV
        'api_key': API_KEY
    }

    # ❌ No try-catch, no logging, undefined function
    response = make_payment_request(payment_data)  # This function doesn't exist!

    return response['success']  # ❌ Assumes response structure


if __name__ == "__main__":
    print("🚨 WARNING: This code contains intentional security vulnerabilities!")
    print("Use this for Copilot security demo only.")
    print("Run: Ask Copilot to 'Review this code for security vulnerabilities'")
