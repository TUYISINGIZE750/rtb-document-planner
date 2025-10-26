# Quick Deployment Reference

## 🚀 One-Minute Local Setup

### Windows
```bash
cd PRODUCTION_READY
START_SYSTEM.bat
# Done! Access http://localhost:5173
```

### Mac/Linux
```bash
cd PRODUCTION_READY/backend
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python init_db.py
python main.py &

cd ../frontend
python -m http.server 5173
# Done! Access http://localhost:5173
```

---

## 🔧 Deployment to PythonAnywhere

### Step 1: Upload Backend Files
1. Login to https://www.pythonanywhere.com
2. Go to **Files** tab
3. Create directory: `/home/username/rtb_backend`
4. Upload these files:
   - `main.py`
   - `document_generator.py`
   - `rtb_template_filler_exact.py`
   - `facilitation_content_generator.py`
   - `content_formatter.py`
   - `ai_content_generator.py`
   - `requirements.txt`
   - `rtb_session_plan_template.docx`
   - `rtb_scheme_template.docx`

### Step 2: Create Web App
1. Go to **Web** tab
2. Click **Add new web app**
3. Choose **Manual configuration** → **Python 3.11**
4. Set **Source code**: `/home/username/rtb_backend`
5. Set **WSGI file**: `/home/username/rtb_backend/pythonanywhere_wsgi.py`

### Step 3: Create WSGI File
Create `/home/username/rtb_backend/pythonanywhere_wsgi.py`:
```python
import sys
import os

path = '/home/username/rtb_backend'
if path not in sys.path:
    sys.path.insert(0, path)

os.chdir(path)

from main import app as application
```

### Step 4: Install Dependencies
In **Bash console**:
```bash
cd /home/username/rtb_backend
pip install -r requirements.txt
```

### Step 5: Update CORS
Edit `main.py` line with CORS:
```python
CORS(app, origins=[
    "https://username.pythonanywhere.com",
    "https://your-frontend-domain.com"
])
```

### Step 6: Reload Web App
Go to **Web** tab → Click **Reload**

**Your backend is now live at**: `https://username.pythonanywhere.com`

---

## 🌐 Deployment to Vercel (Frontend)

### Step 1: Prepare Files
```bash
cd PRODUCTION_READY/frontend
# Already contains vercel.json and necessary files
```

### Step 2: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 3: Deploy
```bash
vercel --prod
# Follow prompts
# Your frontend is now live at: https://your-project.vercel.app
```

### Step 4: Update API URL
Edit `frontend/config.js`:
```javascript
const API_BASE_URL = "https://username.pythonanywhere.com";
```

---

## 🐳 Docker Deployment

### Build & Run Locally
```bash
docker build -t rtb-planner .
docker run -p 8000:8000 rtb-planner
# Access at http://localhost:8000
```

### Deploy to Docker Hub
```bash
docker tag rtb-planner username/rtb-planner
docker push username/rtb-planner
```

### Deploy to Cloud (AWS ECS, Azure, etc.)
Follow cloud provider's Docker container deployment guide.

---

## ✅ Pre-Deployment Checklist

- [ ] All files in `PRODUCTION_READY/backend/` directory
- [ ] `requirements.txt` has all dependencies
- [ ] RTB template files uploaded:
  - [ ] `rtb_session_plan_template.docx`
  - [ ] `rtb_scheme_template.docx`
- [ ] CORS origins updated in `main.py`
- [ ] Database initialized: `python init_db.py`
- [ ] Admin credentials changed (if using production)
- [ ] API endpoints tested locally
- [ ] Frontend `config.js` points to backend
- [ ] Frontend API base URL configured
- [ ] SSL/HTTPS enabled on backend
- [ ] Environment variables set (if needed)
- [ ] Backup of database created
- [ ] Error logging configured
- [ ] Health check endpoint tested

---

## 🔐 Security Checklist

- [ ] Change default admin password (admin123)
- [ ] Enable HTTPS/SSL on backend
- [ ] Restrict CORS to allowed domains only
- [ ] Use strong database passwords
- [ ] Enable API rate limiting (if applicable)
- [ ] Set up regular database backups
- [ ] Monitor error logs
- [ ] Use environment variables for secrets
- [ ] Validate all user inputs
- [ ] Enable CSRF protection (if applicable)

---

## 📊 Admin Credentials

**Default (CHANGE IN PRODUCTION):**
- Phone: `+250789751597`
- Password: `admin123`

**To Create New Admin Account:**
1. Login with default admin
2. Go to Admin Panel
3. Create new user with admin role

---

## 🧪 Quick Test Commands

### Test Backend
```bash
# Health check
curl http://localhost:8000/health

# Register user
curl -X POST http://localhost:8000/users/register \
  -H "Content-Type: application/json" \
  -d '{"phone":"+250788123456","password":"test","name":"Test"}'

# Login
curl -X POST http://localhost:8000/users/login \
  -H "Content-Type: application/json" \
  -d '{"phone":"+250788123456","password":"test"}'
```

### Test Frontend
- Open http://localhost:5173
- Register new account
- Create session plan
- Download document

---

## 🆘 Troubleshooting

| Issue | Solution |
|-------|----------|
| Port 8000 already in use | `lsof -i :8000` then `kill -9 <PID>` |
| Templates not found | Verify `rtb_*.docx` in backend directory |
| CORS errors | Check API URL in frontend `config.js` |
| Database locked | Delete `rtb_planner.db` and run `init_db.py` |
| Module not found | Run `pip install -r requirements.txt` |
| Documents not generating | Check template file permissions |

---

## 📞 Support Files

All located in `PRODUCTION_READY/` directory:
- `SETUP_AND_DEPLOYMENT_GUIDE.md` - Full setup guide
- `CLAUDE.md` - Development notes
- `README.md` - Project overview

---

**Version**: 3.0  
**Updated**: October 25, 2025  
**Status**: Production Ready ✅
