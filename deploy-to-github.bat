@echo off
echo 🚀 Deploying RTB Document Planner to GitHub Pages...
echo.

REM Navigate to project directory
cd /d "c:\Users\PC\Music\Scheme of work and session plan planner"

REM Add all changes
echo 📁 Adding all changes...
git add .

REM Commit with timestamp
echo 💾 Committing changes...
git commit -m "Fix authentication and DOCX generation - Deploy %date% %time%"

REM Push to main branch
echo 🌐 Pushing to GitHub Pages...
git push origin main

echo.
echo ✅ Deployment complete!
echo 🔗 Your site will be available at: https://tuyisingize750.github.io/your-repo-name
echo.
pause