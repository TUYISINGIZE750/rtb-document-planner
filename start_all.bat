@echo off
echo ========================================
echo RTB Document Planner - Starting All Services
echo ========================================

echo.
echo 1. Initializing Database...
cd backend
python init_db.py
if %errorlevel% neq 0 (
    echo ERROR: Database initialization failed!
    pause
    exit /b 1
)

echo.
echo 2. Starting Backend Server (Port 8002)...
start "RTB Backend" cmd /k "python -m uvicorn main:app --host 0.0.0.0 --port 8002 --reload"

echo.
echo 3. Waiting for backend to start...
timeout /t 3 /nobreak >nul

echo.
echo 4. Starting Frontend Server (Port 5173)...
cd ..\frontend
start "RTB Frontend" cmd /k "python -m http.server 5173"

echo.
echo 5. Waiting for frontend to start...
timeout /t 2 /nobreak >nul

echo.
echo ========================================
echo ✅ RTB Document Planner Started!
echo ========================================
echo.
echo 🌐 Frontend: http://localhost:5173
echo 🔧 Backend API: http://localhost:8002/docs
echo 💾 Health Check: http://localhost:8002/health
echo.
echo Press any key to open the application...
pause >nul

start http://localhost:5173