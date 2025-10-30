"""Document Generator - Uses Official RTB Templates"""
from official_template_filler import fill_session_plan_official, fill_scheme_official
import logging

logger = logging.getLogger(__name__)

def generate_session_plan_docx(data):
    try:
        logger.info("Calling fill_session_plan_official")
        result = fill_session_plan_official(data)
        logger.info(f"fill_session_plan_official returned: {result}")
        return result
    except Exception as e:
        logger.error(f"Error in fill_session_plan_official: {str(e)}")
        raise

def generate_scheme_of_work_docx(data):
    try:
        return fill_scheme_official(data)
    except Exception as e:
        logger.error(f"Error in fill_scheme_official: {str(e)}")
        raise
