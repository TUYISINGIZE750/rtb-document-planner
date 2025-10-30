"""AI Content Generator using Google Gemini API"""
import os
import requests
import json

# Get API key - Replace with your actual key
GEMINI_API_KEY = 'AIzaSyDuEdAygLcQ4aEuq2Vqj-9Kl0qZpJcg3A8'

def generate_session_plan_content(data):
    """Generate enhanced session plan content using AI"""
    
    # If no API key, return original data
    if not GEMINI_API_KEY:
        print("⚠️ No API key found, returning original data")
        return data
    
    print(f"🤖 Starting AI content generation for: {data.get('topic_of_session', 'Unknown topic')}")
    
    module = data.get('module_code_title', '')
    topic = data.get('topic_of_session', '')
    learning_outcomes = data.get('learning_outcomes', '')
    indicative_contents = data.get('indicative_contents', '')
    duration = data.get('duration', '45 minutes')
    facilitation = data.get('facilitation_techniques', '')
    
    prompt = f"""You are an expert TVET (Technical and Vocational Education and Training) curriculum developer for Rwanda Technical Board (RTB).

Generate a detailed, professional session plan with the following information:

Module: {module}
Topic: {topic}
Learning Outcomes: {learning_outcomes}
Indicative Contents: {indicative_contents}
Duration: {duration}
Facilitation Technique: {facilitation}

IMPORTANT: Use ONLY the facilitation technique "{facilitation}" throughout the session. Design all activities specifically for this technique.

Please provide:

1. OBJECTIVES (3-5 specific, measurable objectives that align with the learning outcomes)
2. FACILITATION TECHNIQUES (Keep as: {facilitation})
3. LEARNING ACTIVITIES (Design activities specifically for {facilitation} technique):
   - Introduction (5 minutes): How to start using {facilitation} method
   - Development (main activity): Detailed step-by-step {facilitation} activities
   - Conclusion (3 minutes): How to conclude using {facilitation}
4. RESOURCES (Materials needed for {facilitation} activities)
5. ASSESSMENT DETAILS (How to assess learning during {facilitation} activities)
6. REFERENCES (3-5 relevant textbooks, manuals, online resources related to this topic)

Format your response as JSON with these exact keys:
{{
  "objectives": "string",
  "facilitation_techniques": "string",
  "learning_activities": "string (use \\n\\n to separate introduction and development)",
  "resources": "string (one per line)",
  "assessment_details": "string",
  "references": "string (one per line)"
}}

Make it professional, practical, and suitable for TVET training in Rwanda."""

    try:
        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"
        
        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }],
            "generationConfig": {
                "temperature": 0.7,
                "maxOutputTokens": 2048
            }
        }
        
        response = requests.post(url, json=payload, timeout=30)
        
        print(f"📡 API Response status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            text = result['candidates'][0]['content']['parts'][0]['text']
            print(f"✅ AI response received, length: {len(text)} chars")
            
            # Extract JSON from response
            if '```json' in text:
                text = text.split('```json')[1].split('```')[0].strip()
            elif '```' in text:
                text = text.split('```')[1].split('```')[0].strip()
            
            ai_content = json.loads(text)
            print(f"✅ AI content parsed successfully")
            print(f"📊 Generated objectives: {len(ai_content.get('objectives', ''))} chars")
            print(f"📊 Generated activities: {len(ai_content.get('learning_activities', ''))} chars")
            print(f"📊 Generated assessment: {len(ai_content.get('assessment_details', ''))} chars")
            
            # Update data with AI-generated content
            data['objectives'] = ai_content.get('objectives', data.get('objectives', ''))
            data['facilitation_techniques'] = ai_content.get('facilitation_techniques', data.get('facilitation_techniques', ''))
            data['learning_activities'] = ai_content.get('learning_activities', data.get('learning_activities', ''))
            data['resources'] = ai_content.get('resources', data.get('resources', ''))
            data['assessment_details'] = ai_content.get('assessment_details', data.get('assessment_details', ''))
            data['references'] = ai_content.get('references', data.get('references', ''))
            
            print(f"✅ Data updated with AI content")
            return data
        else:
            print(f"❌ AI API failed with status: {response.status_code}")
            print(f"❌ Response: {response.text[:200]}")
            # If AI fails, return original data
            return data
            
    except Exception as e:
        print(f"AI generation error: {e}")
        print(f"Response status: {response.status_code if 'response' in locals() else 'No response'}")
        print(f"Response text: {response.text if 'response' in locals() else 'No response'}")
        # If AI fails, return original data
        return data

def generate_scheme_content(data):
    """Generate enhanced scheme of work content using AI"""
    
    # If no API key, return original data
    if not GEMINI_API_KEY:
        return data
    
    module = data.get('module_code_title', '')
    qualification = data.get('qualification_title', '')
    
    # For now, return original data (scheme generation is more complex)
    # Can be enhanced later if needed
    return data
