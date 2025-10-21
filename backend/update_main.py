"""
Update your PythonAnywhere main.py with this CORS configuration
Copy and paste this into your main.py file on PythonAnywhere
"""

# Add this import at the top of your main.py
from fastapi.middleware.cors import CORSMiddleware

# Add this CORS configuration after creating your FastAPI app
app = FastAPI()

# CORS Configuration for Netlify Integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://schemesession.netlify.app",
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=[
        "Accept",
        "Accept-Language", 
        "Content-Language",
        "Content-Type",
        "Authorization",
        "X-Requested-With"
    ],
    expose_headers=["*"],
    max_age=3600
)