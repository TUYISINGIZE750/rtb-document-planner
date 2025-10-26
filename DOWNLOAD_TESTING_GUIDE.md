# Download Functionality Testing Guide

## Overview

After deploying the fixed `main.py` with improved download endpoints, follow these steps to verify that session plans and schemes of work download correctly.

---

## Pre-Testing Checklist

- [ ] Updated `main.py` with new download endpoints
- [ ] Uploaded to PythonAnywhere
- [ ] Reloaded the web app
- [ ] Flask version is 3.0.0 (see requirements.txt)
- [ ] Template files exist:
  - [ ] `rtb_session_plan_template.docx`
  - [ ] `rtb_scheme_template.docx`
- [ ] `rtb_template_filler_exact.py` is uploaded

---

## Test 1: Session Plan Download

### Steps:

1. **Navigate to Frontend**
   - Go to: https://rtb-document-planner.pages.dev
   - Click "Teacher Login"
   - Use a valid teacher phone number

2. **Create Session Plan**
   - Click "Create Session Plan"
   - Fill in all required fields:
     - Sector: "ICT & MULTIMEDIA"
     - Trade: "Software Development"
     - RQF Level: "Level 4"
     - Teacher Name: "John Doe"
     - Module Code: "CSA-M01"
     - Term: "Term 1"
     - Week: "Week 4"
     - Date: (pick any date)
     - Class Name: "L4CSA-A"
     - Trainees: "25"
     - Duration: "40" minutes
     - Topic: "Variables and Data Types"
     - Learning Outcomes: "Students will understand variables"
     - Indicative Contents: "• Variables\n• Data types"

3. **Click Generate & Download**
   - Click "Generate Session Plan" button
   - You should see a loading spinner
   - After 2-3 seconds, file should download automatically

4. **Verify Download**
   - Check browser downloads folder (usually: `C:\Users\[Your Name]\Downloads`)
   - Look for file named: `RTB_Session_Plan_[ID]_[TIMESTAMP].docx`
   - File should be ~100+ KB

5. **Open File**
   - Double-click to open in Microsoft Word
   - File should open without errors
   - Check:
     - [ ] Title: "RWANDA TECHNICAL BOARD (RTB) SESSION PLAN"
     - [ ] Sector field populated
     - [ ] Trade field populated
     - [ ] All form data appears in document
     - [ ] Font is Book Antiqua, 12pt (check in Word: Home → Font)
     - [ ] Line spacing is 1.5 (check in Word: Home → Line Spacing)
     - [ ] Bibliography section with APA references

---

## Test 2: Scheme of Work Download

### Steps:

1. **Navigate to Dashboard**
   - Go back to: https://rtb-document-planner.pages.dev
   - Click "Create Scheme of Work"

2. **Create Scheme**
   - Fill in all required fields:
     - Province: "Kigali"
     - District: "Kicukiro"
     - School: "Hope School"
     - Sector: "ICT"
     - Qualification Title: "Software Developer"
     - RQF Level: "Level 4"
     - Module Code: "CSA-M01"
     - School Year: "2024/2025"
     - Trainer Name: "John Doe"
     - Class Name: "L4CSA-A"
     - For each term (1, 2, 3):
       - Weeks: "Week 1-5"
       - Learning Outcomes: "Students will..."
       - Contents: "• Topic 1\n• Topic 2"
       - Duration: "60"
       - Learning Place: "Classroom & Lab"

3. **Click Generate & Download**
   - Click "Generate Scheme of Work" button
   - You should see loading spinner
   - After 2-3 seconds, file should download

4. **Verify Download**
   - Check downloads folder
   - Look for: `RTB_Scheme_of_Work_[ID]_[TIMESTAMP].docx`
   - File should be ~70+ KB

5. **Open File**
   - Double-click to open in Word
   - Check:
     - [ ] Title: "SCHEME OF WORK"
     - [ ] All school information present
     - [ ] Three term sections (Term 1, 2, 3)
     - [ ] All data correctly populated
     - [ ] Proper formatting

---

## Test 3: Network Monitoring

### Check Network Traffic:

1. **Open Browser Developer Tools**
   - Press F12
   - Go to "Network" tab

2. **Create and Download Document**
   - Refresh page
   - Create session plan
   - Click download
   - Watch network tab for activity

3. **Verify Request Success**
   - Look for request: `/session-plans/[ID]/download`
   - Should show:
     - Status: **200** (success)
     - Type: `document` (DOCX file)
     - Size: ~100+ KB
     - Response Headers should include:
       ```
       Content-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document
       Content-Disposition: attachment; filename="RTB_Session_Plan_...docx"
       Content-Length: [size]
       ```

---

## Test 4: Error Handling

### Test Missing Parameters:

1. **Try Direct Download URL**
   - Go to: `https://leonardus437.pythonanywhere.com/session-plans/1/download`
   - Should get error: `"Phone parameter required"` (status 400)
   - This is expected - phone is required

2. **Try Invalid Plan ID**
   - Go to: `https://leonardus437.pythonanywhere.com/session-plans/99999/download?phone=%2B250789123456`
   - Should get error: `"Session plan not found"` (status 404)
   - This is expected behavior

3. **Try Invalid Phone**
   - Create and download document
   - This should work if user exists

---

## Test 5: PythonAnywhere Logs

### Check Server Logs:

1. **Access PythonAnywhere**
   - Go to: https://www.pythonanywhere.com
   - Click "Web" tab

2. **View Error Log**
   - Click "Error log"
   - Should see messages like:
     - `Sending file: /tmp/... as RTB_Session_Plan_...docx`
     - `Cleaned up temp file: /tmp/...`
   - **Should NOT see any errors or exceptions**

3. **View Console**
   - Click "Bash console"
   - Optional: Run `tail -f /var/log/pythonanywhere.com/...log`
   - Watch for any Python errors

---

## Test 6: File Integrity

### Verify Downloaded File:

1. **Check File Properties**
   - Right-click downloaded file
   - Properties
   - Should show:
     - Type: "Microsoft Word Document"
     - Size: 95+ KB

2. **Open in Word**
   - Double-click file
   - Should open without:
     - Repair dialog
     - "File is corrupted" warnings
     - Missing fonts warnings

3. **Check Content**
   - Verify all form data is present
   - No placeholder text like `[PLACEHOLDER]` or `None`
   - All sections have content

4. **Check Formatting**
   - Font: Select all (Ctrl+A) → Check Home → Font dropdown → "Book Antiqua"
   - Size: Should show "12"
   - Spacing: Home → Line Spacing → "1.5 lines"
   - Tables should be properly centered

---

## Common Issues & Solutions

### Issue: Download Starts Then Fails

**Solution:**
1. Check browser console (F12 → Console)
2. Look for JavaScript errors
3. Check Network tab for failed request
4. Check PythonAnywhere error log

**Most Common Causes:**
- Backend not running (reload in PythonAnywhere)
- File permissions issue
- Temp directory full

### Issue: File Downloaded But Won't Open

**Solution:**
1. Check file size (should be >95 KB)
2. Right-click → Open with Word → Repair
3. Check if file is actually a DOCX (open as zip)

**Most Common Causes:**
- Partial download (incomplete)
- Wrong MIME type
- Temp file deleted too early

### Issue: File Opens But Data is Missing

**Solution:**
1. Check if all form fields were filled
2. Verify template files exist
3. Check `rtb_template_filler_exact.py` was uploaded

**Most Common Causes:**
- Form validation passed but data missing
- Template file path wrong
- Database query didn't return data

### Issue: Download Hangs (Spinning)

**Solution:**
1. Wait 5-10 seconds (document generation takes 2-3 sec)
2. Check Network tab (F12) for stuck requests
3. Reload PythonAnywhere web app

**Most Common Causes:**
- Server overloaded
- Document generation took too long
- Network timeout

---

## Success Checklist

✅ **All tests passed when:**

- [ ] Session plan downloads automatically after clicking generate
- [ ] Scheme of work downloads automatically after clicking generate
- [ ] Downloaded files open in Microsoft Word without errors
- [ ] All form data appears in the document
- [ ] Font is Book Antiqua, 12pt throughout
- [ ] Line spacing is 1.5 lines
- [ ] Bibliography section exists with APA references
- [ ] Network requests show status 200
- [ ] No errors in PythonAnywhere error log
- [ ] No JavaScript errors in browser console
- [ ] File names match pattern: `RTB_Session_Plan_[ID]_[TIMESTAMP].docx`
- [ ] File sizes are correct (100+ KB for session plan, 70+ KB for scheme)

---

## Performance Benchmarks

Expected times:

| Operation | Expected Time | Max Acceptable |
|-----------|---------------|----------------|
| Form submission | <1 second | 2 seconds |
| Document generation | 2-3 seconds | 5 seconds |
| File download | <1 second | 3 seconds |
| Total time | 3-4 seconds | 8 seconds |

If slower, check:
- PythonAnywhere CPU usage
- Network speed
- System resources

---

## Deployment Verification

After all tests pass:

1. **Document the results**
   - Take screenshots of successful downloads
   - Note any minor issues found

2. **Ready for Production**
   - All tests passed ✅
   - No errors in logs ✅
   - Download working reliably ✅

3. **Go Live**
   - Announce to users
   - Monitor error logs for 24 hours
   - Be ready to troubleshoot if issues arise

---

## Support Contact

If downloads still don't work after all fixes:

1. Check PythonAnywhere error log for specific error message
2. Enable debug mode and check logs
3. Try creating document manually via API
4. Verify all files are uploaded correctly
5. Check Flask version compatibility

**Debug Command** (PythonAnywhere Bash):
```bash
cd /home/leonardus437/rtb-document-planner/
python3 -c "from main import app; app.run(debug=True)"
```

---

## Success Message

When everything works:

```
✅ Session plans download correctly
✅ Schemes of work download correctly
✅ Files open in Word without errors
✅ All data is preserved and formatted correctly
✅ Performance is acceptable
✅ System is production-ready
🎉 DEPLOYMENT SUCCESSFUL!
```

