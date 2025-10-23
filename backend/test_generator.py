from rtb_professional_generator import generate_rtb_session_plan, generate_rtb_scheme_of_work

# Test Session Plan with WIZARD FIELD NAMES
print("Testing Session Plan Generator...")
session_data = {
    'sector': 'ICT & MULTIMEDIA',
    'trade': 'Software Development',
    'rqf_level': 'Level 3',
    'trainer_name': 'TUYISINGIZE Leonard',
    'module_code_title': 'SWDPR301: Analyze project requirements',
    'term': 'Term 1',
    'week': 'Week 1',
    'date': '2025-01-15',
    'number_of_trainees': '55',
    'class_name': 'L3SD-A',
    'duration': '80',
    'topic_of_session': 'Identification of requirements gathering methodologies',
    'learning_outcomes': '1. Identify customer needs\n2. Apply data gathering techniques',
    'indicative_contents': '1.1 Data gathering\n1.2 Communication process\n1.3 Customer pain points',
    'facilitation_techniques': 'Jigsaw'
}

try:
    doc = generate_rtb_session_plan(session_data)
    doc.save('test_session_plan.docx')
    print("[OK] Session Plan generated successfully: test_session_plan.docx")
except Exception as e:
    print(f"[ERROR] Error generating session plan: {e}")

# Test Scheme of Work with WIZARD FIELD NAMES
print("\nTesting Scheme of Work Generator...")
scheme_data = {
    'province': 'Kigali City',
    'district': 'Gasabo',
    'sector': 'ICT & MULTIMEDIA',
    'school': 'IPRC Kigali',
    'trade': 'Software Development',
    'qualification_title': 'Diploma in Software Development',
    'rqf_level': 'Level 4',
    'module_code_title': 'CSAPA301: C Programming',
    'school_year': '2024-2025',
    'terms': 'Term 1, 2, 3',
    'module_hours': '120',
    'number_of_classes': '3',
    'class_name': 'L4CSA-A',
    'cohort_size': '30',
    'trainer_name': 'TUYISINGIZE Leonard',
    'trainer_position': 'Senior Instructor',
    'module_rationale': 'This module introduces C programming fundamentals',
    'entry_requirements': 'Basic computer literacy',
    'competency_codes': 'CSAPA301',
    'indicative_scope': 'C syntax, data types, control structures',
    'standards_alignment': 'REB TVET standards',
    'cross_cutting_issues': 'Safety, ethics',
    'key_skills': 'Problem-solving, logical thinking',
    'delivery_approach': 'Blended learning',
    'term1_weeks': 'Week 1-12 (Jan-Mar 2025)',
    'term1_learning_outcomes': 'LO1: Understand C basics\nLO2: Write simple programs',
    'term1_duration': '40 hours',
    'term1_indicative_contents': 'IC1.1: Variables and data types\nIC1.2: Control structures',
    'term2_weeks': 'Week 13-24 (Apr-Jun 2025)',
    'term2_learning_outcomes': 'LO3: Work with arrays\nLO4: Use functions',
    'term2_duration': '40 hours',
    'term2_indicative_contents': 'IC2.1: Arrays and strings\nIC2.2: Functions and scope',
    'term3_weeks': 'Week 25-36 (Jul-Sep 2025)',
    'term3_learning_outcomes': 'LO5: Manage pointers\nLO6: Handle files',
    'term3_duration': '40 hours',
    'term3_indicative_contents': 'IC3.1: Pointers and memory\nIC3.2: File operations',
    'formative_assessment': 'Weekly quizzes, practical exercises',
    'summative_assessment': 'Final exam, project',
    'resource_inventory': 'Computers, C compiler, textbooks',
    'health_safety': 'Proper ergonomics, electrical safety',
    'dos_name': 'Jane Smith',
    'manager_name': 'Robert Johnson'
}

try:
    doc = generate_rtb_scheme_of_work(scheme_data)
    doc.save('test_scheme_of_work.docx')
    print("[OK] Scheme of Work generated successfully: test_scheme_of_work.docx")
except Exception as e:
    print(f"[ERROR] Error generating scheme: {e}")

print("\n[OK] All tests completed!")
