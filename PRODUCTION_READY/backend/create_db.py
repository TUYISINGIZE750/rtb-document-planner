import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Create database
conn = sqlite3.connect('rtb_planner.db')
cursor = conn.cursor()

# Create users table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        phone TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        password TEXT NOT NULL,
        is_active BOOLEAN DEFAULT 1,
        is_premium BOOLEAN DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

# Create session_plans table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS session_plans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_phone TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_phone) REFERENCES users(phone)
    )
''')

# Create schemes table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS schemes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_phone TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_phone) REFERENCES users(phone)
    )
''')

# Add test user
phone = '+250797856987'
name = 'Test User'
password = hash_password('test123')

cursor.execute('''
    INSERT OR REPLACE INTO users (phone, name, password, is_active, is_premium)
    VALUES (?, ?, ?, 1, 0)
''', (phone, name, password))

conn.commit()
conn.close()

print('Database created successfully!')
print(f'Test user: {name} ({phone})')
print('Password: test123')
