# Repository Copilot Instructions

## Project Overview

This is a Node.js Express API for task management with the following characteristics:

- **Framework**: Express.js with TypeScript
- **Database**: MongoDB with Mongoose ODM
- **Authentication**: JWT tokens
- **API Documentation**: Swagger/OpenAPI 3.0
- **Testing**: Jest with Supertest for integration tests

## Architecture Patterns

- Follow MVC (Model-View-Controller) pattern
- Use dependency injection for services
- Implement repository pattern for data access
- Use middleware for cross-cutting concerns (auth, logging, validation)
- Separate business logic from HTTP handlers

## Database Guidelines

- Use Mongoose schemas with TypeScript interfaces
- Implement proper indexing for performance
- Use transactions for multi-document operations
- Follow naming conventions: collections in plural, fields in camelCase
- Include timestamps (createdAt, updatedAt) on all documents

## API Conventions

- Base URL: `/api/v1`
- Use plural nouns for resource endpoints (e.g., `/users`, `/tasks`)
- Implement proper HTTP methods: GET, POST, PUT, DELETE
- Use query parameters for filtering and pagination
- Return consistent JSON responses with status, data, and message fields

## Error Handling

- Use custom error classes for different error types
- Implement global error handling middleware
- Return appropriate HTTP status codes
- Log errors with sufficient context for debugging
- Never expose sensitive information in error messages

## Security Implementation

- Use helmet middleware for security headers
- Implement rate limiting
- Validate all inputs with Joi or similar
- Use bcrypt for password hashing
- Implement proper CORS configuration
