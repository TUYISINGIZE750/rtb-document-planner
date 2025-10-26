"""
Facilitation Content Generator - Creates structured content based on selected facilitation technique
Generates Introduction, Development, Assessment, and Resources for each technique
"""

def generate_introduction_activities(topic, facilitation_technique):
    """Generate introduction activities based on facilitation technique"""
    
    activities_by_technique = {
        "Trainer-guided instruction": f"""INTRODUCTION ACTIVITIES ({topic})

Trainer's activity:
  • Welcomes trainees and introduces the session topic: {topic}
  • Shows key learning objectives on flipchart/projector
  • Explains session structure and time allocation
  • Asks hook question to activate prior knowledge: "What do you already know about {topic}?"
  • Reveals real-world relevance: "Why does {topic} matter in your trade?"

Learner's activity:
  • Respond to hook question (raise hands or pair-share)
  • Listen to context and relevance explanation
  • Note down key objectives in their workbooks
  • Ask clarification questions about what they'll learn""",

        "Simulation/Role-play": f"""INTRODUCTION ACTIVITIES ({topic})

Trainer's activity:
  • Presents the scenario/situation related to {topic}
  • Clarifies roles and objectives for the simulation
  • Explains assessment criteria during role-play
  • Answers questions about the scenario setup
  • Distributes role cards and scenario materials

Learner's activity:
  • Read and understand their assigned role
  • Ask clarifying questions about the scenario
  • Prepare mentally for the role-play activity
  • Identify key points from the scenario brief
  • Form initial understanding of their responsibility""",

        "Group work/Collaborative learning": f"""INTRODUCTION ACTIVITIES ({topic})

Trainer's activity:
  • Introduces the collaborative task related to {topic}
  • Divides trainees into balanced groups (4-5 per group)
  • Explains group roles: Leader, Scribe, Presenter, Timekeeper
  • Provides clear task instructions and success criteria
  • Sets time expectations (25-30 minutes for task)

Learner's activity:
  • Get into assigned groups
  • Clarify understanding of group task
  • Choose or accept group role
  • Review task instructions together
  • Ask questions before starting work""",

        "Hands-on/Practical exercises": f"""INTRODUCTION ACTIVITIES ({topic})

Trainer's activity:
  • Demonstrates the correct use of equipment/tools for {topic}
  • Shows common mistakes to avoid (2-3 examples)
  • Explains safety procedures and precautions
  • Checks that all materials are available and in working order
  • Pairs experienced trainees with less experienced ones

Learner's activity:
  • Observe the trainer's demonstration carefully
  • Note down safety procedures on their worksheets
  • Ask questions about equipment use
  • Identify available materials and setup
  • Mentally prepare for hands-on practice""",

        "Discussion/Brainstorming": f"""INTRODUCTION ACTIVITIES ({topic})

Trainer's activity:
  • Poses engaging opening question related to {topic}
  • Establishes ground rules: Respect all ideas, No criticism, Build on ideas
  • Divides class into discussion groups (3-4 groups)
  • Provides each group with topic prompts/questions
  • Distributes flipchart paper and markers for recording ideas

Learner's activity:
  • Listen to the opening question
  • Understand the discussion ground rules
  • Get into assigned discussion groups
  • Prepare to contribute ideas about {topic}
  • Receive and review discussion prompts""",

        "Project-based learning": f"""INTRODUCTION ACTIVITIES ({topic})

Trainer's activity:
  • Introduces the project brief related to {topic}
  • Clarifies project objectives, deliverables, and timeline
  • Explains assessment criteria (rubric)
  • Discusses real-world application of the project
  • Forms project teams and assigns roles

Learner's activity:
  • Understand the project scope and requirements
  • Review project deliverables and timeline
  • Study the assessment rubric
  • Identify project team members
  • Clarify their role in the project team"""
    }
    
    return activities_by_technique.get(
        facilitation_technique,
        activities_by_technique["Trainer-guided instruction"]
    )


def generate_development_activities(topic, facilitation_technique, user_input=None):
    """Generate main development activities based on facilitation technique"""
    
    if not facilitation_technique:
        facilitation_technique = "Trainer-guided instruction"
    
    activities_by_technique = {
        "Trainer-guided instruction": f"""DEVELOPMENT ACTIVITIES ({topic})

Trainer's activity (Main Phase - 25-30 minutes):
  • Present content about {topic} using structured approach
  • Use multi-sensory teaching methods (visual aids, examples, demonstrations)
  • Break content into digestible chunks (3-5 minute segments)
  • Check understanding after each segment using questions
  • Provide worked examples showing application of {topic}
  • Use real-world case studies related to trainees' context
  • Encourage active note-taking
  • Clarify misconceptions immediately

Learner's activity:
  • Listen actively and take structured notes
  • Ask questions when concepts are unclear
  • Participate in understanding checks (respond to questions)
  • Observe worked examples carefully
  • Connect new learning to prior knowledge
  • Practice applying concepts with trainer guidance""",

        "Simulation/Role-play": f"""DEVELOPMENT ACTIVITIES ({topic})

Trainer's activity (Main Phase - 25-30 minutes):
  • Monitor role-play progress and participant engagement
  • Provide prompts if discussion stalls
  • Note key instances of learning or misconceptions
  • Ensure all participants are actively engaged
  • Document examples for debriefing
  • Stop activity if safety issues arise
  • Manage time to allow for role rotation if needed
  • Record observations for assessment purposes

Learner's activity:
  • Engage fully in the assigned role
  • Interact with other role-players realistically
  • Apply theoretical knowledge from {topic} to the scenario
  • Respond to unexpected situations in character
  • Demonstrate problem-solving in realistic context
  • Communicate professionally during the role-play
  • Note what works and what doesn't for later debrief""",

        "Group work/Collaborative learning": f"""DEVELOPMENT ACTIVITIES ({topic})

Trainer's activity (Main Phase - 25-30 minutes):
  • Circulate among groups monitoring progress
  • Provide guidance without giving answers
  • Ask probing questions to deepen thinking
  • Manage group dynamics and resolve conflicts
  • Ensure equitable participation (watch for dominators/silent members)
  • Provide resource materials as needed
  • Document group processes for assessment
  • Keep groups on track with time management

Learner's activity:
  • Work collaboratively on the assigned task related to {topic}
  • Share ideas and perspectives with group members
  • Listen to others' viewpoints respectfully
  • Help others understand concepts
  • Contribute unique skills and knowledge
  • Manage group time effectively
  • Create visible outputs (mind map, poster, solution)
  • Prepare presentation of findings""",

        "Hands-on/Practical exercises": f"""DEVELOPMENT ACTIVITIES ({topic})

Trainer's activity (Main Phase - 25-30 minutes):
  • Circulate among trainees providing individual guidance
  • Observe technique and provide corrective feedback
  • Ensure safety protocols are followed
  • Answer questions about equipment and procedures
  • Challenge advanced learners with extensions
  • Support struggling learners with scaffolding
  • Maintain equipment and materials in good condition
  • Document competency development for assessment

Learner's activity:
  • Practice hands-on skills related to {topic} independently
  • Follow correct procedures and safety guidelines
  • Ask for help when unable to proceed
  • Experiment safely within parameters
  • Observe and learn from peer demonstrations
  • Apply feedback to improve technique
  • Work at own pace while meeting basic competency
  • Produce a quality output or completed task""",

        "Discussion/Brainstorming": f"""DEVELOPMENT ACTIVITIES ({topic})

Trainer's activity (Main Phase - 25-30 minutes):
  • Facilitate discussions with strategic questioning
  • Ensure balanced participation across all groups
  • Record key ideas from each group
  • Connect ideas to learning objectives
  • Challenge superficial thinking with follow-up questions
  • Validate contributions and build on ideas
  • Monitor for off-topic discussions
  • Synthesize themes emerging from group discussions

Learner's activity:
  • Actively contribute ideas about {topic} in group
  • Listen to and build on peers' ideas
  • Ask clarifying questions to understand ideas better
  • Think critically about suggestions made
  • Record group's best ideas
  • Prepare to share group findings with whole class
  • Connect personal experience to discussion topics
  • Respectfully disagree or offer alternative views""",

        "Project-based learning": f"""DEVELOPMENT ACTIVITIES ({topic})

Trainer's activity (Main Phase - 25-30 minutes):
  • Provide guidance on project research and planning
  • Help teams access necessary resources and information
  • Monitor project progress against timeline
  • Provide formative feedback on work in progress
  • Facilitate peer review between project teams
  • Address project management issues (resource, team dynamics)
  • Document evidence of learning for assessment
  • Guide reflection on learning process

Learner's activity:
  • Work on assigned project tasks related to {topic}
  • Research and gather relevant information
  • Apply theoretical knowledge to project context
  • Collaborate with team to produce project outputs
  • Seek feedback and revise work based on feedback
  • Manage project timeline and deliverables
  • Document learning process and decisions
  • Prepare project presentation materials"""
    }
    
    return activities_by_technique.get(
        facilitation_technique,
        activities_by_technique["Trainer-guided instruction"]
    )


def generate_assessment(topic, facilitation_technique, user_input=None):
    """Generate assessment methods aligned with facilitation technique"""
    
    if not facilitation_technique:
        facilitation_technique = "Trainer-guided instruction"
    
    assessment_by_technique = {
        "Trainer-guided instruction": f"""ASSESSMENT FOR {topic.upper()}

Assessment Methods:
  • Written quiz: 5-10 multiple choice questions covering key concepts
  • Practical demonstration: Trainee demonstrates understanding of {topic}
  • Question & answer: Trainer asks comprehension questions during learning
  • Observation checklist: Trainer notes correct responses and misconceptions
  • Think-pair-share: Trainees discuss their understanding in pairs

Success Criteria:
  • 80%+ accuracy on written assessment
  • Demonstrates all key procedures/concepts correctly
  • Answers 75%+ of review questions accurately
  • Shows understanding through quality of responses
  • Applies learning to new examples/scenarios

Feedback Strategy:
  • Immediate corrective feedback during teaching
  • Individual feedback on quiz/written work
  • Positive reinforcement of correct responses
  • Identify gaps and provide remedial activities""",

        "Simulation/Role-play": f"""ASSESSMENT FOR {topic.upper()}

Assessment Methods:
  • Observation rubric: Rate quality of role-play performance
  • Peer assessment: Observers evaluate realism and accuracy
  • Trainer checklist: Note demonstration of key competencies during role-play
  • Debriefing discussion: Discuss what was learned from the simulation
  • Reflection journal: Trainees reflect on decisions made in role-play

Success Criteria:
  • Stays in character throughout simulation
  • Applies relevant knowledge to handle scenario appropriately
  • Demonstrates professional communication
  • Makes realistic decisions based on context
  • Reflects critically on experience

Feedback Strategy:
  • Constructive debriefing immediately after role-play
  • Highlight strengths and learning points
  • Discuss alternative approaches and outcomes
  • Connect simulation learning to real workplace practice
  • Provide specific examples from the performance""",

        "Group work/Collaborative learning": f"""ASSESSMENT FOR {topic.upper()}

Assessment Methods:
  • Group product assessment: Evaluate quality of group's output/solution
  • Process observation: Assess collaboration, communication, task management
  • Individual contribution assessment: Each member evaluates own/others' contributions
  • Peer feedback: Group members provide feedback to each other
  • Group presentation: Quality of presentation of findings

Success Criteria:
  • Group product shows understanding of {topic}
  • All members contribute meaningfully
  • Communication is clear and respectful
  • Task is completed on time
  • Solution/output meets quality standards

Feedback Strategy:
  • Provide feedback on group process and product
  • Highlight collaboration strengths
  • Suggest improvements in teamwork and communication
  • Give individual feedback on contributions
  • Public recognition of group achievements""",

        "Hands-on/Practical exercises": f"""ASSESSMENT FOR {topic.upper()}

Assessment Methods:
  • Practical performance assessment: Rate execution of skills related to {topic}
  • Competency checklist: Verify all required procedures performed correctly
  • Quality of output: Assess product/output of hands-on work
  • Safety compliance: Confirm adherence to safety procedures
  • Self-assessment: Trainees rate their own performance and confidence

Success Criteria:
  • All procedures performed correctly (100% compliance)
  • Output meets quality standards
  • No safety violations observed
  • Demonstrates increasing confidence and speed
  • Troubleshoots minor issues independently

Feedback Strategy:
  • Immediate feedback during practice
  • Demonstrate correct technique if needed
  • Highlight improvements and progress
  • Provide specific coaching on weak areas
  • Celebrate achievement of competency""",

        "Discussion/Brainstorming": f"""ASSESSMENT FOR {topic.upper()}

Assessment Methods:
  • Quality of ideas contributed: Assess depth and relevance of contributions
  • Listening skills: Note how well trainees build on others' ideas
  • Critical thinking: Evaluate analysis and evaluation of ideas
  • Participation observation: Track engagement level
  • Synthesis exercise: Ask trainees to summarize key insights from discussion

Success Criteria:
  • Contributes 2-3 substantive ideas to discussion
  • Demonstrates understanding of {topic}
  • Shows respectful engagement with diverse viewpoints
  • Makes connections between ideas
  • Synthesizes discussion into learning outcomes

Feedback Strategy:
  • Positive reinforcement for contributions during discussion
  • Ask follow-up questions to deepen thinking
  • Connect student ideas to learning objectives
  • Group feedback on quality of discussion
  • Reflection on key insights gained""",

        "Project-based learning": f"""ASSESSMENT FOR {topic.upper()}

Assessment Methods:
  • Project deliverables assessment: Rubric-based evaluation of outputs
  • Process portfolio: Evidence of planning, research, and revisions
  • Team collaboration assessment: Contribution and teamwork quality
  • Project presentation: Quality of explanation and demonstration
  • Reflection assessment: Depth of learning reflection

Success Criteria:
  • Project demonstrates understanding of {topic}
  • All deliverables meet quality standards
  • Evidence of research and planning
  • Team collaborated effectively
  • Learning gains evident in reflection

Feedback Strategy:
  • Rubric-based feedback on each component
  • Specific comments on strengths and areas for improvement
  • Peer feedback on presentation
  • Individual feedback on contribution
  • Reflection on learning journey"""
    }
    
    return assessment_by_technique.get(
        facilitation_technique,
        assessment_by_technique["Trainer-guided instruction"]
    )


def generate_resources(facilitation_technique, user_input=None):
    """Generate resource lists based on facilitation technique"""
    
    if not facilitation_technique:
        facilitation_technique = "Trainer-guided instruction"
    
    resources_by_technique = {
        "Trainer-guided instruction": """RESOURCES REQUIRED:
  • Projector and computer for presentations
  • Flipchart and markers for key points
  • Whiteboard/smartboard for interactive teaching
  • Handouts with key concepts summary
  • Worked examples and case study materials
  • Assessment tools (quizzes, question guides)
  • Reference materials for trainees
  • Video clips or multimedia content (if relevant)""",

        "Simulation/Role-play": """RESOURCES REQUIRED:
  • Scenario description document
  • Role cards for participants
  • Props and equipment appropriate to scenario
  • Observation checklists for assessors
  • Debriefing guide
  • Flipchart for capturing key learning points
  • Recording equipment (audio/video - optional)
  • Reflective journals for trainees""",

        "Group work/Collaborative learning": """RESOURCES REQUIRED:
  • Task description and success criteria
  • Flipchart paper and markers for each group
  • Resource materials (articles, case studies, data)
  • Laptops/computers if research needed
  • Templates for organizing work (mind maps, matrices)
  • Timer for time management
  • Presentation materials for sharing findings
  • Assessment rubric for group work quality""",

        "Hands-on/Practical exercises": """RESOURCES REQUIRED:
  • Equipment and tools required for the skill
  • Safety equipment (aprons, gloves, goggles, etc.)
  • Materials for practice (consumables, components)
  • Step-by-step instruction cards
  • Video demonstration (optional)
  • Practice worksheets
  • Quality standards checklist
  • Safety procedure poster""",

        "Discussion/Brainstorming": """RESOURCES REQUIRED:
  • Discussion prompts/starter questions
  • Flipchart and markers for each group
  • Sticky notes for idea capture
  • Concept mapping materials (optional)
  • Ground rules poster
  • Reference materials on discussion topic
  • Presentation materials for sharing ideas
  • Recording sheets for key themes""",

        "Project-based learning": """RESOURCES REQUIRED:
  • Project brief document
  • Research materials and reference sources
  • Access to computers/internet
  • Project planning templates
  • Assessment rubric (shared with learners)
  • Materials for project outputs
  • Presentation equipment
  • Peer review templates
  • Reflection journals"""
    }
    
    return resources_by_technique.get(
        facilitation_technique,
        resources_by_technique["Trainer-guided instruction"]
    )
