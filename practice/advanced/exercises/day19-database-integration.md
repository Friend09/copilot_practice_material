# Day 19: Database Integration with Flask

## Objective

Today focuses on integrating databases with Flask applications using SQLAlchemy ORM. You will learn how to define models, perform database operations, handle migrations, and implement database-backed APIs, with GitHub Copilot assisting in generating the necessary code.

## Prerequisites

Install required packages:
```bash
pip install flask flask-sqlalchemy flask-migrate
```

## Exercises

### Exercise 1: Database Setup and Models

Learn to set up a database and define models using SQLAlchemy.

1.  **Database Configuration**: Configure SQLAlchemy with Flask and set up a SQLite database.
    -   *Prompting Hint*: `# Configure SQLAlchemy with Flask for SQLite database`
2.  **User Model**: Create a User model with fields like id, username, email, password, created_at.
    -   *Prompting Hint*: `# Create User model with SQLAlchemy`
3.  **Post Model**: Create a Post model with fields like id, title, content, user_id, created_at.
    -   *Prompting Hint*: `# Create Post model with foreign key to User`
4.  **Model Relationships**: Define relationships between User and Post models (one-to-many).
    -   *Prompting Hint*: `# Define one-to-many relationship between User and Post`
5.  **Database Initialization**: Create functions to initialize and populate the database with sample data.
    -   *Prompting Hint*: `# Create database initialization with sample data`

### Exercise 2: Basic Database Operations

Implement CRUD operations using SQLAlchemy.

1.  **Create Records**: Implement functions to create new users and posts.
    -   *Prompting Hint*: `# Implement functions to create users and posts`
2.  **Read Records**: Implement functions to query users and posts with various filters.
    -   *Prompting Hint*: `# Implement query functions with filters`
3.  **Update Records**: Implement functions to update existing records.
    -   *Prompting Hint*: `# Implement functions to update user and post records`
4.  **Delete Records**: Implement functions to delete records with proper cascade handling.
    -   *Prompting Hint*: `# Implement delete functions with cascade handling`
5.  **Complex Queries**: Implement complex queries with joins, aggregations, and subqueries.
    -   *Prompting Hint*: `# Implement complex queries with joins and aggregations`

### Exercise 3: Database-Backed API

Convert your Flask API to use database storage instead of in-memory data.

1.  **User API with Database**: Implement user CRUD endpoints using database operations.
    -   *Prompting Hint*: `# Implement user CRUD API with database backend`
2.  **Post API with Database**: Implement post CRUD endpoints with user relationships.
    -   *Prompting Hint*: `# Implement post CRUD API with user relationships`
3.  **Pagination with Database**: Implement database-backed pagination for list endpoints.
    -   *Prompting Hint*: `# Implement database pagination for API endpoints`
4.  **Search with Database**: Implement database search functionality using LIKE queries.
    -   *Prompting Hint*: `# Implement database search with LIKE queries`
5.  **Filtering with Database**: Implement advanced filtering options using SQLAlchemy queries.
    -   *Prompting Hint*: `# Implement advanced filtering with SQLAlchemy`

### Exercise 4: Advanced Database Features

Explore advanced database features and optimizations.

1.  **Database Migrations**: Set up Flask-Migrate for database schema management.
    -   *Prompting Hint*: `# Set up Flask-Migrate for database migrations`
2.  **Database Indexing**: Add indexes to improve query performance.
    -   *Prompting Hint*: `# Add database indexes for better performance`
3.  **Database Transactions**: Implement database transactions for data consistency.
    -   *Prompting Hint*: `# Implement database transactions for consistency`
4.  **Connection Pooling**: Configure database connection pooling for better performance.
    -   *Prompting Hint*: `# Configure database connection pooling`
5.  **Database Backup and Restore**: Implement functions for database backup and restore.
    -   *Prompting Hint*: `# Implement database backup and restore functions`

## Challenge Exercise: Blog Platform API

Create a complete blog platform API with database backend that includes:
-   User registration and authentication
-   User profiles with bio and avatar
-   Blog posts with categories and tags
-   Comments on posts
-   Like/unlike functionality
-   User following system
-   Search and filtering capabilities
-   Database migrations and seeding
-   Performance optimizations

*Prompting Hint*: `# Create complete blog platform API with database backend`

## Reflection

-   How did Copilot help you understand SQLAlchemy ORM concepts and syntax?
-   Were there any specific patterns Copilot suggested for database model design?
-   How effective was Copilot in helping you implement complex database queries and relationships?

