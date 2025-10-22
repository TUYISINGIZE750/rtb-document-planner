@echo off
echo ========================================
echo RTB Document Planner - GitHub Deployment
echo ========================================
echo.
echo This will push your RTB system to GitHub
echo Repository: https://github.com/TUYISINGIZE750/rtb-document-planner
echo.
pause

cd "C:\Users\PC\Music\Scheme of work and session plan planner\FINAL_DEPLOYMENT_TUYISINGIZE750"

echo Adding files to git...
git add .

echo Committing files...
git commit -m "Deploy RTB Document Planner - Complete System with Admin Dashboard"

echo Pushing to GitHub...
git push -u origin master

echo.
echo ========================================
echo DEPLOYMENT COMPLETE!
echo ========================================
echo.
echo Your site will be live at:
echo https://tuyisingize750.github.io/rtb-document-planner/
echo.
echo Admin Dashboard:
echo https://tuyisingize750.github.io/rtb-document-planner/admin.html
echo.
echo Admin Login: +250789751597 / admin123
echo.
echo Now enable GitHub Pages:
echo 1. Go to: https://github.com/TUYISINGIZE750/rtb-document-planner/settings/pages
echo 2. Source: Deploy from a branch
echo 3. Branch: master
echo 4. Click Save
echo.
pause