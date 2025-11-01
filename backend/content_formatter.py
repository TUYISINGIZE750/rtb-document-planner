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



def generate_references(module_title, topic, learning_outcomes, indicative_contents=""):
    """Generate AI-based references relevant to the module content"""
    
    # Combine all content to determine topic area
    content = f"{module_title} {topic} {learning_outcomes} {indicative_contents}".lower()
    
    # Determine topic category
    if any(word in content for word in ['program', 'python', 'java', 'code', 'software', 'algorithm']):
        return """1. Gaddis, T. (2021). Starting Out with Python (5th ed.). Pearson Education.
2. Matthes, E. (2019). Python Crash Course: A Hands-On, Project-Based Introduction to Programming (2nd ed.). No Starch Press.
3. Downey, A. (2015). Think Python: How to Think Like a Computer Scientist (2nd ed.). O'Reilly Media.
4. Lutz, M. (2013). Learning Python (5th ed.). O'Reilly Media."""
    
    elif any(word in content for word in ['network', 'cisco', 'routing', 'tcp', 'ip', 'lan', 'wan']):
        return """1. Tanenbaum, A. S., & Wetherall, D. J. (2021). Computer Networks (6th ed.). Pearson.
2. Kurose, J. F., & Ross, K. W. (2020). Computer Networking: A Top-Down Approach (8th ed.). Pearson.
3. Odom, W. (2019). CCNA 200-301 Official Cert Guide Library. Cisco Press.
4. Lammle, T. (2020). CompTIA Network+ Study Guide (5th ed.). Sybex."""
    
    elif any(word in content for word in ['database', 'sql', 'mysql', 'data', 'query', 'table']):
        return """1. Elmasri, R., & Navathe, S. B. (2015). Fundamentals of Database Systems (7th ed.). Pearson.
2. Silberschatz, A., Korth, H. F., & Sudarshan, S. (2019). Database System Concepts (7th ed.). McGraw-Hill.
3. Beaulieu, A. (2020). Learning SQL: Generate, Manipulate, and Retrieve Data (3rd ed.). O'Reilly Media.
4. DuBois, P. (2013). MySQL (5th ed.). Addison-Wesley Professional."""
    
    elif any(word in content for word in ['web', 'html', 'css', 'javascript', 'website', 'frontend']):
        return """1. Duckett, J. (2014). HTML and CSS: Design and Build Websites. Wiley.
2. Flanagan, D. (2020). JavaScript: The Definitive Guide (7th ed.). O'Reilly Media.
3. Robbins, J. N. (2018). Learning Web Design: A Beginner's Guide (5th ed.). O'Reilly Media.
4. Frain, B. (2020). Responsive Web Design with HTML5 and CSS (3rd ed.). Packt Publishing."""
    
    elif any(word in content for word in ['security', 'cyber', 'encryption', 'firewall', 'threat']):
        return """1. Stallings, W., & Brown, L. (2018). Computer Security: Principles and Practice (4th ed.). Pearson.
2. Whitman, M. E., & Mattord, H. J. (2021). Principles of Information Security (7th ed.). Cengage Learning.
3. Kim, D., & Solomon, M. G. (2021). Fundamentals of Information Systems Security (4th ed.). Jones & Bartlett Learning.
4. Ciampa, M. (2020). CompTIA Security+ Guide to Network Security Fundamentals (7th ed.). Cengage Learning."""
    
    elif any(word in content for word in ['hardware', 'computer', 'maintenance', 'repair', 'component']):
        return """1. Andrews, J. (2019). A+ Guide to IT Technical Support (10th ed.). Cengage Learning.
2. Meyers, M. (2019). CompTIA A+ Certification All-in-One Exam Guide (10th ed.). McGraw-Hill.
3. Mueller, S. (2020). Upgrading and Repairing PCs (22nd ed.). Que Publishing.
4. Soper, M. E. (2019). CompTIA A+ Core 1 (220-1001) and Core 2 (220-1002) Cert Guide (5th ed.). Pearson IT Certification."""
    
    else:
        # General TVET/ICT references
        return """1. Rwanda TVET Curriculum Framework. (2023). Rwanda Polytechnic/REB.
2. UNESCO-UNEVOC. (2021). TVET Best Practices in ICT Education. UNESCO.
3. International Labour Organization. (2020). Skills for a Brighter Future: Technical and Vocational Education and Training in Rwanda. ILO.
4. Rwanda Education Board. (2022). Competency-Based Training Guidelines for TVET Institutions. REB."""
