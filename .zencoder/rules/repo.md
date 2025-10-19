---
description: Repository Information Overview
alwaysApply: true
---

# RTB Document Planner Information

## Summary
A comprehensive FastAPI application for creating, managing, and generating RTB-compliant TVET educational documents with professional formatting. The system allows users to create session plans and schemes of work for educational purposes, with document generation capabilities.

## Structure
- **backend/**: FastAPI backend application with database models and document generation
- **frontend/**: Simple HTML/JS frontend served via Python's HTTP server
- **test_*.py**: System test files for verifying functionality
- **start_*.bat**: Batch files for starting the application on Windows

## Language & Runtime
**Language**: Python 3.11
**Framework**: FastAPI 0.104.1
**Database**: SQLAlchemy 2.0.23 with SQLite (development) and PostgreSQL (production)
**Frontend**: HTML, CSS, JavaScript (vanilla)
**Document Processing**: python-docx 1.1.0

## Dependencies
**Main Dependencies**:
- fastapi==0.104.1
- uvicorn==0.24.0
- sqlalchemy==2.0.23
- python-docx==1.1.0
- pydantic==2.5.0
- jinja2==3.1.2

**Database Dependencies**:
- psycopg2-binary==2.9.9 (PostgreSQL)
- alembic==1.12.1 (Migrations)

## Build & Installation
**Option 1: Windows Quick Start**
```bash
# Double-click or run:
start_all.bat
```

**Option 2: Manual Setup**
```bash
# Install backend dependencies
cd backend
pip install -r requirements.txt

# Initialize database
python init_db.py

# Start backend
python startup.py

# In a new terminal, start frontend
cd ../frontend
python -m http.server 5173
```

## Docker
**Docker Compose**: Full stack deployment with PostgreSQL
```bash
docker-compose up --build
```

**Backend Dockerfile**: Python 3.11 slim image with FastAPI
**Frontend Dockerfile**: Python 3.11 slim image with HTTP server
**Database**: PostgreSQL 15 with persistent volume

## Main Files
**Backend Entry Point**: backend/main.py
**API Endpoints**:
- Session Plans: Create, list, download
- Schemes of Work: Create, list, download
- User Management: Registration, login, activation

**Frontend Entry Point**: frontend/index.html
**Database Models**: backend/models.py
**Document Generation**: backend/document_generator.py

## Testing
**Test Framework**: Python's requests library for API testing
**Main Test File**: test_complete_system.py
**Test Command**:
```bash
python test_complete_system.py
```

**Test Coverage**:
- API connectivity
- Document creation
- DOCX generation
- Download functionality

## Access Points
- **Frontend**: http://localhost:5173
- **API Documentation**: http://localhost:8000/docs
- **API Health Check**: http://localhost:8000/health