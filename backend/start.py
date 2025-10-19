import uvicorn
from init_db import create_tables

if __name__ == "__main__":
    # Create database tables
    create_tables()
    
    # Start the FastAPI application
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)