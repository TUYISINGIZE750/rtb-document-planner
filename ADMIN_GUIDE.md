# Admin Dashboard Guide

## Overview
The Admin Dashboard is a comprehensive control center for managing the RTB Document Planner system, including user activation, notifications, and system monitoring.

## Accessing the Admin Dashboard
Open: `http://localhost:5173/admin.html`

## Dashboard Sections

### 1. Dashboard (Home)
**Quick Stats Display:**
- Total Users
- Premium Users
- Total Session Plans Generated
- Total Schemes Created

**Quick Actions:**
- Activate User
- Send Notification
- Refresh Stats

### 2. User Management
**Features:**
- View all users in the system
- See user subscription status (Free/Premium)
- Track download usage (Session Plans & Schemes)
- View individual user details

**User Information Displayed:**
- User ID
- Premium status (👑 icon for premium users)
- Session Plans: Downloaded/Limit
- Schemes: Downloaded/Limit

### 3. Activate User
**Purpose:** Activate user access after payment verification

**Process:**
1. User contacts you via WhatsApp: +250789751597
2. Verify payment received via MTN MoMo
3. Select appropriate package:
   - **500 RWF**: 10 Session Plans + 5 Schemes
   - **1,000 RWF**: 20 Session Plans + 10 Schemes
   - **2,000 RWF**: 50 Session Plans + 20 Schemes
   - **5,000 RWF**: Unlimited (30 days)
4. Click "Activate & Send Notification"
5. System automatically:
   - Activates user access
   - Sends in-app notification to user
   - Updates user limits

**User ID Field:**
- Leave empty to activate current browser user
- Enter specific user ID for remote activation

### 4. Send Notification
**Purpose:** Send in-app notifications to users

**Notification Types:**
- **Payment Confirmation**: Pre-formatted payment success message
- **Custom Message**: Create your own notification

**Fields:**
- **Notification Type**: Select template or custom
- **User ID**: Leave empty for all users, or specify user
- **Message Title**: Notification headline
- **Message Content**: Full notification text

**Example Use Cases:**
- Payment confirmations
- System maintenance alerts
- Feature announcements
- Support messages

### 5. System Settings
**Configuration Options:**
- Free Session Plans Limit (default: 2)
- Free Schemes Limit (default: 2)
- WhatsApp Contact Number

**Danger Zone:**
- Clear All User Data (use with caution!)

## In-App Notification System

### How It Works
1. Admin sends notification from dashboard
2. Notification stored in localStorage
3. User sees notification bell icon (top-right corner)
4. Unread count displayed on bell badge
5. User clicks bell to view notifications
6. Notifications auto-display as pop-ups

### Notification Features
- **Real-time Display**: Notifications appear immediately
- **Unread Counter**: Badge shows number of unread notifications
- **Auto-dismiss**: Notifications marked as read after 5 seconds
- **Notification Panel**: Click bell to view all notifications
- **Clear All**: Users can clear all notifications

### Notification Bell (User Side)
- **Location**: Top-right corner of all pages
- **Badge**: Red circle with unread count
- **Click**: Opens notification panel
- **Auto-update**: Refreshes when new notifications arrive

## Payment Activation Workflow

### Step-by-Step Process

**1. User Reaches Download Limit**
- User sees payment modal
- Modal shows 4 pricing packages
- WhatsApp contact button displayed

**2. User Contacts Admin**
- User clicks WhatsApp button
- Pre-filled message sent to +250789751597
- User requests package purchase

**3. Payment Verification**
- User sends MTN MoMo payment to 250789751597
- User shares transaction ID via WhatsApp
- Admin verifies payment received

**4. Admin Activation**
- Admin opens admin.html
- Goes to "Activate User" section
- Selects purchased package
- Clicks "Activate & Send Notification"

**5. Automatic Notification**
- System sends notification to user
- Message includes:
  - Payment confirmation
  - Number of session plans activated
  - Number of schemes activated
  - Remaining downloads
  - Instruction to refresh browser

**6. User Receives Access**
- User sees notification bell badge
- Clicks bell to read notification
- Refreshes browser
- Downloads now available

## Notification Message Template

When admin activates a user, this notification is automatically sent:

```
Title: Payment Confirmed

Message:
Your payment has been successfully received! 🎉

Refresh your browser to access:
✓ [X] Session Plans
✓ [Y] Schemes of Work

Remaining: [X] session plans, [Y] schemes

Thank you for your purchase!
```

## Admin Best Practices

### 1. Payment Verification
- Always verify payment before activation
- Keep transaction records
- Confirm user identity

### 2. Notification Management
- Send clear, concise messages
- Use payment confirmation template
- Include refresh instruction
- Specify exact numbers

### 3. User Support
- Respond promptly on WhatsApp
- Guide users through refresh process
- Verify activation successful
- Follow up if issues occur

### 4. System Monitoring
- Check dashboard stats regularly
- Monitor user activity
- Track premium conversions
- Review notification delivery

## Troubleshooting

### User Not Receiving Notification
1. Check notification was sent (admin panel)
2. Ask user to refresh browser
3. Verify localStorage not cleared
4. Check browser compatibility

### Activation Not Working
1. Verify package selected
2. Check localStorage permissions
3. Confirm browser supports localStorage
4. Try manual activation via console

### Manual Activation (Backup Method)
If admin panel fails, use browser console:

```javascript
// Open browser console (F12)
// Run activation command:
activatePremium(10, 5);  // For 500 RWF package
activatePremium(20, 10); // For 1000 RWF package
activatePremium(50, 20); // For 2000 RWF package
activatePremium('unlimited', 'unlimited'); // For 5000 RWF package

// Then send notification manually:
sendUserNotification('Payment Confirmed', 'Your payment has been received! Refresh browser to access your downloads.');
```

## Security Notes

### Current Implementation
- Uses browser localStorage
- No server-side authentication
- Manual payment verification
- WhatsApp-based communication

### Limitations
- Users can clear localStorage to bypass limits
- No persistent user accounts
- No automated payment processing
- Suitable for demonstration/small scale

### Future Enhancements
- Server-side user management
- Database-backed subscriptions
- Automated payment integration
- User authentication system

## Contact Information

**Payment & Support:**
- WhatsApp: +250789751597
- Contact: Leonard TUYISINGIZE
- MTN MoMo: 250789751597

**Developer:**
- Name: Niyonkuru Fabrice
- Institution: IPRC Kigali
- Location: Kigali, Rwanda

## Quick Reference

### Pricing Packages
| Package | Price | Session Plans | Schemes | Duration |
|---------|-------|---------------|---------|----------|
| Starter | 500 RWF | 10 | 5 | Permanent |
| Basic | 1,000 RWF | 20 | 10 | Permanent |
| Pro | 2,000 RWF | 50 | 20 | Permanent |
| Unlimited | 5,000 RWF | Unlimited | Unlimited | 30 days |

### Admin URLs
- Dashboard: `http://localhost:5173/admin.html`
- Session Plan Wizard: `http://localhost:5173/wizard.html`
- Scheme Wizard: `http://localhost:5173/scheme-wizard.html`
- Landing Page: `http://localhost:5173/index.html`

### Key Functions
- `activatePremium(sessions, schemes)` - Activate user
- `sendUserNotification(title, message)` - Send notification
- `getSubscriptionData()` - View user data
- `clearAllNotifications()` - Clear notifications
- `getRemainingDownloads()` - Check remaining downloads

---

**RTB Document Planner Admin Dashboard** - Complete system control and user management.
