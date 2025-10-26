"""Smart Content Generator for RTB Session Plans
Generates pedagogically sound content based on topic and facilitation technique"""

class SmartSessionPlanContentGenerator:
    
    FACILITATION_TEMPLATES = {
        'Trainer-guided instruction': {
            'introduction_trainer': [
                "Reviews previous session's key concepts",
                "Announces the topic and its relevance",
                "Shares learning objectives with learners",
                "Connects content to real-world applications",
                "Sets expectations and success criteria",
            ],
            'introduction_learner': [
                "Listens attentively to trainer's introduction",
                "Reviews notes from previous session",
                "Asks clarifying questions",
                "Takes notes on learning objectives",
                "Considers connections to prior knowledge",
            ],
            'development_trainer': [
                "Presents main concepts in logical sequence",
                "Demonstrates practical examples",
                "Uses questioning to check understanding",
                "Provides guided practice with real-time feedback",
                "Elaborates on complex concepts",
                "Shares expert insights and best practices",
            ],
            'development_learner': [
                "Listens carefully and takes comprehensive notes",
                "Participates in guided practice activities",
                "Asks clarifying questions at appropriate times",
                "Works through practice problems",
                "Seeks feedback on understanding",
                "Records important examples",
            ],
            'assessment': [
                "Oral questioning during instruction",
                "Observation of learner participation",
                "Supervised practice exercises with feedback",
                "Short quiz or written assessment",
                "One-on-one check-ins with learners",
            ]
        },
        'Simulation/Role-play': {
            'introduction_trainer': [
                "Explains simulation scenario and objectives",
                "Describes roles and responsibilities",
                "Sets rules and boundaries for role-play",
                "Distributes role cards and scenario details",
                "Briefs learners on their responsibilities",
            ],
            'introduction_learner': [
                "Understands the simulation scenario",
                "Accepts assigned role",
                "Reviews role card and responsibilities",
                "Asks clarifying questions about scenario",
                "Prepares mentally for role-play",
            ],
            'development_trainer': [
                "Facilitates the simulation/role-play",
                "Observes learner interactions",
                "Intervenes only when necessary",
                "Takes notes on learner performance",
                "Manages time and scenario progression",
            ],
            'development_learner': [
                "Actively participates in assigned role",
                "Interacts authentically with other roles",
                "Applies learning in simulated context",
                "Makes decisions within scenario",
                "Responds to unexpected situation",
            ],
            'assessment': [
                "Quality of role interpretation",
                "Application of knowledge in context",
                "Problem-solving within scenario",
                "Interaction and communication skills",
                "Decision-making quality",
            ]
        },
        'Group work/Collaborative learning': {
            'introduction_trainer': [
                "Explains collaborative task clearly",
                "Divides learners into balanced groups",
                "Assigns specific roles within groups",
                "Distributes materials and instructions",
                "Establishes group norms and expectations",
            ],
            'introduction_learner': [
                "Understands the collaborative task",
                "Accepts assigned group role",
                "Organizes with group members",
                "Clarifies task requirements",
                "Agrees on work distribution",
            ],
            'development_trainer': [
                "Circulates among groups",
                "Provides guidance without solving problems",
                "Ensures equitable participation",
                "Monitors progress toward objectives",
                "Facilitates peer feedback",
            ],
            'development_learner': [
                "Collaborates actively with group members",
                "Contributes ideas and expertise",
                "Listens to peers' perspectives",
                "Works toward group goal",
                "Helps resolve group conflicts",
            ],
            'assessment': [
                "Individual contribution to group work",
                "Quality of collaborative effort",
                "Completeness of group deliverable",
                "Peer evaluation of collaboration",
                "Problem-solving within group",
            ]
        },
        'Hands-on/Practical exercises': {
            'introduction_trainer': [
                "Explains safety procedures and requirements",
                "Demonstrates proper techniques",
                "Shows quality standards and success criteria",
                "Distributes equipment and materials",
                "Assigns learners to stations or pairs",
            ],
            'introduction_learner': [
                "Listens carefully to safety briefing",
                "Observes demonstration closely",
                "Understands quality standards",
                "Prepares workspace and gathers materials",
                "Asks safety-related questions",
            ],
            'development_trainer': [
                "Circulates among learners",
                "Provides real-time feedback on technique",
                "Assists with troubleshooting",
                "Ensures safety compliance",
                "Records competency observations",
            ],
            'development_learner': [
                "Performs hands-on exercise following procedures",
                "Maintains safety protocols throughout",
                "Seeks feedback on technique",
                "Corrects mistakes immediately",
                "Tries alternative approaches when needed",
            ],
            'assessment': [
                "Quality of practical execution",
                "Safety compliance throughout",
                "Adherence to procedures",
                "Problem-solving troubleshooting",
                "Consistency and repeatability",
            ]
        },
        'Discussion/Brainstorming': {
            'introduction_trainer': [
                "Poses discussion question or problem",
                "Clarifies scope and boundaries",
                "Establishes ground rules for discussion",
                "Encourages all perspectives",
                "Provides initial prompts if needed",
            ],
            'introduction_learner': [
                "Understands the discussion topic",
                "Prepares thoughts and examples",
                "Reviews relevant prior knowledge",
                "Considers diverse perspectives",
                "Formulates initial ideas",
            ],
            'development_trainer': [
                "Facilitates open discussion",
                "Asks probing questions",
                "Draws out quiet participants",
                "Manages dominant voices",
                "Records key ideas and themes",
            ],
            'development_learner': [
                "Shares ideas and perspectives",
                "Listens to others' viewpoints",
                "Asks clarifying questions",
                "Challenges ideas respectfully",
                "Builds on others' contributions",
            ],
            'assessment': [
                "Quality of contributions",
                "Depth of thinking demonstrated",
                "Respect for diverse views",
                "Ability to synthesize ideas",
                "Problem-solving through discussion",
            ]
        },
        'Project-based learning': {
            'introduction_trainer': [
                "Presents project scenario and outcomes",
                "Explains evaluation criteria",
                "Provides project timeline",
                "Identifies available resources",
                "Answers clarifying questions",
            ],
            'introduction_learner': [
                "Understands project objectives",
                "Clarifies requirements and deliverables",
                "Identifies available resources",
                "Plans project timeline",
                "Forms project team or group",
            ],
            'development_trainer': [
                "Provides guidance and mentoring",
                "Reviews progress milestones",
                "Facilitates resource access",
                "Ensures quality standards",
                "Provides feedback on work",
            ],
            'development_learner': [
                "Executes project plan systematically",
                "Manages time toward milestones",
                "Collaborates with team members",
                "Solves problems that arise",
                "Incorporates feedback",
            ],
            'assessment': [
                "Quality of final deliverable",
                "Project completion and presentation",
                "Problem-solving demonstrated",
                "Teamwork and collaboration",
                "Application of learning to project",
            ]
        }
    }
    
    @staticmethod
    def generate_introduction_section(topic, facilitation_technique):
        """Generate introduction section with trainer/learner activities"""
        template = SmartSessionPlanContentGenerator.FACILITATION_TEMPLATES.get(
            facilitation_technique,
            SmartSessionPlanContentGenerator.FACILITATION_TEMPLATES['Trainer-guided instruction']
        )
        
        trainer_activities = template['introduction_trainer']
        learner_activities = template['introduction_learner']
        
        content = "Trainer's Activities:\n"
        for activity in trainer_activities:
            content += f"• {activity}\n"
        
        content += "\nLearner's Activities:\n"
        for activity in learner_activities:
            content += f"• {activity}\n"
        
        return content.strip()
    
    @staticmethod
    def generate_development_section(topic, facilitation_technique):
        """Generate development section with topic integration"""
        template = SmartSessionPlanContentGenerator.FACILITATION_TEMPLATES.get(
            facilitation_technique,
            SmartSessionPlanContentGenerator.FACILITATION_TEMPLATES['Trainer-guided instruction']
        )
        
        trainer_activities = template['development_trainer']
        learner_activities = template['development_learner']
        
        content = f"Main Content: {topic}\n\n"
        content += "Trainer's Activities:\n"
        for activity in trainer_activities:
            content += f"• {activity}\n"
        
        content += "\nLearner's Activities:\n"
        for activity in learner_activities:
            content += f"• {activity}\n"
        
        return content.strip()
    
    @staticmethod
    def generate_assessment_section(topic, facilitation_technique):
        """Generate assessment methods appropriate for technique"""
        template = SmartSessionPlanContentGenerator.FACILITATION_TEMPLATES.get(
            facilitation_technique,
            SmartSessionPlanContentGenerator.FACILITATION_TEMPLATES['Trainer-guided instruction']
        )
        
        assessment_methods = template['assessment']
        
        content = f"Assessment Methods for {topic}:\n"
        for method in assessment_methods:
            content += f"• {method}\n"
        
        return content.strip()
    
    @staticmethod
    def generate_conclusion_section(topic):
        """Generate conclusion section"""
        content = f"Conclusion\n\n"
        content += f"Key Takeaways from {topic}:\n"
        content += "• Summarize main learning points\n"
        content += "• Reinforce learning objectives\n"
        content += "• Connect learning to next session\n"
        content += "• Answer remaining questions\n"
        content += "• Preview upcoming topics\n"
        
        return content.strip()
    
    @staticmethod
    def generate_evaluation_section(topic):
        """Generate self-evaluation section"""
        content = "Trainer's Reflection on Session:\n\n"
        content += "• Did learners achieve the learning objectives?\n"
        content += "• What aspects of the lesson were most effective?\n"
        content += "• Which learners need additional support?\n"
        content += "• How can the next session be improved?\n"
        content += "• Was the pace appropriate for the group?\n"
        content += "• Were the facilitation techniques effective?\n"
        
        return content.strip()
