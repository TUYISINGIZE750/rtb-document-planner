# Local Development Setup

## Quick Start (Easiest Way)

**Double-click:** `start-local.bat`

This will:
1. Start backend on http://localhost:8000
2. Start frontend on http://localhost:5173
3. Open browser automatically

## Manual Start

### Terminal 1 - Backend:
```bash
cd backend
python main.py
```

### Terminal 2 - Frontend:
```bash
cd frontend
python -m http.server 5173
```

## Access Your App

- **Frontend:** http://localhost:5173
- **Backend API:** http://localhost:8000
- **Test Page:** http://localhost:5173/system-test.html

## Stop Servers

- Press `Ctrl+C` in each terminal
- Or close the command windows

## Requirements

- Python 3.7+
- Flask
- Flask-CORS

Install dependencies:
```bash
pip install flask flask-cors
```

## Features

✅ Same code as production
✅ Hot reload enabled
✅ CORS configured
✅ All endpoints working
✅ Registration & Login functional

## Troubleshooting

**Port already in use:**
- Change port in backend/main.py: `app.run(port=8001)`
- Change frontend port: `python -m http.server 5174`

**Module not found:**
```bash
pip install flask flask-cors
```

**Can't access from other devices:**
- Backend already uses `0.0.0.0` (accessible from network)
- Frontend: Use `python -m http.server 5173 --bind 0.0.0.0`
- Access via: `http://YOUR_IP:5173`