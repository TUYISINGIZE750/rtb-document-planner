"""
RTB Document Planner - Setup Verification Script
Checks all components and dependencies before running the application
"""
import os
import sys
import subprocess
from pathlib import Path

def check_python_version():
    """Check Python version compatibility"""
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - Compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} - Requires Python 3.8+")
        return False

def check_file_structure():
    """Verify all required files exist"""
    required_files = [
        "backend/main.py",
        "backend/models.py", 
        "backend/schemas.py",
        "backend/database.py",
        "backend/document_generator.py",
        "backend/startup.py",
        "backend/init_db.py",
        "backend/requirements.txt",
        "frontend/index.html",
        "docker-compose.yml",
        "start_all.bat"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if not missing_files:
        print("✅ All required files present")
        return True
    else:
        print("❌ Missing files:")
        for file in missing_files:
            print(f"   - {file}")
        return False

def check_dependencies():
    """Check if Python dependencies are installed"""
    required_packages = [
        "fastapi",
        "uvicorn", 
        "sqlalchemy",
        "pydantic",
        "python-docx"
    ]
    
    missing_packages = []
    for package in required_packages:
        try:
            __import__(package.replace("-", "_"))
        except ImportError:
            missing_packages.append(package)
    
    if not missing_packages:
        print("✅ All Python dependencies installed")
        return True
    else:
        print("❌ Missing Python packages:")
        for package in missing_packages:
            print(f"   - {package}")
        print("\nInstall with: pip install -r backend/requirements.txt")
        return False

def check_ports():
    """Check if required ports are available"""
    import socket
    
    ports_to_check = [8000, 5173]
    busy_ports = []
    
    for port in ports_to_check:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex(('localhost', port))
        sock.close()
        
        if result == 0:
            busy_ports.append(port)
    
    if not busy_ports:
        print("✅ Required ports (8000, 5173) are available")
        return True
    else:
        print("❌ Ports already in use:")
        for port in busy_ports:
            print(f"   - Port {port}")
        print("\nStop services using these ports or use different ports")
        return False

def check_database_setup():
    """Verify database can be initialized"""
    try:
        os.chdir("backend")
        
        # Try to import database modules
        sys.path.insert(0, os.getcwd())
        from database import engine, Base
        from models import SessionPlan, SchemeOfWork
        
        # Test database creation
        Base.metadata.create_all(bind=engine)
        print("✅ Database setup successful")
        
        os.chdir("..")
        return True
        
    except Exception as e:
        print(f"❌ Database setup failed: {e}")
        os.chdir("..")
        return False

def check_document_generation():
    """Test document generation capability"""
    try:
        os.chdir("backend")
        sys.path.insert(0, os.getcwd())
        
        from document_generator import generate_session_plan_docx
        from models import SessionPlan
        
        # Create a test session plan object
        class TestSessionPlan:
            def __init__(self):
                self.sector = "Test Sector"
                self.topic_of_session = "Test Topic"
                self.trainer_name = "Test Trainer"
                self.duration = "40"
                self.learning_outcomes = "Test outcomes"
                self.indicative_contents = "Test contents"
                self.facilitation_techniques = "Test technique"
                self.objectives = "Test objectives"
                self.resources = "Test resources"
                self.references = "Test references"
                self.reflection = "Test reflection"
        
        test_plan = TestSessionPlan()
        
        # Test document generation
        temp_file = generate_session_plan_docx(test_plan)
        
        if os.path.exists(temp_file):
            os.remove(temp_file)  # Clean up
            print("✅ Document generation working")
            os.chdir("..")
            return True
        else:
            print("❌ Document generation failed")
            os.chdir("..")
            return False
            
    except Exception as e:
        print(f"❌ Document generation test failed: {e}")
        os.chdir("..")
        return False

def main():
    """Run all verification checks"""
    print("=" * 60)
    print("RTB Document Planner - Setup Verification")
    print("=" * 60)
    print()
    
    checks = [
        ("Python Version", check_python_version),
        ("File Structure", check_file_structure),
        ("Python Dependencies", check_dependencies),
        ("Port Availability", check_ports),
        ("Database Setup", check_database_setup),
        ("Document Generation", check_document_generation)
    ]
    
    results = []
    
    for check_name, check_func in checks:
        print(f"Checking {check_name}...")
        result = check_func()
        results.append(result)
        print()
    
    print("=" * 60)
    
    if all(results):
        print("🎉 ALL CHECKS PASSED!")
        print("=" * 60)
        print()
        print("Your RTB Document Planner is ready to run!")
        print()
        print("To start the application:")
        print("1. Run: start_all.bat")
        print("2. Or use: docker-compose up --build")
        print("3. Or manually start backend and frontend")
        print()
        print("Access points:")
        print("- Frontend: http://localhost:5173")
        print("- API Docs: http://localhost:8000/docs")
        print("- Health: http://localhost:8000/health")
        
    else:
        print("❌ SOME CHECKS FAILED")
        print("=" * 60)
        print()
        print("Please fix the issues above before running the application.")
        print("Refer to the README.md for detailed setup instructions.")
    
    print()
    print("=" * 60)

if __name__ == "__main__":
    main()