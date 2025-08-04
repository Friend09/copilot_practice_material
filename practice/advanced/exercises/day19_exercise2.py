# day19_exercise2.py

# Exercise 2: Basic Database Operations

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Use the same models from exercise 1
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog_operations.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Copy the User and Post models from exercise 1
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy=True, cascade='all, delete-orphan')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

# 1. Implement functions to create users and posts



# 2. Implement query functions with filters



# 3. Implement functions to update user and post records



# 4. Implement delete functions with cascade handling



# 5. Implement complex queries with joins and aggregations



if __name__ == '__main__':
    with app.app_context():
        # Create tables
        db.create_all()
        
        # Test create operations
        print("Testing Create Operations:")
        user1 = create_user("alice", "alice@example.com", "password123")
        user2 = create_user("bob", "bob@example.com", "password456")
        
        post1 = create_post("First Post", "This is my first post!", user1.id)
        post2 = create_post("Second Post", "This is another post!", user1.id)
        post3 = create_post("Bob's Post", "Hello from Bob!", user2.id)
        
        # Test read operations
        print("\nTesting Read Operations:")
        all_users = get_all_users()
        print(f"All users: {[u.username for u in all_users]}")
        
        alice = get_user_by_username("alice")
        print(f"User by username: {alice.username if alice else 'Not found'}")
        
        alice_posts = get_posts_by_user(user1.id)
        print(f"Alice's posts: {[p.title for p in alice_posts]}")
        
        recent_posts = get_recent_posts(2)
        print(f"Recent posts: {[p.title for p in recent_posts]}")
        
        # Test update operations
        print("\nTesting Update Operations:")
        update_user_email(user1.id, "alice.new@example.com")
        updated_user = get_user_by_id(user1.id)
        print(f"Updated email: {updated_user.email}")
        
        update_post_content(post1.id, "This is my updated first post!")
        updated_post = get_post_by_id(post1.id)
        print(f"Updated content: {updated_post.content}")
        
        # Test complex queries
        print("\nTesting Complex Queries:")
        stats = get_user_post_stats()
        for stat in stats:
            print(f"User {stat[0]} has {stat[1]} posts")
        
        # Test delete operations (commented out to preserve data)
        # print("\nTesting Delete Operations:")
        # delete_post(post3.id)
        # delete_user(user2.id)  # This should also delete Bob's posts due to cascade

