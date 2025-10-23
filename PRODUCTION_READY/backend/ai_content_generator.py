"""
AI-Powered Content Generator for RTB Session Plans
Generates SMART objectives and facilitation-specific activities based on user input
"""

def generate_smart_objectives(topic, learning_outcomes, duration, rqf_level, module_name="", range_content=""):
    """
    Generate professional SMART objectives based on educational best practices
    """
    duration_minutes = int(duration) if str(duration).isdigit() else 40
    
    # Bloom's Taxonomy action verbs by RQF level
    verbs = {
        "Level 1": ["identify", "list", "describe", "recognize", "recall"],
        "Level 2": ["explain", "demonstrate", "illustrate", "summarize", "interpret"],
        "Level 3": ["apply", "implement", "execute", "solve", "use"],
        "Level 4": ["analyze", "compare", "evaluate", "critique", "design"],
        "Level 5": ["create", "synthesize", "formulate", "design", "construct"]
    }.get(rqf_level, ["apply", "demonstrate", "solve", "construct"])
    
    # Extract key learning outcome
    outcome_text = learning_outcomes.split('.')[0].strip() if learning_outcomes else f"the key concepts of {topic}"
    
    objectives = []
    
    # Objective 1: Specific & Measurable
    objectives.append(
        f"By the end of this {duration_minutes}-minute session, trainees will be able to {verbs[0]} "
        f"{outcome_text.lower()}, achieving at least 80% accuracy in assessment tasks."
    )
    
    # Objective 2: Achievable & Relevant
    if range_content:
        objectives.append(
            f"Trainees will successfully {verbs[1]} {topic} concepts including {range_content[:100]}..., "
            f"meeting {rqf_level} competency standards."
        )
    else:
        objectives.append(
            f"Trainees will successfully {verbs[1]} practical applications of {topic}, "
            f"demonstrating {rqf_level} competency standards."
        )
    
    # Objective 3: Application-focused
    if len(verbs) > 2:
        objectives.append(
            f"Trainees will {verbs[2]} real-world scenarios related to {topic}, "
            f"demonstrating critical thinking and professional problem-solving skills."
        )
    
    # Objective 4: Higher-order thinking (for advanced levels)
    if rqf_level in ["Level 4", "Level 5"] and len(verbs) > 3:
        objectives.append(
            f"Trainees will {verbs[3]} innovative solutions for {topic} challenges, "
            f"showing advanced understanding and professional judgment."
        )
    
    return "\n".join([f"• {obj}" for obj in objectives])


def generate_facilitation_activities(technique, topic, duration, number_of_trainees):
    """
    Generate specific activities and steps based on the selected facilitation technique
    Each technique has its own structured format and activities
    """
    
    duration_minutes = int(duration) if str(duration).isdigit() else 40
    num_trainees = int(number_of_trainees) if str(number_of_trainees).isdigit() else 25
    
    # Calculate time allocations
    intro_time = max(5, duration_minutes // 8)
    main_time = duration_minutes - intro_time - 10
    conclusion_time = 10
    
    activities = {
        "Brainstorming": f"""
BRAINSTORMING SESSION STRUCTURE:

1. INTRODUCTION ({intro_time} minutes)
   • Introduce the topic: {topic}
   • Explain brainstorming rules: No criticism, encourage wild ideas, build on others' ideas
   • Set the challenge/question clearly
   • Divide trainees into groups of 4-5 ({num_trainees // 5} groups)

2. IDEA GENERATION PHASE ({main_time // 2} minutes)
   • Each group generates as many ideas as possible about {topic}
   • Trainer circulates to facilitate and encourage participation
   • Use sticky notes or flip charts for idea capture
   • Encourage quantity over quality at this stage

3. IDEA CLUSTERING & REFINEMENT ({main_time // 2} minutes)
   • Groups organize ideas into themes/categories
   • Identify most promising or innovative ideas
   • Combine similar ideas and eliminate duplicates
   • Prioritize top 3-5 ideas per group

4. PRESENTATION & DISCUSSION ({conclusion_time} minutes)
   • Each group presents their top ideas (2 min per group)
   • Class discussion on feasibility and application
   • Trainer summarizes key insights and connections to {topic}
   • Document final ideas for future reference

RESOURCES NEEDED:
• Flip charts or whiteboards
• Sticky notes (multiple colors)
• Markers
• Timer for time management
""",

        "Trainer Guided": f"""
TRAINER-GUIDED INSTRUCTION STRUCTURE:

1. INTRODUCTION & HOOK ({intro_time} minutes)
   • Gain attention with real-world example related to {topic}
   • State learning objectives clearly
   • Connect to prior knowledge
   • Outline session structure

2. DIRECT INSTRUCTION ({main_time // 3} minutes)
   • Present core concepts of {topic} systematically
   • Use visual aids (slides, diagrams, demonstrations)
   • Explain step-by-step procedures
   • Provide clear examples and non-examples
   • Check for understanding through questioning

3. GUIDED PRACTICE ({main_time // 3} minutes)
   • Trainer demonstrates while trainees follow along
   • Work through examples together as a class
   • Provide immediate feedback and correction
   • Gradually increase complexity
   • Address common misconceptions

4. INDEPENDENT PRACTICE ({main_time // 3} minutes)
   • Trainees work on {topic} tasks individually or in pairs
   • Trainer circulates to provide support
   • Monitor progress and provide individual assistance
   • Identify trainees needing additional help

5. CLOSURE & ASSESSMENT ({conclusion_time} minutes)
   • Review key points of {topic}
   • Quick formative assessment (quiz, Q&A, exit ticket)
   • Preview next session
   • Assign homework or practice tasks

RESOURCES NEEDED:
• Presentation slides or visual materials
• Handouts with examples and practice problems
• Assessment tools (quiz, worksheet)
• Demonstration equipment/materials
""",

        "Group Discussion": f"""
GROUP DISCUSSION FACILITATION STRUCTURE:

1. PREPARATION & GROUPING ({intro_time} minutes)
   • Introduce discussion topic: {topic}
   • Establish ground rules (respect, active listening, equal participation)
   • Divide class into groups of 5-6 ({num_trainees // 6} groups)
   • Assign roles: Facilitator, Timekeeper, Note-taker, Reporter
   • Distribute discussion prompts/questions

2. SMALL GROUP DISCUSSIONS ({main_time // 2} minutes)
   • Groups discuss assigned aspects of {topic}
   • Each member contributes perspectives and experiences
   • Note-taker records key points and insights
   • Facilitator ensures everyone participates
   • Trainer moves between groups, listening and prompting

3. INTER-GROUP EXCHANGE ({main_time // 4} minutes)
   • Groups rotate members to share ideas (Jigsaw style)
   • Cross-pollination of ideas between groups
   • Identify common themes and unique perspectives
   • Build on each other's insights

4. WHOLE CLASS SYNTHESIS ({main_time // 4} minutes)
   • Each group reports key findings (2-3 min per group)
   • Trainer facilitates connections between group insights
   • Highlight diverse viewpoints on {topic}
   • Address any misconceptions or gaps

5. REFLECTION & APPLICATION ({conclusion_time} minutes)
   • Individual reflection: What did you learn about {topic}?
   • Discuss practical applications
   • Identify areas for further exploration
   • Summarize consensus and action points

RESOURCES NEEDED:
• Discussion prompt cards
• Flip charts for group notes
• Role assignment cards
• Reflection worksheets
""",

        "Simulation": f"""
SIMULATION-BASED LEARNING STRUCTURE:

1. BRIEFING & CONTEXT SETTING ({intro_time} minutes)
   • Explain the simulation scenario related to {topic}
   • Clarify learning objectives and expected outcomes
   • Describe roles, rules, and procedures
   • Distribute role cards and materials
   • Answer questions about the simulation

2. SIMULATION SETUP ({5} minutes)
   • Organize physical space for simulation
   • Assign roles to trainees ({num_trainees} participants)
   • Distribute necessary materials and resources
   • Ensure everyone understands their role

3. SIMULATION EXECUTION ({main_time - 5} minutes)
   • Trainees engage in the {topic} simulation
   • Trainer observes and takes notes on performance
   • Allow realistic challenges and problem-solving
   • Minimal intervention unless safety/learning at risk
   • Document key moments and decisions

4. DEBRIEFING & ANALYSIS ({conclusion_time + 5} minutes)
   • Participants share experiences and feelings
   • Analyze what happened and why
   • Connect simulation to real-world {topic} applications
   • Identify successful strategies and areas for improvement
   • Extract key lessons learned
   • Relate back to learning objectives

RESOURCES NEEDED:
• Simulation scenario materials
• Role cards and instructions
• Props or equipment for realism
• Observation checklist for trainer
• Debriefing guide
""",

        "Experiential Learning": f"""
EXPERIENTIAL LEARNING CYCLE STRUCTURE:

1. CONCRETE EXPERIENCE ({main_time // 3} minutes)
   • Trainees engage in hands-on activity related to {topic}
   • Provide authentic, real-world task or problem
   • Allow trainees to experience directly (not just observe)
   • Minimal initial instruction - learning through doing
   • Organize in pairs or small groups for collaboration

2. REFLECTIVE OBSERVATION ({main_time // 4} minutes)
   • Pause the activity for reflection
   • Guided questions: What happened? What did you notice?
   • Trainees share observations and experiences
   • Identify patterns, challenges, and surprises
   • Document insights individually or in groups

3. ABSTRACT CONCEPTUALIZATION ({main_time // 4} minutes)
   • Connect experience to theoretical concepts of {topic}
   • Trainer introduces relevant principles and frameworks
   • Trainees develop generalizations and theories
   • Link personal experience to broader knowledge
   • Create mental models and understanding

4. ACTIVE EXPERIMENTATION ({main_time // 6} minutes)
   • Apply new understanding to modified task
   • Test theories and approaches
   • Experiment with different strategies
   • Immediate feedback on application

5. INTEGRATION & TRANSFER ({intro_time + conclusion_time} minutes)
   • Discuss how learning applies beyond classroom
   • Identify real-world applications of {topic}
   • Create action plans for continued practice
   • Reflect on learning process itself

RESOURCES NEEDED:
• Hands-on materials and equipment
• Reflection journals or worksheets
• Theoretical resources (handouts, references)
• Space for active experimentation
""",

        "Jigsaw": f"""
JIGSAW COOPERATIVE LEARNING STRUCTURE:

1. INTRODUCTION & TOPIC DIVISION ({intro_time} minutes)
   • Introduce overall topic: {topic}
   • Divide {topic} into 4-5 subtopics
   • Explain Jigsaw process and expectations
   • Form home groups of 4-5 trainees ({num_trainees // 5} groups)
   • Assign each member a subtopic number

2. EXPERT GROUP PHASE ({main_time // 2} minutes)
   • Trainees with same subtopic form expert groups
   • Each expert group studies their assigned subtopic in depth
   • Use provided resources (texts, videos, materials)
   • Discuss and master the content together
   • Prepare to teach others clearly and effectively
   • Create teaching aids or summaries

3. HOME GROUP TEACHING ({main_time // 2} minutes)
   • Return to original home groups
   • Each expert teaches their subtopic (equal time per person)
   • Home group members take notes and ask questions
   • Ensure everyone understands all subtopics
   • Build complete picture of {topic} together

4. ASSESSMENT & SYNTHESIS ({conclusion_time} minutes)
   • Individual quiz covering all subtopics
   • Group creates concept map connecting all parts of {topic}
   • Whole class discussion on how subtopics integrate
   • Trainer clarifies misconceptions and emphasizes connections

RESOURCES NEEDED:
• Subtopic resource packets (one per subtopic)
• Expert group worksheets
• Teaching planning templates
• Assessment quiz
• Concept mapping materials
"""
    }
    
    # Return the specific activity structure for the chosen technique
    return activities.get(technique, activities["Trainer Guided"])


def generate_assessment_methods(topic, rqf_level, facilitation_technique):
    """
    Generate appropriate assessment methods based on topic, level, and facilitation technique
    """
    
    # Assessment strategies based on RQF level
    level_assessments = {
        "Level 1": [
            "Formative: Oral questioning to check basic understanding",
            "Formative: Observation of practical tasks completion",
            "Summative: Written test with multiple choice and short answers",
            "Summative: Practical demonstration of basic skills"
        ],
        "Level 2": [
            "Formative: Think-pair-share activities",
            "Formative: Exit tickets summarizing key learning",
            "Summative: Practical assignment with clear criteria",
            "Summative: Short written report or presentation"
        ],
        "Level 3": [
            "Formative: Peer assessment of practical work",
            "Formative: Self-assessment using rubrics",
            "Summative: Project-based assessment",
            "Summative: Case study analysis and solution"
        ],
        "Level 4": [
            "Formative: Reflective journals on learning process",
            "Formative: Group critique and feedback sessions",
            "Summative: Research-based assignment",
            "Summative: Portfolio of evidence"
        ],
        "Level 5": [
            "Formative: Peer review of advanced work",
            "Formative: Professional discussion and viva",
            "Summative: Independent project or dissertation",
            "Summative: Professional portfolio with critical reflection"
        ]
    }
    
    assessments = level_assessments.get(rqf_level, level_assessments["Level 3"])
    
    # Add technique-specific assessment
    technique_assessment = {
        "Brainstorming": "• Formative: Quality and quantity of ideas generated\n• Formative: Participation in group discussions",
        "Trainer Guided": "• Formative: Responses to guided practice questions\n• Formative: Accuracy during demonstration",
        "Group Discussion": "• Formative: Quality of contributions to discussion\n• Formative: Peer evaluation of participation",
        "Simulation": "• Formative: Performance during simulation\n• Formative: Decision-making and problem-solving observed",
        "Experiential Learning": "• Formative: Reflection quality and depth\n• Formative: Application of concepts in practice",
        "Jigsaw": "• Formative: Teaching effectiveness in home group\n• Formative: Comprehension quiz on all subtopics"
    }
    
    result = technique_assessment.get(facilitation_technique, "• Formative: Observation and questioning")
    result += "\n" + "\n".join(assessments[:2])
    
    return result


def generate_resources_list(topic, facilitation_technique, number_of_trainees):
    """
    Generate comprehensive resources list based on topic and facilitation technique
    """
    
    num_trainees = int(number_of_trainees) if str(number_of_trainees).isdigit() else 25
    num_groups = max(4, num_trainees // 5)
    
    # Common resources for all techniques
    common_resources = [
        f"• Whiteboard/Smartboard for {topic} demonstrations",
        f"• Handouts with {topic} key concepts and examples",
        "• Projector and laptop for presentations",
        f"• Textbook/Reference materials on {topic}"
    ]
    
    # Technique-specific resources
    technique_resources = {
        "Brainstorming": [
            f"• {num_groups} flip charts with stands",
            f"• {num_trainees * 10} sticky notes (assorted colors)",
            f"• {num_groups} sets of markers",
            "• Timer or stopwatch",
            "• Camera to document ideas"
        ],
        "Trainer Guided": [
            f"• Demonstration materials for {topic}",
            f"• {num_trainees} practice worksheets",
            "• Step-by-step instruction guides",
            "• Assessment quiz (printed)",
            "• Multimedia resources (videos, animations)"
        ],
        "Group Discussion": [
            f"• {num_groups} discussion prompt cards",
            f"• {num_groups} flip charts for notes",
            f"• {num_groups} role assignment cards",
            f"• {num_trainees} reflection worksheets",
            "• Recording device (optional)"
        ],
        "Simulation": [
            f"• Simulation scenario materials for {topic}",
            f"• {num_trainees} role cards",
            "• Props and equipment for realism",
            "• Observation checklist",
            "• Debriefing guide",
            "• Video recording equipment (optional)"
        ],
        "Experiential Learning": [
            f"• Hands-on materials for {topic} activities",
            f"• {num_trainees} reflection journals",
            "• Safety equipment (if needed)",
            "• Theoretical resource handouts",
            "• Experimentation space and tools"
        ],
        "Jigsaw": [
            f"• {num_groups} expert group resource packets",
            f"• {num_trainees} note-taking templates",
            "• Teaching planning worksheets",
            f"• Assessment quiz on {topic}",
            "• Concept mapping materials"
        ]
    }
    
    specific = technique_resources.get(facilitation_technique, technique_resources["Trainer Guided"])
    
    return "\n".join(common_resources + specific)


def enhance_session_plan_data(data):
    """
    Professional AI enhancement: Generate comprehensive, contextually-rich session plan content
    """
    topic = data.get('topic_of_session', 'the topic')
    learning_outcomes = data.get('learning_outcomes', '')
    duration = data.get('duration', '40')
    rqf_level = data.get('rqf_level', 'Level 3')
    module_name = data.get('module_code_title', '')
    range_content = data.get('indicative_contents', '')
    facilitation_technique = data.get('facilitation_techniques', 'Trainer Guided')
    number_of_trainees = data.get('number_of_trainees', '25')
    
    # Generate professional SMART objectives
    if not data.get('objectives') or len(data.get('objectives', '')) < 50:
        data['objectives'] = generate_smart_objectives(
            topic, learning_outcomes, duration, rqf_level, module_name, range_content
        )
    
    # Generate comprehensive facilitation-specific activities
    if facilitation_technique and facilitation_technique != '':
        data['learning_activities'] = generate_facilitation_activities(
            facilitation_technique, topic, duration, number_of_trainees
        )
    
    # Generate RQF level-appropriate assessment
    if not data.get('assessment_details') or len(data.get('assessment_details', '')) < 30:
        data['assessment_details'] = generate_assessment_methods(
            topic, rqf_level, facilitation_technique
        )
    
    # Generate comprehensive resources list
    if not data.get('resources') or len(data.get('resources', '')) < 30:
        data['resources'] = generate_resources_list(
            topic, facilitation_technique, number_of_trainees
        )
    
    return data
