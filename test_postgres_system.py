#!/usr/bin/env python3
"""
PostgreSQL System Test - Verifies PostgreSQL connection and system functionality
"""

import os
import requests
import psycopg2
import time

# Set PostgreSQL connection
os.environ['DATABASE_URL'] = 'postgresql://rtb_user:rtb_password@localhost:5433/rtb_planner'

def test_postgres_connection():
    """Test PostgreSQL database connection"""
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5433",
            database="rtb_planner",
            user="rtb_user",
            password="rtb_password"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"✅ PostgreSQL connected: {version[0][:50]}...")
        
        cursor.execute("SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = 'public';")
        table_count = cursor.fetchone()[0]
        print(f"✅ Tables in database: {table_count}")
        
        conn.close()
        return True
    except Exception as e:
        print(f"❌ PostgreSQL connection failed: {e}")
        return False

def test_backend_api():
    """Test backend API connection"""
    try:
        response = requests.get('http://localhost:8000/health', timeout=5)
        if response.status_code == 200:
            print("✅ Backend API is running")
            return True
        else:
            print(f"❌ Backend API health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Backend API connection failed: {e}")
        return False

def test_users_endpoint():
    """Test users endpoint"""
    try:
        response = requests.get('http://localhost:8000/users/', timeout=10)
        if response.status_code == 200:
            users = response.json()
            print(f"✅ Users endpoint working: {len(users)} users found")
            return len(users) > 0
        else:
            print(f"❌ Users endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Users endpoint error: {e}")
        return False

def main():
    print("🐘 PostgreSQL System Test")
    print("=" * 40)
    
    print("\n1. Testing PostgreSQL connection...")
    postgres_ok = test_postgres_connection()
    
    print("\n2. Testing Backend API...")
    backend_ok = test_backend_api()
    
    print("\n3. Testing Users endpoint...")
    users_ok = test_users_endpoint()
    
    print("\n" + "=" * 40)
    print("📊 TEST RESULTS")
    print("=" * 40)
    
    if postgres_ok:
        print("✅ PostgreSQL: WORKING")
    else:
        print("❌ PostgreSQL: FAILED")
    
    if backend_ok:
        print("✅ Backend API: WORKING")
    else:
        print("❌ Backend API: FAILED")
    
    if users_ok:
        print("✅ User Data: WORKING")
    else:
        print("❌ User Data: FAILED")
    
    if postgres_ok and backend_ok and users_ok:
        print("\n🎉 All systems working with PostgreSQL!")
    else:
        print("\n⚠️  Some issues detected. Check the logs above.")

if __name__ == "__main__":
    main()