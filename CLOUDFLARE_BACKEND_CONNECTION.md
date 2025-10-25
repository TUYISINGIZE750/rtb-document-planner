# Cloudflare ↔ PythonAnywhere Connection Guide

## ✅ What's Been Done

### 1. Frontend (Cloudflare Pages)
- Deployed at: `https://rtb-document-planner.pages.dev`
- Config points to: `https://leonardus437.pythonanywhere.com`

### 2. Backend (PythonAnywhere)
- CORS updated to allow Cloudflare Pages domains
- Accepts requests from: `*.pages.dev`

### 3. Files Updated
- `PRODUCTION_READY/backend/main.py` - Added Cloudflare to CORS
- Pushed to GitHub (commit 6781e40)

---

## 🔧 PythonAnywhere Setup Required

### Upload Updated Backend File
1. Go to PythonAnywhere **Files** tab
2. Navigate to your project folder
3. Upload: `PRODUCTION_READY/backend/main.py`
4. Replace existing file

### Reload Web App
1. Go to **Web** tab
2. Click **Reload leonardus437.pythonanywhere.com**
3. Wait for green checkmark

---

## 🧪 Test Connection

### 1. Open Your Cloudflare Site
Visit: `https://rtb-document-planner.pages.dev`

### 2. Open Browser Console (F12)
Look for these messages:
```
✅ config.js loaded
🌐 API Base URL: https://leonardus437.pythonanywhere.com
✅ API connection successful
```

### 3. Test Login
- Click "Login"
- Use admin credentials:
  - Phone: `+250789751597`
  - Password: `admin123`
- Should login successfully

### 4. Test Document Generation
- Login as teacher
- Create a session plan
- Should generate and download DOCX file

---

## 🔍 Troubleshooting

### Issue: CORS Error
**Symptom**: Console shows "blocked by CORS policy"

**Solution**:
1. Verify `main.py` uploaded to PythonAnywhere
2. Reload web app
3. Check error log in PythonAnywhere

### Issue: API Connection Failed
**Symptom**: "❌ API connection failed" in console

**Solution**:
1. Check PythonAnywhere is running: https://leonardus437.pythonanywhere.com/
2. Should return: `{"status": "online"}`
3. If not, reload web app

### Issue: Login Fails
**Symptom**: "Unable to connect to server"

**Solution**:
1. Check `config.js` has correct API_BASE
2. Verify CORS is configured
3. Check PythonAnywhere error log

---

## 📋 Quick Checklist

- [ ] Upload `main.py` to PythonAnywhere
- [ ] Reload PythonAnywhere web app
- [ ] Visit Cloudflare site
- [ ] Check console for API connection
- [ ] Test login with admin account
- [ ] Test document generation

---

## 🎯 Expected Behavior

### Working Connection:
1. Cloudflare frontend loads
2. Console shows "✅ API connection successful"
3. Login works
4. Document generation works
5. Downloads work

### Connection Flow:
```
User Browser
    ↓
Cloudflare Pages (Frontend)
    ↓ API Calls
PythonAnywhere (Backend)
    ↓ Response
Cloudflare Pages
    ↓ Display
User Browser
```

---

## 🚀 You're All Set!

Once you upload `main.py` and reload PythonAnywhere, your Cloudflare frontend will be fully connected to your backend.

**Cloudflare URL**: https://rtb-document-planner.pages.dev
**Backend API**: https://leonardus437.pythonanywhere.com
