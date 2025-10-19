# RTB Document Planner - Admin Access

## ✅ VERIFIED ADMIN CREDENTIALS

**Phone Number:** `+250789751597`  
**Password:** `admin123`

## Login Instructions

1. **Start the servers** (if not already running):
   - Double-click `start_all.bat` OR
   - Run manually:
     ```bash
     # Terminal 1 - Backend
     cd backend
     python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
     
     # Terminal 2 - Frontend
     cd frontend
     python -m http.server 5173
     ```

2. **Access the login page:**
   - Open browser: http://localhost:5173/login.html

3. **Enter credentials:**
   - Phone: `+250789751597`
   - Password: `admin123`
   - Click "Login"

4. **Admin Dashboard:**
   - After login, go to: http://localhost:5173/admin.html
   - Or click "Admin Panel" in the navigation

## Admin Privileges

✅ Unlimited session plan downloads  
✅ Unlimited scheme of work downloads  
✅ User management access  
✅ Activate/deactivate users  
✅ View all users and their activity  

## Existing User Account

There's also a regular user account in the database:

**Phone:** `0796014803`  
**Password:** `12345678`  
**Name:** UWIRAGIYE Didace  
**Role:** user (limited downloads)

## Troubleshooting

### If login doesn't work:

1. **Verify backend is running:**
   ```bash
   curl http://localhost:8000/health
   ```
   Should return: `{"status":"healthy","database":"connected"}`

2. **Test login API directly:**
   ```bash
   python test_login.py
   ```
   Should show "Login successful!"

3. **Recreate admin user:**
   ```bash
   cd backend
   python create_admin.py
   ```

4. **Check browser console:**
   - Press F12 in browser
   - Look for any error messages
   - Verify API calls are going to http://localhost:8000

### Common Issues:

- **"Network error"** - Backend not running on port 8000
- **"Invalid credentials"** - Database not initialized properly
- **Page redirects immediately** - Check browser console for errors

## API Endpoints

- **Health Check:** http://localhost:8000/health
- **API Docs:** http://localhost:8000/docs
- **Login:** POST http://localhost:8000/users/login
- **All Users:** GET http://localhost:8000/users/

## Database Location

`backend/rtb_planner.db` (SQLite database)

---

**Last Verified:** Admin login tested and working ✅  
**Backend Status:** Running on port 8000 ✅  
**Database Status:** Admin user created ✅
