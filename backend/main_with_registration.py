from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={
    r"/*": {
        "origins": ["https://schemesession.netlify.app", "http://localhost:5173"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# In-memory user storage (replace with database in production)
users_db = {}

@app.route('/')
def home():
    return jsonify({
        "message": "RTB Document Planner API", 
        "status": "online", 
        "cors": "enabled",
        "frontend": "https://schemesession.netlify.app"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "database": "connected"})

@app.route('/users/', methods=['GET'])
def users_list():
    return jsonify({"message": "Users endpoint accessible", "count": len(users_db)})

@app.route('/users/register', methods=['POST', 'OPTIONS'])
def register():
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        data = request.get_json()
        phone = data.get('phone')
        
        if not phone:
            return jsonify({"detail": "Phone number is required"}), 400
        
        if phone in users_db:
            return jsonify({"detail": "Phone number already registered"}), 400
        
        users_db[phone] = {
            "user_id": data.get('user_id'),
            "name": data.get('name'),
            "phone": phone,
            "email": data.get('email', ''),
            "institution": data.get('institution'),
            "role": data.get('role', 'user'),
            "is_premium": False,
            "session_plans_limit": 2,
            "schemes_limit": 2,
            "session_plans_downloaded": 0,
            "schemes_downloaded": 0
        }
        
        return jsonify({"message": "User registered successfully", "user_id": data.get('user_id')}), 201
    except Exception as e:
        return jsonify({"detail": str(e)}), 500

@app.route('/users/login', methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        data = request.get_json()
        phone = data.get('phone')
        
        if phone in users_db:
            user = users_db[phone]
        else:
            user = {
                "user_id": "test123",
                "name": "Test User",
                "phone": phone,
                "email": "test@example.com",
                "institution": "Test School",
                "role": "user",
                "is_premium": False,
                "session_plans_limit": 2,
                "schemes_limit": 2,
                "login_time": 1234567890
            }
        
        return jsonify(user), 200
    except Exception as e:
        return jsonify({"detail": str(e)}), 500

@app.route('/user-limits/<phone>')
def user_limits(phone):
    if phone in users_db:
        user = users_db[phone]
        return jsonify({
            "session_plans_limit": user.get("session_plans_limit", 2),
            "schemes_limit": user.get("schemes_limit", 2),
            "session_plans_downloaded": user.get("session_plans_downloaded", 0),
            "schemes_downloaded": user.get("schemes_downloaded", 0),
            "is_premium": user.get("is_premium", False)
        })
    
    return jsonify({
        "session_plans_limit": 2,
        "schemes_limit": 2,
        "session_plans_downloaded": 0,
        "schemes_downloaded": 0,
        "is_premium": False
    })

if __name__ == '__main__':
    app.run()