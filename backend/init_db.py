from database import engine, Base
from models import SessionPlan, SchemeOfWork, User, Notification, Settings

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")
    
    # Create default admin user if not exists
    from sqlalchemy.orm import sessionmaker
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    
    try:
        existing_admin = db.query(User).filter(User.phone == '+250789751597').first()
        if not existing_admin:
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
        else:
            print("Admin user already exists.")
            
        # Create default settings
        default_settings = [
            ('free_session_plans', '2', 'Number of free session plans for new users'),
            ('free_schemes', '2', 'Number of free schemes for new users'),
            ('per_session_price', '36', 'Price per single session plan (RWF)'),
            ('per_scheme_price', '47', 'Price per single scheme of work (RWF)'),
            ('weekly_sessions_price', '474', 'Price for 15 session plans weekly (RWF)'),
            ('weekly_schemes_price', '526', 'Price for 10 schemes weekly (RWF)'),
            ('monthly_sessions_price', '1000', 'Price for 50 session plans monthly (RWF)'),
            ('monthly_schemes_price', '1889', 'Price for 20 schemes monthly (RWF)'),
            ('unlimited_price', '5200', 'Price for unlimited school year access (RWF)')
        ]
        
        for key, value, description in default_settings:
            existing = db.query(Settings).filter(Settings.key == key).first()
            if not existing:
                setting = Settings(key=key, value=value, description=description)
                db.add(setting)
        
        db.commit()
        print("Default settings created successfully!")
        
    except Exception as e:
        print(f"Error creating defaults: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_tables()