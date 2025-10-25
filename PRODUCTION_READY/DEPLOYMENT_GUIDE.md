# 🚀 DEPLOYMENT GUIDE

## Files Ready for Deployment

### Backend Files (PythonAnywhere):
```
PRODUCTION_READY/backend/
├── main.py
├── document_generator.py
├── rtb_template_filler_exact.py ✅ NEW
├── facilitation_content_generator.py ✅ NEW
├── content_formatter.py ✅ NEW
├── rtb_session_plan_template.docx
├── rtb_scheme_template.docx
└── requirements.txt
```

---

## Step 1: Deploy Backend to PythonAnywhere

### A. Upload Files:
1. Go to: https://www.pythonanywhere.com
2. Login to your account (leonardus437)
3. Go to **Files** tab
4. Navigate to your project folder
5. Upload these files:
   - `rtb_template_filler_exact.py`
   - `facilitation_content_generator.py`
   - `content_formatter.py`
   - `document_generator.py` (updated)

### B. Refresh Database:
```bash
# In PythonAnywhere Bash console:
cd /home/leonardus437/your-project-folder
python init_db.py
```

### C. Reload Web App:
1. Go to **Web** tab
2. Click **Reload leonardus437.pythonanywhere.com**
3. Wait for green checkmark

---

## Step 2: Deploy Frontend to GitHub Pages

### A. Update Frontend Files:
Your frontend is already deployed at:
- https://tuyisingize750.github.io/rtb-document-planner

### B. If you need to update:
```bash
cd "c:\Users\PC\Music\Scheme of work and session plan planner"

# Add all changes
git add .

# Commit
git commit -m "Updated with formatting fixes and facilitation techniques"

# Push to GitHub
git push origin main
```

### C. GitHub Pages will auto-deploy in 1-2 minutes

---

## Step 3: Verify Deployment

### Test Backend:
```bash
# Test API endpoint
curl https://leonardus437.pythonanywhere.com/

# Should return:
{
  "message": "RTB Document Planner API",
  "status": "online",
  "version": "2.0"
}
```

### Test Frontend:
1. Open: https://tuyisingize750.github.io/rtb-document-planner
2. Try generating a session plan
3. Check if document downloads correctly

---

## Step 4: Database Refresh (If Needed)

### Option 1: Reset Database (Clean Start):
```bash
# In PythonAnywhere Bash:
cd /home/leonardus437
rm rtb_planner.db
python init_db.py
```

### Option 2: Keep Existing Data:
```bash
# Database will auto-update with new schema
# No action needed
```

---

## API Endpoint

Your backend is at:
```
https://leonardus437.pythonanywhere.com
```

Endpoints:
- `POST /session-plans/generate` - Generate session plan
- `POST /schemes/generate` - Generate scheme of work
- `GET /session-plans/<id>/download` - Download session plan
- `GET /schemes-of-work/<id>/download` - Download scheme
- `POST /users/register` - Register user
- `POST /users/login` - Login user

---

## Frontend Configuration

Make sure frontend points to correct API:
```javascript
const API_BASE = 'https://leonardus437.pythonanywhere.com';
```

---

## Troubleshooting

### If Backend Not Working:
1. Check PythonAnywhere error log
2. Go to **Web** tab → **Error log**
3. Look for Python errors
4. Fix and reload

### If Frontend Not Working:
1. Check browser console (F12)
2. Look for CORS errors
3. Verify API_BASE URL is correct
4. Check network tab for failed requests

### If Database Issues:
```bash
# Recreate database
cd /home/leonardus437
rm rtb_planner.db
python init_db.py
```

---

## Quick Deployment Checklist

- [ ] Upload new Python files to PythonAnywhere
- [ ] Reload PythonAnywhere web app
- [ ] Test API endpoint
- [ ] Push changes to GitHub (if frontend updated)
- [ ] Wait for GitHub Pages deployment
- [ ] Test full workflow (register → login → generate)
- [ ] Verify document downloads correctly
- [ ] Check formatting in downloaded documents

---

## What's New in This Version

### ✅ Features:
1. **Facilitation Technique Support**
   - Trainer-guided
   - Simulation
   - Group work
   - Hands-on practice
   - Discussion
   - Project-based

2. **Dynamic Content Generation**
   - Content changes based on technique
   - Teacher input fully utilized
   - Custom activities supported

3. **Improved Formatting**
   - Clean spacing
   - Proper bullet points
   - Auto-numbered objectives
   - Organized resources

4. **Template Compliance**
   - 100% RTB format match
   - Preserves fonts and colors
   - Maintains cell merging

---

## Support

If deployment issues occur:
1. Check error logs
2. Verify file uploads
3. Test API endpoints
4. Check CORS settings
5. Reload web app

---

## Success Indicators

✅ API returns status "online"
✅ Frontend loads without errors
✅ Users can register/login
✅ Session plans generate successfully
✅ Documents download correctly
✅ Formatting looks professional
✅ All facilitation techniques work

🎉 **READY FOR PRODUCTION USE!**
