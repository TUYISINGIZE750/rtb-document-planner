# 🚨 URGENT FIX - Files Not Uploaded to PythonAnywhere

## ❌ Current Problem

Error: `{"detail":"Document generation not available yet"}` (503)

**Root Cause**: The new files (`official_template_filler.py` and `DOCS TO REFER TO` folder) are NOT on PythonAnywhere yet!

The error occurs at line 519 in main_minimal.py:
```python
except Exception as gen_error:
    logger.error(f"Generation error: {gen_error}")
    return jsonify({"detail": "Document generation not available yet"}), 503
```

This means `from document_generator import generate_session_plan_docx` is failing because:
1. `document_generator.py` tries to import `official_template_filler`
2. `official_template_filler.py` doesn't exist on PythonAnywhere
3. OR `DOCS TO REFER TO` folder doesn't exist

## ✅ SOLUTION - Upload Missing Files NOW

### Step 1: Go to PythonAnywhere
https://www.pythonanywhere.com → Files tab → `/home/leonardus437/mysite/`

### Step 2: Upload These 3 Files/Folders

#### File 1: document_generator.py
**Location**: `C:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\backend\document_generator.py`

**Content should be**:
```python
"""Document Generator - Uses Official RTB Templates"""
from official_template_filler import fill_session_plan_official, fill_scheme_official

def generate_session_plan_docx(data):
    return fill_session_plan_official(data)

def generate_scheme_of_work_docx(data):
    return fill_scheme_official(data)
```

#### File 2: official_template_filler.py
**Location**: `C:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\backend\official_template_filler.py`

**Upload this entire file** (180 lines with set_cell_font function)

#### Folder 3: DOCS TO REFER TO
**Location**: `C:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\DOCS TO REFER TO\`

**Steps**:
1. In PythonAnywhere Files, click "New directory"
2. Name it: `DOCS TO REFER TO`
3. Go into the folder
4. Upload both files:
   - `SESSION PLAN.docx`
   - `CSAPA 301 Scheme of work.docx`

### Step 3: Verify File Structure

After upload, your PythonAnywhere should have:
```
/home/leonardus437/mysite/
├── main.py                           ← Already there
├── document_generator.py             ← UPLOAD THIS (replace old one)
├── official_template_filler.py       ← UPLOAD THIS (NEW)
├── DOCS TO REFER TO/                 ← CREATE THIS FOLDER
│   ├── SESSION PLAN.docx             ← UPLOAD THIS
│   └── CSAPA 301 Scheme of work.docx ← UPLOAD THIS
├── requirements.txt                  ← Already there
└── rtb_planner.db                    ← Already there
```

### Step 4: Update main.py

**IMPORTANT**: Replace main.py with main_minimal.py

1. Delete old `main.py` on PythonAnywhere
2. Upload `main_minimal.py` from: `C:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\backend\main_minimal.py`
3. Rename `main_minimal.py` to `main.py`

### Step 5: Reload Application

1. Go to **Web** tab
2. Click green **Reload** button
3. Wait 10 seconds

### Step 6: Test Again

1. Go to: https://rtb-document-planner.pages.dev
2. Login as teacher
3. Create session plan
4. Click download
5. Should work now! ✅

## 🔍 How to Verify Files Are Uploaded

### Check 1: document_generator.py
Open the file on PythonAnywhere and verify first line is:
```python
from official_template_filler import fill_session_plan_official, fill_scheme_official
```

### Check 2: official_template_filler.py exists
File should be 180+ lines with `set_cell_font()` function

### Check 3: DOCS TO REFER TO folder exists
Should contain 2 .docx files

### Check 4: Test import in PythonAnywhere console
```python
from official_template_filler import fill_session_plan_official
print("Success!")
```

If this works, files are uploaded correctly.

## 📋 Quick Upload Checklist

- [ ] Upload `document_generator.py` (replace old)
- [ ] Upload `official_template_filler.py` (new file)
- [ ] Create folder `DOCS TO REFER TO`
- [ ] Upload `SESSION PLAN.docx` to folder
- [ ] Upload `CSAPA 301 Scheme of work.docx` to folder
- [ ] Replace `main.py` with `main_minimal.py`
- [ ] Click Reload button
- [ ] Test download

## ⚠️ Common Mistakes

1. ❌ Forgot to upload `official_template_filler.py`
2. ❌ Folder name wrong (must be exactly `DOCS TO REFER TO` with spaces)
3. ❌ Templates not in the folder
4. ❌ Didn't click Reload button
5. ❌ Old `document_generator.py` still importing wrong module

## 🎯 Expected Result After Fix

When teacher downloads session plan:
- ✅ No 503 error
- ✅ File downloads successfully
- ✅ Document has Bookman Old Style 12pt font
- ✅ Professional RTB formatting
- ✅ 23×6 table structure

---

**DO THIS NOW** - Upload the 3 files/folders and reload!
