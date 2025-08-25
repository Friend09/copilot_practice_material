"""
Test script to validate the secure implementation works correctly
"""

import tempfile
import os
import sqlite3
from demo.advanced.demo5_code_review.setup.secure_implementation import (
    SecureUserManager, 
    SecureSQLiteDatabase,
    PasswordManager,
    InputValidator,
    secure_operation_with_error_handling
)

def test_secure_implementation():
    """Test the secure implementation"""
    print("🧪 Testing secure implementation...")
    
    # Create temporary database
    with tempfile.NamedTemporaryFile(suffix='.db', delete=False) as temp_db:
        db_path = temp_db.name
    
    try:
        # Initialize database
        conn = sqlite3.connect(db_path)
        conn.execute("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TEXT NOT NULL,
                is_active BOOLEAN DEFAULT 1,
                deleted_at TEXT
            )
        """)
        conn.commit()
        conn.close()
        
        # Test secure user manager
        db = SecureSQLiteDatabase(db_path)
        user_manager = SecureUserManager(db)
        
        # Test user creation
        print("✅ Testing user creation...")
        user_id = user_manager.create_user(
            "John Doe",
            "john.doe@example.com", 
            "SecurePassword123!"
        )
        assert user_id is not None, "User creation failed"
        print(f"   User created with ID: {user_id}")
        
        # Test authentication
        print("✅ Testing authentication...")
        auth_result = user_manager.authenticate_user(
            "john.doe@example.com",
            "SecurePassword123!"
        )
        assert auth_result == user_id, "Authentication failed"
        print(f"   Authentication successful for user: {auth_result}")
        
        # Test profile retrieval
        print("✅ Testing profile retrieval...")
        profile = user_manager.get_user_profile(user_id)
        assert profile is not None, "Profile retrieval failed"
        assert 'password' not in profile, "Profile contains sensitive data"
        assert 'password_hash' not in profile, "Profile contains password hash"
        print(f"   Profile retrieved: {profile['name']} ({profile['email']})")
        
        # Test password manager
        print("✅ Testing password hashing...")
        password = "TestPassword123!"
        hashed = PasswordManager.hash_password(password)
        assert PasswordManager.verify_password(password, hashed), "Password verification failed"
        print("   Password hashing and verification working correctly")
        
        # Test input validation
        print("✅ Testing input validation...")
        validator = InputValidator()
        
        # Valid data
        valid_data = validator.validate_user_data({
            'name': 'Jane Smith',
            'email': 'jane@example.com',
            'password': 'ValidPass123!'
        })
        assert valid_data['name'] == 'Jane Smith', "Name validation failed"
        
        # Invalid data should raise exception
        try:
            validator.validate_user_data({
                'name': '',
                'email': 'invalid-email',
                'password': 'weak'
            })
            assert False, "Should have raised validation error"
        except ValueError:
            print("   Input validation correctly rejected invalid data")
        
        # Test secure operation
        print("✅ Testing secure operation...")
        result = secure_operation_with_error_handling({
            'required_field': 'test data'
        })
        assert result == 'TEST DATA', "Secure operation failed"
        print("   Secure operation working correctly")
        
        db.close()
        print("\n🎉 All tests passed! Secure implementation is working correctly.")
        
    finally:
        # Cleanup
        try:
            os.unlink(db_path)
        except:
            pass

if __name__ == "__main__":
    test_secure_implementation()