from database import engine
from models import User
from sqlalchemy.orm import Session

db = Session(engine)

# Check all users
users = db.query(User).all()
print(f"Total users in database: {len(users)}")
print("")

for user in users:
    print(f"User ID: {user.user_id}")
    print(f"Name: {user.name}")
    print(f"Phone: {user.phone}")
    print(f"Password: {user.password}")
    print(f"Role: {user.role}")
    print(f"Is Premium: {user.is_premium}")
    print("-" * 40)

db.close()
