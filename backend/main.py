from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from datetime import datetime
import hashlib
import tempfile
import os
from document_generator import generate_session_plan_docx, generate_scheme_of_work_docx, generate_session_plan_pdf, generate_scheme_of_work_pdf
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

CORS(app, 
     origins=[
         "https://tuyisingize750.github.io",
         "https://schemesession.netlify.app",
         "http://localhost:5173"
     ],
     methods=["GET", "POST", "OPTIONS"],
     allow_headers=["Content-Type", "Authorization"],
     supports_credentials=False)

@app.after_request
def after_request(response):
    origin = request.headers.get('Origin')
    if origin in ["https://tuyisingize750.github.io", "https://schemesession.netlify.app"]:
        response.headers.add('Access-Control-Allow-Origin', origin)
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS')
    return response

# Database setup
DATABASE_URL = "sqlite:///./rtb_planner.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(255), unique=True, index=True)
    name = Column(String(255), nullable=False)
    phone = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(255))
    institution = Column(String(255))
    password = Column(String(255), nullable=False)
    role = Column(String(50), default='user')
    is_premium = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    session_plans_limit = Column(Integer, default=2)
    schemes_limit = Column(Integer, default=2)
    session_plans_downloaded = Column(Integer, default=0)
    schemes_downloaded = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class SessionPlan(Base):
    __tablename__ = "session_plans"
    id = Column(Integer, primary_key=True, index=True)
    user_phone = Column(String(50), nullable=False)
    sector = Column(String(255))
    sub_sector = Column(String(255))
    trade = Column(String(255))
    qualification_title = Column(String(500))
    rqf_level = Column(String(50))
    module_code_title = Column(String(500))
    term = Column(String(100))
    week = Column(String(100))
    date = Column(String(100))
    trainer_name = Column(String(255))
    class_name = Column(String(255))
    number_of_trainees = Column(String(100))
    learning_outcomes = Column(Text)
    indicative_contents = Column(Text)
    topic_of_session = Column(String(500))
    duration = Column(String(100))
    objectives = Column(Text)
    facilitation_techniques = Column(Text)
    learning_activities = Column(Text)
    resources = Column(Text)
    assessment_details = Column(Text)
    references = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class SchemeOfWork(Base):
    __tablename__ = "schemes_of_work"
    id = Column(Integer, primary_key=True, index=True)
    user_phone = Column(String(50), nullable=False)
    province = Column(String(255))
    district = Column(String(255))
    sector = Column(String(255))
    school = Column(String(255))
    department_trade = Column(String(255))
    qualification_title = Column(String(500))
    rqf_level = Column(String(50))
    module_code_title = Column(String(500))
    school_year = Column(String(100))
    terms = Column(String(100))
    module_hours = Column(String(100))
    number_of_classes = Column(String(100))
    class_name = Column(String(255))
    trainer_name = Column(String(255))
    term1_weeks = Column(Text)
    term1_learning_outcomes = Column(Text)
    term1_indicative_contents = Column(Text)
    term1_duration = Column(Text)
    term2_weeks = Column(Text)
    term2_learning_outcomes = Column(Text)
    term2_indicative_contents = Column(Text)
    term2_duration = Column(Text)
    term3_weeks = Column(Text)
    term3_learning_outcomes = Column(Text)
    term3_indicative_contents = Column(Text)
    term3_duration = Column(Text)
    dos_name = Column(String(255))
    manager_name = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

Base.metadata.create_all(bind=engine)

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password: str, hashed: str) -> bool:
    return hash_password(password) == hashed

def init_admin():
    db = SessionLocal()
    try:
        admin = db.query(User).filter(User.phone == "+250789751597").first()
        if not admin:
            admin = User(
                user_id="ADMIN_001",
                name="Administrator",
                phone="+250789751597",
                email="admin@rtb.rw",
                institution="RTB",
                password=hash_password("admin123"),
                role="admin",
                is_premium=True,
                is_active=True,
                session_plans_limit=999,
                schemes_limit=999
            )
            db.add(admin)
            db.commit()
    finally:
        db.close()

init_admin()

@app.route('/', methods=['GET', 'OPTIONS'])
def home():
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        db = SessionLocal()
        try:
            users_count = db.query(User).count()
        finally:
            db.close()
    except:
        users_count = 0
    
    return jsonify({
        "message": "RTB Document Planner API",
        "status": "online",
        "cors": "enabled",
        "environment": "production",
        "version": "2.0",
        "features": ["authentication", "docx_generation", "pdf_generation"],
        "users_count": users_count
    })

@app.route('/users/register', methods=['POST', 'OPTIONS'])
def register():
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        data = request.get_json()
        phone = data.get('phone')
        password = data.get('password')
        name = data.get('name')
        
        if not all([phone, password, name]):
            return jsonify({"detail": "Phone, password, and name are required"}), 400
        
        db = SessionLocal()
        try:
            existing_user = db.query(User).filter(User.phone == phone).first()
            if existing_user:
                return jsonify({"detail": "Phone number already registered"}), 400
            
            user = User(
                user_id=f"USER_{datetime.now().strftime('%Y%m%d%H%M%S')}",
                name=name,
                phone=phone,
                email=data.get('email', ''),
                institution=data.get('institution', ''),
                password=hash_password(password)
            )
            
            db.add(user)
            db.commit()
            return jsonify({"message": "User registered successfully"}), 201
        finally:
            db.close()
    except Exception as e:
        return jsonify({"detail": "Registration failed"}), 500

@app.route('/users/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        data = request.get_json()
        phone = data.get('phone')
        password = data.get('password')
        
        if not all([phone, password]):
            return jsonify({"detail": "Phone and password are required"}), 400
        
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.phone == phone).first()
            
            if not user or not verify_password(password, user.password):
                return jsonify({"detail": "Invalid credentials"}), 401
            
            if not user.is_active:
                return jsonify({"detail": "Account not activated"}), 403
            
            return jsonify({
                "message": "Login successful",
                "user": {
                    "name": user.name,
                    "phone": user.phone,
                    "email": user.email,
                    "institution": user.institution,
                    "role": user.role,
                    "is_premium": user.is_premium,
                    "session_plans_limit": user.session_plans_limit,
                    "schemes_limit": user.schemes_limit,
                    "session_plans_downloaded": user.session_plans_downloaded,
                    "schemes_downloaded": user.schemes_downloaded
                }
            }), 200
        finally:
            db.close()
    except Exception as e:
        return jsonify({"detail": "Login failed"}), 500

@app.route('/session-plans/generate', methods=['POST', 'OPTIONS'])
def generate_session_plan():
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        data = request.get_json()
        user_phone = data.get('user_phone')
        format_type = data.get('format', 'docx')
        
        if not user_phone:
            return jsonify({"detail": "User phone required"}), 400
        
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.phone == user_phone).first()
            if not user:
                return jsonify({"detail": "User not found"}), 404
            
            if user.session_plans_downloaded >= user.session_plans_limit:
                return jsonify({"detail": "Download limit reached"}), 403
            
            # Save session plan
            session_plan = SessionPlan(
                user_phone=user_phone,
                sector=data.get('sector'),
                sub_sector=data.get('sub_sector'),
                trade=data.get('trade'),
                qualification_title=data.get('qualification_title'),
                rqf_level=data.get('rqf_level'),
                module_code_title=data.get('module_code_title'),
                term=data.get('term'),
                week=data.get('week'),
                date=data.get('date'),
                trainer_name=data.get('trainer_name'),
                class_name=data.get('class_name'),
                number_of_trainees=data.get('number_of_trainees'),
                learning_outcomes=data.get('learning_outcomes'),
                indicative_contents=data.get('indicative_contents'),
                topic_of_session=data.get('topic_of_session'),
                duration=data.get('duration'),
                objectives=data.get('objectives'),
                facilitation_techniques=data.get('facilitation_techniques'),
                learning_activities=data.get('learning_activities'),
                resources=data.get('resources'),
                assessment_details=data.get('assessment_details'),
                references=data.get('references')
            )
            
            db.add(session_plan)
            
            # Update download count first
            user.session_plans_downloaded += 1
            db.commit()
            
            # Generate document after commit
            if format_type == 'pdf':
                file_path = generate_session_plan_pdf(data)
                mimetype = 'application/pdf'
                filename = f"RTB_Session_Plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            else:
                file_path = generate_session_plan_docx(data)
                mimetype = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
                filename = f"RTB_Session_Plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.docx"
            
            return send_file(
                file_path,
                as_attachment=True,
                download_name=filename,
                mimetype=mimetype
            )
        finally:
            db.close()
    except Exception as e:
        return jsonify({"detail": "Generation failed"}), 500

@app.route('/user-limits/<phone>', methods=['GET', 'OPTIONS'])
def get_user_limits(phone):
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.phone == phone).first()
            if not user:
                return jsonify({"detail": "User not found"}), 404
            
            return jsonify({
                "is_premium": user.is_premium,
                "session_plans_limit": user.session_plans_limit,
                "session_plans_downloaded": user.session_plans_downloaded,
                "session_plans_remaining": user.session_plans_limit - user.session_plans_downloaded if not user.is_premium else 999,
                "schemes_limit": user.schemes_limit,
                "schemes_downloaded": user.schemes_downloaded,
                "schemes_remaining": user.schemes_limit - user.schemes_downloaded if not user.is_premium else 999
            }), 200
        finally:
            db.close()
    except Exception as e:
        return jsonify({"detail": "Failed to get limits"}), 500

@app.route('/schemes/generate', methods=['POST', 'OPTIONS'])
def generate_scheme():
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        data = request.get_json()
        user_phone = data.get('user_phone')
        format_type = data.get('format', 'docx')
        
        if not user_phone:
            return jsonify({"detail": "User phone required"}), 400
        
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.phone == user_phone).first()
            if not user:
                return jsonify({"detail": "User not found"}), 404
            
            if user.schemes_downloaded >= user.schemes_limit:
                return jsonify({"detail": "Download limit reached"}), 403
            
            # Save scheme
            scheme = SchemeOfWork(
                user_phone=user_phone,
                province=data.get('province'),
                district=data.get('district'),
                sector=data.get('sector'),
                school=data.get('school'),
                department_trade=data.get('department_trade'),
                qualification_title=data.get('qualification_title'),
                rqf_level=data.get('rqf_level'),
                module_code_title=data.get('module_code_title'),
                school_year=data.get('school_year'),
                terms=data.get('terms'),
                module_hours=data.get('module_hours'),
                number_of_classes=data.get('number_of_classes'),
                class_name=data.get('class_name'),
                trainer_name=data.get('trainer_name'),
                term1_weeks=data.get('term1_weeks'),
                term1_learning_outcomes=data.get('term1_learning_outcomes'),
                term1_indicative_contents=data.get('term1_indicative_contents'),
                term1_duration=data.get('term1_duration'),
                term2_weeks=data.get('term2_weeks'),
                term2_learning_outcomes=data.get('term2_learning_outcomes'),
                term2_indicative_contents=data.get('term2_indicative_contents'),
                term2_duration=data.get('term2_duration'),
                term3_weeks=data.get('term3_weeks'),
                term3_learning_outcomes=data.get('term3_learning_outcomes'),
                term3_indicative_contents=data.get('term3_indicative_contents'),
                term3_duration=data.get('term3_duration'),
                dos_name=data.get('dos_name'),
                manager_name=data.get('manager_name')
            )
            
            db.add(scheme)
            
            # Update download count first
            user.schemes_downloaded += 1
            db.commit()
            
            # Generate document after commit
            if format_type == 'pdf':
                file_path = generate_scheme_of_work_pdf(data)
                mimetype = 'application/pdf'
                filename = f"RTB_Scheme_of_Work_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
            else:
                file_path = generate_scheme_of_work_docx(data)
                mimetype = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
                filename = f"RTB_Scheme_of_Work_{datetime.now().strftime('%Y%m%d_%H%M%S')}.docx"
            
            return send_file(
                file_path,
                as_attachment=True,
                download_name=filename,
                mimetype=mimetype
            )
        finally:
            db.close()
    except Exception as e:
        return jsonify({"detail": "Generation failed"}), 500

@app.route('/users/', methods=['GET', 'OPTIONS'])
@app.route('/admin/users', methods=['GET', 'OPTIONS'])
def get_all_users():
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        db = SessionLocal()
        try:
            users = db.query(User).all()
            users_list = [{
                "id": user.id,
                "user_id": user.user_id,
                "name": user.name,
                "phone": user.phone,
                "email": user.email,
                "institution": user.institution,
                "role": user.role,
                "is_premium": user.is_premium,
                "is_active": user.is_active,
                "session_plans_limit": user.session_plans_limit,
                "schemes_limit": user.schemes_limit,
                "session_plans_downloaded": user.session_plans_downloaded,
                "schemes_downloaded": user.schemes_downloaded,
                "created_at": user.created_at.isoformat() if user.created_at else None
            } for user in users]
            
            # Return array directly for admin-clean.html compatibility
            return jsonify(users_list), 200
        finally:
            db.close()
    except Exception as e:
        logger.error(f"Error getting users: {e}")
        return jsonify([]), 200

@app.route('/admin/users/<int:user_id>/activate', methods=['POST', 'OPTIONS'])
def activate_user(user_id):
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.id == user_id).first()
            if not user:
                return jsonify({"detail": "User not found"}), 404
            
            user.is_active = True
            db.commit()
            return jsonify({"message": "User activated successfully"}), 200
        finally:
            db.close()
    except Exception as e:
        return jsonify({"detail": "Failed to activate user"}), 500

@app.route('/admin/users/<int:user_id>/deactivate', methods=['POST', 'OPTIONS'])
def deactivate_user(user_id):
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.id == user_id).first()
            if not user:
                return jsonify({"detail": "User not found"}), 404
            
            user.is_active = False
            db.commit()
            return jsonify({"message": "User deactivated successfully"}), 200
        finally:
            db.close()
    except Exception as e:
        return jsonify({"detail": "Failed to deactivate user"}), 500

@app.route('/admin/users/<int:user_id>/upgrade', methods=['POST', 'OPTIONS'])
def upgrade_user(user_id):
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        data = request.get_json() or {}
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.id == user_id).first()
            if not user:
                return jsonify({"detail": "User not found"}), 404
            
            user.is_premium = True
            user.session_plans_limit = 999
            user.schemes_limit = 999
            db.commit()
            return jsonify({"message": "User upgraded to premium"}), 200
        finally:
            db.close()
    except Exception as e:
        return jsonify({"detail": "Failed to upgrade user"}), 500

@app.route('/admin/users/<int:user_id>/downgrade', methods=['POST', 'OPTIONS'])
def downgrade_user(user_id):
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.id == user_id).first()
            if not user:
                return jsonify({"detail": "User not found"}), 404
            
            user.is_premium = False
            user.session_plans_limit = 2
            user.schemes_limit = 2
            db.commit()
            return jsonify({"message": "User downgraded to free"}), 200
        finally:
            db.close()
    except Exception as e:
        return jsonify({"detail": "Failed to downgrade user"}), 500

@app.route('/stats', methods=['GET', 'OPTIONS'])
def get_stats():
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        db = SessionLocal()
        try:
            total_users = db.query(User).count()
            premium_users = db.query(User).filter(User.is_premium == True).count()
            active_users = db.query(User).filter(User.is_active == True).count()
            
            total_session_downloads = db.query(func.sum(User.session_plans_downloaded)).scalar() or 0
            total_scheme_downloads = db.query(func.sum(User.schemes_downloaded)).scalar() or 0
            total_downloads = total_session_downloads + total_scheme_downloads
            
            return jsonify({
                "total_users": total_users,
                "premium_users": premium_users,
                "active_users": active_users,
                "total_downloads": total_downloads,
                "session_downloads": total_session_downloads,
                "scheme_downloads": total_scheme_downloads
            }), 200
        finally:
            db.close()
    except Exception as e:
        return jsonify({"detail": "Failed to get stats"}), 500

@app.route('/admin/notify', methods=['POST', 'OPTIONS'])
def send_notification():
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        data = request.get_json()
        user_ids = data.get('user_ids', [])
        message = data.get('message', '')
        
        if not user_ids or not message:
            return jsonify({"detail": "User IDs and message required"}), 400
        
        logger.info(f"Notification sent to {len(user_ids)} users: {message}")
        return jsonify({"message": f"Notification sent to {len(user_ids)} users"}), 200
    except Exception as e:
        return jsonify({"detail": "Failed to send notification"}), 500

if __name__ == '__main__':
    app.run(debug=True)