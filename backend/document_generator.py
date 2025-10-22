from docx import Document
from docx.shared import Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx2pdf import convert
import tempfile
import os

def generate_session_plan_docx(data):
    """Generate RTB Session Plan DOCX document"""
    doc = Document()
    
    # Header
    header = doc.sections[0].header
    header_para = header.paragraphs[0]
    header_para.text = "REPUBLIC OF RWANDA\nMINISTRY OF EDUCATION\nRWANDA TECHNICAL BOARD (RTB)"
    header_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # Title
    title = doc.add_heading('SESSION PLAN', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # Basic Information Table
    table = doc.add_table(rows=8, cols=4)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Fill basic info
    cells = table.rows[0].cells
    cells[0].text = 'Sector:'
    cells[1].text = data.get('sector', '')
    cells[2].text = 'Sub-Sector:'
    cells[3].text = data.get('sub_sector', '')
    
    cells = table.rows[1].cells
    cells[0].text = 'Trade:'
    cells[1].text = data.get('trade', '')
    cells[2].text = 'Qualification Title:'
    cells[3].text = data.get('qualification_title', '')
    
    cells = table.rows[2].cells
    cells[0].text = 'RQF Level:'
    cells[1].text = data.get('rqf_level', '')
    cells[2].text = 'Module Code & Title:'
    cells[3].text = data.get('module_code_title', '')
    
    cells = table.rows[3].cells
    cells[0].text = 'Term:'
    cells[1].text = data.get('term', '')
    cells[2].text = 'Week:'
    cells[3].text = data.get('week', '')
    
    cells = table.rows[4].cells
    cells[0].text = 'Date:'
    cells[1].text = data.get('date', '')
    cells[2].text = 'Trainer Name:'
    cells[3].text = data.get('trainer_name', '')
    
    cells = table.rows[5].cells
    cells[0].text = 'Class:'
    cells[1].text = data.get('class_name', '')
    cells[2].text = 'Number of Trainees:'
    cells[3].text = data.get('number_of_trainees', '')
    
    cells = table.rows[6].cells
    cells[0].text = 'Learning Outcomes:'
    cells[1].text = data.get('learning_outcomes', '')
    cells[2].text = 'Indicative Contents:'
    cells[3].text = data.get('indicative_contents', '')
    
    cells = table.rows[7].cells
    cells[0].text = 'Topic of Session:'
    cells[1].text = data.get('topic_of_session', '')
    cells[2].text = 'Duration:'
    cells[3].text = data.get('duration', '')
    
    doc.add_paragraph()
    
    # Session Details
    doc.add_heading('Session Details', level=1)
    
    doc.add_heading('Objectives:', level=2)
    doc.add_paragraph(data.get('objectives', ''))
    
    doc.add_heading('Facilitation Techniques:', level=2)
    doc.add_paragraph(data.get('facilitation_techniques', ''))
    
    doc.add_heading('Learning Activities:', level=2)
    doc.add_paragraph(data.get('learning_activities', ''))
    
    doc.add_heading('Resources:', level=2)
    doc.add_paragraph(data.get('resources', ''))
    
    doc.add_heading('Assessment Details:', level=2)
    doc.add_paragraph(data.get('assessment_details', ''))
    
    doc.add_heading('References:', level=2)
    doc.add_paragraph(data.get('references', ''))
    
    # Save to temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
    doc.save(temp_file.name)
    return temp_file.name

def generate_session_plan_pdf(data):
    """Generate RTB Session Plan PDF document"""
    # First generate DOCX
    docx_path = generate_session_plan_docx(data)
    
    # Convert to PDF
    pdf_path = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf').name
    try:
        convert(docx_path, pdf_path)
        # Clean up DOCX file
        os.unlink(docx_path)
        return pdf_path
    except Exception as e:
        # If conversion fails, return DOCX
        return docx_path

def generate_scheme_of_work_docx(data):
    """Generate RTB Scheme of Work DOCX document"""
    doc = Document()
    
    # Header
    header = doc.sections[0].header
    header_para = header.paragraphs[0]
    header_para.text = "REPUBLIC OF RWANDA\nMINISTRY OF EDUCATION\nRWANDA TECHNICAL BOARD (RTB)"
    header_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # Title
    title = doc.add_heading('SCHEME OF WORK', 0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    
    # Basic Information
    doc.add_heading('Basic Information', level=1)
    
    info_table = doc.add_table(rows=6, cols=4)
    info_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    cells = info_table.rows[0].cells
    cells[0].text = 'Province:'
    cells[1].text = data.get('province', '')
    cells[2].text = 'District:'
    cells[3].text = data.get('district', '')
    
    cells = info_table.rows[1].cells
    cells[0].text = 'Sector:'
    cells[1].text = data.get('sector', '')
    cells[2].text = 'School:'
    cells[3].text = data.get('school', '')
    
    cells = info_table.rows[2].cells
    cells[0].text = 'Department/Trade:'
    cells[1].text = data.get('department_trade', '')
    cells[2].text = 'Qualification Title:'
    cells[3].text = data.get('qualification_title', '')
    
    cells = info_table.rows[3].cells
    cells[0].text = 'RQF Level:'
    cells[1].text = data.get('rqf_level', '')
    cells[2].text = 'Module Code & Title:'
    cells[3].text = data.get('module_code_title', '')
    
    cells = info_table.rows[4].cells
    cells[0].text = 'School Year:'
    cells[1].text = data.get('school_year', '')
    cells[2].text = 'Terms:'
    cells[3].text = data.get('terms', '')
    
    cells = info_table.rows[5].cells
    cells[0].text = 'Module Hours:'
    cells[1].text = data.get('module_hours', '')
    cells[2].text = 'Number of Classes:'
    cells[3].text = data.get('number_of_classes', '')
    
    # Term Details
    for term_num in [1, 2, 3]:
        if data.get(f'term{term_num}_weeks'):
            doc.add_heading(f'Term {term_num}', level=1)
            
            term_table = doc.add_table(rows=1, cols=4)
            term_table.alignment = WD_TABLE_ALIGNMENT.CENTER
            
            # Header row
            hdr_cells = term_table.rows[0].cells
            hdr_cells[0].text = 'Weeks'
            hdr_cells[1].text = 'Learning Outcomes'
            hdr_cells[2].text = 'Indicative Contents'
            hdr_cells[3].text = 'Duration'
            
            # Data row
            row_cells = term_table.add_row().cells
            row_cells[0].text = data.get(f'term{term_num}_weeks', '')
            row_cells[1].text = data.get(f'term{term_num}_learning_outcomes', '')
            row_cells[2].text = data.get(f'term{term_num}_indicative_contents', '')
            row_cells[3].text = data.get(f'term{term_num}_duration', '')
    
    # Signatures
    doc.add_heading('Signatures', level=1)
    
    sig_table = doc.add_table(rows=2, cols=2)
    sig_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    cells = sig_table.rows[0].cells
    cells[0].text = 'Trainer Name:'
    cells[1].text = data.get('trainer_name', '')
    
    cells = sig_table.rows[1].cells
    cells[0].text = 'DOS Name:'
    cells[1].text = data.get('dos_name', '')
    
    # Save to temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
    doc.save(temp_file.name)
    return temp_file.name

def generate_scheme_of_work_pdf(data):
    """Generate RTB Scheme of Work PDF document"""
    # First generate DOCX
    docx_path = generate_scheme_of_work_docx(data)
    
    # Convert to PDF
    pdf_path = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf').name
    try:
        convert(docx_path, pdf_path)
        # Clean up DOCX file
        os.unlink(docx_path)
        return pdf_path
    except Exception as e:
        # If conversion fails, return DOCX
        return docx_path