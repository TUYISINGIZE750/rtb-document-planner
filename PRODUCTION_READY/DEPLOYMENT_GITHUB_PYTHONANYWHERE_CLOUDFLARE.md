# Complete Deployment Guide: GitHub → PythonAnywhere → Cloudflare

## 1. FILES TO PUSH TO GITHUB

### Core Backend Files (MUST include):
```
backend/
├── main.py                          ✓ Main Flask application
├── requirements.txt                 ✓ Python dependencies
├── document_generator.py            ✓ DOCX/PDF generation
├── rtb_template_generator.py        ✓ Template filling (UPDATED)
├── ai_content_generator.py          ✓ AI content enhancement
├── facilitation_content_generator.py ✓ Facilitation content
├── smart_content_generator.py       ✓ Smart content generation
├── content_formatter.py             ✓ Content formatting
├── init_db.py                       ✓ Database initialization
└── RTB Templates/                   ✓ Official templates folder
    ├── RTB Session plan template.docx
    └── Scheme of work.docx

frontend/
├── index.html                       ✓ Home/dashboard
├── wizard.html                      ✓ Session plan wizard
├── scheme-wizard.html               ✓ Scheme of work wizard
├── login.html                       ✓ Login page
├── register.html                    ✓ Registration page
├── admin.html                       ✓ Admin dashboard
├── auth.js                          ✓ Authentication logic
├── config.js                        ✓ Configuration
├── subscription-modal.js            ✓ Subscription modal
├── subscription-tracker.js          ✓ Subscription tracking
└── *.css                            ✓ Stylesheets
```

### Optional/Development Files (DO NOT push):
```
✗ test_*.py                         (Test scripts)
✗ TEST_*.docx                       (Test outputs)
✗ *.md (except README.md)           (Documentation)
✗ __pycache__/                      (Cache)
✗ *.pyc                             (Compiled Python)
✗ .env                              (Secrets - NEVER push)
```

---

## 2. GITHUB SETUP

### Step 1: Initialize Git Repository
```bash
cd "c:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY"
git init
git config user.name "Your Name"
git config user.email "your.email@example.com"
```

### Step 2: Create .gitignore File
```bash
# Create file: PRODUCTION_READY/.gitignore
```

**Contents of .gitignore:**
```
# Python
__pycache__/
*.pyc
*.pyo
*.egg-info/
.Python
env/
venv/

# IDE
.vscode/
.idea/
*.swp
*.swo

# Test files
test_*.py
TEST_*.docx
VERIFY_*.py
quick_test.py

# Database
*.db
*.sqlite
*.sqlite3

# Temporary
*.tmp
*.temp
temp_*.py

# Environment
.env
.env.local
.env.*.local

# Documentation (keep README.md only)
*.md
!README.md

# OS
.DS_Store
Thumbs.db

# Cache
.deployment-timestamp
.git/
```

### Step 3: Create GitHub Repository
1. Go to https://github.com/new
2. Create repository: `rtb-document-planner`
3. Initialize with no README (you'll add one)
4. Copy the repository URL

### Step 4: Push Code to GitHub
```bash
cd PRODUCTION_READY

git add .
git commit -m "Initial commit: RTB Document Planner with template generator"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/rtb-document-planner.git
git push -u origin main
```

### Step 5: Create README.md
```bash
# Create: PRODUCTION_READY/README.md
```

**Contents:**
```markdown
# RTB Document Planner

A comprehensive application for generating Rwanda Technical Board (RTB) compliant session plans and schemes of work using official templates.

## Features

- ✅ Generate session plans from official RTB templates
- ✅ Generate schemes of work (3 terms)
- ✅ AI-powered content enhancement
- ✅ Multi-format downloads (DOCX, PDF)
- ✅ User authentication & subscription tracking
- ✅ Real-time document preview

## Quick Start

### Local Development

```bash
# Install dependencies
pip install -r backend/requirements.txt

# Run Flask app
python backend/main.py
```

Visit: http://localhost:5000

### Deployment

See deployment guide: `DEPLOYMENT_GITHUB_PYTHONANYWHERE_CLOUDFLARE.md`

## Technology Stack

- **Backend**: Flask 3.0.0
- **Frontend**: HTML5, JavaScript, CSS3
- **Database**: SQLAlchemy ORM
- **Document Generation**: python-docx, docx2pdf
- **Hosting**: PythonAnywhere + Cloudflare

## License

MIT License
```

---

## 3. UPLOAD TO PYTHONANYWHERE

### Files to Upload via PythonAnywhere Files Manager

**Upload Location**: `/home/YOUR_USERNAME/rtb_planner/`

**Files to Upload** (in this order):

#### 1. Backend Python Files
- `backend/main.py`
- `backend/document_generator.py`
- `backend/rtb_template_generator.py` ← **NEWLY UPDATED**
- `backend/ai_content_generator.py`
- `backend/facilitation_content_generator.py`
- `backend/smart_content_generator.py`
- `backend/content_formatter.py`
- `backend/init_db.py`
- `backend/requirements.txt`

#### 2. Frontend Files
- Upload entire `frontend/` folder

#### 3. RTB Templates (CRITICAL)
- Create folder: `/home/YOUR_USERNAME/rtb_planner/RTB Templates/`
- Upload:
  - `RTB Session plan template.docx`
  - `Scheme of work.docx`

### Step-by-Step Upload

**Method A: Via PythonAnywhere Web Interface (Recommended)**

1. Log in: https://www.pythonanywhere.com
2. Click "Files" → Navigate to `/home/YOUR_USERNAME/rtb_planner/`
3. Click "Upload a file" 
4. Upload each file from `backend/` folder
5. Repeat for `frontend/` files
6. Create folder "RTB Templates" and upload `.docx` files

**Method B: Via Bash Console (Advanced)**

```bash
# SSH into PythonAnywhere
ssh YOUR_USERNAME@ssh.pythonanywhere.com

# Navigate to project
cd /home/YOUR_USERNAME/rtb_planner/

# If cloning from GitHub (recommended for future updates):
git clone https://github.com/YOUR_USERNAME/rtb-document-planner.git .

# Install dependencies
pip install -r backend/requirements.txt

# Create RTB Templates folder if not exists
mkdir -p "RTB Templates"
```

### After Upload: Update requirements.txt

**Edit** `/home/YOUR_USERNAME/rtb_planner/requirements.txt`:

Ensure it includes:
```
flask==3.0.0
flask-cors==4.0.0
python-docx==1.1.0
lxml==4.9.3
sqlalchemy==2.0.23
docx2pdf==0.5.0
pydantic==2.5.0
gunicorn==21.2.0
psycopg2-binary==2.9.9
python-multipart==0.0.6
jinja2==3.1.2
requests==2.31.0
```

### Configure WSGI File

**Edit** `/var/www/YOUR_USERNAME_pythonanywhere_com_wsgi.py`:

```python
import sys
import os

path = '/home/YOUR_USERNAME/rtb_planner'
if path not in sys.path:
    sys.path.insert(0, path)

from backend.main import app as application
```

### Reload Web App

1. Go to "Web" tab
2. Click "Reload YOUR_USERNAME.pythonanywhere.com"
3. Wait 30-45 seconds
4. Verify status: "Last reload: just now" ✓

---

## 4. CLOUDFLARE SETUP & CONFIGURATION

### Step 1: Add Domain to Cloudflare

1. Go to: https://dash.cloudflare.com/
2. Click "Add a site"
3. Enter your domain name
4. Select "Free" plan
5. Update nameservers at your domain registrar

### Step 2: Cloudflare DNS Settings

In Cloudflare Dashboard → DNS:

**Add these records:**

| Type | Name | Content | TTL | Proxy |
|------|------|---------|-----|-------|
| CNAME | @ | your-pythonanywhere-domain.pythonanywhere.com | Auto | 🟠 Proxied |
| CNAME | www | your-pythonanywhere-domain.pythonanywhere.com | Auto | 🟠 Proxied |

### Step 3: SSL/TLS Configuration

1. Go to: SSL/TLS → Overview
2. Encryption mode: **Full (strict)**
3. Minimum TLS Version: **1.2**
4. Always use HTTPS: **ON**

### Step 4: Caching & Performance

1. Go to: Caching → Configuration
   - Caching Level: **Standard**
   - Browser cache TTL: **4 hours**

2. Go to: Speed → Optimization
   - Auto Minify: ✓ JavaScript, CSS, HTML
   - Rocket Loader: **ON**
   - Mirage: **ON**

### Step 5: Page Rules (if needed)

1. Go to: Rules → Page Rules
2. Add new rule:
   - URL: `yoursite.com/api/*`
   - Set Cache Level: **Bypass**
   - (API calls should not be cached)

### Step 6: Update Backend CORS

**Edit** `backend/main.py` lines 27-39:

Replace with your Cloudflare domain:

```python
CORS(app, 
     origins=[
        "https://your-domain.com",
        "https://www.your-domain.com",
        "https://yourdomain.cloudflare.com",
        "http://localhost:5173",
        "http://localhost:8000"
     ],
     methods=["GET", "POST", "OPTIONS", "PUT"],
     allow_headers=["Content-Type", "Authorization"],
     supports_credentials=False)
```

---

## 5. COMPLETE DEPLOYMENT CHECKLIST

### GitHub ✓
- [ ] Repository created
- [ ] `.gitignore` file added
- [ ] Files pushed to `main` branch
- [ ] README.md created
- [ ] Repository is public/accessible

### PythonAnywhere ✓
- [ ] Backend files uploaded
- [ ] Frontend files uploaded
- [ ] RTB Templates folder created with `.docx` files
- [ ] `requirements.txt` updated with all dependencies
- [ ] WSGI file configured
- [ ] Web app reloaded successfully
- [ ] Test API endpoints working

### Cloudflare ✓
- [ ] Domain added to Cloudflare
- [ ] DNS records configured (CNAME)
- [ ] SSL/TLS: Full (strict) enabled
- [ ] Auto HTTPS redirect: ON
- [ ] Caching configured
- [ ] CORS updated in code

---

## 6. TESTING & VERIFICATION

### Test 1: Check if Live
```
https://your-domain.com/
Should show: API features list
```

### Test 2: Generate Session Plan
```
POST https://your-domain.com/api/session-plans/generate
Body: { sector, trade, trainer_name, ... }
Should return: Document download link
```

### Test 3: Download DOCX
```
https://your-domain.com/session-plans/1/download?phone=+250789751595
Should download: .docx file
```

### Test 4: Download PDF
```
https://your-domain.com/session-plans/1/download-pdf?phone=+250789751595
Should download: .pdf file
```

### Test 5: Check SSL
```
https://your-domain.com/
Check browser: Lock icon should show "Secure" + Cloudflare badge
```

---

## 7. FINAL STEPS

### After Deployment
1. **Monitor logs** on PythonAnywhere for 24 hours
2. **Test with real data** - generate a few session plans
3. **Share URL** with teachers
4. **Collect feedback** on document quality
5. **Keep GitHub updated** - push any fixes

### Future Updates

When you make changes:
```bash
# Local changes
git add .
git commit -m "Fix: template generator cell indices"
git push origin main

# On PythonAnywhere:
# Option 1: Pull from GitHub
git pull origin main

# Option 2: Re-upload changed files

# Option 3: Reload web app (if caching issue)
```

---

## 8. TROUBLESHOOTING

| Issue | Solution |
|-------|----------|
| **504 Gateway Timeout** | Increase timeout in Cloudflare or restart PythonAnywhere |
| **SSL Certificate Error** | Wait 24-48 hours for DNS propagation |
| **404 on endpoints** | Verify WSGI configuration, reload web app |
| **Template not found** | Check RTB Templates folder exists in PythonAnywhere |
| **PDF download fails** | Ensure docx2pdf in requirements.txt, wait 2 min after reload |
| **CORS errors** | Update CORS origins in main.py with your domain |

---

## 9. DEPLOYMENT SUMMARY

| Platform | Files | Time | Status |
|----------|-------|------|--------|
| **GitHub** | All code | 5 min | Push code + docs |
| **PythonAnywhere** | Backend + Frontend + Templates | 15 min | Upload files |
| **Cloudflare** | DNS config | 10 min | Configure domain |
| **Testing** | API endpoints | 5 min | Verify working |
| **TOTAL** | - | **35 min** | **✅ LIVE** |

---

## 10. FILES CHECKLIST

### Must Upload to PythonAnywhere
```
✓ backend/main.py
✓ backend/document_generator.py
✓ backend/rtb_template_generator.py (UPDATED)
✓ backend/ai_content_generator.py
✓ backend/facilitation_content_generator.py
✓ backend/smart_content_generator.py
✓ backend/content_formatter.py
✓ backend/init_db.py
✓ backend/requirements.txt
✓ frontend/ (all HTML/JS/CSS)
✓ RTB Templates/RTB Session plan template.docx
✓ RTB Templates/Scheme of work.docx
```

### Must Push to GitHub
```
✓ Same files as above (except test files)
✓ .gitignore
✓ README.md
```

### Do NOT Upload/Push
```
✗ test_*.py files
✗ TEST_*.docx files
✗ __pycache__/
✗ .env
✗ *.pyc
```

---

**Status**: READY FOR DEPLOYMENT ✅
