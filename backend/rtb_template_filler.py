from docx import Document
import tempfile
import os

def fill_session_plan_template(data):
    """Fill RTB session plan template - preserves exact formatting"""
    template_path = os.path.join(os.path.dirname(__file__), 'rtb_session_plan_template.docx')
    
    if not os.path.exists(template_path):
        raise FileNotFoundError("RTB Session Plan template not found")
    
    doc = Document(template_path)
    table = doc.tables[0]
    
    # Fill cells while preserving formatting
    table.rows[1].cells[0].text = f"Sector :    {data.get('sector', '')}"
    table.rows[1].cells[1].text = f"Sub-sector: {data.get('trade', '')}"
    table.rows[1].cells[4].text = f"Date : {data.get('date', '')}"
    
    table.rows[2].cells[0].text = f"Lead Trainer's name : {data.get('trainer_name', '')}"
    table.rows[2].cells[4].text = f"TERM : {data.get('term', '')}"
    
    table.rows[3].cells[0].text = f"Module(Code&Name): {data.get('module_code_title', '')}"
    table.rows[3].cells[1].text = f"Week : {data.get('week', '')}"
    table.rows[3].cells[3].text = f"No. Trainees: {data.get('number_of_trainees', '')}"
    table.rows[3].cells[4].text = f"Class(es): {data.get('class_name', '')}"
    
    table.rows[4].cells[1].text = data.get('learning_outcomes', '')
    table.rows[5].cells[1].text = data.get('indicative_contents', '')
    table.rows[6].cells[0].text = f"Topic of the session: {data.get('topic_of_session', '')}"
    table.rows[7].cells[0].text = f"Range: \n{data.get('indicative_contents', '')}"
    table.rows[7].cells[1].text = f"Duration of the session: {data.get('duration', '')}min"
    table.rows[8].cells[0].text = f"Objectives: By the end of this session every learner should be able to:\n{data.get('objectives', '')}"
    table.rows[9].cells[0].text = f"Facilitation technique(s):   {data.get('facilitation_techniques', '')}"
    
    # Introduction
    intro = f"""Trainer's activity: 
	• Greets and makes roll call
	• Involves learners to set ground rules
	• Involves learners to review previous session
	• Announces topic: {data.get('topic_of_session', '')}
	• Explains objectives

Learner's activity: 
	• Greets and replies to roll call
	• Participates in setting ground rules
	• Participates in review
	• Reads and participates in explaining objectives
	• Asks clarifications if any"""
    table.rows[11].cells[0].text = intro
    table.rows[11].cells[2].text = "Attendance sheet\nPPT\nProjector\nComputers\nFlipchart\nwhiteboard\nMarker pen"
    table.rows[11].cells[5].text = "5 minutes"
    
    # Development
    activities = data.get('learning_activities', f"Development activities for {data.get('topic_of_session', '')}")
    table.rows[13].cells[0].text = activities
    table.rows[13].cells[2].text = data.get('resources', 'Computer\nProjector\nPPT\nInstalled operating system').replace('• ', '')
    table.rows[13].cells[5].text = f"{int(data.get('duration', 40)) - 15}\nminutes"
    
    # Conclusion
    table.rows[17].cells[0].text = "Summary:\nThe trainer involves learners to summarize the session by asking questions reflecting on learning objectives.\nThe learners summarize the session by responding to asked questions."
    table.rows[17].cells[2].text = "Computer \nprojector"
    table.rows[17].cells[5].text = "3 minutes"
    
    # Assessment
    assessment = data.get('assessment_details', f"Trainer gives learners assessment related to {data.get('topic_of_session', '')}")
    table.rows[18].cells[0].text = f"Trainer's activity: \n	{assessment}\n\nLearner's activity:\n	Learners receive assessment and answer questions"
    table.rows[18].cells[2].text = "Assessment sheets"
    table.rows[18].cells[5].text = "5 minutes"
    
    # Evaluation
    table.rows[19].cells[0].text = "Trainer's activity: \n	Trainer involves learners in session evaluation\n	Asks: How was the session? What to improve?\n	Links current session to next one\n\nLearner's activity:\n	Learners answer questions\n	Understand what will be covered in next session"
    table.rows[19].cells[2].text = "Self-assessment form"
    table.rows[19].cells[5].text = "2minutes"
    
    # References
    table.rows[20].cells[0].text = f"References:\nBibliography\n\n{data.get('references', '(To be added by trainer)')}"
    table.rows[21].cells[0].text = "Appendices: PPT, Task Sheets, assessment,"
    table.rows[22].cells[0].text = "Reflection :"
    
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
    doc.save(temp_file.name)
    temp_file.close()
    
    return temp_file.name

def fill_scheme_template(data):
    """Fill RTB scheme of work template - all 3 terms"""
    template_path = os.path.join(os.path.dirname(__file__), 'rtb_scheme_template.docx')
    
    if not os.path.exists(template_path):
        raise FileNotFoundError("RTB Scheme template not found")
    
    doc = Document(template_path)
    
    # Fill all 3 term tables
    for term_idx in range(min(3, len(doc.tables))):
        term_num = term_idx + 1
        table = doc.tables[term_idx]
        
        if len(table.rows) > 2:
            # Fill data row (row 2)
            table.rows[2].cells[0].text = data.get(f'term{term_num}_weeks', '')
            table.rows[2].cells[1].text = data.get(f'term{term_num}_learning_outcomes', '')
            table.rows[2].cells[2].text = data.get(f'term{term_num}_duration', '')
            table.rows[2].cells[3].text = data.get(f'term{term_num}_indicative_contents', '')
    
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
    doc.save(temp_file.name)
    temp_file.close()
    
    return temp_file.name
