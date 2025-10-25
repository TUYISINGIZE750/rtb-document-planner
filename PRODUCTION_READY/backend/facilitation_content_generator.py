"""Generate session plan content based on facilitation technique"""

def generate_introduction_activities(topic, facilitation_technique):
    """Generate introduction based on facilitation technique with proper formatting"""
    base = f"""Trainer's activity:
  • Greets and makes roll call
  • Involves learners to set ground rules
  • Reviews previous session
  • Announces topic: {topic}"""
    
    technique_lower = facilitation_technique.lower()
    
    if 'trainer-guided' in technique_lower or 'demonstration' in technique_lower:
        return base + """
  • Explains objectives clearly
  • Demonstrates key concepts

Learner's activity:
  • Greets and replies to roll call
  • Participates in setting ground rules
  • Observes demonstration
  • Takes notes
  • Asks clarifications"""
    
    elif 'simulation' in technique_lower or 'role-play' in technique_lower:
        return base + """
  • Explains simulation scenario
  • Assigns roles to learners

Learner's activity:
  • Greets and replies to roll call
  • Participates in setting ground rules
  • Understands assigned roles
  • Prepares for simulation
  • Asks clarifications"""
    
    elif 'group work' in technique_lower or 'collaborative' in technique_lower:
        return base + """
  • Explains group work instructions
  • Divides learners into groups

Learner's activity:
  • Greets and replies to roll call
  • Participates in setting ground rules
  • Forms groups as instructed
  • Understands group tasks
  • Asks clarifications"""
    
    elif 'hands-on' in technique_lower or 'practical' in technique_lower:
        return base + """
  • Explains practical exercise
  • Demonstrates safety procedures

Learner's activity:
  • Greets and replies to roll call
  • Participates in setting ground rules
  • Observes safety demonstration
  • Collects materials
  • Asks clarifications"""
    
    elif 'discussion' in technique_lower or 'brainstorming' in technique_lower:
        return base + """
  • Explains discussion topics
  • Poses thought-provoking questions

Learner's activity:
  • Greets and replies to roll call
  • Participates in setting ground rules
  • Prepares to share ideas
  • Thinks about questions
  • Asks clarifications"""
    
    else:
        return base + """
  • Explains objectives
  • Provides session overview

Learner's activity:
  • Greets and replies to roll call
  • Participates in setting ground rules
  • Participates in review
  • Listens to objectives
  • Asks clarifications"""

def generate_development_activities(topic, facilitation_technique, learning_activities=None):
    """Generate development/body based on facilitation technique with proper formatting"""
    if learning_activities and learning_activities.strip():
        return learning_activities.strip()
    
    technique_lower = facilitation_technique.lower()
    
    if 'trainer-guided' in technique_lower or 'demonstration' in technique_lower:
        return f"""Trainer's activity:
  • Demonstrates {topic} step-by-step
  • Explains each step clearly
  • Provides guided practice
  • Monitors understanding

Learner's activity:
  • Observes demonstration
  • Takes notes
  • Practices under supervision
  • Asks questions"""
    
    elif 'simulation' in technique_lower or 'role-play' in technique_lower:
        return f"""Trainer's activity:
  • Sets up simulation for {topic}
  • Assigns roles
  • Monitors progress
  • Facilitates debriefing

Learner's activity:
  • Participates in simulation
  • Performs assigned role
  • Applies knowledge
  • Reflects on experience"""
    
    elif 'group work' in technique_lower or 'collaborative' in technique_lower:
        return f"""Trainer's activity:
  • Assigns group tasks on {topic}
  • Provides resources
  • Monitors progress
  • Facilitates discussions

Learner's activity:
  • Works in groups
  • Shares ideas
  • Completes tasks
  • Presents findings"""
    
    elif 'hands-on' in technique_lower or 'practical' in technique_lower:
        return f"""Trainer's activity:
  • Provides practical exercises on {topic}
  • Demonstrates techniques
  • Supervises practice
  • Ensures safety

Learner's activity:
  • Performs hands-on practice
  • Follows safety procedures
  • Uses tools correctly
  • Completes tasks"""
    
    elif 'discussion' in technique_lower or 'brainstorming' in technique_lower:
        return f"""Trainer's activity:
  • Facilitates discussion on {topic}
  • Poses questions
  • Encourages participation
  • Summarizes key points

Learner's activity:
  • Participates in discussion
  • Shares ideas
  • Listens to others
  • Takes notes"""
    
    elif 'project-based' in technique_lower:
        return f"""Trainer's activity:
  • Introduces project on {topic}
  • Explains requirements
  • Monitors progress
  • Provides feedback

Learner's activity:
  • Plans project
  • Conducts research
  • Develops deliverables
  • Presents project"""
    
    else:
        return f"""Trainer's activity:
  • Presents content on {topic}
  • Provides examples
  • Engages learners
  • Monitors understanding

Learner's activity:
  • Listens and takes notes
  • Participates in activities
  • Practices skills
  • Asks questions"""

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
    """Generate assessment based on facilitation technique with proper formatting"""
    if custom_assessment:
        return f"""Trainer's activity: 
  • {custom_assessment}

Learner's activity:
  • Learners receive assessment and answer questions"""
    
    technique_lower = facilitation_technique.lower()
    
    if 'trainer-guided' in technique_lower or 'demonstration' in technique_lower:
        return f"""Trainer's activity: 
  • Gives practical demonstration test on {topic}
  • Observes learner performance
  • Provides written quiz on key concepts
  • Evaluates understanding

Learner's activity:
  • Demonstrates learned skills
  • Completes written assessment
  • Answers questions accurately"""
    
    elif 'simulation' in technique_lower or 'role-play' in technique_lower:
        return f"""Trainer's activity: 
  • Evaluates simulation performance on {topic}
  • Assesses role-play effectiveness
  • Reviews learner reflections
  • Provides feedback

Learner's activity:
  • Completes simulation assessment
  • Writes reflection on experience
  • Receives and reviews feedback"""
    
    elif 'group work' in technique_lower or 'collaborative' in technique_lower:
        return f"""Trainer's activity: 
  • Evaluates group presentations on {topic}
  • Assesses individual contributions
  • Reviews group deliverables
  • Provides peer evaluation forms

Learner's activity:
  • Presents group work
  • Completes peer evaluations
  • Submits individual reflections"""
    
    elif 'hands-on' in technique_lower or 'practical' in technique_lower:
        return f"""Trainer's activity: 
  • Conducts practical skills test on {topic}
  • Observes technique and safety compliance
  • Evaluates finished work quality
  • Provides performance feedback

Learner's activity:
  • Performs practical assessment
  • Demonstrates proper techniques
  • Completes required tasks"""
    
    else:
        return f"""Trainer's activity: 
  • Gives learners assessment related to {topic}
  • Evaluates understanding through questions
  • Provides feedback

Learner's activity:
  • Receives assessment and answers questions
  • Demonstrates understanding"""
