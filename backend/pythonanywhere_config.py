#!/usr/bin/env python3
"""
PythonAnywhere Configuration Script
Run this on PythonAnywhere to set up environment variables
"""

import os
import sys

def setup_environment():
    """Set up environment variables for production"""
    
    # Set environment to production
    os.environ['ENVIRONMENT'] = 'production'
    os.environ['PORT'] = '8000'
    
    print("Environment variables set:")
    print(f"ENVIRONMENT = {os.environ.get('ENVIRONMENT')}")
    print(f"PORT = {os.environ.get('PORT')}")
    
    # Create a .env file for persistent storage
    env_content = """ENVIRONMENT=production
PORT=8000
"""
    
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("\n.env file created with production settings")
    print("Your backend is now configured for production!")

if __name__ == "__main__":
    setup_environment()