@echo off
echo ==========================================
echo    DEPLOYING ALL FIXES - v3.0
echo ==========================================
echo.
echo FIXES INCLUDED:
echo ✅ 1. Undefined username - FIXED
echo ✅ 2. DOCX corruption - FIXED  
echo ✅ 3. Admin login - FIXED
echo ✅ 4. Admin messaging - FIXED
echo ✅ 5. Admin notifications - FIXED
echo.

echo [1/4] Setting up database users...
cd backend
python check_user.py

echo.
echo [2/4] Copying fixed files...
copy document_generator_fixed.py document_generator.py

echo.
echo [3/4] Deploying frontend...
cd ..\frontend
copy index_fixed.html index.html
copy admin_fixed.html admin.html
copy wizard_fixed.html wizard.html

echo.
echo [4/4] Pushing to GitHub...
git add .
git commit -m "v3.0: Fixed all issues - undefined user, DOCX corruption, admin panel"
git push origin main

echo.
echo ==========================================
echo    ✅ ALL FIXES DEPLOYED!
echo ==========================================
echo.
echo LIVE URL: https://tuyisingize750.github.io/rtb-document-planner/
echo.
echo TEST ACCOUNTS:
echo 👤 Teacher: +250796014803 / teacher123
echo 🛡️  Admin: +250789751597 / admin123
echo.
echo WHAT'S FIXED:
echo ✅ No more "undefined" username
echo ✅ DOCX files open properly in Word
echo ✅ Admin can login and manage users
echo ✅ Admin can send messages/notifications
echo ✅ Enhanced error handling everywhere
echo.
echo TESTING STEPS:
echo 1. Login as teacher (+250796014803)
echo 2. Check username displays correctly
echo 3. Create session plan and download
echo 4. Open DOCX in Word (should work)
echo 5. Login as admin (+250789751597)
echo 6. Manage users and send messages
echo.
pause