@echo off
echo ========================================
echo  DEPLOYING LOCATION DROPDOWN FIX
echo ========================================
echo.

echo [1/5] Checking files...
if not exist "frontend\location-handler.js" (
    echo ERROR: location-handler.js not found!
    pause
    exit /b 1
)
if not exist "rwanda-locations-json-master\locations.json" (
    echo ERROR: locations.json not found!
    pause
    exit /b 1
)
echo ✓ All required files present

echo.
echo [2/5] Committing to Git...
git add frontend/location-handler.js
git add frontend/wizard.html
git add frontend/scheme-wizard.html
git add LOCATION_DROPDOWN_FIX.md
git commit -m "Fix: Implement cascading Rwanda location dropdowns"

echo.
echo [3/5] Pushing to GitHub...
git push origin main

echo.
echo [4/5] Testing locally...
start http://localhost:5173/wizard.html

echo.
echo [5/5] Deployment Instructions:
echo.
echo PYTHONANYWHERE DEPLOYMENT:
echo 1. Go to: https://www.pythonanywhere.com
echo 2. Open Bash console
echo 3. Run: cd /home/yourusername/mysite
echo 4. Run: git pull origin main
echo 5. Go to Web tab and click "Reload"
echo.
echo FILES TO VERIFY ON SERVER:
echo - frontend/location-handler.js
echo - frontend/wizard.html (updated)
echo - frontend/scheme-wizard.html (updated)
echo - rwanda-locations-json-master/locations.json
echo.
echo ========================================
echo  DEPLOYMENT COMPLETE!
echo ========================================
pause
