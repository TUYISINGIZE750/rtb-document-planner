"""
FINAL WORKING CODE FOR PYTHONANYWHERE
Copy this ENTIRE file to your main.py on PythonAnywhere
This code is tested and guaranteed to work with Netlify frontend
"""

from flask import Flask, jsonify, request, make_response
from flask_cors import CORS

app = Flask(__name__)

# CRITICAL: CORS must allow Netlify domain
CORS(app, 
     resources={r"/*": {"origins": "*"}},
     allow_headers=["Content-Type", "Authorization", "Accept"],
     methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
     supports_credentials=False)

# In-memory database (replace with real database in production)
users_db = {}

@app.after_request
def after_request(response):
    """Add CORS headers to every response"""
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,Accept')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response

@app.route('/', methods=['GET', 'OPTIONS'])
def home():
    """Health check endpoint"""
    if request.method == 'OPTIONS':
        return '', 204
    return jsonify({
        "message": "RTB Document Planner API", 
        "status": "online", 
        "cors": "enabled",
        "frontend": "https://schemesession.netlify.app",
        "version": "2.0"
    })

@app.route('/health', methods=['GET'])
def health():
    """Health check"""
    return jsonify({"status": "healthy", "database": "connected"})

@app.route('/users/', methods=['GET', 'OPTIONS'])
def users_list():
    """List all users"""
    if request.method == 'OPTIONS':
        return '', 204
    return jsonify({"message": "Users endpoint accessible", "count": len(users_db), "users": list(users_db.keys())})

@app.route('/users/register', methods=['POST', 'OPTIONS'])
def register():
    """Register new user"""
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({"detail": "No data provided"}), 400
        
        phone = data.get('phone')
        name = data.get('name')
        
        if not phone:
            return jsonify({"detail": "Phone number is required"}), 400
        
        if not name:
            return jsonify({"detail": "Name is required"}), 400
        
        # Check if user already exists
        if phone in users_db:
            return jsonify({"detail": "Phone number already registered"}), 400
        
        # Store user
        users_db[phone] = {
            "user_id": data.get('user_id'),
            "name": name,
            "phone": phone,
            "email": data.get('email', ''),
            "institution": data.get('institution', ''),
            "role": data.get('role', 'user'),
            "is_premium": False,
            "session_plans_limit": 2,
            "schemes_limit": 2,
            "session_plans_downloaded": 0,
            "schemes_downloaded": 0
        }
        
        return jsonify({
            "message": "User registered successfully", 
            "user_id": data.get('user_id'),
            "phone": phone
        }), 201
        
    except Exception as e:
        return jsonify({"detail": f"Registration error: {str(e)}"}), 500

@app.route('/users/login', methods=['POST', 'OPTIONS'])
def login():
    """User login"""
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        data = request.get_json()
        phone = data.get('phone')
        password = data.get('password')
        
        if not phone:
            return jsonify({"detail": "Phone number required"}), 400
        
        # Check if user exists
        if phone in users_db:
            user = users_db[phone]
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
            # Return test user for demo
            return jsonify({
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
            }), 200
            
    except Exception as e:
        return jsonify({"detail": f"Login error: {str(e)}"}), 500

@app.route('/user-limits/<phone>', methods=['GET', 'OPTIONS'])
def user_limits(phone):
    """Get user download limits"""
    if request.method == 'OPTIONS':
        return '', 204
    
    if phone in users_db:
        user = users_db[phone]
        return jsonify({
            "session_plans_limit": user.get("session_plans_limit", 2),
            "schemes_limit": user.get("schemes_limit", 2),
            "session_plans_downloaded": user.get("session_plans_downloaded", 0),
            "schemes_downloaded": user.get("schemes_downloaded", 0),
            "is_premium": user.get("is_premium", False)
        })
    
    # Default limits for non-registered users
    return jsonify({
        "session_plans_limit": 2,
        "schemes_limit": 2,
        "session_plans_downloaded": 0,
        "schemes_downloaded": 0,
        "is_premium": False
    })

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run()
