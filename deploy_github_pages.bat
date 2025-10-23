@echo off
echo ========================================
echo RTB Document Planner - GitHub Pages Deploy
echo ========================================
echo.

cd /d "%~dp0"

echo [1/5] Checking Git status...
git status
echo.

echo [2/5] Adding all files...
git add .
echo.

echo [3/5] Committing changes...
git commit -m "Deploy: Professional RTB document generator with official template structure"
echo.

echo [4/5] Pushing to GitHub...
git push origin main
echo.

echo [5/5] Deployment complete!
echo.
echo Your site will be available at:
echo https://tuyisingize750.github.io/Scheme-of-work-and-session-plan-planner/
echo.
echo Note: It may take 1-2 minutes for changes to appear.
echo.
pause
