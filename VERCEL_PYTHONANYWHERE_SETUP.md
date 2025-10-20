# Vercel + PythonAnywhere Integration Guide

## 🔴 Connection Failed? Here's the Fix

Your system has two parts:
- **Frontend**: Hosted on Vercel
- **Backend API**: Running on PythonAnywhere

---

## Part 1: PythonAnywhere Backend Setup ⚙️

### Step 1: Configure WSGI Application
1. Go to **PythonAnywhere Dashboard** → **Web** tab
2. Click on your web app (e.g., `leonardus437.pythonanywhere.com`)
3. Under **"Code"** section, find **WSGI configuration file**
4. Set it to: `/home/leonardus437/rtb-document-planner/pythonanywhere_wsgi.py`
5. **Save** and scroll up

### Step 2: Set Python Version
- Ensure Python version is **3.9 or higher** (3.11 recommended)

### Step 3: Configure Virtual Environment
1. In the **Virtualenv** section, set path to your virtualenv
2. Or create new: `/home/leonardus437/.virtualenvs/rtb-planner`
3. Run in console:
```bash
mkvirtualenv --python=/usr/bin/python3.11 rtb-planner
workon rtb-planner
pip install -r /home/leonardus437/rtb-document-planner/backend/requirements.txt
```

### Step 4: Restart Web App
- Click **"Reload leonardus437.pythonanywhere.com"** button

### Step 5: Test Backend Connection
Visit: `https://leonardus437.pythonanywhere.com/`

You should see:
```json
{
  "message": "RTB Document Planner API",
  "status": "online",
  "cors": "enabled"
}
```

---

## Part 2: Vercel Frontend Configuration 🌐

### Step 1: Update config.js with Your Domain

Edit `frontend/config.js` and update the production API URL:

**Find this line (line 11):**
```javascript
production: 'https://leonardus437.pythonanywhere.com'
```

**Replace with your actual PythonAnywhere domain:**
```javascript
production: 'https://leonardus437.pythonanywhere.com'
```

### Step 2: Deploy to Vercel
```bash
# In your project root
vercel --prod
```

Or if using Git:
1. Push to GitHub/GitLab
2. Vercel auto-deploys on push

### Step 3: Test Frontend Connection
1. Visit your Vercel domain (e.g., `https://rtb-document-planner.vercel.app`)
2. Open **Browser Console** (F12 → Console tab)
3. Look for messages like:
   ```
   ✅ config.js loaded successfully
   ✅ API connection successful
   ```

---

## Part 3: CORS Validation ✔️

The backend has proper CORS configuration. If you still get "connection failed":

### Check 1: Browser Console
Open DevTools (F12) → Network tab → Try a login
Look for requests to `https://leonardus437.pythonanywhere.com/users/login`

### Check 2: CORS Error?
If you see `CORS error` in console, the domains aren't matching.
- Verify PythonAnywhere domain is correct
- Check vercel.json has correct CORS headers

### Check 3: Backend Not Responding?
Test directly: `https://leonardus437.pythonanywhere.com/health`

Should return:
```json
{"status": "healthy", "database": "connected"}
```

---

## Part 4: Common Issues & Solutions 🛠️

### Issue 1: "502 Bad Gateway" on PythonAnywhere
**Solution:**
- Check virtualenv is activated in WSGI file
- Restart web app
- Check error log: Web tab → Error log

### Issue 2: "Connection Refused"
**Solution:**
- Verify backend URL in `config.js` is correct
- Verify PythonAnywhere web app is running (green icon)
- Test: `curl -I https://leonardus437.pythonanywhere.com/`

### Issue 3: CORS Error in Browser Console
**Solution:**
- Verify Vercel domain is in backend CORS allowed_origins
- Add your custom domain if using one
- Edit `backend/main.py` lines 20-29 to add your Vercel domain

### Issue 4: Database Connection Failed
**Solution:**
- On PythonAnywhere, create SQLite database:
  ```bash
  python /home/leonardus437/rtb-document-planner/backend/init_db.py
  ```

---

## Part 5: Custom Domain (Optional) 🌍

If using a custom domain on Vercel:

### Update Frontend
1. In `frontend/config.js`, add your custom domain:
```javascript
const API_CONFIG = {
    development: 'http://localhost:8000',
    production: 'https://leonardus437.pythonanywhere.com'
};
```

### Update Backend CORS
Edit `backend/main.py` and add your domain:
```python
allow_origins=[
    "*",
    "https://your-custom-domain.com",  # Add this
    "https://leonardus437.pythonanywhere.com",
]
```

Then restart PythonAnywhere.

---

## Part 6: Testing the Complete Flow 🧪

1. Open browser console (F12)
2. Navigate to your Vercel domain
3. Check console for "API connection successful" ✅
4. Try logging in with test user (check ADMIN_CREDENTIALS.md)
5. Create a session plan
6. Download it as DOCX

---

## Troubleshooting Checklist ☑️

- [ ] PythonAnywhere WSGI file set to `pythonanywhere_wsgi.py`
- [ ] Virtual environment created and dependencies installed
- [ ] Python version is 3.9+
- [ ] Web app is in "Running" state (green icon)
- [ ] Backend responds to `/` endpoint
- [ ] Backend responds to `/health` endpoint
- [ ] Frontend config.js points to correct backend URL
- [ ] Vercel domain added to backend CORS (if custom domain)
- [ ] Browser console shows "API connection successful"

---

## Quick Commands

### On PythonAnywhere Console:
```bash
# Activate virtualenv
workon rtb-planner

# Install dependencies
pip install -r /home/leonardus437/rtb-document-planner/backend/requirements.txt

# Initialize database
cd /home/leonardus437/rtb-document-planner
python backend/init_db.py

# Test backend
python -c "from backend.main import app; print('✅ Backend imports successfully')"
```

### Check Backend Status:
```bash
curl -I https://leonardus437.pythonanywhere.com/
```

Expected response: `200 OK`

---

## Support

If connection still fails:
1. Check PythonAnywhere error log: Dashboard → Web → Error log
2. Enable debug in `backend/main.py`
3. Check network tab in browser DevTools
4. Verify all domains match exactly (including https://)

**Backend URL must be:** `https://leonardus437.pythonanywhere.com`
