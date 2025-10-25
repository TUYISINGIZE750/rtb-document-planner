# Scheme of Work - Learning Place Field Added ✅

## What's New

Added **Learning Place** field for each term in Scheme of Work wizard.

### Fields Added:
- ✅ Term 1: Learning Place
- ✅ Term 2: Learning Place  
- ✅ Term 3: Learning Place

### Example Values:
- Classroom
- Workshop
- Laboratory
- Computer Lab
- Practical Workshop
- Field/Outdoor
- Online/Virtual

---

## Changes Made

### 1. Frontend (scheme-wizard.html)
Added Learning Place input field for each term:
```html
<input type="text" name="term1_learning_place" placeholder="e.g., Classroom, Workshop, Lab" required>
```

### 2. Backend (main.py)
Added database columns:
- `term1_learning_place`
- `term2_learning_place`
- `term3_learning_place`

### 3. Template Filler (rtb_template_filler_exact.py)
Updated to fill Learning Place in scheme template (if column exists)

---

## For PythonAnywhere

### Upload Updated Files:

1. **main.py**
   - From: `C:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\backend\main.py`
   - To: `/home/leonardus437/rtb-document-planner/`

2. **rtb_template_filler_exact.py**
   - From: `C:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\backend\rtb_template_filler_exact.py`
   - To: `/home/leonardus437/rtb-document-planner/`

3. **Delete old database** (to recreate with new columns):
   ```bash
   rm rtb_planner.db
   python init_db.py
   ```

4. **Reload web app**

---

## For Cloudflare

Changes auto-deployed (commit 344d230):
- ✅ scheme-wizard.html updated with Learning Place fields

Visit: https://rtb-document-planner.pages.dev

**Hard refresh**: `Ctrl + Shift + R`

---

## Testing

1. Visit scheme wizard
2. Fill Term 1, 2, 3 forms
3. Each term now has "Learning Place" field
4. Enter location (e.g., "Computer Lab")
5. Generate scheme
6. Learning Place should appear in document

---

**Status**: ✅ Complete
**Deployed**: Cloudflare (auto)
**Backend**: Upload 2 files + recreate database
