# PythonAnywhere Upload Guide - CORRECT FILES

## Files to Upload to `/home/leonardus437/`

Upload these **7 files** from:
`C:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\backend\`

1. **main.py** ✅
2. **document_generator.py** ✅
3. **rtb_template_filler_exact.py** ✅ (THIS IS THE CORRECT ONE)
4. **facilitation_content_generator.py** ✅
5. **content_formatter.py** ✅
6. **init_db.py** ✅
7. **requirements.txt** ✅

## Templates to Upload

Create folder: `/home/leonardus437/RTB Templates/`

Upload these **2 templates**:
1. **rtb_session_plan_template.docx** (from backend folder)
2. **rtb_scheme_template.docx** (from backend folder)

**NOT from RTB Templates subfolder - use the ones directly in backend folder!**

## Install Dependencies

```bash
pip install -r requirements.txt
```

## WSGI Configuration

```python
import sys
path = '/home/leonardus437'
if path not in sys.path:
    sys.path.insert(0, path)

from main import app
application = app
```

## Final Structure

```
/home/leonardus437/
├── main.py
├── document_generator.py
├── rtb_template_filler_exact.py
├── facilitation_content_generator.py
├── content_formatter.py
├── init_db.py
├── requirements.txt
└── RTB Templates/
    ├── rtb_session_plan_template.docx
    └── rtb_scheme_template.docx
```

## Initialize Database

After upload, run in Bash console:
```bash
cd /home/leonardus437
python init_db.py
```

## Test

Visit: https://leonardus437.pythonanywhere.com/

Should see: `{"message": "RTB Document Planner API"}`
