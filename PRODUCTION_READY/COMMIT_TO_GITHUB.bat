@echo off
echo ========================================
echo COMMITTING RTB PLANNER UPDATES TO GITHUB
echo ========================================
echo.

cd /d "c:\Users\PC\Music\Scheme of work and session plan planner"

echo Step 1: Adding all changes...
git add .

echo.
echo Step 2: Committing changes...
git commit -m "feat: Add official RTB templates with Bookman Old Style 12pt formatting

- Added official_template_filler.py using templates from DOCS TO REFER TO folder
- Updated document_generator.py to use official templates
- Added DOCS TO REFER TO folder with SESSION PLAN.docx and CSAPA 301 Scheme of work.docx
- Applied Bookman Old Style 12pt font to all generated content
- Updated main_minimal.py with complete API endpoints (stats, users, limits, downloads)
- Fixed CORS configuration to allow all origins
- Improved session plan and scheme generation with exact template matching
- Added comprehensive testing files for verification"

echo.
echo Step 3: Pushing to GitHub...
git push origin main

echo.
echo ========================================
echo DONE! Changes pushed to GitHub
echo ========================================
echo.
echo Next steps:
echo 1. Go to PythonAnywhere Files tab
echo 2. Upload these files from PRODUCTION_READY/backend/:
echo    - main_minimal.py (rename to main.py)
echo    - document_generator.py
echo    - official_template_filler.py
echo    - DOCS TO REFER TO folder (entire folder)
echo 3. Click Reload button on Web tab
echo.
pause
