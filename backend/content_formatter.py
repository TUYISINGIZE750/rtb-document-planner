"""
Content Formatter - Formats and cleans content for RTB documents
Ensures proper formatting, structure, and compliance with RTB standards
"""

def clean_text(text):
    """Remove extra whitespace and clean up text"""
    if not text:
        return ""
    
    # Strip leading/trailing whitespace
    text = text.strip()
    
    # Replace multiple newlines with single newline
    while '\n\n\n' in text:
        text = text.replace('\n\n\n', '\n\n')
    
    # Remove extra spaces
    lines = text.split('\n')
    cleaned_lines = [line.rstrip() for line in lines]
    
    return '\n'.join(cleaned_lines)


def format_objectives(objectives_text):
    """Format objectives with proper SMART structure"""
    if not objectives_text:
        return "No objectives specified"
    
    text = clean_text(objectives_text)
    
    # If text already contains bullet points, clean and return
    if '•' in text or '-' in text:
        return text
    
    # Split by periods to identify individual objectives
    sentences = text.split('.')
    formatted = []
    
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence and len(sentence) > 10:
            # Add bullet point if not present
            if not sentence.startswith('•') and not sentence.startswith('-'):
                formatted.append(f"• {sentence}")
            else:
                formatted.append(sentence)
    
    return '\n'.join(formatted) if formatted else text


def format_resources(resources_text):
    """Format resources list with proper bullet points"""
    if not resources_text:
        return "Standard training resources as per module requirements"
    
    text = clean_text(resources_text)
    
    # If already formatted with bullets, return as-is
    if '•' in text:
        return text
    
    # Split by common delimiters
    items = []
    for delimiter in ['\n', '|', ';', ',']:
        if delimiter in text:
            items = text.split(delimiter)
            break
    
    if not items:
        items = [text]
    
    # Format with bullet points
    formatted_items = []
    for item in items:
        item = item.strip()
        if item and len(item) > 2:
            if not item.startswith('•') and not item.startswith('-'):
                formatted_items.append(f"• {item}")
            else:
                formatted_items.append(item)
    
    return '\n'.join(formatted_items) if formatted_items else text


def format_learning_activities(activities_text):
    """Format learning activities with proper structure"""
    if not activities_text:
        return "Activities to be defined by trainer"
    
    text = clean_text(activities_text)
    
    # Ensure proper numbering if not present
    lines = text.split('\n')
    formatted_lines = []
    
    for i, line in enumerate(lines, 1):
        line = line.strip()
        if line:
            # Check if line starts with number or bullet
            if not (line[0].isdigit() or line.startswith('•') or line.startswith('-')):
                formatted_lines.append(f"• {line}")
            else:
                formatted_lines.append(line)
    
    return '\n'.join(formatted_lines) if formatted_lines else text


def format_assessment_details(assessment_text):
    """Format assessment methods and criteria"""
    if not assessment_text:
        return """Assessment Methods:
• Question and answer during session
• Observation of trainee engagement
• Completion of assessment task
• Achievement of learning objectives

Success Criteria:
• 80% or higher achievement on assessment task
• Demonstrates understanding of key concepts
• Applies learning to new situations"""
    
    text = clean_text(assessment_text)
    
    # If text is short, it's likely custom input
    if len(text) < 100:
        return text
    
    # Format with sections
    if 'Assessment' not in text:
        return f"Assessment Methods:\n{text}"
    
    return text


def format_facilitation_technique(technique):
    """Standardize facilitation technique names"""
    if not technique:
        return "Trainer-guided instruction"
    
    technique = technique.strip()
    
    # Map variations to standard names
    mappings = {
        'trainer guided': 'Trainer-guided instruction',
        'trainer-guided': 'Trainer-guided instruction',
        'instruction': 'Trainer-guided instruction',
        'simulation': 'Simulation/Role-play',
        'roleplay': 'Simulation/Role-play',
        'role play': 'Simulation/Role-play',
        'role-play': 'Simulation/Role-play',
        'group': 'Group work/Collaborative learning',
        'collaborative': 'Group work/Collaborative learning',
        'group work': 'Group work/Collaborative learning',
        'group discussion': 'Discussion/Brainstorming',
        'discussion': 'Discussion/Brainstorming',
        'brainstorming': 'Discussion/Brainstorming',
        'hands-on': 'Hands-on/Practical exercises',
        'practical': 'Hands-on/Practical exercises',
        'hands on': 'Hands-on/Practical exercises',
        'experiential': 'Hands-on/Practical exercises',
        'project': 'Project-based learning',
        'project-based': 'Project-based learning',
        'project based': 'Project-based learning',
    }
    
    technique_lower = technique.lower()
    
    for key, value in mappings.items():
        if key in technique_lower:
            return value
    
    # If no mapping found, return original with proper capitalization
    return technique


def format_duration(duration):
    """Format duration to ensure minutes suffix"""
    if not duration:
        return "40 minutes"
    
    duration = str(duration).strip()
    
    # If already has 'minutes', return as-is
    if 'minute' in duration.lower():
        return duration
    
    # If just a number, add 'minutes'
    if duration.isdigit():
        return f"{duration} minutes"
    
    return duration


def format_module_code(module_code):
    """Format module code/title with proper capitalization"""
    if not module_code:
        return "Module Code and Title"
    
    text = str(module_code).strip()
    
    # If it looks like a code (has numbers and letters), keep it
    if any(char.isdigit() for char in text):
        return text
    
    # Otherwise, capitalize properly
    return ' '.join(word.capitalize() for word in text.split())


def format_sector_and_trade(sector, trade):
    """Format sector and trade/subsector"""
    sector_clean = sector.strip() if sector else "Unspecified Sector"
    trade_clean = trade.strip() if trade else "Unspecified Trade"
    
    # Capitalize properly
    sector_clean = ' '.join(word.capitalize() for word in sector_clean.split())
    trade_clean = ' '.join(word.capitalize() for word in trade_clean.split())
    
    return sector_clean, trade_clean


def format_number_of_trainees(number):
    """Format number of trainees"""
    if not number:
        return "25"
    
    # Extract just the number
    number_str = ''.join(char for char in str(number) if char.isdigit())
    
    return number_str if number_str else "25"


def format_term_week(term, week):
    """Format term and week"""
    term_clean = str(term).strip() if term else "Term 1"
    week_clean = str(week).strip() if week else "Week 1"
    
    # Ensure they start with the label if not already
    if 'term' not in term_clean.lower():
        term_clean = f"Term {term_clean}"
    if 'week' not in week_clean.lower():
        week_clean = f"Week {week_clean}"
    
    return term_clean, week_clean
