from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from datetime import datetime
import hashlib
import tempfile
from simple_document_generator import generate_session_plan_docx, generate_scheme_of_work_docx
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

CORS(app, 
     origins=["https://tuyisingize750.github.io", "http://localhost:5173"],
     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
     allow_headers=["Content-Type", "Authorization"],
     supports_credentials=False)

@app.after_request
def after_request(response):
    origin = request.headers.get('Origin')
    if origin in ["https://tuyisingize750.github.io"]:
        response.headers.add('Access-Control-Allow-Origin', origin)
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

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
    session_plans_limit = Column(Integer, default=5)
    schemes_limit = Column(Integer, default=5)
    session_plans_downloaded = Column(Integer, default=0)
    schemes_downloaded = Column(Integer, default=0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class SessionPlan(Base):
    __tablename__ = "session_plans"
    
    id = Column(Integer, primary_key=True, index=True)
    sector = Column(String(255))
    trade = Column(String(255))
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
    facilitation_techniques = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class SchemeOfWork(Base):
    __tablename__ = "schemes_of_work"
    
    id = Column(Integer, primary_key=True, index=True)
    school = Column(String(255))
    department_trade = Column(String(255))
    module_code_title = Column(String(500))
    trainer_name = Column(String(255))
    school_year = Column(String(100))
    term1_learning_outcomes = Column(Text)
    term1_indicative_contents = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

Base.metadata.create_all(bind=engine)

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password: str, hashed: str) -> bool:
    return hash_password(password) == hashed

@app.route('/', methods=['GET', 'OPTIONS'])
def home():
    if request.method == 'OPTIONS':
        return '', 204
    return jsonify({
        "message": "RTB Document Planner API",
        "status": "online",
        "version": "4.0-complete"
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
                password=hash_password(password),
                role='user',
                is_premium=False,
                is_active=True,
                session_plans_limit=5,
                schemes_limit=5
            )
            
            db.add(user)
            db.commit()
            return jsonify({"message": "User registered successfully"}), 201
            
        finally:
            db.close()
            
    except Exception as e:
        logger.error(f"Registration error: {e}")
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
                return jsonify({"detail": "Account deactivated"}), 403
            
            return jsonify({
                "user_id": user.user_id,
                "name": user.name,
                "phone": user.phone,
                "email": user.email or "",
                "institution": user.institution or "",
                "role": user.role,
                "is_premium": user.is_premium,
                "session_plans_limit": user.session_plans_limit,
                "schemes_limit": user.schemes_limit,
                "session_plans_downloaded": user.session_plans_downloaded,
                "schemes_downloaded": user.schemes_downloaded
            }), 200
            
        finally:
            db.close()
            
    except Exception as e:
        logger.error(f"Login error: {e}")
        return jsonify({"detail": "Login failed"}), 500

@app.route('/session-plans', methods=['POST', 'OPTIONS'])
def create_session_plan():
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        data = request.get_json()
        if not data:
            return jsonify({"detail": "No data provided"}), 400
        
        db = SessionLocal()
        try:
            session_plan = SessionPlan(
                sector=data.get('sector', ''),
                trade=data.get('trade', ''),
                rqf_level=data.get('rqf_level', ''),
                module_code_title=data.get('module_code_title', ''),
                term=data.get('term', ''),
                week=data.get('week', ''),
                date=data.get('date', ''),
                trainer_name=data.get('trainer_name', ''),
                class_name=data.get('class_name', ''),
                number_of_trainees=data.get('number_of_trainees', ''),
                learning_outcomes=data.get('learning_outcomes', ''),
                indicative_contents=data.get('indicative_contents', ''),
                topic_of_session=data.get('topic_of_session', ''),
                duration=data.get('duration', '40'),
                facilitation_techniques=data.get('facilitation_techniques', '')
            )
            
            db.add(session_plan)
            db.commit()
            db.refresh(session_plan)
            
            return jsonify({
                "id": session_plan.id,
                "message": "Session plan created successfully"
            }), 201
            
        finally:
            db.close()
            
    except Exception as e:
        logger.error(f"Session plan creation error: {e}")
        return jsonify({"detail": f"Failed to create session plan: {str(e)}"}), 500

@app.route('/session-plans/<int:plan_id>/download', methods=['GET', 'OPTIONS'])
def download_session_plan(plan_id):
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        db = SessionLocal()
        try:
            session_plan = db.query(SessionPlan).filter(SessionPlan.id == plan_id).first()
            if not session_plan:
                return jsonify({"detail": "Session plan not found"}), 404
            
            docx_path = generate_session_plan_docx(session_plan)
            
            return send_file(
                docx_path,
                as_attachment=True,
                download_name=f"RTB_Session_Plan_{plan_id}.docx",
                mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            )
            
        finally:
            db.close()
            
    except Exception as e:
        logger.error(f"Download error: {e}")
        return jsonify({"detail": "Download failed"}), 500

@app.route('/schemes', methods=['POST', 'OPTIONS'])
def create_scheme():
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        data = request.get_json()
        if not data:
            return jsonify({"detail": "No data provided"}), 400
        
        db = SessionLocal()
        try:
            scheme = SchemeOfWork(
                school=data.get('school', ''),
                department_trade=data.get('department_trade', ''),
                module_code_title=data.get('module_code_title', ''),
                trainer_name=data.get('trainer_name', ''),
                school_year=data.get('school_year', ''),
                term1_learning_outcomes=data.get('term1_learning_outcomes', ''),
                term1_indicative_contents=data.get('term1_indicative_contents', '')
            )
            
            db.add(scheme)
            db.commit()
            db.refresh(scheme)
            
            return jsonify({
                "id": scheme.id,
                "message": "Scheme of work created successfully"
            }), 201
            
        finally:
            db.close()
            
    except Exception as e:
        logger.error(f"Scheme creation error: {e}")
        return jsonify({"detail": f"Failed to create scheme: {str(e)}"}), 500

@app.route('/schemes/<int:scheme_id>/download', methods=['GET', 'OPTIONS'])
def download_scheme(scheme_id):
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        db = SessionLocal()
        try:
            scheme = db.query(SchemeOfWork).filter(SchemeOfWork.id == scheme_id).first()
            if not scheme:
                return jsonify({"detail": "Scheme not found"}), 404
            
            docx_path = generate_scheme_of_work_docx(scheme)
            
            return send_file(
                docx_path,
                as_attachment=True,
                download_name=f"RTB_Scheme_of_Work_{scheme_id}.docx",
                mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            )
            
        finally:
            db.close()
            
    except Exception as e:
        logger.error(f"Download error: {e}")
        return jsonify({"detail": "Download failed"}), 500

if __name__ == '__main__':
    app.run(debug=False)