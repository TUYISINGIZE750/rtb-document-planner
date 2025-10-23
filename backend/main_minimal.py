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
        "phone": "+250796014803"
    },
    "+250789751597": {
        "name": "Administrator", 
        "password": hashlib.sha256("admin123".encode()).hexdigest(),
        "phone": "+250789751597"
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
            return jsonify({
                "name": user['name'],
                "phone": user['phone'],
                "role": "user"
            })
    
    return jsonify({"detail": "Invalid credentials"}), 401

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