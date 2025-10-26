from docx import Document
from docx.shared import Pt, Inches, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import tempfile
import os
import logging
import subprocess
import platform

logger = logging.getLogger(__name__)

try:
    from rtb_template_generator import generate_session_plan_from_template, generate_scheme_of_work_from_template
    
    def fill_session_plan_template(data):
        return generate_session_plan_from_template(data)
    
    def fill_scheme_template(data):
        return generate_scheme_of_work_from_template(data)
    
    USE_TEMPLATES = True
except ImportError:
    try:
        from rtb_template_filler_exact import fill_session_plan_template, fill_scheme_template
        USE_TEMPLATES = True
    except ImportError:
        try:
            from rtb_template_filler import fill_session_plan_template, fill_scheme_template
            USE_TEMPLATES = True
        except ImportError:
            USE_TEMPLATES = False

try:
    from docx2pdf.convert import convert as docx2pdf_convert
    HAS_DOCX2PDF = True
except ImportError:
    HAS_DOCX2PDF = False

def convert_docx_to_pdf(docx_path, pdf_path=None):
    """Convert DOCX file to PDF"""
    if not os.path.exists(docx_path):
        raise FileNotFoundError(f"DOCX file not found: {docx_path}")
    
    if pdf_path is None:
        pdf_path = docx_path.replace('.docx', '.pdf')
    
    try:
        if HAS_DOCX2PDF:
            logger.info(f"Converting {docx_path} to PDF using docx2pdf")
            docx2pdf_convert(docx_path, pdf_path)
            
            if os.path.exists(pdf_path):
                logger.info(f"PDF created successfully: {pdf_path}")
                return pdf_path
            else:
                raise RuntimeError("PDF conversion failed - output file not created")
        else:
            logger.warning("docx2pdf not available, attempting LibreOffice conversion")
            return convert_docx_to_pdf_libreoffice(docx_path, pdf_path)
            
    except Exception as e:
        logger.error(f"Error converting DOCX to PDF: {str(e)}")
        raise

def convert_docx_to_pdf_libreoffice(docx_path, pdf_path):
    """Convert DOCX to PDF using LibreOffice (fallback)"""
    try:
        if platform.system() == "Windows":
            libreoffice_paths = [
                r"C:\Program Files\LibreOffice\program\soffice.exe",
                r"C:\Program Files (x86)\LibreOffice\program\soffice.exe",
            ]
        elif platform.system() == "Darwin":
            libreoffice_paths = [
                "/Applications/LibreOffice.app/Contents/MacOS/soffice"
            ]
        else:
            libreoffice_paths = [
                "/usr/bin/libreoffice",
                "/usr/bin/soffice",
            ]
        
        libreoffice_cmd = None
        for path in libreoffice_paths:
            if os.path.exists(path):
                libreoffice_cmd = path
                break
        
        if not libreoffice_cmd:
            logger.warning("LibreOffice not found on system")
            raise RuntimeError("No PDF converter available (install docx2pdf or LibreOffice)")
        
        output_dir = os.path.dirname(pdf_path)
        cmd = [
            libreoffice_cmd,
            '--headless',
            '--convert-to', 'pdf',
            '--outdir', output_dir,
            docx_path
        ]
        
        logger.info(f"Converting DOCX to PDF using LibreOffice")
        result = subprocess.run(cmd, capture_output=True, timeout=60)
        
        if result.returncode != 0:
            logger.error(f"LibreOffice conversion failed: {result.stderr.decode()}")
            raise RuntimeError(f"LibreOffice conversion failed")
        
        if os.path.exists(pdf_path):
            logger.info(f"PDF created successfully via LibreOffice: {pdf_path}")
            return pdf_path
        else:
            raise RuntimeError("LibreOffice conversion completed but output file not created")
            
    except Exception as e:
        logger.error(f"LibreOffice conversion error: {str(e)}")
        raise

def set_cell_border(cell, **kwargs):
    """Set cell borders"""
    tc = cell._element
    tcPr = tc.get_or_add_tcPr()
    
    tcBorders = OxmlElement('w:tcBorders')
    for edge in ('top', 'left', 'bottom', 'right'):
        if edge in kwargs:
            edge_data = kwargs.get(edge)
            edge_el = OxmlElement(f'w:{edge}')
            edge_el.set(qn('w:val'), 'single')
            edge_el.set(qn('w:sz'), '4')
            edge_el.set(qn('w:space'), '0')
            edge_el.set(qn('w:color'), '000000')
            tcBorders.append(edge_el)
    tcPr.append(tcBorders)

def set_cell_background(cell, fill):
    """Set cell background color"""
    shading_elm = OxmlElement('w:shd')
    shading_elm.set(qn('w:fill'), fill)
    cell._element.get_or_add_tcPr().append(shading_elm)

def generate_session_plan_docx(data):
    """Generate RTB-compliant session plan document"""
    
    if USE_TEMPLATES:
        try:
            logger.info("Attempting to fill session plan using template filler")
            return fill_session_plan_template(data)
        except (IndexError, ValueError, KeyError) as e:
            logger.error(f"Template filling failed with {type(e).__name__}: {str(e)}, falling back to manual generation")
        except Exception as e:
            logger.error(f"Template filling failed with unexpected error: {str(e)}, falling back to manual generation")
    
    template_path = os.path.join(os.path.dirname(__file__), 'rtb_session_plan_template.docx')
    
    if os.path.exists(template_path) and not USE_TEMPLATES:
        doc = Document(template_path)
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    text = cell.text.lower()
                    if 'sector' in text and data.get('sector'):
                        cell.text = data.get('sector', '')
                    elif 'trade' in text and data.get('trade'):
                        cell.text = data.get('trade', '')
                    elif 'level' in text and data.get('rqf_level'):
                        cell.text = data.get('rqf_level', '')
                    elif 'trainer' in text and data.get('trainer_name'):
                        cell.text = data.get('trainer_name', '')
                    elif 'module' in text and data.get('module_code_title'):
                        cell.text = data.get('module_code_title', '')
                    elif 'term' in text and 'term' in data:
                        cell.text = data.get('term', '')
                    elif 'week' in text and data.get('week'):
                        cell.text = data.get('week', '')
                    elif 'date' in text and data.get('date'):
                        cell.text = data.get('date', '')
                    elif 'class' in text and data.get('class_name'):
                        cell.text = data.get('class_name', '')
                    elif 'trainee' in text and data.get('number_of_trainees'):
                        cell.text = str(data.get('number_of_trainees', ''))
                    elif 'duration' in text and data.get('duration'):
                        cell.text = f"{data.get('duration', '')} minutes"
                    elif 'topic' in text and data.get('topic_of_session'):
                        cell.text = data.get('topic_of_session', '')
                    elif 'learning outcome' in text and data.get('learning_outcomes'):
                        cell.text = data.get('learning_outcomes', '')
                    elif 'indicative' in text and data.get('indicative_contents'):
                        cell.text = data.get('indicative_contents', '')
                    elif 'facilitation' in text and data.get('facilitation_techniques'):
                        cell.text = data.get('facilitation_techniques', '')
    else:
        doc = Document()
        
        sections = doc.sections
        for section in sections:
            section.top_margin = Cm(1.27)
            section.bottom_margin = Cm(1.27)
            section.left_margin = Cm(1.27)
            section.right_margin = Cm(1.27)
        
        header = doc.add_table(rows=3, cols=3)
        header.style = 'Table Grid'
        
        cell_logo = header.cell(0, 0)
        cell_logo.text = 'RTB'
        cell_logo.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_cell_background(cell_logo, 'D9E2F3')
        
        cell_title = header.cell(0, 1)
        p = cell_title.paragraphs[0]
        p.text = 'RWANDA TECHNICAL BOARD (RTB)\nSESSION PLAN'
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.runs[0]
        run.bold = True
        run.font.size = Pt(14)
        set_cell_background(cell_title, 'D9E2F3')
        
        cell_code = header.cell(0, 2)
        cell_code.text = f"Code: {data.get('module_code_title', '')[:20]}"
        set_cell_background(cell_code, 'D9E2F3')
        
        header.cell(1, 0).text = f"Sector: {data.get('sector', '')}"
        header.cell(1, 1).text = f"Trade: {data.get('trade', '')}"
        header.cell(1, 2).text = f"Level: {data.get('rqf_level', '')}"
        
        header.cell(2, 0).text = f"Term: {data.get('term', '')}"
        header.cell(2, 1).text = f"Week: {data.get('week', '')}"
        header.cell(2, 2).text = f"Date: {data.get('date', '')}"
        
        doc.add_paragraph()
        
        content = doc.add_table(rows=12, cols=2)
        content.style = 'Table Grid'
        
        content.columns[0].width = Cm(5)
        content.columns[1].width = Cm(12)
        
        rows_data = [
            ('Sector', data.get('sector', '')),
            ('Trade', data.get('trade', '')),
            ('RQF Level', data.get('rqf_level', '')),
            ('Module', data.get('module_code_title', '')),
            ('Class', data.get('class_name', '')),
            ('Number of Trainees', str(data.get('number_of_trainees', ''))),
            ('Topic', data.get('topic_of_session', '')),
            ('Duration', f"{data.get('duration', '')} minutes"),
            ('Learning Outcomes', data.get('learning_outcomes', '')),
            ('Indicative Contents', data.get('indicative_contents', '')),
            ('Facilitation Techniques', data.get('facilitation_techniques', '')),
            ('Resources', data.get('resources', '')),
        ]
        
        for i, (label, value) in enumerate(rows_data):
            content.rows[i].cells[0].text = label
            content.rows[i].cells[1].text = value
    
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
    doc.save(temp_file.name)
    temp_file.close()
    logger.info(f"Session plan DOCX generated: {temp_file.name}")
    return temp_file.name

def generate_scheme_of_work_docx(data):
    """Generate RTB-compliant scheme of work document"""
    
    if USE_TEMPLATES:
        try:
            logger.info("Attempting to fill scheme of work using template filler")
            return fill_scheme_template(data)
        except (IndexError, ValueError, KeyError) as e:
            logger.error(f"Template filling failed with {type(e).__name__}: {str(e)}, falling back to manual generation")
        except Exception as e:
            logger.error(f"Template filling failed with unexpected error: {str(e)}, falling back to manual generation")
    
    template_path = os.path.join(os.path.dirname(__file__), 'rtb_scheme_template.docx')
    
    if os.path.exists(template_path) and not USE_TEMPLATES:
        doc = Document(template_path)
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    text = cell.text.lower()
                    if 'province' in text and data.get('province'):
                        cell.text = data.get('province', '')
                    elif 'district' in text and data.get('district'):
                        cell.text = data.get('district', '')
                    elif 'school' in text and data.get('school'):
                        cell.text = data.get('school', '')
                    elif 'sector' in text and data.get('sector'):
                        cell.text = data.get('sector', '')
                    elif 'trade' in text and data.get('trade'):
                        cell.text = data.get('trade', '')
                    elif 'module' in text and data.get('module_code_title'):
                        cell.text = data.get('module_code_title', '')
                    elif 'level' in text and data.get('rqf_level'):
                        cell.text = data.get('rqf_level', '')
                    elif 'year' in text and data.get('school_year'):
                        cell.text = data.get('school_year', '')
                    elif 'trainer' in text and data.get('trainer_name'):
                        cell.text = data.get('trainer_name', '')
    else:
        doc = Document()
        
        sections = doc.sections
        for section in sections:
            section.top_margin = Cm(1.27)
            section.bottom_margin = Cm(1.27)
            section.left_margin = Cm(1.27)
            section.right_margin = Cm(1.27)
        
        title = doc.add_heading('SCHEME OF WORK', 0)
        title.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        doc.add_paragraph()
        
        info_table = doc.add_table(rows=10, cols=2)
        info_table.style = 'Table Grid'
        
        info_data = [
            ('Province', data.get('province', '')),
            ('District', data.get('district', '')),
            ('Sector', data.get('sector', '')),
            ('School', data.get('school', '')),
            ('Trade/Department', data.get('department_trade', '')),
            ('Qualification Title', data.get('qualification_title', '')),
            ('RQF Level', data.get('rqf_level', '')),
            ('Module Code & Title', data.get('module_code_title', '')),
            ('School Year', data.get('school_year', '')),
            ('Trainer Name', data.get('trainer_name', '')),
        ]
        
        for i, (label, value) in enumerate(info_data):
            info_table.rows[i].cells[0].text = label
            info_table.rows[i].cells[1].text = value
        
        doc.add_paragraph()
        
        for term_num in [1, 2, 3]:
            weeks = data.get(f'term{term_num}_weeks')
            if weeks:
                doc.add_heading(f'Term {term_num}', level=1)
                
                term_table = doc.add_table(rows=2, cols=4)
                term_table.style = 'Table Grid'
                
                hdr_cells = term_table.rows[0].cells
                hdr_cells[0].text = 'Weeks'
                hdr_cells[1].text = 'Learning Outcomes'
                hdr_cells[2].text = 'Indicative Contents'
                hdr_cells[3].text = 'Duration'
                
                row_cells = term_table.rows[1].cells
                row_cells[0].text = data.get(f'term{term_num}_weeks', '')
                row_cells[1].text = data.get(f'term{term_num}_learning_outcomes', '')
                row_cells[2].text = data.get(f'term{term_num}_indicative_contents', '')
                row_cells[3].text = data.get(f'term{term_num}_duration', '')
        
        doc.add_paragraph()
        
        sig_table = doc.add_table(rows=3, cols=2)
        sig_table.style = 'Table Grid'
        sig_table.rows[0].cells[0].text = 'Trainer Name'
        sig_table.rows[0].cells[1].text = data.get('trainer_name', '')
        sig_table.rows[1].cells[0].text = 'Director of Studies'
        sig_table.rows[1].cells[1].text = data.get('dos_name', '')
        sig_table.rows[2].cells[0].text = 'School Manager'
        sig_table.rows[2].cells[1].text = data.get('manager_name', '')
    
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
    doc.save(temp_file.name)
    temp_file.close()
    logger.info(f"Scheme of work DOCX generated: {temp_file.name}")
    return temp_file.name

def generate_session_plan_pdf(data):
    """Generate RTB Session Plan as PDF"""
    try:
        docx_path = generate_session_plan_docx(data)
        if not docx_path or not os.path.exists(docx_path):
            raise RuntimeError("DOCX generation failed for PDF conversion")
        
        pdf_path = docx_path.replace('.docx', '.pdf')
        pdf_path = convert_docx_to_pdf(docx_path, pdf_path)
        
        if os.path.exists(docx_path):
            os.remove(docx_path)
            logger.info(f"Cleaned up temp DOCX: {docx_path}")
        
        return pdf_path
    except Exception as e:
        logger.error(f"Error generating session plan PDF: {str(e)}")
        raise

def generate_scheme_of_work_pdf(data):
    """Generate RTB Scheme of Work as PDF"""
    try:
        docx_path = generate_scheme_of_work_docx(data)
        if not docx_path or not os.path.exists(docx_path):
            raise RuntimeError("DOCX generation failed for PDF conversion")
        
        pdf_path = docx_path.replace('.docx', '.pdf')
        pdf_path = convert_docx_to_pdf(docx_path, pdf_path)
        
        if os.path.exists(docx_path):
            os.remove(docx_path)
            logger.info(f"Cleaned up temp DOCX: {docx_path}")
        
        return pdf_path
    except Exception as e:
        logger.error(f"Error generating scheme of work PDF: {str(e)}")
        raise
