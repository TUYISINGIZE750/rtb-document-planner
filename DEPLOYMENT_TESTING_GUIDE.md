# RTB Document Planner - Deployment Testing Guide

## 🚀 Quick Start Testing

### Step 1: Access the Application
**Frontend URL**: https://rtb-document-planner.pages.dev
**Backend API**: https://leonardus437.pythonanywhere.com

### Step 2: Hard Refresh (Clear Cache)
Press **Ctrl + Shift + R** (Windows) or **Cmd + Shift + R** (Mac)
This ensures you see the latest deployed version.

---

## 🧪 Complete Testing Checklist

### ✅ Test 1: Landing Page & Auto-Redirect
1. Visit: https://rtb-document-planner.pages.dev
2. **Expected**: See RTB-styled landing page (blue/gold colors)
3. If already logged in → should auto-redirect to dashboard
4. **Check**: Hero section, features, services, stats display correctly

### ✅ Test 2: Teacher Registration
1. Click **"Get Started"** or **"Teacher Login"**
2. Click **"Register here"**
3. Fill form:
   - Full Name: `Test Teacher`
   - Phone: `+250788123456` (use unique number)
   - Email: `test@teacher.com`
   - Password: `test123`
4. Click **"Register"**
5. **Expected**: "Registration successful! Please wait for admin approval"

### ✅ Test 3: Admin Login & Activation
1. Visit: https://rtb-document-planner.pages.dev
2. Click **"Admin Login"**
3. Login:
   - Phone: `+250789751597`
   - Password: `admin123`
4. **Expected**: Redirect to `admin.html` (NOT teacher-dashboard)
5. **Check**: See pending users list
6. Find "Test Teacher" → Click **"Activate"**
7. **Expected**: User status changes to "Active"

### ✅ Test 4: Teacher Login
1. Logout from admin
2. Click **"Teacher Login"**
3. Login:
   - Phone: `+250788123456`
   - Password: `test123`
4. **Expected**: Redirect to `teacher-dashboard.html`
5. **Check**: See dashboard with:
   - Session Plans count: 0/5
   - Schemes of Work count: 0/2
   - "Create Session Plan" button
   - "Create Scheme of Work" button

---

## 📄 Test 5: Session Plan Generation (CRITICAL)

### Create Session Plan
1. Click **"Create Session Plan"**
2. Fill all fields:

**Basic Information**:
- School Name: `IPRC Kigali`
- Teacher Name: `John Doe`
- Module Code: `CSC101`
- Module Title: `Introduction to Programming`
- Class: `S4 Computer Science`
- Unit Number: `1`
- Unit Title: `Python Basics`
- Lesson Number: `1`
- Lesson Title: `Variables and Data Types`
- Duration: `90 minutes`
- Date: `2024-01-15`

**Learning Outcomes**:
```
Students will be able to:
- Define variables in Python
- Identify different data types
- Create and manipulate variables
```

**Facilitation Technique**: Select **"Hands-on Practice"**

**Teaching and Learning Activities**:
```
Students will practice creating variables and working with different data types through coding exercises
```

**Resources**:
```
Computer lab
Python IDE
Practice worksheets
```

**Assessment**:
```
Students will complete a coding exercise creating variables of different types
```

3. Click **"Generate Session Plan"**
4. **Expected**: Success message + Download button
5. Click **"Download Session Plan"**

### Verify Downloaded Document
1. Open the downloaded `.docx` file
2. **Check Structure**:
   - ✅ Uses official RTB template format
   - ✅ Times New Roman 12pt font
   - ✅ Proper table structure (23 rows × 6 columns)
   - ✅ Merged cells preserved
   - ✅ All fields filled correctly
   - ✅ No excessive spacing or tabs
   - ✅ Clean bullet points
   - ✅ SMART objectives (concise, no redundancy)
   - ✅ References section (4-5 AI-generated sources)

3. **Verify Content**:
   - School name appears correctly
   - Module and unit info correct
   - Learning outcomes formatted as numbered list
   - Introduction activities match "Hands-on" technique
   - Development activities are technique-specific
   - Resources listed one per line
   - Assessment clear and measurable
   - References relevant to "Programming" topic

---

## 📚 Test 6: Scheme of Work Generation (CRITICAL)

### Create Scheme of Work
1. Return to dashboard
2. Click **"Create Scheme of Work"**
3. Follow 8-step wizard:

**Step 1: Basic Information**
- School Name: `IPRC Kigali`
- Teacher Name: `John Doe`
- Module Code: `CSC201`
- Module Title: `Database Management`
- Class: `S5 Computer Science`
- Academic Year: `2024`

**Step 2: Term 1**
- Number of Weeks: `12`
- Learning Place: `Computer Lab`
- Learning Outcomes:
```
Design database schemas
Create tables and relationships
Write SQL queries
```
- Duration: `48 hours`
- Indicative Contents:
```
Database concepts
ER diagrams
SQL basics
```

**Step 3: Term 2**
- Number of Weeks: `12`
- Learning Place: `Computer Lab`
- Learning Outcomes:
```
Implement advanced queries
Optimize database performance
Create stored procedures
```
- Duration: `48 hours`
- Indicative Contents:
```
Advanced SQL
Indexing
Stored procedures
```

**Step 4: Term 3**
- Number of Weeks: `12`
- Learning Place: `Computer Lab`
- Learning Outcomes:
```
Design complete database systems
Implement security measures
Deploy databases
```
- Duration: `48 hours`
- Indicative Contents:
```
Database security
Backup and recovery
Project implementation
```

**Steps 5-7**: Review each term
**Step 8**: Confirm and generate

4. Click **"Generate Scheme of Work"**
5. **Expected**: Success message + Download button
6. Click **"Download Scheme of Work"**

### Verify Downloaded Scheme
1. Open the downloaded `.docx` file
2. **Check Structure**:
   - ✅ Uses official RTB scheme template
   - ✅ 3 separate tables (Term 1, 2, 3)
   - ✅ Proper column structure (9+ columns)
   - ✅ Times New Roman font
   - ✅ Merged cells preserved
   - ✅ All terms filled correctly
   - ✅ Learning Place field appears for each term
   - ✅ No excessive spacing
   - ✅ Clean formatting

3. **Verify Content**:
   - School and teacher info correct
   - Module code and title correct
   - Each term has correct weeks
   - Learning outcomes formatted properly
   - Duration calculated correctly
   - Indicative contents clear
   - Learning Place specified for each term
   - References section (4-5 AI-generated database sources)

---

## 🔄 Test 7: Download Limits

### Test Free Tier Limits
1. Create 5 session plans (use different topics)
2. **Expected**: After 5th plan, counter shows 5/5
3. Try creating 6th plan
4. **Expected**: "Upgrade Required" button enabled
5. Click button → Payment modal appears

6. Create 2 schemes of work
7. **Expected**: After 2nd scheme, counter shows 2/2
8. Try creating 3rd scheme
9. **Expected**: "Upgrade Required" button enabled

---

## 🐛 Common Issues & Fixes

### Issue 1: "Invalid Document ID" Error
**Cause**: Duplicate checkDownloadLimits() function
**Status**: ✅ FIXED in scheme-wizard.html
**Test**: Create scheme → should work without error

### Issue 2: Admin Sees Landing Page
**Cause**: Auto-redirect not working
**Status**: ✅ FIXED in index.html
**Test**: Admin login → should go to admin.html

### Issue 3: Scattered Content in Documents
**Cause**: Excessive tabs and spacing
**Status**: ✅ FIXED in facilitation_content_generator.py
**Test**: Download document → content should be clean

### Issue 4: Missing References
**Cause**: References not generated
**Status**: ✅ FIXED in content_formatter.py
**Test**: Download document → should have 4-5 references

### Issue 5: Learning Place Missing
**Cause**: Field not in scheme wizard
**Status**: ✅ FIXED in scheme-wizard.html
**Test**: Create scheme → Learning Place field appears for each term

---

## 📊 Backend Verification

### Check PythonAnywhere Files
1. Login to PythonAnywhere
2. Go to **Files** tab
3. Navigate to: `/home/leonardus437/rtb-document-planner/`
4. **Verify these files exist**:
   - ✅ `main.py`
   - ✅ `rtb_template_filler_exact.py`
   - ✅ `facilitation_content_generator.py`
   - ✅ `content_formatter.py`
   - ✅ `document_generator.py`
   - ✅ `rtb_session_plan_template.docx`
   - ✅ `rtb_scheme_template.docx`
   - ✅ `rtb_documents.db`

### Check Database Schema
1. In PythonAnywhere, open **Bash console**
2. Run:
```bash
cd rtb-document-planner
python3
```
3. In Python console:
```python
from main import db, SchemeOfWork
import inspect
print(inspect.getmembers(SchemeOfWork))
```
4. **Verify**: Should see `term1_learning_place`, `term2_learning_place`, `term3_learning_place`

### Check API Endpoints
1. Visit: https://leonardus437.pythonanywhere.com/
2. **Expected**: `{"message": "RTB Document Planner API"}`
3. Test CORS:
   - Open browser console on https://rtb-document-planner.pages.dev
   - Run: `fetch('https://leonardus437.pythonanywhere.com/').then(r => r.json()).then(console.log)`
   - **Expected**: No CORS errors

---

## ✅ Success Criteria

### Frontend ✅
- [ ] Landing page loads with RTB styling
- [ ] Auto-redirect works for logged-in users
- [ ] Admin redirects to admin.html
- [ ] Teacher redirects to teacher-dashboard.html
- [ ] Registration works
- [ ] Login works
- [ ] Session plan wizard completes
- [ ] Scheme wizard completes (8 steps)
- [ ] Download buttons work
- [ ] Download limits enforced

### Backend ✅
- [ ] API responds at pythonanywhere.com
- [ ] CORS allows Cloudflare Pages
- [ ] Database has all required columns
- [ ] Templates exist in backend folder
- [ ] Document generation works
- [ ] Downloads work without errors

### Documents ✅
- [ ] Session plans use official RTB template
- [ ] Schemes use official RTB template
- [ ] Formatting preserved (fonts, colors, merging)
- [ ] Content clean (no excessive spacing)
- [ ] Objectives SMART-formatted
- [ ] Resources one per line
- [ ] References generated (4-5 sources)
- [ ] Learning Place appears in schemes
- [ ] All fields filled correctly
- [ ] Documents match official RTB structure

---

## 🎯 Final Verification Steps

1. **Clear browser cache**: Ctrl + Shift + R
2. **Test complete flow**: Register → Activate → Login → Create → Download
3. **Open documents**: Verify structure matches official RTB templates
4. **Compare side-by-side**:
   - Open official: `TUYISINGIZE LEONARD_SESSION PLAN_S4F3.docx`
   - Open generated session plan
   - **Check**: Same structure, fonts, formatting
   - Open official: `CSAPA 301 Scheme of work.docx`
   - Open generated scheme
   - **Check**: Same structure, 3 tables, formatting

5. **Test different facilitation techniques**:
   - Create session plan with "Trainer-guided"
   - Create session plan with "Group work"
   - Create session plan with "Simulation"
   - **Verify**: Each generates different content

6. **Test different topics**:
   - Programming → References about Python, Java, etc.
   - Networking → References about TCP/IP, routing, etc.
   - Databases → References about SQL, normalization, etc.
   - **Verify**: References match topic

---

## 📞 Support

If any test fails:
1. Check browser console for errors (F12)
2. Check PythonAnywhere error logs
3. Verify all files uploaded to PythonAnywhere
4. Verify database schema updated
5. Hard refresh browser (Ctrl + Shift + R)

---

## 🎉 Deployment Status

**Frontend**: ✅ Deployed to Cloudflare Pages
**Backend**: ✅ Deployed to PythonAnywhere
**Templates**: ✅ Official RTB templates uploaded
**Database**: ✅ Schema updated with learning_place fields
**CORS**: ✅ Configured for *.pages.dev
**Auto-redirect**: ✅ Working for admin/teacher
**Download limits**: ✅ Enforced (5 plans, 2 schemes)

**Last Commit**: cb1cdb7
**Status**: PRODUCTION READY 🚀

