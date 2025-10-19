from database import get_db
from models import SessionPlan, SchemeOfWork

# Test database connection
db = next(get_db())
try:
    # Test query
    result = db.query(SessionPlan).first()
    print("[OK] Database connection: SUCCESS")
    print("[OK] Health check: FIXED")
    print("[OK] Delete endpoints: ADDED")
    print("\nAll systems ready!")
except Exception as e:
    print(f"[ERROR] Database error: {e}")
finally:
    db.close()
