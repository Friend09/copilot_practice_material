# day18_exercise3.py

# Exercise 3: Request Validation and Data Processing

from flask import Flask, jsonify, request
import math

app = Flask(__name__)

# Sample data
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "age": 30, "department": "Engineering"},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "age": 25, "department": "Marketing"},
    {"id": 3, "name": "Bob Johnson", "email": "bob@example.com", "age": 35, "department": "Sales"},
    {"id": 4, "name": "Alice Brown", "email": "alice@example.com", "age": 28, "department": "Engineering"},
    {"id": 5, "name": "Charlie Wilson", "email": "charlie@example.com", "age": 32, "department": "Sales"},
]

# 1. Validate incoming JSON data in Flask



# 2. Create data serialization functions for user objects



# 3. Implement filtering and pagination for users endpoint



# 4. Add search functionality to users API



# 5. Implement sorting options for users list



if __name__ == '__main__':
    app.run(debug=True, port=5002)

