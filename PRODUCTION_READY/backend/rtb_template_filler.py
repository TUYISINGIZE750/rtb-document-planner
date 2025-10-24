from docx import Document
import tempfile
import os

def fill_session_plan_template(data):
    """Fill RTB session plan template with teacher's data - EXACT RTB FORMAT"""
    template_path = os.path.join(os.path.dirname(__file__), 'rtb_session_plan_template.docx')
    
    if not os.path.exists(template_path):
        raise FileNotFoundError("RTB Session Plan template not found")
    
    doc = Document(template_path)
    table = doc.tables[0]
    
    # HEADER SECTION
    table.rows[1].cells[0].text = f"Sector :    {data.get('sector', '')}"
    table.rows[1].cells[1].text = f"Sub-sector: {data.get('trade', '')}"
    table.rows[1].cells[4].text = f"Date : {data.get('date', '')}"
    
    table.rows[2].cells[0].text = f"Lead Trainer's name : {data.get('trainer_name', '')}"
    table.rows[2].cells[4].text = f"TERM : {data.get('term', '')}"
    
    table.rows[3].cells[0].text = f"Module(Code&Name): {data.get('module_code_title', '')}"
    table.rows[3].cells[1].text = f"Week : {data.get('week', '')}"
    table.rows[3].cells[3].text = f"No. Trainees: {data.get('number_of_trainees', '')}"
    table.rows[3].cells[4].text = f"Class(es): {data.get('class_name', '')}"
    
    # LEARNING CONTENT
    table.rows[4].cells[0].text = "Learning outcome:"
    table.rows[4].cells[1].text = data.get('learning_outcomes', '')
    
    table.rows[5].cells[0].text = "Indicative contents:"
    table.rows[5].cells[1].text = data.get('indicative_contents', '')
    
    table.rows[6].cells[0].text = f"Topic of the session: {data.get('topic_of_session', '')}"
    
    # RANGE AND DURATION
    table.rows[7].cells[0].text = f"Range: \\n{data.get('indicative_contents', '')}"
    table.rows[7].cells[1].text = f"Duration of the session: {data.get('duration', '')}min"
    
    # OBJECTIVES
    objectives = data.get('objectives', '')
    table.rows[8].cells[0].text = f"Objectives: By the end of this session every learner should be able to:\\n{objectives}"
    
    # FACILITATION TECHNIQUE
    table.rows[9].cells[0].text = f"Facilitation technique(s):   {data.get('facilitation_techniques', '')}"
    
    # INTRODUCTION
    intro_text = f"""Trainer's activity: 
\t• Greets and makes roll call
\t• Involves learners to set ground rules
\t• Involves learners to review previous session
\t• Announces topic: {data.get('topic_of_session', '')}
\t• Explains objectives

Learner's activity: 
\t• Greets and replies to roll call
\t• Participates in setting ground rules
\t• Participates in review
\t• Reads and participates in explaining objectives
\t• Asks clarifications if any"""
    
    table.rows[11].cells[0].text = intro_text
    table.rows[11].cells[2].text = "Attendance sheet\\nPPT\\nProjector\\nComputers\\nFlipchartwhiteboard\\nMarker pen"
    table.rows[11].cells[5].text = "5 minutes"
    
    # DEVELOPMENT/BODY - Use AI generated activities
    activities = data.get('learning_activities', '')
    if activities:
        table.rows[13].cells[0].text = activities
    else:
        table.rows[13].cells[0].text = f"Development activities for {data.get('topic_of_session', '')}"
    
    resources = data.get('resources', '')
    if resources:
        table.rows[13].cells[2].text = resources.replace("• ", "")
    else:
        table.rows[13].cells[2].text = "Computer\\nProjector\\nPPT\\nInstalled operating system"
    
    duration_main = int(data.get('duration', 40)) - 15
    table.rows[13].cells[5].text = f"{duration_main}\\nminutes"
    
    # CONCLUSION
    conclusion_text = f"""Summary:
The trainer involves learners to summarize the session by asking questions reflecting on learning objectives.
The learners summarize the session by responding to asked questions."""
    
    table.rows[17].cells[0].text = conclusion_text
    table.rows[17].cells[2].text = "Computer\\nProjector"
    table.rows[17].cells[5].text = "3 minutes"
    
    # ASSESSMENT
    assessment = data.get('assessment_details', '')
    if assessment:
        assessment_text = f"""Trainer's activity: 
\t{assessment}

Learner's activity:
\tLearners receive assessment and answer questions"""
    else:
        assessment_text = f"""Trainer's activity: 
\tTrainer gives learners assessment related to {data.get('topic_of_session', '')}

Learner's activity:
\tLearners receive assessment and answer questions"""
    
    table.rows[18].cells[0].text = assessment_text
    table.rows[18].cells[2].text = "Assessment sheets"
    table.rows[18].cells[5].text = "5 minutes"
    
    # EVALUATION
    evaluation_text = """Trainer's activity: 
\tTrainer involves learners in session evaluation
\tAsks: How was the session? What to improve?
\tLinks current session to next one

Learner's activity:
\tLearners answer questions
\tUnderstand what will be covered in next session"""
    
    table.rows[19].cells[0].text = evaluation_text
    table.rows[19].cells[2].text = "Self-assessment form"
    table.rows[19].cells[5].text = "2 minutes"
    
    # REFERENCES
    references = data.get('references', '')
    if references:
        table.rows[20].cells[0].text = f"References:\\nBibliography\\n\\n{references}"
    else:
        table.rows[20].cells[0].text = "References:\\nBibliography\\n\\n(To be added by trainer)"
    
    # APPENDICES
    table.rows[21].cells[0].text = "Appendices: PPT, Task Sheets, Assessment"
    
    # REFLECTION
    table.rows[22].cells[0].text = "Reflection: (To be completed after session)"
    
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
    doc.save(temp_file.name)
    temp_file.close()
    
    return temp_file.name

def fill_scheme_template(data):
    """Fill RTB scheme of work template"""
    template_path = os.path.join(os.path.dirname(__file__), 'rtb_scheme_template.docx')
    
    if not os.path.exists(template_path):
        raise FileNotFoundError("RTB Scheme template not found")
    
    doc = Document(template_path)
    
    if len(doc.tables) > 0:
        header_table = doc.tables[0]
        if len(header_table.rows) > 2:
            header_table.rows[2].cells[0].text = data.get('term1_weeks', '')
            header_table.rows[2].cells[1].text = data.get('term1_learning_outcomes', '')
            header_table.rows[2].cells[2].text = data.get('term1_duration', '')
            header_table.rows[2].cells[3].text = data.get('term1_indicative_contents', '')
    
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
    doc.save(temp_file.name)
    temp_file.close()
    
    return temp_file.name
