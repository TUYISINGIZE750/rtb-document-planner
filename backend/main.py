from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql import func
from datetime import datetime
import hashlib
import tempfile
import os
import logging
from io import BytesIO

from document_generator import (
    generate_session_plan_docx,
    generate_scheme_of_work_docx
)
from ai_content_generator import generate_session_plan_content

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

CORS(app, origins=["*"])

# Use PostgreSQL in production, SQLite for local development
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///./rtb_planner.db')

# Fix for Render PostgreSQL URL (postgres:// -> postgresql://)
if DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)

# Create engine with appropriate settings
if DATABASE_URL.startswith('postgresql://'):
    engine = create_engine(DATABASE_URL)
else:
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

    notifications = relationship("Notification", back_populates="user", cascade="all, delete-orphan")

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
    range = Column(Text)
    appendix = Column(Text)
    school_name = Column(String(500))
    school_logo = Column(Text)
    province = Column(String(255))
    district = Column(String(255))
    sector_location = Column(String(255))
    cell = Column(String(255))
    village = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class SchemeOfWork(Base):
    __tablename__ = "schemes_of_work"
    id = Column(Integer, primary_key=True, index=True)
    user_phone = Column(String(50), nullable=False)
    province = Column(String(255))
    district = Column(String(255))
    sector = Column(String(255))
    sector_location = Column(String(255))
    cell = Column(String(255))
    village = Column(String(255))
    school = Column(String(255))
    school_name = Column(String(500))
    school_logo = Column(Text)
    department_trade = Column(String(255))
    trade = Column(String(255))
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
    term1_competence = Column(Text)
    term1_learning_outcomes = Column(Text)
    term1_indicative_contents = Column(Text)
    term1_duration = Column(Text)
    term1_learning_place = Column(Text)
    term2_weeks = Column(Text)
    term2_competence = Column(Text)
    term2_learning_outcomes = Column(Text)
    term2_indicative_contents = Column(Text)
    term2_duration = Column(Text)
    term2_learning_place = Column(Text)
    term3_weeks = Column(Text)
    term3_competence = Column(Text)
    term3_learning_outcomes = Column(Text)
    term3_indicative_contents = Column(Text)
    term3_duration = Column(Text)
    term3_learning_place = Column(Text)
    prepared_by_name = Column(String(255))
    prepared_by_position = Column(String(255))
    verified_by_name = Column(String(255))
    verified_by_position = Column(String(255))
    approved_by_name = Column(String(255))
    approved_by_position = Column(String(255))
    dos_name = Column(String(255))
    manager_name = Column(String(255))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Notification(Base):
    __tablename__ = "notifications"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(255), nullable=False)
    message = Column(Text, nullable=False)
    type = Column(String(50), default='info')
    is_read = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User", back_populates="notifications", lazy='joined')

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
        "version": "2.6",
        "deployment": "DB_MIGRATION_READY",
        "features": ["authentication", "docx_generation", "ai_content"],
        "users_count": users_count,
        "migration_endpoint": "/admin/migrate-db"
    })

@app.route('/test-scheme', methods=['GET', 'OPTIONS'])
def test_scheme():
    """Test endpoint to verify scheme generation works"""
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        test_data = {
            'province': 'Kigali City',
            'district': 'Gasabo',
            'sector': 'ICT',
            'school': 'Test School',
            'trainer_name': 'Test Trainer',
            'department_trade': 'ICT',
            'module_code_title': 'TEST101',
            'school_year': '2024-2025',
            'module_hours': '120',
            'qualification_title': 'Test Qualification',
            'terms': 'Term 1',
            'rqf_level': 'Level 5',
            'number_of_classes': '1',
            'class_name': 'Test Class',
            'term1_weeks': '1-4',
            'term1_learning_outcomes': 'LO1: Test outcome 1\nLO2: Test outcome 2',
            'term1_indicative_contents': 'IC1: Test content 1\nIC2: Test content 2',
            'term1_duration': '40 hours',
            'term1_learning_place': 'Lab'
        }
        
        logger.info("Testing scheme generation...")
        file_path = generate_scheme_of_work_docx(test_data)
        
        if file_path and os.path.exists(file_path):
            file_size = os.path.getsize(file_path)
            os.remove(file_path)
            return jsonify({
                "status": "success",
                "message": "Scheme generation working",
                "file_size": file_size
            }), 200
        else:
            return jsonify({
                "status": "error",
                "message": "File not generated"
            }), 500
    except Exception as e:
        logger.error(f"Test scheme error: {str(e)}")
        import traceback
        return jsonify({
            "status": "error",
            "message": str(e),
            "traceback": traceback.format_exc()
        }), 500

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
@app.route('/session-plans', methods=['POST', 'OPTIONS'])
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

            if not user.is_premium and user.session_plans_downloaded >= user.session_plans_limit:
                return jsonify({"detail": "Download limit reached. Please upgrade to premium."}), 403

            logger.info(f"🤖 Generating AI content for topic: {data.get('topic_of_session')}")
            data = generate_session_plan_content(data)
            logger.info(f"✅ AI returned - Objectives: {len(data.get('objectives', ''))} chars")
            logger.info(f"✅ Activities: {len(data.get('learning_activities', ''))} chars")
            logger.info(f"✅ Assessment: {len(data.get('assessment_details', ''))} chars")
            logger.info(f"✅ References: {len(data.get('references', ''))} chars")

            session_plan = SessionPlan(
                user_phone=user_phone,
                sector=data.get('sector'),
                sub_sector=data.get('sub_sector'),
                trade=data.get('trade'),
                qualification_title=data.get('qualification_title'),
                rqf_level=data.get('rqf_level') or data.get('level'),
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
                references=data.get('references'),
                range=data.get('range'),
                appendix=data.get('appendix'),
                school_name=data.get('school_name'),
                school_logo=data.get('school_logo'),
                province=data.get('province'),
                district=data.get('district'),
                sector_location=data.get('sector_location'),
                cell=data.get('cell'),
                village=data.get('village')
            )

            db.add(session_plan)

            if not user.is_premium:
                user.session_plans_downloaded += 1
            db.commit()

            return jsonify({"id": session_plan.id, "message": "Session plan created successfully"}), 201
        finally:
            db.close()
    except Exception as e:
        return jsonify({"detail": "Generation failed"}), 500

@app.route('/session-plans/<int:plan_id>/download', methods=['GET', 'OPTIONS'])
def download_session_plan(plan_id):
    if request.method == 'OPTIONS':
        return '', 204

    phone = request.args.get('phone')
    if not phone:
        return jsonify({"detail": "Phone parameter required"}), 400

    db = SessionLocal()
    try:
        session_plan = db.query(SessionPlan).filter(SessionPlan.id == plan_id).first()
        if not session_plan:
            return jsonify({"detail": "Session plan not found"}), 404

        user = db.query(User).filter(User.phone == phone).first()
        if not user:
            return jsonify({"detail": "User not found"}), 404

        data = {
            'sector': session_plan.sector or '',
            'sub_sector': session_plan.sub_sector or '',
            'trade': session_plan.trade or '',
            'qualification_title': session_plan.qualification_title or '',
            'level': session_plan.rqf_level or '',
            'module_code_title': session_plan.module_code_title or '',
            'term': session_plan.term or '',
            'week': session_plan.week or '',
            'date': session_plan.date or '',
            'trainer_name': session_plan.trainer_name or '',
            'class_name': session_plan.class_name or '',
            'number_of_trainees': session_plan.number_of_trainees or '',
            'learning_outcomes': session_plan.learning_outcomes or '',
            'indicative_contents': session_plan.indicative_contents or '',
            'topic_of_session': session_plan.topic_of_session or '',
            'duration': session_plan.duration or '',
            'objectives': session_plan.objectives or '',
            'facilitation_techniques': session_plan.facilitation_techniques or '',
            'learning_activities': session_plan.learning_activities or '',
            'resources': session_plan.resources or '',
            'assessment_details': session_plan.assessment_details or '',
            'references': session_plan.references or '',
            'range': session_plan.range or '',
            'appendix': session_plan.appendix or '',
            'school_name': session_plan.school_name or '',
            'school_logo': session_plan.school_logo or '',
            'school_year': '2024-2025',
            'province': session_plan.province or '',
            'district': session_plan.district or '',
            'sector_location': session_plan.sector_location or '',
            'cell': session_plan.cell or '',
            'village': session_plan.village or ''
        }

        logger.info(f"📄 Generating document for plan ID: {session_plan.id}")
        
        file_path = generate_session_plan_docx(data)
        
        if not file_path:
            logger.error(f"❌ generate_session_plan_docx returned None")
            return jsonify({"detail": "Document generation failed"}), 500
            
        logger.info(f"✅ Document generated at: {file_path}")
        
        if not os.path.exists(file_path):
            logger.error(f'❌ Generated file does not exist: {file_path}')
            return jsonify({"detail": "Generated file not found"}), 500

        filename = f"RTB_Session_Plan_{plan_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.docx"

        with open(file_path, 'rb') as f:
            file_data = f.read()

        try:
            os.remove(file_path)
        except:
            pass

        try:
            return send_file(
                BytesIO(file_data),
                mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                as_attachment=True,
                download_name=filename
            )
        except TypeError:
            return send_file(
                BytesIO(file_data),
                mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                as_attachment=True,
                attachment_filename=filename
            )
    except Exception as e:
        logger.error(f'Session plan download error: {str(e)}')
        import traceback
        logger.error(traceback.format_exc())
        return jsonify({"detail": f"Download failed: {str(e)}"}), 500
    finally:
        db.close()





@app.route('/user-limits/<path:phone>', methods=['GET', 'OPTIONS'])
def get_user_limits(phone):
    if request.method == 'OPTIONS':
        return '', 204

    try:
        from urllib.parse import unquote
        phone = unquote(phone)
        logger.info(f"Getting limits for phone: {phone}")
        
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.phone == phone).first()
            if not user:
                logger.warning(f"User not found for phone: {phone}")
                return jsonify({"detail": "User not found", "phone": phone}), 404

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
        logger.error(f"Error getting limits: {str(e)}")
        return jsonify({"detail": f"Failed to get limits: {str(e)}"}), 500

@app.route('/schemes/generate', methods=['POST', 'OPTIONS'])
@app.route('/schemes', methods=['POST', 'OPTIONS'])
def generate_scheme():
    if request.method == 'OPTIONS':
        return '', 204

    try:
        data = request.get_json()
        logger.info(f"Received scheme data: {list(data.keys()) if data else 'None'}")
        user_phone = data.get('user_phone')
        format_type = data.get('format', 'docx')

        if not user_phone:
            return jsonify({"detail": "User phone required"}), 400

        db = SessionLocal()
        try:
            user = db.query(User).filter(User.phone == user_phone).first()
            if not user:
                return jsonify({"detail": "User not found"}), 404

            if not user.is_premium and user.schemes_downloaded >= user.schemes_limit:
                return jsonify({"detail": "Download limit reached. Please upgrade to premium."}), 403

            scheme = SchemeOfWork(
                user_phone=user_phone,
                province=data.get('province'),
                district=data.get('district'),
                sector=data.get('sector'),
                sector_location=data.get('sector_location'),
                cell=data.get('cell'),
                village=data.get('village'),
                school=data.get('school') or data.get('school_name'),
                school_name=data.get('school_name') or data.get('school'),
                school_logo=data.get('school_logo'),
                department_trade=data.get('department_trade') or data.get('trade'),
                trade=data.get('trade') or data.get('department_trade'),
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
                term1_competence=data.get('term1_competence'),
                term1_learning_outcomes=data.get('term1_learning_outcomes'),
                term1_indicative_contents=data.get('term1_indicative_contents'),
                term1_duration=data.get('term1_duration'),
                term1_learning_place=data.get('term1_learning_place') or '',
                term2_weeks=data.get('term2_weeks'),
                term2_competence=data.get('term2_competence'),
                term2_learning_outcomes=data.get('term2_learning_outcomes'),
                term2_indicative_contents=data.get('term2_indicative_contents'),
                term2_duration=data.get('term2_duration'),
                term2_learning_place=data.get('term2_learning_place') or '',
                term3_weeks=data.get('term3_weeks'),
                term3_competence=data.get('term3_competence'),
                term3_learning_outcomes=data.get('term3_learning_outcomes'),
                term3_indicative_contents=data.get('term3_indicative_contents'),
                term3_duration=data.get('term3_duration'),
                term3_learning_place=data.get('term3_learning_place') or '',
                prepared_by_name=data.get('prepared_by_name'),
                prepared_by_position=data.get('prepared_by_position'),
                verified_by_name=data.get('verified_by_name'),
                verified_by_position=data.get('verified_by_position'),
                approved_by_name=data.get('approved_by_name'),
                approved_by_position=data.get('approved_by_position'),
                dos_name=data.get('dos_name') or data.get('verified_by_name'),
                manager_name=data.get('manager_name') or data.get('approved_by_name')
            )

            db.add(scheme)

            if not user.is_premium:
                user.schemes_downloaded += 1
            db.commit()

            return jsonify({"id": scheme.id, "message": "Scheme of work created successfully"}), 201
        finally:
            db.close()
    except Exception as e:
        logger.error(f"Scheme generation error: {str(e)}")
        import traceback
        logger.error(traceback.format_exc())
        return jsonify({"detail": f"Generation failed: {str(e)}"}), 500

@app.route('/schemes-of-work/<int:scheme_id>/download', methods=['GET', 'OPTIONS'])
def download_scheme_of_work(scheme_id):
    if request.method == 'OPTIONS':
        response = jsonify({})
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET, OPTIONS')
        return response, 204

    try:
        phone = request.args.get('phone')
        if not phone:
            return jsonify({"detail": "Phone parameter required"}), 400

        db = SessionLocal()
        try:
            scheme = db.query(SchemeOfWork).filter(SchemeOfWork.id == scheme_id).first()
            if not scheme:
                return jsonify({"detail": "Scheme of work not found"}), 404

            user = db.query(User).filter(User.phone == phone).first()
            if not user:
                return jsonify({"detail": "User not found"}), 404

            data = {
                'province': scheme.province or '',
                'district': scheme.district or '',
                'sector': scheme.sector or '',
                'school': scheme.school or '',
                'school_name': scheme.school or '',
                'department_trade': scheme.department_trade or '',
                'trade': scheme.department_trade or '',
                'qualification_title': scheme.qualification_title or '',
                'rqf_level': scheme.rqf_level or '',
                'module_code_title': scheme.module_code_title or '',
                'school_year': scheme.school_year or '',
                'terms': scheme.terms or '',
                'module_hours': scheme.module_hours or '',
                'number_of_classes': scheme.number_of_classes or '',
                'class_name': scheme.class_name or '',
                'trainer_name': scheme.trainer_name or '',
                'term1_weeks': scheme.term1_weeks or '',
                'term1_learning_outcomes': scheme.term1_learning_outcomes or '',
                'term1_indicative_contents': scheme.term1_indicative_contents or '',
                'term1_duration': scheme.term1_duration or '',
                'term1_learning_place': scheme.term1_learning_place or '',
                'term2_weeks': scheme.term2_weeks or '',
                'term2_learning_outcomes': scheme.term2_learning_outcomes or '',
                'term2_indicative_contents': scheme.term2_indicative_contents or '',
                'term2_duration': scheme.term2_duration or '',
                'term2_learning_place': scheme.term2_learning_place or '',
                'term3_weeks': scheme.term3_weeks or '',
                'term3_learning_outcomes': scheme.term3_learning_outcomes or '',
                'term3_indicative_contents': scheme.term3_indicative_contents or '',
                'term3_duration': scheme.term3_duration or '',
                'term3_learning_place': scheme.term3_learning_place or '',
                'dos_name': scheme.dos_name or '',
                'manager_name': scheme.manager_name or ''
            }

            logger.info(f'📄 Generating scheme document for ID: {scheme_id}')
            logger.info(f'📊 Data keys: {list(data.keys())}')
            
            file_path = generate_scheme_of_work_docx(data)
            
            logger.info(f'📄 Generated file path: {file_path}')
            
            if not file_path:
                logger.error(f'❌ generate_scheme_of_work_docx returned None')
                return jsonify({"detail": "Document generation returned no file"}), 500
                
            if not os.path.exists(file_path):
                logger.error(f'❌ Generated file does not exist: {file_path}')
                return jsonify({"detail": "Generated file not found"}), 500

            filename = f"RTB_Scheme_of_Work_{scheme_id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.docx"
            logger.info(f'Sending file: {file_path} as {filename}')

            try:
                with open(file_path, 'rb') as f:
                    file_data = f.read()

                try:
                    response = send_file(
                        BytesIO(file_data),
                        mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                        as_attachment=True,
                        download_name=filename
                    )
                except TypeError:
                    response = send_file(
                        BytesIO(file_data),
                        mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                        as_attachment=True,
                        attachment_filename=filename
                    )
                
                # Add CORS and download headers
                response.headers['Access-Control-Allow-Origin'] = '*'
                response.headers['Access-Control-Expose-Headers'] = 'Content-Disposition'
                response.headers['Content-Disposition'] = f'attachment; filename="{filename}"'
                response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'
                return response
            except Exception as send_error:
                logger.error(f'Error sending file: {str(send_error)}')
                return jsonify({"detail": f"Download failed: {str(send_error)}"}), 500
            finally:
                try:
                    if file_path and os.path.exists(file_path):
                        os.remove(file_path)
                        logger.info(f'Cleaned up temp file: {file_path}')
                except Exception as cleanup_error:
                    logger.warning(f'Could not clean up temp file: {str(cleanup_error)}')
        finally:
            db.close()
    except Exception as e:
        logger.error(f'Scheme download error: {str(e)}')
        import traceback
        logger.error(traceback.format_exc())
        return jsonify({"detail": f"Download failed: {str(e)}"}), 500





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
        title = data.get('title', 'Notification')
        notif_type = data.get('type', 'info')

        if not user_ids or not message:
            return jsonify({"detail": "User IDs and message required"}), 400

        db = SessionLocal()
        try:
            users = db.query(User).filter(User.id.in_(user_ids)).all()
            if not users:
                return jsonify({"detail": "No valid users found"}), 404

            for user in users:
                notification = Notification(
                    user_id=user.id,
                    title=title,
                    message=message,
                    type=notif_type
                )
                db.add(notification)
            db.commit()
            return jsonify({"message": f"Notification sent to {len(users)} users"}), 200
        finally:
            db.close()
    except Exception as e:
        logger.error(f"Notification error: {e}")
        return jsonify({"detail": "Failed to send notification"}), 500

@app.route('/users/<phone>/status', methods=['PUT', 'OPTIONS'])
def update_user_status(phone):
    if request.method == 'OPTIONS':
        return '', 204

    try:
        data = request.get_json()
        is_active = data.get('is_active')

        db = SessionLocal()
        try:
            user = db.query(User).filter(User.phone == phone).first()
            if not user:
                return jsonify({"detail": "User not found"}), 404

            user.is_active = is_active
            db.commit()
            return jsonify({"message": "Status updated"}), 200
        finally:
            db.close()
    except Exception as e:
        return jsonify({"detail": "Failed to update status"}), 500

@app.route('/users/<phone>/premium', methods=['PUT', 'OPTIONS'])
def update_user_premium(phone):
    if request.method == 'OPTIONS':
        return '', 204

    try:
        data = request.get_json()
        is_premium = data.get('is_premium')

        db = SessionLocal()
        try:
            user = db.query(User).filter(User.phone == phone).first()
            if not user:
                return jsonify({"detail": "User not found"}), 404

            user.is_premium = is_premium
            if is_premium:
                user.session_plans_limit = 999
                user.schemes_limit = 999
            else:
                user.session_plans_limit = 2
                user.schemes_limit = 2
            db.commit()
            return jsonify({"message": "Premium updated"}), 200
        finally:
            db.close()
    except Exception as e:
        return jsonify({"detail": "Failed to update premium"}), 500

@app.route('/users/<phone>', methods=['PUT', 'OPTIONS'])
def update_user(phone):
    if request.method == 'OPTIONS':
        return '', 204

    try:
        data = request.get_json()

        db = SessionLocal()
        try:
            user = db.query(User).filter(User.phone == phone).first()
            if not user:
                return jsonify({"detail": "User not found"}), 404

            user.name = data.get('name', user.name)
            user.institution = data.get('institution', user.institution)
            user.session_plans_limit = data.get('session_plans_limit', user.session_plans_limit)
            user.schemes_limit = data.get('schemes_limit', user.schemes_limit)
            user.is_premium = data.get('is_premium', user.is_premium)
            user.is_active = data.get('is_active', user.is_active)
            db.commit()
            return jsonify({"message": "User updated"}), 200
        finally:
            db.close()
    except Exception as e:
        return jsonify({"detail": "Failed to update user"}), 500

@app.route('/users/<phone>/notifications', methods=['GET', 'OPTIONS'])
def get_user_notifications_by_phone(phone):
    if request.method == 'OPTIONS':
        return '', 204

    try:
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.phone == phone).first()
            if not user:
                return jsonify([]), 200

            notifications = db.query(Notification).filter(Notification.user_id == user.id).order_by(Notification.created_at.desc()).all()
            return jsonify([
                {
                    "id": n.id,
                    "title": n.title,
                    "message": n.message,
                    "type": n.type,
                    "is_read": n.is_read,
                    "created_at": n.created_at.isoformat() if n.created_at else None
                } for n in notifications
            ]), 200
        finally:
            db.close()
    except Exception as e:
        logger.error(f"Get notifications error: {e}")
        return jsonify([]), 200

@app.route('/notifications/user/<int:user_id>', methods=['GET', 'OPTIONS'])
def get_user_notifications(user_id):
    if request.method == 'OPTIONS':
        return '', 204

    try:
        db = SessionLocal()
        try:
            notifications = db.query(Notification).filter(Notification.user_id == user_id).order_by(Notification.created_at.desc()).all()
            return jsonify([
                {
                    "id": n.id,
                    "title": n.title,
                    "message": n.message,
                    "type": n.type,
                    "is_read": n.is_read,
                    "created_at": n.created_at.isoformat() if n.created_at else None
                } for n in notifications
            ]), 200
        finally:
            db.close()
    except Exception as e:
        logger.error(f"Get notifications error: {e}")
        return jsonify([]), 200

@app.route('/notifications/<int:notification_id>/read', methods=['PUT', 'OPTIONS'])
def mark_notification_read(notification_id):
    if request.method == 'OPTIONS':
        return '', 204

    try:
        db = SessionLocal()
        try:
            notification = db.query(Notification).filter(Notification.id == notification_id).first()
            if not notification:
                return jsonify({"detail": "Notification not found"}), 404
            notification.is_read = True
            db.commit()
            return jsonify({"message": "Notification marked as read"}), 200
        finally:
            db.close()
    except Exception as e:
        logger.error(f"Mark notification read error: {e}")
        return jsonify({"detail": "Failed to update notification"}), 500

@app.route('/notifications/unread/<int:user_id>', methods=['GET', 'OPTIONS'])
def get_unread_count(user_id):
    if request.method == 'OPTIONS':
        return '', 204

    try:
        db = SessionLocal()
        try:
            count = db.query(Notification).filter(Notification.user_id == user_id, Notification.is_read == False).count()
            return jsonify({"unread_count": count}), 200
        finally:
            db.close()
    except Exception as e:
        logger.error(f"Unread count error: {e}")
        return jsonify({"unread_count": 0}), 200

@app.route('/notifications/broadcast', methods=['POST', 'OPTIONS'])
def broadcast_notification():
    if request.method == 'OPTIONS':
        return '', 204

    try:
        data = request.get_json()
        target = data.get('target', 'all')
        message = data.get('message', '')
        title = data.get('title', 'Notification')
        notif_type = data.get('type', 'info')

        if not message:
            return jsonify({"detail": "Message required"}), 400

        db = SessionLocal()
        try:
            query = db.query(User)
            if target == 'premium':
                query = query.filter(User.is_premium == True)
            elif target == 'free':
                query = query.filter(User.is_premium == False)
            elif target == 'inactive':
                query = query.filter(User.is_active == False)
            users = query.all()

            if not users:
                return jsonify({"detail": "No users for selected target"}), 404

            for user in users:
                notification = Notification(
                    user_id=user.id,
                    title=title,
                    message=message,
                    type=notif_type
                )
                db.add(notification)
            db.commit()
            return jsonify({"message": f"Notification sent to {len(users)} users"}), 200
        finally:
            db.close()
    except Exception as e:
        logger.error(f"Broadcast error: {e}")
        return jsonify({"detail": "Failed to send notification"}), 500

@app.route('/notifications/send', methods=['POST', 'OPTIONS'])
def send_personal_notification():
    if request.method == 'OPTIONS':
        return '', 204

    try:
        data = request.get_json()
        recipient = data.get('recipient', '')
        message = data.get('message', '')
        title = data.get('title', 'Message')
        notif_type = data.get('type', 'info')

        if not recipient or not message:
            return jsonify({"detail": "Recipient and message required"}), 400

        db = SessionLocal()
        try:
            user = db.query(User).filter(User.phone == recipient).first()
            if not user:
                return jsonify({"detail": "Recipient not found"}), 404

            notification = Notification(
                user_id=user.id,
                title=title,
                message=message,
                type=notif_type
            )
            db.add(notification)
            db.commit()
            return jsonify({"message": "Message sent"}), 200
        finally:
            db.close()
    except Exception as e:
        logger.error(f"Personal notification error: {e}")
        return jsonify({"detail": "Failed to send message"}), 500

@app.route('/settings', methods=['GET', 'OPTIONS'])
def get_settings():
    if request.method == 'OPTIONS':
        return '', 204
    
    return jsonify({
        "session_plan_price": 33,
        "scheme_price": 79,
        "weekly_session_bundle": 556,
        "weekly_scheme_bundle": 777,
        "monthly_session_bundle": 1109,
        "monthly_scheme_bundle": 2300,
        "unlimited_monthly": 5300,
        "payment_phone": "+250789751597",
        "payment_name": "TUYISINGIZE Leonard"
    }), 200

@app.route('/admin/migrate-db', methods=['POST', 'OPTIONS'])
def migrate_database():
    """Add ALL missing columns to schemes_of_work table"""
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        from sqlalchemy import text
        db = SessionLocal()
        try:
            columns_to_add = [
                ('sector_location', 'VARCHAR(255)'),
                ('cell', 'VARCHAR(255)'),
                ('village', 'VARCHAR(255)')
            ]
            
            added = []
            for col_name, col_type in columns_to_add:
                # Check if column exists
                result = db.execute(text(f"""
                    SELECT column_name 
                    FROM information_schema.columns 
                    WHERE table_name='schemes_of_work' AND column_name='{col_name}'
                """))
                
                if not result.fetchone():
                    # Add column
                    db.execute(text(f"""
                        ALTER TABLE schemes_of_work 
                        ADD COLUMN {col_name} {col_type}
                    """))
                    added.append(col_name)
            
            db.commit()
            
            if added:
                return jsonify({"message": f"Migration successful - added columns: {', '.join(added)}"}), 200
            else:
                return jsonify({"message": "All columns already exist"}), 200
        finally:
            db.close()
    except Exception as e:
        logger.error(f"Migration error: {e}")
        import traceback
        logger.error(traceback.format_exc())
        return jsonify({"detail": f"Migration failed: {str(e)}"}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=False)
