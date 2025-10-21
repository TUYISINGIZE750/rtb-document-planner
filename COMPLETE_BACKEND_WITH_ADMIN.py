from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app, 
     resources={r"/*": {"origins": "*"}},
     allow_headers=["Content-Type", "Authorization", "Accept"],
     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])

users_db = {}

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
        "version": "2.2",
        "users_count": len(users_db)
    })

@app.route('/users/', methods=['GET', 'OPTIONS'])
def get_all_users():
    """Get all users - Admin only"""
    if request.method == 'OPTIONS':
        return '', 204
    
    # Return list of all users (without passwords)
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
    """Get or update specific user"""
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
        # Update user
        if phone not in users_db:
            return jsonify({"detail": "User not found"}), 404
        
        data = request.get_json()
        user = users_db[phone]
        
        # Update allowed fields
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
        return jsonify({
            "session_plans_limit": user.get('session_plans_limit', 2),
            "schemes_limit": user.get('schemes_limit', 2),
            "session_plans_downloaded": user.get('session_plans_downloaded', 0),
            "schemes_downloaded": user.get('schemes_downloaded', 0),
            "is_premium": user.get('is_premium', False)
        })
    
    return jsonify({
        "session_plans_limit": 2,
        "schemes_limit": 2,
        "session_plans_downloaded": 0,
        "schemes_downloaded": 0,
        "is_premium": False
    })

@app.route('/stats', methods=['GET', 'OPTIONS'])
def get_stats():
    """Get system statistics for admin dashboard"""
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

if __name__ == '__main__':
    app.run()
