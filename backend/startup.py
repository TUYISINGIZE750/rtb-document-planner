"""
Startup script for RTB Document Planner
Initializes database and starts the application
"""
import os
import sys
from pathlib import Path

# Add the current directory to Python path
sys.path.append(str(Path(__file__).parent))

from database import engine, Base
from models import SessionPlan, SchemeOfWork
import uvicorn

def initialize_database():
    """Create database tables if they don't exist"""
    try:
        Base.metadata.create_all(bind=engine)
        print("Database tables initialized successfully!")
        return True
    except Exception as e:
        print(f"Database initialization failed: {e}")
        return False

def start_application():
    """Start the FastAPI application"""
    print("Starting RTB Document Planner API...")
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True,
        log_level="info"
    )

if __name__ == "__main__":
    print("=" * 50)
    print("RTB Document Planner - Backend Startup")
    print("=" * 50)
    
    # Initialize database
    if initialize_database():
        # Start the application
        start_application()
    else:
        print("Failed to start application due to database issues")
        sys.exit(1)