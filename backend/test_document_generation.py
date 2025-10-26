"""Quick test script to verify document generation works correctly"""
import os
from rtb_template_filler_exact import fill_session_plan_template, fill_scheme_template

def test_session_plan():
    """Test session plan generation"""
    print("Testing Session Plan Generation...")
    
    data = {
        'sector': 'ICT',
        'trade': 'Computer Science',
        'date': '2024-01-15',
        'trainer_name': 'John Doe',
        'term': 'Term 1',
        'module_code_title': 'CSC101 - Introduction to Programming',
        'week': '1',
        'number_of_trainees': '30',
        'class_name': 'S4 Computer Science',
        'learning_outcomes': 'Students will be able to:\n- Define variables in Python\n- Identify different data types\n- Create and manipulate variables',
        'indicative_contents': 'Variables, Data types, Type conversion, Variable naming conventions',
        'topic_of_session': 'Variables and Data Types in Python',
        'duration': '90',
        'objectives': 'Define variables in Python\nIdentify different data types\nCreate and manipulate variables',
        'facilitation_techniques': 'Hands-on practice',
        'learning_activities': 'Students will practice creating variables and working with different data types through coding exercises',
        'resources': 'Computer lab\nPython IDE\nPractice worksheets',
        'assessment_details': 'Students will complete a coding exercise creating variables of different types',
        'references': ''
    }
    
    try:
        output_path = fill_session_plan_template(data)
        print(f"✅ Session Plan generated successfully: {output_path}")
        
        # Check file size
        size = os.path.getsize(output_path)
        print(f"   File size: {size:,} bytes")
        
        if size > 50000:  # Should be > 50KB
            print("   ✅ File size looks good")
        else:
            print("   ⚠️ File size seems small")
        
        return True
    except Exception as e:
        print(f"❌ Session Plan generation failed: {e}")
        return False

def test_scheme_of_work():
    """Test scheme of work generation"""
    print("\nTesting Scheme of Work Generation...")
    
    data = {
        'term1_weeks': '1-12',
        'term1_learning_outcomes': 'Design database schemas\nCreate tables and relationships\nWrite SQL queries',
        'term1_duration': '48 hours',
        'term1_indicative_contents': 'Database concepts\nER diagrams\nSQL basics',
        'term1_learning_place': 'Computer Lab',
        
        'term2_weeks': '13-24',
        'term2_learning_outcomes': 'Implement advanced queries\nOptimize database performance\nCreate stored procedures',
        'term2_duration': '48 hours',
        'term2_indicative_contents': 'Advanced SQL\nIndexing\nStored procedures',
        'term2_learning_place': 'Computer Lab',
        
        'term3_weeks': '25-36',
        'term3_learning_outcomes': 'Design complete database systems\nImplement security measures\nDeploy databases',
        'term3_duration': '48 hours',
        'term3_indicative_contents': 'Database security\nBackup and recovery\nProject implementation',
        'term3_learning_place': 'Computer Lab'
    }
    
    try:
        output_path = fill_scheme_template(data)
        print(f"✅ Scheme of Work generated successfully: {output_path}")
        
        # Check file size
        size = os.path.getsize(output_path)
        print(f"   File size: {size:,} bytes")
        
        if size > 50000:  # Should be > 50KB
            print("   ✅ File size looks good")
        else:
            print("   ⚠️ File size seems small")
        
        return True
    except Exception as e:
        print(f"❌ Scheme of Work generation failed: {e}")
        return False

if __name__ == "__main__":
    print("=" * 60)
    print("RTB Document Generation Test")
    print("=" * 60)
    
    session_ok = test_session_plan()
    scheme_ok = test_scheme_of_work()
    
    print("\n" + "=" * 60)
    print("Test Results:")
    print("=" * 60)
    print(f"Session Plan: {'✅ PASS' if session_ok else '❌ FAIL'}")
    print(f"Scheme of Work: {'✅ PASS' if scheme_ok else '❌ FAIL'}")
    
    if session_ok and scheme_ok:
        print("\n🎉 All tests passed! Documents are ready for deployment.")
    else:
        print("\n⚠️ Some tests failed. Please check the errors above.")
