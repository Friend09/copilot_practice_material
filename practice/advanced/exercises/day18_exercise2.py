# day18_exercise2.py

# Exercise 2: CRUD Operations

from flask import Flask, jsonify, request

app = Flask(__name__)

# 1. Create in-memory data store for users
users = [
    {"id": 1, "name": "John Doe", "email": "john@example.com", "age": 30},
    {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "age": 25},
    {"id": 3, "name": "Bob Johnson", "email": "bob@example.com", "age": 35}
]

# Helper function to get next ID
def get_next_id():
    return max([user['id'] for user in users], default=0) + 1

# 2. Implement GET endpoint to retrieve all users



# 3. Implement GET endpoint for single user by ID



# 4. Implement POST endpoint to create new user



# 5. Implement PUT endpoint to update user



# 6. Implement DELETE endpoint to remove user



if __name__ == '__main__':
    app.run(debug=True, port=5001)

