@echo off
echo ========================================
echo DEPLOYING TO GITHUB PAGES
echo ========================================
echo.

cd /d "%~dp0"

echo Step 1: Adding all changes...
git add .

echo.
echo Step 2: Committing changes...
git commit -m "Updated with formatting fixes, facilitation techniques, and content improvements"

echo.
echo Step 3: Pushing to GitHub...
git push origin main

echo.
echo ========================================
echo DEPLOYMENT COMPLETE!
echo ========================================
echo.
echo GitHub Pages will auto-deploy in 1-2 minutes
echo Check: https://tuyisingize750.github.io/rtb-document-planner
echo.
pause
