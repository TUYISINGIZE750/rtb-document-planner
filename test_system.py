#!/usr/bin/env python3
"""
Quick system test for RTB Document Planner
"""
import requests
import time
import sys

def test_backend():
    """Test if backend is running"""
    try:
        response = requests.get("http://localhost:8001/health", timeout=5)
        if response.status_code == 200:
            print("✅ Backend is running and healthy")
            return True
        else:
            print(f"❌ Backend returned status {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Backend not accessible: {e}")
        return False

def test_frontend():
    """Test if frontend is accessible"""
    try:
        response = requests.get("http://localhost:5173", timeout=5)
        if response.status_code == 200:
            print("✅ Frontend is accessible")
            return True
        else:
            print(f"❌ Frontend returned status {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Frontend not accessible: {e}")
        return False

def main():
    print("🔍 Testing RTB Document Planner System...")
    print("-" * 40)
    
    backend_ok = test_backend()
    frontend_ok = test_frontend()
    
    print("-" * 40)
    if backend_ok and frontend_ok:
        print("🎉 System is running correctly!")
        print("📱 Access the app at: http://localhost:5173")
    else:
        print("⚠️  Some services are not running.")
        print("📖 Check START_HERE.md for setup instructions")
    
    return 0 if (backend_ok and frontend_ok) else 1

if __name__ == "__main__":
    sys.exit(main())