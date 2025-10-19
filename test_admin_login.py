#!/usr/bin/env python3
"""
Test admin login functionality
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_admin_login():
    print("Testing Admin Login")
    print("=" * 30)
    
    try:
        # Test admin login
        print("1. Testing admin login...")
        login_data = {
            "phone": "+250789751597",
            "password": "admin123"
        }
        
        response = requests.post(f"{BASE_URL}/users/login", json=login_data)
        
        if response.status_code == 200:
            user = response.json()
            print(f"[OK] Admin login successful")
            print(f"   Name: {user['name']}")
            print(f"   Role: {user['role']}")
            print(f"   Phone: {user['phone']}")
            
            if user['role'] == 'admin':
                print("[OK] Admin role confirmed")
            else:
                print(f"[ERROR] Expected admin role, got: {user['role']}")
        else:
            print(f"[ERROR] Login failed: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("[ERROR] Cannot connect to backend API")
        print("   Make sure backend is running: cd backend && python startup.py")
    except Exception as e:
        print(f"[ERROR] Test failed: {e}")

if __name__ == "__main__":
    test_admin_login()