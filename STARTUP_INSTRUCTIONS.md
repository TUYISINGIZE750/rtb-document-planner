# RTB Document Planner - Startup Instructions

## Quick Start (Recommended)

### Option 1: Docker Containers (PostgreSQL)
```bash
# Start all containers (PostgreSQL + Backend + Frontend)
start_containers.bat
```

### Option 2: Manual Terminals (PostgreSQL)
```bash
# Terminal 1: Start PostgreSQL container
docker run -d --name rtb-postgres -p 5433:5432 -e POSTGRES_DB=rtb_planner -e POSTGRES_USER=rtb_user -e POSTGRES_PASSWORD=rtb_password postgres:15

# Terminal 2: Start Backend
start_backend_terminal.bat

# Terminal 3: Start Frontend  
start_frontend_terminal.bat
```

### Option 3: Individual Commands

#### Terminal 1 - PostgreSQL
```bash
docker run -d --name rtb-postgres -p 5433:5432 -e POSTGRES_DB=rtb_planner -e POSTGRES_USER=rtb_user -e POSTGRES_PASSWORD=rtb_password postgres:15
```

#### Terminal 2 - Backend
```bash
cd backend
set DATABASE_URL=postgresql://rtb_user:rtb_password@localhost:5433/rtb_planner
python startup.py
```

#### Terminal 3 - Frontend
```bash
cd frontend
python -m http.server 5173
```

## Access Points

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **PostgreSQL**: localhost:5433

## Default Credentials

- **Admin**: +250789751597 / admin123
- **Test User**: +250123456789 / test123

## Testing

```bash
# Test PostgreSQL system
python test_postgres_system.py

# Test session management
python test_session_fix.py
```

## Container Management

```bash
# View running containers
docker ps

# Stop all containers
docker-compose down

# View logs
docker-compose logs backend
docker-compose logs db

# Restart specific service
docker-compose restart backend
```

## Troubleshooting

### PostgreSQL Issues
```bash
# Check if PostgreSQL is running
docker ps | grep postgres

# Connect to PostgreSQL directly
docker exec -it rtb-postgres psql -U rtb_user -d rtb_planner

# View database tables
\dt
```

### Backend Issues
```bash
# Check backend logs
docker-compose logs backend

# Restart backend
docker-compose restart backend
```

### Database Connection Issues
```bash
# Test connection
python test_postgres_system.py

# Reset database
docker-compose down
docker volume rm rtb_postgres_data
docker-compose up -d
```