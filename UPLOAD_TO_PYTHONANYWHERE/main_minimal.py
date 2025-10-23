from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import hashlib
import tempfile
import os
from rtb_professional_generator import generate_rtb_session_plan, generate_rtb_scheme_of_work

app = Flask(__name__)
CORS(app, origins=["https://tuyisingize750.github.io"])

# Simple in-memory storage for demo
users = {
    "+250796014803": {
        "name": "Test Teacher",
        "password": hashlib.sha256("teacher123".encode()).hexdigest(),
        "phone": "+250796014803",
        "role": "user",
        "is_active": True,
        "is_premium": False,
        "institution": "Test School",
        "session_plans_downloaded": 0,
        "session_plans_limit": 2,
        "schemes_downloaded": 0,
        "schemes_limit": 2
    },
    "+250789751597": {
        "name": "Administrator", 
        "password": hashlib.sha256("admin123".encode()).hexdigest(),
        "phone": "+250789751597",
        "role": "admin",
        "is_active": True,
        "is_premium": True,
        "institution": "RTB Admin",
        "session_plans_downloaded": 0,
        "session_plans_limit": 999,
        "schemes_downloaded": 0,
        "schemes_limit": 999
    }
}

documents = {}
doc_counter = 1

@app.route('/', methods=['GET', 'OPTIONS'])
def home():
    if request.method == 'OPTIONS':
        return '', 204
    return jsonify({"message": "RTB API", "status": "online", "version": "minimal"})

@app.route('/users/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        return '', 204
    
    data = request.get_json()
    phone = data.get('phone')
    password = data.get('password')
    
    if phone in users:
        user = users[phone]
        if hashlib.sha256(password.encode()).hexdigest() == user['password']:
            if not user.get('is_active', True):
                return jsonify({"detail": "Account deactivated"}), 403
            return jsonify({
                "name": user['name'],
                "phone": user['phone'],
                "role": user.get('role', 'user')
            })
    
    return jsonify({"detail": "Invalid credentials"}), 401

@app.route('/users/', methods=['GET', 'OPTIONS'])
def get_users():
    if request.method == 'OPTIONS':
        return '', 204
    user_list = []
    for phone, user in users.items():
        user_list.append({
            "name": user['name'],
            "phone": user['phone'],
            "role": user.get('role', 'user'),
            "is_active": user.get('is_active', True),
            "is_premium": user.get('is_premium', False),
            "institution": user.get('institution', 'N/A'),
            "session_plans_downloaded": user.get('session_plans_downloaded', 0),
            "session_plans_limit": user.get('session_plans_limit', 2),
            "schemes_downloaded": user.get('schemes_downloaded', 0),
            "schemes_limit": user.get('schemes_limit', 2)
        })
    return jsonify(user_list)

@app.route('/users/<phone>', methods=['PUT', 'OPTIONS'])
def update_user(phone):
    if request.method == 'OPTIONS':
        return '', 204
    if phone not in users:
        return jsonify({"detail": "User not found"}), 404
    data = request.get_json()
    if 'is_active' in data:
        users[phone]['is_active'] = data['is_active']
    if 'is_premium' in data:
        users[phone]['is_premium'] = data['is_premium']
    if 'session_plans_limit' in data:
        users[phone]['session_plans_limit'] = data['session_plans_limit']
    if 'schemes_limit' in data:
        users[phone]['schemes_limit'] = data['schemes_limit']
    return jsonify({"message": "User updated"})

@app.route('/stats', methods=['GET', 'OPTIONS'])
def get_stats():
    if request.method == 'OPTIONS':
        return '', 204
    total = len(users)
    active = sum(1 for u in users.values() if u.get('is_active', True))
    premium = sum(1 for u in users.values() if u.get('is_premium', False))
    downloads = sum(u.get('session_plans_downloaded', 0) + u.get('schemes_downloaded', 0) for u in users.values())
    return jsonify({
        "total_users": total,
        "active_users": active,
        "premium_users": premium,
        "total_downloads": downloads
    })

@app.route('/session-plans', methods=['POST', 'OPTIONS'])
def create_session_plan():
    if request.method == 'OPTIONS':
        return '', 204
    
    global doc_counter
    doc_id = doc_counter
    doc_counter += 1
    
    data = request.get_json()
    documents[doc_id] = {
        'type': 'session_plan',
        'data': data
    }
    
    return jsonify({"id": doc_id, "message": "Session plan created"})

@app.route('/schemes', methods=['POST', 'OPTIONS'])
def create_scheme():
    if request.method == 'OPTIONS':
        return '', 204
    
    global doc_counter
    doc_id = doc_counter
    doc_counter += 1
    
    data = request.get_json()
    documents[doc_id] = {
        'type': 'scheme',
        'data': data
    }
    
    return jsonify({"id": doc_id, "message": "Scheme created"})

@app.route('/session-plans/<int:plan_id>/download', methods=['GET'])
def download_session_plan(plan_id):
    if plan_id not in documents:
        return jsonify({"detail": "Not found"}), 404
    
    data = documents[plan_id]['data']
    
    # Generate professional RTB session plan
    doc = generate_rtb_session_plan(data)
    
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
    doc.save(temp_file.name)
    
    return send_file(temp_file.name, as_attachment=True, download_name=f"RTB_Session_Plan_{plan_id}.docx")

@app.route('/schemes/<int:scheme_id>/download', methods=['GET'])
def download_scheme(scheme_id):
    if scheme_id not in documents:
        return jsonify({"detail": "Not found"}), 404
    
    data = documents[scheme_id]['data']
    
    # Generate professional RTB scheme of work
    doc = generate_rtb_scheme_of_work(data)
    
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.docx')
    doc.save(temp_file.name)
    
    return send_file(temp_file.name, as_attachment=True, download_name=f"RTB_Scheme_of_Work_{scheme_id}.docx")

if __name__ == '__main__':
    app.run(debug=False)