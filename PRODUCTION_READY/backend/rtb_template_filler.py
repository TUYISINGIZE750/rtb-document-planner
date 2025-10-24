from docx import Document
import tempfile
import os

def fill_session_plan_template(data):
    """Fill RTB session plan template with exact user data matching RTB format"""
    template_path = os.path.join(os.path.dirname(__file__), 'rtb_session_plan_template.docx')
    
    if not os.path.exists(template_path):
        raise FileNotFoundError("RTB Session Plan template not found")
    
    doc = Document(template_path)
    table = doc.tables[0]  # Main session plan table
    
    # Fill header information (rows 1-3)
    table.rows[1].cells[0].text = f"Sector :    {data.get('sector', '')}"
    table.rows[1].cells[1].text = f"Sub-sector: {data.get('trade', '')}"
    table.rows[1].cells[4].text = f"Date : {data.get('date', '')}"
    
    table.rows[2].cells[0].text = f"Lead Trainer's name : {data.get('trainer_name', '')}"
    table.rows[2].cells[4].text = f"TERM : {data.get('term', '')}"
    
    table.rows[3].cells[0].text = f"Module(Code&Name): {data.get('module_code_title', '')}"
    table.rows[3].cells[1].text = f"Week : {data.get('week', '')}"
    table.rows[3].cells[3].text = f"No. Trainees: {data.get('number_of_trainees', '')}"
    table.rows[3].cells[4].text = f"Class(es): {data.get('class_name', '')}"
    
    # Fill learning content (rows 4-6)
    table.rows[4].cells[1].text = data.get('learning_outcomes', '')
    table.rows[5].cells[1].text = data.get('indicative_contents', '')
    table.rows[6].cells[0].text = f"Topic of the session: {data.get('topic_of_session', '')}"
    
    # Fill range and duration (row 7)
    range_text = f"Range: \n{data.get('indicative_contents', '')}"
    table.rows[7].cells[0].text = range_text
    table.rows[7].cells[1].text = f"Duration of the session: {data.get('duration', '')}min"
    
    # Fill objectives (row 8)
    objectives_text = data.get('objectives', 'Objectives: By the end of this session every learner should be able to:')
    table.rows[8].cells[0].text = objectives_text
    
    # Fill facilitation technique (row 9)
    table.rows[9].cells[0].text = f"Facilitation technique(s):   {data.get('facilitation_techniques', '')}"
    
    # Fill session activities (rows 11, 13-15)
    activities = data.get('learning_activities', '')
    if activities:
        # Introduction (row 11)
        table.rows[11].cells[0].text = "Trainer's activity: \nGreets and Make roll calls\nInvolves the learners to set the ground rules\nIntroduces the session topic"
        table.rows[11].cells[2].text = data.get('resources', 'Attendance sheet\nPPT\nProjector\nComputers\nFlipchart or whiteboard\nMarker pen')
        table.rows[11].cells[5].text = "5 minutes"
        
        # Development/Body (rows 13-15)
        table.rows[13].cells[0].text = activities[:500] + "..." if len(activities) > 500 else activities
        table.rows[13].cells[2].text = data.get('resources', 'Computer\nprojector\nPPT\nInstalled operating system')
        duration_minutes = int(data.get('duration', 40)) - 15  # Total minus intro/conclusion
        table.rows[13].cells[5].text = f"{duration_minutes}\nminutes"
    
    # Fill conclusion and assessment (rows 17-19)
    table.rows[17].cells[0].text = "Summary:\nThe trainer involves the learners to summarize the session by asking questions reflecting on the learning objectives"
    table.rows[17].cells[2].text = "Computer\nprojector"
    table.rows[17].cells[5].text = "3 minutes"
    
    assessment_text = data.get('assessment_details', 'Trainer gives learners assessment questions related to the session topic')
    table.rows[18].cells[0].text = f"Assessment/Assignment\nTrainer's activity: \n{assessment_text}"
    table.rows[18].cells[2].text = "Assessment sheets"
    table.rows[18].cells[5].text = "5 minutes"
    
    table.rows[19].cells[0].text = "Evaluation of the session:\nTrainer's activity: \nTrainer involves learners in the evaluation of the session"
    table.rows[19].cells[2].text = "Self-assessment form"
    table.rows[19].cells[5].text = "2minutes"
    
    # Save to temp file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
    doc.save(temp_file.name)
    temp_file.close()
    
    return temp_file.name

def fill_scheme_template(data):
    """Fill RTB scheme of work template with exact user data matching RTB format"""
    template_path = os.path.join(os.path.dirname(__file__), 'rtb_scheme_template.docx')
    
    if not os.path.exists(template_path):
        raise FileNotFoundError("RTB Scheme template not found")
    
    doc = Document(template_path)
    
    # Fill header information in first table if it exists
    if len(doc.tables) > 0:
        header_table = doc.tables[0]
        if len(header_table.rows) > 2:
            # Fill weeks, learning outcomes, duration, indicative contents
            header_table.rows[2].cells[0].text = data.get('term1_weeks', f"{data.get('date', '')} - End of Term 1")
            header_table.rows[2].cells[1].text = data.get('term1_learning_outcomes', data.get('learning_outcomes', ''))
            header_table.rows[2].cells[2].text = data.get('term1_duration', f"{data.get('duration', '40')} hours")
            header_table.rows[2].cells[3].text = data.get('term1_indicative_contents', data.get('indicative_contents', ''))
            
            # Fill learning activities and resources
            if len(header_table.rows[2].cells) > 4:
                activities = data.get('learning_activities', 'Practical exercises, Group discussions, Individual assignments')
                header_table.rows[2].cells[4].text = activities[:200] + "..." if len(activities) > 200 else activities
                
                resources = data.get('resources', 'Computers, Projector, Textbooks, Internet access')
                header_table.rows[2].cells[5].text = resources[:200] + "..." if len(resources) > 200 else resources
                
                assessment = data.get('assessment_details', 'Continuous assessment, Practical tests, Portfolio assessment')
                header_table.rows[2].cells[6].text = assessment[:150] + "..." if len(assessment) > 150 else assessment
                
                header_table.rows[2].cells[7].text = "Classroom/Lab"
                header_table.rows[2].cells[8].text = "Completed successfully"
    
    # Fill additional term tables if they exist
    if len(doc.tables) > 1:
        table2 = doc.tables[1]
        if len(table2.rows) > 2:
            table2.rows[2].cells[0].text = data.get('term2_weeks', 'Term 2 weeks')
            table2.rows[2].cells[1].text = data.get('term2_learning_outcomes', data.get('learning_outcomes', ''))
            table2.rows[2].cells[2].text = data.get('term2_duration', f"{data.get('duration', '40')} hours")
            table2.rows[2].cells[3].text = data.get('term2_indicative_contents', data.get('indicative_contents', ''))
    
    if len(doc.tables) > 2:
        table3 = doc.tables[2]
        if len(table3.rows) > 2:
            table3.rows[2].cells[0].text = data.get('term3_weeks', 'Term 3 weeks')
            table3.rows[2].cells[1].text = data.get('term3_learning_outcomes', data.get('learning_outcomes', ''))
            table3.rows[2].cells[2].text = data.get('term3_duration', f"{data.get('duration', '40')} hours")
            table3.rows[2].cells[3].text = data.get('term3_indicative_contents', data.get('indicative_contents', ''))
    
    # Save to temp file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
    doc.save(temp_file.name)
    temp_file.close()
    
    return temp_file.name
