"""Test AI Content Generation"""
import requests
import json

GEMINI_API_KEY = 'AIzaSyDuEdAygLcQ4aEuq2Vqj-9Kl0qZpJcg3A8'

url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

prompt = """Generate a session plan for:
Module: Computer Systems
Topic: Operating Systems
Learning Outcomes: Identify OS types

Provide JSON with keys: objectives, facilitation_techniques, learning_activities, resources, assessment_details, references"""

payload = {
    "contents": [{
        "parts": [{"text": prompt}]
    }],
    "generationConfig": {
        "temperature": 0.7,
        "maxOutputTokens": 2048
    }
}

try:
    response = requests.post(url, json=payload, timeout=30)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        result = response.json()
        text = result['candidates'][0]['content']['parts'][0]['text']
        print(f"\nAI Response:\n{text}")
    else:
        print(f"Error: {response.text}")
except Exception as e:
    print(f"Error: {e}")
