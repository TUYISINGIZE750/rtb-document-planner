@echo off
echo ========================================
echo   RTB Document Planner - GitHub Deploy
echo ========================================
echo.

echo [1/5] Checking Git status...
git status

echo.
echo [2/5] Adding all files...
git add .

echo.
echo [3/5] Committing changes...
git commit -m "Deploy complete teacher workflow with dashboard, wizards, and subscription system"

echo.
echo [4/5] Pushing to GitHub...
git push origin main

echo.
echo [5/5] Deployment complete!
echo.
echo ✅ Your RTB Document Planner is now deployed to GitHub Pages
echo 🌐 It will be available at: https://tuyisingize750.github.io/rtb-document-planner/
echo.
echo 📋 Teacher Features Deployed:
echo    - Teacher registration and login
echo    - Teacher dashboard with download tracking
echo    - Session plan wizard
echo    - Scheme of work wizard  
echo    - Subscription system with payment modal
echo    - Mobile responsive design
echo.
echo ⏱️  GitHub Pages may take 5-10 minutes to update
echo 🔗 Check deployment status at: https://github.com/tuyisingize750/rtb-document-planner/actions
echo.
pause