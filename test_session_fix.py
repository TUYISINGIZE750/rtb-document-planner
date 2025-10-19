#!/usr/bin/env python3
"""
Session Management Test Script - Verifies that session management and user data retrieval work correctly
"""

import requests
import json
import time
import sys

API_BASE = 'http://localhost:8000'

def test_api_health():
    """Test if API is running"""
    try:
        response = requests.get(f'{API_BASE}/health', timeout=5)
        if response.status_code == 200:
            print("✅ Backend API is running")
            return True
        else:
            print(f"❌ Backend API health check failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Cannot connect to backend API: {e}")
        return False

def test_user_registration():
    """Test user registration"""
    print("\n🧪 Testing user registration...")
    
    test_user = {
        "user_id": f"TEST_USER_{int(time.time())}",
        "name": "Test User Session",
        "phone": f"+25078{int(time.time()) % 10000000}",
        "email": "testsession@example.com",
        "institution": "Test Institution",
        "password": "testpass123",
        "role": "user"
    }
    
    try:
        response = requests.post(f'{API_BASE}/users/register', json=test_user, timeout=10)
        if response.status_code == 200:
            print(f"✅ User registration successful: {test_user['phone']}")
            return test_user
        else:
            print(f"❌ User registration failed: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Registration request failed: {e}")
        return None

def test_user_login(phone, password):
    """Test user login"""
    print(f"\n🔐 Testing login for {phone}...")
    
    try:
        response = requests.post(f'{API_BASE}/users/login', 
                               json={"phone": phone, "password": password}, 
                               timeout=10)
        if response.status_code == 200:
            user_data = response.json()
            print(f"✅ Login successful for {user_data['name']} ({user_data['role']})")
            return user_data
        else:
            print(f"❌ Login failed: {response.status_code} - {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Login request failed: {e}")
        return None

def test_get_all_users():
    """Test retrieving all users"""
    print("\n👥 Testing user data retrieval...")
    
    try:
        response = requests.get(f'{API_BASE}/users/', timeout=10)
        if response.status_code == 200:
            users = response.json()
            print(f"✅ Retrieved {len(users)} users from database")
            
            for user in users[:3]:  # Show first 3 users
                print(f"   👤 {user['name']} ({user['phone']}) - {user['role']}")
                
            return users
        else:
            print(f"❌ Failed to retrieve users: {response.status_code} - {response.text}")
            return []
    except requests.exceptions.RequestException as e:
        print(f"❌ Users retrieval request failed: {e}")
        return []

def test_session_validation(phone):
    """Test session validation"""
    print(f"\n🔍 Testing session validation for {phone}...")
    
    try:
        response = requests.post(f'{API_BASE}/users/validate-session', 
                               json={"phone": phone}, 
                               timeout=10)
        if response.status_code == 200:
            validation_data = response.json()
            print(f"✅ Session validation successful: {validation_data}")
            return True
        else:
            print(f"❌ Session validation failed: {response.status_code} - {response.text}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Session validation request failed: {e}")
        return False

def test_admin_login():
    """Test admin login specifically"""
    print("\n👑 Testing admin login...")
    return test_user_login('+250789751597', 'admin123')

def main():
    print("🚀 Starting Session Management Test Suite")
    print("=" * 50)
    
    # Test 1: API Health
    if not test_api_health():
        print("\n💥 Backend API is not running. Please start it first:")
        print("   cd backend && python startup.py")
        sys.exit(1)
    
    # Test 2: Admin Login
    admin_data = test_admin_login()
    if not admin_data:
        print("\n💥 Admin login failed. This is critical!")
        sys.exit(1)
    
    # Test 3: Get All Users
    users = test_get_all_users()
    if len(users) == 0:
        print("\n⚠️  No users found in database. This might be the issue!")
    
    # Test 4: User Registration
    test_user = test_user_registration()
    if test_user:
        # Test 5: New User Login
        user_data = test_user_login(test_user['phone'], test_user['password'])
        
        if user_data:
            # Test 6: Session Validation
            test_session_validation(user_data['phone'])
    
    # Test 7: Verify users count after registration
    final_users = test_get_all_users()
    
    print("\n" + "=" * 50)
    print("📊 TEST SUMMARY")
    print("=" * 50)
    
    if admin_data:
        print("✅ Admin login: WORKING")
    else:
        print("❌ Admin login: FAILED")
    
    if len(final_users) > 0:
        print(f"✅ User data retrieval: WORKING ({len(final_users)} users)")
    else:
        print("❌ User data retrieval: FAILED (0 users)")
    
    if test_user:
        print("✅ User registration: WORKING")
    else:
        print("❌ User registration: FAILED")
    
    print("\n🎯 RECOMMENDATIONS:")
    
    if len(final_users) == 0:
        print("1. Run: python fix_database.py")
        print("2. Restart backend: cd backend && python startup.py")
    
    if not admin_data:
        print("3. Check admin credentials in database")
        print("4. Verify backend is properly connected to database")
    
    print("\n✨ Session management fixes have been applied to:")
    print("   - frontend/auth.js (improved session validation)")
    print("   - backend/main.py (added session endpoints)")
    print("   - backend/init_db.py (proper user table creation)")

if __name__ == "__main__":
    main()