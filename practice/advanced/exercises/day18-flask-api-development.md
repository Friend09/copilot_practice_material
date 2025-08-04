# Day 18: Flask API Development

## Objective

Today focuses on building RESTful APIs using Flask. You will learn how to create endpoints, handle different HTTP methods, work with JSON data, implement authentication, and structure a professional API, with GitHub Copilot assisting in generating the necessary code.

## Prerequisites

Install Flask and related packages:
```bash
pip install flask flask-cors flask-jwt-extended
```

## Exercises

### Exercise 1: Basic Flask API Setup

Learn the fundamentals of creating a Flask API.

1.  **Basic Flask App**: Create a simple Flask application with a "Hello World" endpoint.
    -   *Prompting Hint*: `# Create basic Flask app with hello world endpoint`
2.  **Multiple Routes**: Add multiple routes with different HTTP methods (GET, POST, PUT, DELETE).
    -   *Prompting Hint*: `# Add multiple routes with different HTTP methods`
3.  **Route Parameters**: Create routes that accept URL parameters and query parameters.
    -   *Prompting Hint*: `# Create routes with URL and query parameters`
4.  **JSON Responses**: Return JSON responses from your endpoints.
    -   *Prompting Hint*: `# Return JSON responses from Flask endpoints`
5.  **Error Handling**: Implement custom error handlers for common HTTP errors.
    -   *Prompting Hint*: `# Implement custom error handlers in Flask`

### Exercise 2: CRUD Operations

Implement Create, Read, Update, Delete operations for a resource.

1.  **In-Memory Data Store**: Create an in-memory list to store data (e.g., users, products).
    -   *Prompting Hint*: `# Create in-memory data store for users`
2.  **GET All Items**: Implement endpoint to retrieve all items.
    -   *Prompting Hint*: `# Implement GET endpoint to retrieve all users`
3.  **GET Single Item**: Implement endpoint to retrieve a single item by ID.
    -   *Prompting Hint*: `# Implement GET endpoint for single user by ID`
4.  **POST Create Item**: Implement endpoint to create a new item.
    -   *Prompting Hint*: `# Implement POST endpoint to create new user`
5.  **PUT Update Item**: Implement endpoint to update an existing item.
    -   *Prompting Hint*: `# Implement PUT endpoint to update user`
6.  **DELETE Item**: Implement endpoint to delete an item.
    -   *Prompting Hint*: `# Implement DELETE endpoint to remove user`

### Exercise 3: Request Validation and Data Processing

Handle and validate incoming data properly.

1.  **Request Validation**: Validate incoming JSON data and return appropriate error messages.
    -   *Prompting Hint*: `# Validate incoming JSON data in Flask`
2.  **Data Serialization**: Create functions to serialize/deserialize data objects.
    -   *Prompting Hint*: `# Create data serialization functions for user objects`
3.  **Filtering and Pagination**: Implement filtering and pagination for list endpoints.
    -   *Prompting Hint*: `# Implement filtering and pagination for users endpoint`
4.  **Search Functionality**: Add search capability to your API.
    -   *Prompting Hint*: `# Add search functionality to users API`
5.  **Sorting**: Implement sorting options for list endpoints.
    -   *Prompting Hint*: `# Implement sorting options for users list`

### Exercise 4: Authentication and Security

Implement authentication and security measures.

1.  **Basic Authentication**: Implement basic HTTP authentication.
    -   *Prompting Hint*: `# Implement basic HTTP authentication in Flask`
2.  **JWT Authentication**: Implement JWT-based authentication using Flask-JWT-Extended.
    -   *Prompting Hint*: `# Implement JWT authentication with Flask-JWT-Extended`
3.  **Protected Routes**: Create routes that require authentication.
    -   *Prompting Hint*: `# Create protected routes requiring JWT authentication`
4.  **User Registration and Login**: Implement user registration and login endpoints.
    -   *Prompting Hint*: `# Implement user registration and login endpoints`
5.  **CORS Configuration**: Configure Cross-Origin Resource Sharing (CORS).
    -   *Prompting Hint*: `# Configure CORS for Flask API`

## Challenge Exercise: Complete Task Management API

Create a comprehensive task management API that includes:
-   User registration and authentication
-   CRUD operations for tasks
-   Task categories and priorities
-   Task assignment to users
-   Filtering tasks by status, category, assignee
-   Pagination and sorting
-   Proper error handling and validation
-   API documentation

*Prompting Hint*: `# Create comprehensive task management API with authentication and CRUD`

## Reflection

-   How did Copilot help you understand Flask routing and request handling?
-   Were there any specific patterns Copilot suggested for API structure and organization?
-   How effective was Copilot in helping you implement authentication and security features?

