# Testing Guide - Payment & Subscription System

## 🧪 How to Test Everything Before Deployment

### Step 1: Start the Backend

1. Open Command Prompt/Terminal
2. Navigate to backend folder:
   ```bash
   cd "C:\Users\PC\Music\Scheme of work and session plan planner\backend"
   ```
3. Start the server:
   ```bash
   python startup.py
   ```
4. You should see: `Uvicorn running on http://0.0.0.0:8000`

### Step 2: Open the Application

1. Open your browser (Chrome/Edge recommended)
2. Go to: `http://localhost:5173`
3. You should see the landing page with 2 buttons

---

## ✅ Test Checklist

### Test 1: Free Downloads (Session Plans)

1. Click "Session Plan" button
2. Fill in the form with test data:
   - Sector: ICT & MULTIMEDIA
   - Trade: Software Development
   - Level: Level 4
   - Date: Today's date
   - Teacher: Test Teacher
   - Term: Term 1
   - Module: Test Module
   - Week: Week 1
   - Class Size: 25
   - Class Name: L4CSA-A
   - Topic: Test Topic
   - Learning Outcomes: Test outcomes
   - Indicative Content: Test content
   - Range: Test range
   - Facilitation: Trainer Guided
   - Duration: 40

3. Click "Generate Session Plan"
4. ✅ Document should download
5. ✅ Notification shows: "Free downloads remaining: 1 session plans, 2 schemes"

6. Repeat steps 2-4 one more time
7. ✅ Second document downloads
8. ✅ Notification shows: "Free downloads remaining: 0 session plans, 2 schemes"

9. Try to download a 3rd session plan
10. ✅ **Payment modal should appear** with all 4 packages
11. ✅ Check that it shows:
    - 500 RWF - 10 session plans + 5 schemes
    - 1,000 RWF - 20 session plans + 10 schemes
    - 2,000 RWF - 50 session plans + 20 schemes
    - 5,000 RWF - Unlimited
    - Payment number: 250789751597
    - WhatsApp button with +250789751597

### Test 2: Free Downloads (Schemes of Work)

1. Go back to home (click Back button)
2. Click "Scheme of Work" button
3. Fill in all required fields (8 steps)
4. Generate 2 schemes
5. ✅ Both should download successfully
6. Try to download a 3rd scheme
7. ✅ Payment modal should appear

### Test 3: Admin Panel Activation

1. Open new browser tab
2. Go to: `http://localhost:5173/admin.html`
3. ✅ You should see Admin Panel with 4 packages

**Test 500 RWF Package:**
1. Click on "500 RWF - Starter" package
2. ✅ Package should highlight (blue border)
3. Click "Activate Access"
4. ✅ Confirm dialog appears
5. Click OK
6. ✅ Success message appears

**Verify Activation:**
1. Go back to main app tab
2. Try to download a session plan
3. ✅ Should download successfully (no payment modal)
4. Check notification
5. ✅ Should show remaining downloads from package

**Test Other Packages:**
1. Clear browser data (see Step 4 below)
2. Use up free downloads again
3. Activate different packages (1000, 2000, 5000)
4. Verify each package gives correct limits

### Test 4: Reset/Clear Data

To test again from scratch:

**Method 1: Browser Console**
1. Press F12 (Developer Tools)
2. Go to "Console" tab
3. Type: `localStorage.clear()`
4. Press Enter
5. Refresh page (F5)
6. ✅ You're back to 2 free downloads

**Method 2: Browser Settings**
1. Chrome: Settings → Privacy → Clear browsing data
2. Check "Cookies and site data"
3. Time range: "All time"
4. Clear data
5. Refresh page

### Test 5: WhatsApp Link

1. Trigger payment modal
2. Click "Contact on WhatsApp" button
3. ✅ Should open WhatsApp Web/App
4. ✅ Should have pre-filled message
5. ✅ Should be to number: +250789751597

### Test 6: Browser Console Commands

1. Press F12
2. Go to Console tab
3. Test activation commands:

```javascript
// Check current status
getRemainingDownloads()
// Should show: {sessionPlans: X, schemes: Y, isPremium: false}

// Activate 500 RWF package
activatePremium(10, 5);

// Check status again
getRemainingDownloads()
// Should show: {sessionPlans: 10, schemes: 5, isPremium: false}

// Activate unlimited
activatePremium('unlimited', 'unlimited');

// Check status
getRemainingDownloads()
// Should show: {sessionPlans: "Unlimited", schemes: "Unlimited", isPremium: true}
```

---

## 🐛 Common Issues & Solutions

### Issue 1: Payment Modal Not Appearing
**Solution:** 
- Check browser console (F12) for errors
- Verify `subscription.js` is loaded
- Clear browser cache and reload

### Issue 2: Downloads Not Counting
**Solution:**
- Check localStorage: Press F12 → Application → Local Storage → http://localhost:5173
- Should see `rtb_subscription` key
- Clear and try again

### Issue 3: Admin Panel Not Working
**Solution:**
- Make sure you're on `http://localhost:5173/admin.html`
- Check that `subscription.js` is in same folder
- Clear browser cache

### Issue 4: WhatsApp Link Not Working
**Solution:**
- Make sure WhatsApp is installed or use WhatsApp Web
- Check that number format is correct: +250789751597

---

## 📊 Test Scenarios

### Scenario 1: New User Journey
1. ✅ User opens app
2. ✅ Downloads 2 session plans (free)
3. ✅ Downloads 2 schemes (free)
4. ✅ Tries 3rd download → Payment modal
5. ✅ Clicks WhatsApp button
6. ✅ Contacts you
7. ✅ You activate via admin panel
8. ✅ User refreshes and continues

### Scenario 2: Returning User
1. ✅ User opens app (has localStorage data)
2. ✅ Sees remaining downloads
3. ✅ Uses purchased downloads
4. ✅ When limit reached → Payment modal again

### Scenario 3: Unlimited User
1. ✅ User purchases 5000 RWF
2. ✅ You activate unlimited
3. ✅ User downloads without limits
4. ✅ No payment modal appears

---

## 🎯 Final Verification Checklist

Before deployment, verify:

- [ ] Backend starts without errors
- [ ] Frontend loads at localhost:5173
- [ ] Can create and download session plans
- [ ] Can create and download schemes
- [ ] Free limit works (2+2)
- [ ] Payment modal appears after limit
- [ ] All 4 packages display correctly
- [ ] Payment number is 250789751597
- [ ] WhatsApp number is +250789751597
- [ ] WhatsApp link works
- [ ] Admin panel loads
- [ ] Can activate all 4 packages
- [ ] Activation increases limits correctly
- [ ] Unlimited package works
- [ ] Can reset via localStorage.clear()
- [ ] Footer shows correct contact info

---

## 🚀 Ready for Deployment?

If all tests pass:
1. ✅ System is working correctly
2. ✅ Payment flow is functional
3. ✅ Admin activation works
4. ✅ Ready to deploy!

---

## 📝 Quick Test Script

Run this in browser console to quickly test:

```javascript
// Quick test script
console.log("=== RTB Planner Test ===");

// 1. Check initial state
console.log("1. Initial state:", getRemainingDownloads());

// 2. Simulate downloads
recordSessionPlanDownload();
recordSessionPlanDownload();
console.log("2. After 2 session plans:", getRemainingDownloads());

// 3. Activate 500 RWF
activatePremium(10, 5);
console.log("3. After 500 RWF activation:", getRemainingDownloads());

// 4. Activate unlimited
activatePremium('unlimited', 'unlimited');
console.log("4. After unlimited activation:", getRemainingDownloads());

// 5. Reset
localStorage.clear();
console.log("5. After reset:", getRemainingDownloads());

console.log("=== Test Complete ===");
```

---

## 💡 Tips

1. **Test in Incognito Mode**: To test fresh user experience
2. **Test on Mobile**: Open on your phone to test mobile view
3. **Test Different Browsers**: Chrome, Firefox, Edge
4. **Keep Admin Panel Open**: In separate tab for quick activation
5. **Document Issues**: Note any bugs you find

Good luck with testing! 🎉
