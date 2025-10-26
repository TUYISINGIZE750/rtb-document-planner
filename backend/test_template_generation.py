import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from rtb_template_generator import generate_session_plan_from_template, generate_scheme_of_work_from_template

test_data = {
    'code': 'Introduction to PLC',
    'sector': 'ICT and Multimedia',
    'trade': 'Computer system and architecture',
    'rqf_level': 'Level 3',
    'term': 'Term 2',
    'week': 'Week 11',
    'date': '2025-10-26',
    'trainer_name': 'John Doe',
    'module_code_title': 'Introduction to PLC',
    'class_name': 'L4 CSA',
    'number_of_trainees': '35',
    'topic_of_session': 'Use of Do while loops in C program',
    'duration': '40',
    'learning_outcomes': 'Use of Do while loops in C program',
    'indicative_contents': 'Use of Do while loops in C program',
    'facilitation_techniques': 'Simulation',
    'resources': '• Whiteboard/Smartboard for demonstrations\n• Handouts with key concepts and examples\n• Projector and laptop for presentations\n• Textbook/Reference materials\n• Simulation scenario materials\n• 35 role cards\n• Props and equipment for realism',
}

print("Testing Session Plan Generation...")
try:
    session_file = generate_session_plan_from_template(test_data)
    print(f"✓ Session plan generated: {session_file}")
    print(f"  File exists: {os.path.exists(session_file)}")
    print(f"  File size: {os.path.getsize(session_file)} bytes")
except Exception as e:
    print(f"✗ Error generating session plan: {e}")
    import traceback
    traceback.print_exc()

scheme_data = {
    'sector': 'ICT and Multimedia',
    'trade': 'Computer system and architecture',
    'trainer_name': 'John Doe',
    'module_code_title': 'Introduction to PLC',
    'term1_weeks': 'Week 1-4',
    'term1_learning_outcomes': 'Understand PLC basics',
    'term1_indicative_contents': 'PLC fundamentals',
    'term1_duration': '40 hours',
    'term2_weeks': 'Week 5-8',
    'term2_learning_outcomes': 'Advanced PLC programming',
    'term2_indicative_contents': 'Ladder logic programming',
    'term2_duration': '40 hours',
    'term3_weeks': 'Week 9-12',
    'term3_learning_outcomes': 'PLC applications',
    'term3_indicative_contents': 'Industrial applications',
    'term3_duration': '40 hours',
}

print("\nTesting Scheme of Work Generation...")
try:
    scheme_file = generate_scheme_of_work_from_template(scheme_data)
    print(f"✓ Scheme generated: {scheme_file}")
    print(f"  File exists: {os.path.exists(scheme_file)}")
    print(f"  File size: {os.path.getsize(scheme_file)} bytes")
except Exception as e:
    print(f"✗ Error generating scheme: {e}")
    import traceback
    traceback.print_exc()

print("\nDone!")
