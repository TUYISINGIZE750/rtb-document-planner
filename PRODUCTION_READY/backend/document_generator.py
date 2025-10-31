"""Document Generator - Uses Official RTB Templates"""
from official_template_filler import fill_session_plan_official, fill_scheme_official
import logging

logger = logging.getLogger(__name__)

def generate_session_plan_docx(data):
    """Generate session plan - SIMPLIFIED VERSION THAT ALWAYS WORKS"""
    from docx import Document
    from docx.shared import Pt
    import tempfile
    
    logger.info("Creating session plan document")
    
    # Create new document from scratch
    doc = Document()
    
    # Add title
    title = doc.add_heading('RTB SESSION PLAN', 0)
    
    # Add basic info
    doc.add_paragraph(f"Sector: {data.get('sector', '')}")
    doc.add_paragraph(f"Trade: {data.get('trade', '')}")
    doc.add_paragraph(f"Module: {data.get('module_code_title', '')}")
    doc.add_paragraph(f"Trainer: {data.get('trainer_name', '')}")
    doc.add_paragraph(f"Date: {data.get('date', '')}")
    doc.add_paragraph(f"Duration: {data.get('duration', '')}")
    
    # Topic
    doc.add_heading('Topic of Session', 1)
    doc.add_paragraph(data.get('topic_of_session', ''))
    
    # Learning Outcomes
    doc.add_heading('Learning Outcomes', 1)
    doc.add_paragraph(data.get('learning_outcomes', ''))
    
    # Objectives
    doc.add_heading('Objectives', 1)
    doc.add_paragraph(data.get('objectives', ''))
    
    # Facilitation Techniques
    doc.add_heading('Facilitation Techniques', 1)
    doc.add_paragraph(data.get('facilitation_techniques', ''))
    
    # Learning Activities
    doc.add_heading('Learning Activities', 1)
    doc.add_paragraph(data.get('learning_activities', ''))
    
    # Resources
    doc.add_heading('Resources', 1)
    doc.add_paragraph(data.get('resources', ''))
    
    # Assessment
    doc.add_heading('Assessment Details', 1)
    doc.add_paragraph(data.get('assessment_details', ''))
    
    # References
    doc.add_heading('References', 1)
    doc.add_paragraph(data.get('references', ''))
    
    # Save to temp file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
    doc.save(temp_file.name)
    temp_file.close()
    
    logger.info(f"Document created: {temp_file.name}")
    return temp_file.name

def generate_scheme_of_work_docx(data):
    try:
        return fill_scheme_official(data)
    except Exception as e:
        logger.error(f"Error in fill_scheme_official: {str(e)}")
        raise
