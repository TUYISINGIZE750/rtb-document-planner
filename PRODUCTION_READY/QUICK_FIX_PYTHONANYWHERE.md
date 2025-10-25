# Quick Fix for PythonAnywhere

## Problem: init_db.py not found

## Solution: Create it manually

### Step 1: Open Bash Console in PythonAnywhere

### Step 2: Navigate to your project
```bash
cd ~/rtb-document-planner
```

### Step 3: Create init_db.py
```bash
cat > init_db.py << 'EOF'
from main import Base, engine, SessionLocal, User, hash_password

def init_database():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created")
    
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
            print("Admin user created")
        else:
            print("Admin user already exists")
    finally:
        db.close()
    print("Database initialized!")

if __name__ == "__main__":
    init_database()
EOF
```

### Step 4: Run it
```bash
python init_db.py
```

### Step 5: Verify
```bash
ls -la rtb_planner.db
```

You should see the database file created.

---

## Alternative: Upload via Web Interface

1. Go to PythonAnywhere **Files** tab
2. Navigate to `rtb-document-planner` folder
3. Click **Upload a file**
4. Upload `init_db.py` from your local `PRODUCTION_READY/backend/` folder
5. Then run: `python init_db.py`

---

## After Database Created

### Reload Web App:
1. Go to **Web** tab
2. Click **Reload leonardus437.pythonanywhere.com**
3. Wait for green checkmark

### Test API:
```bash
curl https://leonardus437.pythonanywhere.com/
```

Should return:
```json
{
  "message": "RTB Document Planner API",
  "status": "online"
}
```

---

## Upload New Backend Files

Upload these files to PythonAnywhere:

1. `rtb_template_filler_exact.py`
2. `facilitation_content_generator.py`
3. `content_formatter.py`
4. `document_generator.py` (updated)
5. `init_db.py`

### Via Files Tab:
- Click **Upload a file**
- Select each file
- Upload to `rtb-document-planner` folder

### Via Git (if you have repo):
```bash
cd ~/rtb-document-planner
git pull origin main
```

---

## Complete Checklist

- [ ] Create/upload init_db.py
- [ ] Run: python init_db.py
- [ ] Upload new Python files
- [ ] Reload web app
- [ ] Test API endpoint
- [ ] Try generating a document

---

## Success Indicators

✓ Database file exists (rtb_planner.db)
✓ API returns "status": "online"
✓ No errors in error log
✓ Can generate documents

Done! 🎉
