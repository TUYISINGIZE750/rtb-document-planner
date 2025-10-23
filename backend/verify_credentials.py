#!/usr/bin/env python3
"""
Simple script to verify login credentials work
"""
import requests
import json

API_BASE = 'https://leonardus437.pythonanywhere.com'

def test_login(phone, password):
    """Test login with given credentials"""
    try:
        print(f"Testing login for: {phone}")
        
        response = requests.post(f'{API_BASE}/users/login', 
                               json={'phone': phone, 'password': password},
                               headers={'Content-Type': 'application/json'})
        
        print(f"Status Code: {response.status_code}")
        
        if response.ok:
            data = response.json()
            print("✅ LOGIN SUCCESS")
            print(f"Name: {data.get('name')}")
            print(f"Role: {data.get('role')}")
            print(f"Premium: {data.get('is_premium')}")
            return True
        else:
            print("❌ LOGIN FAILED")
            try:
                error = response.json()
                print(f"Error: {error.get('detail', 'Unknown error')}")
            except:
                print(f"Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ CONNECTION ERROR: {e}")
        return False

def test_registration(phone, password, name):
    """Test user registration"""
    try:
        print(f"Testing registration for: {phone}")
        
        response = requests.post(f'{API_BASE}/users/register',
                               json={
                                   'phone': phone,
                                   'password': password,
                                   'name': name,
                                   'email': 'test@example.com',
                                   'institution': 'Test School'
                               },
                               headers={'Content-Type': 'application/json'})
        
        print(f"Status Code: {response.status_code}")
        
        if response.ok:
            print("✅ REGISTRATION SUCCESS")
            return True
        else:
            print("❌ REGISTRATION FAILED")
            try:
                error = response.json()
                print(f"Error: {error.get('detail', 'Unknown error')}")
            except:
                print(f"Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ CONNECTION ERROR: {e}")
        return False

if __name__ == "__main__":
    print("RTB Document Planner - Credential Verification")
    print("=" * 50)
    
    # Test API connection
    try:
        response = requests.get(f'{API_BASE}/')
        if response.ok:
            print("✅ API is online")
            data = response.json()
            print(f"Version: {data.get('version')}")
        else:
            print("❌ API connection failed")
            exit(1)
    except Exception as e:
        print(f"❌ Cannot connect to API: {e}")
        exit(1)
    
    print("\n" + "=" * 50)
    
    # Test existing credentials
    print("Testing existing credentials...")
    
    test_accounts = [
        ("+250796014803", "teacher123", "Test Teacher"),
        ("+250789751597", "admin123", "Administrator")
    ]
    
    working_accounts = []
    
    for phone, password, name in test_accounts:
        print(f"\n📱 Testing {phone}")
        if test_login(phone, password):
            working_accounts.append((phone, password, name))
        else:
            print(f"Trying to register {phone}...")
            if test_registration(phone, password, name):
                print("Registration successful, testing login...")
                if test_login(phone, password):
                    working_accounts.append((phone, password, name))
    
    print("\n" + "=" * 50)
    print("SUMMARY:")
    
    if working_accounts:
        print("✅ Working accounts:")
        for phone, password, name in working_accounts:
            print(f"  📱 {phone} / {password} ({name})")
    else:
        print("❌ No working accounts found")
        print("\nTrying to create a new test account...")
        
        # Create a fresh test account
        import time
        timestamp = str(int(time.time()))
        new_phone = f"+25079{timestamp[-6:]}"
        
        if test_registration(new_phone, "test123", "New Test User"):
            if test_login(new_phone, "test123"):
                print(f"✅ Created new working account: {new_phone} / test123")