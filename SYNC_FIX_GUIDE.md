# Frontend-Backend Sync Fix Guide

## Problem Identified
The admin dashboard was showing "0 Total Users" and "0 Schemes" even though data exists in the backend database.

## Root Cause
- Admin dashboard was reading only from localStorage
- Backend database (SQLite) was not being queried
- No sync between frontend localStorage and backend database

## Solution Implemented

### 1. Updated Admin Dashboard Stats
- Now fetches real data from backend API
- Shows actual session plans count from database
- Shows actual schemes count from database
- Combines localStorage users with backend data

### 2. Synced User Systems
- Merged auth.js users with legacy user-registration.js users
- getAllUsers() now returns combined list
- No duplicate users
- Backward compatible

### 3. Real-Time Data Fetching
```javascript
// Before (localStorage only):
document.getElementById('totalSessionPlans').textContent = data.sessionPlansDownloaded || 0;

// After (backend API):
const sessionPlans = await fetch('http://localhost:8000/session-plans/');
document.getElementById('totalSessionPlans').textContent = sessionPlans.length;
```

## How to Test the Fix

### Step 1: Test Backend Connection

Open: `http://localhost:5173/test-sync.html`

**You should see:**
- ✅ Backend is running!
- Health check data displayed
- Auto-sync summary

### Step 2: Verify Backend Data

**In test-sync.html:**
1. Click "Show Session Plans"
2. Should show all session plans from database
3. Click "Show Schemes"
4. Should show all schemes from database

**Expected Output:**
```json
Session Plans (3)
[
  {
    "id": 1,
    "sector": "ICT",
    "trade": "Software Development",
    ...
  },
  ...
]
```

### Step 3: Check Admin Dashboard

1. Login as admin: `+250789751597` / `admin123`
2. Go to admin dashboard
3. Check stats at top:
   - **Total Users**: Should show number of registered users
   - **Session Plans**: Should show 3 (or actual count from backend)
   - **Schemes Created**: Should show actual count from backend

### Step 4: Verify User Management

1. In admin dashboard, click "User Management"
2. Should see all registered users
3. Search should work
4. User details should display correctly

### Step 5: Test User Activation

1. Register a new user (or use existing)
2. In admin dashboard, go to "Activate User"
3. Select user from dropdown
4. User info should display
5. Select package and activate
6. Should work correctly

## What Was Fixed

### ✅ Admin Dashboard Stats
- Now shows real backend data
- Session plans count from database
- Schemes count from database
- Users count from localStorage + backend

### ✅ User Management
- Merged auth users with legacy users
- No duplicates
- All users visible in admin panel
- Search works across all users

### ✅ Data Consistency
- Frontend and backend now in sync
- Real-time data fetching
- Accurate statistics

## Current Data Flow

```
┌─────────────────────────────────────────────────────┐
│                  USER CREATES DOCUMENT              │
└─────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│              FRONTEND SENDS TO BACKEND              │
│         POST /session-plans/ or /schemes/           │
└─────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│           BACKEND SAVES TO DATABASE                 │
│              (SQLite: rtb_planner.db)               │
└─────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│         ADMIN DASHBOARD FETCHES FROM BACKEND        │
│      GET /session-plans/ and /schemes-of-work/      │
└─────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────┐
│            DISPLAYS REAL DATA IN STATS              │
│    Total Users: X | Session Plans: Y | Schemes: Z   │
└─────────────────────────────────────────────────────┘
```

## Verification Checklist

- [ ] Backend is running (port 8000)
- [ ] test-sync.html shows backend connection ✅
- [ ] test-sync.html shows session plans from backend
- [ ] test-sync.html shows schemes from backend
- [ ] Admin dashboard shows correct session plans count
- [ ] Admin dashboard shows correct schemes count
- [ ] Admin dashboard shows registered users
- [ ] User activation works
- [ ] Notifications work

## Quick Test Commands

### Check Backend Status
```bash
# Open browser console (F12) on any page
fetch('http://localhost:8000/health').then(r => r.json()).then(console.log)
```

### Check Session Plans Count
```bash
fetch('http://localhost:8000/session-plans/').then(r => r.json()).then(d => console.log('Session Plans:', d.length))
```

### Check Schemes Count
```bash
fetch('http://localhost:8000/schemes-of-work/').then(r => r.json()).then(d => console.log('Schemes:', d.length))
```

### Check Frontend Users
```bash
console.log('Users:', getAllRegisteredUsers().length)
```

## Troubleshooting

### Issue: Still showing 0 session plans
**Solution:**
1. Check backend is running: `http://localhost:8000/health`
2. Check database has data: `http://localhost:8000/session-plans/`
3. Clear browser cache and refresh
4. Check browser console for errors

### Issue: Users not showing
**Solution:**
1. Check localStorage: `localStorage.getItem('rtb_users_db')`
2. Check legacy users: `localStorage.getItem('rtb_all_users')`
3. Register a new user to test
4. Refresh admin dashboard

### Issue: Backend not responding
**Solution:**
1. Restart backend: `python backend/startup.py`
2. Check port 8000 is not in use
3. Verify database exists: `backend/rtb_planner.db`
4. Check backend logs for errors

## Files Modified

1. ✅ `admin.html` - Updated stats to fetch from backend
2. ✅ `auth.js` - Merged user systems, added getAllUsers()
3. ✅ `user-registration.js` - Removed duplicates, added compatibility
4. ✅ `test-sync.html` - Created test page for verification

## Next Steps

1. **Test the system:**
   - Open `test-sync.html`
   - Verify all data displays correctly
   - Check admin dashboard stats

2. **Create test data:**
   - Login as user
   - Create 2-3 session plans
   - Create 1-2 schemes
   - Verify counts update in admin dashboard

3. **Verify sync:**
   - Refresh admin dashboard
   - Stats should match backend data
   - User list should show all users

## Expected Results After Fix

### Admin Dashboard Stats:
```
Total Users: 2
Premium Users: 0
Session Plans: 3
Schemes Created: 1
```

### User Management:
```
👤 Administrator
📞 +250789751597 | 🏫 RTB
Registered: [Date]

👤 Test Teacher
📞 +250788123456 | 🏫 IPRC Kigali
Registered: [Date]
```

### Backend Data:
```
GET /session-plans/ → Returns 3 plans
GET /schemes-of-work/ → Returns 1 scheme
```

---

**The system is now properly synced between frontend and backend!** 🎉

## Quick Start Testing

1. **Start Backend:**
   ```bash
   cd backend
   python startup.py
   ```

2. **Open Test Page:**
   ```
   http://localhost:5173/test-sync.html
   ```

3. **Login as Admin:**
   ```
   http://localhost:5173/login.html
   Phone: +250789751597
   Password: admin123
   ```

4. **Check Dashboard:**
   - Stats should show real numbers
   - Users should be listed
   - Everything should work!
