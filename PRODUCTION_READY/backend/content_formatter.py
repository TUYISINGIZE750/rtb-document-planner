"""Format content properly for RTB documents - clean spacing and organization"""

def clean_text(text):
    """Remove extra spaces and organize text properly"""
    if not text:
        return ""
    # Remove multiple spaces
    text = ' '.join(text.split())
    # Remove multiple newlines but keep intentional ones
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    return '\n'.join(lines)

def format_list_items(items, bullet='•'):
    """Format list items with consistent spacing"""
    if isinstance(items, str):
        items = [i.strip() for i in items.split('\n') if i.strip()]
    return '\n'.join([f"{bullet} {item}" for item in items if item])

def format_trainer_learner_activities(trainer_activities, learner_activities):
    """Format trainer and learner activities with proper spacing"""
    trainer_list = [a.strip() for a in trainer_activities if a.strip()]
    learner_list = [a.strip() for a in learner_activities if a.strip()]
    
    result = "Trainer's activity:\n"
    for activity in trainer_list:
        result += f"  • {activity}\n"
    
    result += "\nLearner's activity:\n"
    for activity in learner_list:
        result += f"  • {activity}\n"
    
    return result.rstrip()

def format_resources(resources_list):
    """Format resources with clean line breaks"""
    if isinstance(resources_list, str):
        resources_list = [r.strip() for r in resources_list.replace('•', '').split('\n') if r.strip()]
    return '\n'.join(resources_list)

def format_objectives(objectives):
    """Format objectives with proper numbering"""
    if not objectives:
        return ""
    
    lines = [line.strip() for line in objectives.split('\n') if line.strip()]
    formatted = []
    
    for i, line in enumerate(lines, 1):
        # Remove existing numbers
        line = line.lstrip('0123456789.)-• ')
        formatted.append(f"{i}. {line}")
    
    return '\n'.join(formatted)
