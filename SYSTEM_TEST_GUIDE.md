# System Testing Guide - RTB Document Planner

## Complete System Test Checklist

### 1. User Registration Test ✅

**Test Steps:**
1. Open `http://localhost:5173/index.html` in a **new incognito/private window**
2. Registration modal should appear automatically after 0.5 seconds
3. Fill in the form:
   - Full Name: `Test Teacher`
   - Phone: `+250788123456`
   - Email: `test@iprc.rw` (optional)
   - Institution: `IPRC Kigali`
4. Click "Continue to RTB Planner"
5. Modal should close
6. Welcome notification should appear (top-right)

**Expected Results:**
- ✅ Registration modal appears on first visit
- ✅ Form validates required fields
- ✅ User profile saved to localStorage
- ✅ Welcome notification displayed
- ✅ Notification bell appears with badge

**Check localStorage:**
```javascript
// Open browser console (F12)
JSON.parse(localStorage.getItem('rtb_user_profile'))
// Should show: {userId, name, phone, email, institution, registeredAt}
```

---

### 2. Admin Dashboard - View Users ✅

**Test Steps:**
1. Open `http://localhost:5173/admin.html`
2. Click "User Management" in sidebar
3. You should see the registered user

**Expected Results:**
- ✅ User appears in list with name, phone, institution
- ✅ Registration date displayed
- ✅ Search box works (type user name/phone)
- ✅ "Details" button shows user info

**What You'll See:**
```
👤 Test Teacher
📞 +250788123456 | 🏫 IPRC Kigali
Registered: [Today's Date]
```

---

### 3. User Activation Test ✅

**Test Steps:**
1. In admin dashboard, click "Activate User"
2. Select user from dropdown: `Test Teacher - +250788123456`
3. User info should display below dropdown
4. Select package: **500 RWF** (10 Session Plans + 5 Schemes)
5. Click "Activate & Send Notification"
6. Confirm activation

**Expected Results:**
- ✅ User dropdown populated with registered users
- ✅ User info displays when selected
- ✅ Package selection works
- ✅ Success message shows user name and phone
- ✅ Notification sent automatically

**Admin sees:**
```
User Test Teacher (+250788123456) activated successfully! Notification sent.
```

---

### 4. User Receives Notification ✅

**Test Steps:**
1. Go back to user window (where you registered)
2. Refresh the page: `F5` or `Ctrl+R`
3. Look at top-right corner

**Expected Results:**
- ✅ Notification bell has red badge with "1"
- ✅ Notification pop-up appears automatically
- ✅ Message shows: "Payment Confirmed"
- ✅ Details: "Your payment has been successfully received! 🎉"
- ✅ Shows: "✓ 10 Session Plans" and "✓ 5 Schemes of Work"

**Click notification bell:**
- ✅ Panel opens showing notification history
- ✅ Can read full message
- ✅ Timestamp displayed

---

### 5. Download Limits Test ✅

**Test Steps:**
1. In user window, click "Session Plan"
2. Fill in minimal form data (just required fields)
3. Generate and download session plan
4. Repeat 10 times

**Expected Results:**
- ✅ First 10 downloads work (activated package)
- ✅ 11th download shows payment modal
- ✅ Counter shows remaining downloads

**After each download:**
```
Free downloads remaining: 9 session plans, 5 schemes
Free downloads remaining: 8 session plans, 5 schemes
...
```

---

### 6. Send Custom Notification Test ✅

**Test Steps:**
1. In admin dashboard, click "Send Notification"
2. Select notification type: **Custom Message**
3. Send To: Select `Test Teacher` OR leave as "All Users"
4. Title: `System Update`
5. Message: `New features available! Check them out.`
6. Click "Send Notification"

**Expected Results:**
- ✅ Success message: "Notification sent to Test Teacher!"
- ✅ User receives notification immediately
- ✅ Notification bell badge updates

**User sees:**
- New notification pop-up
- Bell badge increases
- Message in notification panel

---

### 7. Multiple Users Test ✅

**Test Steps:**
1. Open **another incognito window**
2. Go to `http://localhost:5173`
3. Register as different user:
   - Name: `Second Teacher`
   - Phone: `+250789999888`
   - Institution: `IPRC Musanze`
4. Check admin dashboard

**Expected Results:**
- ✅ Admin shows "Total Users: 2"
- ✅ Both users in User Management list
- ✅ Search works for both users
- ✅ Can activate each user separately
- ✅ Can send notifications to specific user or all

---

### 8. Broadcast Notification Test ✅

**Test Steps:**
1. In admin dashboard, "Send Notification"
2. Send To: **All Users (Broadcast)**
3. Title: `Maintenance Notice`
4. Message: `System will be down for 1 hour tonight.`
5. Send notification

**Expected Results:**
- ✅ All registered users receive notification
- ✅ Each user's bell badge updates
- ✅ Notification appears in all user windows

---

## How to Identify Users for Notifications

### Method 1: User Management Panel (Recommended)
1. Open admin dashboard
2. Click "User Management"
3. See all registered users with:
   - Full name
   - Phone number
   - Institution
   - Registration date
4. Use search to find specific user
5. Click "Details" to see full info including User ID

### Method 2: When User Contacts You
When a teacher contacts you on WhatsApp:
1. Ask for their phone number
2. Search in User Management panel
3. Find their profile
4. Select them in "Activate User" dropdown
5. Activate and send notification

### Method 3: User Provides Phone Number
1. User sends payment via MTN MoMo
2. User messages: "I paid 500 RWF, my phone is +250788123456"
3. Search phone in admin panel
4. Find user profile
5. Activate their account

---

## User Identification System

### How It Works:
1. **First Visit**: User must register (name, phone, institution)
2. **Unique ID**: System generates unique User ID (e.g., `USER_1738123456789_abc123def`)
3. **localStorage**: Profile saved in browser
4. **Admin Access**: All users visible in admin dashboard
5. **Phone Number**: Primary identifier for admin

### User Profile Structure:
```javascript
{
  userId: "USER_1738123456789_abc123def",
  name: "Test Teacher",
  phone: "+250788123456",
  email: "test@iprc.rw",
  institution: "IPRC Kigali",
  registeredAt: "2025-01-29T10:30:00.000Z"
}
```

---

## Testing Checklist Summary

- [ ] Registration modal appears on first visit
- [ ] User profile saved successfully
- [ ] Welcome notification received
- [ ] User appears in admin dashboard
- [ ] Admin can search users
- [ ] Admin can select user from dropdown
- [ ] Package activation works
- [ ] Payment notification sent automatically
- [ ] User receives notification
- [ ] Notification bell shows unread count
- [ ] Download limits enforced correctly
- [ ] Custom notifications work
- [ ] Broadcast notifications work
- [ ] Multiple users can register
- [ ] Each user tracked separately

---

## Common Issues & Solutions

### Issue: Registration modal doesn't appear
**Solution:** 
- Clear browser cache and localStorage
- Use incognito/private window
- Check console for errors (F12)

### Issue: User not showing in admin dashboard
**Solution:**
- Refresh admin page
- Check localStorage: `localStorage.getItem('rtb_all_users')`
- Verify registration completed

### Issue: Notification not received
**Solution:**
- User must refresh browser after activation
- Check notification bell (top-right)
- Verify notification sent from admin

### Issue: Can't identify which user to activate
**Solution:**
- Ask user for phone number
- Search in User Management panel
- Match phone number to user profile

---

## Quick Test Commands (Browser Console)

```javascript
// View current user profile
JSON.parse(localStorage.getItem('rtb_user_profile'))

// View all registered users
JSON.parse(localStorage.getItem('rtb_all_users'))

// View subscription data
JSON.parse(localStorage.getItem('rtb_subscription'))

// View notifications
JSON.parse(localStorage.getItem('rtb_notifications'))

// Clear everything (reset)
localStorage.clear()
```

---

## Production Workflow

### When Teacher Contacts You:

**Step 1: Teacher Reaches Limit**
- Teacher sees payment modal
- Clicks WhatsApp button
- Messages: "I want to buy 500 RWF package"

**Step 2: You Request Info**
- Reply: "What's your phone number?"
- Teacher: "+250788123456"

**Step 3: You Find User**
- Open admin dashboard
- Go to User Management
- Search: "+250788123456"
- Find: "Test Teacher - IPRC Kigali"

**Step 4: Verify Payment**
- Check MTN MoMo: 250789751597
- Confirm payment received
- Note transaction ID

**Step 5: Activate User**
- Go to "Activate User"
- Select: "Test Teacher - +250788123456"
- Choose package: 500 RWF
- Click "Activate & Send Notification"

**Step 6: Confirm with Teacher**
- WhatsApp: "Payment confirmed! Please refresh your browser."
- Teacher refreshes
- Teacher sees notification
- Downloads now available

---

**System is now fully functional with user tracking and notifications!** 🎉
