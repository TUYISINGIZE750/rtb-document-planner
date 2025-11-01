import sqlite3
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Connect to database
conn = sqlite3.connect('rtb_planner.db')
cursor = conn.cursor()

# Add test user
phone = '+250797856987'
name = 'Test User'
password = hash_password('test123')

try:
    cursor.execute('''
        INSERT OR REPLACE INTO users (phone, name, password, is_active, is_premium)
        VALUES (?, ?, ?, 1, 0)
    ''', (phone, name, password))
    
    conn.commit()
    print(f'✅ User added: {name} ({phone})')
    print('Password: test123')
    
except Exception as e:
    print(f'❌ Error: {e}')
finally:
    conn.close()
