# 📤 PythonAnywhere Upload Guide

## Visual Step-by-Step Instructions

### Step 1: Go to Files Tab
```
[Dashboard] → Click "Files" tab at the top
```

### Step 2: Navigate to Your Directory
```
You should see: /home/leonardus437/
If not, click "leonardus437" in the breadcrumb
```

### Step 3: Upload Files (One by One)

#### File 1: rtb_professional_generator.py
1. Click "Upload a file" button
2. Select `rtb_professional_generator.py` from UPLOAD_TO_PYTHONANYWHERE folder
3. Click "Upload"
4. Wait for confirmation

#### File 2: main_minimal.py
1. Click "Upload a file" button again
2. Select `main_minimal.py`
3. Click "Upload"
4. Click "Yes" if asked to overwrite

#### File 3: requirements.txt
1. Click "Upload a file" button again
2. Select `requirements.txt`
3. Click "Upload"
4. Click "Yes" if asked to overwrite

### Step 4: Verify Files Are There
You should now see these files in /home/leonardus437/:
- ✅ rtb_professional_generator.py (NEW!)
- ✅ main_minimal.py
- ✅ requirements.txt

---

## Next: Install Dependencies

### Step 5: Open Bash Console
```
[Dashboard] → Click "Consoles" tab
→ Click "Bash" (or "$ Bash" button)
```

### Step 6: Run Installation Command
Copy and paste this EXACT command:
```bash
pip3.10 install --user flask flask-cors python-docx lxml
```

Press ENTER and wait (takes 30-60 seconds)

You should see:
```
Successfully installed flask-3.0.0 flask-cors-4.0.0 python-docx-1.1.0 lxml-4.9.3
```

---

## Next: Reload Web App

### Step 7: Go to Web Tab
```
[Dashboard] → Click "Web" tab at the top
```

### Step 8: Reload Your App
```
Find the big green button that says "Reload leonardus437.pythonanywhere.com"
Click it!
```

Wait 5 seconds for reload to complete.

---

## Test It!

### Step 9: Test Backend
Open new tab and visit:
```
https://leonardus437.pythonanywhere.com/
```

You should see:
```json
{"message": "RTB API", "status": "online", "version": "minimal"}
```

If you see this, SUCCESS! ✅

---

## Troubleshooting

### If you see an error page:
1. Go to Web tab
2. Click "Error log" link
3. Look at the last few lines
4. Common issues:
   - "No module named 'rtb_professional_generator'" → File not uploaded
   - "No module named 'flask'" → Dependencies not installed
   - "No module named 'docx'" → Run: `pip3.10 install --user python-docx`

### If backend shows error:
1. Check all 3 files are uploaded
2. Re-run the pip install command
3. Click Reload again
4. Check error log

---

## You're Done When:
- ✅ Backend URL shows: {"message": "RTB API", "status": "online"}
- ✅ No errors in error log
- ✅ All 3 files visible in Files tab

Then proceed to test the full system!
