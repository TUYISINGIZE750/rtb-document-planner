# Testing Checklist - After Deployment

## 1. Backend API Test
- [ ] Visit: https://leonardus437.pythonanywhere.com/
- [ ] Should see: `{"message": "RTB Document Planner API"}`

## 2. Frontend Test
- [ ] Visit: https://rtb-document-planner.pages.dev
- [ ] Hard refresh: **Ctrl + Shift + R**
- [ ] Landing page loads with RTB colors (blue/gold)

## 3. Registration Test
- [ ] Click "Get Started" or "Teacher Login"
- [ ] Click "Register here"
- [ ] Fill form with test data
- [ ] Submit → Should see success message

## 4. Admin Login Test
- [ ] Click "Admin Login"
- [ ] Phone: `+250789751597`
- [ ] Password: `admin123`
- [ ] Should redirect to **admin.html** (NOT teacher-dashboard)

## 5. Activate User Test
- [ ] In admin panel, find test user
- [ ] Click "Activate"
- [ ] Status changes to "Active"

## 6. Teacher Login Test
- [ ] Logout from admin
- [ ] Login as test teacher
- [ ] Should redirect to **teacher-dashboard.html**
- [ ] See counts: 0/5 plans, 0/2 schemes

## 7. Session Plan Test
- [ ] Click "Create Session Plan"
- [ ] Fill all fields:
  - Module: `CSC101 - Programming`
  - Topic: `Python Variables`
  - Facilitation: `Hands-on practice`
  - Duration: `90`
- [ ] Click "Generate Session Plan"
- [ ] Should see success + download button
- [ ] Click "Download Session Plan"

## 8. Verify Session Plan Document
- [ ] Open downloaded .docx file
- [ ] Check structure matches RTB template
- [ ] Check Times New Roman 12pt font
- [ ] Check no excessive spacing
- [ ] Check objectives are SMART-formatted
- [ ] Check references section exists (4-5 sources)
- [ ] Check content is clean and well-organized

## 9. Scheme of Work Test
- [ ] Return to dashboard
- [ ] Click "Create Scheme of Work"
- [ ] Complete 8-step wizard:
  - Basic info
  - Term 1 (include Learning Place)
  - Term 2 (include Learning Place)
  - Term 3 (include Learning Place)
  - Review steps
  - Confirm
- [ ] Click "Generate Scheme of Work"
- [ ] Should see success + download button
- [ ] Click "Download Scheme of Work"

## 10. Verify Scheme Document
- [ ] Open downloaded .docx file
- [ ] Check 3 tables (Term 1, 2, 3)
- [ ] Check all terms filled correctly
- [ ] Check Learning Place appears for each term
- [ ] Check formatting matches RTB template
- [ ] Check no excessive spacing

## 11. Download Limits Test
- [ ] Create 5 session plans total
- [ ] Counter should show 5/5
- [ ] Try creating 6th → "Upgrade Required" button enabled
- [ ] Create 2 schemes total
- [ ] Counter should show 2/2
- [ ] Try creating 3rd → "Upgrade Required" button enabled

## 12. Different Facilitation Techniques Test
Create session plans with each technique:
- [ ] Trainer-guided
- [ ] Simulation
- [ ] Group work
- [ ] Hands-on practice
- [ ] Discussion
- [ ] Project-based

Verify each generates different content.

## 13. Browser Console Check
- [ ] Press F12
- [ ] Check Console tab
- [ ] Should see NO errors
- [ ] Should see NO CORS errors

## 14. Mobile Responsive Test
- [ ] Press F12 → Toggle device toolbar
- [ ] Test on mobile view
- [ ] All buttons clickable
- [ ] Forms usable

## Success Criteria

✅ All 14 tests pass
✅ Documents match RTB template structure
✅ No errors in browser console
✅ Download limits enforced
✅ Different techniques generate different content

## If Any Test Fails

1. Check browser console (F12) for errors
2. Check PythonAnywhere error logs
3. Verify all files uploaded correctly
4. Verify database initialized
5. Hard refresh browser (Ctrl + Shift + R)
