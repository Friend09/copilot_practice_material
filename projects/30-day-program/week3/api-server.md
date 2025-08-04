# Week 3 Project: RESTful API Server

## Project Overview
Build a complete RESTful API server using Flask and GitHub Copilot. This project will teach you to create professional-grade APIs with proper structure, validation, and documentation.

## Features to Implement

### Core Features
1. **CRUD Operations**: Create, Read, Update, Delete for resources
2. **Data Validation**: Input validation and error handling
3. **Authentication**: Basic API key or JWT authentication
4. **Database Integration**: SQLite or PostgreSQL integration
5. **API Documentation**: Auto-generated API docs

### API Endpoints
Choose one domain:

#### Option 1: Task Management API
- `GET /api/tasks` - List all tasks
- `POST /api/tasks` - Create new task
- `GET /api/tasks/{id}` - Get specific task
- `PUT /api/tasks/{id}` - Update task
- `DELETE /api/tasks/{id}` - Delete task

#### Option 2: User Management API
- `GET /api/users` - List users
- `POST /api/users` - Create user
- `GET /api/users/{id}` - Get user profile
- `PUT /api/users/{id}` - Update user
- `DELETE /api/users/{id}` - Delete user

## Project Structure
```
api-server/
├── app.py              # Flask application
├── models.py           # Database models
├── routes/             # API route handlers
│   ├── __init__.py
│   ├── tasks.py
│   └── auth.py
├── utils/              # Utility functions
│   ├── validation.py
│   └── auth.py
├── tests/              # Unit tests
├── requirements.txt
└── README.md
```

## Implementation Guidelines

### Using Copilot for API Development
- "Create a Flask route that handles POST requests for creating new tasks"
- "Implement input validation for user registration with email and password"
- "Generate SQLAlchemy model for a task with title, description, and due date"

### Key Technologies
- Flask for the web framework
- SQLAlchemy for database ORM
- Marshmallow for serialization
- Flask-JWT-Extended for authentication

## Testing Strategy

1. **Unit Tests**: Test individual functions
2. **Integration Tests**: Test API endpoints
3. **Manual Testing**: Use Postman or curl
4. **Error Handling**: Test edge cases and invalid inputs

## Success Criteria

Your API should:
- ✅ Handle all CRUD operations correctly
- ✅ Validate input data and return appropriate errors
- ✅ Include authentication and authorization
- ✅ Have comprehensive error handling
- ✅ Include API documentation
- ✅ Pass all unit and integration tests

