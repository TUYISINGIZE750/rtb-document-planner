@echo off
cd /d "c:\Users\PC\Music\Scheme of work and session plan planner"
git add -A
git status
git commit -m "Deploy: Enhanced document formatting, smart references, and admin panel modernization - Session plan improvements with Book Antiqua 12pt font, 1.5 line spacing, proper section structure, and intelligent APA-formatted reference generation based on content"
git log --oneline -3
pause
