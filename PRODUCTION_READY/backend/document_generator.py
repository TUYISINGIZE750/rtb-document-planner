"""Document Generator - Uses Official RTB Templates"""
from official_template_filler import fill_session_plan_official, fill_scheme_official
import logging

logger = logging.getLogger(__name__)

def generate_session_plan_docx(data):
    logger.info("=" * 50)
    logger.info("Starting generate_session_plan_docx")
    logger.info(f"Data type: {type(data)}")
    logger.info(f"Data is None: {data is None}")
    
    if data is None:
        logger.error("Data is None! Creating emergency fallback")
        data = {}
    
    try:
        logger.info("Attempting to call fill_session_plan_official")
        result = fill_session_plan_official(data)
        logger.info(f"fill_session_plan_official returned: {result}")
        logger.info(f"Result type: {type(result)}")
        
        if result is None:
            logger.error("fill_session_plan_official returned None!")
            raise Exception("Template filler returned None")
        
        logger.info(f"Success! Returning: {result}")
        return result
        
    except Exception as e:
        logger.error(f"="*50)
        logger.error(f"EXCEPTION in fill_session_plan_official: {str(e)}")
        logger.error(f"Exception type: {type(e).__name__}")
        import traceback
        logger.error(f"Traceback: {traceback.format_exc()}")
        logger.error(f"="*50)
        logger.warning("Creating simple fallback document")
        
        try:
            from docx import Document
            import tempfile
            
            doc = Document()
            doc.add_heading('RTB Session Plan', 0)
            doc.add_paragraph(f"Topic: {data.get('topic_of_session', 'N/A') if data else 'N/A'}")
            doc.add_paragraph(f"\nObjectives:\n{data.get('objectives', 'N/A') if data else 'N/A'}")
            doc.add_paragraph(f"\nLearning Activities:\n{data.get('learning_activities', 'N/A') if data else 'N/A'}")
            doc.add_paragraph(f"\nAssessment:\n{data.get('assessment_details', 'N/A') if data else 'N/A'}")
            doc.add_paragraph(f"\nReferences:\n{data.get('references', 'N/A') if data else 'N/A'}")
            
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
            logger.info(f"Saving fallback to: {temp_file.name}")
            doc.save(temp_file.name)
            temp_file.close()
            logger.info(f"Fallback document created successfully: {temp_file.name}")
            return temp_file.name
            
        except Exception as fallback_error:
            logger.error(f"FALLBACK ALSO FAILED: {str(fallback_error)}")
            import traceback
            logger.error(f"Fallback traceback: {traceback.format_exc()}")
            raise

def generate_scheme_of_work_docx(data):
    try:
        return fill_scheme_official(data)
    except Exception as e:
        logger.error(f"Error in fill_scheme_official: {str(e)}")
        raise
