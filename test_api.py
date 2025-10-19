import requests
import json

# Test API connection
api_base = "http://localhost:8000"

print("Testing RTB Document Planner API...")

# Test health
try:
    response = requests.get(f"{api_base}/health")
    print(f"Health: {response.json()}")
except Exception as e:
    print(f"Health check failed: {e}")

# Test session plans list
try:
    response = requests.get(f"{api_base}/session-plans/")
    plans = response.json()
    print(f"Session plans: {len(plans)} found")
except Exception as e:
    print(f"Session plans list failed: {e}")

# Create a test session plan
test_plan = {
    "sector": "ICT & MULTIMEDIA",
    "trade": "Software Development", 
    "topic_of_session": "Test Session",
    "trainer_name": "Test Trainer"
}

try:
    response = requests.post(
        f"{api_base}/session-plans/",
        headers={"Content-Type": "application/json"},
        json=test_plan
    )
    if response.status_code == 200:
        plan = response.json()
        print(f"Created session plan with ID: {plan['id']}")
        
        # Test list again
        response = requests.get(f"{api_base}/session-plans/")
        plans = response.json()
        print(f"Session plans after creation: {len(plans)} found")
    else:
        print(f"Failed to create session plan: {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"Create session plan failed: {e}")