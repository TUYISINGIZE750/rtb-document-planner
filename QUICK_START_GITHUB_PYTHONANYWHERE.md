# Quick Start: GitHub + PythonAnywhere Setup

## ⚡ GitHub Setup (5 minutes)

### Step 1: Open Git Bash
Right-click in your project folder → **Git Bash Here**

### Step 2: Initialize & Configure
```bash
git init
git config user.email "your@email.com"
git config user.name "Your Name"
```

### Step 3: Create .gitignore
```bash
cat > .gitignore << 'EOF'
__pycache__/
*.py[cod]
.Python
env/
venv/
*.db
*.sqlite
*.sqlite3
.env
.vscode/
.idea/
TEST_*.docx
test_*.py
EOF
```

### Step 4: Add Remote (Replace YOUR_USERNAME)
```bash
git remote add origin https://github.com/YOUR_USERNAME/rtb-document-planner.git
```

### Step 5: Stage & Commit
```bash
git add .
git commit -m "Initial commit: RTB Document Planner production ready"
```

### Step 6: Push
```bash
git branch -M main
git push -u origin main
```

---

## 🚀 PythonAnywhere Upload (10 minutes)

### Step 1: Log In
https://www.pythonanywhere.com → Sign in

### Step 2: Create Directories
**Files tab** → Create:
- `/var/www/backend/RTB Templates/`

### Step 3: Upload Backend Files
Upload to `/var/www/`:
- `main.py`
- `document_generator.py`
- `ai_content_generator.py`
- `facilitation_content_generator.py`
- `init_db.py`
- `requirements.txt`

### Step 4: Upload Templates
Upload to `/var/www/backend/RTB Templates/`:
- `RTB Session plan template.docx`
- `Scheme of work.docx`

### Step 5: Install Dependencies
**Bash Console:**
```bash
cd /var/www
pip install -r requirements.txt
```

### Step 6: Configure WSGI
**Web tab** → Click your app → WSGI configuration file

Replace with:
```python
import sys
path = '/var/www'
if path not in sys.path:
    sys.path.insert(0, path)

from main import app
application = app
```

### Step 7: Reload
Click green **Reload** button

### Step 8: Verify
Open https://leonardus437.pythonanywhere.com in browser

---

## ✅ What You Have

### Backend (Production Ready)
- ✅ `document_generator.py` - FIXED (no unstructured text)
- ✅ `main.py` - CORS configured for Cloudflare
- ✅ `ai_content_generator.py` - AI enhancements
- ✅ RTB Templates - Professional formatting

### Frontend (Production Ready)
- ✅ `config.js` - Auto-detects backend URL
- ✅ All HTML files - Full application UI
- ✅ All JS files - Authentication & features

### Documentation (Complete)
- ✅ `PYTHONANYWHERE_FILES_TO_UPLOAD.md` - Detailed upload guide
- ✅ `GITHUB_COMMIT_GUIDE.md` - Full GitHub instructions
- ✅ `FINAL_VERIFICATION_CHECKLIST.md` - Pre-deployment checklist

---

## 📋 Files to Keep Track Of

**Critical (must upload):**
- `PRODUCTION_READY/backend/main.py`
- `PRODUCTION_READY/backend/document_generator.py`
- `PRODUCTION_READY/backend/ai_content_generator.py`
- `PRODUCTION_READY/backend/facilitation_content_generator.py`
- `PRODUCTION_READY/backend/requirements.txt`
- `PRODUCTION_READY/backend/RTB Templates/` (both .docx files)
- `PRODUCTION_READY/frontend/` (all HTML, JS, CSS files)

**Documentation (reference):**
- `PYTHONANYWHERE_FILES_TO_UPLOAD.md`
- `GITHUB_COMMIT_GUIDE.md`
- `FINAL_VERIFICATION_CHECKLIST.md`
- `QUICK_START_GITHUB_PYTHONANYWHERE.md`

---

## 🔍 Key Changes Made

| Issue | Fix |
|-------|-----|
| Documents unstructured | Rewrote `document_generator.py` to use RTB template first |
| CORS errors with Cloudflare | Updated main.py CORS to support `*.pages.dev` |
| API URL hardcoded | Made config.js dynamic URL detection |
| Multiple conflicting modules | Consolidated to single document generator |

---

## 💡 Pro Tips

1. **Test Locally First**
   - Run frontend on `localhost:8000`
   - Run backend on separate terminal
   - Verify document generation works before uploading

2. **Check Logs if Issues**
   - PythonAnywhere: **Web tab** → Error log
   - Frontend: Browser DevTools → Console tab

3. **RTB Templates Matter**
   - Documents MUST be in `/var/www/backend/RTB Templates/`
   - Path IS case-sensitive on Linux
   - If missing, documents still have structure (not unstructured text)

4. **Future Updates**
   - Just push new changes to GitHub
   - Pull them on PythonAnywhere
   - Reload the app

---

## ❓ Troubleshooting

**Document still unstructured?**
→ Check that uploaded `document_generator.py` has "FIXED" in docstring

**API returns 403?**
→ Verify CORS in main.py matches your frontend domain

**Template not loading?**
→ Check exact path and filename in PythonAnywhere Files

**Build failed on Cloudflare?**
→ Ensure all frontend files present and valid

---

## ✨ You're Ready!

All code is production-ready. Just follow the steps above to deploy. Start with GitHub (5 min), then PythonAnywhere (10 min).
