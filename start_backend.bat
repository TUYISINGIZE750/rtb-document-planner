@echo off
echo Starting RTB Document Planner Backend...
cd backend
python -m uvicorn main:app --host 0.0.0.0 --port 8002 --reload
pause