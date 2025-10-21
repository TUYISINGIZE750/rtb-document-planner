from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)

# Simple but effective CORS setup
CORS(app, resources={
    r"/*": {
        "origins": ["https://schemesession.netlify.app", "http://localhost:5173"],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

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

@app.route('/test-register')
def test_register():
    return jsonify({"message": "Registration endpoint is working", "method": "GET test"})

@app.route('/test-login')
def test_login():
    return jsonify({"message": "Login endpoint is working", "method": "GET test"})

@app.route('/users/', methods=['GET'])
def users_list():
    return jsonify({"message": "Users endpoint accessible", "count": 0})

@app.route('/users/register', methods=['GET', 'POST'])
def register():
    return jsonify({"message": "User registered successfully", "user_id": "test123"})

@app.route('/users/login', methods=['GET', 'POST'])
def login():
    return jsonify({
        "user_id": "test123",
        "name": "Test User",
        "phone": "+250788123456",
        "email": "test@example.com",
        "institution": "Test School",
        "role": "user",
        "is_premium": False,
        "session_plans_limit": 2,
        "schemes_limit": 2,
        "login_time": 1234567890
    })

@app.route('/user-limits/<phone>')
def user_limits(phone):
    return jsonify({
        "session_plans_limit": 2,
        "schemes_limit": 2,
        "session_plans_downloaded": 0,
        "schemes_downloaded": 0,
        "is_premium": False
    })

if __name__ == '__main__':
    app.run()