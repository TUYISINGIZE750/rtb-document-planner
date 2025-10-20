"""
PythonAnywhere WSGI Configuration File
This file must be set as the WSGI application in PythonAnywhere dashboard

Place this file in: /home/leonardus437/rtb-document-planner/
Then set WSGI Application to: /home/leonardus437/rtb-document-planner/pythonanywhere_wsgi.py
"""

import os
import sys

# Add the backend directory to Python path
path = '/home/leonardus437/rtb-document-planner'
if path not in sys.path:
    sys.path.insert(0, path)

# Change to the app directory
os.chdir(path)

# Set environment to production
os.environ['ENVIRONMENT'] = 'production'

# Import the FastAPI app from backend/main.py
from backend.main import app

# WSGI application - required by PythonAnywhere
application = app

# Application is ready - no need for debug prints
# PythonAnywhere will log "Import successful" automatically