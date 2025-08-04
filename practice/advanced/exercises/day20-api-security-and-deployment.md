# Day 20: API Security and Deployment

## Objective

Today focuses on securing your Flask APIs and preparing them for deployment. You will learn about common API security vulnerabilities, how to mitigate them, and basic deployment strategies for Flask applications, with GitHub Copilot assisting in generating the necessary code and configurations.

## Prerequisites

Install required packages:
```bash
pip install python-dotenv gunicorn
```

## Exercises

### Exercise 1: API Security Best Practices

Understand and implement common API security measures.

1.  **Input Validation and Sanitization**: Implement robust input validation for all API endpoints to prevent common attacks like SQL injection and XSS.
    -   *Prompting Hint*: `# Implement input validation and sanitization for Flask API`
2.  **Rate Limiting**: Implement basic rate limiting to prevent abuse and denial-of-service attacks.
    -   *Prompting Hint*: `# Implement rate limiting for Flask API endpoints`
3.  **Secure Password Handling**: Ensure passwords are never stored in plain text. Use hashing (e.g., `werkzeug.security`) and salting.
    -   *Prompting Hint*: `# Implement secure password hashing and verification`
4.  **Error Handling for Security**: Avoid revealing sensitive information in error messages. Provide generic error responses.
    -   *Prompting Hint*: `# Implement generic error responses for Flask API`
5.  **CORS Configuration**: Properly configure CORS to restrict access to your API from authorized domains only.
    -   *Prompting Hint*: `# Configure CORS for Flask API to allow specific origins`

### Exercise 2: Environment Management and Configuration

Manage application configurations and sensitive data securely.

1.  **Environment Variables**: Use `python-dotenv` to load environment variables for sensitive data (e.g., database credentials, API keys).
    -   *Prompting Hint*: `# Load environment variables using python-dotenv`
2.  **Configuration Classes**: Implement a configuration class for different environments (development, production).
    -   *Prompting Hint*: `# Create Flask configuration classes for dev and prod`
3.  **Logging**: Implement structured logging for your API to monitor activity and debug issues without exposing sensitive data.
    -   *Prompting Hint*: `# Implement structured logging for Flask API`
4.  **Secret Management**: Discuss and simulate basic secret management practices (e.g., not committing `.env` files).
    -   *Prompting Hint*: `# Explain best practices for secret management in Python`

### Exercise 3: Basic API Deployment

Prepare and deploy your Flask API.

1.  **WSGI Server (Gunicorn)**: Configure your Flask application to run with Gunicorn.
    -   *Prompting Hint*: `# Configure Flask app to run with Gunicorn`
2.  **`requirements.txt`**: Generate a `requirements.txt` file for your project dependencies.
    -   *Prompting Hint*: `# Generate requirements.txt for Flask project`
3.  **Dockerfile**: Create a basic Dockerfile to containerize your Flask application.
    -   *Prompting Hint*: `# Create Dockerfile for Flask Gunicorn application`
4.  **`.dockerignore`**: Create a `.dockerignore` file to exclude unnecessary files from your Docker image.
    -   *Prompting Hint*: `# Create .dockerignore for Flask project`
5.  **Basic Deployment Script**: Write a simple shell script to build and run your Docker image locally.
    -   *Prompting Hint*: `# Write shell script to build and run Docker image`

### Exercise 4: API Testing and Monitoring

Implement testing and monitoring for your deployed API.

1.  **API Unit Tests**: Write unit tests for your API endpoints using `pytest`.
    -   *Prompting Hint*: `# Write pytest unit tests for Flask API endpoints`
2.  **API Integration Tests**: Write integration tests to ensure different API components work together.
    -   *Prompting Hint*: `# Write pytest integration tests for Flask API`
3.  **Health Check Endpoint**: Implement a simple health check endpoint (`/health`) for monitoring.
    -   *Prompting Hint*: `# Implement /health endpoint for Flask API`
4.  **Basic Monitoring**: Discuss basic monitoring strategies (e.g., checking logs, uptime).
    -   *Prompting Hint*: `# Explain basic API monitoring strategies`

## Challenge Exercise: Secure and Deployable Microservice

Take one of your previous API exercises (e.g., the Task Management API from Day 18) and make it production-ready:
-   Implement all security best practices (validation, hashing, rate limiting).
-   Containerize it using Docker.
-   Configure it to run with Gunicorn.
-   Set up environment variables for sensitive configurations.
-   Write comprehensive unit and integration tests.
-   Add a health check endpoint.

*Prompting Hint*: `# Make Flask API production-ready with security, Docker, Gunicorn, and tests`

## Reflection

-   How did Copilot assist you in identifying and mitigating security vulnerabilities?
-   Were there any specific patterns Copilot suggested for Dockerfiles or deployment scripts?
-   How effective was Copilot in helping you write tests for your API?

