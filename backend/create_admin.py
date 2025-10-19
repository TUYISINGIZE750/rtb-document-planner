from database import engine, Base
from models import User
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)
print("Database tables created successfully!")

db = Session(engine)

# Delete existing admin if exists
existing_admin = db.query(User).filter(User.phone == '+250789751597').first()
if existing_admin:
    db.delete(existing_admin)
    db.commit()
    print("Deleted existing admin user")

# Create new admin user
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
print("Admin user created successfully!")
print("")
print("=== ADMIN LOGIN CREDENTIALS ===")
print("Phone: +250789751597")
print("Password: admin123")
print("================================")

db.close()
