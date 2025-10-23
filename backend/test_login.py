#!/usr/bin/env python3
import requests
import json

API_BASE = 'https://leonardus437.pythonanywhere.com'

def test_login(phone, password):
    try:
        print(f"Testing login for: {phone}")
        
        response = requests.post(f'{API_BASE}/users/login', 
                               json={'phone': phone, 'password': password},
                               headers={'Content-Type': 'application/json'})
        
        print(f"Status Code: {response.status_code}")
        
        if response.ok:
            data = response.json()
            print("LOGIN SUCCESS")
            print(f"Name: {data.get('name')}")
            print(f"Role: {data.get('role')}")
            return True
        else:
            print("LOGIN FAILED")
            try:
                error = response.json()
                print(f"Error: {error.get('detail', 'Unknown error')}")
            except:
                print(f"Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"CONNECTION ERROR: {e}")
        return False

def test_registration(phone, password, name):
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
            print("REGISTRATION SUCCESS")
            return True
        else:
            print("REGISTRATION FAILED")
            try:
                error = response.json()
                print(f"Error: {error.get('detail', 'Unknown error')}")
            except:
                print(f"Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"CONNECTION ERROR: {e}")
        return False

if __name__ == "__main__":
    print("RTB Document Planner - Credential Test")
    print("=" * 40)
    
    # Test API connection
    try:
        response = requests.get(f'{API_BASE}/')
        if response.ok:
            print("API is online")
        else:
            print("API connection failed")
            exit(1)
    except Exception as e:
        print(f"Cannot connect to API: {e}")
        exit(1)
    
    print("\nTesting credentials...")
    
    # Test existing accounts
    test_accounts = [
        ("+250796014803", "teacher123"),
        ("+250789751597", "admin123")
    ]
    
    for phone, password in test_accounts:
        print(f"\nTesting {phone}")
        if not test_login(phone, password):
            print(f"Trying to register {phone}...")
            name = "Test Teacher" if "796" in phone else "Administrator"
            if test_registration(phone, password, name):
                test_login(phone, password)