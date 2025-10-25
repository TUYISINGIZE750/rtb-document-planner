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
    """Generate relevant references based on session content - 4-5 properly formatted APA references"""
    references = []
    
    # Extract key terms
    topic_lower = topic.lower() if topic else ""
    module_lower = module.lower() if module else ""
    content_lower = f"{topic_lower} {module_lower}"
    
    # Programming/ICT references
    if any(term in content_lower for term in ['programming', 'python', 'java', 'code', 'software', 'variable', 'datatype', 'algorithm']):
        references.extend([
            "Deitel, P., & Deitel, H. (2019). Python for programmers. Pearson Education.",
            "Gaddis, T. (2020). Starting out with programming logic and design. Pearson.",
            "Downey, A. (2015). Think Python: How to think like a computer scientist. O'Reilly Media.",
            "Matthes, E. (2019). Python crash course: A hands-on, project-based introduction to programming. No Starch Press.",
            "McConnell, S. (2004). Code complete: A practical handbook of software construction. Microsoft Press."
        ])
    # Networking references
    elif any(term in content_lower for term in ['network', 'cisco', 'routing', 'switching', 'tcp', 'ip', 'internet']):
        references.extend([
            "Tanenbaum, A. S., & Wetherall, D. J. (2021). Computer networks (6th ed.). Pearson Education.",
            "Kurose, J. F., & Ross, K. W. (2020). Computer networking: A top-down approach (8th ed.). Pearson.",
            "Cisco Networking Academy. (2020). CCNA routing and switching course materials. Cisco Systems.",
            "Odom, W. (2019). CCNA 200-301 official cert guide library (2nd ed.). Cisco Press.",
            "Doyle, J. C., Alderson, D. L., & Willinger, W. (2015). Internet topology and the evolution of the Internet. ACM."
        ])
    # Database references
    elif any(term in content_lower for term in ['database', 'sql', 'mysql', 'data management', 'data modeling']):
        references.extend([
            "Elmasri, R., & Navathe, S. B. (2020). Fundamentals of database systems (8th ed.). Pearson Education.",
            "Coronel, C., & Morris, S. (2019). Database systems: Design, implementation, and management (13th ed.). Cengage.",
            "Beaulieu, A. (2020). Learning SQL: Generate, manipulate, and retrieve data (3rd ed.). O'Reilly Media.",
            "Garcia-Molina, H., Ullman, J. D., & Widom, J. (2008). Database systems: The complete book (2nd ed.). Prentice Hall.",
            "DuBois, P. (2020). MySQL cookbook: Solutions for database developers and administrators. O'Reilly."
        ])
    # Web development references
    elif any(term in content_lower for term in ['web', 'html', 'css', 'javascript', 'frontend', 'responsive']):
        references.extend([
            "Duckett, J. (2014). HTML and CSS: Design and build websites. Wiley Publishing.",
            "Flanagan, D. (2020). JavaScript: The definitive guide (7th ed.). O'Reilly Media.",
            "Robbins, J. N. (2018). Learning web design: A beginner's guide to HTML, CSS, JavaScript (5th ed.). O'Reilly.",
            "Nielsen, J., & Norman, D. A. (2014). Usability 101: Introduction to usability. Nielsen Norman Group.",
            "Mozilla Foundation. (2023). Web development documentation and standards. Retrieved from https://developer.mozilla.org"
        ])
    # Business/Management references
    elif any(term in content_lower for term in ['business', 'management', 'leadership', 'entrepreneurship', 'accounting']):
        references.extend([
            "Drucker, P. F. (2006). The effective executive: The definitive guide to getting the right things done. Harper Business.",
            "Porter, M. E. (2008). Competitive advantage: Creating and sustaining superior performance. Free Press.",
            "Mintzberg, H. (2009). Managing. Berrett-Koehler Publishers.",
            "Ryan, R. M., & Deci, E. L. (2000). Intrinsic and extrinsic motivations: Classic definitions and new directions. Contemporary Educational Psychology, 25(1), 54-67.",
            "Kotter, J. P. (2012). Leading change. Harvard Business Review Press."
        ])
    # General TVET/Technical references
    else:
        references.extend([
            "Rwanda Education Board. (2021). TVET curriculum framework. REB Publications.",
            "UNESCO-UNEVOC. (2020). Technical and vocational education and training (TVET) and the sustainable development goals (SDGs). UNESCO Publications.",
            "Ministry of Education Rwanda. (2022). Competency-based training guidelines for technical and vocational education. MINEDUC.",
            "Rwanda Technical and Vocational Education and Training Board. (2023). National module guidelines and standards. RTVETB Publications.",
            "International Labour Organization. (2021). World employment and social outlook: The role of digital labour platforms in transforming the world of work. ILO."
        ])
    
    # Format as numbered list with proper spacing
    formatted_refs = []
    for i, ref in enumerate(references[:5], 1):
        formatted_refs.append(f"{i}. {ref}")
    
    return '\n\n'.join(formatted_refs)

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
