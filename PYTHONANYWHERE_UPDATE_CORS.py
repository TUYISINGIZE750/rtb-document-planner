# URGENT: Upload this to PythonAnywhere to fix CORS for GitHub Pages
# Replace the CORS section in your main.py file with this code

from flask_cors import CORS

# Updated CORS configuration for GitHub Pages
CORS(app, 
     origins=[
         "https://tuyisingize750.github.io",
         "https://tuyisingize750.github.io/rtb-document-planner",
         "https://schemesession.netlify.app",
         "http://localhost:5173",
         "http://localhost:8000"
     ],
     methods=["GET", "POST", "OPTIONS", "PUT"],
     allow_headers=["Content-Type", "Authorization"],
     supports_credentials=False)

@app.after_request
def after_request(response):
    origin = request.headers.get('Origin')
    allowed_origins = [
        "https://tuyisingize750.github.io",
        "https://tuyisingize750.github.io/rtb-document-planner", 
        "https://schemesession.netlify.app",
        "http://localhost:5173",
        "http://localhost:8000"
    ]
    if origin in allowed_origins:
        response.headers.add('Access-Control-Allow-Origin', origin)
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS,PUT')
    return response

# INSTRUCTIONS:
# 1. Go to PythonAnywhere Files tab
# 2. Open your main.py file
# 3. Replace the CORS section (lines ~20-40) with the code above
# 4. Save the file
# 5. Go to Web tab and reload your web app
# 6. Test registration at: https://tuyisingize750.github.io/rtb-document-planner/register.html