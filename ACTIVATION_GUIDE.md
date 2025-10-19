# User Activation Guide

## 📱 How It Works

### For Users:
1. User downloads 2 free session plans + 2 free schemes
2. When limit reached, payment modal appears
3. User contacts you on WhatsApp: **+250789751597**
4. User sends payment via MTN MoMo to: **250789751597**
5. User shares transaction ID with you
6. You activate their account
7. User refreshes browser and continues downloading

---

## 💰 Pricing Packages

| Package | Price | Session Plans | Schemes of Work |
|---------|-------|---------------|-----------------|
| Starter | 500 RWF | 10 | 5 |
| Basic | 1,000 RWF | 20 | 10 |
| Pro | 2,000 RWF | 50 | 20 |
| Unlimited | 5,000 RWF | Unlimited | Unlimited (30 days) |

---

## 🔧 How to Activate Users

### Method 1: Using Admin Panel (Easiest)

1. Open: `admin.html` in your browser
2. User contacts you on WhatsApp
3. Verify payment received
4. Select the package they paid for
5. Click "Activate Access"
6. Tell user to refresh their browser

### Method 2: Using Browser Console

1. User contacts you on WhatsApp
2. Verify payment received
3. Open the app in YOUR browser
4. Press F12 to open Developer Console
5. Type one of these commands:

**For 500 RWF (10 session plans + 5 schemes):**
```javascript
activatePremium(10, 5);
```

**For 1,000 RWF (20 session plans + 10 schemes):**
```javascript
activatePremium(20, 10);
```

**For 2,000 RWF (50 session plans + 20 schemes):**
```javascript
activatePremium(50, 20);
```

**For 5,000 RWF (Unlimited):**
```javascript
activatePremium('unlimited', 'unlimited');
```

6. Tell user to refresh their browser

---

## 📝 Sample WhatsApp Conversation

**User:** "Hello, I want to purchase RTB Document Planner access"

**You:** "Hello! Here are our packages:
- 500 RWF: 10 session plans + 5 schemes
- 1,000 RWF: 20 session plans + 10 schemes
- 2,000 RWF: 50 session plans + 20 schemes
- 5,000 RWF: Unlimited access (30 days)

Which package would you like?"

**User:** "I want the 1,000 RWF package"

**You:** "Great! Please send 1,000 RWF via MTN MoMo to 250789751597 and share the transaction ID with me."

**User:** "Done! Transaction ID: MP123456789"

**You:** "Payment confirmed! Your account is now activated. Please refresh your browser and you'll have 20 session plans and 10 schemes available. Thank you!"

---

## ⚠️ Important Notes

1. **Activation is per browser**: If user clears browser data or uses different browser, they lose access
2. **Keep records**: Note down who paid what and when
3. **Transaction IDs**: Always verify transaction ID before activating
4. **Unlimited package**: Lasts 30 days from activation

---

## 🔄 If User Loses Access

If user clears browser data or switches devices:

1. Verify they previously paid (check your records)
2. Use admin panel or console to reactivate
3. Consider keeping a spreadsheet of:
   - User phone number
   - Package purchased
   - Transaction ID
   - Activation date

---

## 📊 Tracking Payments

Create a simple spreadsheet with:

| Date | Phone | Package | Amount | Transaction ID | Status |
|------|-------|---------|--------|----------------|--------|
| 2025-01-17 | 078... | Basic | 1,000 | MP123... | Activated |

---

## 🚀 Future Improvements

When you have many users, consider:
1. Building a proper backend with user accounts
2. Automatic payment verification via MTN API
3. User login system
4. Payment history tracking
5. Automatic renewal reminders

---

## 📞 Support

Your WhatsApp: **+250789751597**
MTN MoMo: **250789751597**

Keep this guide handy for quick reference when users contact you!
