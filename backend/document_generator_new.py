import re

def generate_smart_objectives_clean(topic, learning_outcomes, session_range=None, indicative_contents=None):
    """Clean SMART objectives generator"""
    
    # Clean all inputs thoroughly
    def deep_clean(text):
        if not text:
            return ''
        text = re.sub(r'^\d+\.?\d*\s*', '', str(text), flags=re.MULTILINE)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    topic = deep_clean(topic) or 'the topic'
    learning_outcomes = deep_clean(learning_outcomes) or ''
    session_range = deep_clean(session_range) or ''
    indicative_contents = deep_clean(indicative_contents) or ''
    
    # Extract key term (last 2-3 words)
    words = [w for w in topic.split() if len(w) > 2]
    key_term = ' '.join(words[-2:]) if len(words) >= 2 else topic
    
    # Determine verbs
    lo = learning_outcomes.lower()
    if 'identify' in lo:
        v1, v2, v3 = 'Define clearly', 'Select properly', 'Name appropriately'
    elif 'write' in lo or 'code' in lo:
        v1, v2, v3 = 'Explain clearly', 'Write correctly', 'Apply properly'
    elif 'demonstrat' in lo:
        v1, v2, v3 = 'Demonstrate properly', 'Perform correctly', 'Execute effectively'
    else:
        v1, v2, v3 = 'Define clearly', 'Identify properly', 'Apply correctly'
    
    # Extract first phrase from range and content (max 40 chars)
    range_text = session_range[:40] if session_range else 'methods'
    content_text = indicative_contents[:40] if indicative_contents else 'techniques'
    
    # Build objectives
    obj1 = f"{v1} the term {key_term} as used in {learning_outcomes.lower()}."
    obj2 = f"{v2} 2 {range_text.lower()} used in {content_text.lower()}."
    obj3 = f"{v3} 2 {content_text.lower()} as used in {topic.lower()}."
    
    return f"1.\t{obj1}\n2.\t{obj2}\n3.\t{obj3}"
