from database import engine, Base
from models import SessionPlan, SchemeOfWork, User

print("Creating database tables...")
Base.metadata.create_all(bind=engine)
print("✅ Database tables created successfully!")

# Create default admin user
from sqlalchemy.orm import Session
db = Session(engine)

admin_exists = db.query(User).filter(User.phone == '+250789751597').first()
if not admin_exists:
    admin = User(
        user_id='ADMIN_001',
        name='Administrator',
        phone='+250789751597',
        email='admin@rtb.rw',
        institution='RTB',
        password='admin123',
        role='admin',
        is_premium=True,
        session_plans_limit=999999,
        schemes_limit=999999
    )
    db.add(admin)
    db.commit()
    print("✅ Default admin user created!")
else:
    print("ℹ️  Admin user already exists")

db.close()
print("✅ Database initialization complete!")
