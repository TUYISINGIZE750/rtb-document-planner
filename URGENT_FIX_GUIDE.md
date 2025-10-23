# URGENT FIX: Invalid Credentials Issue

## Problem
Users getting "Invalid credentials" error when trying to login with test accounts.

## Root Cause
1. Backend API returning `None` values for user name and role
2. Test users may not exist in production database

## IMMEDIATE SOLUTION

### Step 1: Upload Fixed Backend Files to PythonAnywhere

Upload these 2 files to your PythonAnywhere account:

1. **main.py** (replace existing)
   - Upload: `backend/main_fixed.py` → rename to `main.py`
   - This fixes the login response to return proper user data

2. **simple_document_generator.py** (replace existing)  
   - Upload: `backend/simple_document_generator.py`
   - This ensures DOCX files are generated correctly

### Step 2: Test Working Credentials

After uploading, these accounts should work:

**Teacher Account:**
- Phone: `+250796014803`
- Password: `teacher123`

**Admin Account:**
- Phone: `+250789751597` 
- Password: `admin123`

### Step 3: Verify Fix

1. Go to: https://tuyisingize750.github.io/rtb-document-planner/
2. Click "Login"
3. Use: `+250796014803` / `teacher123`
4. Should see: "Welcome, Test Teacher!" (not "undefined")
5. Create a session plan - DOCX should download and open properly

## Files to Upload to PythonAnywhere

```
backend/main_fixed.py → main.py
backend/simple_document_generator.py → simple_document_generator.py
```

## Expected Results After Fix

✅ Login shows proper username (not "undefined")
✅ DOCX files download and open in Microsoft Word
✅ No more "Invalid credentials" for test accounts
✅ Both session plans and schemes work properly

## If Still Having Issues

Run this test script locally to verify API:
```bash
cd backend
python test_login.py
```

This will show if the API is working and create test accounts if needed.

## Technical Details

**Fixed in main_fixed.py:**
- Login endpoint now returns complete user data with fallbacks
- Proper null checking for all user fields
- Increased default limits to 5 documents each

**Fixed in simple_document_generator.py:**
- Simplified DOCX generation without complex tables
- Better error handling for data extraction
- Compatible with both dict and SQLAlchemy objects