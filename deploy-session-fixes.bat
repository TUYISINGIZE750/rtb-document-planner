@echo off
echo ========================================
echo RTB Document Planner - Session Fixes
echo ========================================
echo.
echo This will deploy:
echo 1. Fixed DOCX generation (document_generator.py)
echo 2. Session management fixes (auth-fixed.js, index.html, wizard.html, scheme-wizard.html)
echo 3. Prevent "undefined" user display
echo 4. Block back button after logout
echo.
pause

echo.
echo [1/4] Adding files to git...
git add backend/document_generator.py
git add frontend/auth-fixed.js
git add frontend/index.html
git add frontend/wizard.html
git add frontend/scheme-wizard.html
git add URGENT_FIX_DEPLOYED.md
git add SESSION_MANAGEMENT_FIXED.md

echo.
echo [2/4] Committing changes...
git commit -m "Fix: DOCX corruption + Session management (undefined user & back button)"

echo.
echo [3/4] Pushing to GitHub...
git push origin main

echo.
echo [4/4] Deployment Status
echo ========================================
echo ✅ Frontend: Pushed to GitHub
echo    Will be live in 2-3 minutes at:
echo    https://tuyisingize750.github.io/rtb-document-planner/
echo.
echo ⚠️  Backend: Manual upload required
echo    1. Go to: https://www.pythonanywhere.com/user/leonardus437/files/
echo    2. Upload: backend/document_generator.py
echo    3. Reload: https://www.pythonanywhere.com/user/leonardus437/webapps/
echo.
echo ========================================
echo.
echo Test after deployment:
echo 1. Login with: +250796014803
echo 2. Check user name displays correctly
echo 3. Create and download a session plan
echo 4. Logout and try back button
echo.
pause
