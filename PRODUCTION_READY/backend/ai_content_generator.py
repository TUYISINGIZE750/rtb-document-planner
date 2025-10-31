"""AI Content Generator using Google Gemini API"""
import os
import requests
import json

# Get API key - Replace with your actual key
GEMINI_API_KEY = 'AIzaSyDuEdAygLcQ4aEuq2Vqj-9Kl0qZpJcg3A8'

def generate_session_plan_content(data):
    """Generate enhanced session plan content"""
    import logging
    logger = logging.getLogger(__name__)
    
    module = data.get('module_code_title', '')
    topic = data.get('topic_of_session', '')
    learning_outcomes = data.get('learning_outcomes', '')
    indicative_contents = data.get('indicative_contents', '')
    duration = data.get('duration', '45 minutes')
    facilitation = data.get('facilitation_techniques', '')
    
    logger.info(f"Generating content for: {topic}")
    
    # Generate rich content based on input
    data['objectives'] = f"""By the end of this session, learners will be able to:
1. Understand the concept and purpose of {topic}
2. Apply {topic} in practical scenarios related to {module}
3. Demonstrate proficiency in {learning_outcomes}
4. Analyze and solve problems using {topic}
5. Evaluate the effectiveness of different approaches to {topic}"""
    
    # Generate activities based on facilitation technique
    if facilitation == "Group Discussion":
        data['learning_activities'] = f"""Introduction:
Divide learners into groups of 4-5 members. Introduce the topic "{topic}" and explain group discussion rules. Assign roles: facilitator, note-taker, and presenter.

Development:
Groups discuss {indicative_contents}. Each group analyzes different aspects of {topic}. Groups share findings and debate key points. Trainer facilitates inter-group discussions and guides learning process.

Conclusion:
Each group presents main conclusions. Class votes on best solutions. Trainer summarizes key learning points and connects to learning outcomes."""
    elif facilitation == "Simulation":
        data['learning_activities'] = f"""Introduction:
Explain simulation scenario for {topic}. Assign roles to learners and distribute simulation materials. Brief learners on expected outcomes and safety procedures.

Development:
Learners perform simulation of {indicative_contents}. Practice real-world application of {topic}. Trainer observes and provides guidance. Learners rotate roles and repeat simulation with feedback.

Conclusion:
Discuss simulation experience and lessons learned. Connect simulation to real workplace scenarios. Identify key competencies developed."""
    elif facilitation == "Brainstorming":
        data['learning_activities'] = f"""Introduction:
Explain brainstorming rules (no criticism, quantity over quality). Present challenge related to {topic}. Prepare flip charts and markers.

Development:
Learners generate ideas about {indicative_contents}. Record all ideas on flip charts. Categorize and prioritize ideas. Discuss feasibility of top ideas and develop action plans.

Conclusion:
Review all generated ideas. Select most innovative solutions. Assign follow-up tasks for implementation."""
    elif facilitation == "Jigsaw":
        data['learning_activities'] = f"""Introduction:
Divide {topic} into subtopics. Form home groups and expert groups. Assign each learner a subtopic and explain jigsaw process.

Development:
Expert groups study their subtopic of {indicative_contents}. Experts return to home groups and teach their subtopic. Home groups compile complete understanding and create comprehensive summaries.

Conclusion:
Test understanding across all subtopics. Clarify any misconceptions. Emphasize connections between subtopics."""
    elif facilitation == "Experiential Learning":
        data['learning_activities'] = f"""Introduction:
Present hands-on challenge: {topic}. Explain safety procedures. Distribute materials and tools. Set clear learning objectives.

Development:
Learners perform practical tasks on {indicative_contents}. Experience real-world application. Make mistakes and learn from them. Reflect on experience and apply learning to new situations.

Conclusion:
Share experiences and insights. Connect practice to theory. Identify skills developed through hands-on practice."""
    else:  # Trainer Guided (default)
        data['learning_activities'] = f"""Introduction:
Welcome learners and introduce {topic}. Review previous knowledge of {indicative_contents}. Explain learning outcomes and demonstrate key concepts.

Development:
Present theory of {topic} step-by-step. Demonstrate practical examples from {module}. Guide learners through exercises on {indicative_contents}. Provide individual support and check understanding regularly.

Conclusion:
Summarize key points of {topic}. Answer questions and clarify doubts. Assign practice exercises for reinforcement."""
    
    # Generate assessment based on facilitation technique
    if facilitation in ["Group Discussion", "Brainstorming", "Jigsaw"]:
        data['assessment_details'] = f"""Formative: Observe group participation, evaluate discussion quality, check individual contributions, assess teamwork skills.

Summative: Group presentation on {topic}, peer evaluation, written reflection, individual quiz on {indicative_contents}."""  
    elif facilitation in ["Simulation", "Experiential Learning"]:
        data['assessment_details'] = f"""Formative: Observe performance during activities, check skill application, evaluate problem-solving, provide feedback during practice.

Summative: Practical demonstration of {topic}, performance test, portfolio of completed tasks, skills checklist evaluation."""  
    else:  # Trainer Guided
        data['assessment_details'] = f"""Formative: Ask oral questions during session, check exercises, observe learner engagement, provide immediate feedback.

Summative: Written test on {topic}, practical exercise on {indicative_contents}, individual assignment, end-of-module assessment."""
    
    data['resources'] = f"""Whiteboard and markers
Projector and laptop
Handouts on {topic}
Textbooks on {module}
Assessment sheets"""
    
    data['references'] = f"""1. {module} - Official Curriculum Guide, Rwanda Technical Board
2. Technical and Vocational Education Training Manual - {topic}
3. Practical Guide to {indicative_contents}
4. Online Resources: www.rtb.rw and related educational platforms
5. Industry Standards and Best Practices for {topic}"""
    
    logger.info(f"Content generated successfully")
    return data
    
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
        import logging
        logger = logging.getLogger(__name__)
        
        url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.0-flash-exp:generateContent?key={GEMINI_API_KEY}"
        
        payload = {
            "contents": [{
                "parts": [{"text": prompt}]
            }],
            "generationConfig": {
                "temperature": 0.7,
                "maxOutputTokens": 2048,
                "responseMimeType": "application/json"
            }
        }
        
        logger.info("Calling Gemini API...")
        response = requests.post(url, json=payload, timeout=30)
        logger.info(f"API Response status: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            text = result['candidates'][0]['content']['parts'][0]['text']
            logger.info(f"AI response length: {len(text)} chars")
            
            # Parse JSON response
            ai_content = json.loads(text)
            
            # Update data with AI-generated content
            data['objectives'] = ai_content.get('objectives', data.get('objectives', ''))
            data['facilitation_techniques'] = ai_content.get('facilitation_techniques', data.get('facilitation_techniques', ''))
            data['learning_activities'] = ai_content.get('learning_activities', data.get('learning_activities', ''))
            data['resources'] = ai_content.get('resources', data.get('resources', ''))
            data['assessment_details'] = ai_content.get('assessment_details', data.get('assessment_details', ''))
            data['references'] = ai_content.get('references', data.get('references', ''))
            
            logger.info(f"AI content applied: objectives={len(data['objectives'])} chars")
            return data
        else:
            logger.error(f"AI API failed: {response.status_code} - {response.text[:200]}")
            return data
            
    except Exception as e:
        import logging
        logger = logging.getLogger(__name__)
        logger.error(f"AI generation error: {str(e)}")
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
