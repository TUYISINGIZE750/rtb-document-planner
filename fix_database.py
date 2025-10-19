#!/usr/bin/env python3
"""
Database Fix Script - Ensures proper database initialization with User table and admin user
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from backend.database import engine, Base
from backend.models import SessionPlan, SchemeOfWork, User
from sqlalchemy.orm import sessionmaker

def fix_database():
    print("Fixing database initialization...")
    
    try:
        # Create all tables
        Base.metadata.create_all(bind=engine)
        print("Database tables created successfully!")
        
        # Create session
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        db = SessionLocal()
        
        try:
            # Check if admin user exists
            existing_admin = db.query(User).filter(User.phone == '+250789751597').first()
            
            if not existing_admin:
                # Create default admin user
                admin_user = User(
                    user_id='ADMIN_DEFAULT',
                    name='Administrator',
                    phone='+250789751597',
                    email='admin@rtb.rw',
                    institution='RTB',
                    password='admin123',
                    role='admin',
                    is_premium=True,
                    session_plans_limit=999,
                    schemes_limit=999
                )
                db.add(admin_user)
                db.commit()
                print("Default admin user created successfully!")
                print("   Phone: +250789751597")
                print("   Password: admin123")
            else:
                print("Admin user already exists")
                
            # Create a test regular user
            existing_test_user = db.query(User).filter(User.phone == '+250123456789').first()
            if not existing_test_user:
                test_user = User(
                    user_id='USER_TEST_001',
                    name='Test Teacher',
                    phone='+250123456789',
                    email='teacher@test.com',
                    institution='Test School',
                    password='test123',
                    role='user',
                    is_premium=False,
                    session_plans_limit=2,
                    schemes_limit=2
                )
                db.add(test_user)
                db.commit()
                print("Test user created successfully!")
                print("   Phone: +250123456789")
                print("   Password: test123")
            else:
                print("Test user already exists")
                
            # Verify users count
            total_users = db.query(User).count()
            admin_users = db.query(User).filter(User.role == 'admin').count()
            regular_users = db.query(User).filter(User.role == 'user').count()
            
            print(f"\nDatabase Status:")
            print(f"   Total Users: {total_users}")
            print(f"   Admin Users: {admin_users}")
            print(f"   Regular Users: {regular_users}")
            
        except Exception as e:
            print(f"Error creating users: {e}")
            db.rollback()
        finally:
            db.close()
            
    except Exception as e:
        print(f"Database error: {e}")
        return False
        
    print("\nDatabase fix completed successfully!")
    return True

if __name__ == "__main__":
    success = fix_database()
    if success:
        print("\nYou can now start the backend server:")
        print("   cd backend && python startup.py")
    else:
        print("\nDatabase fix failed. Please check the errors above.")
        sys.exit(1)