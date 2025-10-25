"""Initialize database with tables and admin user"""
from main import Base, engine, SessionLocal, User, hash_password

def init_database():
    """Create all tables and admin user"""
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("✓ Tables created")
    
    # Create admin user
    db = SessionLocal()
    try:
        admin = db.query(User).filter(User.phone == "+250789751597").first()
        if not admin:
            admin = User(
                user_id="ADMIN_001",
                name="Administrator",
                phone="+250789751597",
                email="admin@rtb.rw",
                institution="RTB",
                password=hash_password("admin123"),
                role="admin",
                is_premium=True,
                is_active=True,
                session_plans_limit=999,
                schemes_limit=999
            )
            db.add(admin)
            db.commit()
            print("✓ Admin user created")
            print("  Phone: +250789751597")
            print("  Password: admin123")
        else:
            print("✓ Admin user already exists")
    finally:
        db.close()
    
    print("\n✓ Database initialized successfully!")

if __name__ == "__main__":
    init_database()
