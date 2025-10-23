from docx import Document
from docx.shared import Pt, Inches, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import tempfile
import os

try:
    from rtb_template_filler import fill_session_plan_template, fill_scheme_template
    USE_TEMPLATES = True
except ImportError:
    USE_TEMPLATES = False

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
    
    # Use template filler if available
    if USE_TEMPLATES:
        try:
            return fill_session_plan_template(data)
        except Exception as e:
            print(f"Template filling failed: {e}, falling back to manual generation")
    
    # Try to use template first
    template_path = os.path.join(os.path.dirname(__file__), 'rtb_session_plan_template.docx')
    
    if os.path.exists(template_path) and not USE_TEMPLATES:
        doc = Document(template_path)
        # Fill template - simplified approach
        for table in doc.tables:
            for row in table.rows:
                for cell in row.cells:
                    text = cell.text.lower()
                    # Replace placeholders
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
        # Create from scratch with RTB format
        doc = Document()
        
        # Set margins
        sections = doc.sections
        for section in sections:
            section.top_margin = Cm(1.27)
            section.bottom_margin = Cm(1.27)
            section.left_margin = Cm(1.27)
            section.right_margin = Cm(1.27)
        
        # Header table - RTB format
        header = doc.add_table(rows=3, cols=3)
        header.style = 'Table Grid'
        
        # Row 1: Logo, Title, Code
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
        
        # Row 2: Institution details
        header.cell(1, 0).text = f"Sector: {data.get('sector', '')}"
        header.cell(1, 1).text = f"Trade: {data.get('trade', '')}"
        header.cell(1, 2).text = f"Level: {data.get('rqf_level', '')}"
        
        # Row 3: Session details
        header.cell(2, 0).text = f"Term: {data.get('term', '')}"
        header.cell(2, 1).text = f"Week: {data.get('week', '')}"
        header.cell(2, 2).text = f"Date: {data.get('date', '')}"
        
        doc.add_paragraph()
        
        # Main content table
        content = doc.add_table(rows=12, cols=2)
        content.style = 'Table Grid'
        
        # Set column widths
        content.columns[0].width = Cm(5)
        content.columns[1].width = Cm(12)
        
        # Fill content
        rows_data = [
            ('Trainer Name', data.get('trainer_name', '')),
            ('Class Name', data.get('class_name', '')),
            ('Number of Trainees', str(data.get('number_of_trainees', ''))),
            ('Duration', f"{data.get('duration', '')} minutes"),
            ('Module Code & Title', data.get('module_code_title', '')),
            ('Topic of Session', data.get('topic_of_session', '')),
            ('Learning Outcomes', data.get('learning_outcomes', '')),
            ('SMART Objectives', data.get('objectives', '')),
            ('Indicative Contents', data.get('indicative_contents', '')),
            ('Facilitation Technique', data.get('facilitation_techniques', 'Trainer-guided')),
            ('Learning Activities & Steps', data.get('learning_activities', 'Practical exercises, Discussions')),
            ('Resources Required', data.get('resources', 'Textbooks, Computers, Projector')),
            ('Assessment Methods', data.get('assessment_details', 'Formative: Q&A, Observation\nSummative: Practical test'))
        ]
        
        for idx, (label, value) in enumerate(rows_data):
            # Label cell
            label_cell = content.cell(idx, 0)
            label_cell.text = label
            set_cell_background(label_cell, 'E7E6E6')
            for paragraph in label_cell.paragraphs:
                for run in paragraph.runs:
                    run.bold = True
                    run.font.size = Pt(11)
                    run.font.name = 'Calibri'
            
            # Value cell
            value_cell = content.cell(idx, 1)
            value_cell.text = value
            for paragraph in value_cell.paragraphs:
                for run in paragraph.runs:
                    run.font.size = Pt(11)
                    run.font.name = 'Calibri'
    
    # Save to temp file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
    doc.save(temp_file.name)
    temp_file.close()
    
    return temp_file.name

def generate_scheme_of_work_docx(data):
    """Generate RTB-compliant scheme of work document"""
    
    # Use template filler if available
    if USE_TEMPLATES:
        try:
            return fill_scheme_template(data)
        except Exception as e:
            print(f"Template filling failed: {e}, falling back to manual generation")
    
    # Try to use template first
    template_path = os.path.join(os.path.dirname(__file__), 'rtb_scheme_template.docx')
    
    if os.path.exists(template_path) and not USE_TEMPLATES:
        doc = Document(template_path)
        # Fill template
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
        # Create from scratch
        doc = Document()
        
        # Set margins
        sections = doc.sections
        for section in sections:
            section.top_margin = Cm(1.27)
            section.bottom_margin = Cm(1.27)
            section.left_margin = Cm(1.27)
            section.right_margin = Cm(1.27)
        
        # Title
        title = doc.add_heading('SCHEME OF WORK', 0)
        title.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
        doc.add_paragraph()
        
        # Institution details table
        info_table = doc.add_table(rows=10, cols=2)
        info_table.style = 'Table Grid'
        
        info_data = [
            ('Province', data.get('province', '')),
            ('District', data.get('district', '')),
            ('School', data.get('school', '')),
            ('Sector/Trade', data.get('trade', '')),
            ('Qualification Title', data.get('qualification_title', '')),
            ('RQF Level', data.get('rqf_level', '')),
            ('Module Code & Title', data.get('module_code_title', '')),
            ('School Year', data.get('school_year', '')),
            ('Trainer Name', data.get('trainer_name', '')),
            ('Class Name', data.get('class_name', ''))
        ]
        
        for idx, (label, value) in enumerate(info_data):
            label_cell = info_table.cell(idx, 0)
            label_cell.text = label
            set_cell_background(label_cell, 'D9E2F3')
            for paragraph in label_cell.paragraphs:
                for run in paragraph.runs:
                    run.bold = True
                    run.font.size = Pt(11)
            
            info_table.cell(idx, 1).text = value
        
        doc.add_paragraph()
        
        # Term tables
        for term_num in [1, 2, 3]:
            doc.add_heading(f'TERM {term_num}', level=2)
            
            term_table = doc.add_table(rows=4, cols=2)
            term_table.style = 'Table Grid'
            
            term_data = [
                ('Weeks & Dates', data.get(f'term{term_num}_weeks', '')),
                ('Duration', data.get(f'term{term_num}_duration', '')),
                ('Learning Outcomes', data.get(f'term{term_num}_learning_outcomes', '')),
                ('Indicative Contents', data.get(f'term{term_num}_indicative_contents', ''))
            ]
            
            for idx, (label, value) in enumerate(term_data):
                label_cell = term_table.cell(idx, 0)
                label_cell.text = label
                set_cell_background(label_cell, 'E7E6E6')
                for paragraph in label_cell.paragraphs:
                    for run in paragraph.runs:
                        run.bold = True
                
                term_table.cell(idx, 1).text = value
            
            doc.add_paragraph()
        
        # Sign-offs
        doc.add_heading('SIGN-OFFS', level=2)
        sign_table = doc.add_table(rows=2, cols=2)
        sign_table.style = 'Table Grid'
        
        sign_table.cell(0, 0).text = 'Director of Studies'
        sign_table.cell(0, 1).text = data.get('dos_name', '')
        sign_table.cell(1, 0).text = 'School Manager'
        sign_table.cell(1, 1).text = data.get('manager_name', '')
    
    # Save to temp file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
    doc.save(temp_file.name)
    temp_file.close()
    
    return temp_file.name
