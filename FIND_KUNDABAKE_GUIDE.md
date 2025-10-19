# Finding KUNDABAKE Eriphase in the System

## Quick Check Steps

### Step 1: Open User Check Page
Open: `http://localhost:5173/check-users.html`

**This page will automatically:**
- Search for "KUNDABAKE" on load
- Highlight the user if found
- Show all users in the system

### Step 2: Verify in Admin Dashboard
1. Login as admin: `http://localhost:5173/login.html`
   - Phone: `+250789751597`
   - Password: `admin123`

2. Go to "User Management"
3. Search for "KUNDABAKE" in the search box
4. User should appear in the list

### Step 3: Check User Selection
1. In admin dashboard, go to "Activate User"
2. Click the "Select User" dropdown
3. Look for "KUNDABAKE Eriphase - [phone number]"
4. Select the user
5. User info should display below

## If User Not Found

### Check localStorage Directly

Open browser console (F12) and run:

```javascript
// Check Auth Database
console.log('Auth Users:', JSON.parse(localStorage.getItem('rtb_users_db') || '[]'));

// Check Legacy Database
console.log('Legacy Users:', JSON.parse(localStorage.getItem('rtb_all_users') || '[]'));

// Search for KUNDABAKE
const authUsers = JSON.parse(localStorage.getItem('rtb_users_db') || '[]');
const legacyUsers = JSON.parse(localStorage.getItem('rtb_all_users') || '[]');
const allUsers = [...authUsers, ...legacyUsers];
const kundabake = allUsers.find(u => u.name?.toLowerCase().includes('kundabake'));
console.log('KUNDABAKE found:', kundabake);
```

## Manual Registration (If Needed)

If KUNDABAKE is not in the system, register manually:

### Option 1: Via Registration Page
1. Go to: `http://localhost:5173/register.html`
2. Fill in:
   - Name: `KUNDABAKE Eriphase`
   - Phone: `[phone number]`
   - Email: `[email]` (optional)
   - Institution: `[institution name]`
   - Password: `[password]`
3. Click "Sign Up"

### Option 2: Via Browser Console
```javascript
// Add user directly to auth database
const users = JSON.parse(localStorage.getItem('rtb_users_db') || '[]');
users.push({
    userId: 'USER_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9),
    name: 'KUNDABAKE Eriphase',
    phone: '+250788123456', // Replace with actual phone
    email: 'kundabake@iprc.rw',
    institution: 'IPRC Kigali',
    password: 'teacher123',
    role: 'user',
    registeredAt: new Date().toISOString()
});
localStorage.setItem('rtb_users_db', JSON.stringify(users));
console.log('User added! Refresh the page.');
```

## Verification Checklist

- [ ] Open `check-users.html` - KUNDABAKE appears
- [ ] Admin Dashboard → User Management - KUNDABAKE in list
- [ ] Admin Dashboard → Activate User - KUNDABAKE in dropdown
- [ ] Select KUNDABAKE - User info displays correctly
- [ ] Can activate package for KUNDABAKE
- [ ] Can send notification to KUNDABAKE

## Expected Output

### In check-users.html:
```
✅ Found 1 user(s):

👤 KUNDABAKE Eriphase
📞 +250788123456
🏫 IPRC Kigali
📧 kundabake@iprc.rw
🔑 Role: user
📅 Registered: [Date]
```

### In Admin Dashboard User Management:
```
👤 KUNDABAKE Eriphase
📞 +250788123456 | 🏫 IPRC Kigali
Registered: [Date]
[Details]
```

### In Activate User Dropdown:
```
Select User: [▼]
  -- Select a user --
  Administrator - +250789751597
  KUNDABAKE Eriphase - +250788123456
  [other users...]
```

## Troubleshooting

### Issue: User not appearing in dropdown
**Solution:**
1. Refresh admin dashboard
2. Click "User Management" first to load users
3. Then go to "Activate User"
4. Dropdown should populate

### Issue: User appears but can't select
**Solution:**
1. Open browser console (F12)
2. Check for JavaScript errors
3. Run: `location.reload()` to refresh
4. Try selecting again

### Issue: User info not displaying after selection
**Solution:**
1. Check console for errors
2. Verify user has all required fields
3. Refresh page and try again

## Quick Commands

```javascript
// Count total users
const authUsers = JSON.parse(localStorage.getItem('rtb_users_db') || '[]');
const legacyUsers = JSON.parse(localStorage.getItem('rtb_all_users') || '[]');
console.log('Total users:', authUsers.length + legacyUsers.length);

// List all user names
const allUsers = [...authUsers, ...legacyUsers];
console.log('All users:', allUsers.map(u => u.name));

// Find specific user
const user = allUsers.find(u => u.name?.toLowerCase().includes('kundabake'));
console.log('Found:', user);
```

## Files Updated

1. ✅ `check-users.html` - Debug page to find users
2. ✅ `admin.html` - Fixed user loading and selection
3. ✅ Updated `loadUsers()` to combine both databases
4. ✅ Updated `populateUserSelects()` to show all users
5. ✅ Updated `activateUserAccess()` to find users correctly
6. ✅ Updated `viewUserDetails()` to search both databases

---

**The system now properly loads and displays all users including KUNDABAKE Eriphase!** 🎉

## Next Steps

1. Open `check-users.html` to verify KUNDABAKE is in system
2. Login to admin dashboard
3. Go to "Activate User"
4. Select KUNDABAKE from dropdown
5. Activate package and send notification
