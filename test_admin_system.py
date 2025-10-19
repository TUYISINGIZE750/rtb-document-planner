import requests
import json

API_BASE = 'http://localhost:8000'

print("=" * 60)
print("ADMIN SYSTEM COMPREHENSIVE TEST")
print("=" * 60)

# 1. Test Backend Health
print("\n1. BACKEND HEALTH CHECK")
print("-" * 60)
try:
    response = requests.get(f'{API_BASE}/health')
    data = response.json()
    print(f"[OK] Backend Status: {data['status']}")
    print(f"[OK] Database: {data['database']}")
except Exception as e:
    print(f"[ERROR] Backend not accessible: {e}")
    exit(1)

# 2. Test Admin Login
print("\n2. ADMIN LOGIN TEST")
print("-" * 60)
try:
    response = requests.post(f'{API_BASE}/users/login', 
        json={'phone': '+250789751597', 'password': 'admin123'})
    
    if response.status_code == 200:
        admin = response.json()
        print(f"[OK] Admin login successful")
        print(f"    Name: {admin['name']}")
        print(f"    Role: {admin['role']}")
        print(f"    Phone: {admin['phone']}")
    else:
        print(f"[ERROR] Admin login failed: {response.text}")
        exit(1)
except Exception as e:
    print(f"[ERROR] Login test failed: {e}")
    exit(1)

# 3. Test Users API
print("\n3. USERS API TEST")
print("-" * 60)
try:
    response = requests.get(f'{API_BASE}/users/')
    if response.status_code == 200:
        users = response.json()
        print(f"[OK] Found {len(users)} users in database:")
        for user in users:
            status = "PREMIUM" if user['is_premium'] else "FREE"
            print(f"    - {user['name']} ({user['phone']}) - {status}")
            print(f"      Plans: {user['session_plans_downloaded']}/{user['session_plans_limit']}")
            print(f"      Schemes: {user['schemes_downloaded']}/{user['schemes_limit']}")
    else:
        print(f"[ERROR] Users API failed: {response.text}")
except Exception as e:
    print(f"[ERROR] Users API test failed: {e}")

# 4. Test Session Plans API
print("\n4. SESSION PLANS API TEST")
print("-" * 60)
try:
    response = requests.get(f'{API_BASE}/session-plans/')
    if response.status_code == 200:
        plans = response.json()
        print(f"[OK] Found {len(plans)} session plans in database")
    else:
        print(f"[ERROR] Session plans API failed: {response.text}")
except Exception as e:
    print(f"[ERROR] Session plans API test failed: {e}")

# 5. Test Schemes API
print("\n5. SCHEMES API TEST")
print("-" * 60)
try:
    response = requests.get(f'{API_BASE}/schemes-of-work/')
    if response.status_code == 200:
        schemes = response.json()
        print(f"[OK] Found {len(schemes)} schemes in database")
    else:
        print(f"[ERROR] Schemes API failed: {response.text}")
except Exception as e:
    print(f"[ERROR] Schemes API test failed: {e}")

# 6. Test User Activation API
print("\n6. USER ACTIVATION API TEST")
print("-" * 60)
try:
    # Find a non-admin user to test activation
    response = requests.get(f'{API_BASE}/users/')
    users = response.json()
    test_user = None
    for user in users:
        if user['role'] != 'admin':
            test_user = user
            break
    
    if test_user:
        print(f"[INFO] Testing activation for user: {test_user['name']} ({test_user['phone']})")
        
        # Test activation endpoint
        response = requests.put(f"{API_BASE}/users/{test_user['phone']}/activate",
            json={'session_plans': 5, 'schemes': 3})
        
        if response.status_code == 200:
            print(f"[OK] User activation API working")
        else:
            print(f"[ERROR] User activation failed: {response.text}")
    else:
        print(f"[INFO] No non-admin users found to test activation")
        
except Exception as e:
    print(f"[ERROR] User activation test failed: {e}")

print("\n" + "=" * 60)
print("ADMIN SYSTEM TEST SUMMARY")
print("=" * 60)
print("\n[ADMIN CREDENTIALS]")
print("Phone: +250789751597")
print("Password: admin123")
print("\n[ACCESS URLS]")
print("Admin Login: http://localhost:5173/direct-login.html")
print("Admin Dashboard: http://localhost:5173/admin.html")
print("API Documentation: http://localhost:8000/docs")
print("\n[FEATURES TESTED]")
print("✓ Backend health check")
print("✓ Admin authentication")
print("✓ Users API (fetch all users)")
print("✓ Session plans API")
print("✓ Schemes API")
print("✓ User activation API")
print("\n" + "=" * 60)