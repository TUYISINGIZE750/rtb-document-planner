#!/usr/bin/env python3
import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Connect to database
conn = sqlite3.connect('rtb_planner.db')
cursor = conn.cursor()

# Check if user exists
cursor.execute("SELECT * FROM users WHERE phone = ?", ("+250796014803",))
user = cursor.fetchone()

if user:
    print("✅ User found:")
    print(f"ID: {user[0]}")
    print(f"User ID: {user[1]}")
    print(f"Name: {user[2]}")
    print(f"Phone: {user[3]}")
    print(f"Email: {user[4]}")
    print(f"Institution: {user[5]}")
    print(f"Role: {user[7]}")
    print(f"Is Premium: {user[8]}")
    print(f"Is Active: {user[9]}")
else:
    print("❌ User not found. Creating user...")
    
    # Create the user
    cursor.execute("""
        INSERT INTO users (user_id, name, phone, email, institution, password, role, is_premium, is_active, session_plans_limit, schemes_limit)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "USER_0785269312",
        "Test Teacher",
        "+250796014803", 
        "teacher@test.com",
        "Test School",
        hash_password("teacher123"),
        "user",
        False,
        True,
        5,
        5
    ))
    
    conn.commit()
    print("✅ User created successfully!")

# Check admin user
cursor.execute("SELECT * FROM users WHERE phone = ?", ("+250789751597",))
admin = cursor.fetchone()

if admin:
    print("\n✅ Admin found:")
    print(f"Name: {admin[2]}")
    print(f"Phone: {admin[3]}")
    print(f"Role: {admin[7]}")
else:
    print("\n❌ Admin not found. Creating admin...")
    cursor.execute("""
        INSERT INTO users (user_id, name, phone, email, institution, password, role, is_premium, is_active, session_plans_limit, schemes_limit)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        "ADMIN_001",
        "Administrator",
        "+250789751597",
        "admin@rtb.rw", 
        "RTB",
        hash_password("admin123"),
        "admin",
        True,
        True,
        999,
        999
    ))
    
    conn.commit()
    print("✅ Admin created successfully!")

conn.close()
print("\n🎯 Database setup complete!")