@echo off
echo ========================================
echo RTB Document Planner - Fixed System Startup
echo ========================================

echo.
echo 1. Fixing database initialization...
python fix_database.py
if errorlevel 1 (
    echo Database fix failed!
    pause
    exit /b 1
)

echo.
echo 2. Starting backend server...
cd backend
start "RTB Backend" cmd /k "python startup.py"
cd ..

echo.
echo 3. Waiting for backend to start...
timeout /t 5 /nobreak > nul

echo.
echo 4. Testing system...
python test_session_fix.py

echo.
echo 5. Starting frontend...
cd frontend
start "RTB Frontend" cmd /k "python -m http.server 5173"
cd ..

echo.
echo 6. Opening application...
timeout /t 3 /nobreak > nul
start http://localhost:5173

echo.
echo ========================================
echo System started successfully!
echo ========================================
echo Backend: http://localhost:8000
echo Frontend: http://localhost:5173
echo Admin Login: +250789751597 / admin123
echo ========================================
pause