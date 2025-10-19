@echo off
echo ========================================
echo RTB Document Planner - System Test
echo ========================================
echo.

echo 1. Verifying Setup...
python verify_setup.py
if %errorlevel% neq 0 (
    echo.
    echo Setup verification failed. Please check the issues above.
    pause
    exit /b 1
)

echo.
echo 2. Testing Complete System...
echo (Make sure the backend is running on port 8000)
echo.
timeout /t 3 /nobreak >nul

python test_complete_system.py

echo.
echo ========================================
echo Test Complete!
echo ========================================
echo.
echo If tests passed, your RTB Document Planner is working correctly.
echo.
pause