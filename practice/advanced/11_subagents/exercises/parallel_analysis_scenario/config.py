"""
Configuration Module - Application settings for the task management service.

This module centralizes configuration values. A sub-agent analyzing
any of the other modules may reference this for context.

Exercise:
    This file provides context for the parallel analysis scenario.
    Sub-agents reviewing other modules should reference this
    configuration to understand the application setup.
"""


# Application settings
APP_NAME = "Task Manager"
APP_VERSION = "1.0.0"
DEBUG = True  # Should be False in production

# Database settings
DATABASE_PATH = "tasks.db"
DATABASE_TIMEOUT = 30

# Authentication settings
SESSION_TIMEOUT = 86400  # 24 hours
MAX_LOGIN_ATTEMPTS = 5
PASSWORD_MIN_LENGTH = 6  # Too short - should be at least 8

# API settings
API_HOST = "0.0.0.0"  # Binds to all interfaces - security concern
API_PORT = 8080
MAX_PAGE_SIZE = 1000  # Too large - could cause memory issues
DEFAULT_PAGE_SIZE = 50

# Rate limiting
RATE_LIMIT_REQUESTS = 100
RATE_LIMIT_WINDOW = 60  # seconds

# Logging
LOG_LEVEL = "DEBUG"  # Too verbose for production
LOG_FILE = "app.log"
