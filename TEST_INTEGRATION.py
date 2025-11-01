#!/usr/bin/env python3
"""
Integration Test Script
Tests connectivity between frontend and backend

Usage: python TEST_INTEGRATION.py
"""

import requests
import json
import sys

# Configuration
BACKEND_URL = 'https://leonardus437.pythonanywhere.com'
FRONTEND_DOMAINS = [
    'rtb-planner.pages.dev',  # Replace with your actual domain
    'localhost:5173',
    'your-custom-domain.com'
]

# Test results
tests_passed = 0
tests_failed = 0

def print_header(text):
    print(f"\n{'='*60}")
    print(f"🧪 {text}")
    print(f"{'='*60}")

def test_status(name, passed, message=""):
    global tests_passed, tests_failed
    if passed:
        tests_passed += 1
        print(f"✅ {name}")
    else:
        tests_failed += 1
        print(f"❌ {name}")
    if message:
        print(f"   └─ {message}")

print_header("RTB Document Planner - Integration Test")

# Test 1: Backend API Health
print_header("1. Backend API Health Check")
try:
    response = requests.get(f"{BACKEND_URL}/", timeout=10, verify=True)
    if response.status_code == 200:
        data = response.json()
        test_status("Backend API accessible", True, f"Response: {data}")
    else:
        test_status("Backend API accessible", False, f"Status: {response.status_code}")
except requests.exceptions.SSLError as e:
    test_status("Backend API accessible", False, "SSL Certificate Error - Check HTTPS")
except requests.exceptions.ConnectionError as e:
    test_status("Backend API accessible", False, f"Connection Error: {str(e)[:50]}")
except Exception as e:
    test_status("Backend API accessible", False, f"Error: {str(e)[:50]}")

# Test 2: User Registration Endpoint
print_header("2. User Registration Endpoint")
try:
    test_data = {
        "name": "Test User",
        "phone": "+250700000099",
        "email": "test@example.com",
        "institution": "Test School",
        "password": "TestPassword123!"
    }
    response = requests.post(
        f"{BACKEND_URL}/users/register",
        json=test_data,
        timeout=10
    )
    test_status(
        "Registration endpoint responds",
        response.status_code in [200, 201, 400],  # Accept existing user error
        f"Status: {response.status_code}"
    )
except Exception as e:
    test_status("Registration endpoint responds", False, str(e)[:50])

# Test 3: Login Endpoint
print_header("3. User Login Endpoint")
try:
    login_data = {
        "phone": "+250700000099",
        "password": "TestPassword123!"
    }
    response = requests.post(
        f"{BACKEND_URL}/users/login",
        json=login_data,
        timeout=10
    )
    test_status(
        "Login endpoint responds",
        response.status_code in [200, 401],  # Accept auth failure
        f"Status: {response.status_code}"
    )
except Exception as e:
    test_status("Login endpoint responds", False, str(e)[:50])

# Test 4: CORS Headers
print_header("4. CORS Configuration")
try:
    headers = {
        'Origin': 'https://rtb-planner.pages.dev',
        'Content-Type': 'application/json'
    }
    response = requests.options(
        f"{BACKEND_URL}/",
        headers=headers,
        timeout=10
    )
    cors_origin = response.headers.get('Access-Control-Allow-Origin')
    test_status(
        "CORS headers present",
        'Access-Control-Allow-Origin' in response.headers,
        f"Origin: {cors_origin}"
    )
except Exception as e:
    test_status("CORS headers present", False, str(e)[:50])

# Test 5: Session Plan Endpoint
print_header("5. Session Plan Endpoints")
try:
    response = requests.get(
        f"{BACKEND_URL}/user-limits/%2B250700000099",
        timeout=10
    )
    test_status(
        "User limits endpoint responds",
        response.status_code in [200, 404],
        f"Status: {response.status_code}"
    )
except Exception as e:
    test_status("User limits endpoint responds", False, str(e)[:50])

# Test 6: Admin Endpoints
print_header("6. Admin Endpoints")
try:
    response = requests.get(
        f"{BACKEND_URL}/admin/users",
        timeout=10
    )
    test_status(
        "Admin users endpoint responds",
        response.status_code in [200, 401, 403],
        f"Status: {response.status_code}"
    )
except Exception as e:
    test_status("Admin users endpoint responds", False, str(e)[:50])

# Test 7: Frontend Accessibility
print_header("7. Frontend Accessibility (Manual Check)")
print(f"  Frontend should be accessible at:")
for domain in FRONTEND_DOMAINS:
    if domain != 'your-custom-domain.com':
        print(f"  - https://{domain}")

# Summary
print_header("Test Summary")
total = tests_passed + tests_failed
print(f"Passed: {tests_passed}/{total}")
print(f"Failed: {tests_failed}/{total}")

if tests_failed == 0:
    print("\n✅ All tests passed! Your deployment looks good.")
    sys.exit(0)
else:
    print(f"\n⚠️  {tests_failed} test(s) failed. Check above for details.")
    print("\nCommon fixes:")
    print("  1. Verify PythonAnywhere web app is running (click Reload)")
    print("  2. Check CORS configuration in main.py")
    print("  3. Verify API URL in frontend config.js")
    print("  4. Check PythonAnywhere error logs")
    sys.exit(1)
