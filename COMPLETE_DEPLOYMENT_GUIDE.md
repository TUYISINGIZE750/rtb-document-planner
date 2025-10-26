# COMPLETE DEPLOYMENT GUIDE - RTB Document Planner

## 📋 Current Backend Files (7 files total)

### Files in PRODUCTION_READY/backend/:
1. ✅ **main.py** - Main Flask API (KEEP - already deployed)
2. ✅ **document_generator.py** - Document generator (UPDATE - new version)
3. ✅ **requirements.txt** - Dependencies (KEEP - already deployed)
4. ✅ **rtb_template_filler.py** - NEW - Fills RTB templates
5. ✅ **rtb_document_generator.py** - OLD - Not needed (DELETE)
6. ✅ **rtb_session_plan_template.docx** - Official RTB template
7. ✅ **rtb_scheme_template.docx** - Official RTB template
8. ✅ **test_templates.py** - Test script (optional, for local testing)

## 🎯 DEPLOYMENT PLAN

### Files to Upload to PythonAnywhere:

**UPLOAD THESE 4 FILES:**
1. `document_generator.py` (REPLACE existing)
2. `rtb_template_filler.py` (NEW)
3. `rtb_session_plan_template.docx` (NEW)
4. `rtb_scheme_template.docx` (NEW)

**DELETE THIS FILE from PythonAnywhere:**
- `rtb_document_generator.py` (old, not used)

**KEEP THESE FILES (already deployed):**
- `main.py`
- `requirements.txt`

## 📝 STEP-BY-STEP DEPLOYMENT

### Step 1: Login to PythonAnywhere
```
1. Go to: https://www.pythonanywhere.com
2. Login with your credentials
3. Click on "Files" tab
```

### Step 2: Navigate to Your Directory
```
1. Click on path: /home/leonardus437/
2. You should see existing files: main.py, requirements.txt, etc.
```

### Step 3: Delete Old File (if exists)
```
1. Find: rtb_document_generator.py
2. Click the trash icon to delete it
3. Confirm deletion
```

### Step 4: Upload New Files
```
1. Click "Upload a file" button
2. Upload these 4 files ONE BY ONE:
   
   a) document_generator.py
      - Browse to: PRODUCTION_READY/backend/document_generator.py
      - Click Upload
      - If asked to replace, click YES
   
   b) rtb_template_filler.py
      - Browse to: PRODUCTION_READY/backend/rtb_template_filler.py
      - Click Upload
   
   c) rtb_session_plan_template.docx
      - Browse to: PRODUCTION_READY/backend/rtb_session_plan_template.docx
      - Click Upload
   
   d) rtb_scheme_template.docx
      - Browse to: PRODUCTION_READY/backend/rtb_scheme_template.docx
      - Click Upload
```

### Step 5: Verify Files
```
After upload, you should see these files in /home/leonardus437/:
- main.py
- document_generator.py (updated)
- rtb_template_filler.py (new)
- rtb_session_plan_template.docx (new)
- rtb_scheme_template.docx (new)
- requirements.txt
- rtb_planner.db
```

### Step 6: Reload Web App
```
1. Click "Web" tab at top
2. Find your web app: leonardus437.pythonanywhere.com
3. Scroll to top
4. Click the green "Reload" button
5. Wait 30 seconds
```

### Step 7: Test API
```
1. Open new browser tab
2. Go to: https://leonardus437.pythonanywhere.com/
3. Should see:
   {
     "message": "RTB Document Planner API",
     "status": "online",
     ...
   }
```

## ✅ TESTING THE SYSTEM

### Test 1: Login as Teacher
```
1. Go to: https://tuyisingize750.github.io/rtb-document-planner/
2. Click "Teacher Login"
3. Login with your test account
4. Should see dashboard with download limits
```

### Test 2: Create Session Plan
```
1. Click "Create Session Plan"
2. Fill in all fields:
   - Sector: ICT & MULTIMEDIA
   - Trade: Software Development
   - Level: Level 4
   - Trainer: Your Name
   - Module: TEST301 Test Module
   - Term: Term 1
   - Week: Week 1
   - Date: Today's date
   - Class: L4CSA-A
   - Trainees: 30
   - Duration: 80
   - Topic: Test Topic
   - Learning Outcomes: Test outcomes
   - Indicative Contents: Test contents
   - Facilitation: Demonstration
3. Click "Generate Session Plan"
4. Document should download
```

### Test 3: Verify Document Format
```
1. Open downloaded .docx file
2. Check:
   ✓ Times New Roman font, 12pt
   ✓ Bold labels
   ✓ Table with 23 rows, 6 columns
   ✓ All your data filled in
   ✓ Looks EXACTLY like RTB template
```

### Test 4: Test Subscription Modal
```
1. Create 2 session plans (use up free limit)
2. Try to create 3rd session plan
3. Should see subscription modal with:
   - 7 subscription plans
   - Payment instructions
   - Mobile money: +250789751597
   - Name: Leonard TUYISINGIZE
```

### Test 5: Premium User (Admin Test)
```
1. Login as admin
2. Upgrade a test user to premium
3. Login as that user
4. Should NOT see upgrade card
5. Can create unlimited documents
```

## 🔍 TROUBLESHOOTING

### Problem: API shows offline
**Solution:**
```
1. Check PythonAnywhere error log:
   - Web tab → Error log
2. Look for Python errors
3. Common issues:
   - Missing file
   - Syntax error
   - Import error
```

### Problem: Document generation fails
**Solution:**
```
1. Check if templates uploaded:
   - Files tab → /home/leonardus437/
   - Should see both .docx files
2. Check file permissions
3. Check error log for details
```

### Problem: Document doesn't match RTB format
**Solution:**
```
1. Re-download templates from RTB Templates folder
2. Re-upload to PythonAnywhere
3. Reload web app
4. Test again
```

### Problem: Subscription modal not showing
**Solution:**
```
1. Clear browser cache (Ctrl+Shift+Delete)
2. Hard refresh (Ctrl+F5)
3. Wait 2 minutes for GitHub Pages to update
4. Try in incognito mode
```

## 📊 VERIFICATION CHECKLIST

After deployment, verify:

**Backend (PythonAnywhere):**
- [ ] API responds at https://leonardus437.pythonanywhere.com/
- [ ] All 5 files present in /home/leonardus437/
- [ ] No errors in error log
- [ ] Web app shows "Running"

**Frontend (GitHub Pages):**
- [ ] Site loads at https://tuyisingize750.github.io/rtb-document-planner/
- [ ] Login works
- [ ] Dashboard shows correctly
- [ ] Subscription modal appears when needed

**Documents:**
- [ ] Session plans download successfully
- [ ] Session plans match RTB format exactly
- [ ] Schemes download successfully
- [ ] Schemes match RTB format exactly

**Subscription System:**
- [ ] Free users see download limits
- [ ] Free users see upgrade card
- [ ] Premium users don't see upgrade card
- [ ] Modal shows payment instructions
- [ ] Modal has all 7 subscription plans

## 🎉 SUCCESS CRITERIA

✅ All files uploaded to PythonAnywhere
✅ Web app reloaded successfully
✅ API responds with status "online"
✅ Teachers can login and create documents
✅ Documents match RTB templates EXACTLY
✅ Subscription modal works correctly
✅ Premium users have clean interface

## 📞 SUPPORT

If you encounter issues:

1. **Check error logs** in PythonAnywhere
2. **Verify all files** are uploaded
3. **Test in incognito mode** to rule out cache issues
4. **Compare downloaded document** with original RTB template

---

**Deployment Time:** 10-15 minutes
**Downtime:** None (files replaced while running)
**Rollback:** Keep backup of old document_generator.py

**Status:** READY TO DEPLOY ✅
