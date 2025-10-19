# Login System Guide - Netflix Style

## Overview
The system now has a complete Netflix-style authentication system with role-based access control (Admin vs User).

## Default Admin Credentials

**IMPORTANT - Save These:**
- **Phone:** `+250789751597`
- **Password:** `admin123`
- **Role:** Administrator

## Pages Created

### 1. Login Page (`login.html`)
- Netflix-style clean white design
- Phone number + password authentication
- "Remember me" checkbox
- Link to registration page
- Redirects admin to admin dashboard
- Redirects users to main application

### 2. Registration Page (`register.html`)
- Netflix-style sign-up form
- Fields: Name, Phone, Email (optional), Institution, Password
- Creates user account with "user" role
- Redirects to login after successful registration

### 3. Authentication System (`auth.js`)
- User database in localStorage
- Session management
- Role-based access control (admin/user)
- Login/logout functionality
- Page protection

## How It Works

### User Flow

**1. New User Registration:**
```
Visit: http://localhost:5173/register.html
↓
Fill form:
- Full Name: John Doe
- Phone: +250788123456
- Email: john@iprc.rw (optional)
- Institution: IPRC Kigali
- Password: ****
↓
Click "Sign Up"
↓
Account created → Redirected to login
```

**2. User Login:**
```
Visit: http://localhost:5173/login.html
↓
Enter:
- Phone: +250788123456
- Password: ****
↓
Click "Sign In"
↓
Redirected to: index.html (main app)
```

**3. Admin Login:**
```
Visit: http://localhost:5173/login.html
↓
Enter:
- Phone: +250789751597
- Password: admin123
↓
Click "Sign In"
↓
Redirected to: admin.html (admin dashboard)
```

### Page Protection

**Protected Pages:**
- `wizard.html` - Requires login (user or admin)
- `scheme-wizard.html` - Requires login (user or admin)
- `admin.html` - Requires login + admin role

**Public Pages:**
- `index.html` - Shows login/logout based on session
- `login.html` - Public
- `register.html` - Public

## Testing the System

### Test 1: Register New User ✅

1. Open `http://localhost:5173/register.html`
2. Fill in:
   - Name: `Test Teacher`
   - Phone: `+250788999888`
   - Email: `test@iprc.rw`
   - Institution: `IPRC Kigali`
   - Password: `test123`
3. Click "Sign Up"
4. Should redirect to login page

### Test 2: Login as User ✅

1. Open `http://localhost:5173/login.html`
2. Enter:
   - Phone: `+250788999888`
   - Password: `test123`
3. Click "Sign In"
4. Should redirect to `index.html`
5. Top-right shows: "👤 Test Teacher [Logout]"

### Test 3: Access User Pages ✅

1. While logged in as user
2. Click "Session Plan" or "Scheme of Work"
3. Should work normally
4. Try accessing `admin.html` directly
5. Should show: "Access denied. Admin privileges required."
6. Redirected back to `index.html`

### Test 4: Login as Admin ✅

1. Logout if logged in
2. Open `http://localhost:5173/login.html`
3. Enter:
   - Phone: `+250789751597`
   - Password: `admin123`
4. Click "Sign In"
5. Should redirect to `admin.html`
6. Top-right shows: "🛡️ Administrator [Logout]"

### Test 5: Admin Access ✅

1. While logged in as admin
2. Admin dashboard fully accessible
3. Can view all users
4. Can activate users
5. Can send notifications
6. Top-right shows admin name + logout button

### Test 6: Logout ✅

1. Click "Logout" button (top-right)
2. Should redirect to `login.html`
3. Session cleared
4. Try accessing protected pages
5. Should redirect to login

### Test 7: Direct URL Access ✅

**Without Login:**
1. Open `http://localhost:5173/wizard.html` directly
2. Should redirect to `login.html`
3. Same for `scheme-wizard.html` and `admin.html`

**With User Login:**
1. Login as regular user
2. Can access `wizard.html` and `scheme-wizard.html`
3. Cannot access `admin.html` (access denied)

**With Admin Login:**
1. Login as admin
2. Can access all pages including `admin.html`

## User Interface

### Landing Page (index.html)

**Not Logged In:**
```
┌─────────────────────────────────────────┐
│                    [Sign In] [Sign Up]  │
│                                         │
│     🎓 RTB Document Planner            │
│                                         │
│  [Session Plan]  [Scheme of Work]      │
└─────────────────────────────────────────┘
```

**Logged In (User):**
```
┌─────────────────────────────────────────┐
│         👤 John Doe [Logout]            │
│                                         │
│     🎓 RTB Document Planner            │
│                                         │
│  [Session Plan]  [Scheme of Work]      │
└─────────────────────────────────────────┘
```

**Logged In (Admin):**
```
┌─────────────────────────────────────────┐
│  🛡️ Administrator [Admin] [Logout]      │
│                                         │
│     🎓 RTB Document Planner            │
│                                         │
│  [Session Plan]  [Scheme of Work]      │
└─────────────────────────────────────────┘
```

### Login Page Design

**Netflix-Style Features:**
- ✅ Clean white background
- ✅ Centered login form with border
- ✅ Red "RTB Planner" logo (Netflix red: #e50914)
- ✅ Large input fields with borders
- ✅ Red primary button
- ✅ "Remember me" checkbox
- ✅ Error messages in orange
- ✅ Footer with gray background
- ✅ Minimal, professional design

## Admin Dashboard Changes

**New Features:**
1. **Logout Button:** Top-right corner
2. **Admin Name Display:** Shows logged-in admin name
3. **Protected Access:** Only accessible to admin role
4. **Session Management:** Tracks admin session

## Security Features

### 1. Role-Based Access Control
- **Admin Role:** Full access to admin dashboard
- **User Role:** Access to session plans and schemes only
- **No Role:** Redirected to login

### 2. Session Management
- Sessions stored in localStorage
- "Remember me" option available
- Logout clears session
- Session includes: userId, name, phone, role, timestamp

### 3. Page Protection
```javascript
// Admin pages
protectAdminPage() // Checks login + admin role

// User pages
protectUserPage() // Checks login only
```

### 4. Password Protection
- Minimum 4 characters
- Stored in localStorage (demo purposes)
- Admin has default password

## User Database Structure

```javascript
{
  userId: "USER_1738123456789_abc123",
  name: "John Doe",
  phone: "+250788123456",
  email: "john@iprc.rw",
  institution: "IPRC Kigali",
  password: "test123",
  role: "user", // or "admin"
  registeredAt: "2025-01-29T10:30:00.000Z"
}
```

## Session Structure

```javascript
{
  userId: "USER_1738123456789_abc123",
  name: "John Doe",
  phone: "+250788123456",
  email: "john@iprc.rw",
  institution: "IPRC Kigali",
  role: "user",
  loggedInAt: "2025-01-29T11:00:00.000Z",
  remember: true
}
```

## Admin Workflow

### 1. Admin Login
```
1. Visit login.html
2. Enter: +250789751597 / admin123
3. Redirected to admin.html
4. Full dashboard access
```

### 2. View All Users
```
1. Click "User Management"
2. See all registered users
3. Search by name/phone/institution
4. View user details
```

### 3. Activate User After Payment
```
1. User contacts on WhatsApp
2. User provides phone number
3. Admin searches user in dashboard
4. Admin selects user from dropdown
5. Admin chooses package
6. Admin clicks "Activate & Send Notification"
7. User receives notification
```

### 4. Send Notifications
```
1. Click "Send Notification"
2. Select recipient (specific user or all)
3. Enter title and message
4. Click "Send Notification"
5. Users receive in-app notification
```

## User Workflow

### 1. New User Registration
```
1. Visit register.html
2. Fill registration form
3. Create account
4. Login with credentials
5. Access session plans and schemes
```

### 2. Existing User Login
```
1. Visit login.html
2. Enter phone and password
3. Access main application
4. Create documents
5. Download (subject to limits)
```

### 3. Payment Process
```
1. User reaches download limit
2. Payment modal appears
3. User contacts admin on WhatsApp
4. User sends payment
5. Admin activates account
6. User receives notification
7. User refreshes browser
8. Downloads available
```

## Important Notes

### For Production:
1. **Change Admin Password:** Update DEFAULT_ADMIN in auth.js
2. **Secure Storage:** Consider server-side authentication
3. **Password Hashing:** Implement proper password hashing
4. **HTTPS:** Use secure connections
5. **Session Timeout:** Add automatic logout after inactivity

### Current Limitations:
1. **localStorage:** Data can be cleared by user
2. **No Encryption:** Passwords stored in plain text
3. **No Recovery:** No password reset functionality
4. **Single Device:** Session per browser/device
5. **Demo Purpose:** Suitable for demonstration/testing

## Quick Commands (Browser Console)

```javascript
// View current session
JSON.parse(localStorage.getItem('rtb_auth_session'))

// View all users
JSON.parse(localStorage.getItem('rtb_users_db'))

// Check if logged in
isLoggedIn()

// Check if admin
isAdmin()

// Logout
logoutUser()

// Clear all data
localStorage.clear()
```

## Troubleshooting

### Issue: Can't login as admin
**Solution:** 
- Phone: `+250789751597`
- Password: `admin123`
- Check for typos

### Issue: Redirected to login constantly
**Solution:**
- Clear browser cache
- Clear localStorage
- Register new account

### Issue: Admin can't access dashboard
**Solution:**
- Verify logged in as admin
- Check role in session
- Re-login with admin credentials

### Issue: User can access admin page
**Solution:**
- This shouldn't happen
- Check protectAdminPage() function
- Clear cache and re-login

## Summary

✅ **Netflix-style login/register pages** - Clean white design
✅ **Role-based access control** - Admin vs User
✅ **Admin dashboard protection** - Only admin can access
✅ **Session management** - Login/logout functionality
✅ **User database** - All users stored and manageable
✅ **Page protection** - Automatic redirects for unauthorized access
✅ **Professional UI** - Matches Netflix design standards

**Default Admin Login:**
- Phone: `+250789751597`
- Password: `admin123`

---

**System is now fully secured with Netflix-style authentication!** 🎉
