@echo off
echo ========================================
echo Starting RTB Frontend Server
echo ========================================

cd frontend

echo.
echo Starting frontend on port 5173...
python -m http.server 5173

pause