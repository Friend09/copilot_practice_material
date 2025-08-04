# day19_exercise1.py

# Exercise 1: Database Setup and Models

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# 1. Configure SQLAlchemy with Flask for SQLite database



# 2. Create User model with SQLAlchemy



# 3. Create Post model with foreign key to User



# 4. Define one-to-many relationship between User and Post
# (This should be added to the User model above)

# 5. Create database initialization with sample data



if __name__ == '__main__':
    # Initialize the database and add sample data
    with app.app_context():
        init_db()
    
    print("Database initialized with sample data!")
    
    # Test the models
    with app.app_context():
        # Query all users
        users = User.query.all()
        print(f"\nUsers in database: {len(users)}")
        for user in users:
            print(f"- {user.username} ({user.email})")
            print(f"  Posts: {len(user.posts)}")
        
        # Query all posts
        posts = Post.query.all()
        print(f"\nPosts in database: {len(posts)}")
        for post in posts:
            print(f"- {post.title} by {post.author.username}")
    
    app.run(debug=True, port=5004)

