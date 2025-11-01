# Complete Deployment Guide: Cloudflare + PythonAnywhere

## Overview
- **Frontend**: Cloudflare Pages (static HTML/JS)
- **Backend**: PythonAnywhere (Flask API)
- **Database**: SQLite on PythonAnywhere
- **Domain**: Auto-generated or custom

---

## PART 1: BACKEND DEPLOYMENT (PythonAnywhere)

### Step 1: Prepare PythonAnywhere Account
1. Go to https://www.pythonanywhere.com
2. Create account or log in (using: leonardus437)
3. Go to **Web** tab → **Add a new web app**
4. Select **Manual configuration** → **Python 3.10 or 3.11**

### Step 2: Upload Backend Files
1. Go to **Files** tab in PythonAnywhere
2. Create folder: `/home/leonardus437/rtb-document-planner/`
3. Upload from `PRODUCTION_READY/backend/`:
   ```
   - main.py
   - document_generator.py
   - ai_content_generator.py
   - facilitation_content_generator.py
   - content_formatter.py
   - enhanced_document_generator.py
   - requirements.txt
   - init_db.py
   - RTB Templates/
     ├── RTB Session plan template.docx
     └── Scheme of work.docx
   ```

### Step 3: Install Dependencies
1. Go to **Web** tab → Click on your web app
2. Scroll to **Virtualenv** section
3. Click "Start virtualenv"
4. **IMPORTANT**: Wait for it to complete (5-10 minutes)
5. Open **Bash console** and run:
   ```bash
   cd /home/leonardus437/rtb-document-planner
   pip install -r requirements.txt
   ```

### Step 4: Create Database
In **Bash console**, run:
```bash
cd /home/leonardus437/rtb-document-planner
python init_db.py
```

### Step 5: Configure WSGI File
1. Go to **Web** tab
2. In **WSGI configuration file** section, click the file link
3. Replace content with:
   ```python
   import sys
   import os
   
   project_home = '/home/leonardus437/rtb-document-planner'
   if project_home not in sys.path:
       sys.path.insert(0, project_home)
   
   os.chdir(project_home)
   
   from main import app as application
   
   os.environ['FLASK_ENV'] = 'production'
   os.environ['DATABASE_URL'] = 'sqlite:////home/leonardus437/rtb_planner.db'
   ```
4. **Save** and reload web app

### Step 6: Reload & Test
1. Go to **Web** tab
2. Click green **Reload** button
3. Visit `https://leonardus437.pythonanywhere.com/`
4. You should see: `{"message":"RTB Document Planner API is running"}`

### Troubleshooting PythonAnywhere
**If API not responding:**
- Check error log: **Web** → scroll down → **Error log**
- Check access log: **Web** → scroll down → **Access log**
- Verify virtualenv is active: bash console → `which python`
- Reinstall packages: `pip install --upgrade -r requirements.txt`

---

## PART 2: FRONTEND DEPLOYMENT (Cloudflare Pages)

### Option A: Cloudflare Pages (RECOMMENDED)

#### Step 1: Connect GitHub
1. Go to https://dash.cloudflare.com
2. Select your domain (or create free domain with .pages.dev)
3. Go to **Pages** → **Create a project**
4. Connect to GitHub account
5. Select your RTB repository
6. Select branch: `main`

#### Step 2: Configure Build Settings
1. **Framework preset**: None (static HTML)
2. **Build command**: Leave empty
3. **Build output directory**: `PRODUCTION_READY/frontend`
4. **Environment variables**: Add if needed
5. Click **Save and Deploy**

#### Step 3: Cloudflare Pages Deployment Settings
1. Go to **Pages** → Your project → **Settings**
2. Go to **Custom domains**
3. Add custom domain or use auto-generated `*.pages.dev`
4. Note your URL (e.g., `https://rtb-planner.pages.dev`)

#### Step 4: Update Frontend Config (if using custom domain)
1. Edit `PRODUCTION_READY/frontend/config.js`
2. If your domain is different, add it to detection logic:
   ```javascript
   if (window.location.hostname.includes('your-custom-domain.com')) {
       return 'https://leonardus437.pythonanywhere.com';
   }
   ```

#### Step 5: Redeploy
1. Push changes to GitHub
2. Cloudflare automatically redeploys
3. Visit your domain and test

---

### Option B: Manual Upload (Zip)

If not using GitHub:

1. Go to https://dash.cloudflare.com/pages
2. Create a new project → **Upload assets**
3. Drag and drop contents of `PRODUCTION_READY/frontend/` folder
4. Configure custom domain
5. Click **Save**

---

## PART 3: CONNECTING FRONTEND & BACKEND

### Verify CORS Configuration

**Check if already updated:**
1. Backend (`PRODUCTION_READY/backend/main.py`, lines 27-60) includes:
   ```python
   "https://*.pages.dev",
   "https://*.cloudflareaccess.com",
   ```

**If not, apply these changes:**
- Update `main.py` CORS origins (see template below)
- Redeploy to PythonAnywhere

### Frontend API Configuration

**File**: `PRODUCTION_READY/frontend/config.js`

Already includes dynamic detection:
```javascript
if (window.location.hostname.includes('pages.dev')) {
    return 'https://leonardus437.pythonanywhere.com';
}
```

---

## PART 4: TESTING INTEGRATION

### Test 1: API Health Check
Open browser console and run:
```javascript
fetch('https://leonardus437.pythonanywhere.com/', {
    method: 'GET',
    mode: 'cors',
    headers: {'Content-Type': 'application/json'}
})
.then(r => r.json())
.then(d => console.log('✅ Backend OK:', d))
.catch(e => console.error('❌ Backend Error:', e))
```

### Test 2: Frontend Loads
Visit your Cloudflare domain and check browser console for:
```
✅ config.js loaded (PRODUCTION CLOUDFLARE + PYTHONANYWHERE)
🌐 API Base URL: https://leonardus437.pythonanywhere.com
✅ API connection successful
```

### Test 3: Full Workflow
1. Register new user
2. Log in
3. Create session plan
4. Download as DOCX
5. Verify file integrity

---

## PART 5: PRODUCTION CHECKLIST

- [ ] Backend running on PythonAnywhere (`https://leonardus437.pythonanywhere.com`)
- [ ] Frontend deployed to Cloudflare Pages
- [ ] API endpoint accessible from frontend
- [ ] CORS properly configured
- [ ] Database initialized on PythonAnywhere
- [ ] RTB templates uploaded to `/home/leonardus437/rtb-document-planner/`
- [ ] User registration working
- [ ] Document generation working
- [ ] Downloads functioning correctly
- [ ] SSL certificates valid (automatic with both services)

---

## IMPORTANT FILES TO UPLOAD

### To PythonAnywhere `/home/leonardus437/rtb-document-planner/`:

**Core:**
- `main.py` - Main Flask app
- `requirements.txt` - Python dependencies
- `init_db.py` - Database initialization

**Generators:**
- `document_generator.py`
- `ai_content_generator.py`
- `facilitation_content_generator.py`
- `content_formatter.py`
- `enhanced_document_generator.py`

**Templates:**
- `RTB Templates/RTB Session plan template.docx`
- `RTB Templates/Scheme of work.docx`

### To Cloudflare Pages `PRODUCTION_READY/frontend/`:

- `index.html`
- `login.html`
- `register.html`
- `teacher-dashboard.html`
- `admin.html`
- `admin-final.html`
- `scheme-wizard.html`
- `wizard.html`
- `config.js`
- `auth.js`
- `*.js` - All JavaScript files
- `*.css` - All CSS files

---

## QUICK TROUBLESHOOTING

| Issue | Solution |
|-------|----------|
| CORS errors | Check main.py lines 27-60, add domain to allowed_origins |
| 404 on API | Verify WSGI file configured, run reload in Web tab |
| Documents not generating | Check RTB template files uploaded to correct path |
| Database errors | Run `python init_db.py` in PythonAnywhere console |
| Frontend blank | Check browser console for JavaScript errors |
| API timeout | Increase PythonAnywhere timeout in Web tab settings |

---

## MAINTENANCE

### Regular Tasks:
- Monitor PythonAnywhere logs for errors
- Backup database monthly
- Monitor Cloudflare analytics
- Update dependencies quarterly

### Database Backup:
```bash
# In PythonAnywhere Bash console:
cd /home/leonardus437/rtb-document-planner
cp rtb_planner.db rtb_planner.db.backup.$(date +%Y%m%d)
```

---

## SUPPORT RESOURCES

- **PythonAnywhere Docs**: https://www.pythonanywhere.com/help/
- **Cloudflare Docs**: https://developers.cloudflare.com/pages/
- **Flask CORS**: https://flask-cors.readthedocs.io/

---

**Last Updated**: October 26, 2025
**Status**: Ready for Deployment
