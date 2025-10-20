from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from database import get_db
from models import SessionPlan, SchemeOfWork, User, Notification, Settings
from schemas import SessionPlanCreate, SchemeOfWorkCreate
from pydantic import BaseModel
from document_generator import generate_session_plan_docx, generate_scheme_of_work_docx
from fastapi.responses import FileResponse
import os
from typing import Optional, List
import time

app = FastAPI(title="RTB Document Planner", version="1.0.0")

# CORS Configuration - Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "RTB Document Planner API", "status": "online", "cors": "enabled"}

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.query(SessionPlan).first()
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "disconnected", "error": str(e)}

# User Management
class UserCreate(BaseModel):
    user_id: str
    name: str
    phone: str
    email: str = None
    institution: str
    password: str
    role: str = 'user'

class UserLogin(BaseModel):
    phone: str
    password: str

@app.post("/users/register")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.phone == user.phone).first()
    if existing:
        raise HTTPException(status_code=400, detail="Phone number already registered")
    
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User registered successfully", "user_id": db_user.user_id}

@app.post("/users/login")
def login_user(credentials: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.phone == credentials.phone, User.password == credentials.password).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    user.updated_at = func.now()
    db.commit()
    
    return {
        "user_id": user.user_id,
        "name": user.name,
        "phone": user.phone,
        "email": user.email,
        "institution": user.institution,
        "role": user.role,
        "is_premium": user.is_premium,
        "session_plans_limit": user.session_plans_limit,
        "schemes_limit": user.schemes_limit,
        "login_time": int(time.time())
    }

@app.get("/user-limits/{phone}")
def get_user_limits(phone: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.phone == phone).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
        
    return {
        "session_plans_limit": user.session_plans_limit,
        "schemes_limit": user.schemes_limit,
        "session_plans_downloaded": user.session_plans_downloaded,
        "schemes_downloaded": user.schemes_downloaded,
        "is_premium": user.is_premium
    }

if __name__ == "__main__":
    import uvicorn
    PORT = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=PORT)