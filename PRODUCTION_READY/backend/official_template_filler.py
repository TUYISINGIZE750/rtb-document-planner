"""Official RTB Template Filler - Uses templates from DOCS TO REFER TO folder"""
from docx import Document
from docx.shared import Pt, RGBColor
import os
import tempfile
from datetime import datetime

def set_cell_font(cell, font_name='Bookman Old Style', font_size=12):
    """Set font for all paragraphs and runs in a cell"""
    for paragraph in cell.paragraphs:
        for run in paragraph.runs:
            run.font.name = font_name
            run.font.size = Pt(font_size)
        # If no runs, add one with the text
        if not paragraph.runs and paragraph.text:
            run = paragraph.add_run(paragraph.text)
            paragraph.text = ''
            run.font.name = font_name
            run.font.size = Pt(font_size)

def fill_session_plan_official(data):
    """Fill RTB Session plan template.docx from RTB Templates folder"""
    import sys
    import logging
    logger = logging.getLogger(__name__)
    
    if data is None:
        logger.error("❌ Data is None!")
        raise ValueError("Data cannot be None")
    
    logger.info(f"🐍 Python version: {sys.version}")
    logger.info(f"📂 Current file: {__file__}")
    logger.info(f"📂 Current dir: {os.getcwd()}")
    logger.info(f"📊 Data type: {type(data)}")
    logger.info(f"📊 Data keys: {list(data.keys()) if isinstance(data, dict) else 'NOT A DICT'}")
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    logger.info(f"📂 Base dir: {base_dir}")
    
    # List files in base directory
    try:
        files = os.listdir(base_dir)
        logger.info(f"📂 Files in base dir: {files[:10]}")
    except Exception as e:
        logger.error(f"❌ Cannot list base dir: {e}")
    
    # Check if RTB Templates folder exists
    rtb_folder = os.path.join(base_dir, 'RTB Templates')
    logger.info(f"📂 RTB Templates path: {rtb_folder}")
    logger.info(f"📂 RTB Templates exists: {os.path.exists(rtb_folder)}")
    
    if os.path.exists(rtb_folder):
        try:
            template_files = os.listdir(rtb_folder)
            logger.info(f"📂 Files in RTB Templates: {template_files}")
        except Exception as e:
            logger.error(f"❌ Cannot list RTB Templates: {e}")
    
    template_path = os.path.join(base_dir, 'RTB Templates', 'RTB Session plan template.docx')
    logger.info(f"📂 Full template path: {template_path}")
    logger.info(f"📂 Template exists: {os.path.exists(template_path)}")
    
    if not os.path.exists(template_path):
        logger.warning(f"⚠️ Template not found, creating simple document")
        # Fallback: create simple document
        doc = Document()
        doc.add_heading('RTB Session Plan', 0)
        doc.add_paragraph(f"Topic: {data.get('topic_of_session', '')}")
        doc.add_paragraph(f"Objectives: {data.get('objectives', '')}")
        doc.add_paragraph(f"Learning Activities: {data.get('learning_activities', '')}")
        doc.add_paragraph(f"Assessment: {data.get('assessment_details', '')}")
        doc.add_paragraph(f"References: {data.get('references', '')}")
        
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
        doc.save(temp_file.name)
        temp_file.close()
        logger.info(f"✅ Fallback document created: {temp_file.name}")
        return temp_file.name
    
    try:
        doc = Document(template_path)
        logger.info(f"✅ Template loaded, tables: {len(doc.tables)}")
        
        if not doc.tables:
            raise Exception("No table found in template")
    except Exception as e:
        logger.error(f"❌ Error loading template: {str(e)}")
        raise
    
    if not doc.tables:
        logger.error("❌ No tables in template!")
        raise Exception("Template has no tables")
    
    table = doc.tables[0]
    logger.info(f"✅ Table found with {len(table.rows)} rows")
    
    # Row 1: Sector, Sub-sector, Trade, Date
    table.rows[1].cells[0].text = f"Sector : {data.get('sector', '') if data else ''}"
    set_cell_font(table.rows[1].cells[0])
    table.rows[1].cells[1].text = f"Sub-sector: {data.get('sub_sector', '')}"
    set_cell_font(table.rows[1].cells[1])
    table.rows[1].cells[2].text = f"Trade: {data.get('trade', '')}"
    set_cell_font(table.rows[1].cells[2])
    table.rows[1].cells[4].text = f"Date : {data.get('date', '')}"
    set_cell_font(table.rows[1].cells[4])
    
    # Row 2: Trainer name, Term
    table.rows[2].cells[0].text = f"Lead Trainer's name : {data.get('trainer_name', '')}"
    set_cell_font(table.rows[2].cells[0])
    table.rows[2].cells[4].text = f"TERM : {data.get('term', '')}"
    set_cell_font(table.rows[2].cells[4])
    
    # Row 3: Module, Week, Learners, Class
    table.rows[3].cells[0].text = f"Module(Code&Name): {data.get('module_code_title', '')}"
    set_cell_font(table.rows[3].cells[0])
    table.rows[3].cells[1].text = f"Week : {data.get('week', '')}"
    set_cell_font(table.rows[3].cells[1])
    table.rows[3].cells[3].text = f"No. Learners: {data.get('number_of_trainees', '')}"
    set_cell_font(table.rows[3].cells[3])
    table.rows[3].cells[4].text = f"Class: {data.get('class_name', '')}"
    set_cell_font(table.rows[3].cells[4])
    
    # Row 4: Learning outcome
    table.rows[4].cells[0].text = "Learning outcome:"
    set_cell_font(table.rows[4].cells[0])
    table.rows[4].cells[1].text = data.get('learning_outcomes', '')
    set_cell_font(table.rows[4].cells[1])
    
    # Row 5: Indicative contents
    table.rows[5].cells[0].text = "Indicative contents:"
    set_cell_font(table.rows[5].cells[0])
    table.rows[5].cells[1].text = data.get('indicative_contents', '')
    set_cell_font(table.rows[5].cells[1])
    
    # Row 6: Topic
    table.rows[6].cells[0].text = f"Topic of the session: {data.get('topic_of_session', '')}"
    set_cell_font(table.rows[6].cells[0])
    
    # Row 7: Duration
    table.rows[7].cells[1].text = f"Duration of the session: {data.get('duration', '')}"
    set_cell_font(table.rows[7].cells[1])
    
    # Row 8: Objectives - LOG IT
    objectives = data.get('objectives', '')
    logger.info(f"📝 Filling objectives: {objectives[:100] if objectives else 'EMPTY'}")
    table.rows[8].cells[0].text = f"Objectives: {objectives}"
    set_cell_font(table.rows[8].cells[0])
    
    # Row 9: Facilitation techniques
    table.rows[9].cells[0].text = f"Facilitation technique(s): {data.get('facilitation_techniques', '')}"
    set_cell_font(table.rows[9].cells[0])
    
    # Row 10: Introduction
    learning_acts = data.get('learning_activities', '')
    resources = data.get('resources', '')
    
    if learning_acts:
        sections = learning_acts.split('\n\n')
        intro = sections[0] if len(sections) > 0 else learning_acts
        table.rows[10].cells[0].text = intro
    set_cell_font(table.rows[10].cells[0])
    
    # Rows 12-14: Development steps
    if learning_acts:
        sections = learning_acts.split('\n\n')
        dev = sections[1] if len(sections) > 1 else learning_acts
        table.rows[12].cells[0].text = dev
    set_cell_font(table.rows[12].cells[0])
    
    # Row 16: Conclusion/Summary
    if learning_acts:
        sections = learning_acts.split('\n\n')
        conclusion = sections[2] if len(sections) > 2 else "Summary"
        table.rows[16].cells[0].text = conclusion
    set_cell_font(table.rows[16].cells[0])
    
    # Row 17: Assessment
    assessment = data.get('assessment_details', '')
    table.rows[17].cells[0].text = assessment if assessment else "Assessment"
    set_cell_font(table.rows[17].cells[0])
    table.rows[18].cells[2].text = "Assessment sheets"
    set_cell_font(table.rows[18].cells[2])
    table.rows[18].cells[5].text = "5 minutes"
    set_cell_font(table.rows[18].cells[5])
    
    # Row 19: References
    references = data.get('references', '')
    table.rows[19].cells[0].text = references if references else "References"
    set_cell_font(table.rows[19].cells[0])
    
    # Save to temp file
    try:
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
        logger.info(f"💾 Saving to: {temp_file.name}")
        doc.save(temp_file.name)
        temp_file.close()
        logger.info(f"✅ Document saved successfully")
        return temp_file.name
    except Exception as e:
        logger.error(f"❌ Error saving document: {str(e)}")
        raise

def fill_scheme_official(data):
    """Fill Scheme of work.docx from RTB Templates folder"""
    template_path = os.path.join(os.path.dirname(__file__), 'RTB Templates', 'Scheme of work.docx')
    doc = Document(template_path)
    
    # Update header paragraphs
    if len(doc.paragraphs) > 3:
        doc.paragraphs[0].text = data.get('province', '')
        doc.paragraphs[1].text = data.get('district', '')
        doc.paragraphs[2].text = data.get('sector', '')
        doc.paragraphs[3].text = data.get('school', '')
    
    # Fill Term 1 table
    if len(doc.tables) > 0:
        table1 = doc.tables[0]
        term1_weeks = data.get('term1_weeks', '').split('\n')
        term1_outcomes = data.get('term1_learning_outcomes', '').split('\n')
        term1_contents = data.get('term1_indicative_contents', '').split('\n')
        term1_duration = data.get('term1_duration', '').split('\n')
        term1_place = data.get('term1_learning_place', '').split('\n')
        
        for i in range(1, min(len(table1.rows), len(term1_weeks) + 1)):
            if i - 1 < len(term1_weeks):
                table1.rows[i].cells[0].text = term1_weeks[i-1]
            if i - 1 < len(term1_outcomes):
                table1.rows[i].cells[1].text = term1_outcomes[i-1]
            if i - 1 < len(term1_contents):
                table1.rows[i].cells[3].text = term1_contents[i-1]
            if i - 1 < len(term1_duration):
                table1.rows[i].cells[4].text = term1_duration[i-1]
            if i - 1 < len(term1_place):
                table1.rows[i].cells[7].text = term1_place[i-1]
    
    # Fill Term 2 table
    if len(doc.tables) > 1:
        table2 = doc.tables[1]
        term2_weeks = data.get('term2_weeks', '').split('\n')
        term2_outcomes = data.get('term2_learning_outcomes', '').split('\n')
        term2_contents = data.get('term2_indicative_contents', '').split('\n')
        term2_duration = data.get('term2_duration', '').split('\n')
        term2_place = data.get('term2_learning_place', '').split('\n')
        
        for i in range(1, min(len(table2.rows), len(term2_weeks) + 1)):
            if i - 1 < len(term2_weeks):
                table2.rows[i].cells[0].text = term2_weeks[i-1]
            if i - 1 < len(term2_outcomes):
                table2.rows[i].cells[1].text = term2_outcomes[i-1]
            if i - 1 < len(term2_contents):
                table2.rows[i].cells[3].text = term2_contents[i-1]
            if i - 1 < len(term2_duration):
                table2.rows[i].cells[4].text = term2_duration[i-1]
            if i - 1 < len(term2_place):
                table2.rows[i].cells[7].text = term2_place[i-1]
    
    # Fill Term 3 table
    if len(doc.tables) > 2:
        table3 = doc.tables[2]
        term3_weeks = data.get('term3_weeks', '').split('\n')
        term3_outcomes = data.get('term3_learning_outcomes', '').split('\n')
        term3_contents = data.get('term3_indicative_contents', '').split('\n')
        term3_duration = data.get('term3_duration', '').split('\n')
        term3_place = data.get('term3_learning_place', '').split('\n')
        
        for i in range(1, min(len(table3.rows), len(term3_weeks) + 1)):
            if i - 1 < len(term3_weeks):
                table3.rows[i].cells[0].text = term3_weeks[i-1]
            if i - 1 < len(term3_outcomes):
                table3.rows[i].cells[1].text = term3_outcomes[i-1]
            if i - 1 < len(term3_contents):
                table3.rows[i].cells[3].text = term3_contents[i-1]
            if i - 1 < len(term3_duration):
                table3.rows[i].cells[4].text = term3_duration[i-1]
            if i - 1 < len(term3_place):
                table3.rows[i].cells[7].text = term3_place[i-1]
    
    # Save to temp file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
    doc.save(temp_file.name)
    temp_file.close()
    return temp_file.name
