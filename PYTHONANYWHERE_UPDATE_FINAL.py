"""
FINAL PYTHONANYWHERE UPDATE - COMPLETE BACKEND CODE
Copy this ENTIRE code to PythonAnywhere main.py and reload the web app
"""

from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import io
import json
from datetime import datetime

app = Flask(__name__)

CORS(app, 
     resources={r"/*": {"origins": "*"}},
     allow_headers=["Content-Type", "Authorization", "Accept"],
     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])

users_db = {}
session_plans_db = []
schemes_db = []

# Pre-load admin account
users_db['+250789751597'] = {
    'user_id': 'ADMIN_001',
    'name': 'Administrator',
    'phone': '+250789751597',
    'email': 'admin@rtb.rw',
    'institution': 'RTB',
    'password': 'admin123',
    'role': 'admin',
    'is_premium': True,
    'is_active': True,
    'session_plans_limit': 999,
    'schemes_limit': 999,
    'session_plans_downloaded': 0,
    'schemes_downloaded': 0
}

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,Accept')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/', methods=['GET', 'OPTIONS'])
def home():
    if request.method == 'OPTIONS':
        return '', 204
    return jsonify({
        "message": "RTB Document Planner API", 
        "status": "online", 
        "cors": "enabled", 
        "version": "3.2",
        "users_count": len(users_db),
        "session_plans_count": len(session_plans_db),
        "schemes_count": len(schemes_db)
    })

@app.route('/users/', methods=['GET', 'OPTIONS'])
def get_all_users():
    if request.method == 'OPTIONS':
        return '', 204
    
    users_list = []
    for phone, user in users_db.items():
        user_data = {
            'user_id': user.get('user_id'),
            'name': user.get('name'),
            'phone': phone,
            'email': user.get('email', ''),
            'institution': user.get('institution', ''),
            'role': user.get('role', 'user'),
            'is_premium': user.get('is_premium', False),
            'is_active': user.get('is_active', True),
            'session_plans_limit': user.get('session_plans_limit', 2),
            'schemes_limit': user.get('schemes_limit', 2),
            'session_plans_downloaded': user.get('session_plans_downloaded', 0),
            'schemes_downloaded': user.get('schemes_downloaded', 0)
        }
        users_list.append(user_data)
    
    return jsonify(users_list), 200

@app.route('/users/<phone>', methods=['GET', 'PUT', 'OPTIONS'])
def manage_user(phone):
    if request.method == 'OPTIONS':
        return '', 204
    
    if request.method == 'GET':
        if phone in users_db:
            user = users_db[phone]
            return jsonify({
                'user_id': user.get('user_id'),
                'name': user.get('name'),
                'phone': phone,
                'email': user.get('email', ''),
                'institution': user.get('institution', ''),
                'role': user.get('role', 'user'),
                'is_premium': user.get('is_premium', False),
                'is_active': user.get('is_active', True),
                'session_plans_limit': user.get('session_plans_limit', 2),
                'schemes_limit': user.get('schemes_limit', 2)
            }), 200
        else:
            return jsonify({"detail": "User not found"}), 404
    
    elif request.method == 'PUT':
        if phone not in users_db:
            return jsonify({"detail": "User not found"}), 404
        
        data = request.get_json()
        user = users_db[phone]
        
        if 'name' in data:
            user['name'] = data['name']
        if 'institution' in data:
            user['institution'] = data['institution']
        if 'is_active' in data:
            user['is_active'] = data['is_active']
        if 'is_premium' in data:
            user['is_premium'] = data['is_premium']
        if 'session_plans_limit' in data:
            user['session_plans_limit'] = data['session_plans_limit']
        if 'schemes_limit' in data:
            user['schemes_limit'] = data['schemes_limit']
        
        users_db[phone] = user
        return jsonify({"message": "User updated successfully"}), 200

@app.route('/users/<phone>/status', methods=['PUT', 'OPTIONS'])
def update_user_status(phone):
    if request.method == 'OPTIONS':
        return '', 204
    
    if phone not in users_db:
        return jsonify({"detail": "User not found"}), 404
    
    data = request.get_json()
    users_db[phone]['is_active'] = data.get('is_active', True)
    
    return jsonify({"message": "User status updated successfully"}), 200

@app.route('/users/<phone>/premium', methods=['PUT', 'OPTIONS'])
def update_user_premium(phone):
    if request.method == 'OPTIONS':
        return '', 204
    
    if phone not in users_db:
        return jsonify({"detail": "User not found"}), 404
    
    data = request.get_json()
    is_premium = data.get('is_premium', False)
    users_db[phone]['is_premium'] = is_premium
    
    # Update limits based on premium status
    if is_premium:
        users_db[phone]['session_plans_limit'] = 999
        users_db[phone]['schemes_limit'] = 999
    else:
        users_db[phone]['session_plans_limit'] = 2
        users_db[phone]['schemes_limit'] = 2
    
    return jsonify({"message": "Premium status updated successfully"}), 200

@app.route('/users/register', methods=['POST', 'OPTIONS'])
def register():
    if request.method == 'OPTIONS':
        return '', 204
    
    data = request.get_json()
    phone = data.get('phone')
    password = data.get('password')
    
    if not phone:
        return jsonify({"detail": "Phone required"}), 400
    
    if phone in users_db:
        return jsonify({"detail": "Phone already registered"}), 400
    
    users_db[phone] = {
        'user_id': data.get('user_id'),
        'name': data.get('name'),
        'phone': phone,
        'email': data.get('email', ''),
        'institution': data.get('institution', ''),
        'password': password,
        'role': 'user',
        'is_premium': False,
        'is_active': True,
        'session_plans_limit': 2,
        'schemes_limit': 2,
        'session_plans_downloaded': 0,
        'schemes_downloaded': 0
    }
    
    return jsonify({"message": "User registered successfully"}), 201

@app.route('/users/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        return '', 204
    
    data = request.get_json()
    phone = data.get('phone')
    password = data.get('password')
    
    if not phone or not password:
        return jsonify({"detail": "Phone and password required"}), 400
    
    if phone in users_db:
        user = users_db[phone]
        
        if user.get('password') != password:
            return jsonify({"detail": "Incorrect phone number or password"}), 401
        
        if not user.get('is_active', True):
            return jsonify({"detail": "Account is deactivated. Contact admin."}), 403
        
        return jsonify({
            "user_id": user.get('user_id'),
            "name": user.get('name'),
            "phone": phone,
            "email": user.get('email', ''),
            "institution": user.get('institution', ''),
            "role": user.get('role', 'user'),
            "is_premium": user.get('is_premium', False),
            "session_plans_limit": user.get('session_plans_limit', 2),
            "schemes_limit": user.get('schemes_limit', 2)
        }), 200
    else:
        return jsonify({"detail": "User not found. Please register first."}), 404

@app.route('/user-limits/<phone>')
def user_limits(phone):
    if phone in users_db:
        user = users_db[phone]
        session_plans_remaining = max(0, user.get('session_plans_limit', 2) - user.get('session_plans_downloaded', 0))
        schemes_remaining = max(0, user.get('schemes_limit', 2) - user.get('schemes_downloaded', 0))
        
        return jsonify({
            "session_plans_limit": user.get('session_plans_limit', 2),
            "schemes_limit": user.get('schemes_limit', 2),
            "session_plans_downloaded": user.get('session_plans_downloaded', 0),
            "schemes_downloaded": user.get('schemes_downloaded', 0),
            "session_plans_remaining": session_plans_remaining,
            "schemes_remaining": schemes_remaining,
            "is_premium": user.get('is_premium', False)
        })
    
    return jsonify({
        "session_plans_limit": 2,
        "schemes_limit": 2,
        "session_plans_downloaded": 0,
        "schemes_downloaded": 0,
        "session_plans_remaining": 2,
        "schemes_remaining": 2,
        "is_premium": False
    })

@app.route('/stats', methods=['GET', 'OPTIONS'])
def get_stats():
    if request.method == 'OPTIONS':
        return '', 204
    
    total_users = len(users_db)
    active_users = sum(1 for u in users_db.values() if u.get('is_active', True))
    premium_users = sum(1 for u in users_db.values() if u.get('is_premium', False))
    total_downloads = sum(
        u.get('session_plans_downloaded', 0) + u.get('schemes_downloaded', 0) 
        for u in users_db.values()
    )
    
    return jsonify({
        "total_users": total_users,
        "active_users": active_users,
        "premium_users": premium_users,
        "total_downloads": total_downloads,
        "free_users": total_users - premium_users
    }), 200

# SESSION PLANS ENDPOINTS - CRITICAL FOR FUNCTIONALITY
@app.route('/session-plans', methods=['GET', 'POST', 'OPTIONS'])
def session_plans():
    if request.method == 'OPTIONS':
        return '', 204
    
    if request.method == 'GET':
        return jsonify(session_plans_db), 200
    
    elif request.method == 'POST':
        data = request.get_json()
        
        # Create session plan with all the form data
        session_plan = {
            'id': len(session_plans_db) + 1,
            'sector': data.get('sector'),
            'trade': data.get('trade'),
            'rqf_level': data.get('rqf_level'),
            'date': data.get('date'),
            'trainer_name': data.get('trainer_name'),
            'term': data.get('term'),
            'module_code_title': data.get('module_code_title'),
            'week': data.get('week'),
            'number_of_trainees': data.get('number_of_trainees'),
            'class_name': data.get('class_name'),
            'topic_of_session': data.get('topic_of_session'),
            'learning_outcomes': data.get('learning_outcomes'),
            'indicative_contents': data.get('indicative_contents'),
            'session_range': data.get('session_range'),
            'facilitation_techniques': data.get('facilitation_techniques'),
            'duration': data.get('duration'),
            'created_at': datetime.now().isoformat()
        }
        
        session_plans_db.append(session_plan)
        
        return jsonify({
            "message": "Session plan created successfully",
            "id": session_plan['id']
        }), 201

@app.route('/session-plans/<int:plan_id>/download')
def download_session_plan(plan_id):
    phone = request.args.get('phone', '')
    
    # Find the session plan
    plan = None
    for p in session_plans_db:
        if p['id'] == plan_id:
            plan = p
            break
    
    if not plan:
        return jsonify({"error": "Session plan not found"}), 404
    
    # Update download count for user
    if phone and phone in users_db:
        users_db[phone]['session_plans_downloaded'] = users_db[phone].get('session_plans_downloaded', 0) + 1
    
    # Create a simple text file (in production, this would be a DOCX file)
    content = f"""RTB SESSION PLAN

Sector: {plan.get('sector', '')}
Trade: {plan.get('trade', '')}
Level: {plan.get('rqf_level', '')}
Date: {plan.get('date', '')}
Trainer: {plan.get('trainer_name', '')}
Term: {plan.get('term', '')}

Module: {plan.get('module_code_title', '')}
Week: {plan.get('week', '')}
Class: {plan.get('class_name', '')}
Number of Trainees: {plan.get('number_of_trainees', '')}

Topic: {plan.get('topic_of_session', '')}
Duration: {plan.get('duration', '')} minutes

Learning Outcomes:
{plan.get('learning_outcomes', '')}

Indicative Contents:
{plan.get('indicative_contents', '')}

Range: {plan.get('session_range', '')}
Facilitation Technique: {plan.get('facilitation_techniques', '')}

Generated on: {plan.get('created_at', '')}
"""
    
    # Create file-like object
    file_obj = io.BytesIO(content.encode('utf-8'))
    file_obj.seek(0)
    
    return send_file(
        file_obj,
        as_attachment=True,
        download_name=f'session_plan_{plan_id}.txt',
        mimetype='text/plain'
    )

# SCHEMES OF WORK ENDPOINTS - CRITICAL FOR FUNCTIONALITY
@app.route('/schemes-of-work', methods=['GET', 'POST', 'OPTIONS'])
def schemes_of_work():
    if request.method == 'OPTIONS':
        return '', 204
    
    if request.method == 'GET':
        return jsonify(schemes_db), 200
    
    elif request.method == 'POST':
        data = request.get_json()
        
        # Create scheme of work with all form data
        scheme = {
            'id': len(schemes_db) + 1,
            'province': data.get('province'),
            'district': data.get('district'),
            'sector': data.get('sector'),
            'school': data.get('school'),
            'trade': data.get('trade'),
            'qualification_title': data.get('qualification_title'),
            'rqf_level': data.get('rqf_level'),
            'module_code_title': data.get('module_code_title'),
            'school_year': data.get('school_year'),
            'terms': data.get('terms'),
            'module_hours': data.get('module_hours'),
            'number_of_classes': data.get('number_of_classes'),
            'class_name': data.get('class_name'),
            'cohort_size': data.get('cohort_size'),
            'trainer_name': data.get('trainer_name'),
            'trainer_position': data.get('trainer_position'),
            'module_rationale': data.get('module_rationale'),
            'entry_requirements': data.get('entry_requirements'),
            'competency_codes': data.get('competency_codes'),
            'indicative_scope': data.get('indicative_scope'),
            'standards_alignment': data.get('standards_alignment'),
            'cross_cutting_issues': data.get('cross_cutting_issues'),
            'key_skills': data.get('key_skills'),
            'delivery_approach': data.get('delivery_approach'),
            'term1_weeks': data.get('term1_weeks'),
            'term1_learning_outcomes': data.get('term1_learning_outcomes'),
            'term1_duration': data.get('term1_duration'),
            'term1_indicative_contents': data.get('term1_indicative_contents'),
            'term2_weeks': data.get('term2_weeks'),
            'term2_learning_outcomes': data.get('term2_learning_outcomes'),
            'term2_duration': data.get('term2_duration'),
            'term2_indicative_contents': data.get('term2_indicative_contents'),
            'term3_weeks': data.get('term3_weeks'),
            'term3_learning_outcomes': data.get('term3_learning_outcomes'),
            'term3_duration': data.get('term3_duration'),
            'term3_indicative_contents': data.get('term3_indicative_contents'),
            'formative_assessment': data.get('formative_assessment'),
            'summative_assessment': data.get('summative_assessment'),
            'resource_inventory': data.get('resource_inventory'),
            'health_safety': data.get('health_safety'),
            'dos_name': data.get('dos_name'),
            'manager_name': data.get('manager_name'),
            'created_at': datetime.now().isoformat()
        }
        
        schemes_db.append(scheme)
        
        return jsonify({
            "message": "Scheme of work created successfully",
            "id": scheme['id']
        }), 201

@app.route('/schemes-of-work/<int:scheme_id>/download')
def download_scheme(scheme_id):
    phone = request.args.get('phone', '')
    
    # Find the scheme
    scheme = None
    for s in schemes_db:
        if s['id'] == scheme_id:
            scheme = s
            break
    
    if not scheme:
        return jsonify({"error": "Scheme not found"}), 404
    
    # Update download count for user
    if phone and phone in users_db:
        users_db[phone]['schemes_downloaded'] = users_db[phone].get('schemes_downloaded', 0) + 1
    
    # Create a simple text file (in production, this would be a DOCX file)
    content = f"""RTB SCHEME OF WORK

INSTITUTIONAL INFORMATION
Province: {scheme.get('province', '')}
District: {scheme.get('district', '')}
Sector: {scheme.get('sector', '')}
School: {scheme.get('school', '')}
Trade: {scheme.get('trade', '')}
Qualification: {scheme.get('qualification_title', '')}
Level: {scheme.get('rqf_level', '')}

MODULE INFORMATION
Module: {scheme.get('module_code_title', '')}
School Year: {scheme.get('school_year', '')}
Terms: {scheme.get('terms', '')}
Module Hours: {scheme.get('module_hours', '')}
Classes: {scheme.get('number_of_classes', '')}
Class Name: {scheme.get('class_name', '')}
Cohort Size: {scheme.get('cohort_size', '')}
Trainer: {scheme.get('trainer_name', '')} ({scheme.get('trainer_position', '')})

MODULE OVERVIEW
Rationale: {scheme.get('module_rationale', '')}
Entry Requirements: {scheme.get('entry_requirements', '')}
Competency Codes: {scheme.get('competency_codes', '')}

TERM 1
Weeks: {scheme.get('term1_weeks', '')}
Duration: {scheme.get('term1_duration', '')}
Learning Outcomes: {scheme.get('term1_learning_outcomes', '')}
Content: {scheme.get('term1_indicative_contents', '')}

TERM 2
Weeks: {scheme.get('term2_weeks', '')}
Duration: {scheme.get('term2_duration', '')}
Learning Outcomes: {scheme.get('term2_learning_outcomes', '')}
Content: {scheme.get('term2_indicative_contents', '')}

TERM 3
Weeks: {scheme.get('term3_weeks', '')}
Duration: {scheme.get('term3_duration', '')}
Learning Outcomes: {scheme.get('term3_learning_outcomes', '')}
Content: {scheme.get('term3_indicative_contents', '')}

ASSESSMENT
Formative: {scheme.get('formative_assessment', '')}
Summative: {scheme.get('summative_assessment', '')}

RESOURCES & SAFETY
Resources: {scheme.get('resource_inventory', '')}
Health & Safety: {scheme.get('health_safety', '')}

SIGN-OFFS
DOS: {scheme.get('dos_name', '')}
Manager: {scheme.get('manager_name', '')}

Generated on: {scheme.get('created_at', '')}
"""
    
    # Create file-like object
    file_obj = io.BytesIO(content.encode('utf-8'))
    file_obj.seek(0)
    
    return send_file(
        file_obj,
        as_attachment=True,
        download_name=f'scheme_of_work_{scheme_id}.txt',
        mimetype='text/plain'
    )

# NOTIFICATION ENDPOINTS (Mock implementation)
@app.route('/notifications/send', methods=['POST', 'OPTIONS'])
def send_notification():
    if request.method == 'OPTIONS':
        return '', 204
    
    data = request.get_json()
    # In a real implementation, this would send actual notifications
    return jsonify({"message": "Notification sent successfully"}), 200

@app.route('/notifications/broadcast', methods=['POST', 'OPTIONS'])
def broadcast_notification():
    if request.method == 'OPTIONS':
        return '', 204
    
    data = request.get_json()
    # In a real implementation, this would broadcast to multiple users
    return jsonify({"message": "Broadcast sent successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)