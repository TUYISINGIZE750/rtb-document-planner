from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml.shared import OxmlElement, qn
from docx.oxml.ns import nsdecls
from docx.oxml import parse_xml
import os
import tempfile

def merge_cells_in_row(table, row_idx, start_col, end_col):
    """Merge cells in a table row"""
    start_cell = table.cell(row_idx, start_col)
    end_cell = table.cell(row_idx, end_col)
    start_cell.merge(end_cell)
    return start_cell

def set_cell_border(cell, **kwargs):
    """Set cell borders"""
    tc = cell._tc
    tcPr = tc.get_or_add_tcPr()
    
    # Create borders element
    tcBorders = tcPr.find(qn('w:tcBorders'))
    if tcBorders is None:
        tcBorders = OxmlElement('w:tcBorders')
        tcPr.append(tcBorders)
    
    for edge in ('top', 'left', 'bottom', 'right'):
        edge_data = kwargs.get(edge)
        if edge_data:
            tag = 'w:{}'.format(edge)
            element = tcBorders.find(qn(tag))
            if element is None:
                element = OxmlElement(tag)
                tcBorders.append(element)
            element.set(qn('w:val'), edge_data['val'])
            element.set(qn('w:sz'), str(edge_data['sz']))
            element.set(qn('w:space'), '0')
            element.set(qn('w:color'), edge_data['color'])

def style_header_cell(cell, text, bold=True, size=12):
    """Style header cells"""
    cell.text = text
    paragraph = cell.paragraphs[0]
    paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = paragraph.runs[0]
    run.font.bold = bold
    run.font.size = Pt(size)
    run.font.name = 'Bookman Old Style'
    
    # Add borders
    set_cell_border(cell, 
                   top={'val': 'single', 'sz': '4', 'color': '000000'},
                   bottom={'val': 'single', 'sz': '4', 'color': '000000'},
                   left={'val': 'single', 'sz': '4', 'color': '000000'},
                   right={'val': 'single', 'sz': '4', 'color': '000000'})

def set_cell_text(cell, text, bold=False):
    """Set cell text with Bookman Old Style 12"""
    para = cell.paragraphs[0]
    run = para.add_run(text)
    run.font.size = Pt(12)
    run.font.name = 'Bookman Old Style'
    run.font.bold = bold
    return cell

def generate_smart_objectives(topic, learning_outcomes, session_range=None, indicative_contents=None):
    """Generate clean SMART objectives"""
    import re
    
    # Clean inputs
    def clean(text):
        if not text:
            return ''
        text = re.sub(r'^\d+\.?\d*\s*', '', str(text), flags=re.MULTILINE)
        text = re.sub(r'\s+', ' ', text)
        return text.strip()
    
    topic = clean(topic) or 'the topic'
    learning_outcomes = clean(learning_outcomes) or ''
    session_range = clean(session_range) or ''
    indicative_contents = clean(indicative_contents) or ''
    
    # Extract key term
    words = [w for w in topic.split() if len(w) > 2]
    key_term = ' '.join(words[-2:]) if len(words) >= 2 else topic
    
    # Determine verbs
    lo = learning_outcomes.lower()
    if 'identify' in lo:
        v1, v2, v3 = 'Define clearly', 'Select properly', 'Name appropriately'
    elif 'write' in lo or 'code' in lo:
        v1, v2, v3 = 'Explain clearly', 'Write correctly', 'Apply properly'
    elif 'demonstrat' in lo:
        v1, v2, v3 = 'Demonstrate properly', 'Perform correctly', 'Execute effectively'
    else:
        v1, v2, v3 = 'Define clearly', 'Identify properly', 'Apply correctly'
    
    # Extract subjects (first 40 chars)
    range_text = session_range[:40] if session_range else 'methods'
    content_text = indicative_contents[:40] if indicative_contents else 'techniques'
    
    # Build objectives
    obj1 = f"{v1} the term {key_term} as used in {learning_outcomes.lower()}."
    obj2 = f"{v2} 2 {range_text.lower()} used in {content_text.lower()}."
    obj3 = f"{v3} 2 {content_text.lower()} as used in {topic.lower()}."
    
    return f"1.\t{obj1}\n2.\t{obj2}\n3.\t{obj3}"

def generate_session_plan_docx(session_plan):
    doc = Document()
    
    # Add RTB Header with logo placeholders
    header_section = doc.sections[0]
    header = header_section.header
    
    # Create header table for logos and title
    header_table = header.add_table(rows=1, cols=3, width=Inches(6.5))
    header_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Left cell - RTB Logo placeholder
    left_cell = header_table.cell(0, 0)
    left_para = left_cell.paragraphs[0]
    left_para.text = "[Click to insert\nRTB LOGO]"
    left_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    left_run = left_para.runs[0]
    left_run.font.size = Pt(8)
    left_run.font.color.rgb = RGBColor(128, 128, 128)
    
    # Center cell - Title
    center_cell = header_table.cell(0, 1)
    center_para = center_cell.paragraphs[0]
    center_para.text = "RWANDA TECHNICAL BOARD\nSESSION PLAN"
    center_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    center_run = center_para.runs[0]
    center_run.font.size = Pt(14)
    center_run.font.bold = True
    center_run.font.color.rgb = RGBColor(0, 51, 102)
    
    # Right cell - School Logo placeholder
    right_cell = header_table.cell(0, 2)
    right_para = right_cell.paragraphs[0]
    right_para.text = "[Click to insert\nSCHOOL LOGO]"
    right_para.alignment = WD_ALIGN_PARAGRAPH.CENTER
    right_run = right_para.runs[0]
    right_run.font.size = Pt(8)
    right_run.font.color.rgb = RGBColor(128, 128, 128)
    
    # Add some space after header
    doc.add_paragraph()
    
    # Create the main table with 6 columns and 22 rows (matching RTB format)
    table = doc.add_table(rows=22, cols=6)
    table.style = 'Table Grid'
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Row 0: Sector, Sub-sector, Date
    style_header_cell(table.cell(0, 0), f"Sector : {session_plan.sector or 'ICT & MULTIMEDIA'}")
    style_header_cell(merge_cells_in_row(table, 0, 1, 3), f"Sub-sector: {session_plan.sub_sector or 'Computer system and architecture'}")
    style_header_cell(merge_cells_in_row(table, 0, 4, 5), f"Date : {session_plan.date or ''}")
    
    # Row 1: Lead Trainer, Term
    style_header_cell(merge_cells_in_row(table, 1, 0, 3), f"Lead Trainers name : {session_plan.trainer_name or ''}")
    style_header_cell(merge_cells_in_row(table, 1, 4, 5), f"TERM : {session_plan.term or ''}")
    
    # Row 2: Module, Week, No. Trainees, Class
    style_header_cell(table.cell(2, 0), f"Module(Code&Name): {session_plan.module_code_title or ''}")
    style_header_cell(merge_cells_in_row(table, 2, 1, 2), f"Week : {session_plan.week or ''}")
    style_header_cell(table.cell(2, 3), f"No. Trainees: {session_plan.number_of_trainees or ''}")
    style_header_cell(merge_cells_in_row(table, 2, 4, 5), f"Class: {session_plan.class_name or ''}")
    
    # Row 3: Learning outcome
    cell = table.cell(3, 0)
    para = cell.paragraphs[0]
    run = para.add_run("Learning outcome:")
    run.font.bold = True
    run.font.size = Pt(12)
    run.font.name = 'Bookman Old Style'
    
    cell = merge_cells_in_row(table, 3, 1, 5)
    para = cell.paragraphs[0]
    run = para.add_run(session_plan.learning_outcomes or '')
    run.font.size = Pt(12)
    run.font.name = 'Bookman Old Style'
    
    # Row 4: Indicative contents
    cell = table.cell(4, 0)
    para = cell.paragraphs[0]
    run = para.add_run("Indicative contents:")
    run.font.bold = True
    run.font.size = Pt(12)
    run.font.name = 'Bookman Old Style'
    
    cell = merge_cells_in_row(table, 4, 1, 5)
    para = cell.paragraphs[0]
    run = para.add_run(session_plan.indicative_contents or '')
    run.font.size = Pt(12)
    run.font.name = 'Bookman Old Style'
    
    # Row 5: Topic of the session
    cell = merge_cells_in_row(table, 5, 0, 5)
    para = cell.paragraphs[0]
    run_bold = para.add_run("Topic of the session: ")
    run_bold.font.bold = True
    run_bold.font.size = Pt(12)
    run_bold.font.name = 'Bookman Old Style'
    run_normal = para.add_run(session_plan.topic_of_session or '')
    run_normal.font.size = Pt(12)
    run_normal.font.name = 'Bookman Old Style'
    
    # Row 6: Range and Duration
    range_text = getattr(session_plan, 'session_range', None) or session_plan.learning_outcomes or ''
    cell = table.cell(6, 0)
    para = cell.paragraphs[0]
    run_bold = para.add_run("Range: \n")
    run_bold.font.bold = True
    run_bold.font.size = Pt(12)
    run_bold.font.name = 'Bookman Old Style'
    run_normal = para.add_run(range_text)
    run_normal.font.size = Pt(12)
    run_normal.font.name = 'Bookman Old Style'
    
    duration_text = f"{session_plan.duration or '40'} minutes" if session_plan.duration else "40 minutes"
    cell = merge_cells_in_row(table, 6, 1, 5)
    para = cell.paragraphs[0]
    run_bold = para.add_run("Duration of the session: ")
    run_bold.font.bold = True
    run_bold.font.size = Pt(12)
    run_bold.font.name = 'Bookman Old Style'
    run_normal = para.add_run(duration_text)
    run_normal.font.size = Pt(12)
    run_normal.font.name = 'Bookman Old Style'
    
    # Row 7: SMART Objectives
    smart_objectives = generate_smart_objectives(
        session_plan.topic_of_session or 'the topic',
        session_plan.learning_outcomes or '',
        getattr(session_plan, 'session_range', None) or '',
        session_plan.indicative_contents or ''
    )
    cell = merge_cells_in_row(table, 7, 0, 5)
    para = cell.paragraphs[0]
    run_bold = para.add_run("Objectives: By the end of this session every learner should be able to:\n")
    run_bold.font.bold = True
    run_bold.font.size = Pt(12)
    run_bold.font.name = 'Bookman Old Style'
    run_normal = para.add_run(smart_objectives)
    run_normal.font.size = Pt(12)
    run_normal.font.name = 'Bookman Old Style'
    
    # Row 8: Facilitation technique
    technique_text = session_plan.facilitation_techniques or 'Trainer Guided'
    cell = merge_cells_in_row(table, 8, 0, 5)
    para = cell.paragraphs[0]
    run_bold = para.add_run("Facilitation technique(s): ")
    run_bold.font.bold = True
    run_bold.font.size = Pt(12)
    run_bold.font.name = 'Bookman Old Style'
    run_normal = para.add_run(technique_text)
    run_normal.font.size = Pt(12)
    run_normal.font.name = 'Bookman Old Style'
    
    # Row 9: Headers for activities section
    style_header_cell(table.cell(9, 0), "Introduction", bold=True, size=12)
    style_header_cell(table.cell(9, 1), "Introduction", bold=True, size=12)
    style_header_cell(merge_cells_in_row(table, 9, 2, 4), "Resources", bold=True, size=12)
    style_header_cell(table.cell(9, 5), "Duration", bold=True, size=12)
    
    # Row 10: Introduction activities
    topic = session_plan.topic_of_session or 'the session topic'
    activities_text = f'''Trainers activity: 
• Greets and makes roll calls
• Involves the learners to set the ground rules
• Involves learners to review the previous session
• Announces the topic: "{topic}"
• Explains objectives of the session

Learners activity: 
• Greets and replies to the roll call
• Participates and sets the ground rules
• Participates to review the previous session
• Reads and participates in explaining the objectives
• Asks clarifications about the topic and objectives if any'''
    
    cell = merge_cells_in_row(table, 10, 0, 1)
    para = cell.paragraphs[0]
    run = para.add_run(activities_text)
    run.font.size = Pt(12)
    run.font.name = 'Bookman Old Style'
    sector = session_plan.sector or 'General'
    if 'ICT' in sector.upper() or 'SOFTWARE' in (session_plan.trade or '').upper():
        resources_text = '''Attendance sheet
PowerPoint presentation
Projector/Smart board
Computers/Laptops
IDE Software
Whiteboard and markers
Handouts'''
    elif 'HOSPITALITY' in sector.upper() or 'FOOD' in (session_plan.trade or '').upper():
        resources_text = '''Attendance sheet
PowerPoint presentation
Projector
Kitchen equipment
Ingredients/Materials
Whiteboard and markers
Practical worksheets'''
    else:
        resources_text = session_plan.resources or '''Attendance sheet
PowerPoint presentation
Projector
Relevant equipment
Materials/Tools
Whiteboard and markers
Handouts/Worksheets'''
    cell = merge_cells_in_row(table, 10, 2, 4)
    para = cell.paragraphs[0]
    run = para.add_run(resources_text)
    run.font.size = Pt(12)
    run.font.name = 'Bookman Old Style'
    
    cell = table.cell(10, 5)
    para = cell.paragraphs[0]
    run = para.add_run("5 minutes")
    run.font.size = Pt(12)
    run.font.name = 'Bookman Old Style'
    
    # Row 11: Development/Body header
    style_header_cell(merge_cells_in_row(table, 11, 0, 5), "Development/Body", bold=True, size=12)
    
    # Rows 12-14: Development activities (technique-specific)
    topic = session_plan.topic_of_session or 'the topic'
    technique = session_plan.facilitation_techniques or 'Trainer Guided'
    
    # Generate technique-specific development activities
    if technique == 'Brainstorming':
        development_text = f'''Step 1: Idea Generation
Trainers activity: Presents guiding question about {topic}. Encourages free idea sharing. Records all responses.
Learners activity: Suggest ideas without judgment. Contribute individually or in pairs.

Step 2: Clustering Ideas
Trainers activity: Groups similar ideas. Highlights categories.
Learners activity: Help categorize ideas. Identify patterns.

Step 3: Application
Trainers activity: Guides selection of relevant ideas. Assigns groups to expand ideas.
Learners activity: Work in groups to refine ideas into practical tasks.'''
    elif technique == 'Trainer Guided':
        development_text = f'''Step 1: Direct Explanation (I Do)
Trainers activity: Explains {topic} concept, syntax, and examples. Demonstrates on board/projector.
Learners activity: Listen, take notes, ask clarifying questions.

Step 2: Guided Practice (We Do)
Trainers activity: Works through example with learners. Asks for next steps.
Learners activity: Respond to prompts, suggest solutions, correct mistakes together.

Step 3: Independent Practice (You Do)
Trainers activity: Assigns exercise on {topic}. Circulates to support.
Learners activity: Complete task individually. Test and debug.'''
    elif technique == 'Group Discussion':
        development_text = f'''Step 1: Discussion Question
Trainers activity: Presents guiding question about {topic}. Provides sub-questions.
Learners activity: Listen, note question, prepare to contribute.

Step 2: Small Group Discussions
Trainers activity: Divides into groups. Assigns roles. Monitors.
Learners activity: Discuss in groups, share examples, record key points.

Step 3: Whole-Class Sharing
Trainers activity: Invites group presentations. Summarizes themes.
Learners activity: Present findings, listen to others, compare perspectives.'''
    elif technique == 'Simulation':
        development_text = f'''Step 1: Briefing
Trainers activity: Explains simulation scenario for {topic}. Provides rules and roles.
Learners activity: Listen, ask questions, prepare to engage.

Step 2: Running Simulation
Trainers activity: Assigns teams. Provides task sheets. Monitors progress.
Learners activity: Work in teams to solve simulated problem. Collaborate and debug.

Step 3: Debriefing
Trainers activity: Leads debrief discussion. Connects to real-world applications.
Learners activity: Share experiences, reflect on challenges.'''
    elif technique == 'Experiential Learning':
        development_text = f'''Step 1: Concrete Experience
Trainers activity: Provides hands-on coding challenge on {topic}.
Learners activity: Work individually/pairs to complete activity.

Step 2: Reflective Observation
Trainers activity: Asks learners to reflect on what was easy/difficult.
Learners activity: Share reflections in groups.

Step 3: Abstract Conceptualization
Trainers activity: Explains theory using learners' experiences as examples.
Learners activity: Take notes, connect experience to theory.

Step 4: Active Application
Trainers activity: Assigns new problem applying {topic}.
Learners activity: Apply understanding to solve new problem.'''
    elif technique == 'Jigsaw':
        development_text = f'''Step 1: Expert Groups
Trainers activity: Divides {topic} into sub-topics. Assigns expert groups.
Learners activity: Study assigned sub-topic in expert groups.

Step 2: Home Groups
Trainers activity: Reorganizes into home groups with one expert per sub-topic.
Learners activity: Teach sub-topic to home group members.

Step 3: Synthesis
Trainers activity: Facilitates whole-class discussion. Clarifies misconceptions.
Learners activity: Share insights, ask questions, complete understanding.'''
    else:
        development_text = f'''Trainers activity: 
• Explains and demonstrates {topic}
• Provides practical examples
• Uses {technique} approach
• Gives practice activities
• Monitors and guides learners
• Provides feedback

Learners activity:
• Observes demonstrations
• Takes notes and asks questions
• Participates actively
• Practices skills
• Applies learned concepts
• Seeks guidance when needed'''
    
    if 'ICT' in sector.upper():
        dev_resources = '''Computers/Laptops
Projector/Smart board
PowerPoint presentation
IDE/Software tools
Internet connection
Whiteboard and markers'''
    elif 'HOSPITALITY' in sector.upper():
        dev_resources = '''Kitchen equipment
Ingredients/Materials
Projector
PowerPoint presentation
Practical tools
Whiteboard and markers'''
    else:
        dev_resources = '''Relevant equipment
Projector
PowerPoint presentation
Practical materials
Tools and instruments
Whiteboard and markers'''
    
    # Use all 3 rows for development text
    cell = merge_cells_in_row(table, 12, 0, 1)
    para = cell.paragraphs[0]
    run = para.add_run(development_text)
    run.font.size = Pt(12)
    run.font.name = 'Bookman Old Style'
    
    cell = merge_cells_in_row(table, 12, 2, 4)
    para = cell.paragraphs[0]
    run = para.add_run(dev_resources)
    run.font.size = Pt(12)
    run.font.name = 'Bookman Old Style'
    
    cell = table.cell(12, 5)
    para = cell.paragraphs[0]
    run = para.add_run("25\nminutes")
    run.font.size = Pt(12)
    run.font.name = 'Bookman Old Style'
    
    # Merge rows 13-14 with row 12 for more space
    for row in [13, 14]:
        merge_cells_in_row(table, row, 0, 1)
        merge_cells_in_row(table, row, 2, 4)
        table.cell(row, 5)
    
    # Row 15: Conclusion header
    style_header_cell(merge_cells_in_row(table, 15, 0, 5), "Conclusion", bold=True, size=12)
    
    # Row 16: Summary
    summary_text = '''Summary:
The trainer involves the learners to summarize the session by asking questions reflecting on the learning objectives.
The learners summarize the session as by responding to asked questions.'''
    cell = merge_cells_in_row(table, 16, 0, 1)
    para = cell.paragraphs[0]
    run = para.add_run(summary_text)
    run.font.size = Pt(12)
    run.font.name = 'Bookman Old Style'
    
    cell = merge_cells_in_row(table, 16, 2, 4)
    para = cell.paragraphs[0]
    run = para.add_run("Computer \nprojector")
    run.font.size = Pt(12)
    run.font.name = 'Bookman Old Style'
    
    cell = table.cell(16, 5)
    para = cell.paragraphs[0]
    run = para.add_run("3 minutes")
    run.font.size = Pt(12)
    run.font.name = 'Bookman Old Style'
    
    # Row 17: Assessment/Assignment
    assessment_text = f'''Assessment/Assignment
Trainers activity: 
• Provides practical assessment tasks related to {topic}
• Gives oral questions to test understanding
• Observes learner performance during activities
• Provides immediate feedback

Learners activity:
• Completes assessment tasks
• Answers questions confidently
• Demonstrates learned skills
• Receives and acts on feedback'''
    cell = merge_cells_in_row(table, 17, 0, 1)
    para = cell.paragraphs[0]
    run = para.add_run(assessment_text)
    run.font.size = Pt(12)
    run.font.name = 'Bookman Old Style'
    
    cell = merge_cells_in_row(table, 17, 2, 4)
    para = cell.paragraphs[0]
    run = para.add_run("Assessment sheets")
    run.font.size = Pt(12)
    run.font.name = 'Bookman Old Style'
    
    cell = table.cell(17, 5)
    para = cell.paragraphs[0]
    run = para.add_run("5 minutes")
    run.font.size = Pt(12)
    run.font.name = 'Bookman Old Style'
    
    # Row 18: Evaluation of the session
    evaluation_text = f'''Evaluation of the session:
Trainers activity: 
• Involves learners in session evaluation
• Asks: "How was today's session on {topic}?"
• Asks: "What should we improve next time?"
• Links current session to the next topic
• Previews upcoming learning content

Learners activity:
• Provides honest feedback about the session
• Suggests improvements for future sessions
• Shows understanding of session content
• Expresses readiness for next session'''
    cell = merge_cells_in_row(table, 18, 0, 1)
    para = cell.paragraphs[0]
    run = para.add_run(evaluation_text)
    run.font.size = Pt(12)
    run.font.name = 'Bookman Old Style'
    
    cell = merge_cells_in_row(table, 18, 2, 4)
    para = cell.paragraphs[0]
    run = para.add_run("Self-assessment form")
    run.font.size = Pt(12)
    run.font.name = 'Bookman Old Style'
    
    cell = table.cell(18, 5)
    para = cell.paragraphs[0]
    run = para.add_run("2minutes")
    run.font.size = Pt(12)
    run.font.name = 'Bookman Old Style'
    
    # Row 19: References
    cell = merge_cells_in_row(table, 19, 0, 5)
    para = cell.paragraphs[0]
    run_bold = para.add_run("References: ")
    run_bold.font.bold = True
    run_bold.font.size = Pt(12)
    run_bold.font.name = 'Bookman Old Style'
    run_normal = para.add_run(session_plan.references or '')
    run_normal.font.size = Pt(12)
    run_normal.font.name = 'Bookman Old Style'
    
    # Row 20: Appendices
    appendices_text = f"PowerPoint presentation on {topic}, Practical worksheets, Assessment rubrics, Answer keys, Resource materials"
    cell = merge_cells_in_row(table, 20, 0, 5)
    para = cell.paragraphs[0]
    run_bold = para.add_run("Appendices: ")
    run_bold.font.bold = True
    run_bold.font.size = Pt(12)
    run_bold.font.name = 'Bookman Old Style'
    run_normal = para.add_run(appendices_text)
    run_normal.font.size = Pt(12)
    run_normal.font.name = 'Bookman Old Style'
    
    # Row 21: Reflection
    reflection_text = session_plan.reflection or f"Session on {topic} was well-received. Learners showed good engagement with {technique.lower()} approach. Areas for improvement: [To be filled after session delivery]"
    cell = merge_cells_in_row(table, 21, 0, 5)
    para = cell.paragraphs[0]
    run_bold = para.add_run("Reflection : ")
    run_bold.font.bold = True
    run_bold.font.size = Pt(12)
    run_bold.font.name = 'Bookman Old Style'
    run_normal = para.add_run(reflection_text)
    run_normal.font.size = Pt(12)
    run_normal.font.name = 'Bookman Old Style'
    
    # Save to temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
    doc.save(temp_file.name)
    return temp_file.name

def generate_scheme_of_work_docx(scheme):
    doc = Document()
    
    # Set landscape orientation
    section = doc.sections[0]
    section.orientation = 1
    section.page_width = Inches(11.69)
    section.page_height = Inches(8.27)
    section.left_margin = Inches(0.5)
    section.right_margin = Inches(0.5)
    section.top_margin = Inches(0.5)
    section.bottom_margin = Inches(0.5)
    
    # School header
    header = doc.add_paragraph()
    header.alignment = WD_ALIGN_PARAGRAPH.CENTER
    header.paragraph_format.space_before = Pt(0)
    header.paragraph_format.space_after = Pt(6)
    run = header.add_run(f"{getattr(scheme, 'province', None) or 'PROVINCE'}\n")
    run.font.size = Pt(11)
    run.font.bold = True
    run = header.add_run(f"{getattr(scheme, 'district', None) or 'DISTRICT'}\n")
    run.font.size = Pt(11)
    run = header.add_run(f"{getattr(scheme, 'sector', None) or 'SECTOR'}\n")
    run.font.size = Pt(11)
    run = header.add_run(f"{getattr(scheme, 'school', None) or 'SCHOOL'}")
    run.font.size = Pt(12)
    run.font.bold = True
    
    # Title
    title = doc.add_paragraph()
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    title.paragraph_format.space_before = Pt(6)
    title.paragraph_format.space_after = Pt(6)
    title_run = title.add_run('SCHEME OF WORK')
    title_run.font.size = Pt(16)
    title_run.font.bold = True
    
    # Module Details Table - 6 rows x 4 cols
    details_table = doc.add_table(rows=6, cols=4)
    details_table.style = 'Table Grid'
    
    # Row 0: Sector (label + value) | Trainer (label + value)
    cell = details_table.cell(0, 0)
    para = cell.paragraphs[0]
    run = para.add_run('Sector:')
    run.font.bold = True
    run.font.size = Pt(11)
    run.font.name = 'Bookman Old Style'
    
    cell = details_table.cell(0, 1)
    para = cell.paragraphs[0]
    run = para.add_run(getattr(scheme, 'sector', None) or '')
    run.font.size = Pt(11)
    run.font.name = 'Bookman Old Style'
    
    cell = details_table.cell(0, 2)
    para = cell.paragraphs[0]
    run = para.add_run('Trainer:')
    run.font.bold = True
    run.font.size = Pt(11)
    run.font.name = 'Bookman Old Style'
    
    cell = details_table.cell(0, 3)
    para = cell.paragraphs[0]
    run = para.add_run(scheme.trainer_name or '')
    run.font.size = Pt(11)
    run.font.name = 'Bookman Old Style'
    
    # Row 1: Trade | School Year
    cell = details_table.cell(1, 0)
    para = cell.paragraphs[0]
    run = para.add_run('Trade:')
    run.font.bold = True
    run.font.size = Pt(11)
    run.font.name = 'Bookman Old Style'
    
    cell = details_table.cell(1, 1)
    para = cell.paragraphs[0]
    run = para.add_run(getattr(scheme, 'trade', None) or getattr(scheme, 'department_trade', None) or '')
    run.font.size = Pt(11)
    run.font.name = 'Bookman Old Style'
    
    cell = details_table.cell(1, 2)
    para = cell.paragraphs[0]
    run = para.add_run('School Year:')
    run.font.bold = True
    run.font.size = Pt(11)
    run.font.name = 'Bookman Old Style'
    
    cell = details_table.cell(1, 3)
    para = cell.paragraphs[0]
    run = para.add_run(getattr(scheme, 'school_year', None) or '')
    run.font.size = Pt(11)
    run.font.name = 'Bookman Old Style'
    
    # Row 2: Qualification Title | Term
    cell = details_table.cell(2, 0)
    para = cell.paragraphs[0]
    run = para.add_run('Qualification Title:')
    run.font.bold = True
    run.font.size = Pt(11)
    run.font.name = 'Bookman Old Style'
    
    cell = details_table.cell(2, 1)
    para = cell.paragraphs[0]
    run = para.add_run(scheme.qualification_title or '')
    run.font.size = Pt(11)
    run.font.name = 'Bookman Old Style'
    
    cell = details_table.cell(2, 2)
    para = cell.paragraphs[0]
    run = para.add_run('Term:')
    run.font.bold = True
    run.font.size = Pt(11)
    run.font.name = 'Bookman Old Style'
    
    cell = details_table.cell(2, 3)
    para = cell.paragraphs[0]
    run = para.add_run(getattr(scheme, 'terms', None) or getattr(scheme, 'term', None) or 'ALL TERM')
    run.font.size = Pt(11)
    run.font.name = 'Bookman Old Style'
    
    # Row 3: RQF Level | Module details (rowspan 3)
    cell = details_table.cell(3, 0)
    para = cell.paragraphs[0]
    run = para.add_run('RQF Level:')
    run.font.bold = True
    run.font.size = Pt(11)
    run.font.name = 'Bookman Old Style'
    
    cell = details_table.cell(3, 1)
    para = cell.paragraphs[0]
    run = para.add_run(getattr(scheme, 'rqf_level', None) or '')
    run.font.size = Pt(11)
    run.font.name = 'Bookman Old Style'
    
    # Merge cells for Module details (row 3-5, col 2-3)
    cell = details_table.cell(3, 2)
    cell.merge(details_table.cell(5, 2))
    para = cell.paragraphs[0]
    run = para.add_run('Module details')
    run.font.bold = True
    run.font.size = Pt(11)
    run.font.name = 'Bookman Old Style'
    
    # Row 3 col 3: Module code and title
    cell = details_table.cell(3, 3)
    para = cell.paragraphs[0]
    run_bold = para.add_run('Module code and title\n')
    run_bold.font.bold = True
    run_bold.font.size = Pt(11)
    run_bold.font.name = 'Bookman Old Style'
    run_normal = para.add_run(getattr(scheme, 'module_code_title', None) or '')
    run_normal.font.size = Pt(11)
    run_normal.font.name = 'Bookman Old Style'
    
    # Row 4: Empty | Empty | (merged) | Learning hours
    cell = details_table.cell(4, 3)
    para = cell.paragraphs[0]
    run_bold = para.add_run('Learning hours:\n')
    run_bold.font.bold = True
    run_bold.font.size = Pt(11)
    run_bold.font.name = 'Bookman Old Style'
    module_hours = getattr(scheme, 'module_hours', None) or getattr(scheme, 'module_learning_hours', None) or ''
    run_normal = para.add_run(str(module_hours))
    run_normal.font.size = Pt(11)
    run_normal.font.name = 'Bookman Old Style'
    
    # Row 5: Date | Class Name | (merged) | Number of Classes
    cell = details_table.cell(5, 0)
    para = cell.paragraphs[0]
    run = para.add_run('Date:')
    run.font.bold = True
    run.font.size = Pt(11)
    run.font.name = 'Bookman Old Style'
    
    cell = details_table.cell(5, 1)
    para = cell.paragraphs[0]
    run = para.add_run(getattr(scheme, 'school_year', None) or '')
    run.font.size = Pt(11)
    run.font.name = 'Bookman Old Style'
    
    cell = details_table.cell(5, 3)
    para = cell.paragraphs[0]
    run_bold = para.add_run('Number of Classes:\n')
    run_bold.font.bold = True
    run_bold.font.size = Pt(11)
    run_bold.font.name = 'Bookman Old Style'
    num_classes = getattr(scheme, 'number_of_classes', None) or ''
    run_normal = para.add_run(str(num_classes) + '\n')
    run_normal.font.size = Pt(11)
    run_normal.font.name = 'Bookman Old Style'
    run_bold2 = para.add_run('Class Name:\n')
    run_bold2.font.bold = True
    run_bold2.font.size = Pt(11)
    run_bold2.font.name = 'Bookman Old Style'
    class_name = getattr(scheme, 'class_name', None) or ''
    run_normal2 = para.add_run(str(class_name))
    run_normal2.font.size = Pt(11)
    run_normal2.font.name = 'Bookman Old Style'
    
    # Default values for last 4 columns (standard RTB format)
    DEFAULT_ACTIVITIES = '''● Demonstration and simulation
● Individual and group work
● Practical exercise
● Individualized
● Trainer guided
● Group discussion'''
    
    DEFAULT_RESOURCES = '''Computers
Projector
Projection screen
Printers
Internet connection
Whiteboard and markers'''
    
    DEFAULT_ASSESSMENT = '''Written test
Practical assessment
Oral questions
Observation
Project work'''
    
    DEFAULT_PLACE = '''Class
Computer lab
Workshop'''
    
    # Generate for each term
    for term_num in [1, 2, 3]:
        # Term heading
        term_para = doc.add_paragraph()
        term_para.paragraph_format.space_before = Pt(6)
        term_para.paragraph_format.space_after = Pt(6)
        term_run = term_para.add_run(f'Term: {term_num}')
        term_run.font.size = Pt(14)
        term_run.font.bold = True
        
        # Get term data (only first 3 columns from user)
        weeks = getattr(scheme, f'term{term_num}_weeks', None) or f'Week 1-12'
        los = getattr(scheme, f'term{term_num}_learning_outcomes', None) or ''
        ics = getattr(scheme, f'term{term_num}_indicative_contents', None) or ''
        duration = getattr(scheme, f'term{term_num}_duration', None) or '10 hours'
        
        # Create table with 9 columns (matching official RTB format)
        table = doc.add_table(rows=2, cols=9)
        table.style = 'Table Grid'
        
        def set_cell_bg_color(cell, color):
            shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color}"/>')
            cell._element.get_or_add_tcPr().append(shading)
        
        # Row 0: Main headers with colspan and gray background
        # Weeks (col 0, rowspan 2)
        cell = table.cell(0, 0)
        cell.merge(table.cell(1, 0))
        cell.text = 'Weeks'
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_bg_color(cell, 'D9D9D9')
        for para in cell.paragraphs:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in para.runs:
                run.font.bold = True
                run.font.size = Pt(12)
                run.font.name = 'Bookman Old Style'
                run.font.color.rgb = RGBColor(0, 0, 0)
        
        # Competence code and name (cols 1-3 merged)
        cell = table.cell(0, 1)
        cell.merge(table.cell(0, 3))
        cell.text = 'Competence code and name'
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_bg_color(cell, 'D9D9D9')
        for para in cell.paragraphs:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in para.runs:
                run.font.bold = True
                run.font.size = Pt(12)
                run.font.name = 'Bookman Old Style'
                run.font.color.rgb = RGBColor(0, 0, 0)
        
        # Learning Activities (col 4, rowspan 2)
        cell = table.cell(0, 4)
        cell.merge(table.cell(1, 4))
        cell.text = 'Learning Activities'
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_bg_color(cell, 'D9D9D9')
        for para in cell.paragraphs:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in para.runs:
                run.font.bold = True
                run.font.size = Pt(12)
                run.font.name = 'Bookman Old Style'
                run.font.color.rgb = RGBColor(0, 0, 0)
        
        # Resources (col 5, rowspan 2)
        cell = table.cell(0, 5)
        cell.merge(table.cell(1, 5))
        cell.text = 'Resources (Equipment, tools, and materials)'
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_bg_color(cell, 'D9D9D9')
        for para in cell.paragraphs:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in para.runs:
                run.font.bold = True
                run.font.size = Pt(12)
                run.font.name = 'Bookman Old Style'
                run.font.color.rgb = RGBColor(0, 0, 0)
        
        # Evidences (col 6, rowspan 2)
        cell = table.cell(0, 6)
        cell.merge(table.cell(1, 6))
        cell.text = 'Evidences of formative assessment'
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_bg_color(cell, 'D9D9D9')
        for para in cell.paragraphs:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in para.runs:
                run.font.bold = True
                run.font.size = Pt(12)
                run.font.name = 'Bookman Old Style'
                run.font.color.rgb = RGBColor(0, 0, 0)
        
        # Learning Place (col 7, rowspan 2)
        cell = table.cell(0, 7)
        cell.merge(table.cell(1, 7))
        cell.text = 'Learning Place'
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_bg_color(cell, 'D9D9D9')
        for para in cell.paragraphs:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in para.runs:
                run.font.bold = True
                run.font.size = Pt(12)
                run.font.name = 'Bookman Old Style'
                run.font.color.rgb = RGBColor(0, 0, 0)
        
        # Observation (col 8, rowspan 2)
        cell = table.cell(0, 8)
        cell.merge(table.cell(1, 8))
        cell.text = 'Observation'
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_bg_color(cell, 'D9D9D9')
        for para in cell.paragraphs:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in para.runs:
                run.font.bold = True
                run.font.size = Pt(12)
                run.font.name = 'Bookman Old Style'
                run.font.color.rgb = RGBColor(0, 0, 0)
        
        # Row 1: Sub-headers with gray background
        cell = table.cell(1, 1)
        cell.text = 'Learning outcome (LO)'
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_bg_color(cell, 'D9D9D9')
        for para in cell.paragraphs:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in para.runs:
                run.font.bold = True
                run.font.size = Pt(12)
                run.font.name = 'Bookman Old Style'
                run.font.color.rgb = RGBColor(0, 0, 0)
        
        cell = table.cell(1, 2)
        cell.text = 'Duration'
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_bg_color(cell, 'D9D9D9')
        for para in cell.paragraphs:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in para.runs:
                run.font.bold = True
                run.font.size = Pt(12)
                run.font.name = 'Bookman Old Style'
                run.font.color.rgb = RGBColor(0, 0, 0)
        
        cell = table.cell(1, 3)
        cell.text = 'Indicative content (IC)'
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_bg_color(cell, 'D9D9D9')
        for para in cell.paragraphs:
            para.alignment = WD_ALIGN_PARAGRAPH.CENTER
            for run in para.runs:
                run.font.bold = True
                run.font.size = Pt(12)
                run.font.name = 'Bookman Old Style'
                run.font.color.rgb = RGBColor(0, 0, 0)
        
        # Parse LOs and ICs
        lo_list = [l.strip() for l in los.split('\n') if l.strip()]
        ic_list = [c.strip() for c in ics.split('\n') if c.strip()]
        
        # Add data rows
        num_rows = max(len(lo_list), len(ic_list), 1)
        for i in range(num_rows):
            row = table.add_row()
            
            # Weeks (only in first row) - Bold, Bookman Old Style 12
            if i == 0:
                cell = row.cells[0]
                para = cell.paragraphs[0]
                run = para.add_run(weeks)
                run.font.bold = True
                run.font.size = Pt(12)
                run.font.name = 'Bookman Old Style'
            
            # LO - "LO1:" bold, rest normal
            lo_text = lo_list[i] if i < len(lo_list) else ''
            cell = row.cells[1]
            para = cell.paragraphs[0]
            run_bold = para.add_run(f"LO{i+1}:")
            run_bold.font.bold = True
            run_bold.font.size = Pt(12)
            run_bold.font.name = 'Bookman Old Style'
            run_normal = para.add_run(f"   {lo_text}")
            run_normal.font.bold = False
            run_normal.font.size = Pt(12)
            run_normal.font.name = 'Bookman Old Style'
            
            # Duration - Normal
            cell = row.cells[2]
            para = cell.paragraphs[0]
            run = para.add_run(duration)
            run.font.size = Pt(12)
            run.font.name = 'Bookman Old Style'
            
            # IC - "IC1.1:" bold, rest normal
            ic_text = ic_list[i] if i < len(ic_list) else ''
            cell = row.cells[3]
            para = cell.paragraphs[0]
            run_bold = para.add_run(f"IC{i+1}:")
            run_bold.font.bold = True
            run_bold.font.size = Pt(12)
            run_bold.font.name = 'Bookman Old Style'
            run_normal = para.add_run(f"  {ic_text}")
            run_normal.font.bold = False
            run_normal.font.size = Pt(12)
            run_normal.font.name = 'Bookman Old Style'
            
            # Default values for last 4 columns - Bookman Old Style 12
            for idx, text in [(4, DEFAULT_ACTIVITIES), (5, DEFAULT_RESOURCES), 
                              (6, DEFAULT_ASSESSMENT), (7, DEFAULT_PLACE), (8, '')]:
                cell = row.cells[idx]
                para = cell.paragraphs[0]
                run = para.add_run(text)
                run.font.size = Pt(12)
                run.font.name = 'Bookman Old Style'
        
        # Integrated Assessment row
        assess_row = table.add_row()
        for idx, text in [(0, 'Integrated Assessment (for specific module)'), 
                          (1, 'Task'), (2, 'Consumables'), (7, 'workshop')]:
            cell = assess_row.cells[idx]
            para = cell.paragraphs[0]
            run = para.add_run(text)
            run.font.size = Pt(12)
            run.font.name = 'Bookman Old Style'
        
        # Trainer signature
        sig = doc.add_paragraph(f"Trainer's name and signature: {scheme.trainer_name or ''}")
        sig.alignment = WD_ALIGN_PARAGRAPH.LEFT
        sig.paragraph_format.space_before = Pt(6)
        sig.paragraph_format.space_after = Pt(6)
        
        if term_num < 3:
            doc.add_page_break()
    
    # Final sign-offs
    doc.add_page_break()
    doc.add_paragraph(f"Prepared by: (Name, position and Signature) TRAINER: {scheme.trainer_name or ''}")
    doc.add_paragraph(f"Verified by: (Name, position and Signature) DOS: {getattr(scheme, 'dos_name', None) or ''}")
    doc.add_paragraph(f"Approved by: (Name, position and Signature) SCHOOL MANAGER: {getattr(scheme, 'manager_name', None) or ''}")
    
    # Save
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
    doc.save(temp_file.name)
    return temp_file.name