# PythonAnywhere - Fresh Clean Start

## Step 1: Delete Everything

1. Log into **PythonAnywhere.com**
2. Go to **Files** tab
3. Click on `/home/leonardus437/` folder
4. **Select ALL files** (Click checkbox at top)
5. Click **Delete** button
6. Confirm deletion
7. **Wait** until folder is completely empty

---

## Step 2: Upload ONLY These 6 Files

In `/home/leonardus437/` upload:

1. **main.py**
2. **document_generator.py**
3. **ai_content_generator.py**
4. **facilitation_content_generator.py**
5. **init_db.py**
6. **requirements.txt**

**Source location on your computer:**
```
C:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\backend\
```

---

## Step 3: Create RTB Templates Folder

1. In PythonAnywhere Files (in `/home/leonardus437/`)
2. Click **New Folder**
3. Name: `RTB Templates`
4. Press Enter

---

## Step 4: Upload Templates

Into the `RTB Templates/` folder, upload these 2 files:

1. **RTB Session plan template.docx**
2. **Scheme of work.docx**

**Source location on your computer:**
```
C:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\backend\RTB Templates\
```

---

## Step 5: Install Dependencies

1. In PythonAnywhere, click **"Open Bash console here"** (next to your folder)
2. Type:
```bash
pip install -r requirements.txt
```
3. Wait for installation to complete (should see ✓ Installed successfully)

---

## Step 6: Update WSGI File

1. Go to **Web** tab in PythonAnywhere
2. Find **WSGI configuration file** (blue link on the right)
3. Delete ALL content
4. Paste this:

```python
import sys
path = '/home/leonardus437'
if path not in sys.path:
    sys.path.insert(0, path)

from main import app
application = app
```

5. Click **Save**

---

## Step 7: Reload App

1. Still in **Web** tab
2. Click the green **Reload** button
3. Wait 5-10 seconds

---

## Step 8: Test

1. Open your browser
2. Go to: **https://leonardus437.pythonanywhere.com/**
3. You should see a response (check browser console F12 if nothing shows)

---

## Final Directory Structure

After all steps, your `/home/leonardus437/` should look like:

```
/home/leonardus437/
├── main.py
├── document_generator.py
├── ai_content_generator.py
├── facilitation_content_generator.py
├── init_db.py
├── requirements.txt
└── RTB Templates/
    ├── RTB Session plan template.docx
    └── Scheme of work.docx
```

**That's it. Nothing else.**

---

## Checklist

- [ ] Deleted all old files
- [ ] Uploaded 6 Python files
- [ ] Created RTB Templates folder
- [ ] Uploaded 2 template files
- [ ] Ran pip install -r requirements.txt
- [ ] Updated WSGI file
- [ ] Clicked Reload
- [ ] Tested API at https://leonardus437.pythonanywhere.com/

✅ When all checked, you're done!
