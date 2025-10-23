from docx import Document
import tempfile
import os

def fill_session_plan_template(data):
    """Fill RTB session plan template with user data"""
    template_path = os.path.join(os.path.dirname(__file__), 'rtb_session_plan_template.docx')
    
    if not os.path.exists(template_path):
        raise FileNotFoundError("RTB Session Plan template not found")
    
    doc = Document(template_path)
    
    # Get the main table (first table)
    table = doc.tables[0]
    
    # Row 2: Sector, Sub-sector, Date
    table.rows[1].cells[0].text = f"Sector :    {data.get('sector', '')}"
    table.rows[1].cells[1].text = f"Sub-sector: {data.get('trade', '')}"
    table.rows[1].cells[4].text = f"Date : {data.get('date', '')}"
    
    # Row 3: Trainer name, Term
    table.rows[2].cells[0].text = f"Lead Trainer's name : {data.get('trainer_name', '')}"
    table.rows[2].cells[4].text = f"TERM : {data.get('term', '')}"
    
    # Row 4: Module, Week, Trainees, Class
    table.rows[3].cells[0].text = f"Module(Code&Name): {data.get('module_code_title', '')}"
    table.rows[3].cells[1].text = f"Week : {data.get('week', '')}"
    table.rows[3].cells[3].text = f"No. Trainees: {data.get('number_of_trainees', '')}"
    table.rows[3].cells[4].text = f"Class(es): {data.get('class_name', '')}"
    
    # Row 5: Learning outcome
    table.rows[4].cells[1].text = data.get('learning_outcomes', '')
    
    # Row 6: Indicative contents
    table.rows[5].cells[1].text = data.get('indicative_contents', '')
    
    # Row 7: Topic
    table.rows[6].cells[0].text = f"Topic of the session: {data.get('topic_of_session', '')}"
    
    # Row 8: Range and Duration
    table.rows[7].cells[1].text = f"Duration of the session: {data.get('duration', '')}min"
    
    # Row 10: Facilitation technique
    table.rows[9].cells[0].text = f"Facilitation technique(s):   {data.get('facilitation_techniques', '')}"
    
    # Row 11-12: SMART Objectives (if available)
    if data.get('objectives'):
        table.rows[10].cells[1].text = data.get('objectives', '')
    
    # Row 13-15: Learning Activities (if available)
    if data.get('learning_activities'):
        table.rows[12].cells[1].text = data.get('learning_activities', '')
    
    # Row 16-17: Resources (if available)
    if data.get('resources'):
        table.rows[15].cells[1].text = data.get('resources', '')
    
    # Row 18-19: Assessment (if available)
    if data.get('assessment_details'):
        table.rows[17].cells[1].text = data.get('assessment_details', '')
    
    # Save to temp file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
    doc.save(temp_file.name)
    temp_file.close()
    
    return temp_file.name

def fill_scheme_template(data):
    """Fill RTB scheme of work template with user data"""
    template_path = os.path.join(os.path.dirname(__file__), 'rtb_scheme_template.docx')
    
    if not os.path.exists(template_path):
        raise FileNotFoundError("RTB Scheme template not found")
    
    doc = Document(template_path)
    
    # Fill Term 1 table (table 0)
    if len(doc.tables) > 0:
        table1 = doc.tables[0]
        # Row 3: Weeks, LO, Duration, IC
        if len(table1.rows) > 2:
            table1.rows[2].cells[0].text = data.get('term1_weeks', '')
            table1.rows[2].cells[1].text = data.get('term1_learning_outcomes', '')
            table1.rows[2].cells[2].text = data.get('term1_duration', '')
            table1.rows[2].cells[3].text = data.get('term1_indicative_contents', '')
    
    # Fill Term 2 table (table 1)
    if len(doc.tables) > 1:
        table2 = doc.tables[1]
        if len(table2.rows) > 2:
            table2.rows[2].cells[0].text = data.get('term2_weeks', '')
            table2.rows[2].cells[1].text = data.get('term2_learning_outcomes', '')
            table2.rows[2].cells[2].text = data.get('term2_duration', '')
            table2.rows[2].cells[3].text = data.get('term2_indicative_contents', '')
    
    # Fill Term 3 table (table 2)
    if len(doc.tables) > 2:
        table3 = doc.tables[2]
        if len(table3.rows) > 2:
            table3.rows[2].cells[0].text = data.get('term3_weeks', '')
            table3.rows[2].cells[1].text = data.get('term3_learning_outcomes', '')
            table3.rows[2].cells[2].text = data.get('term3_duration', '')
            table3.rows[2].cells[3].text = data.get('term3_indicative_contents', '')
    
    # Save to temp file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
    doc.save(temp_file.name)
    temp_file.close()
    
    return temp_file.name
