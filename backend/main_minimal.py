from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql import func
from datetime import datetime
import hashlib
import os
import logging
from io import BytesIO

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app, origins=["*"])

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
    term1_learning_place = Column(Text)
    term2_weeks = Column(Text)
    term2_learning_outcomes = Column(Text)
    term2_indicative_contents = Column(Text)
    term2_duration = Column(Text)
    term2_learning_place = Column(Text)
    term3_weeks = Column(Text)
    term3_learning_outcomes = Column(Text)
    term3_indicative_contents = Column(Text)
    term3_duration = Column(Text)
    term3_learning_place = Column(Text)
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
    return jsonify({"message": "RTB API Online", "status": "ok", "cors": "enabled"})

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
        logger.error(f"Registration error: {e}")
        return jsonify({"detail": str(e)}), 500

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
        logger.error(f"Login error: {e}")
        return jsonify({"detail": str(e)}), 500

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
            return jsonify({
                "total_users": total_users,
                "premium_users": premium_users,
                "active_users": active_users,
                "total_downloads": total_session_downloads + total_scheme_downloads,
                "session_downloads": total_session_downloads,
                "scheme_downloads": total_scheme_downloads
            }), 200
        finally:
            db.close()
    except Exception as e:
        logger.error(f"Stats error: {e}")
        return jsonify({"detail": str(e)}), 500

@app.route('/users/', methods=['GET', 'OPTIONS'])
@app.route('/admin/users', methods=['GET', 'OPTIONS'])
def get_all_users():
    if request.method == 'OPTIONS':
        return '', 204
    try:
        db = SessionLocal()
        try:
            users = db.query(User).all()
            return jsonify([{
                "id": u.id,
                "user_id": u.user_id,
                "name": u.name,
                "phone": u.phone,
                "email": u.email,
                "institution": u.institution,
                "role": u.role,
                "is_premium": u.is_premium,
                "is_active": u.is_active,
                "session_plans_limit": u.session_plans_limit,
                "schemes_limit": u.schemes_limit,
                "session_plans_downloaded": u.session_plans_downloaded,
                "schemes_downloaded": u.schemes_downloaded,
                "created_at": u.created_at.isoformat() if u.created_at else None
            } for u in users]), 200
        finally:
            db.close()
    except Exception as e:
        logger.error(f"Get users error: {e}")
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
            return jsonify({"message": "User activated"}), 200
        finally:
            db.close()
    except Exception as e:
        logger.error(f"Activate error: {e}")
        return jsonify({"detail": str(e)}), 500

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
            return jsonify({"message": "User deactivated"}), 200
        finally:
            db.close()
    except Exception as e:
        logger.error(f"Deactivate error: {e}")
        return jsonify({"detail": str(e)}), 500

@app.route('/admin/users/<int:user_id>/upgrade', methods=['POST', 'OPTIONS'])
def upgrade_user(user_id):
    if request.method == 'OPTIONS':
        return '', 204
    try:
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.id == user_id).first()
            if not user:
                return jsonify({"detail": "User not found"}), 404
            user.is_premium = True
            user.session_plans_limit = 999
            user.schemes_limit = 999
            db.commit()
            return jsonify({"message": "User upgraded"}), 200
        finally:
            db.close()
    except Exception as e:
        logger.error(f"Upgrade error: {e}")
        return jsonify({"detail": str(e)}), 500

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
            return jsonify({"message": "User downgraded"}), 200
        finally:
            db.close()
    except Exception as e:
        logger.error(f"Downgrade error: {e}")
        return jsonify({"detail": str(e)}), 500

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
        logger.error(f"Get limits error: {e}")
        return jsonify({"detail": str(e)}), 500

@app.route('/session-plans', methods=['POST', 'OPTIONS'])
@app.route('/session-plans/generate', methods=['POST', 'OPTIONS'])
def generate_session_plan():
    if request.method == 'OPTIONS':
        return '', 204
    try:
        data = request.get_json()
        user_phone = data.get('user_phone')
        if not user_phone:
            return jsonify({"detail": "User phone required"}), 400
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.phone == user_phone).first()
            if not user:
                return jsonify({"detail": "User not found"}), 404
            if not user.is_premium and user.session_plans_downloaded >= user.session_plans_limit:
                return jsonify({"detail": "Download limit reached"}), 403
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
            if not user.is_premium:
                user.session_plans_downloaded += 1
            db.commit()
            return jsonify({"id": session_plan.id, "message": "Session plan created"}), 201
        finally:
            db.close()
    except Exception as e:
        logger.error(f"Session plan error: {e}")
        return jsonify({"detail": str(e)}), 500

@app.route('/schemes', methods=['POST', 'OPTIONS'])
@app.route('/schemes/generate', methods=['POST', 'OPTIONS'])
def generate_scheme():
    if request.method == 'OPTIONS':
        return '', 204
    try:
        data = request.get_json()
        user_phone = data.get('user_phone')
        if not user_phone:
            return jsonify({"detail": "User phone required"}), 400
        db = SessionLocal()
        try:
            user = db.query(User).filter(User.phone == user_phone).first()
            if not user:
                return jsonify({"detail": "User not found"}), 404
            if not user.is_premium and user.schemes_downloaded >= user.schemes_limit:
                return jsonify({"detail": "Download limit reached"}), 403
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
                term1_learning_place=data.get('term1_learning_place'),
                term2_weeks=data.get('term2_weeks'),
                term2_learning_outcomes=data.get('term2_learning_outcomes'),
                term2_indicative_contents=data.get('term2_indicative_contents'),
                term2_duration=data.get('term2_duration'),
                term2_learning_place=data.get('term2_learning_place'),
                term3_weeks=data.get('term3_weeks'),
                term3_learning_outcomes=data.get('term3_learning_outcomes'),
                term3_indicative_contents=data.get('term3_indicative_contents'),
                term3_duration=data.get('term3_duration'),
                term3_learning_place=data.get('term3_learning_place'),
                dos_name=data.get('dos_name'),
                manager_name=data.get('manager_name')
            )
            db.add(scheme)
            if not user.is_premium:
                user.schemes_downloaded += 1
            db.commit()
            return jsonify({"id": scheme.id, "message": "Scheme created"}), 201
        finally:
            db.close()
    except Exception as e:
        logger.error(f"Scheme error: {e}")
        return jsonify({"detail": str(e)}), 500

@app.route('/session-plans/<int:plan_id>/download', methods=['GET', 'OPTIONS'])
def download_session_plan(plan_id):
    if request.method == 'OPTIONS':
        return '', 204
    try:
        phone = request.args.get('phone')
        if not phone:
            return jsonify({"detail": "Phone required"}), 400
        db = SessionLocal()
        try:
            plan = db.query(SessionPlan).filter(SessionPlan.id == plan_id).first()
            if not plan:
                return jsonify({"detail": "Session plan not found"}), 404
            user = db.query(User).filter(User.phone == phone).first()
            if not user:
                return jsonify({"detail": "User not found"}), 404
            
            try:
                from document_generator import generate_session_plan_docx
                data = {
                    'sector': plan.sector, 'sub_sector': plan.sub_sector, 'trade': plan.trade,
                    'qualification_title': plan.qualification_title, 'rqf_level': plan.rqf_level,
                    'module_code_title': plan.module_code_title, 'term': plan.term, 'week': plan.week,
                    'date': plan.date, 'trainer_name': plan.trainer_name, 'class_name': plan.class_name,
                    'number_of_trainees': plan.number_of_trainees, 'learning_outcomes': plan.learning_outcomes,
                    'indicative_contents': plan.indicative_contents, 'topic_of_session': plan.topic_of_session,
                    'duration': plan.duration, 'objectives': plan.objectives,
                    'facilitation_techniques': plan.facilitation_techniques, 'learning_activities': plan.learning_activities,
                    'resources': plan.resources, 'assessment_details': plan.assessment_details, 'references': plan.references
                }
                file_path = generate_session_plan_docx(data)
                if file_path and os.path.exists(file_path):
                    filename = f"RTB_Session_Plan_{plan_id}.docx"
                    with open(file_path, 'rb') as f:
                        file_data = f.read()
                    try:
                        os.remove(file_path)
                    except:
                        pass
                    return send_file(BytesIO(file_data), mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document', as_attachment=True, download_name=filename)
            except Exception as gen_error:
                logger.error(f"Generation error: {gen_error}")
                return jsonify({"detail": "Document generation not available yet"}), 503
        finally:
            db.close()
    except Exception as e:
        logger.error(f"Download error: {e}")
        return jsonify({"detail": str(e)}), 500

@app.route('/schemes-of-work/<int:scheme_id>/download', methods=['GET', 'OPTIONS'])
def download_scheme(scheme_id):
    if request.method == 'OPTIONS':
        return '', 204
    try:
        phone = request.args.get('phone')
        if not phone:
            return jsonify({"detail": "Phone required"}), 400
        db = SessionLocal()
        try:
            scheme = db.query(SchemeOfWork).filter(SchemeOfWork.id == scheme_id).first()
            if not scheme:
                return jsonify({"detail": "Scheme not found"}), 404
            user = db.query(User).filter(User.phone == phone).first()
            if not user:
                return jsonify({"detail": "User not found"}), 404
            
            try:
                from document_generator import generate_scheme_of_work_docx
                data = {
                    'province': scheme.province, 'district': scheme.district, 'sector': scheme.sector,
                    'school': scheme.school, 'department_trade': scheme.department_trade,
                    'qualification_title': scheme.qualification_title, 'rqf_level': scheme.rqf_level,
                    'module_code_title': scheme.module_code_title, 'school_year': scheme.school_year,
                    'terms': scheme.terms, 'module_hours': scheme.module_hours,
                    'number_of_classes': scheme.number_of_classes, 'class_name': scheme.class_name,
                    'trainer_name': scheme.trainer_name, 'term1_weeks': scheme.term1_weeks,
                    'term1_learning_outcomes': scheme.term1_learning_outcomes,
                    'term1_indicative_contents': scheme.term1_indicative_contents,
                    'term1_duration': scheme.term1_duration, 'term1_learning_place': scheme.term1_learning_place,
                    'term2_weeks': scheme.term2_weeks, 'term2_learning_outcomes': scheme.term2_learning_outcomes,
                    'term2_indicative_contents': scheme.term2_indicative_contents,
                    'term2_duration': scheme.term2_duration, 'term2_learning_place': scheme.term2_learning_place,
                    'term3_weeks': scheme.term3_weeks, 'term3_learning_outcomes': scheme.term3_learning_outcomes,
                    'term3_indicative_contents': scheme.term3_indicative_contents,
                    'term3_duration': scheme.term3_duration, 'term3_learning_place': scheme.term3_learning_place,
                    'dos_name': scheme.dos_name, 'manager_name': scheme.manager_name
                }
                file_path = generate_scheme_of_work_docx(data)
                if file_path and os.path.exists(file_path):
                    filename = f"RTB_Scheme_{scheme_id}.docx"
                    with open(file_path, 'rb') as f:
                        file_data = f.read()
                    try:
                        os.remove(file_path)
                    except:
                        pass
                    return send_file(BytesIO(file_data), mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document', as_attachment=True, download_name=filename)
            except Exception as gen_error:
                logger.error(f"Generation error: {gen_error}")
                return jsonify({"detail": "Document generation not available yet"}), 503
        finally:
            db.close()
    except Exception as e:
        logger.error(f"Download error: {e}")
        return jsonify({"detail": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
