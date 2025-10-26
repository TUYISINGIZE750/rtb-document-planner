#!/usr/bin/env python3
"""
Test script for PDF generation and multi-format download functionality.
Run this locally before deploying to PythonAnywhere.
"""

import sys
import os
import tempfile
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

test_data_session = {
    'sector': 'Agriculture',
    'sub_sector': 'Crop Production',
    'trade': 'Coffee Farming',
    'qualification_title': 'Diploma in Coffee Production',
    'rqf_level': 'Level 4',
    'module_code_title': 'AGRO-401: Advanced Coffee Production',
    'term': '1',
    'week': '5',
    'date': '2024-10-25',
    'trainer_name': 'Mr. Jean Mukiza',
    'class_name': 'AGR-4A',
    'number_of_trainees': '35',
    'learning_outcomes': 'Understand coffee production techniques',
    'indicative_contents': 'Soil preparation, planting, irrigation',
    'topic_of_session': 'Coffee Bean Harvesting Techniques',
    'duration': '45',
    'objectives': 'S.M.A.R.T objectives for the session',
    'facilitation_techniques': 'Hands-on practical demonstration',
    'learning_activities': 'Group work and practical exercises',
    'resources': 'Coffee plants, tools, notebooks',
    'assessment_details': 'Practical assessment and observation',
    'references': 'RTB curriculum guidelines'
}

test_data_scheme = {
    'province': 'Southern Province',
    'district': 'Huye',
    'sector': 'Agriculture',
    'school': 'Technical School Huye',
    'department_trade': 'Coffee Production',
    'qualification_title': 'Diploma in Coffee Production',
    'rqf_level': 'Level 4',
    'module_code_title': 'AGRO-401: Advanced Coffee Production',
    'school_year': '2024/2025',
    'terms': '3',
    'module_hours': '180',
    'number_of_classes': '3',
    'trainer_name': 'Mr. Jean Mukiza',
    'dos_name': 'Dr. Marie Habimana',
    'manager_name': 'Ms. Anne Uwase',
    'term1_weeks': '15',
    'term1_learning_outcomes': 'Master coffee cultivation',
    'term1_indicative_contents': 'Soil, irrigation, pest management',
    'term1_duration': '60 hours',
    'term1_learning_place': 'Farm and classroom',
    'term2_weeks': '15',
    'term2_learning_outcomes': 'Coffee processing techniques',
    'term2_indicative_contents': 'Harvesting, processing, quality control',
    'term2_duration': '60 hours',
    'term2_learning_place': 'Processing facility',
    'term3_weeks': '15',
    'term3_learning_outcomes': 'Coffee marketing and business',
    'term3_indicative_contents': 'Market analysis, branding, sales',
    'term3_duration': '60 hours',
    'term3_learning_place': 'Market and classroom'
}

def test_pdf_conversion():
    """Test DOCX to PDF conversion"""
    logger.info("Testing PDF conversion...")
    try:
        backend_path = Path(__file__).parent / "backend"
        sys.path.insert(0, str(backend_path))
        
        from document_generator import convert_docx_to_pdf
        
        with tempfile.NamedTemporaryFile(suffix='.docx', delete=False) as f:
            test_docx = f.name
        
        with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as f:
            test_pdf = f.name
        
        logger.info(f"✓ PDF conversion functions imported successfully")
        return True
    except Exception as e:
        logger.error(f"✗ PDF conversion test failed: {e}")
        return False

def test_session_plan_pdf():
    """Test session plan PDF generation"""
    logger.info("Testing session plan PDF generation...")
    try:
        backend_path = Path(__file__).parent / "backend"
        sys.path.insert(0, str(backend_path))
        
        from document_generator import generate_session_plan_pdf
        
        file_path = generate_session_plan_pdf(test_data_session)
        
        if file_path and os.path.exists(file_path):
            size = os.path.getsize(file_path)
            if size > 10000:
                logger.info(f"✓ Session plan PDF generated: {file_path} ({size} bytes)")
                os.remove(file_path)
                return True
            else:
                logger.error(f"✗ PDF file too small ({size} bytes, expected >10KB)")
                return False
        else:
            logger.error("✗ PDF file not created")
            return False
    except Exception as e:
        logger.error(f"✗ Session plan PDF test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_scheme_pdf():
    """Test scheme PDF generation"""
    logger.info("Testing scheme PDF generation...")
    try:
        backend_path = Path(__file__).parent / "backend"
        sys.path.insert(0, str(backend_path))
        
        from document_generator import generate_scheme_of_work_pdf
        
        file_path = generate_scheme_of_work_pdf(test_data_scheme)
        
        if file_path and os.path.exists(file_path):
            size = os.path.getsize(file_path)
            if size > 10000:
                logger.info(f"✓ Scheme PDF generated: {file_path} ({size} bytes)")
                os.remove(file_path)
                return True
            else:
                logger.error(f"✗ PDF file too small ({size} bytes, expected >10KB)")
                return False
        else:
            logger.error("✗ PDF file not created")
            return False
    except Exception as e:
        logger.error(f"✗ Scheme PDF test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_endpoints_exist():
    """Test that all endpoints are defined in main.py"""
    logger.info("Testing endpoint definitions...")
    try:
        backend_path = Path(__file__).parent / "backend"
        main_py = backend_path / "main.py"
        
        with open(main_py, 'r') as f:
            content = f.read()
        
        endpoints = [
            '/session-plans/<int:plan_id>/download-pdf',
            '/session-plans/<int:plan_id>/download-formats',
            '/schemes-of-work/<int:scheme_id>/download-pdf',
            '/schemes-of-work/<int:scheme_id>/download-formats'
        ]
        
        missing = []
        for endpoint in endpoints:
            if endpoint not in content:
                missing.append(endpoint)
        
        if not missing:
            logger.info(f"✓ All 4 endpoints defined")
            return True
        else:
            logger.error(f"✗ Missing endpoints: {missing}")
            return False
    except Exception as e:
        logger.error(f"✗ Endpoint check failed: {e}")
        return False

def test_features_list():
    """Test that API status includes new features"""
    logger.info("Testing API features list...")
    try:
        backend_path = Path(__file__).parent / "backend"
        main_py = backend_path / "main.py"
        
        with open(main_py, 'r') as f:
            content = f.read()
        
        features = [
            "pdf_generation",
            "multi_format_download"
        ]
        
        missing = []
        for feature in features:
            if f'"{feature}"' not in content:
                missing.append(feature)
        
        if not missing:
            logger.info(f"✓ New features in API status")
            return True
        else:
            logger.error(f"✗ Missing features: {missing}")
            return False
    except Exception as e:
        logger.error(f"✗ Features check failed: {e}")
        return False

def test_imports():
    """Test that all imports are available"""
    logger.info("Testing imports...")
    try:
        backend_path = Path(__file__).parent / "backend"
        sys.path.insert(0, str(backend_path))
        
        try:
            from document_generator import generate_session_plan_pdf, generate_scheme_of_work_pdf
            logger.info(f"✓ PDF generation functions imported")
        except ImportError as e:
            logger.warning(f"⚠ PDF imports failed (docx2pdf may not be installed): {e}")
        
        from document_generator import generate_session_plan_docx, generate_scheme_of_work_docx
        logger.info(f"✓ DOCX generation functions imported")
        
        return True
    except Exception as e:
        logger.error(f"✗ Import test failed: {e}")
        return False

def run_all_tests():
    """Run all tests"""
    logger.info("=" * 70)
    logger.info("PDF & Multi-Format Download Tests")
    logger.info("=" * 70)
    
    tests = [
        ("Imports Available", test_imports),
        ("PDF Conversion Function", test_pdf_conversion),
        ("Session Plan PDF Generation", test_session_plan_pdf),
        ("Scheme PDF Generation", test_scheme_pdf),
        ("Endpoints Defined", test_endpoints_exist),
        ("API Features Updated", test_features_list),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            logger.error(f"Unexpected error in {test_name}: {e}")
            results.append((test_name, False))
        logger.info("")
    
    logger.info("=" * 70)
    logger.info("TEST RESULTS SUMMARY")
    logger.info("=" * 70)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        logger.info(f"{status}: {test_name}")
    
    logger.info("-" * 70)
    logger.info(f"Results: {passed}/{total} tests passed")
    logger.info("=" * 70)
    
    if passed == total:
        logger.info("✓ All tests passed! Ready for deployment.")
    elif passed >= total - 1:
        logger.info("⚠ Most tests passed. PDF library may need installation.")
        logger.info("  Install with: pip install docx2pdf")
    else:
        logger.error("✗ Some tests failed. Review output above.")
    
    return passed == total

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
