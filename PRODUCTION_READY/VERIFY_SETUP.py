#!/usr/bin/env python3
"""
RTB Document Planner - Setup Verification Script
Checks all required files, dependencies, and configurations
"""

import os
import sys
import importlib
import subprocess
from pathlib import Path

BACKEND_DIR = Path(__file__).parent / "backend"
FRONTEND_DIR = Path(__file__).parent / "frontend"

# ANSI color codes
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

def print_header(text):
    print(f"\n{BLUE}{'='*60}{RESET}")
    print(f"{BLUE}{text.center(60)}{RESET}")
    print(f"{BLUE}{'='*60}{RESET}\n")

def print_success(text):
    print(f"{GREEN}✓ {text}{RESET}")

def print_error(text):
    print(f"{RED}✗ {text}{RESET}")

def print_warning(text):
    print(f"{YELLOW}⚠ {text}{RESET}")

def print_info(text):
    print(f"{BLUE}ℹ {text}{RESET}")

def check_python_version():
    print_header("1. Python Version Check")
    version = sys.version_info
    if version.major == 3 and version.minor >= 11:
        print_success(f"Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print_error(f"Python 3.11+ required (found {version.major}.{version.minor})")
        return False

def check_backend_files():
    print_header("2. Backend Files Check")
    required_files = [
        "main.py",
        "document_generator.py",
        "rtb_template_filler_exact.py",
        "facilitation_content_generator.py",
        "content_formatter.py",
        "ai_content_generator.py",
        "requirements.txt",
        "init_db.py",
        "rtb_session_plan_template.docx",
        "rtb_scheme_template.docx",
    ]
    
    all_present = True
    for file in required_files:
        filepath = BACKEND_DIR / file
        if filepath.exists():
            size_mb = filepath.stat().st_size / (1024 * 1024)
            print_success(f"{file} ({size_mb:.2f} MB)")
        else:
            print_error(f"{file} - MISSING")
            all_present = False
    
    return all_present

def check_frontend_files():
    print_header("3. Frontend Files Check")
    required_files = [
        "index.html",
        "login.html",
        "register.html",
        "wizard.html",
        "scheme-wizard.html",
        "teacher-dashboard.html",
        "admin.html",
        "auth.js",
        "config.js",
    ]
    
    all_present = True
    for file in required_files:
        filepath = FRONTEND_DIR / file
        if filepath.exists():
            size_kb = filepath.stat().st_size / 1024
            print_success(f"{file} ({size_kb:.1f} KB)")
        else:
            print_error(f"{file} - MISSING")
            all_present = False
    
    return all_present

def check_dependencies():
    print_header("4. Python Dependencies Check")
    required_packages = [
        "flask",
        "flask_cors",
        "docx",
        "sqlalchemy",
        "lxml",
    ]
    
    all_installed = True
    for package in required_packages:
        try:
            importlib.import_module(package)
            print_success(f"{package}")
        except ImportError:
            print_warning(f"{package} - NOT INSTALLED (install with: pip install -r requirements.txt)")
            all_installed = False
    
    return all_installed

def check_python_syntax():
    print_header("5. Python Syntax Check")
    python_files = [
        "main.py",
        "document_generator.py",
        "rtb_template_filler_exact.py",
        "facilitation_content_generator.py",
        "content_formatter.py",
        "ai_content_generator.py",
    ]
    
    all_valid = True
    for file in python_files:
        filepath = BACKEND_DIR / file
        if not filepath.exists():
            print_warning(f"{file} - FILE NOT FOUND")
            all_valid = False
            continue
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                compile(f.read(), str(filepath), 'exec')
            print_success(f"{file} - Syntax OK")
        except SyntaxError as e:
            print_error(f"{file} - Syntax Error: {e}")
            all_valid = False
        except Exception as e:
            print_error(f"{file} - Error: {e}")
            all_valid = False
    
    return all_valid

def check_database():
    print_header("6. Database Check")
    db_file = BACKEND_DIR / "rtb_planner.db"
    
    if db_file.exists():
        size_mb = db_file.stat().st_size / (1024 * 1024)
        print_success(f"Database found ({size_mb:.2f} MB)")
        return True
    else:
        print_warning("Database not found. Run: python init_db.py")
        return False

def check_port_availability():
    print_header("7. Port Availability Check")
    ports = {"8000": "Backend", "5173": "Frontend"}
    
    all_available = True
    for port, name in ports.items():
        try:
            import socket
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(('127.0.0.1', int(port)))
            sock.close()
            
            if result == 0:
                print_warning(f"Port {port} ({name}) - In use")
                all_available = False
            else:
                print_success(f"Port {port} ({name}) - Available")
        except Exception as e:
            print_error(f"Port {port} - Error checking: {e}")
            all_available = False
    
    return all_available

def main():
    print(f"\n{BLUE}╔{'='*58}╗{RESET}")
    print(f"{BLUE}║{'RTB Document Planner - Setup Verification'.center(58)}║{RESET}")
    print(f"{BLUE}╚{'='*58}╝{RESET}")
    
    results = {
        "Python Version": check_python_version(),
        "Backend Files": check_backend_files(),
        "Frontend Files": check_frontend_files(),
        "Dependencies": check_dependencies(),
        "Python Syntax": check_python_syntax(),
        "Database": check_database(),
        "Port Availability": check_port_availability(),
    }
    
    print_header("Verification Summary")
    
    passed = sum(1 for v in results.values() if v)
    total = len(results)
    
    for check, result in results.items():
        status = f"{GREEN}PASS{RESET}" if result else f"{RED}FAIL{RESET}"
        print(f"  {check}: {status}")
    
    print(f"\n  Total: {passed}/{total} checks passed\n")
    
    if passed == total:
        print_success("All checks passed! System is ready.")
        print("\nNext steps:")
        print("  1. Run: cd backend")
        print("  2. Run: pip install -r requirements.txt")
        print("  3. Run: python init_db.py")
        print("  4. Run: python main.py")
        print("\n  In another terminal:")
        print("  1. Run: cd frontend")
        print("  2. Run: python -m http.server 5173")
        return 0
    else:
        print_error(f"Some checks failed ({total - passed}/{total})")
        print("\nPlease fix the issues above before proceeding.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
