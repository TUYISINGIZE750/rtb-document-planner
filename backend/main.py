from fastapi import FastAPI, HTTPException, Depends, Header
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy.sql import func
from database import get_db
from models import SessionPlan, SchemeOfWork, User, Notification, Settings
from schemas import SessionPlanCreate, SchemeOfWorkCreate, SessionPlanResponse, SchemeOfWorkResponse
from pydantic import BaseModel
from document_generator import generate_session_plan_docx, generate_scheme_of_work_docx
from fastapi.responses import FileResponse
import os
from typing import Optional, List
import time

app = FastAPI(title="RTB Document Planner", version="1.0.0")

# Enhanced CORS Configuration for cross-device compatibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH"],
    allow_headers=[
        "*",
        "Accept",
        "Accept-Language",
        "Content-Language",
        "Content-Type",
        "Authorization",
        "X-Requested-With",
        "Origin",
        "Access-Control-Request-Method",
        "Access-Control-Request-Headers"
    ],
    expose_headers=["*"],
    max_age=86400,
)

# Add middleware for security headers and OPTIONS handling
@app.middleware("http")
async def add_security_headers(request, call_next):
    # Handle preflight OPTIONS requests
    if request.method == "OPTIONS":
        from fastapi import Response
        response = Response()
        response.headers["Access-Control-Allow-Origin"] = "*"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS, HEAD, PATCH"
        response.headers["Access-Control-Allow-Headers"] = "*"
        response.headers["Access-Control-Max-Age"] = "86400"
        return response
    
    response = await call_next(request)
    
    # Add security headers
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    
    return response

# Fallback OPTIONS handler
@app.options("/{path:path}")
async def options_handler(path: str):
    return {"message": "OK"}

@app.get("/")
def read_root():
    from fastapi import Response
    response_data = {"message": "RTB Document Planner API", "status": "online", "cors": "enabled"}
    return response_data

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        # Test database connection by querying a table
        db.query(SessionPlan).first()
        return {"status": "healthy", "database": "connected"}
    except Exception as e:
        return {"status": "unhealthy", "database": "disconnected", "error": str(e)}

@app.post("/session-plans/")
def create_session_plan(plan: SessionPlanCreate, db: Session = Depends(get_db)):
    try:
        db_plan = SessionPlan(**plan.dict())
        db.add(db_plan)
        db.commit()
        db.refresh(db_plan)
        
        # Send notification to trainer if trainer_name is provided
        if hasattr(plan, 'trainer_name') and plan.trainer_name:
            trainer = db.query(User).filter(User.name.ilike(f"%{plan.trainer_name}%")).first()
            if trainer:
                send_auto_notification(
                    user_id=trainer.id,
                    title="New Session Plan Created",
                    message=f"A new session plan has been created for {plan.module_code_title or 'your module'}. You can now download and use it for your classes.",
                    notification_type="success",
                    db=db
                )
        
        # Return the plan with ID explicitly included
        return {
            "id": db_plan.id,
            "sector": db_plan.sector,
            "trade": db_plan.trade,
            "module_code_title": db_plan.module_code_title,
            "trainer_name": db_plan.trainer_name,
            "created_at": db_plan.created_at
        }
    except Exception as e:
        db.rollback()
        print(f"Database error: {e}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.post("/schemes-of-work/")
def create_scheme_of_work(scheme: SchemeOfWorkCreate, db: Session = Depends(get_db)):
    try:
        db_scheme = SchemeOfWork(**scheme.dict())
        db.add(db_scheme)
        db.commit()
        db.refresh(db_scheme)
        
        # Send notification to trainer if trainer_name is provided
        if hasattr(scheme, 'trainer_name') and scheme.trainer_name:
            trainer = db.query(User).filter(User.name.ilike(f"%{scheme.trainer_name}%")).first()
            if trainer:
                send_auto_notification(
                    user_id=trainer.id,
                    title="New Scheme of Work Created",
                    message=f"A new scheme of work has been created for {scheme.module_code_title or 'your module'}. You can now download and use it for your curriculum planning.",
                    notification_type="success",
                    db=db
                )
        
        # Return the scheme with ID explicitly included
        return {
            "id": db_scheme.id,
            "school": db_scheme.school,
            "sector": db_scheme.sector,
            "module_code_title": db_scheme.module_code_title,
            "trainer_name": db_scheme.trainer_name,
            "created_at": db_scheme.created_at
        }
    except Exception as e:
        db.rollback()
        print(f"Database error: {e}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.get("/session-plans/{plan_id}/download")
def download_session_plan(plan_id: int, phone: str = None, db: Session = Depends(get_db)):
    plan = db.query(SessionPlan).filter(SessionPlan.id == plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Session plan not found")
    
    # Track download if phone provided
    if phone:
        user = db.query(User).filter(User.phone == phone).first()
        if user and not user.is_premium:
            user.session_plans_downloaded += 1
            db.commit()
    
    docx_file = generate_session_plan_docx(plan)
    return FileResponse(docx_file, filename=f"session_plan_{plan_id}.docx")

@app.get("/schemes-of-work/{scheme_id}/download")
def download_scheme_of_work(scheme_id: int, phone: str = None, db: Session = Depends(get_db)):
    scheme = db.query(SchemeOfWork).filter(SchemeOfWork.id == scheme_id).first()
    if not scheme:
        raise HTTPException(status_code=404, detail="Scheme of work not found")
    
    # Track download if phone provided
    if phone:
        user = db.query(User).filter(User.phone == phone).first()
        if user and not user.is_premium:
            user.schemes_downloaded += 1
            db.commit()
    
    docx_file = generate_scheme_of_work_docx(scheme)
    return FileResponse(docx_file, filename=f"scheme_of_work_{scheme_id}.docx")

@app.get("/session-plans/")
def get_session_plans(db: Session = Depends(get_db)):
    try:
        plans = db.query(SessionPlan).all()
        return plans
    except Exception as e:
        print(f"Database error: {e}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.get("/schemes-of-work/")
def get_schemes_of_work(db: Session = Depends(get_db)):
    try:
        schemes = db.query(SchemeOfWork).all()
        return schemes
    except Exception as e:
        print(f"Database error: {e}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.delete("/session-plans/{plan_id}")
def delete_session_plan(plan_id: int, db: Session = Depends(get_db)):
    try:
        plan = db.query(SessionPlan).filter(SessionPlan.id == plan_id).first()
        if not plan:
            raise HTTPException(status_code=404, detail="Session plan not found")
        
        db.delete(plan)
        db.commit()
        return {"message": f"Session plan {plan_id} deleted successfully"}
    except Exception as e:
        db.rollback()
        print(f"Database error: {e}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.delete("/schemes-of-work/{scheme_id}")
def delete_scheme_of_work(scheme_id: int, db: Session = Depends(get_db)):
    try:
        scheme = db.query(SchemeOfWork).filter(SchemeOfWork.id == scheme_id).first()
        if not scheme:
            raise HTTPException(status_code=404, detail="Scheme of work not found")
        
        db.delete(scheme)
        db.commit()
        return {"message": f"Scheme of work {scheme_id} deleted successfully"}
    except Exception as e:
        db.rollback()
        print(f"Database error: {e}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

# User Management Endpoints
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

class NotificationCreate(BaseModel):
    user_id: int
    title: str
    message: str
    type: str = 'info'

class NotificationResponse(BaseModel):
    id: int
    title: str
    message: str
    type: str
    is_read: bool
    created_at: str

class BulkNotificationCreate(BaseModel):
    title: str
    message: str
    type: str = 'info'
    user_ids: Optional[List[int]] = None  # If None, send to all users

class SettingsUpdate(BaseModel):
    free_session_plans: int = 2
    free_schemes: int = 2
    per_session_price: int = 36
    per_scheme_price: int = 47
    weekly_sessions_price: int = 474
    weekly_schemes_price: int = 526
    monthly_sessions_price: int = 1000
    monthly_schemes_price: int = 1889
    unlimited_price: int = 5200

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
    
    # Update last login time
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

@app.get("/users/")
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return [{"id": u.id, "user_id": u.user_id, "name": u.name, "phone": u.phone, "email": u.email, "institution": u.institution, "role": u.role, "is_premium": u.is_premium, "session_plans_limit": u.session_plans_limit, "schemes_limit": u.schemes_limit, "session_plans_downloaded": u.session_plans_downloaded, "schemes_downloaded": u.schemes_downloaded, "created_at": u.created_at} for u in users]

@app.get("/users/{phone}")
def get_user_by_phone(phone: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.phone == phone).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user_id": user.user_id, "name": user.name, "phone": user.phone, "email": user.email, "institution": user.institution, "role": user.role, "is_premium": user.is_premium, "session_plans_limit": user.session_plans_limit, "schemes_limit": user.schemes_limit, "created_at": user.created_at}

@app.post("/users/validate-session")
def validate_session(phone: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.phone == phone).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"valid": True, "user_id": user.user_id, "role": user.role}

@app.post("/users/logout")
def logout_user(phone: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.phone == phone).first()
    if user:
        user.updated_at = func.now()
        db.commit()
    return {"message": "Logged out successfully"}



@app.put("/users/{phone}/activate")
def activate_user(phone: str, session_plans: int, schemes: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.phone == phone).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if session_plans == -1:
        user.is_premium = True
        # Send premium activation notification
        send_auto_notification(
            user_id=user.id,
            title="Premium Account Activated!",
            message="Congratulations! Your premium account has been activated. You now have unlimited access to session plans and schemes of work.",
            notification_type="success",
            db=db
        )
    else:
        user.session_plans_limit += session_plans
        user.schemes_limit += schemes
        # Send subscription notification
        send_auto_notification(
            user_id=user.id,
            title="Subscription Updated",
            message=f"Your subscription has been updated! You now have {session_plans} additional session plans and {schemes} additional schemes of work.",
            notification_type="info",
            db=db
        )
    
    db.commit()
    return {"message": "User activated successfully"}

# Notification Endpoints
@app.post("/notifications/")
def create_notification(notification: NotificationCreate, db: Session = Depends(get_db)):
    """Create a notification for a specific user"""
    try:
        db_notification = Notification(**notification.dict())
        db.add(db_notification)
        db.commit()
        db.refresh(db_notification)
        return {"message": "Notification created successfully", "id": db_notification.id}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to create notification: {str(e)}")

@app.post("/notifications/bulk")
def create_bulk_notification(notification: BulkNotificationCreate, db: Session = Depends(get_db)):
    """Send notification to multiple users or all users"""
    try:
        if notification.user_ids:
            # Send to specific users
            users = db.query(User).filter(User.id.in_(notification.user_ids)).all()
        else:
            # Send to all users
            users = db.query(User).all()
        
        notifications_created = 0
        for user in users:
            db_notification = Notification(
                user_id=user.id,
                title=notification.title,
                message=notification.message,
                type=notification.type
            )
            db.add(db_notification)
            notifications_created += 1
        
        db.commit()
        return {"message": f"Notification sent to {notifications_created} users"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to send bulk notification: {str(e)}")

@app.get("/notifications/user/{user_id}")
def get_user_notifications(user_id: int, db: Session = Depends(get_db)):
    """Get all notifications for a specific user"""
    try:
        notifications = db.query(Notification).filter(Notification.user_id == user_id).order_by(Notification.created_at.desc()).all()
        return [{
            "id": n.id,
            "title": n.title,
            "message": n.message,
            "type": n.type,
            "is_read": n.is_read,
            "created_at": n.created_at.isoformat()
        } for n in notifications]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get notifications: {str(e)}")

@app.put("/notifications/{notification_id}/read")
def mark_notification_read(notification_id: int, db: Session = Depends(get_db)):
    """Mark a notification as read"""
    try:
        notification = db.query(Notification).filter(Notification.id == notification_id).first()
        if not notification:
            raise HTTPException(status_code=404, detail="Notification not found")
        
        notification.is_read = True
        db.commit()
        return {"message": "Notification marked as read"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to mark notification as read: {str(e)}")

@app.get("/notifications/unread/{user_id}")
def get_unread_count(user_id: int, db: Session = Depends(get_db)):
    """Get unread notification count for a user"""
    try:
        count = db.query(Notification).filter(Notification.user_id == user_id, Notification.is_read == False).count()
        return {"unread_count": count}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get unread count: {str(e)}")

@app.get("/cleanup-files")
def cleanup_generated_files():
    """Clean up generated DOCX files"""
    try:
        import glob
        files_deleted = 0
        
        # Clean up session plan files
        for file in glob.glob("session_plan_*.docx"):
            try:
                os.remove(file)
                files_deleted += 1
            except:
                pass
        
        # Clean up scheme of work files
        for file in glob.glob("scheme_of_work_*.docx"):
            try:
                os.remove(file)
                files_deleted += 1
            except:
                pass
                
        return {"message": f"Cleaned up {files_deleted} generated files"}
    except Exception as e:
        return {"error": f"Failed to cleanup files: {str(e)}"}

# Settings endpoints
@app.get("/settings")
def get_settings(db: Session = Depends(get_db)):
    """Get system settings"""
    try:
        settings = db.query(Settings).all()
        settings_dict = {s.key: s.value for s in settings}
        
        # Default values if not set
        defaults = {
            'free_session_plans': '2',
            'free_schemes': '2',
            'per_session_price': '36',
            'per_scheme_price': '47',
            'weekly_sessions_price': '474',
            'weekly_schemes_price': '526',
            'monthly_sessions_price': '1000',
            'monthly_schemes_price': '1889',
            'unlimited_price': '5200'
        }
        
        for key, default_value in defaults.items():
            if key not in settings_dict:
                settings_dict[key] = default_value
                
        return settings_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get settings: {str(e)}")

@app.post("/settings")
def update_settings(settings: SettingsUpdate, db: Session = Depends(get_db)):
    """Update system settings"""
    try:
        settings_data = {
            'free_session_plans': str(settings.free_session_plans),
            'free_schemes': str(settings.free_schemes),
            'per_session_price': str(settings.per_session_price),
            'per_scheme_price': str(settings.per_scheme_price),
            'weekly_sessions_price': str(settings.weekly_sessions_price),
            'weekly_schemes_price': str(settings.weekly_schemes_price),
            'monthly_sessions_price': str(settings.monthly_sessions_price),
            'monthly_schemes_price': str(settings.monthly_schemes_price),
            'unlimited_price': str(settings.unlimited_price)
        }
        
        for key, value in settings_data.items():
            setting = db.query(Settings).filter(Settings.key == key).first()
            if setting:
                setting.value = value
            else:
                setting = Settings(key=key, value=value)
                db.add(setting)
        
        db.commit()
        return {"message": "Settings updated successfully"}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to update settings: {str(e)}")

@app.get("/user-limits/{phone}")
def get_user_limits(phone: str, db: Session = Depends(get_db)):
    """Get user download limits and remaining counts"""
    try:
        user = db.query(User).filter(User.phone == phone).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
            
        settings = db.query(Settings).all()
        settings_dict = {s.key: int(s.value) for s in settings}
        
        free_session_plans = settings_dict.get('free_session_plans', 2)
        free_schemes = settings_dict.get('free_schemes', 2)
        
        return {
            "session_plans_limit": user.session_plans_limit,
            "schemes_limit": user.schemes_limit,
            "session_plans_downloaded": user.session_plans_downloaded,
            "schemes_downloaded": user.schemes_downloaded,
            "session_plans_remaining": max(0, user.session_plans_limit - user.session_plans_downloaded),
            "schemes_remaining": max(0, user.schemes_limit - user.schemes_downloaded),
            "is_premium": user.is_premium,
            "free_session_plans": free_session_plans,
            "free_schemes": free_schemes
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get user limits: {str(e)}")

@app.post("/users/{phone}/upgrade")
def upgrade_user(phone: str, upgrade_data: dict, db: Session = Depends(get_db)):
    """Upgrade user subscription after payment"""
    try:
        user = db.query(User).filter(User.phone == phone).first()
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        
        plan_type = upgrade_data.get('plan_type')
        payment_confirmed = upgrade_data.get('payment_confirmed', False)
        
        if not payment_confirmed:
            raise HTTPException(status_code=400, detail="Payment not confirmed")
        
        # Update user based on plan type - all paid plans get premium status
        user.is_premium = True
        
        # Send upgrade notification
        plan_names = {
            'per_session': 'Per Session Plan',
            'per_scheme': 'Per Scheme',
            'weekly_sessions': 'Weekly Sessions',
            'weekly_schemes': 'Weekly Schemes',
            'monthly_sessions': 'Monthly Sessions',
            'monthly_schemes': 'Monthly Schemes',
            'unlimited': 'School Year Unlimited'
        }
        
        send_auto_notification(
            user_id=user.id,
            title="Welcome to Premium!",
            message="Your account has been successfully upgraded. You now have unlimited access to create professional RTB documents.",
            notification_type="success",
            db=db
        )
        
        db.commit()
        
        return {"message": "User upgraded successfully", "is_premium": user.is_premium}
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Failed to upgrade user: {str(e)}")

# Helper function to send automatic notifications
def send_auto_notification(user_id: int, title: str, message: str, notification_type: str = 'info', db: Session = None):
    """Helper function to send automatic notifications"""
    if db:
        try:
            notification = Notification(
                user_id=user_id,
                title=title,
                message=message,
                type=notification_type
            )
            db.add(notification)
            db.commit()
        except Exception as e:
            print(f"Failed to send auto notification: {e}")
            db.rollback()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=PORT)