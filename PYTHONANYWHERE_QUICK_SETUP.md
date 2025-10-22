# PythonAnywhere Quick Setup Guide

## 🚨 URGENT: Backend Not Deployed Yet

Your frontend is live but the backend needs to be uploaded to PythonAnywhere.

## Quick Setup Steps:

### 1. Login to PythonAnywhere
- Go to https://www.pythonanywhere.com
- Login to your account: `leonardus437`

### 2. Upload Backend File
- Go to "Files" tab
- Navigate to your web app directory
- Upload `backend/main_production.py`
- Rename it to `main.py` (or update WSGI config)

### 3. Install Packages
Open a Bash console and run:
```bash
pip3.10 install --user flask flask-cors sqlalchemy python-docx
```

### 4. Update WSGI Configuration
- Go to "Web" tab
- Click on your web app
- In WSGI configuration file, make sure it points to your `main.py`

### 5. Reload Web App
- Click "Reload" button in Web tab
- Your API should now be available at: https://leonardus437.pythonanywhere.com

## Test Backend
Visit: https://leonardus437.pythonanywhere.com
Should return: `{"message": "RTB Document Planner API", "status": "online"}`

## After Backend is Live:
1. Teachers can register and login
2. Documents will download as proper DOCX files
3. Download limits will be enforced
4. Admin panel will work

## Files to Upload:
- `backend/main_production.py` → rename to `main.py`
- `backend/document_generator.py` (if not already there)

The frontend will automatically detect when the backend comes online!