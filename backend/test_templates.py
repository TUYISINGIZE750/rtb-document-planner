"""Test script to verify RTB templates work correctly"""
from rtb_template_filler import fill_session_plan_template, fill_scheme_template
import os

# Test data for session plan
session_data = {
    'sector': 'ICT & MULTIMEDIA',
    'trade': 'Software Development',
    'date': '20th January 2025',
    'trainer_name': 'Test Teacher',
    'term': 'Term 1',
    'module_code_title': 'TEST301 Test Module',
    'week': 'Week 1',
    'number_of_trainees': '30',
    'class_name': 'L4CSA-A',
    'learning_outcomes': 'Students will be able to test the system',
    'indicative_contents': '1. Testing basics\n2. Test procedures',
    'topic_of_session': 'Introduction to Testing',
    'duration': '80',
    'facilitation_techniques': 'Demonstration, Group work'
}

# Test data for scheme
scheme_data = {
    'term1_weeks': 'Week 1-12 (Jan-Mar 2025)',
    'term1_learning_outcomes': 'LO1: Test learning outcome',
    'term1_duration': '40 hours',
    'term1_indicative_contents': 'IC1.1: Test content',
    'term2_weeks': 'Week 13-24 (Apr-Jun 2025)',
    'term2_learning_outcomes': 'LO2: Second learning outcome',
    'term2_duration': '40 hours',
    'term2_indicative_contents': 'IC2.1: Second content',
    'term3_weeks': 'Week 25-36 (Jul-Sep 2025)',
    'term3_learning_outcomes': 'LO3: Third learning outcome',
    'term3_duration': '40 hours',
    'term3_indicative_contents': 'IC3.1: Third content'
}

print("Testing RTB Template System...")
print("="*60)

# Test session plan
try:
    print("\n1. Testing Session Plan Template...")
    session_file = fill_session_plan_template(session_data)
    if os.path.exists(session_file):
        print(f"   [OK] Session plan created: {session_file}")
        print(f"   File size: {os.path.getsize(session_file)} bytes")
    else:
        print("   [ERROR] Session plan file not created")
except Exception as e:
    print(f"   [ERROR] Error: {e}")

# Test scheme
try:
    print("\n2. Testing Scheme of Work Template...")
    scheme_file = fill_scheme_template(scheme_data)
    if os.path.exists(scheme_file):
        print(f"   [OK] Scheme created: {scheme_file}")
        print(f"   File size: {os.path.getsize(scheme_file)} bytes")
    else:
        print("   [ERROR] Scheme file not created")
except Exception as e:
    print(f"   [ERROR] Error: {e}")

print("\n" + "="*60)
print("Test complete! Check the generated files.")
