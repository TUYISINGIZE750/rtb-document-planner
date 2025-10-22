@echo off
echo ========================================
echo TESTING DEPLOYED RTB DOCUMENT PLANNER
echo ========================================
echo.

echo [1/5] Testing Backend API...
curl -s https://leonardus437.pythonanywhere.com/ | findstr "version"
echo.

echo [2/5] Testing Frontend Site...
curl -s -I https://tuyisingize750.github.io/rtb-document-planner/ | findstr "200"
echo.

echo [3/5] Testing Login Page...
curl -s -I https://tuyisingize750.github.io/rtb-document-planner/login.html | findstr "200"
echo.

echo [4/5] Testing Dashboard Page...
curl -s -I https://tuyisingize750.github.io/rtb-document-planner/dashboard.html | findstr "200"
echo.

echo [5/5] Testing Wizard Page...
curl -s -I https://tuyisingize750.github.io/rtb-document-planner/wizard-fixed.html | findstr "200"
echo.

echo ========================================
echo DEPLOYMENT TEST COMPLETE
echo ========================================
echo.
echo NEXT STEPS:
echo 1. Visit: https://tuyisingize750.github.io/rtb-document-planner/
echo 2. Login with: +250789751597 / admin123
echo 3. Check if name shows correctly (not "Undefined")
echo 4. Try creating a session plan
echo.
pause