"""Official RTB Template Filler - Uses templates from DOCS TO REFER TO folder"""
from docx import Document
from docx.shared import Pt, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import parse_xml
import os
import tempfile
from datetime import datetime
import base64

def set_cell_font(cell, font_name='Bookman Old Style', font_size=12, bold=False):
    """Set font for all paragraphs and runs in a cell"""
    for paragraph in cell.paragraphs:
        paragraph.paragraph_format.space_before = Pt(0)
        paragraph.paragraph_format.space_after = Pt(0)
        paragraph.paragraph_format.line_spacing = 1.0
        for run in paragraph.runs:
            run.font.name = font_name
            run.font.size = Pt(font_size)
            run.font.bold = bold
        if not paragraph.runs and paragraph.text:
            run = paragraph.add_run(paragraph.text)
            paragraph.text = ''
            run.font.name = font_name
            run.font.size = Pt(font_size)
            run.font.bold = bold

def set_cell_text_with_bold_label(cell, label, value, font_name='Bookman Old Style', font_size=12):
    """Set cell text with bold label and normal value"""
    cell.text = ''
    p = cell.paragraphs[0] if cell.paragraphs else cell.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.0
    
    label_run = p.add_run(label)
    label_run.font.name = font_name
    label_run.font.size = Pt(font_size)
    label_run.font.bold = True
    
    value_run = p.add_run(value.strip())
    value_run.font.name = font_name
    value_run.font.size = Pt(font_size)
    value_run.font.bold = False

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
    
    # Use edited template from OFFICIALRTBTEMPLATES (no shapes)
    parent_dir = os.path.dirname(base_dir)
    template_path = os.path.join(parent_dir, 'OFFICIALRTBTEMPLATES', 'SESSION PLAN TEMPLATES.docx')
    
    # Fallback to old template if new one doesn't exist
    if not os.path.exists(template_path):
        template_path = os.path.join(base_dir, 'RTB Templates', 'RTB Session plan template.docx')
        logger.info(f"⚠️ Using fallback template: {template_path}")
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
    
    # Add header section at top of document
    school_name = data.get('school_name', '')
    province = data.get('province', '')
    district = data.get('district', '')
    sector_loc = data.get('sector_location', '')
    cell_loc = data.get('cell', '')
    village = data.get('village', '')
    
    # Insert header table at beginning
    header_table = doc.add_table(rows=1, cols=3)
    header_table.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # Remove spacing from header table
    for row in header_table.rows:
        for cell in row.cells:
            cell._element.get_or_add_tcPr().append(parse_xml(r'<w:tcMar xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:top w:w="0" w:type="dxa"/><w:bottom w:w="0" w:type="dxa"/></w:tcMar>'))
    
    # LEFT: RTB Logo
    left_cell = header_table.rows[0].cells[0]
    left_para = left_cell.paragraphs[0]
    left_para.alignment = WD_ALIGN_PARAGRAPH.LEFT
    left_para.paragraph_format.space_before = Pt(0)
    left_para.paragraph_format.space_after = Pt(0)
    left_run = left_para.add_run('RWANDA\nTVET BOARD')
    left_run.font.bold = True
    left_run.font.size = Pt(12)
    left_run.font.name = 'Bookman Old Style'
    
    # CENTER: School info
    center_cell = header_table.rows[0].cells[1]
    center_para = center_cell.paragraphs[0]
    center_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    center_para.paragraph_format.space_before = Pt(0)
    center_para.paragraph_format.space_after = Pt(0)
    
    name_run = center_para.add_run(school_name + '\n')
    name_run.font.bold = True
    name_run.font.size = Pt(14)
    name_run.font.name = 'Bookman Old Style'
    
    location_text = f"{province} - {district} - {sector_loc} - {cell_loc} - {village}"
    loc_run = center_para.add_run(location_text)
    loc_run.font.size = Pt(10)
    loc_run.font.name = 'Bookman Old Style'
    
    # RIGHT: School logo
    right_cell = header_table.rows[0].cells[2]
    right_para = right_cell.paragraphs[0]
    right_para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    right_para.paragraph_format.space_before = Pt(0)
    right_para.paragraph_format.space_after = Pt(0)
    
    school_logo_base64 = data.get('school_logo', '')
    if school_logo_base64 and 'base64' in school_logo_base64:
        try:
            logo_data = school_logo_base64.split(',')[1] if ',' in school_logo_base64 else school_logo_base64
            logo_bytes = base64.b64decode(logo_data)
            temp_logo = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
            temp_logo.write(logo_bytes)
            temp_logo.close()
            
            right_run = right_para.add_run()
            right_run.add_picture(temp_logo.name, width=Inches(1.2))
            
            try:
                os.remove(temp_logo.name)
            except:
                pass
            logger.info('✅ School logo added')
        except Exception as e:
            logger.error(f"Logo error: {e}")
            right_run = right_para.add_run('SCHOOL\nLOGO')
            right_run.font.size = Pt(10)
            right_run.font.name = 'Bookman Old Style'
    else:
        right_run = right_para.add_run('SCHOOL\nLOGO')
        right_run.font.size = Pt(10)
        right_run.font.name = 'Bookman Old Style'
    
    # Move header table to beginning
    header_element = header_table._element
    doc._element.body.insert(0, header_element)
    
    # Remove any paragraphs between header and main table
    body = doc._element.body
    elements_to_remove = []
    found_header = False
    for i, element in enumerate(body):
        if element.tag.endswith('tbl') and not found_header:
            found_header = True
        elif found_header and element.tag.endswith('p'):
            elements_to_remove.append(element)
        elif found_header and element.tag.endswith('tbl'):
            break
    
    for element in elements_to_remove:
        body.remove(element)
    
    logger.info('✅ Header table added at top with no spacing')
    
    # Main session plan table (first table after moving header)
    table = doc.tables[1]
    logger.info(f"✅ Main table found with {len(table.rows)} rows")
    
    # Row 0: Bold headers
    set_cell_text_with_bold_label(table.rows[0].cells[0], "Sector: ", data.get('sector', '').strip())
    set_cell_text_with_bold_label(table.rows[0].cells[1], "Trade: ", data.get('trade', '').strip())
    set_cell_text_with_bold_label(table.rows[0].cells[4], "Level: ", data.get('level', 'Level 4').strip())
    set_cell_text_with_bold_label(table.rows[0].cells[5], "Date: ", data.get('date', '').strip())
    
    # Row 1: Bold headers
    set_cell_text_with_bold_label(table.rows[1].cells[0], "Trainer name: ", data.get('trainer_name', '').strip())
    
    # School year and term in cell 5
    cell = table.rows[1].cells[5]
    cell.text = ''
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.0
    
    r1 = p.add_run("School year: ")
    r1.font.bold = True
    r1.font.name = 'Bookman Old Style'
    r1.font.size = Pt(12)
    r2 = p.add_run(data.get('school_year', '2024-2025').strip())
    r2.font.name = 'Bookman Old Style'
    r2.font.size = Pt(12)
    p.add_run('\n')
    r3 = p.add_run("Term: ")
    r3.font.bold = True
    r3.font.name = 'Bookman Old Style'
    r3.font.size = Pt(12)
    r4 = p.add_run(data.get('term', '').strip())
    r4.font.name = 'Bookman Old Style'
    r4.font.size = Pt(12)
    
    # Row 2: Bold headers
    set_cell_text_with_bold_label(table.rows[2].cells[0], "Module (Code&Name): ", data.get('module_code_title', '').strip())
    set_cell_text_with_bold_label(table.rows[2].cells[1], "Week: ", data.get('week', '1').strip())
    set_cell_text_with_bold_label(table.rows[2].cells[4], "No. Trainees: ", data.get('number_of_trainees', '').strip())
    set_cell_text_with_bold_label(table.rows[2].cells[5], "Class(es): ", data.get('class_name', '').strip())
    
    # Row 3: Learning Outcome
    set_cell_font(table.rows[3].cells[0], bold=True)
    table.rows[3].cells[1].text = data.get('learning_outcomes', '').strip()
    set_cell_font(table.rows[3].cells[1])
    
    # Row 4: Indicative content
    set_cell_font(table.rows[4].cells[0], bold=True)
    table.rows[4].cells[1].text = data.get('indicative_contents', '').strip()
    set_cell_font(table.rows[4].cells[1])
    
    # Row 5: Topic
    set_cell_text_with_bold_label(table.rows[5].cells[0], "Topic of the session: ", data.get('topic_of_session', '').strip())
    
    # Row 6: Range and Duration
    range_val = data.get('range', '').strip()
    set_cell_text_with_bold_label(table.rows[6].cells[0], "Range: ", range_val)
    set_cell_text_with_bold_label(table.rows[6].cells[2], "Duration of the session: ", data.get('duration', '').strip())
    
    # Row 7: Objectives
    objectives = data.get('objectives', '').strip()
    logger.info(f"📝 Filling objectives: {objectives[:100] if objectives else 'EMPTY'}")
    set_cell_text_with_bold_label(table.rows[7].cells[0], "Objectives:\n", objectives)
    
    # Row 8: Facilitation techniques
    facilitation = data.get('facilitation_techniques', '').strip()
    logger.info(f"📝 Facilitation: '{facilitation}'")
    if facilitation:
        set_cell_text_with_bold_label(table.rows[8].cells[0], "Facilitation technique(s): ", facilitation)
    else:
        set_cell_text_with_bold_label(table.rows[8].cells[0], "Facilitation technique(s): ", "Trainer Guided")
    
    # Parse learning activities and resources
    learning_acts = data.get('learning_activities', '')
    resources_text = data.get('resources', '')
    
    # Split activities into sections
    sections = learning_acts.split('\n\n') if learning_acts else []
    intro = ''
    dev = ''
    conclusion = ''
    
    for section in sections:
        if 'Introduction:' in section:
            intro = section.replace('Introduction:', '').strip()
        elif 'Development:' in section:
            dev = section.replace('Development:', '').strip()
        elif 'Conclusion:' in section:
            conclusion = section.replace('Conclusion:', '').strip()
    
    # Parse resources
    resource_lines = [r.strip() for r in resources_text.split('\n') if r.strip()] if resources_text else []
    all_resources = ', '.join(resource_lines) if resource_lines else 'Whiteboard, markers, handouts'
    
    # Row 9: Bold headers
    set_cell_font(table.rows[9].cells[0], bold=True)
    set_cell_font(table.rows[9].cells[3], bold=True)
    if len(table.rows[9].cells) > 5:
        set_cell_font(table.rows[9].cells[5], bold=True)
    
    # Row 10: Introduction
    set_cell_text_with_bold_label(table.rows[10].cells[0], "Trainer's activity: ", f"{intro}\n\n")
    cell = table.rows[10].cells[0]
    p = cell.paragraphs[0]
    r = p.add_run("Learner's activity: ")
    r.font.bold = True
    r.font.name = 'Bookman Old Style'
    r.font.size = Pt(12)
    r2 = p.add_run("Participate actively and ask questions")
    r2.font.name = 'Bookman Old Style'
    r2.font.size = Pt(12)
    table.rows[10].cells[3].text = all_resources
    set_cell_font(table.rows[10].cells[3])
    if len(table.rows[10].cells) > 5:
        table.rows[10].cells[5].text = "5 min"
        set_cell_font(table.rows[10].cells[5])
    
    # Row 11: Bold header
    set_cell_font(table.rows[11].cells[0], bold=True)
    
    # Row 12: Development
    cell = table.rows[12].cells[0]
    cell.text = ''
    p = cell.paragraphs[0]
    r1 = p.add_run("Step 1:\n")
    r1.font.bold = True
    r1.font.name = 'Bookman Old Style'
    r1.font.size = Pt(12)
    r2 = p.add_run("Trainer's activity: ")
    r2.font.bold = True
    r2.font.name = 'Bookman Old Style'
    r2.font.size = Pt(12)
    r3 = p.add_run(f"{dev}\n\n")
    r3.font.name = 'Bookman Old Style'
    r3.font.size = Pt(12)
    r4 = p.add_run("Learner's activity: ")
    r4.font.bold = True
    r4.font.name = 'Bookman Old Style'
    r4.font.size = Pt(12)
    r5 = p.add_run("Practice and apply concepts")
    r5.font.name = 'Bookman Old Style'
    r5.font.size = Pt(12)
    table.rows[12].cells[3].text = all_resources
    set_cell_font(table.rows[12].cells[3])
    if len(table.rows[12].cells) > 5:
        table.rows[12].cells[5].text = "30 min"
        set_cell_font(table.rows[12].cells[5])
    
    # Row 15: Bold header
    set_cell_font(table.rows[15].cells[0], bold=True)
    
    # Row 16: Conclusion
    set_cell_text_with_bold_label(table.rows[16].cells[0], "Summary: ", conclusion)
    table.rows[16].cells[3].text = all_resources
    set_cell_font(table.rows[16].cells[3])
    if len(table.rows[16].cells) > 5:
        table.rows[16].cells[5].text = "5 min"
        set_cell_font(table.rows[16].cells[5])
    
    # Row 17: Assessment - bold header
    assessment = data.get('assessment_details', '').strip()
    table.rows[17].cells[0].text = assessment
    set_cell_font(table.rows[17].cells[0])
    table.rows[17].cells[3].text = "Assessment sheets"
    set_cell_font(table.rows[17].cells[3])
    if len(table.rows[17].cells) > 5:
        table.rows[17].cells[5].text = "5 min"
        set_cell_font(table.rows[17].cells[5])
    
    # Row 19: References
    references = data.get('references', '').strip()
    set_cell_text_with_bold_label(table.rows[19].cells[0], "References:\n", references)
    
    # Row 18: Evaluation of the session
    evaluation = data.get('evaluation', '').strip()
    if not evaluation:
        evaluation = "Self-assessment form"
    set_cell_text_with_bold_label(table.rows[18].cells[0], "Evaluation of the session: ", evaluation)
    
    # Row 20: Appendices
    appendix = data.get('appendix', '').strip()
    if not appendix:
        appendix = "PPT, Task Sheets, Assessment"
    set_cell_text_with_bold_label(table.rows[20].cells[0], "Appendices:\n", appendix)
    
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
    import logging
    logger = logging.getLogger(__name__)
    
    logger.info("=== SCHEME GENERATION START ===")
    logger.info(f"Current dir: {os.getcwd()}")
    logger.info(f"File location: {__file__}")
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    logger.info(f"Base dir: {base_dir}")
    
    template_path = os.path.join(base_dir, 'RTB Templates', 'Scheme of work.docx')
    logger.info(f"Template path: {template_path}")
    logger.info(f"Template exists: {os.path.exists(template_path)}")
    
    # List files in base dir
    try:
        files = os.listdir(base_dir)
        logger.info(f"Files in base dir: {files}")
    except Exception as e:
        logger.error(f"Cannot list base dir: {e}")
    
    # Check RTB Templates folder
    rtb_folder = os.path.join(base_dir, 'RTB Templates')
    if os.path.exists(rtb_folder):
        try:
            rtb_files = os.listdir(rtb_folder)
            logger.info(f"Files in RTB Templates: {rtb_files}")
        except Exception as e:
            logger.error(f"Cannot list RTB Templates: {e}")
    else:
        logger.error(f"RTB Templates folder not found: {rtb_folder}")
    
    if not os.path.exists(template_path):
        logger.error(f"Template not found: {template_path}")
        logger.error("Creating fallback document...")
        doc = Document()
        doc.add_heading('Scheme of Work', 0)
        doc.add_paragraph(f"Province: {data.get('province', '')}")
        doc.add_paragraph(f"District: {data.get('district', '')}")
        doc.add_paragraph(f"School: {data.get('school', '')}")
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
        doc.save(temp_file.name)
        temp_file.close()
        return temp_file.name
    
    doc = Document(template_path)
    logger.info(f"Scheme template loaded, tables: {len(doc.tables)}")
    
    # Add school header at top
    school_name = data.get('school', '')
    province = data.get('province', '')
    district = data.get('district', '')
    
    header_table = doc.add_table(rows=1, cols=3)
    header_table.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # Remove spacing from header table
    for row in header_table.rows:
        for cell in row.cells:
            cell._element.get_or_add_tcPr().append(parse_xml(r'<w:tcMar xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:top w:w="0" w:type="dxa"/><w:bottom w:w="0" w:type="dxa"/></w:tcMar>'))
    
    # LEFT: RTB Logo
    left_cell = header_table.rows[0].cells[0]
    left_para = left_cell.paragraphs[0]
    left_para.alignment = WD_ALIGN_PARAGRAPH.LEFT
    left_para.paragraph_format.space_before = Pt(0)
    left_para.paragraph_format.space_after = Pt(0)
    left_run = left_para.add_run('RWANDA\nTVET BOARD')
    left_run.font.bold = True
    left_run.font.size = Pt(12)
    left_run.font.name = 'Bookman Old Style'
    
    # CENTER: School info
    center_cell = header_table.rows[0].cells[1]
    center_para = center_cell.paragraphs[0]
    center_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    center_para.paragraph_format.space_before = Pt(0)
    center_para.paragraph_format.space_after = Pt(0)
    
    name_run = center_para.add_run(school_name + '\n')
    name_run.font.bold = True
    name_run.font.size = Pt(14)
    name_run.font.name = 'Bookman Old Style'
    
    location_text = f"{province} - {district}"
    loc_run = center_para.add_run(location_text)
    loc_run.font.size = Pt(10)
    loc_run.font.name = 'Bookman Old Style'
    
    # RIGHT: School logo placeholder
    right_cell = header_table.rows[0].cells[2]
    right_para = right_cell.paragraphs[0]
    right_para.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    right_para.paragraph_format.space_before = Pt(0)
    right_para.paragraph_format.space_after = Pt(0)
    right_run = right_para.add_run('SCHOOL\nLOGO')
    right_run.font.size = Pt(10)
    right_run.font.name = 'Bookman Old Style'
    
    # Move header table to beginning
    header_element = header_table._element
    doc._element.body.insert(0, header_element)
    
    # Remove any paragraphs between header and main table
    body = doc._element.body
    elements_to_remove = []
    found_header = False
    for i, element in enumerate(body):
        if element.tag.endswith('tbl') and not found_header:
            found_header = True
        elif found_header and element.tag.endswith('p'):
            elements_to_remove.append(element)
        elif found_header and element.tag.endswith('tbl'):
            break
    
    for element in elements_to_remove:
        body.remove(element)
    
    logger.info('Header table added to scheme with no spacing')
    
    # Fill header table (Table 1 now) - Match exact RTB template structure
    if len(doc.tables) > 1:
        h = doc.tables[1]
        try:
            # Row 0: Sector (cell 1), Trainer (cell 3)
            h.rows[0].cells[1].text = data.get('sector') or ''
            h.rows[0].cells[3].text = data.get('trainer_name') or ''
            
            # Row 1: Trade (cell 1), School Year (cell 3)
            h.rows[1].cells[1].text = data.get('department_trade') or data.get('trade') or ''
            h.rows[1].cells[3].text = data.get('school_year') or ''
            
            # Row 2: Qualification (cell 1), Term (cell 3)
            h.rows[2].cells[1].text = data.get('qualification_title') or ''
            h.rows[2].cells[3].text = data.get('terms') or ''
            
            # Row 3: RQF Level (cell 1)
            h.rows[3].cells[1].text = data.get('rqf_level') or ''
            
            # Row 4: Module code and title (cell 3)
            h.rows[4].cells[3].text = data.get('module_code_title') or ''
            
            # Row 5: Learning hours (cell 3)
            h.rows[5].cells[3].text = data.get('module_hours') or ''
            
            # Row 6: Number of Classes (cell 3)
            h.rows[6].cells[3].text = data.get('number_of_classes') or ''
            
            # Row 7: Date (cell 1), Class Name (cell 3)
            h.rows[7].cells[1].text = datetime.now().strftime('%d/%m/%Y')
            h.rows[7].cells[3].text = data.get('class_name') or ''
            
            logger.info("Header table filled successfully")
        except Exception as e:
            logger.error(f"Error filling header: {e}")
            import traceback
            logger.error(traceback.format_exc())
    
    # Fill Term 1 table
    if len(doc.tables) > 2:
        table1 = doc.tables[2]
        term1_weeks = (data.get('term1_weeks') or '').strip()
        term1_outcomes_raw = (data.get('term1_learning_outcomes') or '').strip()
        term1_contents_raw = (data.get('term1_indicative_contents') or '').strip()
        term1_duration = (data.get('term1_duration') or '').strip()
        term1_place = (data.get('term1_learning_place') or '').strip()
        
        # Split by newline and filter empty lines
        term1_outcomes = [lo.strip() for lo in term1_outcomes_raw.replace('\r\n', '\n').split('\n') if lo.strip()]
        term1_contents = [ic.strip() for ic in term1_contents_raw.replace('\r\n', '\n').split('\n') if ic.strip()]
        
        logger.info(f"Term 1: {len(term1_outcomes)} LOs, {len(term1_contents)} ICs")
        
        # Keep existing rows and fill them, add more if needed
        data_row_start = 2
        for i, (lo, ic) in enumerate(zip(term1_outcomes, term1_contents)):
            row_idx = data_row_start + i
            
            # Add row if needed
            if row_idx >= len(table1.rows):
                # Copy structure from row 2 (first data row)
                from copy import deepcopy
                new_row = deepcopy(table1.rows[2]._element)
                table1._element.append(new_row)
            
            row = table1.rows[row_idx]
            row.cells[0].text = term1_weeks
            row.cells[1].text = lo
            row.cells[2].text = term1_duration
            row.cells[3].text = ic
            if len(row.cells) > 7:
                row.cells[7].text = term1_place
            logger.info(f"  Term 1 Row {row_idx}: {lo[:30]}")
    
    # Fill Term 2 table
    if len(doc.tables) > 3:
        table2 = doc.tables[3]
        term2_weeks = (data.get('term2_weeks') or '').strip()
        term2_outcomes_raw = (data.get('term2_learning_outcomes') or '').strip()
        term2_contents_raw = (data.get('term2_indicative_contents') or '').strip()
        term2_duration = (data.get('term2_duration') or '').strip()
        term2_place = (data.get('term2_learning_place') or '').strip()
        
        term2_outcomes = [lo.strip() for lo in term2_outcomes_raw.replace('\r\n', '\n').split('\n') if lo.strip()]
        term2_contents = [ic.strip() for ic in term2_contents_raw.replace('\r\n', '\n').split('\n') if ic.strip()]
        
        logger.info(f"Term 2: {len(term2_outcomes)} LOs, {len(term2_contents)} ICs")
        
        # Fill existing rows, add more if needed
        data_row_start = 2
        for i, (lo, ic) in enumerate(zip(term2_outcomes, term2_contents)):
            row_idx = data_row_start + i
            
            if row_idx >= len(table2.rows):
                from copy import deepcopy
                new_row = deepcopy(table2.rows[2]._element)
                table2._element.append(new_row)
            
            row = table2.rows[row_idx]
            row.cells[0].text = term2_weeks
            row.cells[1].text = lo
            row.cells[2].text = term2_duration
            row.cells[3].text = ic
            if len(row.cells) > 7:
                row.cells[7].text = term2_place
            logger.info(f"  Term 2 Row {row_idx}: {lo[:30]}")
    
    # Fill Term 3 table
    if len(doc.tables) > 4:
        table3 = doc.tables[4]
        term3_weeks = (data.get('term3_weeks') or '').strip()
        term3_outcomes_raw = (data.get('term3_learning_outcomes') or '').strip()
        term3_contents_raw = (data.get('term3_indicative_contents') or '').strip()
        term3_duration = (data.get('term3_duration') or '').strip()
        term3_place = (data.get('term3_learning_place') or '').strip()
        
        term3_outcomes = [lo.strip() for lo in term3_outcomes_raw.replace('\r\n', '\n').split('\n') if lo.strip()]
        term3_contents = [ic.strip() for ic in term3_contents_raw.replace('\r\n', '\n').split('\n') if ic.strip()]
        
        logger.info(f"Term 3: {len(term3_outcomes)} LOs, {len(term3_contents)} ICs")
        
        # Fill existing rows, add more if needed
        data_row_start = 2
        for i, (lo, ic) in enumerate(zip(term3_outcomes, term3_contents)):
            row_idx = data_row_start + i
            
            if row_idx >= len(table3.rows):
                from copy import deepcopy
                new_row = deepcopy(table3.rows[2]._element)
                table3._element.append(new_row)
            
            row = table3.rows[row_idx]
            row.cells[0].text = term3_weeks
            row.cells[1].text = lo
            row.cells[2].text = term3_duration
            row.cells[3].text = ic
            if len(row.cells) > 7:
                row.cells[7].text = term3_place
            logger.info(f"  Term 3 Row {row_idx}: {lo[:30]}")
    
    logger.info("Scheme of work filled successfully")
    
    # Save to temp file
    try:
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
        logger.info(f"Saving to: {temp_file.name}")
        doc.save(temp_file.name)
        temp_file.close()
        
        if os.path.exists(temp_file.name):
            size = os.path.getsize(temp_file.name)
            logger.info(f"Scheme saved successfully: {size} bytes")
        else:
            logger.error("Saved file does not exist!")
        
        return temp_file.name
    except Exception as e:
        logger.error(f"Error saving scheme: {e}")
        import traceback
        logger.error(traceback.format_exc())
        raise
