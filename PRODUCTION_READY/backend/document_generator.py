"""Document Generator - Uses Official RTB Templates"""
from official_template_filler import fill_session_plan_official, fill_scheme_official

def generate_session_plan_docx(data):
    return fill_session_plan_official(data)

def generate_scheme_of_work_docx(data):
    return fill_scheme_official(data)
