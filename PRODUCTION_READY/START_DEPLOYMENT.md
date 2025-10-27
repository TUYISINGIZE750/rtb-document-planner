# 🚀 Quick Start: Deploy RTB Planner

## 5-Minute Checklist

### What You Need
- ✓ PythonAnywhere account (https://pythonanywhere.com)
- ✓ Cloudflare account (https://dash.cloudflare.com)
- ✓ GitHub account (optional, for auto-deploy)

---

## STEP 1: Deploy Backend (PythonAnywhere) - 15 mins

### 1.1 Create Web App
1. Log in to **PythonAnywhere**
2. **Web** tab → **Add a new web app** → **Manual configuration** → **Python 3.10**
3. Note your URL: `https://leonardus437.pythonanywhere.com`

### 1.2 Upload Files
1. Go to **Files** tab
2. Create folder: `rtb-document-planner`
3. Upload from `PRODUCTION_READY/backend/`:
   - `main.py`
   - `requirements.txt`
   - `init_db.py`
   - `document_generator.py`
   - `ai_content_generator.py`
   - `facilitation_content_generator.py`
   - `content_formatter.py`
   - `enhanced_document_generator.py`
4. Create subfolder: `RTB Templates`
5. Upload template files:
   - `RTB Session plan template.docx`
   - `Scheme of work.docx`

### 1.3 Install Dependencies
1. **Web** tab → Your web app → **Virtualenv** → "Start virtualenv"
2. Wait 5-10 minutes
3. Open **Bash console**:
   ```bash
   cd /home/leonardus437/rtb-document-planner
   pip install -r requirements.txt
   python init_db.py
   ```

### 1.4 Configure WSGI
1. **Web** tab → Scroll to **WSGI configuration file**
2. Click the file path link
3. **Copy and paste** this code:
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
4. **Save file** → Go back to **Web** tab → Click green **Reload** button

### 1.5 Test Backend
Visit: `https://leonardus437.pythonanywhere.com/`

Expected response:
```json
{"message":"RTB Document Planner API is running"}
```

**✅ Backend Ready!**

---

## STEP 2: Deploy Frontend (Cloudflare Pages) - 10 mins

### OPTION A: GitHub Integration (AUTO-DEPLOY)

1. Push `PRODUCTION_READY/frontend/` to GitHub
2. Go to **https://dash.cloudflare.com**
3. **Pages** → **Create a project** → **Connect to Git**
4. Select repository
5. Configuration:
   - **Framework**: None (static HTML)
   - **Build command**: Leave empty
   - **Build output directory**: `PRODUCTION_READY/frontend`
6. **Save and deploy** ✨

### OPTION B: Manual Upload

1. Go to **https://dash.cloudflare.com/pages**
2. **Create a project** → **Upload assets**
3. Drag & drop contents of `PRODUCTION_READY/frontend/` folder
4. Click **Deploy** 🎉

### 1.6 Get Your Frontend URL
- **Auto**: `https://your-project.pages.dev`
- **Custom**: Configure in Cloudflare dashboard
- **Note**: Your URL is used in next step

**✅ Frontend Ready!**

---

## STEP 3: Connect Frontend to Backend - 2 mins

Your config is **already set up** to auto-detect!

### Verify Connection
1. Visit your Cloudflare frontend URL
2. Open **Browser Console** (F12 key)
3. Look for:
   ```
   ✅ config.js loaded
   🌐 API Base URL: https://leonardus437.pythonanywhere.com
   ✅ API connection successful
   ```

If you see ✅ all green → **Connected! 🎉**

### If Not Connected
Edit `PRODUCTION_READY/frontend/config.js` line 7:
```javascript
if (window.location.hostname.includes('your-cloudflare-domain')) {
    return 'https://leonardus437.pythonanywhere.com';
}
```

Redeploy with new config.

---

## STEP 4: Test Everything Works

### Test User Registration
1. Visit your frontend URL
2. Click "Register"
3. Fill in test data:
   - Name: Test Teacher
   - Phone: +250700000099
   - Email: test@example.com
   - Institution: Test School
   - Password: Test123456
4. Click **Register** → Should redirect to login

### Test Login
1. Enter phone: `+250700000099`
2. Enter password: `Test123456`
3. Click **Login** → Should show dashboard

### Test Document Creation
1. Click **Create Session Plan** (or **Create Scheme**)
2. Fill in required fields
3. Click **Submit** → Document generates
4. Click **Download** → DOCX file downloads

### Test Downloaded Document
1. Open downloaded DOCX with Microsoft Word or LibreOffice
2. Verify RTB template structure intact
3. Check data properly filled in

**✅ Everything Working!**

---

## MONITORING & MAINTENANCE

### Check Backend Status
```bash
# In PythonAnywhere Bash console:
tail -f /var/log/leonardus437.pythonanywhere.com.error.log
```

### View Activity Logs
- **PythonAnywhere**: Web → Scroll down → Error log / Access log
- **Cloudflare**: Pages → Analytics

### Monthly Tasks
- Backup database: `cp rtb_planner.db rtb_planner.db.backup`
- Check for errors in logs
- Update dependencies if needed

---

## TROUBLESHOOTING

| Problem | Solution |
|---------|----------|
| Backend returns 500 error | Check PythonAnywhere error log |
| CORS errors in browser | Verify main.py line 56 includes your domain |
| Files not found | Use `ls` in PythonAnywhere bash to verify files exist |
| Slow performance | Increase PythonAnywhere CPU/RAM in settings |
| Documents won't generate | Verify RTB template files in correct folder |

---

## FULL DOCUMENTATION

For detailed info, see:
- **Complete Guide**: `CLOUDFLARE_PYTHONANYWHERE_DEPLOYMENT.md`
- **Files to Upload**: `FILES_TO_UPLOAD.md`
- **Test Script**: `TEST_INTEGRATION.py` (run locally)

---

## SUPPORT

Need help? Check these resources:
- **PythonAnywhere Help**: https://help.pythonanywhere.com/
- **Cloudflare Pages Docs**: https://developers.cloudflare.com/pages/
- **Flask CORS**: https://flask-cors.readthedocs.io/

---

**Status**: Ready for Production ✨  
**Last Updated**: October 26, 2025
