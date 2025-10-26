@echo off
REM RTB Document Planner - Startup Script
REM This script starts both backend and frontend servers

setlocal enabledelayedexpansion

echo.
echo ====================================================
echo RTB Document Planner - System Startup
echo ====================================================
echo.

REM Get the directory of this batch file
set SCRIPT_DIR=%~dp0

REM Change to backend directory
echo [1/4] Starting Backend Server...
echo.
cd /d "%SCRIPT_DIR%backend"

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Check if requirements are installed
pip show flask >nul 2>&1
if errorlevel 1 (
    echo Installing dependencies...
    pip install -r requirements.txt
    echo.
)

REM Initialize database if needed
if not exist "rtb_planner.db" (
    echo Initializing database...
    python init_db.py
    echo.
)

REM Start backend in a new window
echo Starting Flask backend on http://localhost:8000
start "RTB Backend" cmd /k python main.py

REM Give backend time to start
timeout /t 3 /nobreak

REM Start frontend in a new window
echo [2/4] Starting Frontend Server...
echo.
cd /d "%SCRIPT_DIR%frontend"
echo Starting HTTP server on http://localhost:5173
start "RTB Frontend" cmd /k python -m http.server 5173

REM Wait for servers
timeout /t 3 /nobreak

echo.
echo ====================================================
echo System Started Successfully!
echo ====================================================
echo.
echo Frontend: http://localhost:5173
echo Backend API: http://localhost:8000
echo API Docs: http://localhost:8000/docs
echo Health Check: http://localhost:8000/health
echo.
echo Default Admin:
echo   Phone: +250789751597
echo   Password: admin123
echo.
echo Press any key to continue...
pause
