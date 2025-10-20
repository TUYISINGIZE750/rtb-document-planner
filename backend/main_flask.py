from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app, origins="*", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"], 
     allow_headers=["Content-Type", "Authorization", "Accept", "Origin", "X-Requested-With"])

# Simple in-memory storage (replace with database in production)
users_db = {}
session_plans_db = {}
schemes_db = {}

@app.route('/', methods=['GET', 'OPTIONS'])
def root():
    return jsonify({"message": "RTB Document Planner API", "status": "online", "cors": "enabled"})

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "database": "connected"})

@app.route('/users/register', methods=['POST', 'OPTIONS'])
def register_user():
    if request.method == 'OPTIONS':
        return '', 200
    
    try:
        data = request.get_json()
        phone = data.get('phone')
        
        if phone in users_db:
            return jsonify({"detail": "Phone number already registered"}), 400
        
        user = {
            "user_id": data.get('user_id'),
            "name": data.get('name'),
            "phone": phone,
            "email": data.get('email'),
            "institution": data.get('institution'),
            "password": data.get('password'),
            "role": data.get('role', 'user'),
            "is_premium": False,
            "is_active": True,
            "session_plans_downloaded": 0,
            "schemes_downloaded": 0,
            "created_at": datetime.now().isoformat()
        }
        
        users_db[phone] = user
        
        return jsonify({
            "user_id": user["user_id"],
            "name": user["name"],
            "phone": user["phone"],
            "email": user["email"],
            "institution": user["institution"],
            "role": user["role"],
            "is_premium": user["is_premium"],
            "is_active": user["is_active"]
        })
    except Exception as e:
        return jsonify({"detail": f"Registration failed: {str(e)}"}), 500

@app.route('/users/login', methods=['POST', 'OPTIONS'])
def login_user():
    if request.method == 'OPTIONS':
        return '', 200
    
    try:
        data = request.get_json()
        phone = data.get('phone')
        password = data.get('password')
        
        user = users_db.get(phone)
        
        if not user or user['password'] != password:
            return jsonify({"detail": "Incorrect phone number or password"}), 401
        
        if not user['is_active']:
            return jsonify({"detail": "Account is deactivated"}), 401
        
        return jsonify({
            "user_id": user["user_id"],
            "name": user["name"],
            "phone": user["phone"],
            "email": user["email"],
            "institution": user["institution"],
            "role": user["role"],
            "is_premium": user["is_premium"],
            "is_active": user["is_active"],
            "session_plans_downloaded": user.get("session_plans_downloaded", 0),
            "schemes_downloaded": user.get("schemes_downloaded", 0)
        })
    except Exception as e:
        return jsonify({"detail": f"Login failed: {str(e)}"}), 500

@app.route('/users/<user_id>/limits', methods=['GET'])
def get_user_limits(user_id):
    try:
        user = None
        for u in users_db.values():
            if u['user_id'] == user_id:
                user = u
                break
        
        if not user:
            return jsonify({"detail": "User not found"}), 404
        
        session_plan_limit = 999 if user['is_premium'] else 5
        scheme_limit = 999 if user['is_premium'] else 3
        
        return jsonify({
            "session_plans_downloaded": user.get("session_plans_downloaded", 0),
            "schemes_downloaded": user.get("schemes_downloaded", 0),
            "session_plan_limit": session_plan_limit,
            "scheme_limit": scheme_limit,
            "is_premium": user["is_premium"],
            "can_download_session_plan": user.get("session_plans_downloaded", 0) < session_plan_limit,
            "can_download_scheme": user.get("schemes_downloaded", 0) < scheme_limit
        })
    except Exception as e:
        return jsonify({"detail": f"Failed to fetch limits: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)