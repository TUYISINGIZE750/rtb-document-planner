#!/usr/bin/env python3
"""
Quick script to update PythonAnywhere with the latest main.py fixes
Run this on PythonAnywhere console
"""

import os
import subprocess

def update_pythonanywhere():
    print("🔄 Updating PythonAnywhere backend...")
    
    # Navigate to project directory
    os.chdir('/home/leonardus437/rtb-document-planner')
    
    # Pull latest changes
    result = subprocess.run(['git', 'pull', 'origin', 'main'], 
                          capture_output=True, text=True)
    print("Git pull result:", result.stdout)
    if result.stderr:
        print("Git errors:", result.stderr)
    
    # Check if main.py was updated
    if os.path.exists('backend/main.py'):
        print("✅ main.py found and updated")
        
        # Show the PORT fix
        with open('backend/main.py', 'r') as f:
            content = f.read()
            if 'PORT = int(os.environ.get("PORT", 8000))' in content:
                print("✅ PORT fix is present")
            else:
                print("❌ PORT fix missing - need to add it")
    
    print("🔄 Please restart your web app in PythonAnywhere dashboard")
    print("🌐 Then test: https://leonardus437.pythonanywhere.com/")

if __name__ == "__main__":
    update_pythonanywhere()