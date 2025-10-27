# PythonAnywhere File Upload Guide

## Critical Files - MUST Upload These

### Backend Core Files (Upload to `/var/www/` directory)
```
backend/main.py                              [REQUIRED] - Flask app with CORS
backend/document_generator.py                [REQUIRED] - RTB document generation (FIXED)
backend/ai_content_generator.py              [REQUIRED] - AI content enhancement
backend/facilitation_content_generator.py    [REQUIRED] - Facilitation techniques
backend/init_db.py                           [OPTIONAL] - Database initialization
backend/requirements.txt                     [REQUIRED] - Python dependencies
```

### RTB Template Files (Upload to `/var/www/backend/RTB Templates/`)
```
backend/RTB Templates/RTB Session plan template.docx    [REQUIRED] - Session plan template
backend/RTB Templates/Scheme of work.docx               [REQUIRED] - Scheme of work template
```

## Frontend Files (Upload to your web root)
```
frontend/index.html              [REQUIRED]
frontend/wizard.html             [REQUIRED]
frontend/scheme-wizard.html      [REQUIRED]
frontend/teacher-dashboard.html  [REQUIRED]
frontend/login.html              [REQUIRED]
frontend/register.html           [REQUIRED]
frontend/admin.html              [OPTIONAL]
frontend/config.js               [REQUIRED] - API configuration
frontend/auth.js                 [REQUIRED] - Authentication
frontend/subscription-modal.js   [REQUIRED]
frontend/subscription-modal.css  [REQUIRED]
frontend/subscription-tracker.js [REQUIRED]
```

## Step-by-Step PythonAnywhere Upload

### 1. **Log into PythonAnywhere**
   - Go to https://www.pythonanywhere.com
   - Sign in with your account (leonardus437)

### 2. **Create Directory Structure**
   - Go to **Files** tab
   - Create `/var/www/backend/RTB Templates/` directory
   - Create `/var/www/` if it doesn't exist

### 3. **Upload Backend Files**
   - Navigate to `/var/www/` in PythonAnywhere Files
   - Upload these files:
     - `main.py`
     - `document_generator.py`
     - `ai_content_generator.py`
     - `facilitation_content_generator.py`
     - `init_db.py`
     - `requirements.txt`

### 4. **Upload RTB Templates**
   - Navigate to `/var/www/backend/RTB Templates/`
   - Upload these files:
     - `RTB Session plan template.docx`
     - `Scheme of work.docx`

### 5. **Install Dependencies**
   - Go to **Web** tab → Your PythonAnywhere app
   - Open **Bash console**
   - Run commands:
     ```bash
     cd /var/www
     pip install -r requirements.txt
     ```

### 6. **Configure WSGI File**
   - Go to **Web** tab
   - Click on your PythonAnywhere app (e.g., `leonardus437.pythonanywhere.com`)
   - Scroll to **WSGI configuration file**
   - Replace content with:

```python
import sys
path = '/var/www'
if path not in sys.path:
    sys.path.insert(0, path)

from main import app
application = app
```

### 7. **Reload Your App**
   - In the **Web** tab, click the green **Reload** button
   - Wait 5-10 seconds for reload

### 8. **Verify Installation**
   - Open your browser: `https://leonardus437.pythonanywhere.com/`
   - Should see API response (check browser console for details)
   - If error, check **Error log** in PythonAnywhere Web tab

---

## Verification Checklist

- [ ] Backend files uploaded to `/var/www/`
- [ ] RTB templates uploaded to `/var/www/backend/RTB Templates/`
- [ ] requirements.txt installed via pip
- [ ] WSGI file configured correctly
- [ ] App reloaded
- [ ] API endpoint responds at `https://leonardus437.pythonanywhere.com/`
- [ ] Frontend config.js points to correct API URL

## Troubleshooting

**If documents are still unstructured:**
- ✅ Check that `document_generator.py` is the new version (should have "FIXED" in docstring)
- ✅ Verify RTB templates exist in `/var/www/backend/RTB Templates/`
- ✅ Check error log in PythonAnywhere

**If API returns 403/CORS error:**
- ✅ Verify CORS configuration in `main.py`
- ✅ Check frontend config.js has correct API URL
- ✅ Reload PythonAnywhere app after changes

**If templates not loading:**
- ✅ Verify exact path: `/var/www/backend/RTB Templates/`
- ✅ Check file permissions (should be readable)
- ✅ Verify template filenames match exactly
