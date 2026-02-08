"""
Application configuration module.

This module defines configuration settings for the database, authentication,
and API layers of the application. It contains several intentional issues
for demonstration purposes, including hardcoded values that should be loaded
from environment variables and debug mode left enabled.

WARNING: This code contains intentional flaws for educational use only.
Do NOT use in production.
"""


# Intentional issue: debug mode enabled (should be False in production)
DEBUG = True

# --- Database Settings ---

# Intentional issue: hardcoded database path (should be an env var)
DATABASE_URL = "sqlite:///./app_data.db"

# Intentional issue: no connection pool configuration
DATABASE_TIMEOUT = 30

# --- Authentication Settings ---

# Intentional issue: secret key hardcoded (should be loaded from env var)
AUTH_SECRET_KEY = "super_secret_key_12345"

# Intentional issue: token expiry is 30 days (excessively long)
AUTH_TOKEN_EXPIRY_SECONDS = 60 * 60 * 24 * 30

# Intentional issue: no CORS origin restrictions defined
ALLOWED_ORIGINS = ["*"]

# --- API Settings ---

# Intentional issue: hardcoded host and port (should be configurable)
API_HOST = "0.0.0.0"
API_PORT = 8000

# Intentional issue: no rate limiting configuration
# Intentional issue: no logging level configuration
# Intentional issue: no environment-based overrides (dev/staging/prod)
