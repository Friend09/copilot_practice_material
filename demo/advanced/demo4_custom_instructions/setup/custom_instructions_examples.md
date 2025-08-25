# Demo 4: Custom Instructions Examples

## Web Scraping Domain Custom Instructions

```text
# GitHub Copilot Custom Instructions: Web Scraping Best Practices

## Code Style Guidelines:
1. Use type hints for all function parameters and return values
2. Include docstrings with parameter descriptions and examples
3. Use dataclasses for structured data models
4. Include comprehensive logging for all scraping operations
5. Add rate limiting and retry mechanisms for all web requests
6. Follow the Repository pattern for data persistence
7. Use Pydantic models for data validation
8. Include robust error handling with custom exceptions

## Web Scraping Best Practices:
1. Always respect robots.txt and rate limits
2. Use random delays between requests to avoid detection
3. Implement proper session management and cookie handling
4. Include User-Agent rotation for different requests
5. Add proxy support for large-scale operations
6. Use headless browsers for JavaScript-heavy sites
7. Implement data validation and sanitization
8. Cache responses to minimize redundant requests

## Architecture Patterns:
1. Separate scraping logic from data processing
2. Use dependency injection for external services
3. Implement the Strategy pattern for different ticket sites
4. Use Observer pattern for real-time notifications
5. Include circuit breakers for unreliable websites
6. Use queue systems for batch processing

Ask Copilot to follow these instructions when generating code!
```

## E-commerce Domain Custom Instructions

```text
# GitHub Copilot Custom Instructions: E-commerce Development

## API Development Standards:
- Use FastAPI with async/await patterns
- Implement comprehensive input validation with Pydantic
- Include rate limiting and authentication middleware
- Add OpenAPI documentation with examples
- Use SQLAlchemy with proper relationship mapping
- Implement caching strategies for performance

## Business Logic Requirements:
- All monetary calculations use Decimal type for precision
- Include audit trails for all financial transactions
- Implement proper inventory tracking and reservations
- Add comprehensive logging for business operations
- Include rollback mechanisms for failed transactions
- Validate business rules before database operations

## Security Standards:
- Never store plain text passwords or payment information
- Use environment variables for all secrets
- Implement proper session management
- Add SQL injection prevention measures
- Include comprehensive input sanitization
- Log security events for monitoring
```

## Team Development Standards

```text
# GitHub Copilot Custom Instructions: Team Standards

## Code Quality:
- Follow PEP 8 style guidelines strictly
- Include type hints for all function signatures
- Write comprehensive docstrings with examples
- Add unit tests for all business logic
- Include integration tests for API endpoints
- Implement proper error handling with custom exceptions

## Architecture Patterns:
- Use dependency injection for all external services
- Implement repository pattern for data access
- Use factory pattern for object creation
- Apply single responsibility principle consistently
- Include proper separation of concerns
- Design for testability and maintainability

## Documentation:
- Include README files for all modules
- Document all configuration options
- Provide setup and deployment instructions
- Include API documentation with examples
- Add troubleshooting guides for common issues
```
