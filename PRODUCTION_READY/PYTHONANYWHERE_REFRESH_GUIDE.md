# 🔄 PythonAnywhere Database Refresh Guide

## Quick Refresh (Keep Users)

### Method 1: Automatic Migration
```bash
# Your database will auto-update
# No action needed - just reload web app
```

### Method 2: Manual Refresh
```bash
# Login to PythonAnywhere
# Open Bash console

cd /home/leonardus437
python
```

```python
from main import Base, engine
Base.metadata.create_all(bind=engine)
exit()
```

---

## Full Reset (Clean Database)

### Step 1: Backup Current Database (Optional)
```bash
cd /home/leonardus437
cp rtb_planner.db rtb_planner_backup_$(date +%Y%m%d).db
```

### Step 2: Delete Old Database
```bash
rm rtb_planner.db
```

### Step 3: Create New Database
```bash
python init_db.py
```

### Step 4: Reload Web App
1. Go to **Web** tab
2. Click **Reload leonardus437.pythonanywhere.com**

---

## Upload New Files to PythonAnywhere

### Via Web Interface:
1. Go to https://www.pythonanywhere.com
2. Click **Files** tab
3. Navigate to your project folder
4. Click **Upload a file**
5. Select files:
   - `rtb_template_filler_exact.py`
   - `facilitation_content_generator.py`
   - `content_formatter.py`
   - `document_generator.py`
6. Click **Upload**

### Via Git (Recommended):
```bash
# In PythonAnywhere Bash console:
cd /home/leonardus437/your-project-folder

# Pull latest changes
git pull origin main

# Reload web app
```

---

## Verify Everything Works

### Test 1: API Health Check
```bash
curl https://leonardus437.pythonanywhere.com/
```

Expected response:
```json
{
  "message": "RTB Document Planner API",
  "status": "online"
}
```

### Test 2: Database Check
```bash
python
```

```python
from main import SessionLocal, User
db = SessionLocal()
users = db.query(User).count()
print(f"Total users: {users}")
db.close()
exit()
```

### Test 3: Generate Document
Use frontend or curl:
```bash
curl -X POST https://leonardus437.pythonanywhere.com/session-plans/generate \
  -H "Content-Type: application/json" \
  -d '{"user_phone":"+250789751597","sector":"ICT","topic_of_session":"Test"}'
```

---

## Common Issues & Solutions

### Issue 1: "Module not found"
```bash
# Install missing packages
pip install --user python-docx
pip install --user flask-cors
```

### Issue 2: "Database locked"
```bash
# Stop all processes using database
pkill python
# Then recreate database
python init_db.py
```

### Issue 3: "Permission denied"
```bash
# Fix file permissions
chmod 644 *.py
chmod 755 .
```

### Issue 4: "Import error"
```bash
# Check file names match exactly
ls -la *.py
# Ensure no typos in imports
```

---

## File Checklist

Make sure these files exist in your PythonAnywhere folder:

```
/home/leonardus437/your-project/
├── main.py ✅
├── document_generator.py ✅
├── rtb_template_filler_exact.py ✅ NEW
├── facilitation_content_generator.py ✅ NEW
├── content_formatter.py ✅ NEW
├── rtb_session_plan_template.docx ✅
├── rtb_scheme_template.docx ✅
├── init_db.py ✅
└── requirements.txt ✅
```

---

## After Deployment

### 1. Test All Features:
- [ ] User registration
- [ ] User login
- [ ] Session plan generation
- [ ] Scheme generation
- [ ] Document download
- [ ] Different facilitation techniques

### 2. Monitor Logs:
```bash
# Check error log
tail -f /var/log/leonardus437.pythonanywhere.com.error.log

# Check access log
tail -f /var/log/leonardus437.pythonanywhere.com.access.log
```

### 3. Performance Check:
- Response time < 3 seconds
- No memory errors
- No timeout errors

---

## Rollback (If Needed)

### If new version has issues:
```bash
# Restore backup database
cd /home/leonardus437
cp rtb_planner_backup_YYYYMMDD.db rtb_planner.db

# Revert code changes
git checkout previous-commit-hash

# Reload web app
```

---

## Success Checklist

After refresh, verify:
- [ ] API responds with status "online"
- [ ] Database has admin user
- [ ] Can register new users
- [ ] Can login
- [ ] Can generate session plans
- [ ] Can generate schemes
- [ ] Documents download correctly
- [ ] Formatting is correct
- [ ] All facilitation techniques work

✅ **ALL CHECKS PASSED = DEPLOYMENT SUCCESSFUL!**
