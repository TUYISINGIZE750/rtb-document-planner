"""
Complete System Test for RTB Document Planner
Tests all API endpoints and document generation
"""
import requests
import json
import time
import os
from pathlib import Path

API_BASE = "http://localhost:8000"

def test_api_health():
    """Test API health endpoint"""
    try:
        response = requests.get(f"{API_BASE}/health", timeout=5)
        if response.status_code == 200:
            health_data = response.json()
            print(f"✅ API Health: {health_data}")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Cannot connect to API: {e}")
        return False

def test_session_plan_creation():
    """Test session plan creation"""
    session_plan_data = {
        "sector": "ICT & MULTIMEDIA",
        "sub_sector": "Computer system and architecture",
        "trade": "Software Development",
        "qualification_title": "Diploma in Software Development",
        "rqf_level": "Level 4",
        "module_code_title": "GENCP 401: C Programming",
        "term": "Term 1",
        "week": "Week 4",
        "date": "2025-01-17",
        "trainer_name": "John Doe",
        "class_name": "L4CSA-A",
        "number_of_trainees": "25",
        "learning_outcomes": "By the end of this session, learners will be able to implement basic C programming concepts including variables, data types, and control structures.",
        "indicative_contents": "• Introduction to C programming syntax\n• Variables and data types\n• Basic input/output operations\n• Control structures (if-else, loops)",
        "topic_of_session": "Introduction to C Programming Fundamentals",
        "duration": "40",
        "objectives": "1. Understand C programming syntax\n2. Declare and use variables\n3. Implement basic control structures",
        "facilitation_techniques": "Trainer Guided",
        "learning_activities": "Hands-on coding exercises, pair programming, debugging activities",
        "resources": "Computers, IDE software, C compiler, programming worksheets",
        "assessment_details": "Practical coding assessment, oral questions on syntax",
        "references": "C Programming Language by Kernighan & Ritchie",
        "session_range": "From basic syntax to simple program structure"
    }
    
    try:
        response = requests.post(
            f"{API_BASE}/session-plans/",
            headers={"Content-Type": "application/json"},
            json=session_plan_data,
            timeout=10
        )
        
        if response.status_code == 200:
            plan = response.json()
            print(f"✅ Session plan created with ID: {plan['id']}")
            return plan['id']
        else:
            print(f"❌ Session plan creation failed: {response.status_code}")
            print(f"Response: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Session plan creation error: {e}")
        return None

def test_scheme_of_work_creation():
    """Test scheme of work creation"""
    scheme_data = {
        "sector": "ICT & MULTIMEDIA",
        "sub_sector": "Computer system and architecture",
        "trade": "Software Development",
        "qualification_title": "Diploma in Software Development",
        "rqf_level": "Level 4",
        "module_code_title": "GENCP 401: C Programming",
        "school_year": "2024-2025",
        "term": "Term 1",
        "weeks_covered": "Weeks 1-12",
        "class_name": "L4CSA-A",
        "number_of_classes": "3 classes per week",
        "trainer_name": "John Doe",
        "module_learning_hours": "120 hours",
        "learning_outcomes": "Students will master C programming fundamentals, data structures, and algorithm implementation.",
        "indicative_contents": "C syntax, variables, control structures, functions, arrays, pointers, file handling",
        "duration_per_lo_ic": "10 hours per learning outcome",
        "learning_activities": "Coding exercises, projects, peer programming, debugging sessions",
        "resources": "Computers, IDE, compilers, textbooks, online resources",
        "evidence_of_assessment": "Practical assignments, written tests, project work",
        "learning_place": "Computer Laboratory",
        "observation_notes": "Monitor student progress regularly",
        "integrated_assessment": "Final project combining all learned concepts",
        "verification_approval": "Approved by Head of Department"
    }
    
    try:
        response = requests.post(
            f"{API_BASE}/schemes-of-work/",
            headers={"Content-Type": "application/json"},
            json=scheme_data,
            timeout=10
        )
        
        if response.status_code == 200:
            scheme = response.json()
            print(f"✅ Scheme of work created with ID: {scheme['id']}")
            return scheme['id']
        else:
            print(f"❌ Scheme creation failed: {response.status_code}")
            print(f"Response: {response.text}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"❌ Scheme creation error: {e}")
        return None

def test_document_download(plan_id, scheme_id):
    """Test document download functionality"""
    downloads_dir = Path("test_downloads")
    downloads_dir.mkdir(exist_ok=True)
    
    # Test session plan download
    if plan_id:
        try:
            response = requests.get(f"{API_BASE}/session-plans/{plan_id}/download", timeout=30)
            if response.status_code == 200:
                session_file = downloads_dir / f"test_session_plan_{plan_id}.docx"
                with open(session_file, 'wb') as f:
                    f.write(response.content)
                print(f"✅ Session plan downloaded: {session_file}")
            else:
                print(f"❌ Session plan download failed: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"❌ Session plan download error: {e}")
    
    # Test scheme download
    if scheme_id:
        try:
            response = requests.get(f"{API_BASE}/schemes-of-work/{scheme_id}/download", timeout=30)
            if response.status_code == 200:
                scheme_file = downloads_dir / f"test_scheme_{scheme_id}.docx"
                with open(scheme_file, 'wb') as f:
                    f.write(response.content)
                print(f"✅ Scheme of work downloaded: {scheme_file}")
            else:
                print(f"❌ Scheme download failed: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"❌ Scheme download error: {e}")

def test_list_endpoints():
    """Test list endpoints"""
    try:
        # Test session plans list
        response = requests.get(f"{API_BASE}/session-plans/", timeout=10)
        if response.status_code == 200:
            plans = response.json()
            print(f"✅ Retrieved {len(plans)} session plans")
        else:
            print(f"❌ Session plans list failed: {response.status_code}")
        
        # Test schemes list
        response = requests.get(f"{API_BASE}/schemes-of-work/", timeout=10)
        if response.status_code == 200:
            schemes = response.json()
            print(f"✅ Retrieved {len(schemes)} schemes of work")
        else:
            print(f"❌ Schemes list failed: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        print(f"❌ List endpoints error: {e}")

def main():
    """Run complete system test"""
    print("=" * 60)
    print("RTB Document Planner - Complete System Test")
    print("=" * 60)
    print()
    
    # Test 1: API Health
    print("1. Testing API Health...")
    if not test_api_health():
        print("❌ API is not running. Please start the backend first.")
        return
    print()
    
    # Test 2: Session Plan Creation
    print("2. Testing Session Plan Creation...")
    plan_id = test_session_plan_creation()
    print()
    
    # Test 3: Scheme of Work Creation
    print("3. Testing Scheme of Work Creation...")
    scheme_id = test_scheme_of_work_creation()
    print()
    
    # Test 4: List Endpoints
    print("4. Testing List Endpoints...")
    test_list_endpoints()
    print()
    
    # Test 5: Document Downloads
    print("5. Testing Document Downloads...")
    test_document_download(plan_id, scheme_id)
    print()
    
    print("=" * 60)
    print("✅ System Test Complete!")
    print("=" * 60)
    print()
    print("🌐 Frontend: http://localhost:5173")
    print("🔧 API Docs: http://localhost:8000/docs")
    print("💾 Health: http://localhost:8000/health")

if __name__ == "__main__":
    main()