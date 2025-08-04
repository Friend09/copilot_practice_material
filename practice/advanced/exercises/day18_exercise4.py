# day18_exercise4.py

# Exercise 4: Authentication and Security

from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import base64

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-string'  # Change this in production

# Initialize extensions
jwt = JWTManager(app)
CORS(app)

# Sample users database
users_db = [
    {
        "id": 1,
        "username": "admin",
        "password": generate_password_hash("password123"),
        "email": "admin@example.com"
    }
]

# 1. Implement basic HTTP authentication in Flask



# 2. Implement JWT authentication with Flask-JWT-Extended



# 3. Create protected routes requiring JWT authentication



# 4. Implement user registration and login endpoints



# 5. Configure CORS for Flask API (already done above with CORS(app))

# Sample protected data
protected_data = [
    {"id": 1, "title": "Secret Document 1", "content": "This is confidential"},
    {"id": 2, "title": "Secret Document 2", "content": "This is also confidential"}
]

@app.route('/protected-data')
@jwt_required()
def get_protected_data():
    current_user = get_jwt_identity()
    return jsonify({
        "message": f"Hello {current_user}",
        "data": protected_data
    })

if __name__ == '__main__':
    app.run(debug=True, port=5003)

