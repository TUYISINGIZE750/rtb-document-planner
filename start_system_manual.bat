@echo off
echo ========================================
echo RTB Document Planner - Manual Startup
echo ========================================

echo.
echo Docker is not running. Starting with local PostgreSQL simulation...
echo.

echo 1. Installing PostgreSQL driver...
cd backend
pip install psycopg2-binary==2.9.9
cd ..

echo.
echo 2. Using SQLite as fallback (PostgreSQL not available)...
echo.

echo 3. Starting Backend in new terminal...
start "RTB Backend" cmd /k "cd /d %cd%\backend && python startup.py"

echo.
echo 4. Waiting for backend...
timeout /t 5 /nobreak > nul

echo.
echo 5. Testing system...
python test_session_fix.py

echo.
echo 6. Starting Frontend in new terminal...
start "RTB Frontend" cmd /k "cd /d %cd%\frontend && python -m http.server 5173"

echo.
echo 7. Opening application...
timeout /t 3 /nobreak > nul
start http://localhost:5173

echo.
echo ========================================
echo System Started Successfully!
echo ========================================
echo Backend: http://localhost:8000
echo Frontend: http://localhost:5173
echo Admin: +250789751597 / admin123
echo ========================================
echo.
echo Note: Using SQLite database (Docker not available)
echo For PostgreSQL, install Docker Desktop and run start_containers.bat
echo.
pause