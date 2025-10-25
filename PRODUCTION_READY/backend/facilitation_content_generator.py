"""Generate session plan content based on facilitation technique"""

def generate_introduction_activities(topic, facilitation_technique):
    """Generate introduction based on facilitation technique"""
    base = f"""Trainer's activity: 
\t• Greets and makes roll call
\t• Involves learners to set ground rules
\t• Involves learners to review previous session
\t• Announces topic: {topic}"""
    
    technique_lower = facilitation_technique.lower()
    
    if 'trainer-guided' in technique_lower or 'demonstration' in technique_lower:
        return base + """
\t• Explains objectives and demonstrates key concepts
\t• Shows examples and models the process

Learner's activity: 
\t• Greets and replies to roll call
\t• Participates in setting ground rules
\t• Observes demonstration attentively
\t• Takes notes on key points
\t• Asks clarifications if any"""
    
    elif 'simulation' in technique_lower or 'role-play' in technique_lower:
        return base + """
\t• Explains objectives and simulation scenario
\t• Assigns roles and sets up simulation environment
\t• Provides guidelines for the activity

Learner's activity: 
\t• Greets and replies to roll call
\t• Participates in setting ground rules
\t• Understands assigned roles
\t• Prepares for simulation activity
\t• Asks clarifications if any"""
    
    elif 'group work' in technique_lower or 'collaborative' in technique_lower:
        return base + """
\t• Explains objectives and group work instructions
\t• Divides learners into groups
\t• Assigns tasks to each group

Learner's activity: 
\t• Greets and replies to roll call
\t• Participates in setting ground rules
\t• Forms groups as instructed
\t• Understands group tasks
\t• Asks clarifications if any"""
    
    elif 'hands-on' in technique_lower or 'practical' in technique_lower:
        return base + """
\t• Explains objectives and practical exercise
\t• Demonstrates safety procedures
\t• Distributes materials and tools

Learner's activity: 
\t• Greets and replies to roll call
\t• Participates in setting ground rules
\t• Observes safety demonstration
\t• Collects materials
\t• Asks clarifications if any"""
    
    elif 'discussion' in technique_lower or 'brainstorming' in technique_lower:
        return base + """
\t• Explains objectives and discussion topics
\t• Poses thought-provoking questions
\t• Encourages participation

Learner's activity: 
\t• Greets and replies to roll call
\t• Participates in setting ground rules
\t• Prepares to share ideas
\t• Thinks about discussion questions
\t• Asks clarifications if any"""
    
    else:
        return base + """
\t• Explains objectives
\t• Provides overview of the session

Learner's activity: 
\t• Greets and replies to roll call
\t• Participates in setting ground rules
\t• Participates in review
\t• Reads and participates in explaining objectives
\t• Asks clarifications if any"""

def generate_development_activities(topic, facilitation_technique, learning_activities=None):
    """Generate development/body based on facilitation technique"""
    if learning_activities:
        return learning_activities
    
    technique_lower = facilitation_technique.lower()
    
    if 'trainer-guided' in technique_lower or 'demonstration' in technique_lower:
        return f"""Trainer's activity:
\t• Demonstrates {topic} step-by-step
\t• Explains each step clearly with examples
\t• Shows best practices and common mistakes to avoid
\t• Provides guided practice opportunities
\t• Monitors learner understanding
\t• Gives immediate feedback

Learner's activity:
\t• Observes demonstration carefully
\t• Takes notes on important steps
\t• Follows along with trainer's demonstration
\t• Practices under supervision
\t• Asks questions when unclear
\t• Applies learned concepts"""
    
    elif 'simulation' in technique_lower or 'role-play' in technique_lower:
        return f"""Trainer's activity:
\t• Sets up simulation scenario for {topic}
\t• Assigns roles to learners
\t• Monitors simulation progress
\t• Provides guidance when needed
\t• Facilitates debriefing after simulation
\t• Highlights key learning points

Learner's activity:
\t• Participates actively in simulation
\t• Performs assigned role realistically
\t• Interacts with other participants
\t• Applies knowledge to scenario
\t• Reflects on experience
\t• Shares observations and insights"""
    
    elif 'group work' in technique_lower or 'collaborative' in technique_lower:
        return f"""Trainer's activity:
\t• Assigns group tasks related to {topic}
\t• Provides resources and guidelines
\t• Circulates among groups to monitor progress
\t• Facilitates inter-group discussions
\t• Ensures all members participate
\t• Guides groups toward solutions

Learner's activity:
\t• Works collaboratively in assigned groups
\t• Shares ideas and knowledge with team
\t• Divides tasks among group members
\t• Researches and analyzes information
\t• Prepares group presentation
\t• Presents findings to class"""
    
    elif 'hands-on' in technique_lower or 'practical' in technique_lower:
        return f"""Trainer's activity:
\t• Provides practical exercises on {topic}
\t• Demonstrates proper techniques and safety
\t• Distributes tools and materials
\t• Supervises hands-on practice
\t• Provides individual assistance
\t• Ensures safety protocols are followed

Learner's activity:
\t• Performs hands-on practice
\t• Follows safety procedures
\t• Uses tools and equipment correctly
\t• Completes practical tasks
\t• Troubleshoots problems independently
\t• Seeks help when needed"""
    
    elif 'discussion' in technique_lower or 'brainstorming' in technique_lower:
        return f"""Trainer's activity:
\t• Facilitates discussion on {topic}
\t• Poses open-ended questions
\t• Encourages diverse viewpoints
\t• Records key points on board
\t• Guides discussion toward learning objectives
\t• Summarizes main ideas

Learner's activity:
\t• Participates actively in discussion
\t• Shares ideas and experiences
\t• Listens to others' perspectives
\t• Asks thoughtful questions
\t• Builds on others' contributions
\t• Takes notes on key insights"""
    
    elif 'project-based' in technique_lower:
        return f"""Trainer's activity:
\t• Introduces project on {topic}
\t• Explains project requirements and timeline
\t• Provides resources and support
\t• Monitors project progress
\t• Offers feedback and guidance
\t• Facilitates project presentations

Learner's activity:
\t• Plans project approach
\t• Conducts research on topic
\t• Develops project deliverables
\t• Collaborates with team members
\t• Solves problems creatively
\t• Presents completed project"""
    
    else:
        return f"""Trainer's activity:
\t• Presents content on {topic}
\t• Provides examples and explanations
\t• Engages learners with questions
\t• Monitors understanding
\t• Provides practice opportunities
\t• Gives feedback

Learner's activity:
\t• Listens and takes notes
\t• Participates in activities
\t• Practices new skills
\t• Asks questions
\t• Completes exercises
\t• Applies learning"""

def generate_resources(facilitation_technique, custom_resources=None):
    """Generate resources based on facilitation technique"""
    if custom_resources:
        return custom_resources
    
    technique_lower = facilitation_technique.lower()
    
    if 'trainer-guided' in technique_lower or 'demonstration' in technique_lower:
        return "Computer\nProjector\nPPT presentation\nDemonstration materials\nHandouts\nWhiteboard\nMarkers"
    
    elif 'simulation' in technique_lower or 'role-play' in technique_lower:
        return "Simulation materials\nRole cards\nScenario descriptions\nProps\nEvaluation forms\nVideo recording equipment"
    
    elif 'group work' in technique_lower or 'collaborative' in technique_lower:
        return "Flipcharts\nMarkers\nGroup task sheets\nReference materials\nComputers\nProjector\nPresentation materials"
    
    elif 'hands-on' in technique_lower or 'practical' in technique_lower:
        return "Tools and equipment\nSafety gear\nMaterials\nWorkbenches\nInstruction manuals\nSafety guidelines"
    
    elif 'discussion' in technique_lower or 'brainstorming' in technique_lower:
        return "Whiteboard\nMarkers\nDiscussion prompts\nReference materials\nNote-taking materials\nProjector"
    
    else:
        return "Computer\nProjector\nPPT\nHandouts\nWhiteboard\nMarkers"

def generate_assessment(topic, facilitation_technique, custom_assessment=None):
    """Generate assessment based on facilitation technique"""
    if custom_assessment:
        return f"Trainer's activity: \n\t{custom_assessment}\n\nLearner's activity:\n\tLearners receive assessment and answer questions"
    
    technique_lower = facilitation_technique.lower()
    
    if 'trainer-guided' in technique_lower or 'demonstration' in technique_lower:
        return f"""Trainer's activity: 
\t• Gives practical demonstration test on {topic}
\t• Observes learner performance
\t• Provides written quiz on key concepts
\t• Evaluates understanding

Learner's activity:
\t• Demonstrates learned skills
\t• Completes written assessment
\t• Answers questions accurately"""
    
    elif 'simulation' in technique_lower or 'role-play' in technique_lower:
        return f"""Trainer's activity: 
\t• Evaluates simulation performance on {topic}
\t• Assesses role-play effectiveness
\t• Reviews learner reflections
\t• Provides feedback

Learner's activity:
\t• Completes simulation assessment
\t• Writes reflection on experience
\t• Receives and reviews feedback"""
    
    elif 'group work' in technique_lower or 'collaborative' in technique_lower:
        return f"""Trainer's activity: 
\t• Evaluates group presentations on {topic}
\t• Assesses individual contributions
\t• Reviews group deliverables
\t• Provides peer evaluation forms

Learner's activity:
\t• Presents group work
\t• Completes peer evaluations
\t• Submits individual reflections"""
    
    elif 'hands-on' in technique_lower or 'practical' in technique_lower:
        return f"""Trainer's activity: 
\t• Conducts practical skills test on {topic}
\t• Observes technique and safety compliance
\t• Evaluates finished work quality
\t• Provides performance feedback

Learner's activity:
\t• Performs practical assessment
\t• Demonstrates proper techniques
\t• Completes required tasks"""
    
    else:
        return f"""Trainer's activity: 
\t• Gives learners assessment related to {topic}
\t• Evaluates understanding through questions
\t• Provides feedback

Learner's activity:
\t• Receives assessment and answers questions
\t• Demonstrates understanding"""
