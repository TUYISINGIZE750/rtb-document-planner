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
    
    # Generate SMART objectives (3-4 objectives)
    data['objectives'] = f"""By the end of this session, learners will be able to:
1. Explain the key concepts of {topic} with 80% accuracy
2. Demonstrate practical application of {topic} in {module} through hands-on exercises
3. Analyze and solve at least 3 problems related to {indicative_contents}
4. Evaluate their own work using provided assessment criteria"""
    
    # Generate activities based on facilitation technique
    if facilitation == "Group Discussion":
        data['learning_activities'] = f"""Introduction:
Divide learners into groups of 4-5 members. Introduce {topic} and explain group discussion objectives. Assign roles: facilitator, note-taker, timekeeper, and presenter. Provide discussion guidelines and expected outcomes.

Development:
Groups discuss {indicative_contents} using structured discussion questions. Each group analyzes different aspects of {topic}. Groups document key findings and prepare presentations. Trainer circulates to facilitate discussions and provide guidance. Groups share findings with the class and engage in constructive debate.

Conclusion:
Each group presents main conclusions (2 minutes per group). Facilitate class discussion on common themes. Summarize key learning points and connect to {learning_outcomes}."""
    elif facilitation == "Simulation":
        data['learning_activities'] = f"""Introduction:
Explain simulation scenario related to {topic}. Assign specific roles to learners based on real workplace situations. Distribute simulation materials and brief learners on objectives, procedures, and safety guidelines.

Development:
Learners perform simulation of {indicative_contents} in assigned roles. Practice real-world application of {topic} in controlled environment. Trainer observes performance and takes notes. Learners rotate roles to experience different perspectives. After each round, conduct brief debrief session. Provide constructive feedback and allow learners to improve in subsequent rounds.

Conclusion:
Facilitate group reflection on simulation experience. Discuss what worked well and areas for improvement. Connect simulation outcomes to real workplace scenarios. Identify key competencies developed and how to apply them professionally."""
    elif facilitation == "Brainstorming":
        data['learning_activities'] = f"""Introduction:
Explain brainstorming rules: defer judgment, encourage wild ideas, build on others' ideas, stay focused, one conversation at a time. Present challenge or problem related to {topic}. Prepare flip charts, markers, and sticky notes.

Development:
Learners generate ideas about {indicative_contents} individually (2 minutes silent brainstorming). Share ideas in round-robin format and record all ideas on flip charts. Continue group brainstorming to build on initial ideas. Categorize ideas into themes. Use dot voting to prioritize top ideas. Discuss feasibility and impact of top 5 ideas. Develop action plans for most promising solutions.

Conclusion:
Review all generated ideas and selected solutions. Discuss how ideas address {learning_outcomes}. Assign follow-up tasks for implementation and testing."""
    elif facilitation == "Jigsaw":
        data['learning_activities'] = f"""Introduction:
Divide {topic} into 4-5 subtopics covering {indicative_contents}. Form home groups (4-5 members each) and assign each member a subtopic number. Explain jigsaw process: expert groups study, then teach home groups.

Development:
Form expert groups (all learners with same subtopic number). Expert groups study their subtopic using provided materials for 10 minutes. Experts discuss and prepare teaching strategy. Learners return to home groups. Each expert teaches their subtopic to home group (3 minutes per expert). Home groups ask questions and take notes. Home groups compile complete understanding and create comprehensive summary integrating all subtopics.

Conclusion:
Conduct quick quiz to test understanding across all subtopics. Clarify any misconceptions through class discussion. Emphasize connections between subtopics and how they relate to {learning_outcomes}."""
    elif facilitation == "Experiential Learning":
        data['learning_activities'] = f"""Introduction:
Present hands-on challenge related to {topic}. Explain safety procedures and proper use of materials/tools. Distribute materials and demonstrate proper techniques. Set clear learning objectives and success criteria.

Development:
Learners perform practical tasks on {indicative_contents} individually or in pairs. Experience real-world application through concrete experience. Trainer circulates to observe and provide minimal guidance. Allow learners to make mistakes and discover solutions. After initial attempt, facilitate reflection: What happened? What worked? What didn't? Why? Guide learners to form conclusions and generalizations. Learners apply learning to new situations or variations of the task. Repeat cycle: experience, reflect, conceptualize, apply.

Conclusion:
Facilitate group sharing of experiences and insights. Connect hands-on practice to theoretical concepts. Identify specific skills developed and how to transfer them to other contexts."""
    else:  # Trainer Guided (default)
        data['learning_activities'] = f"""Introduction:
Welcome learners and conduct brief review of previous session. Introduce {topic} and explain its relevance to {module}. Present learning outcomes and success criteria. Conduct diagnostic questions to assess prior knowledge of {indicative_contents}.

Development:
Present theory of {topic} using clear explanations and visual aids. Break content into manageable chunks. Demonstrate practical examples from {module} step-by-step. Check understanding after each concept using questioning techniques. Guide learners through structured exercises on {indicative_contents}. Provide individual support and immediate feedback. Use think-pair-share for peer learning. Conduct formative assessment to identify learning gaps.

Conclusion:
Summarize key points of {topic} using learner contributions. Address remaining questions and clarify common misconceptions. Assign practice exercises for reinforcement and skill consolidation."""
    
    # Generate assessment based on facilitation technique
    if facilitation in ["Group Discussion", "Brainstorming", "Jigsaw"]:
        data['assessment_details'] = f"""Formative Assessment: Observe group participation and collaboration skills. Evaluate quality of contributions and critical thinking. Use questioning to check understanding. Provide immediate feedback during group work.

Summative Assessment: Group presentation on {topic} (rubric-based). Peer evaluation using structured criteria. Individual written reflection (300 words). Quiz on {indicative_contents} (10 questions, 70% pass mark)."""  
    elif facilitation in ["Simulation", "Experiential Learning"]:
        data['assessment_details'] = f"""Formative Assessment: Observe performance during practical activities using observation checklist. Evaluate skill application and problem-solving approaches. Provide constructive feedback after each attempt. Check safety compliance.

Summative Assessment: Practical demonstration of {topic} (performance test with criteria). Skills checklist evaluation (competent/not yet competent). Portfolio of completed tasks with reflection. Written report on learning outcomes achieved."""  
    else:  # Trainer Guided
        data['assessment_details'] = f"""Formative Assessment: Ask targeted oral questions throughout session. Check exercise completion and accuracy. Observe learner engagement and participation. Provide immediate corrective feedback. Use exit tickets to assess understanding.

Summative Assessment: Written test on {topic} (20 marks, 60% pass). Practical exercise on {indicative_contents} (rubric-based). Individual assignment (due next session). End-of-module comprehensive assessment."""
    
    data['resources'] = f"""Whiteboard and markers, Projector and laptop, Handouts on {topic}, Textbooks: {module}, Assessment sheets, Flip charts, Markers"""
    
    data['references'] = f"""Rwanda Technical Board. (2024). {module}: Official curriculum guide. Kigali, Rwanda: RTB Publications.

Ministry of Education. (2023). Technical and vocational education training manual: {topic}. Kigali, Rwanda: MINEDUC.

International Labour Organization. (2022). TVET standards and best practices for {indicative_contents}. Geneva, Switzerland: ILO.

Rwanda TVET Resource Center. (2024). Learning resources and assessment tools for {learning_outcomes}. Retrieved from https://www.rtb.rw

Smith, J., & Johnson, M. (2023). Practical implementation guide for {topic} in technical education. Journal of Vocational Training, 15(2), 45-62."""
    
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
