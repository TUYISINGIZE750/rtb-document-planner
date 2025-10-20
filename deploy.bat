@echo off
echo RTB Document Planner - Netlify Deployment
echo ==========================================

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python not found. Please install Python first.
    pause
    exit /b 1
)

REM Check if Node.js is installed
node --version >nul 2>&1
if errorlevel 1 (
    echo Node.js not found. Installing via winget...
    winget install OpenJS.NodeJS
    echo Please restart this script after Node.js installation.
    pause
    exit /b 1
)

REM Run deployment script
python deploy-netlify.py

echo.
echo Deployment script completed!
pause