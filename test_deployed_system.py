#!/usr/bin/env python3
"""
Test script to verify the deployed RTB Document Planner system
"""
import requests
import json

def test_backend():
    """Test backend API"""
    print("🔍 Testing Backend API...")
    
    try:
        response = requests.get("https://leonardus437.pythonanywhere.com/")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Backend Status: {data.get('status')}")
            print(f"✅ Version: {data.get('version')}")
            print(f"✅ CORS: {data.get('cors')}")
            print(f"✅ Users: {data.get('users_count')}")
            print(f"✅ Session Plans: {data.get('session_plans_count')}")
            return True
        else:
            print(f"❌ Backend Error: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Backend Connection Error: {e}")
        return False

def test_session_plan_creation():
    """Test session plan creation"""
    print("\n🔍 Testing Session Plan Creation...")
    
    test_data = {
        "sector": "ICT & MULTIMEDIA",
        "trade": "Software Development",
        "rqf_level": "Level 4",
        "date": "2024-01-15",
        "trainer_name": "Test Teacher",
        "term": "Term 1",
        "module_code_title": "Introduction to Programming",
        "week": "Week 1",
        "number_of_trainees": 25,
        "class_name": "L4CSA-A",
        "topic_of_session": "Variables and Data Types",
        "learning_outcomes": "Students will understand basic programming concepts",
        "indicative_contents": "• Variables\n• Data types\n• Basic operations",
        "session_range": "Basic to intermediate",
        "facilitation_techniques": "Trainer Guided",
        "duration": 40
    }
    
    try:
        response = requests.post(
            "https://leonardus437.pythonanywhere.com/session-plans",
            headers={"Content-Type": "application/json"},
            json=test_data
        )
        
        if response.status_code == 201:
            result = response.json()
            print(f"✅ Session Plan Created: ID {result.get('id')}")
            return result.get('id')
        else:
            print(f"❌ Session Plan Creation Error: {response.status_code}")
            print(f"Response: {response.text}")
            return None
    except Exception as e:
        print(f"❌ Session Plan Creation Error: {e}")
        return None

def test_frontend_access():
    """Test frontend accessibility"""
    print("\n🔍 Testing Frontend Access...")
    
    urls = [
        "https://tuyisingize750.github.io/rtb-document-planner/",
        "https://tuyisingize750.github.io/rtb-document-planner/login.html",
        "https://tuyisingize750.github.io/rtb-document-planner/wizard-fixed.html",
        "https://tuyisingize750.github.io/rtb-document-planner/scheme-wizard-fixed.html"
    ]
    
    for url in urls:
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                print(f"✅ {url.split('/')[-1] or 'index.html'}: Accessible")
            else:
                print(f"❌ {url.split('/')[-1] or 'index.html'}: {response.status_code}")
        except Exception as e:
            print(f"❌ {url.split('/')[-1] or 'index.html'}: {e}")

def main():
    print("🚀 RTB Document Planner System Test")
    print("=" * 50)
    
    # Test backend
    backend_ok = test_backend()
    
    # Test session plan creation
    if backend_ok:
        session_id = test_session_plan_creation()
    
    # Test frontend
    test_frontend_access()
    
    print("\n" + "=" * 50)
    if backend_ok:
        print("✅ System Status: READY FOR TESTING")
        print("\n📋 Test Instructions:")
        print("1. Visit: https://tuyisingize750.github.io/rtb-document-planner/")
        print("2. Login with: +250789751597 / admin123")
        print("3. Try creating session plans and schemes")
        print("4. Check admin dashboard functionality")
    else:
        print("❌ System Status: BACKEND ISSUES DETECTED")

if __name__ == "__main__":
    main()