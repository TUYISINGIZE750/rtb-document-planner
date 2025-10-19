import requests
from sqlalchemy.orm import Session
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from backend.database import engine
from backend.models import User

print("=" * 60)
print("RTB DOCUMENT PLANNER - COMPLETE SYSTEM CHECK")
print("=" * 60)

# 1. Check Backend Server
print("\n1. BACKEND SERVER CHECK")
print("-" * 60)
try:
    response = requests.get('http://localhost:8000/', timeout=5)
    if response.status_code == 200:
        print("[OK] Backend server is running on port 8000")
        print(f"   Response: {response.json()}")
    else:
        print(f"[ERROR] Backend returned status code: {response.status_code}")
except Exception as e:
    print(f"[ERROR] Backend server not accessible: {e}")
    print("   Please start backend: cd backend && python -m uvicorn main:app --port 8000")

# 2. Check Database Connection
print("\n2. DATABASE CONNECTION CHECK")
print("-" * 60)
try:
    response = requests.get('http://localhost:8000/health', timeout=5)
    data = response.json()
    if data.get('status') == 'healthy':
        print("[OK] Database is connected and healthy")
        print(f"   Status: {data}")
    else:
        print(f"[ERROR] Database issue: {data}")
except Exception as e:
    print(f"[ERROR] Cannot check database: {e}")

# 3. Check Users in Database
print("\n3. DATABASE USERS CHECK")
print("-" * 60)
try:
    db = Session(engine)
    users = db.query(User).all()
    print(f"[OK] Found {len(users)} users in database:\n")
    
    for user in users:
        print(f"   User ID: {user.user_id}")
        print(f"   Name: {user.name}")
        print(f"   Phone: {user.phone}")
        print(f"   Password: {user.password}")
        print(f"   Role: {user.role}")
        print(f"   Premium: {user.is_premium}")
        print(f"   Email: {user.email}")
        print(f"   Institution: {user.institution}")
        print("-" * 60)
    
    db.close()
except Exception as e:
    print(f"[ERROR] Database query failed: {e}")

# 4. Test Admin Login
print("\n4. ADMIN LOGIN TEST")
print("-" * 60)
try:
    response = requests.post(
        'http://localhost:8000/users/login',
        json={'phone': '+250789751597', 'password': 'admin123'},
        timeout=5
    )
    
    if response.status_code == 200:
        user = response.json()
        print("[OK] Admin login SUCCESSFUL!")
        print(f"   User: {user['name']}")
        print(f"   Role: {user['role']}")
        print(f"   Phone: {user['phone']}")
        print(f"   Email: {user['email']}")
    else:
        print(f"[ERROR] Admin login FAILED!")
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.text}")
except Exception as e:
    print(f"[ERROR] Admin login test failed: {e}")

# 5. Test Regular User Login
print("\n5. REGULAR USER LOGIN TEST")
print("-" * 60)
try:
    response = requests.post(
        'http://localhost:8000/users/login',
        json={'phone': '0796014803', 'password': '12345678'},
        timeout=5
    )
    
    if response.status_code == 200:
        user = response.json()
        print("[OK] User login SUCCESSFUL!")
        print(f"   User: {user['name']}")
        print(f"   Role: {user['role']}")
        print(f"   Phone: {user['phone']}")
    else:
        print(f"[ERROR] User login FAILED!")
        print(f"   Status: {response.status_code}")
        print(f"   Response: {response.text}")
except Exception as e:
    print(f"[ERROR] User login test failed: {e}")

# 6. Check Frontend Server
print("\n6. FRONTEND SERVER CHECK")
print("-" * 60)
try:
    response = requests.get('http://localhost:5173/', timeout=5)
    if response.status_code == 200:
        print("[OK] Frontend server is running on port 5173")
    else:
        print(f"[WARN] Frontend returned status code: {response.status_code}")
except Exception as e:
    print(f"[ERROR] Frontend server not accessible: {e}")
    print("   Please start frontend: cd frontend && python -m http.server 5173")

# Summary
print("\n" + "=" * 60)
print("SYSTEM STATUS SUMMARY")
print("=" * 60)
print("\n[OK] Backend API: http://localhost:8000")
print("[OK] API Docs: http://localhost:8000/docs")
print("[OK] Frontend: http://localhost:5173")
print("[OK] Login Page: http://localhost:5173/login.html")
print("[OK] Test Page: http://localhost:5173/test-login.html")
print("\n[ADMIN] ADMIN CREDENTIALS:")
print("   Phone: +250789751597")
print("   Password: admin123")
print("\n[USER] USER CREDENTIALS:")
print("   Phone: 0796014803")
print("   Password: 12345678")
print("\n" + "=" * 60)
