# RTB Document Planner - Notification System Guide

## Overview
The RTB Document Planner now includes a comprehensive notification system that allows administrators to send notifications to teachers and automatically notifies users about important events.

## Features

### 🔔 Real-time Notifications
- **In-app notifications** with notification bell
- **Automatic notifications** for system events
- **Admin-controlled notifications** for announcements
- **Notification templates** for common scenarios

### 📱 Notification Types
- **Success**: Payment confirmations, activations
- **Info**: General announcements, updates
- **Warning**: Reminders, low subscription alerts
- **Error**: System issues, failed operations

## For Administrators

### Accessing Admin Panel
1. Open http://localhost:5173
2. Click "Injira nka Mwarimu" 
3. Use admin credentials:
   - Phone: `+250789751597`
   - Password: `admin123`

### Sending Notifications

#### 1. Individual User Notifications
1. Go to **Admin Dashboard** → **Send Notification**
2. Select **Send To**: Choose specific user
3. Choose **Notification Template**:
   - Payment Confirmation
   - Welcome Message
   - Session Plan Ready
   - Scheme of Work Ready
   - Subscription Update
   - Payment Reminder
   - System Announcement
   - Custom Message
4. Customize title and message
5. Click **Send Notification**

#### 2. Bulk Notifications (All Users)
1. Go to **Admin Dashboard** → **Send Notification**
2. Leave **Send To** as "All Users (Broadcast)"
3. Choose template or write custom message
4. Click **Send Notification**

### Notification Templates

#### Payment Confirmation
```
Title: Payment Received - Access Activated! 🎉
Message: Your payment has been successfully received!

You now have access to:
✓ Additional Session Plans
✓ Additional Schemes of Work

Thank you for your purchase! Start creating your documents now.
```

#### Welcome Message
```
Title: Welcome to RTB Document Planner! 🎓
Message: Welcome to the RTB Document Planner system!

You can now:
✓ Create professional session plans
✓ Generate schemes of work
✓ Download RTB-compliant documents

Get started by visiting the main dashboard.
```

#### Session Plan Ready
```
Title: New Session Plan Available 📋
Message: A new session plan has been created and is ready for download.

You can now:
✓ Download the document
✓ Use it for your classes
✓ Print or share as needed

Check your dashboard to access it.
```

## For Teachers/Users

### Viewing Notifications

#### Notification Bell
- Located in **top-right corner** of user pages
- Shows **red badge** with unread count
- Click to open notification panel

#### Notification Panel
- Shows **all notifications** (read and unread)
- **Unread notifications** highlighted in blue
- **Read notifications** shown in gray
- Click **Clear All** to remove all notifications

#### Auto-popup Notifications
- **New notifications** appear automatically
- Show for **5 seconds** then auto-dismiss
- Click **×** to dismiss manually

### Automatic Notifications

Users receive automatic notifications for:

#### 1. Subscription Updates
- When admin activates additional session plans/schemes
- When premium subscription is activated
- Payment confirmations

#### 2. Document Creation
- When new session plans are created for them
- When new schemes of work are generated
- Document ready for download alerts

#### 3. System Events
- Welcome messages for new users
- Important system announcements
- Maintenance notifications

## Technical Implementation

### Backend API Endpoints

#### Create Notification
```http
POST /notifications/
Content-Type: application/json

{
  "user_id": 1,
  "title": "Notification Title",
  "message": "Notification message",
  "type": "info"
}
```

#### Bulk Notification
```http
POST /notifications/bulk
Content-Type: application/json

{
  "title": "Announcement Title",
  "message": "Message for all users",
  "type": "success",
  "user_ids": [1, 2, 3] // Optional: specific users
}
```

#### Get User Notifications
```http
GET /notifications/user/{user_id}
```

#### Mark as Read
```http
PUT /notifications/{notification_id}/read
```

#### Get Unread Count
```http
GET /notifications/unread/{user_id}
```

### Database Schema

```sql
CREATE TABLE notifications (
    id INTEGER PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    title VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    type VARCHAR(50) DEFAULT 'info',
    is_read BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Frontend Integration

#### JavaScript Functions
```javascript
// Get notifications for current user
await getNotifications()

// Mark notification as read
await markNotificationAsRead(notificationId)

// Get unread count
await getUnreadCount()

// Display notification bell
await addNotificationBell()

// Show notification panel
await showNotificationPanel()
```

## Testing the System

### Run Notification Test
```bash
cd "c:\Users\PC\Music\Scheme of work and session plan planner"
python test_notifications_simple.py
```

### Expected Output
```
Testing RTB Notification System
==================================================
1. Testing API connection...
[OK] API is healthy

2. Getting users...
[OK] Found X users

3. Testing single user notification...
[OK] Single notification created

4. Testing bulk notification...
[OK] Bulk notification sent to X users

5. Testing notification retrieval...
[OK] Retrieved X notifications for user

6. Testing unread count...
[OK] Unread notifications: X

7. Testing mark as read...
[OK] Notification marked as read

NOTIFICATION SYSTEM TEST COMPLETE!
```

## Best Practices

### For Administrators
1. **Use templates** for consistent messaging
2. **Test notifications** before sending to all users
3. **Keep messages clear** and actionable
4. **Use appropriate notification types** (success, info, warning, error)
5. **Don't spam users** - send meaningful notifications only

### For Developers
1. **Always handle errors** when sending notifications
2. **Use async functions** for notification operations
3. **Refresh notification bell** after operations
4. **Test with different user roles**
5. **Handle network failures gracefully**

## Troubleshooting

### Common Issues

#### Notifications Not Appearing
1. Check if backend is running on port 8000
2. Verify user is logged in correctly
3. Check browser console for JavaScript errors
4. Ensure notification bell is initialized

#### Admin Can't Send Notifications
1. Verify admin login credentials
2. Check if users exist in database
3. Test API endpoints directly
4. Check network connectivity

#### Database Errors
1. Run database initialization: `python backend/init_db.py`
2. Check if Notification table exists
3. Verify user relationships are correct

### Debug Commands

#### Check API Health
```bash
curl http://localhost:8000/health
```

#### List All Users
```bash
curl http://localhost:8000/users/
```

#### Get User Notifications
```bash
curl http://localhost:8000/notifications/user/1
```

## Future Enhancements

### Planned Features
- **Email notifications** for important events
- **SMS notifications** for critical alerts
- **Notification scheduling** for future delivery
- **Notification categories** and filtering
- **Push notifications** for mobile apps
- **Notification history** and analytics

### Integration Possibilities
- **WhatsApp Business API** for instant messaging
- **Email service** (SendGrid, AWS SES)
- **SMS gateway** for text notifications
- **Mobile push notifications** (Firebase)

## Support

For technical support or questions about the notification system:

1. **Check this guide** for common solutions
2. **Run the test script** to verify system health
3. **Check backend logs** for error messages
4. **Contact system administrator** for assistance

---

**RTB Document Planner Notification System** - Keeping teachers informed and engaged! 🔔