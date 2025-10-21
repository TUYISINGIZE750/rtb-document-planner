"""
CORS Configuration for Netlify + PythonAnywhere Integration
Add this to your main.py file on PythonAnywhere
"""

from fastapi.middleware.cors import CORSMiddleware

# Production CORS settings for Netlify frontend
CORS_ORIGINS = [
    "https://schemesession.netlify.app",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:8080"
]

def setup_cors(app):
    """Configure CORS for production deployment"""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=CORS_ORIGINS,
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
    return app