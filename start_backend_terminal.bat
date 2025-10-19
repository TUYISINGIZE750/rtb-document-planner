@echo off
echo ========================================
echo Starting RTB Backend Server
echo ========================================

cd backend

echo.
echo 1. Fixing database with PostgreSQL...
python -c "
import os
os.environ['DATABASE_URL'] = 'postgresql://rtb_user:rtb_password@localhost:5433/rtb_planner'
exec(open('../fix_database.py').read())
"

echo.
echo 2. Starting backend server...
set DATABASE_URL=postgresql://rtb_user:rtb_password@localhost:5433/rtb_planner
python startup.py

pause