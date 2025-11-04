"""
Migration: Add sector_location column to schemes_of_work table
Run this once on production database
"""
import os
from sqlalchemy import create_engine, text

# Get database URL from environment
DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:///./rtb_planner.db')

# Fix for Render PostgreSQL URL
if DATABASE_URL.startswith('postgres://'):
    DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)

print(f"Connecting to: {DATABASE_URL[:30]}...")

engine = create_engine(DATABASE_URL)

try:
    with engine.connect() as conn:
        # Check if column exists
        result = conn.execute(text("""
            SELECT column_name 
            FROM information_schema.columns 
            WHERE table_name='schemes_of_work' AND column_name='sector_location'
        """))
        
        if result.fetchone():
            print("✓ Column 'sector_location' already exists")
        else:
            print("Adding column 'sector_location'...")
            conn.execute(text("""
                ALTER TABLE schemes_of_work 
                ADD COLUMN sector_location VARCHAR(255)
            """))
            conn.commit()
            print("✓ Column 'sector_location' added successfully")
            
except Exception as e:
    print(f"✗ Error: {e}")
    print("\nFor SQLite (local), column might already exist or use different syntax")
