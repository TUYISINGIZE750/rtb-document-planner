# URGENT FIX - DOCX Corruption & Offline Mode

## Issues Fixed

### 1. Corrupted DOCX Files ✅
**Problem**: Word couldn't open downloaded files - "Word experienced an error trying to open the file"

**Root Cause**: The `document_generator.py` was using `.get()` method (for dictionaries) but receiving database model objects from the backend.

**Solution**: Updated both `generate_session_plan_docx()` and `generate_scheme_of_work_docx()` functions to handle both dictionaries AND database objects using a helper function.

### 2. Persistent "Offline Mode" Message ✅
**Problem**: Users kept seeing "Session plan download (Offline mode)" even when trying to use the backend.

**Solution**: Updated error message in `wizard.html` to clearly indicate when backend is offline.

## Files Updated

1. **backend/document_generator.py**
   - Added `get_val()` helper function to handle both dict and object data
   - Updated all field access to use the helper
   - Now works with database models from Flask backend

2. **frontend/wizard.html**
   - Improved error message clarity
   - Backend failure now shows: "⚠️ Backend server is offline. Please contact support."

## Deployment Steps for PythonAnywhere

### Step 1: Upload Fixed File
1. Go to: https://www.pythonanywhere.com/user/leonardus437/files/
2. Navigate to your project folder
3. Upload the updated `document_generator.py` file

### Step 2: Reload Web App
1. Go to: https://www.pythonanywhere.com/user/leonardus437/webapps/
2. Click the green "Reload" button for `leonardus437.pythonanywhere.com`
3. Wait for reload to complete

### Step 3: Test
1. Login to your app: https://tuyisingize750.github.io/rtb-document-planner/
2. Create a session plan
3. Download it
4. Open in Microsoft Word - should work perfectly now!

## Technical Details

### Before (Broken):
```python
cells[1].text = data.get('sector', '')  # ❌ Fails with database objects
```

### After (Fixed):
```python
def get_val(key, default=''):
    if isinstance(data, dict):
        return str(data.get(key, default))
    return str(getattr(data, key, default))  # ✅ Works with objects

cells[1].text = get_val('sector')
```

## Why This Happened

The backend passes SQLAlchemy model objects (SessionPlan, SchemeOfWork) to the document generator, not dictionaries. The old code assumed dictionaries, causing:
- AttributeError when accessing fields
- Incomplete/corrupted DOCX files
- Word unable to open the files

## Verification

After deployment, test with phone: **+250796014803**

Expected result:
- ✅ DOCX downloads successfully
- ✅ Word opens file without errors
- ✅ All fields populated correctly
- ✅ Professional RTB formatting intact

## Support

If issues persist:
1. Check PythonAnywhere error logs
2. Verify `document_generator.py` was uploaded correctly
3. Ensure web app was reloaded
4. Test with a fresh session plan creation

---
**Fixed**: January 2025
**Status**: Ready for deployment
