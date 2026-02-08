# Team Coding Standards

## Python Standards

- **Naming**: `snake_case` for functions and variables, `PascalCase` for classes, `UPPER_SNAKE_CASE` for constants
- **Docstrings**: Required on all modules, classes, and public functions; use Google-style format
- **Type hints**: Required on all function signatures (parameters and return types)
- **Line length**: 88 characters maximum (Black formatter default)
- **Formatting**: Use Black for auto-formatting, isort for import sorting

## API Standards

- **REST conventions**: Use nouns for resources, HTTP verbs for actions
- **Versioning**: URL path versioning (`/api/v1/`, `/api/v2/`)
- **Error responses**: Standard envelope format:
  ```json
  {
    "error": {
      "code": "RESOURCE_NOT_FOUND",
      "message": "Product with ID 42 was not found",
      "status": 404
    }
  }
  ```
- **Pagination**: Cursor-based for v2 endpoints; include `next_cursor` in response meta
- **Date format**: ISO 8601 (`2025-01-15T10:30:00Z`) for all date/time fields

## Testing Requirements

- **Coverage**: Minimum 80% line coverage for all services
- **Framework**: pytest with pytest-asyncio for async code
- **Structure**: Mirror source layout in `tests/` directory
- **Naming**: Test files prefixed with `test_`, test functions prefixed with `test_`
- **Required tests**: Unit tests for business logic, integration tests for API endpoints, error path tests for all error responses

## Security Requirements

- **No hardcoded secrets**: Use environment variables or a secrets manager
- **Input validation**: Validate all user input at the API boundary using Pydantic models
- **SQL injection**: Use parameterized queries only (ORM handles this)
- **Rate limiting**: All public endpoints must have rate limits configured at the gateway
- **Logging**: Never log sensitive data (passwords, tokens, PII)
- **Dependencies**: Run `pip-audit` weekly; no known vulnerabilities in production
