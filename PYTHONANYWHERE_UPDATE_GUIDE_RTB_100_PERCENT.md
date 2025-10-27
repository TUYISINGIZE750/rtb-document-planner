# PythonAnywhere Backend Update Guide
## RTB 100% Compliance Solution Deployment

---

## **Overview**

You will be adding two new Python files to your existing PythonAnywhere backend while keeping everything else working. This is a safe, non-breaking update.

**What changes**: 
- ✅ Session plan generation improves (100% RTB-compliant)
- ✅ Scheme generation stays the same (no breaking changes)
- ✅ Everything else unchanged

---

## **Part 1: Pre-Update Checklist** ✓

Before starting:
- [ ] You have access to your PythonAnywhere account
- [ ] You know your PythonAnywhere username
- [ ] You have the two new files ready:
  - `rtb_template_filler_100_percent.py`
  - `smart_content_generator.py`
- [ ] You have the two files locally on your computer
- [ ] You have a backup of your current `main.py` (we'll create this)

---

## **Part 2: Backup Your Current System**

### **Step 1: Download Current main.py**

1. Log in to [www.pythonanywhere.com](https://www.pythonanywhere.com)
2. Go to **Files** tab
3. Navigate to your Flask app directory (usually `/home/yourusername/`)
4. Find and download `main.py`
5. Save it as `main.py.backup` on your computer

### **Step 2: Download All Current Backend Files**

In PythonAnywhere Files browser, download these files to your computer:
```
main.py
document_generator.py
models.py (if exists)
requirements.txt (if exists)
```

Store them in a folder called `PythonAnywhere_Backup_[DATE]`

---

## **Part 3: Upload New Files to PythonAnywhere**

### **Method A: Using PythonAnywhere Web Interface (Easiest)**

#### **Step 1: Locate Your Backend Directory**

1. Login to PythonAnywhere
2. Click **Files** tab
3. Navigate to your Flask app directory (should be at `/home/yourusername/` or similar)
4. Note the exact path shown (e.g., `/home/tuyisingize750/`)

#### **Step 2: Upload rtb_template_filler_100_percent.py**

1. In the Files browser, click **Upload a file**
2. Choose `rtb_template_filler_100_percent.py` from your computer
3. Click **Upload**
4. Verify it appears in the file list

#### **Step 3: Upload smart_content_generator.py**

1. Click **Upload a file** again
2. Choose `smart_content_generator.py`
3. Click **Upload**
4. Verify it appears in the file list

### **Method B: Using Console (If Upload Doesn't Work)**

1. In PythonAnywhere, go to **Consoles** tab
2. Open a **Bash** console
3. Navigate to your app directory:
   ```bash
   cd /home/yourusername/
   ```

4. If you're on Windows and can't use scp, use this approach:
   - Use the Files upload interface (Method A) instead
   - OR copy the file content and create it in PythonAnywhere:

5. Create the file using bash:
   ```bash
   cat > smart_content_generator.py << 'EOF'
   [paste entire content of smart_content_generator.py here]
   EOF
   ```

---

## **Part 4: Update main.py**

### **Step 1: Open main.py in PythonAnywhere**

1. Go to **Files** tab
2. Click on `main.py` to open it in the editor
3. Look for the imports section (first 20-30 lines)

### **Step 2: Find These Lines**

Search for (Ctrl+F):
```python
from rtb_template_filler_exact import
```

You should find something like:
```python
from rtb_template_filler_exact import (
    fill_session_plan_template,
    fill_scheme_template,
    ...
)
```

### **Step 3: Replace the Import**

**BEFORE:**
```python
from rtb_template_filler_exact import (
    fill_session_plan_template,
    fill_scheme_template
)
```

**AFTER:**
```python
from rtb_template_filler_100_percent import fill_session_plan_template_100_percent as fill_session_plan_template
from rtb_template_filler_exact import fill_scheme_template
```

### **Step 4: Save the File**

- Click **Save** in the PythonAnywhere editor
- Verify it saved (should see a confirmation message)

---

## **Part 5: Reload Your Web App**

This is **CRITICAL** for the changes to take effect.

### **Step 1: Go to Web App Settings**

1. Click **Web** tab in PythonAnywhere
2. Find your Flask app in the list
3. Click on it to open settings

### **Step 2: Reload the App**

You should see a large **Reload** button at the top of the page.
- Click **Reload** 
- Wait for it to finish (usually 5-10 seconds)
- You should see: "Webapp reloaded at [time]"

### **Step 3: Verify the Reload**

After reloading, check the error log to ensure no errors:
1. Click the **Error log** link on the same Web page
2. Scroll to the bottom
3. Should NOT see any errors related to imports
4. If you see errors, copy them (we'll troubleshoot below)

---

## **Part 6: Test the Update**

### **Test 1: Quick Health Check**

1. Open your app URL in browser
2. Login to your app
3. Go to teacher dashboard
4. Verify normal functionality works

### **Test 2: Create and Download a Session Plan**

1. Create a new session plan with test data:
   - **Sector**: Information & Communication Technology
   - **Trade**: Software Development
   - **Module**: CS401 - Python Programming
   - **Topic**: Object-Oriented Programming
   - **Facilitation**: Trainer-guided instruction
   - **Duration**: 90
   - **Learning Outcomes**: Test outcome
   - **Resources**: Test resource

2. Complete the wizard
3. Download the document
4. Open it in Word

### **Test 3: Verify Document Quality**

Check these things in the downloaded document:

✅ **Font**: Should be "Book Antiqua" (select all text, check font name)
✅ **Size**: Should be 12pt (select all text, check size)
✅ **Spacing**: Should be 1.5 (Format → Paragraph → Line spacing)
✅ **Content**: Should have:
   - Introduction section with trainer/learner activities
   - Development section
   - Assessment section
   - References (APA format)
   - Professional formatting

✅ **Appearance**: Should look professional, no weird formatting

### **Test 4: Check with Different Facilitation Techniques**

Repeat Test 2 with different facilitation techniques:
- Trainer-guided instruction ✅
- Hands-on/Practical exercises ✅
- Group work/Collaborative learning ✅
- Simulation/Role-play ✅
- Discussion/Brainstorming ✅
- Project-based learning ✅

Each should generate different but appropriate activities.

---

## **Troubleshooting**

### **Issue: Reload button not found**

**Solution**: 
- Make sure you're in the **Web** tab (not Files or Consoles)
- Look for your app name in the list on the left
- Click your app name to see settings
- Reload button is at the top

### **Issue: "ModuleNotFoundError: No module named smart_content_generator"**

**Solution**:
1. Verify both files are uploaded to **same directory** as main.py
2. Check filenames are exactly:
   - `smart_content_generator.py` ✓
   - `rtb_template_filler_100_percent.py` ✓
3. Try uploading files again
4. Check error log for exact error message
5. Reload the app again

### **Issue: "SyntaxError" in one of the new files**

**Solution**:
1. Go to Files tab
2. Click the `.py` file to view it
3. Look at the error line number
4. Check for missing quotes, colons, parentheses
5. If you can't find it, re-download the file from the guide and re-upload

### **Issue: main.py says "ModuleNotFoundError: No module named rtb_template_filler_100_percent"**

**Solution**:
1. Check that `rtb_template_filler_100_percent.py` is uploaded
2. Verify it's in the same folder as `main.py`
3. Check the import line exactly matches:
   ```python
   from rtb_template_filler_100_percent import fill_session_plan_template_100_percent as fill_session_plan_template
   ```
4. Make sure there are no typos in the filename or import
5. Reload the app after uploading

### **Issue: Sessions plans download but are still using old format**

**Solution**:
1. **Hard refresh your browser**: Press `Ctrl+Shift+Delete` (or Cmd+Shift+Delete on Mac)
2. Wait 2-3 minutes for PythonAnywhere cache to clear
3. Try downloading again
4. If still old format, check in PythonAnywhere:
   - Go to Web tab
   - Click "Reload" again
   - Wait 30 seconds
   - Try downloading again

---

## **Part 7: Verify Everything Is Working**

### **Checklist - All Should Be YES:**

- [ ] Both new Python files uploaded to PythonAnywhere
- [ ] `main.py` updated with new import
- [ ] Web app reloaded successfully
- [ ] No errors in error log
- [ ] Can login and use app normally
- [ ] Downloaded session plan has correct formatting
- [ ] Font is Book Antiqua throughout
- [ ] Content has trainer/learner sections
- [ ] References are present and formatted
- [ ] Different facilitation techniques work

---

## **Part 8: Rollback Plan (If Needed)**

If something goes wrong, you can quickly revert:

### **Step 1: Restore main.py**

1. Go to **Files** tab in PythonAnywhere
2. Open `main.py` in editor
3. Select all (Ctrl+A)
4. Delete
5. Paste the content from `main.py.backup` you saved earlier
6. Click **Save**

### **Step 2: Reload**

1. Go to **Web** tab
2. Click **Reload**
3. App should work again with old system

### **Step 3: Check Error Log**

Verify no errors appear in error log.

---

## **Command Reference**

### **If Using Console/Terminal**

```bash
# Check files are in right place
ls -la /home/yourusername/

# Should show:
# main.py
# smart_content_generator.py
# rtb_template_filler_100_percent.py
# [other files]

# Check Python syntax of files
python3 -m py_compile smart_content_generator.py
python3 -m py_compile rtb_template_filler_100_percent.py

# Should say nothing if no errors
```

---

## **File Locations**

Your PythonAnywhere structure should look like:

```
/home/yourusername/
├── main.py (UPDATED ✓)
├── smart_content_generator.py (NEW ✓)
├── rtb_template_filler_100_percent.py (NEW ✓)
├── rtb_template_filler_exact.py (existing, unchanged)
├── document_generator.py (existing, unchanged)
├── models.py (existing, unchanged)
├── requirements.txt (existing, unchanged)
└── [other existing files...]
```

---

## **Testing Script (Optional)**

If you want to test locally first before uploading to PythonAnywhere:

Create `test_local.py`:

```python
from PRODUCTION_READY.backend.rtb_template_filler_100_percent import fill_session_plan_template_100_percent

test_data = {
    'sector': 'ICT',
    'trade': 'Software Development',
    'trainer_name': 'Test Trainer',
    'module_code_title': 'CS401',
    'rqf_level': 'Level 4',
    'week': '1',
    'term': '1',
    'date': '2025-10-26',
    'topic_of_session': 'Python Programming Basics',
    'duration': '90',
    'number_of_trainees': '25',
    'class_name': 'Class A',
    'learning_outcomes': 'Learn Python basics',
    'facilitation_techniques': 'Trainer-guided instruction',
    'indicative_contents': 'Variables, loops, functions',
    'resources': 'Python IDE, Laptops'
}

try:
    output = fill_session_plan_template_100_percent(test_data)
    print(f"✓ Document generated: {output}")
except Exception as e:
    print(f"✗ Error: {e}")
```

Run it:
```bash
python test_local.py
```

If it works locally, it will work on PythonAnywhere.

---

## **Support Checklist**

After completing all steps, save this information:

```
Date Updated: _______________
PythonAnywhere Username: _______________
Files Uploaded: ✓ smart_content_generator.py, ✓ rtb_template_filler_100_percent.py
main.py Updated: ✓ YES
App Reloaded: ✓ YES
Testing Passed: ✓ YES
First Test Download: [Save example]
```

---

## **Next Steps**

1. ✅ **Complete all steps above**
2. ✅ **Test thoroughly** - try different scenarios
3. ✅ **Notify users** that documents now have improved formatting
4. ✅ **Monitor** - check error log for first 48 hours
5. ✅ **Keep backups** - store the backup files you created

---

## **Important Notes**

⚠️ **DO NOT**:
- Delete `rtb_template_filler_exact.py` (still needed for schemes)
- Delete `document_generator.py` (still used)
- Change `requirements.txt` (no new dependencies needed)
- Share `main.py` credentials in error logs

✅ **DO**:
- Keep backups of all original files
- Test thoroughly before telling users
- Check error log after reload
- Have rollback plan ready
- Document what you changed

---

**Status**: Ready for Deployment
**Estimated Time**: 15-20 minutes
**Difficulty**: Easy (Copy-Paste)
**Risk Level**: Very Low (Can easily rollback)

---

**Questions? Refer to the troubleshooting section above or check the error log for specific error messages.**
