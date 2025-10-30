"""Document Generator - Uses Official RTB Templates"""
from official_template_filler import fill_session_plan_official, fill_scheme_official
import logging

logger = logging.getLogger(__name__)

def generate_session_plan_docx(data):
    try:
        logger.info("Calling fill_session_plan_official")
        result = fill_session_plan_official(data)
        logger.info(f"fill_session_plan_official returned: {result}")
        if result is None:
            logger.error("fill_session_plan_official returned None, creating fallback")
            raise Exception("Template filler returned None")
        return result
    except Exception as e:
        logger.error(f"Error in fill_session_plan_official: {str(e)}")
        logger.warning("Creating simple fallback document")
        # Create simple document as fallback
        from docx import Document
        import tempfile
        doc = Document()
        doc.add_heading('RTB Session Plan', 0)
        doc.add_paragraph(f"Topic: {data.get('topic_of_session', 'N/A')}")
        doc.add_paragraph(f"\nObjectives:\n{data.get('objectives', 'N/A')}")
        doc.add_paragraph(f"\nLearning Activities:\n{data.get('learning_activities', 'N/A')}")
        doc.add_paragraph(f"\nAssessment:\n{data.get('assessment_details', 'N/A')}")
        doc.add_paragraph(f"\nReferences:\n{data.get('references', 'N/A')}")
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
        doc.save(temp_file.name)
        temp_file.close()
        logger.info(f"Fallback document created: {temp_file.name}")
        return temp_file.name

def generate_scheme_of_work_docx(data):
    try:
        return fill_scheme_official(data)
    except Exception as e:
        logger.error(f"Error in fill_scheme_official: {str(e)}")
        raise
