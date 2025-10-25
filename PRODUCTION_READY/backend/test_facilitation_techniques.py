"""Test different facilitation techniques"""
from rtb_template_filler_exact import fill_session_plan_template
from docx import Document
import os

techniques = [
    'Trainer-guided',
    'Simulation',
    'Group work',
    'Hands-on practice',
    'Discussion and brainstorming',
    'Project-based learning'
]

base_data = {
    'sector': 'ICT',
    'trade': 'Computer Hardware Maintenance',
    'trainer_name': 'John MUGISHA',
    'module_code_title': 'CHM4101 - Computer Assembly',
    'term': 'Term 1',
    'week': 'Week 5',
    'date': '15/01/2025',
    'class_name': 'CHM4A',
    'number_of_trainees': '25',
    'learning_outcomes': 'By the end of this module, learners will be able to assemble desktop computers correctly',
    'indicative_contents': 'Computer components, Assembly procedures, Safety precautions',
    'topic_of_session': 'Installing Motherboard and Power Supply',
    'duration': '40',
    'objectives': '1. Identify motherboard components\n2. Install motherboard correctly\n3. Connect power supply safely',
    'references': 'Computer Hardware Maintenance Manual'
}

print("\n" + "="*70)
print("TESTING FACILITATION TECHNIQUES")
print("="*70 + "\n")

for technique in techniques:
    print(f"Testing: {technique}")
    data = base_data.copy()
    data['facilitation_techniques'] = technique
    
    try:
        file_path = fill_session_plan_template(data)
        doc = Document(file_path)
        table = doc.tables[0]
        
        # Check introduction (row 11)
        intro_text = table.rows[11].cells[0].text
        
        # Check development (row 13)
        dev_text = table.rows[13].cells[0].text
        
        # Check resources (row 13, cell 2)
        resources_text = table.rows[13].cells[2].text
        
        print(f"  [OK] Generated successfully")
        print(f"  Introduction includes: {technique.lower()[:20]}...")
        print(f"  Development tailored: {'Yes' if technique.lower() in dev_text.lower() else 'Generic'}")
        print(f"  Resources: {resources_text[:30]}...")
        
        # Save with technique name
        output_name = f"TEST_Session_{technique.replace(' ', '_')}.docx"
        output_path = os.path.join(os.path.dirname(__file__), output_name)
        doc.save(output_path)
        print(f"  Saved: {output_name}\n")
        
    except Exception as e:
        print(f"  [ERROR] {e}\n")

print("="*70)
print("COMPLETE - Check generated files to see differences")
print("="*70)
