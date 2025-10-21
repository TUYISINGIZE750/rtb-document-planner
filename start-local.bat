@echo off
echo ========================================
echo RTB Document Planner - Local Development
echo ========================================
echo.

REM Start backend in new window
echo Starting Backend Server...
start "RTB Backend" cmd /k "cd backend && python main.py"

timeout /t 3 /nobreak >nul

REM Start frontend in new window
echo Starting Frontend Server...
start "RTB Frontend" cmd /k "cd frontend && python -m http.server 5173"

timeout /t 2 /nobreak >nul

echo.
echo ========================================
echo System Started Successfully!
echo ========================================
echo.
echo Backend:  http://localhost:8000
echo Frontend: http://localhost:5173
echo.
echo Opening browser...
timeout /t 2 /nobreak >nul

start http://localhost:5173

echo.
echo Press any key to stop all servers...
pause >nul

taskkill /FI "WindowTitle eq RTB Backend*" /T /F
taskkill /FI "WindowTitle eq RTB Frontend*" /T /F

echo.
echo All servers stopped.
pause