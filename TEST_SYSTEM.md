# 🧪 Complete System Test

## Test 1: Backend Health Check ✅

**Open this URL:**
```
https://leonardus437.pythonanywhere.com/
```

**Expected Result:**
```json
{"message": "RTB API", "status": "online", "version": "minimal"}
```

✅ If you see this → Backend is working!
❌ If you see error → Go back to Step 4, check error logs

---

## Test 2: Frontend Login ✅

**Open this URL:**
```
https://tuyisingize750.github.io/rtb-document-planner/
```

**Test Login:**
- Phone: `+250796014803`
- Password: `teacher123`

✅ If login works → Frontend is working!
❌ If error → Check browser console (F12)

---

## Test 3: Create Session Plan ✅

After logging in:

1. Click **"Create Session Plan"** button
2. Fill out the form:
   - Sector: `ICT & MULTIMEDIA`
   - Trade: `Software Development`
   - RQF Level: `Level 3`
   - Teacher Name: `Your Name`
   - Module: `TEST301: Test Module`
   - Term: `Term 1`
   - Week: `Week 1`
   - Date: (today's date)
   - Number of Trainees: `25`
   - Class Name: `L3SD-A`
   - Duration: `40`
   - Topic: `Test Session Plan`
   - Learning Outcomes: `Test learning outcomes`
   - Indicative Contents: `Test content`
   - Facilitation Technique: `Brainstorming`

3. Click **"Generate Session Plan"**

**Expected Result:**
- ✅ Success message appears
- ✅ Document downloads automatically
- ✅ File name: `RTB_Session_Plan_1.docx`

---

## Test 4: Verify Document Structure ✅

1. Open the downloaded `RTB_Session_Plan_1.docx` in Microsoft Word
2. Check for:
   - ✅ Table with multiple rows
   - ✅ Sector, Trade, Date in header
   - ✅ Trainer name, Term
   - ✅ Module, Week, Trainees
   - ✅ Learning outcome section
   - ✅ Topic of session
   - ✅ Introduction section
   - ✅ Development/Body section
   - ✅ Conclusion section
   - ✅ Assessment section
   - ✅ Evaluation section

**Does it look professional and structured?**
✅ YES → Perfect! System is working!
❌ NO → Check backend error logs

---

## Test 5: Create Scheme of Work ✅

1. Go back to home page
2. Click **"Create Scheme of Work"**
3. Fill out the form
4. Click **"Generate Scheme"**
5. Download should start
6. Open in Word and verify structure

---

## 🎉 Success Checklist

Mark each as you complete:

- [ ] Backend health check passes
- [ ] Frontend loads correctly
- [ ] Can login successfully
- [ ] Can create session plan
- [ ] Document downloads automatically
- [ ] Document opens in Word
- [ ] Document has proper RTB structure
- [ ] Can create scheme of work
- [ ] Scheme downloads and opens correctly

**All checked?** 🎊 **CONGRATULATIONS! Everything is working!**

---

## 🐛 If Something Doesn't Work

### Backend Issues:
1. Check: https://leonardus437.pythonanywhere.com/
2. If error, check PythonAnywhere error logs
3. Verify all 3 files uploaded
4. Re-run pip install command
5. Reload web app

### Frontend Issues:
1. Clear browser cache (Ctrl+Shift+Delete)
2. Try incognito/private window
3. Check browser console (F12) for errors

### Document Issues:
1. Check backend error logs
2. Verify `rtb_professional_generator.py` is uploaded
3. Verify `python-docx` is installed
4. Reload web app

---

## 📞 Need Help?

If you're stuck:
1. Note which test failed
2. Check error messages
3. Review the error logs
4. Try the troubleshooting steps above

**Most common issue:** Files not uploaded or dependencies not installed
**Solution:** Re-do Step 4 carefully
