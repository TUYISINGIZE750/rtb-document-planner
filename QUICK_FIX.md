# 🚨 Connection Failed? Quick Fix Guide

## The 3 Issues Found

Your Vercel → PythonAnywhere connection is failing because:

### ❌ Issue 1: WSGI Configuration Missing (CRITICAL)
- **Problem**: PythonAnywhere uses WSGI by default, but FastAPI needs ASGI
- **Fix**: Use the `pythonanywhere_wsgi.py` file we created

### ❌ Issue 2: Config Not Updated
- **Problem**: Frontend hardcodes backend URL but doesn't verify it's running
- **Fix**: Updated `config.js` with better logging

### ❌ Issue 3: No Diagnostic Tool
- **Problem**: Hard to debug when connection fails
- **Fix**: Created `vercel-debug.html` for testing

---

## 🔧 Step-by-Step Fix (5 minutes)

### Step 1: PythonAnywhere WSGI Setup
1. Login to PythonAnywhere → **Web** tab
2. Click your web app (`leonardus437.pythonanywhere.com`)
3. Under **"Code"**, find **WSGI configuration file**
4. Set it to: `/home/leonardus437/rtb-document-planner/pythonanywhere_wsgi.py`
5. Click **Save**

### Step 2: Install Dependencies
On PythonAnywhere console:
```bash
workon rtb-planner
pip install -r /home/leonardus437/rtb-document-planner/backend/requirements.txt
python /home/leonardus437/rtb-document-planner/backend/init_db.py
```

### Step 3: Restart Backend
In PythonAnywhere Web tab → Click **"Reload leonardus437.pythonanywhere.com"**

### Step 4: Test Backend
Visit: `https://leonardus437.pythonanywhere.com/`

Should show:
```json
{"message": "RTB Document Planner API", "status": "online", "cors": "enabled"}
```

### Step 5: Deploy Frontend
```bash
vercel --prod
```
Or push to GitHub (if connected).

### Step 6: Test Full Connection
1. Open your Vercel domain in browser
2. Press `F12` to open Developer Console
3. Look for: `✅ API connection successful`
4. Try to login

---

## 🧪 Quick Diagnosis

### Use the Debug Tool
Open in browser: `https://your-vercel-domain.com/vercel-debug.html`

This will:
- ✅ Check frontend setup
- ✅ Test backend connection
- ✅ Verify CORS headers
- ✅ Check API health
- ✅ Show common issues

---

## 📋 Checklist

Before you say "Still not working":

- [ ] PythonAnywhere WSGI file updated
- [ ] Web app restarted (green icon visible)
- [ ] Backend responds to `https://leonardus437.pythonanywhere.com/`
- [ ] Dependencies installed on PythonAnywhere
- [ ] Database initialized (`init_db.py` run)
- [ ] Frontend redeployed to Vercel
- [ ] Browser console shows connection successful
- [ ] No CORS errors in Network tab

---

## 🆘 Still Failing?

### 1. Check Backend Directly
```bash
curl -I https://leonardus437.pythonanywhere.com/
```
Should return: `HTTP/1.1 200 OK`

### 2. Check PythonAnywhere Logs
- Dashboard → Web → Error log
- Look for import/syntax errors

### 3. Check Browser Console
- F12 → Console tab
- Look for specific error messages
- Check Network tab for failed requests

### 4. Use Debug Tool
- Open `vercel-debug.html`
- Run all tests
- Share results

---

## 📞 Common Errors & Fixes

| Error | Fix |
|-------|-----|
| **502 Bad Gateway** | Restart web app, check error log |
| **Connection Refused** | Verify domain URL, check web app is running |
| **CORS Error** | Add Vercel domain to backend `allow_origins` |
| **Module Not Found** | Install dependencies: `pip install -r requirements.txt` |
| **Database Error** | Run: `python backend/init_db.py` |
| **Connection Timeout** | Check PythonAnywhere CPU/memory usage |

---

## 📁 Files Modified

✅ **Created**:
- `pythonanywhere_wsgi.py` - WSGI configuration
- `VERCEL_PYTHONANYWHERE_SETUP.md` - Full setup guide
- `vercel-debug.html` - Debug & test tool
- `QUICK_FIX.md` - This file

✅ **Updated**:
- `frontend/config.js` - Better logging & documentation
- `frontend/connection-fix.js` - Enhanced debugging

---

## 🎯 Expected Result

After following these steps:
1. ✅ Backend runs on PythonAnywhere
2. ✅ Frontend deployed on Vercel
3. ✅ Frontend can reach backend
4. ✅ Users can login and create documents
5. ✅ Documents download correctly

---

## 📞 Need Help?

1. Check browser console (F12)
2. Run `vercel-debug.html`
3. Check PythonAnywhere error log
4. Verify all URLs match exactly (including https://)
5. Ensure no typos in domain names

Good luck! 🚀