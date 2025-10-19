# RTB Document Planner - Quick Start Guide

## 🚀 How to Start the Application

### Step 1: Start Backend Server
1. Double-click `start_backend.bat` 
2. Wait for "Application startup complete" message
3. Backend will run on: http://localhost:8001

### Step 2: Start Frontend Server  
1. Double-click `start_frontend.bat`
2. Frontend will run on: http://localhost:5173

### Step 3: Access the Application
Open your browser and go to: **http://localhost:5173**

## 🔧 Manual Startup (Alternative)

### Backend:
```bash
cd backend
python -m uvicorn main:app --host 0.0.0.0 --port 8001 --reload
```

### Frontend:
```bash
cd frontend  
python -m http.server 5173
```

## ✅ Verification
- Backend API: http://localhost:8001/docs
- Frontend App: http://localhost:5173
- Health Check: http://localhost:8001/health

## 🛠 Troubleshooting
- If port 8001 is busy, change port in both `start_backend.bat` and `frontend/index.html`
- Make sure Python is installed and in PATH
- Database is SQLite (no setup required)

## 📁 Project Structure
- `backend/` - FastAPI server
- `frontend/` - Web interface  
- `rtb_planner.db` - SQLite database (auto-created)