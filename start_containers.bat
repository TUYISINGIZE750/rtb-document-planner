@echo off
echo ========================================
echo Starting RTB Document Planner with PostgreSQL
echo ========================================

echo.
echo 1. Stopping any existing containers...
docker-compose down

echo.
echo 2. Starting PostgreSQL and all services...
docker-compose up -d

echo.
echo 3. Waiting for PostgreSQL to be ready...
timeout /t 10 /nobreak > nul

echo.
echo 4. Checking container status...
docker-compose ps

echo.
echo ========================================
echo Services Status:
echo ========================================
echo Backend API: http://localhost:8000
echo Frontend: http://localhost:5173  
echo PostgreSQL: localhost:5433
echo ========================================

echo.
echo 5. Testing database connection...
docker-compose exec db psql -U rtb_user -d rtb_planner -c "\dt"

echo.
echo All containers are running!
echo You can now access the application at http://localhost:5173
pause