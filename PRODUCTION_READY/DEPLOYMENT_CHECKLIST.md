# 📋 DEPLOYMENT CHECKLIST

## PRE-DEPLOYMENT

- [ ] I have access to PythonAnywhere account
- [ ] I can see `/home/leonardus437/` directory
- [ ] I have all 4 files ready to upload:
  - [ ] document_generator.py
  - [ ] rtb_template_filler.py
  - [ ] rtb_session_plan_template.docx
  - [ ] rtb_scheme_template.docx

## DEPLOYMENT STEPS

### Phase 1: Backup (Optional but Recommended)
- [ ] Download current `document_generator.py` as backup
- [ ] Note current file sizes for comparison

### Phase 2: Upload Files
- [ ] Logged into PythonAnywhere
- [ ] Navigated to `/home/leonardus437/`
- [ ] Uploaded `document_generator.py` (replaced existing)
- [ ] Uploaded `rtb_template_filler.py` (new file)
- [ ] Uploaded `rtb_session_plan_template.docx` (new file)
- [ ] Uploaded `rtb_scheme_template.docx` (new file)

### Phase 3: Cleanup
- [ ] Deleted `rtb_document_generator.py` (if it existed)
- [ ] Verified 6 files total in directory

### Phase 4: Reload
- [ ] Went to Web tab
- [ ] Clicked green "Reload" button
- [ ] Waited 30 seconds
- [ ] No errors shown

## POST-DEPLOYMENT TESTING

### Test 1: API Health Check
- [ ] Visited https://leonardus437.pythonanywhere.com/
- [ ] Saw `{"status": "online"}`
- [ ] Response time < 2 seconds

### Test 2: Teacher Login
- [ ] Went to https://tuyisingize750.github.io/rtb-document-planner/
- [ ] Clicked "Teacher Login"
- [ ] Logged in successfully
- [ ] Dashboard loaded correctly

### Test 3: Session Plan Generation
- [ ] Clicked "Create Session Plan"
- [ ] Filled all required fields
- [ ] Clicked "Generate Session Plan"
- [ ] Document downloaded successfully
- [ ] Opened .docx file
- [ ] Verified RTB format:
  - [ ] Times New Roman font, 12pt
  - [ ] Bold labels present
  - [ ] Table structure correct (23 rows, 6 columns)
  - [ ] All my data filled in correctly
  - [ ] Looks EXACTLY like RTB template

### Test 4: Scheme of Work Generation
- [ ] Clicked "Create Scheme of Work"
- [ ] Filled all required fields (all 3 terms)
- [ ] Clicked "Generate Scheme"
- [ ] Document downloaded successfully
- [ ] Opened .docx file
- [ ] Verified RTB format:
  - [ ] Bookman Old Style font
  - [ ] Tan/beige header colors (C4BC96)
  - [ ] Light tan sub-headers (DDD9C3)
  - [ ] 3 tables (one per term)
  - [ ] All my data filled in correctly
  - [ ] Looks EXACTLY like RTB template

### Test 5: Subscription Modal (Free User)
- [ ] Created 2 session plans (used up free limit)
- [ ] Tried to create 3rd session plan
- [ ] Subscription modal appeared
- [ ] Modal shows:
  - [ ] 7 subscription plans
  - [ ] Prices (36 RWF to 5,200 RWF)
  - [ ] Payment instructions
  - [ ] Mobile money: +250789751597
  - [ ] Name: Leonard TUYISINGIZE
  - [ ] Professional design

### Test 6: Premium User Experience
- [ ] Logged in as admin
- [ ] Upgraded test user to premium
- [ ] Logged in as premium user
- [ ] Verified:
  - [ ] Upgrade card is HIDDEN
  - [ ] Can create unlimited documents
  - [ ] No subscription prompts

### Test 7: Error Handling
- [ ] Checked PythonAnywhere error log
- [ ] No Python errors present
- [ ] No import errors
- [ ] No file not found errors

## VERIFICATION

### Document Quality Check
Compare downloaded document with original RTB template:
- [ ] Header format matches
- [ ] Table structure identical
- [ ] Font and sizes correct
- [ ] Colors match (if any)
- [ ] Borders and spacing correct
- [ ] Cell merging (rowspan/colspan) preserved

### User Experience Check
- [ ] Free users see download limits
- [ ] Free users see upgrade card
- [ ] Premium users don't see upgrade card
- [ ] Subscription modal is user-friendly
- [ ] Payment instructions are clear
- [ ] No broken links or buttons

### Performance Check
- [ ] Document generation < 5 seconds
- [ ] Download starts immediately
- [ ] No timeout errors
- [ ] API responds quickly

## FINAL SIGN-OFF

- [ ] All tests passed
- [ ] Documents match RTB format EXACTLY
- [ ] Subscription system works correctly
- [ ] No errors in logs
- [ ] System is production-ready

## ROLLBACK PLAN (If Needed)

If something goes wrong:
1. [ ] Re-upload backup of old `document_generator.py`
2. [ ] Delete new files (rtb_template_filler.py, templates)
3. [ ] Reload web app
4. [ ] Verify old system works
5. [ ] Contact support for help

---

## ✅ DEPLOYMENT COMPLETE

**Date:** _______________
**Time:** _______________
**Deployed By:** _______________
**Status:** _______________

**Notes:**
_________________________________________________
_________________________________________________
_________________________________________________

---

**Next Steps After Successful Deployment:**
1. Monitor error logs for 24 hours
2. Collect user feedback
3. Test with real teachers
4. Document any issues
5. Plan next improvements

**Congratulations! Your RTB Document Planner is now live with official RTB templates! 🎉**
