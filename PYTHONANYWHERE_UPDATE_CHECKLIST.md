# PythonAnywhere Update Checklist
## RTB 100% Compliance Solution

**Date Started**: ________________  
**Your PythonAnywhere Username**: ________________  
**Target Completion Date**: ________________

---

## **PHASE 1: PREPARATION** ⏱️ Estimated: 5 minutes

- [ ] Download the 3 guidance documents:
  - `PYTHONANYWHERE_UPDATE_GUIDE_RTB_100_PERCENT.md`
  - `PYTHONANYWHERE_QUICK_REFERENCE.txt`
  - `PYTHONANYWHERE_POST_UPDATE_TEST.py`

- [ ] Gather the 2 new Python files:
  - [ ] `rtb_template_filler_100_percent.py` - location: `PRODUCTION_READY/backend/`
  - [ ] `smart_content_generator.py` - location: `PRODUCTION_READY/backend/`

- [ ] Create a work folder on your computer named:
  `PythonAnywhere_Update_[TODAY'S_DATE]`

- [ ] Copy both `.py` files into that folder

- [ ] Test files locally (optional but recommended):
  ```
  python test_local.py
  ```
  - [ ] Local test passed ✓

---

## **PHASE 2: BACKUP** ⏱️ Estimated: 3 minutes

- [ ] Login to https://www.pythonanywhere.com

- [ ] Navigate to **Files** tab

- [ ] Download current `main.py`:
  - [ ] Click on `main.py`
  - [ ] Download to your computer
  - [ ] Save as `main.py.backup.YYYY-MM-DD`
  - [ ] Store in your work folder

- [ ] Download these files as backup (optional but recommended):
  - [ ] `document_generator.py`
  - [ ] `models.py` (if exists)
  - [ ] `requirements.txt` (if exists)

- [ ] Create a folder: `PythonAnywhere_Backup_[DATE]`
- [ ] Store all downloaded files there

**Backup Location**: ________________  
**Backup Date/Time**: ________________

---

## **PHASE 3: UPLOAD NEW FILES** ⏱️ Estimated: 5 minutes

### **File 1: smart_content_generator.py**

- [ ] In PythonAnywhere Files tab, click **"Upload a file"**
- [ ] Select `smart_content_generator.py` from your computer
- [ ] Click **Upload**
- [ ] Verify file appears in file list
- [ ] Note: File size should be approximately 6-7 KB

**Uploaded**: ________________ (Date/Time)

### **File 2: rtb_template_filler_100_percent.py**

- [ ] Click **"Upload a file"** again
- [ ] Select `rtb_template_filler_100_percent.py` from your computer
- [ ] Click **Upload**
- [ ] Verify file appears in file list
- [ ] Note: File size should be approximately 10-12 KB

**Uploaded**: ________________ (Date/Time)

### **Verification**

In PythonAnywhere Files browser, you should now see:
- [ ] smart_content_generator.py ✓
- [ ] rtb_template_filler_100_percent.py ✓
- [ ] main.py ✓
- [ ] (other existing files) ✓

---

## **PHASE 4: UPDATE main.py** ⏱️ Estimated: 5 minutes

### **Step 1: Open main.py**

- [ ] In **Files** tab, click on `main.py`
- [ ] File opens in editor

### **Step 2: Find the Import Section**

- [ ] Use Ctrl+F to find: `rtb_template_filler_exact`
- [ ] This should be around line 14-20

### **Step 3: Locate Exact Text to Replace**

Current code should look like:
```python
from rtb_template_filler_exact import (
    fill_session_plan_template,
    fill_scheme_template
)
```

- [ ] Found the import section ✓

### **Step 4: Replace with New Import**

**DELETE** these lines:
```python
from rtb_template_filler_exact import (
    fill_session_plan_template,
    fill_scheme_template
)
```

**REPLACE WITH** exactly this:
```python
from rtb_template_filler_100_percent import fill_session_plan_template_100_percent as fill_session_plan_template
from rtb_template_filler_exact import fill_scheme_template
```

### **Verification in Editor**

- [ ] Old import is removed
- [ ] New import is in correct position
- [ ] No typos in filenames
- [ ] Proper spacing/indentation

### **Step 5: Save**

- [ ] Click **Save** button in editor
- [ ] See confirmation message
- [ ] File shows as saved (no asterisk in filename)

**Updated**: ________________ (Date/Time)

---

## **PHASE 5: RELOAD WEB APP** ⏱️ Estimated: 2 minutes

- [ ] Click **Web** tab in PythonAnywhere
- [ ] Look for your Flask app in the list on the left
- [ ] Click on your app name to open settings
- [ ] Find large **Reload** button at top
- [ ] Click **Reload**
- [ ] Wait for process to complete
- [ ] See message: "Webapp reloaded at [time]"

**Reloaded**: ________________ (Date/Time)

### **Check Error Log**

- [ ] Click **Error log** link on Web page
- [ ] Scroll to bottom of log
- [ ] Look for any errors related to:
  - [ ] ❌ "ModuleNotFoundError"
  - [ ] ❌ "ImportError"
  - [ ] ❌ "SyntaxError"

**Result**: 
- [ ] ✓ No errors found
- [ ] ⚠️ Errors found (See Troubleshooting section)

---

## **PHASE 6: INITIAL FUNCTIONALITY TEST** ⏱️ Estimated: 5 minutes

### **Test 1: App Still Works**

- [ ] Open your app URL in browser
- [ ] Homepage loads ✓
- [ ] Can navigate to login ✓
- [ ] Login functionality works ✓
- [ ] Dashboard loads ✓

### **Test 2: Check No Errors**

- [ ] Open browser developer console (F12)
- [ ] Go to **Console** tab
- [ ] No red errors visible ✓
- [ ] No connection errors ✓

**Basic Functionality**: ✓ PASSED

---

## **PHASE 7: DOCUMENT GENERATION TEST** ⏱️ Estimated: 10 minutes

### **Create Test Session Plan**

In your app, create a new session plan with this test data:

| Field | Value |
|-------|-------|
| **Sector** | Information & Communication Technology |
| **Trade** | Software Development |
| **Trainer Name** | Test Trainer |
| **RQF Level** | Level 4 |
| **Module** | CS401 - Python Programming |
| **Week** | 1 |
| **Term** | 1 |
| **Date** | Today's date |
| **Topic** | Object-Oriented Programming: Classes |
| **Duration** | 90 |
| **Number of Trainees** | 25 |
| **Class Name** | Class A |
| **Learning Outcomes** | Learners will understand OOP concepts |
| **Facilitation** | Trainer-guided instruction |
| **Contents** | Classes, objects, inheritance |
| **Resources** | IDE, laptops, documentation |

- [ ] Form filled out
- [ ] Data submitted successfully

### **Download Document**

- [ ] Click **Download** button
- [ ] Document downloads (should be ~100-150 KB)
- [ ] File saved as `.docx` format
- [ ] Filename shows date/session info

**Downloaded File**: ________________  
**Download Time**: ________________

---

## **PHASE 8: DOCUMENT QUALITY VERIFICATION** ⏱️ Estimated: 10 minutes

### **Open Document in Microsoft Word**

- [ ] Double-click downloaded `.docx` file
- [ ] File opens in Word without errors
- [ ] All content visible and readable

### **Check Formatting**

#### **Font Check**
- [ ] Select all text (Ctrl+A)
- [ ] Check font dropdown → should show **"Book Antiqua"**
- [ ] If showing different font, formatting may have issues

#### **Font Size Check**
- [ ] Select all text (Ctrl+A)
- [ ] Check font size → should be **"12 pt"**
- [ ] If different, notify developer

#### **Line Spacing Check**
- [ ] Select all text (Ctrl+A)
- [ ] Format menu → Paragraph → Line spacing → should be **"1.5 lines"**

### **Check Content Sections**

- [ ] **Title Section**: "RWANDA TECHNICAL BOARD SESSION PLAN"
- [ ] **Header Info**: Sector, Trade, Module, Trainer, Date visible
- [ ] **Learning Outcomes**: Present with correct content
- [ ] **Facilitation Techniques**: Present with correct content
- [ ] **Introduction Section**: 
  - [ ] Has "Trainer's Activities" subsection
  - [ ] Has "Learner's Activities" subsection
  - [ ] Bullet points properly formatted
- [ ] **Development Section**:
  - [ ] Has "Main Content" with topic
  - [ ] Has "Trainer's Activities"
  - [ ] Has "Learner's Activities"
- [ ] **Conclusion Section**: Present
- [ ] **Assessment Section**: 
  - [ ] Has assessment methods
  - [ ] Matches facilitation technique
- [ ] **Evaluation Section**: Present
- [ ] **Resources Section**: 
  - [ ] Lists resources provided
  - [ ] Properly formatted as bullet list
- [ ] **References Section**:
  - [ ] Has multiple references
  - [ ] References in **APA format**
  - [ ] Each reference numbered (1. 2. 3. etc.)
- [ ] **Appendices & Reflection**: Present

### **Visual Appearance**

- [ ] Document looks **professional**
- [ ] No weird formatting or symbols
- [ ] Proper spacing between sections
- [ ] Tables (if any) centered
- [ ] Text not running off edges
- [ ] Overall appearance matches **official RTB template**

**Document Quality**: 
- [ ] ✓ EXCELLENT - Ready to use
- [ ] ⚠️ NEEDS IMPROVEMENT - Some issues (See Troubleshooting)

---

## **PHASE 9: TEST DIFFERENT FACILITATION TECHNIQUES** ⏱️ Estimated: 15 minutes

Create 6 test documents with different facilitation techniques:

### **Test 1: Trainer-guided instruction**
- [ ] Create session plan
- [ ] Set Facilitation: **"Trainer-guided instruction"**
- [ ] Download document
- [ ] Verify content appropriate for this technique
- [ ] ✓ PASSED

### **Test 2: Hands-on/Practical exercises**
- [ ] Create session plan
- [ ] Set Facilitation: **"Hands-on/Practical exercises"**
- [ ] Download document
- [ ] Verify content includes safety/practical aspects
- [ ] ✓ PASSED

### **Test 3: Group work/Collaborative learning**
- [ ] Create session plan
- [ ] Set Facilitation: **"Group work/Collaborative learning"**
- [ ] Download document
- [ ] Verify content mentions groups/collaboration
- [ ] ✓ PASSED

### **Test 4: Simulation/Role-play**
- [ ] Create session plan
- [ ] Set Facilitation: **"Simulation/Role-play"**
- [ ] Download document
- [ ] Verify content mentions scenarios/roles
- [ ] ✓ PASSED

### **Test 5: Discussion/Brainstorming**
- [ ] Create session plan
- [ ] Set Facilitation: **"Discussion/Brainstorming"**
- [ ] Download document
- [ ] Verify content encourages discussion
- [ ] ✓ PASSED

### **Test 6: Project-based learning**
- [ ] Create session plan
- [ ] Set Facilitation: **"Project-based learning"**
- [ ] Download document
- [ ] Verify content mentions projects
- [ ] ✓ PASSED

**All Techniques Tested**: ✓ PASSED

---

## **PHASE 10: FINAL VERIFICATION** ⏱️ Estimated: 5 minutes

### **Master Checklist**

- [ ] Both new Python files uploaded to PythonAnywhere
- [ ] main.py updated with correct import statement
- [ ] Web app reloaded successfully
- [ ] No errors in error log
- [ ] Can login and use app normally
- [ ] Downloaded session plans open without errors
- [ ] Documents have correct formatting (Book Antiqua, 12pt, 1.5 spacing)
- [ ] Introduction sections have trainer/learner activities separated
- [ ] Development sections are topic-relevant
- [ ] Assessment methods match facilitation technique
- [ ] References are present and APA-formatted
- [ ] Documents look professional and polished
- [ ] No text overflow or formatting issues
- [ ] Structure matches official RTB templates
- [ ] All 6 facilitation techniques generate appropriate content

**Final Status**: ✓ **READY FOR PRODUCTION**

---

## **PHASE 11: ROLLBACK PLAN (If Needed)** ⏱️ Keep for reference

**Only use if something breaks!**

- [ ] Go to Files tab → main.py
- [ ] Select all content (Ctrl+A) → Delete
- [ ] Open your `main.py.backup` file
- [ ] Copy all content
- [ ] Paste into PythonAnywhere main.py editor
- [ ] Click Save
- [ ] Go to Web tab → Click Reload
- [ ] Check error log for any issues
- [ ] Test app functionality

**Rollback completed**: ________________ (if needed)

---

## **COMPLETION SUMMARY**

### **Update Information**

| Item | Value |
|------|-------|
| **Update Date** | ________________ |
| **Completion Time** | ________________ |
| **Total Duration** | ________________ |
| **Issues Encountered** | ________________ |
| **Final Status** | ✓ SUCCESS |

### **File Verification**

- [ ] smart_content_generator.py - Uploaded ✓
- [ ] rtb_template_filler_100_percent.py - Uploaded ✓
- [ ] main.py - Updated ✓
- [ ] Backup files - Stored safely ✓

### **Testing Results**

- [ ] Basic functionality - PASSED ✓
- [ ] Document generation - PASSED ✓
- [ ] Formatting verification - PASSED ✓
- [ ] All techniques - PASSED ✓
- [ ] Visual appearance - PASSED ✓

### **Next Steps**

- [ ] Notify your users that documents are improved
- [ ] Have users create test documents
- [ ] Monitor error log for 48 hours
- [ ] Gather feedback on new format
- [ ] Archive this checklist with date

---

## **SIGN-OFF**

**Update Completed By**: ________________

**Date**: ________________

**Time**: ________________

**Verified By**: ________________

**Comments/Notes**:
```
_________________________________________________________________

_________________________________________________________________

_________________________________________________________________
```

---

**Congratulations! Your PythonAnywhere backend is now 100% RTB-compliant!** 🎉

Session plans generated will now:
- ✓ Look exactly like official RTB templates
- ✓ Have intelligent, topic-relevant content
- ✓ Follow professional formatting standards
- ✓ Include proper APA references
- ✓ Be ready to print or distribute immediately

**For support, refer to**: `PYTHONANYWHERE_UPDATE_GUIDE_RTB_100_PERCENT.md`
