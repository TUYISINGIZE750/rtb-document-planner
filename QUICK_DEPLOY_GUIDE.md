# Quick Deployment Guide - Location Dropdown Fix

## 🚀 Local Testing (Do This First!)

### Step 1: Test Locally
```bash
cd "c:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\frontend"
python -m http.server 5173
```

### Step 2: Open Test Page
Open browser and go to:
- http://localhost:5173/test-locations.html

### Step 3: Verify Tests Pass
✅ All tests should show green checkmarks
✅ Try selecting Province → District → Sector → Cell → Village
✅ Click "Show Selected Values" to verify

### Step 4: Test Real Wizards
- http://localhost:5173/wizard.html (Session Plan)
- http://localhost:5173/scheme-wizard.html (Scheme of Work)

---

## 📤 GitHub Deployment

### Option A: Using Batch File (Windows)
```bash
cd "c:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY"
DEPLOY_LOCATION_FIX.bat
```

### Option B: Manual Git Commands
```bash
cd "c:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY"
git add .
git commit -m "Fix: Implement cascading Rwanda location dropdowns"
git push origin main
```

---

## 🌐 PythonAnywhere Deployment

### Step 1: Login to PythonAnywhere
Go to: https://www.pythonanywhere.com

### Step 2: Open Bash Console
Click: "Consoles" → "Bash"

### Step 3: Pull Latest Changes
```bash
cd /home/yourusername/mysite
git pull origin main
```

### Step 4: Verify Files Uploaded
```bash
ls -la frontend/location-handler.js
ls -la rwanda-locations-json-master/locations.json
```

### Step 5: Reload Web App
1. Go to "Web" tab
2. Click "Reload yourusername.pythonanywhere.com"
3. Wait for green "Reload successful" message

---

## ✅ Production Testing

### Test Checklist:
1. Open your live site: `https://yourusername.pythonanywhere.com`
2. Navigate to Session Plan Wizard
3. Check Province dropdown is populated
4. Select Province → verify Districts appear
5. Select District → verify Sectors appear
6. Select Sector → verify Cells appear
7. Select Cell → verify Villages appear
8. Try creating a session plan with selected locations
9. Repeat for Scheme of Work Wizard

---

## 🔧 Troubleshooting

### Issue: Dropdowns not populating
**Solution:**
```bash
# Check if locations.json is accessible
curl https://yourusername.pythonanywhere.com/rwanda-locations-json-master/locations.json

# If 404, check file path in location-handler.js
```

### Issue: JavaScript errors in console
**Solution:**
1. Open browser DevTools (F12)
2. Check Console tab for errors
3. Verify location-handler.js loaded correctly
4. Clear browser cache (Ctrl+Shift+Delete)

### Issue: Old version still showing
**Solution:**
1. Clear browser cache
2. Hard refresh (Ctrl+F5)
3. Check PythonAnywhere reload was successful
4. Verify git pull completed without errors

---

## 📋 Files Changed

### New Files:
- `frontend/location-handler.js` ← Main cascading dropdown logic
- `frontend/test-locations.html` ← Test page
- `LOCATION_DROPDOWN_FIX.md` ← Documentation
- `DEPLOY_LOCATION_FIX.bat` ← Deployment script
- `QUICK_DEPLOY_GUIDE.md` ← This file

### Modified Files:
- `frontend/wizard.html` ← Updated location fields
- `frontend/scheme-wizard.html` ← Updated location fields

### Existing Files (No Changes):
- `rwanda-locations-json-master/locations.json` ← Data source

---

## 🎯 Success Criteria

✅ Province dropdown shows all Rwanda provinces
✅ Selecting province populates districts
✅ Selecting district populates sectors
✅ Selecting sector populates cells
✅ Selecting cell populates villages
✅ All dropdowns are required fields
✅ Form submission includes correct location data
✅ No JavaScript errors in console
✅ Works on both Session Plan and Scheme wizards

---

## 📞 Support

If issues persist:
1. Check browser console for errors (F12)
2. Verify all files uploaded to PythonAnywhere
3. Test locally first to isolate server issues
4. Check PythonAnywhere error logs
