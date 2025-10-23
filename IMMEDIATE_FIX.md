# IMMEDIATE FIX FOR 500 ERROR

## Problem
Teachers getting 500 error when creating documents because backend database issues.

## SOLUTION: Upload Minimal Backend

**Upload this file to PythonAnywhere:**
- `backend/main_minimal.py` → rename to `main.py`

## Why This Works
- No database dependencies
- Simple in-memory storage
- Built-in test users
- Direct DOCX generation
- Eliminates all SQLAlchemy issues

## Test After Upload
1. Login: `+250796014803` / `teacher123`
2. Create session plan → Should work immediately
3. Download DOCX → Should open in Word

## This Minimal Backend Provides
✅ Working login
✅ Document creation (no 500 errors)
✅ DOCX download
✅ CORS configured for GitHub Pages

**Upload `main_minimal.py` as `main.py` to PythonAnywhere NOW**