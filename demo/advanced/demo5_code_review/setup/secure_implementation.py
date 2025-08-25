"""
Demo 5: Code Review - Secure Implementation Examples
===================================================

This file demonstrates secure implementations and best practices that address
the vulnerabilities found in the problematic code.

These examples show how to properly implement:
- Secure password handling
- SQL injection prevention  
- Input validation
- Error handling
- Configuration management
"""

import os
import logging
import bcrypt
import sqlite3
from datetime import datetime
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from email_validator import validate_email, EmailNotValidError
import re
from abc import ABC, abstractmethod
from functools import wraps

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class SecureConfig:
    """✅ Secure configuration management using environment variables"""
    secret_key: str
    database_url: str
    api_key: str
    debug: bool = False
    
    @classmethod
    def from_env(cls) -> 'SecureConfig':
        """Create configuration from environment variables"""
        required_vars = ['SECRET_KEY', 'DATABASE_URL', 'API_KEY']
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        
        if missing_vars:
            raise ValueError(f"Missing required environment variables: {missing_vars}")
        
        return cls(
            secret_key=os.getenv('SECRET_KEY'),
            database_url=os.getenv('DATABASE_URL'),
            api_key=os.getenv('API_KEY'),
            debug=os.getenv('DEBUG', 'false').lower() == 'true'
        )


def log_security_event(event_type: str):
    """✅ Decorator for logging security-relevant events"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                logger.info(f"Security event: {event_type} - {func.__name__} succeeded")
                return result
            except Exception as e:
                logger.error(f"Security event: {event_type} - {func.__name__} failed: {e}")
                raise
        return wrapper
    return decorator


class PasswordManager:
    """✅ Secure password handling with bcrypt"""
    
    @staticmethod
    def hash_password(password: str) -> str:
        """Securely hash a password using bcrypt"""
        if not password:
            raise ValueError("Password cannot be empty")
        
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed.decode('utf-8')
    
    @staticmethod
    def verify_password(password: str, hashed: str) -> bool:
        """Verify a password against its hash"""
        if not password or not hashed:
            return False
        
        try:
            return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))
        except (ValueError, TypeError):
            logger.warning("Invalid password hash format")
            return False
    
    @staticmethod
    def validate_password_strength(password: str) -> List[str]:
        """Validate password strength and return list of issues"""
        issues = []
        
        if len(password) < 8:
            issues.append("Password must be at least 8 characters")
        if len(password) > 128:
            issues.append("Password must be less than 128 characters")
        if not re.search(r'[A-Z]', password):
            issues.append("Password must contain at least one uppercase letter")
        if not re.search(r'[a-z]', password):
            issues.append("Password must contain at least one lowercase letter")
        if not re.search(r'\d', password):
            issues.append("Password must contain at least one digit")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            issues.append("Password must contain at least one special character")
        
        return issues


class InputValidator:
    """✅ Comprehensive input validation"""
    
    @staticmethod
    def validate_user_data(data: Dict[str, Any]) -> Dict[str, Any]:
        """Validate user registration data"""
        if not isinstance(data, dict):
            raise ValueError("Input must be a dictionary")
        
        errors = []
        
        # Validate required fields
        required_fields = ['name', 'email', 'password']
        for field in required_fields:
            if field not in data or not data[field]:
                errors.append(f"Missing required field: {field}")
        
        if errors:
            raise ValueError(f"Validation errors: {', '.join(errors)}")
        
        # Validate name
        name = str(data['name']).strip()
        if len(name) < 2 or len(name) > 50:
            errors.append("Name must be 2-50 characters")
        if not re.match(r'^[a-zA-Z\s\-\'\.]+$', name):
            errors.append("Name contains invalid characters")
        
        # Validate email
        try:
            email_info = validate_email(data['email'])
            email = email_info.email
        except EmailNotValidError as e:
            errors.append(f"Invalid email: {str(e)}")
            email = None
        
        # Validate password
        password = str(data['password'])
        password_issues = PasswordManager.validate_password_strength(password)
        errors.extend(password_issues)
        
        if errors:
            raise ValueError(f"Validation errors: {', '.join(errors)}")
        
        return {
            'name': name,
            'email': email,
            'password': password
        }
    
    @staticmethod
    def sanitize_string(value: str, max_length: int = 255) -> str:
        """Sanitize string input"""
        if not isinstance(value, str):
            value = str(value)
        
        # Remove null bytes and control characters
        sanitized = ''.join(char for char in value if ord(char) >= 32 or char in '\t\n\r')
        
        # Truncate to max length
        return sanitized[:max_length].strip()


class DatabaseInterface(ABC):
    """✅ Abstract database interface for dependency injection"""
    
    @abstractmethod
    def execute_query(self, query: str, params: tuple = ()) -> Any:
        """Execute a database query with parameters"""
        pass
    
    @abstractmethod
    def execute_many(self, query: str, params_list: List[tuple]) -> None:
        """Execute a query multiple times with different parameters"""
        pass
    
    @abstractmethod
    def commit(self) -> None:
        """Commit the current transaction"""
        pass
    
    @abstractmethod
    def rollback(self) -> None:
        """Rollback the current transaction"""
        pass
    
    @abstractmethod
    def close(self) -> None:
        """Close the database connection"""
        pass


class SecureSQLiteDatabase(DatabaseInterface):
    """✅ Secure SQLite database implementation"""
    
    def __init__(self, database_path: str):
        self.database_path = database_path
        self.connection = sqlite3.connect(database_path)
        self.connection.row_factory = sqlite3.Row
        
        # Enable foreign keys and secure settings
        self.connection.execute("PRAGMA foreign_keys = ON")
        self.connection.execute("PRAGMA secure_delete = ON")
    
    def execute_query(self, query: str, params: tuple = ()) -> Any:
        """✅ Execute parameterized query to prevent SQL injection"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
        except sqlite3.Error as e:
            logger.error(f"Database query failed: {e}")
            raise
    
    def execute_many(self, query: str, params_list: List[tuple]) -> None:
        """Execute query multiple times with different parameters"""
        try:
            cursor = self.connection.cursor()
            cursor.executemany(query, params_list)
        except sqlite3.Error as e:
            logger.error(f"Database batch operation failed: {e}")
            raise
    
    def commit(self) -> None:
        """Commit the current transaction"""
        self.connection.commit()
    
    def rollback(self) -> None:
        """Rollback the current transaction"""
        self.connection.rollback()
    
    def close(self) -> None:
        """Close the database connection"""
        self.connection.close()


class SecureUserManager:
    """✅ Secure user management with proper practices"""
    
    def __init__(self, database: DatabaseInterface):
        self.db = database
        self.validator = InputValidator()
        self.password_manager = PasswordManager()
    
    @log_security_event("user_creation")
    def create_user(self, name: str, email: str, password: str) -> int:
        """✅ Create user with secure validation and password hashing"""
        try:
            # Validate input data
            validated_data = self.validator.validate_user_data({
                'name': name,
                'email': email,
                'password': password
            })
            
            # Check if email already exists
            if self.get_user_by_email(validated_data['email']):
                raise ValueError("Email already registered")
            
            # Hash password securely
            password_hash = self.password_manager.hash_password(validated_data['password'])
            
            # Insert user with parameterized query
            query = """
                INSERT INTO users (name, email, password_hash, created_at, is_active)
                VALUES (?, ?, ?, ?, ?)
            """
            params = (
                validated_data['name'],
                validated_data['email'],
                password_hash,
                datetime.now().isoformat(),
                True
            )
            
            self.db.execute_query(query, params)
            self.db.commit()
            
            # Get the user ID (secure way)
            user = self.get_user_by_email(validated_data['email'])
            logger.info(f"User created successfully: {validated_data['email']}")
            return user['id'] if user else None
            
        except Exception as e:
            self.db.rollback()
            logger.error(f"Failed to create user: {e}")
            raise
    
    def get_user_by_id(self, user_id: int) -> Optional[Dict[str, Any]]:
        """✅ Get user by ID with parameterized query"""
        try:
            query = "SELECT id, name, email, created_at, is_active FROM users WHERE id = ? AND is_active = 1"
            result = self.db.execute_query(query, (user_id,))
            
            if result:
                return dict(result[0])
            return None
            
        except Exception as e:
            logger.error(f"Failed to get user {user_id}: {e}")
            return None
    
    def get_user_by_email(self, email: str) -> Optional[Dict[str, Any]]:
        """✅ Get user by email with parameterized query"""
        try:
            query = "SELECT id, name, email, created_at, is_active FROM users WHERE email = ? AND is_active = 1"
            result = self.db.execute_query(query, (email,))
            
            if result:
                return dict(result[0])
            return None
            
        except Exception as e:
            logger.error(f"Failed to get user by email: {e}")
            return None
    
    @log_security_event("user_authentication")
    def authenticate_user(self, email: str, password: str) -> Optional[int]:
        """✅ Authenticate user with secure password verification"""
        try:
            # Get user with password hash
            query = "SELECT id, password_hash FROM users WHERE email = ? AND is_active = 1"
            result = self.db.execute_query(query, (email,))
            
            if not result:
                # Log failed attempt but don't reveal if email exists
                logger.warning(f"Authentication failed for email: {email}")
                return None
            
            user_data = dict(result[0])
            
            # Verify password
            if self.password_manager.verify_password(password, user_data['password_hash']):
                logger.info(f"Successful authentication for user: {user_data['id']}")
                return user_data['id']
            else:
                logger.warning(f"Invalid password for user: {user_data['id']}")
                return None
                
        except Exception as e:
            logger.error(f"Authentication error: {e}")
            return None
    
    def get_user_profile(self, user_id: int) -> Optional[Dict[str, Any]]:
        """✅ Get user profile without sensitive data"""
        user = self.get_user_by_id(user_id)
        if user:
            # Return only safe profile data
            return {
                'id': user['id'],
                'name': user['name'],
                'email': user['email'],
                'created_at': user['created_at']
                # ✅ Never return password or password_hash
            }
        return None
    
    def update_user_profile(self, user_id: int, updates: Dict[str, Any]) -> bool:
        """✅ Update user profile with validation"""
        try:
            # Validate updates
            allowed_fields = {'name', 'email'}
            update_fields = set(updates.keys())
            
            if not update_fields.issubset(allowed_fields):
                invalid_fields = update_fields - allowed_fields
                raise ValueError(f"Invalid fields for update: {invalid_fields}")
            
            # Validate individual fields
            if 'name' in updates:
                name = self.validator.sanitize_string(updates['name'], 50)
                if not name:
                    raise ValueError("Invalid name")
                updates['name'] = name
            
            if 'email' in updates:
                try:
                    email_info = validate_email(updates['email'])
                    updates['email'] = email_info.email
                except EmailNotValidError:
                    raise ValueError("Invalid email format")
            
            # Build update query
            set_clauses = [f"{field} = ?" for field in updates.keys()]
            query = f"UPDATE users SET {', '.join(set_clauses)} WHERE id = ? AND is_active = 1"
            params = list(updates.values()) + [user_id]
            
            self.db.execute_query(query, tuple(params))
            self.db.commit()
            
            logger.info(f"User profile updated: {user_id}")
            return True
            
        except Exception as e:
            self.db.rollback()
            logger.error(f"Failed to update user profile {user_id}: {e}")
            return False
    
    def soft_delete_user(self, user_id: int) -> bool:
        """✅ Soft delete user (deactivate instead of hard delete)"""
        try:
            query = "UPDATE users SET is_active = 0, deleted_at = ? WHERE id = ?"
            params = (datetime.now().isoformat(), user_id)
            
            self.db.execute_query(query, params)
            self.db.commit()
            
            logger.info(f"User soft deleted: {user_id}")
            return True
            
        except Exception as e:
            self.db.rollback()
            logger.error(f"Failed to delete user {user_id}: {e}")
            return False


def secure_operation_with_error_handling(data: Dict[str, Any]) -> str:
    """✅ Proper error handling with specific exceptions and logging"""
    try:
        if not isinstance(data, dict):
            raise TypeError("Input must be a dictionary")
        
        if 'required_field' not in data:
            raise ValueError("Missing required field 'required_field'")
        
        value = data['required_field']
        
        if not isinstance(value, str):
            raise TypeError(f"Field 'required_field' must be string, got {type(value).__name__}")
        
        if not value.strip():
            raise ValueError("Field 'required_field' cannot be empty")
        
        processed = value.strip().upper()
        logger.info("Operation completed successfully")
        return processed
        
    except (TypeError, ValueError) as e:
        logger.error(f"Input validation error: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error in secure_operation: {e}")
        raise RuntimeError("An unexpected error occurred") from e


# ✅ Example usage and testing
if __name__ == "__main__":
    print("🔒 Secure implementation examples loaded successfully!")
    print("✅ Features demonstrated:")
    print("   - Secure password hashing with bcrypt")
    print("   - SQL injection prevention with parameterized queries")
    print("   - Comprehensive input validation")
    print("   - Proper error handling and logging")
    print("   - Configuration management with environment variables")
    print("   - Secure data structures and dependency injection")
    print("\n🎯 This code addresses all major security vulnerabilities found in the review.")