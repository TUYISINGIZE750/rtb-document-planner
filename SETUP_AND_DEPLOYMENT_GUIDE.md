# RTB Document Planner - Complete Setup & Deployment Guide

## System Overview

**RTB Document Planner** is a professional TVET (Technical and Vocational Education and Training) document generation system. It enables educators to create RTB-compliant:
- Session Plans
- Schemes of Work
- Professional DOCX/PDF exports

**Tech Stack:**
- **Backend**: Flask 3.0.0 + SQLAlchemy 2.0.23 + SQLite/PostgreSQL
- **Frontend**: HTML5 + JavaScript (Vanilla)
- **Documents**: python-docx 1.1.0 with RTB template integration
- **Deployment**: Local, PythonAnywhere, Docker, or Vercel

---

## Part 1: Local Development Setup

### Windows Setup (Recommended for Local Testing)

#### Step 1: Install Python 3.11+
```bash
# Download from https://www.python.org/downloads/
# During installation, CHECK: "Add Python to PATH"
python --version  # Should be 3.11+
```

#### Step 2: Navigate to Project Directory
```bash
cd "c:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY"
```

#### Step 3: Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

#### Step 4: Install Backend Dependencies
```bash
cd backend
pip install --upgrade pip
pip install -r requirements.txt
```

#### Step 5: Initialize Database
```bash
python init_db.py
```

#### Step 6: Start Backend Server
```bash
python main.py
```
**Expected Output:**
```
 * Running on http://127.0.0.1:8000
```

#### Step 7: Start Frontend (New Terminal)
```bash
cd "..\frontend"
python -m http.server 5173
```
**Expected Output:**
```
Serving HTTP on 0.0.0.0 port 5173
```

#### Step 8: Access Application
- **Frontend**: http://localhost:5173
- **API Docs**: http://localhost:8000/docs
- **Health Check**: http://localhost:8000/health

---

## Part 2: Admin & User Credentials

### Default Admin Account
```
Phone: +250789751597
Password: admin123
Role: Admin
```

### Test Teacher Account (Create via Frontend)
1. Click "Register" on login page
2. Enter:
   - **Name**: Test Teacher
   - **Phone**: +250788123456
   - **Email**: teacher@rtb.rw
   - **Institution**: Test School
   - **Password**: password123
3. Login and test document generation

---

## Part 3: Document Generation Features

### Session Plan Generation
**Input Fields:**
- Module Code/Title
- Topic of Session
- Duration (minutes)
- Learning Outcomes
- Indicative Contents
- Facilitation Techniques (dropdown):
  - Trainer-guided instruction
  - Simulation/Role-play
  - Group work/Collaborative learning
  - Hands-on/Practical exercises
  - Discussion/Brainstorming
  - Project-based learning

**Output Format:** 
- Professional DOCX with RTB template structure
- Book Antiqua font, 12pt, 1.5 line spacing
- Automatic content generation based on facilitation technique
- Bibliography with APA-formatted references

### Scheme of Work Generation
**Input Fields (per Term):**
- Weeks
- Learning Outcomes
- Indicative Contents
- Duration
- Learning Place

**Output Format:**
- Multi-table DOCX with Term 1, 2, 3 sections
- Professional formatting matching RTB standards

---

## Part 4: API Endpoints Reference

### Authentication
```
POST /users/register
POST /users/login
GET /users/{phone}/profile
```

### Document Operations
```
POST /session-plans                    # Create session plan
GET /session-plans/<id>/download      # Download DOCX
POST /schemes                          # Create scheme of work
GET /schemes/<id>/download            # Download scheme DOCX
```

### Admin Operations
```
GET /admin/stats                       # User statistics
POST /notifications/broadcast          # Send bulk notifications
POST /notifications/send               # Send personal message
PUT /users/{phone}/status             # Activate/deactivate user
PUT /users/{phone}/premium            # Grant/revoke premium
```

### Notifications
```
GET /users/{phone}/notifications      # Get user notifications
```

---

## Part 5: Database Configuration

### SQLite (Default - Development)
No additional setup needed. Database file:
```
PRODUCTION_READY/backend/rtb_planner.db
```

### PostgreSQL (Production)
1. Install PostgreSQL 12+
2. Create database:
```sql
CREATE DATABASE rtb_planner;
CREATE USER rtb_user WITH PASSWORD 'secure_password';
ALTER ROLE rtb_user SET client_encoding TO 'utf8';
ALTER ROLE rtb_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE rtb_user SET default_transaction_deferrable TO on;
ALTER ROLE rtb_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE rtb_planner TO rtb_user;
```

3. Update `main.py` database URL:
```python
DATABASE_URL = "postgresql://rtb_user:secure_password@localhost:5432/rtb_planner"
```

---

## Part 6: Deployment Options

### Option A: PythonAnywhere

1. **Sign up** at https://www.pythonanywhere.com
2. **Upload files** via Web tab:
   - Upload `PRODUCTION_READY/backend/main.py`
   - Upload RTB templates (*.docx files)
   - Upload all Python helper files
3. **Create Web App**:
   - Select "Flask"
   - Python 3.11
   - WSGI file location: `/var/www/yourusername_pythonanywhere_com_wsgi.py`

4. **Install requirements** via Bash console:
```bash
pip install -r requirements.txt
```

5. **Reload Web App** in Web tab

6. **Update CORS origins** in `main.py`:
```python
CORS(app, 
     origins=[
         "https://yourdomain.pythonanywhere.com",
         "https://your-frontend-domain.com"
     ])
```

### Option B: Docker (Local/Production)

1. **Build image**:
```bash
docker build -t rtb-planner .
```

2. **Run container**:
```bash
docker run -p 8000:8000 \
  -e DATABASE_URL="sqlite:///rtb_planner.db" \
  rtb-planner
```

3. **Docker Compose** (with PostgreSQL):
```bash
docker-compose up --build
```

### Option C: Vercel + Backend Separation

1. **Deploy Frontend to Vercel**:
```bash
cd frontend
vercel deploy
```

2. **Deploy Backend** to PythonAnywhere or Heroku

3. **Update API endpoint** in `frontend/config.js`:
```javascript
const API_BASE_URL = "https://your-backend-domain.com";
```

### Option D: Heroku

1. Create `runtime.txt`:
```
python-3.11.0
```

2. Create `Procfile`:
```
web: gunicorn -w 4 -b 0.0.0.0:$PORT main:app
```

3. **Deploy**:
```bash
heroku create rtb-planner
git push heroku main
heroku config:set DATABASE_URL="postgresql://..."
```

---

## Part 7: Testing & Verification

### Test Backend Connection
```bash
curl http://localhost:8000/health
```

### Test Session Plan Creation
```bash
python test_complete_system.py
```

### Manual API Test
```bash
# Register user
curl -X POST http://localhost:8000/users/register \
  -H "Content-Type: application/json" \
  -d '{"phone":"+250788123456","password":"test123","name":"Test User"}'

# Login
curl -X POST http://localhost:8000/users/login \
  -H "Content-Type: application/json" \
  -d '{"phone":"+250788123456","password":"test123"}'

# Create session plan
curl -X POST http://localhost:8000/session-plans \
  -H "Content-Type: application/json" \
  -d '{
    "user_phone":"+250788123456",
    "sector":"ICT and Multimedia",
    "trade":"Computer system and architecture",
    "topic_of_session":"Use of Do while loops in C program",
    "duration":"40",
    "learning_outcomes":"Write a c program using do and while loop in C",
    "indicative_contents":"Do while loop and while loop",
    "facilitation_techniques":"Simulation"
  }'
```

---

## Part 8: Frontend Configuration

### Update API Base URL
**File**: `PRODUCTION_READY/frontend/config.js`
```javascript
const API_BASE_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";
const API_TIMEOUT = 30000;
```

### Required Frontend Files
- ✅ index.html (landing page)
- ✅ login.html (authentication)
- ✅ register.html (user registration)
- ✅ wizard.html (session plan creator)
- ✅ scheme-wizard.html (scheme of work creator)
- ✅ teacher-dashboard.html (user dashboard)
- ✅ admin.html (admin panel)
- ✅ auth.js (authentication helper)
- ✅ config.js (API configuration)

---

## Part 9: Production Checklist

- [ ] Database backed up
- [ ] CORS origins configured correctly
- [ ] Admin credentials changed from default
- [ ] SSL/HTTPS enabled
- [ ] Environment variables set:
  - DATABASE_URL (if PostgreSQL)
  - SECRET_KEY (for sessions)
  - ALLOWED_ORIGINS (CORS)
- [ ] API rate limiting configured
- [ ] Error logging enabled
- [ ] Template files (*.docx) uploaded
- [ ] All Python dependencies installed
- [ ] Frontend API URL points to production backend
- [ ] Email notifications tested (if configured)
- [ ] Backup strategy implemented

---

## Part 10: Troubleshooting

### Backend Won't Start
```bash
# Check Python version
python --version  # Must be 3.11+

# Check dependencies
pip list | grep -E "flask|sqlalchemy|python-docx"

# Check port availability
netstat -ano | findstr :8000  # Windows
lsof -i :8000  # Mac/Linux
```

### Documents Not Generating
1. Verify template files exist:
   - `rtb_session_plan_template.docx`
   - `rtb_scheme_template.docx`
2. Check file permissions
3. Review backend logs for errors

### CORS Errors
Update `main.py` CORS origins to match frontend domain:
```python
CORS(app, 
     origins=[
         "http://localhost:5173",
         "https://your-frontend-domain.com"
     ])
```

### Database Connection Issues
```bash
# Test SQLite
python -c "import sqlite3; sqlite3.connect('rtb_planner.db')"

# Test PostgreSQL
psql -h localhost -U rtb_user -d rtb_planner
```

---

## Part 11: File Structure

```
PRODUCTION_READY/
├── backend/
│   ├── main.py                          # FastAPI backend
│   ├── document_generator.py            # DOCX generation
│   ├── rtb_template_filler_exact.py    # Template filler
│   ├── facilitation_content_generator.py
│   ├── content_formatter.py
│   ├── ai_content_generator.py
│   ├── rtb_session_plan_template.docx  # RTB template
│   ├── rtb_scheme_template.docx        # RTB template
│   ├── requirements.txt                 # Dependencies
│   ├── init_db.py                       # Database init
│   └── rtb_planner.db                  # SQLite database
├── frontend/
│   ├── index.html                      # Landing page
│   ├── login.html                      # Login form
│   ├── register.html                   # Registration
│   ├── wizard.html                     # Session plan wizard
│   ├── scheme-wizard.html             # Scheme wizard
│   ├── teacher-dashboard.html         # Dashboard
│   ├── admin.html                     # Admin panel
│   ├── auth.js                        # Auth utilities
│   ├── config.js                      # API config
│   ├── admin-final.html               # Admin dashboard
│   └── *.css / *.js                   # Styling & helpers
└── SETUP_AND_DEPLOYMENT_GUIDE.md      # This file
```

---

## Part 12: Quick Start Commands

### Windows Quick Start
```bash
# Terminal 1 - Backend
cd "c:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\backend"
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python init_db.py
python main.py

# Terminal 2 - Frontend
cd "c:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\frontend"
python -m http.server 5173
```

### Mac/Linux Quick Start
```bash
# Terminal 1 - Backend
cd "~/path/to/PRODUCTION_READY/backend"
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python init_db.py
python main.py

# Terminal 2 - Frontend
cd "~/path/to/PRODUCTION_READY/frontend"
python -m http.server 5173
```

---

## Part 13: Support & Resources

### Documentation Files
- `COMPLETE_DEPLOYMENT_GUIDE.md` - Advanced deployment
- `DOCUMENT_FORMATTING_IMPROVEMENTS.md` - Formatting details
- `LOGIN_SYSTEM_GUIDE.md` - Authentication details
- `NOTIFICATION_SYSTEM_GUIDE.md` - Notifications setup

### Key Contact Points
- **Admin Phone**: +250789751597
- **Test User**: Create via registration form
- **API Health**: GET `/health`

---

**Last Updated**: October 25, 2025  
**Version**: 3.0  
**Status**: Production Ready ✅
