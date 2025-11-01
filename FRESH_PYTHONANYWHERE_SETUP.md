# 🆕 FRESH PythonAnywhere Setup - From Scratch

## 📋 Complete File List to Upload

You deleted everything, so here's what you need to upload:

### **ALL FILES FROM YOUR COMPUTER:**

```
From: C:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\backend\

Upload these 3 Python files:
1. main_minimal.py (rename to main.py)
2. document_generator.py
3. official_template_filler.py
4. requirements.txt

From: C:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\DOCS TO REFER TO\

Upload these 2 Word files:
5. SESSION PLAN.docx
6. CSAPA 301 Scheme of work.docx
```

---

## 🚀 STEP-BY-STEP SETUP (Fresh Start)

### **STEP 1: Create mysite folder**

1. Go to: https://www.pythonanywhere.com/user/leonardus437/files/home/leonardus437/
2. Click: **"New directory"** button
3. Type: `mysite`
4. Press Enter
5. Click on **mysite** folder to enter it
6. You're now at: `/home/leonardus437/mysite/`

---

### **STEP 2: Upload requirements.txt**

1. Still in `/home/leonardus437/mysite/`
2. Click: **"Upload a file"** button
3. Select: `C:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\backend\requirements.txt`
4. Upload

---

### **STEP 3: Upload main_minimal.py**

1. Click: **"Upload a file"** button
2. Select: `C:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\backend\main_minimal.py`
3. After upload, click on the filename **main_minimal.py**
4. Click: **"Rename"** button at top
5. Change name to: `main.py`
6. Click: **"OK"** or press Enter

---

### **STEP 4: Upload document_generator.py**

1. Click: **"Upload a file"** button
2. Select: `C:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\backend\document_generator.py`
3. Upload

---

### **STEP 5: Upload official_template_filler.py**

1. Click: **"Upload a file"** button
2. Select: `C:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\backend\official_template_filler.py`
3. Upload

---

### **STEP 6: Create "DOCS TO REFER TO" folder**

1. Still in `/home/leonardus437/mysite/`
2. Click: **"New directory"** button
3. Type EXACTLY: `DOCS TO REFER TO` (with spaces)
4. Press Enter
5. Click on **DOCS TO REFER TO** folder to enter it
6. You're now at: `/home/leonardus437/mysite/DOCS TO REFER TO/`

---

### **STEP 7: Upload SESSION PLAN.docx**

1. Inside the `DOCS TO REFER TO` folder
2. Click: **"Upload a file"** button
3. Select: `C:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\DOCS TO REFER TO\SESSION PLAN.docx`
4. Upload

---

### **STEP 8: Upload CSAPA 301 Scheme of work.docx**

1. Still inside `DOCS TO REFER TO` folder
2. Click: **"Upload a file"** button
3. Select: `C:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\DOCS TO REFER TO\CSAPA 301 Scheme of work.docx`
4. Upload

---

### **STEP 9: Go back to mysite folder**

1. Click on **mysite** in the breadcrumb at top
2. Or navigate to: `/home/leonardus437/mysite/`

---

### **STEP 10: Verify file structure**

Your `/home/leonardus437/mysite/` should now have:

```
/home/leonardus437/mysite/
├── main.py                           ✓
├── document_generator.py             ✓
├── official_template_filler.py       ✓
├── requirements.txt                  ✓
└── DOCS TO REFER TO/                 ✓
    ├── SESSION PLAN.docx             ✓
    └── CSAPA 301 Scheme of work.docx ✓
```

**Total: 4 files + 1 folder (with 2 files inside) = 6 items**

---

### **STEP 11: Install dependencies**

1. Go to: **Consoles** tab
2. Click: **"Bash"** to start a new console
3. Type these commands:

```bash
cd /home/leonardus437/mysite
pip3.10 install --user -r requirements.txt
```

4. Wait for installation to complete
5. Should see: "Successfully installed flask flask-cors python-docx lxml sqlalchemy"

---

### **STEP 12: Initialize database**

1. Still in the Bash console
2. Type:

```bash
cd /home/leonardus437/mysite
python3.10 -c "from main import Base, engine; Base.metadata.create_all(bind=engine); print('Database created!')"
```

3. Should see: "Database created!"
4. This creates `rtb_planner.db` file

---

### **STEP 13: Configure Web App**

1. Go to: **Web** tab
2. Click: **"Add a new web app"** button
3. Choose: **"Flask"**
4. Python version: **Python 3.10**
5. Path to Flask app: `/home/leonardus437/mysite/main.py`
6. Click: **"Next"** through the setup

---

### **STEP 14: Configure WSGI file**

1. Still on **Web** tab
2. Find section: **"Code"**
3. Click on: **WSGI configuration file** link (e.g., `/var/www/leonardus437_pythonanywhere_com_wsgi.py`)
4. Replace ALL content with:

```python
import sys
path = '/home/leonardus437/mysite'
if path not in sys.path:
    sys.path.append(path)

from main import app as application
```

5. Click: **"Save"** button at top

---

### **STEP 15: Reload application**

1. Go back to: **Web** tab
2. Scroll to top
3. Click: **Green "Reload" button**
4. Wait 10 seconds

---

### **STEP 16: Test API**

1. Open new browser tab
2. Go to: https://leonardus437.pythonanywhere.com/
3. Should see:

```json
{
  "message": "RTB API Online",
  "status": "ok",
  "cors": "enabled"
}
```

✅ **If you see this, setup is successful!**

---

### **STEP 17: Test Frontend**

1. Go to: https://rtb-document-planner.pages.dev/
2. Click: **"Register"**
3. Create a new teacher account
4. Login
5. Create a session plan
6. Download it
7. Open the .docx file
8. Verify: **Bookman Old Style 12pt font** throughout

---

## ✅ Final Checklist

- [ ] mysite folder created
- [ ] 4 Python files uploaded (main.py, document_generator.py, official_template_filler.py, requirements.txt)
- [ ] DOCS TO REFER TO folder created
- [ ] 2 .docx files uploaded to folder
- [ ] Dependencies installed
- [ ] Database initialized
- [ ] Web app configured
- [ ] WSGI file updated
- [ ] Application reloaded
- [ ] API responding correctly
- [ ] Frontend can connect
- [ ] Documents download with correct formatting

---

## 🔧 Troubleshooting

### If API shows error:
1. Check **Error log** on Web tab
2. Look for import errors
3. Verify all files are in `/home/leonardus437/mysite/`

### If documents don't download:
1. Verify `DOCS TO REFER TO` folder exists
2. Check both .docx files are inside
3. Check error log for "FileNotFoundError"

### If formatting is wrong:
1. Verify `official_template_filler.py` was uploaded
2. Check it has `set_cell_font()` function
3. Verify templates are the correct ones from DOCS TO REFER TO folder

---

## 📞 Quick Commands Reference

```bash
# Navigate to mysite
cd /home/leonardus437/mysite

# Install dependencies
pip3.10 install --user -r requirements.txt

# Initialize database
python3.10 -c "from main import Base, engine; Base.metadata.create_all(bind=engine)"

# Test imports
python3.10 -c "from official_template_filler import fill_session_plan_official; print('Success!')"

# List files
ls -la

# Check folder contents
ls -la "DOCS TO REFER TO/"
```

---

**Follow these steps in order and your PythonAnywhere will be set up correctly!** 🎉
