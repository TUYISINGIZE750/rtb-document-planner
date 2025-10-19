import requests
import json

API_BASE = 'http://localhost:8000'

# Test admin login
print("Testing admin login...")
print("Phone: +250789751597")
print("Password: admin123")
print("")

try:
    response = requests.post(
        f'{API_BASE}/users/login',
        json={'phone': '+250789751597', 'password': 'admin123'}
    )
    
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
    
    if response.status_code == 200:
        user = response.json()
        print("\nLogin successful!")
        print(f"User: {user['name']}")
        print(f"Role: {user['role']}")
    else:
        print("\nLogin failed!")
        
except Exception as e:
    print(f"Error: {e}")
    print("\nMake sure the backend server is running on port 8000")
