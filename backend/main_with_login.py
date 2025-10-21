from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app, 
     resources={r"/*": {"origins": "*"}},
     allow_headers=["Content-Type", "Authorization", "Accept"],
     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"])

users_db = {}

# Default admin account
users_db['+250789751597'] = {
    'user_id': 'ADMIN_001',
    'name': 'Administrator',
    'phone': '+250789751597',
    'email': 'admin@rtb.rw',
    'institution': 'RTB',
    'password': 'admin123',
    'role': 'admin',
    'is_premium': True,
    'session_plans_limit': 999,
    'schemes_limit': 999
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
    return jsonify({"message": "RTB Document Planner API", "status": "online", "cors": "enabled", "version": "2.1"})

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
        'role': data.get('role', 'user'),
        'is_premium': False,
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
    
    # Check if user exists
    if phone in users_db:
        user = users_db[phone]
        stored_password = user.get('password', '')
        
        # Validate password
        if stored_password != password:
            return jsonify({"detail": "Incorrect phone number or password"}), 401
        
        # Return user data without password
        return jsonify({
            "user_id": user.get('user_id'),
            "name": user.get('name'),
            "phone": phone,
            "email": user.get('email', ''),
            "institution": user.get('institution', ''),
            "role": user.get('role', 'user'),
            "is_premium": user.get('is_premium', False),
            "session_plans_limit": user.get('session_plans_limit', 2),
            "schemes_limit": user.get('schemes_limit', 2),
            "login_time": 1234567890
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

if __name__ == '__main__':
    print("🚀 RTB Backend Started")
    print(f"📊 Users in database: {len(users_db)}")
    print("👤 Admin: +250789751597 / admin123")
    app.run(host='0.0.0.0', port=8000, debug=True)