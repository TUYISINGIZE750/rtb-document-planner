"""Format content properly for RTB documents - clean spacing and organization"""

def clean_text(text):
    """Remove extra spaces and organize text properly"""
    if not text:
        return ""
    # Remove multiple spaces within lines
    lines = [' '.join(line.split()) for line in text.split('\n')]
    # Remove empty lines but keep structure
    lines = [line for line in lines if line.strip()]
    return '\n'.join(lines)

def generate_references(module, topic, learning_outcomes, indicative_contents):
    """Generate relevant references based on session content"""
    references = []
    
    # Extract key terms
    topic_lower = topic.lower() if topic else ""
    
    # Programming/ICT references
    if any(term in topic_lower for term in ['programming', 'python', 'java', 'code', 'software', 'variable', 'datatype']):
        references.extend([
            "Deitel, P., & Deitel, H. (2019). Python for Programmers. Pearson Education.",
            "Gaddis, T. (2020). Starting Out with Programming Logic and Design. Pearson.",
            "Downey, A. (2015). Think Python: How to Think Like a Computer Scientist. O'Reilly Media.",
            "Matthes, E. (2019). Python Crash Course: A Hands-On, Project-Based Introduction to Programming. No Starch Press."
        ])
    # Networking references
    elif any(term in topic_lower for term in ['network', 'cisco', 'routing', 'switching', 'tcp', 'ip']):
        references.extend([
            "Tanenbaum, A. S., & Wetherall, D. J. (2021). Computer Networks. Pearson.",
            "Kurose, J. F., & Ross, K. W. (2020). Computer Networking: A Top-Down Approach. Pearson.",
            "Cisco Networking Academy. (2020). CCNA Routing and Switching Course Materials.",
            "Odom, W. (2019). CCNA 200-301 Official Cert Guide Library. Cisco Press."
        ])
    # Database references
    elif any(term in topic_lower for term in ['database', 'sql', 'mysql', 'data']):
        references.extend([
            "Elmasri, R., & Navathe, S. B. (2020). Fundamentals of Database Systems. Pearson.",
            "Coronel, C., & Morris, S. (2019). Database Systems: Design, Implementation, & Management. Cengage.",
            "Beaulieu, A. (2020). Learning SQL: Generate, Manipulate, and Retrieve Data. O'Reilly Media.",
            "DuBois, P. (2020). MySQL Cookbook: Solutions for Database Developers and Administrators. O'Reilly."
        ])
    # Web development references
    elif any(term in topic_lower for term in ['web', 'html', 'css', 'javascript', 'frontend']):
        references.extend([
            "Duckett, J. (2014). HTML and CSS: Design and Build Websites. Wiley.",
            "Flanagan, D. (2020). JavaScript: The Definitive Guide. O'Reilly Media.",
            "Robbins, J. N. (2018). Learning Web Design: A Beginner's Guide to HTML, CSS, JavaScript. O'Reilly.",
            "Mozilla Developer Network. (2023). Web Development Documentation. https://developer.mozilla.org"
        ])
    # General TVET/Technical references
    else:
        references.extend([
            "Rwanda Education Board. (2021). TVET Curriculum Framework. REB Publications.",
            "UNESCO-UNEVOC. (2020). Technical and Vocational Education and Training. UNESCO.",
            "Ministry of Education Rwanda. (2022). Competency-Based Training Guidelines. MINEDUC.",
            "Rwanda Technical and Vocational Education and Training Board. (2023). Module Guidelines."
        ])
    
    return '\n'.join(references[:5])  # Return top 5 references

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
    """Format objectives as SMART objectives with proper numbering and spacing"""
    if not objectives:
        return ""
    
    lines = [line.strip() for line in objectives.split('\n') if line.strip()]
    formatted = []
    
    for i, line in enumerate(lines, 1):
        # Remove existing numbers and extra text
        line = line.lstrip('0123456789.)-• ')
        # Remove redundant phrases
        line = line.replace('By the end of this', '').replace('session, trainees will be able to', '')
        line = line.replace('Trainees will', '').replace('achieving at least', '')
        line = line.replace('meeting Level', '').replace('competency standards', '')
        line = line.strip(', ')
        if line:
            formatted.append(f"{i}. {line}")
    
    return '\n'.join(formatted)
