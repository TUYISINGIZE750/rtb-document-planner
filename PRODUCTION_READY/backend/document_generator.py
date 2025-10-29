"""Document Generator - Uses Official RTB Templates with AI Enhancement"""
from official_template_filler import fill_session_plan_official, fill_scheme_official
try:
    from ai_content_generator import generate_session_plan_content, generate_scheme_content
    AI_AVAILABLE = True
except:
    AI_AVAILABLE = False

def generate_session_plan_docx(data):
    if AI_AVAILABLE:
        try:
            enhanced_data = generate_session_plan_content(data)
            return fill_session_plan_official(enhanced_data)
        except:
            pass
    return fill_session_plan_official(data)

def generate_scheme_of_work_docx(data):
    if AI_AVAILABLE:
        try:
            enhanced_data = generate_scheme_content(data)
            return fill_scheme_official(enhanced_data)
        except:
            pass
    return fill_scheme_official(data)
