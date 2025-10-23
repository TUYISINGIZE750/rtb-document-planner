from rtb_professional_generator import generate_rtb_session_plan, generate_rtb_scheme_of_work

# Test Session Plan
print("Testing Session Plan Generator...")
session_data = {
    'sector': 'SGGS',
    'sub_sector': 'HH',
    'date': '2025-01-15',
    'trainer_name': 'SJJS',
    'term': 'I',
    'module_code': 'TEST301 Test Module',
    'week': 'I',
    'num_trainees': '55',
    'classes': '1',
    'learning_outcome': '1. Test learning outcome',
    'indicative_content': '1.1 Test content',
    'topic_of_session': 'Push the latest code to github pages',
    'range': 'Key concepts\nTest methods',
    'duration': '55',
    'objectives': 'Define key concepts\nApply test methods',
    'facilitation_technique': 'JIGSAW',
    'intro_trainer_activity': 'Greets and makes roll calls',
    'intro_resources': 'Attendance sheet\nPPT\nProjector',
    'intro_duration': '5 minutes',
    'step1': {
        'title': 'Introduction to concepts',
        'activity': 'Explains key concepts',
        'resources': 'Computer\nProjector\nPPT',
        'duration': '20 minutes'
    },
    'step2': {
        'title': 'Practical application',
        'activity': 'Demonstrates practical examples',
        'resources': 'Computer\nProjector\nPPT',
        'duration': '20 minutes'
    },
    'step3': {
        'title': 'Group work',
        'activity': 'Assigns group tasks',
        'resources': 'Computer\nProjector\nPPT',
        'duration': '10 minutes'
    },
    'summary': 'Trainer involves learners to summarize',
    'summary_resources': 'Computer\nProjector',
    'summary_duration': '3 minutes',
    'assessment_activity': 'Gives assessment questions',
    'assessment_resources': 'Assessment sheets',
    'assessment_duration': '5 minutes',
    'evaluation_activity': 'Involves learners in evaluation',
    'evaluation_resources': 'Self-assessment form',
    'evaluation_duration': '2 minutes',
    'references': 'RTB Curriculum Guide 2024',
    'appendices': 'PPT, Task Sheets, Assessment',
    'reflection': ''
}

try:
    doc = generate_rtb_session_plan(session_data)
    doc.save('test_session_plan.docx')
    print("[OK] Session Plan generated successfully: test_session_plan.docx")
except Exception as e:
    print(f"[ERROR] Error generating session plan: {e}")

# Test Scheme of Work
print("\nTesting Scheme of Work Generator...")
scheme_data = {
    'school': 'Test TVET School',
    'module_code_title': 'TEST301: Test Module',
    'trainer_name': 'SJJS',
    'school_year': '2024-2025',
    'term': 'I',
    'weeks': [
        {
            'week_range': '1-2',
            'learning_outcome': 'LO1: Test outcome',
            'duration': '10 hours',
            'indicative_content': 'IC1.1: Test content',
            'learning_activities': 'Lectures, Practicals',
            'resources': 'Computer, Projector',
            'assessment_evidence': 'Written test',
            'learning_place': 'Lab',
            'observation': 'N/A'
        }
    ]
}

try:
    doc = generate_rtb_scheme_of_work(scheme_data)
    doc.save('test_scheme_of_work.docx')
    print("[OK] Scheme of Work generated successfully: test_scheme_of_work.docx")
except Exception as e:
    print(f"[ERROR] Error generating scheme: {e}")

print("\n[OK] All tests completed!")
