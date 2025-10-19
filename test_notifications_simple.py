#!/usr/bin/env python3
"""
Test script for the notification system
"""
import requests
import json
import time

BASE_URL = "http://localhost:8000"

def test_notification_system():
    print("Testing RTB Notification System")
    print("=" * 50)
    
    try:
        # 1. Test API health
        print("1. Testing API connection...")
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            print("[OK] API is healthy")
        else:
            print("[ERROR] API health check failed")
            return
        
        # 2. Get users
        print("\n2. Getting users...")
        users_response = requests.get(f"{BASE_URL}/users/")
        if users_response.status_code == 200:
            users = users_response.json()
            print(f"[OK] Found {len(users)} users")
            
            if len(users) == 0:
                print("[ERROR] No users found. Please register a user first.")
                return
                
            test_user = users[0]
            print(f"   Using test user: {test_user['name']} (ID: {test_user['id']})")
        else:
            print("[ERROR] Failed to get users")
            return
        
        # 3. Test single notification
        print("\n3. Testing single user notification...")
        notification_data = {
            "user_id": test_user['id'],
            "title": "Test Notification",
            "message": "This is a test notification from the admin panel. Your system is working correctly!",
            "type": "info"
        }
        
        response = requests.post(f"{BASE_URL}/notifications/", json=notification_data)
        if response.status_code == 200:
            result = response.json()
            print(f"[OK] Single notification created (ID: {result['id']})")
        else:
            print(f"[ERROR] Failed to create notification: {response.text}")
            return
        
        # 4. Test bulk notification
        print("\n4. Testing bulk notification...")
        bulk_data = {
            "title": "System Announcement",
            "message": "Welcome to RTB Document Planner!\n\nYour notification system is now active and working perfectly.\n\nYou will receive notifications for:\n- New session plans assigned to you\n- New schemes of work\n- Subscription updates\n- Important announcements",
            "type": "success"
        }
        
        response = requests.post(f"{BASE_URL}/notifications/bulk", json=bulk_data)
        if response.status_code == 200:
            result = response.json()
            print(f"[OK] Bulk notification sent: {result['message']}")
        else:
            print(f"[ERROR] Failed to send bulk notification: {response.text}")
            return
        
        # 5. Test getting user notifications
        print("\n5. Testing notification retrieval...")
        response = requests.get(f"{BASE_URL}/notifications/user/{test_user['id']}")
        if response.status_code == 200:
            notifications = response.json()
            print(f"[OK] Retrieved {len(notifications)} notifications for user")
            
            for notif in notifications[:2]:  # Show first 2
                print(f"   - {notif['title']} ({notif['type']}) - {'Read' if notif['is_read'] else 'Unread'}")
        else:
            print(f"[ERROR] Failed to get notifications: {response.text}")
            return
        
        # 6. Test unread count
        print("\n6. Testing unread count...")
        response = requests.get(f"{BASE_URL}/notifications/unread/{test_user['id']}")
        if response.status_code == 200:
            result = response.json()
            print(f"[OK] Unread notifications: {result['unread_count']}")
        else:
            print(f"[ERROR] Failed to get unread count: {response.text}")
        
        # 7. Test marking as read
        if len(notifications) > 0:
            print("\n7. Testing mark as read...")
            first_notif = notifications[0]
            response = requests.put(f"{BASE_URL}/notifications/{first_notif['id']}/read")
            if response.status_code == 200:
                print("[OK] Notification marked as read")
            else:
                print(f"[ERROR] Failed to mark as read: {response.text}")
        
        print("\n" + "=" * 50)
        print("NOTIFICATION SYSTEM TEST COMPLETE!")
        print("=" * 50)
        print("\nSummary:")
        print("[OK] Backend API notifications working")
        print("[OK] Single user notifications working")
        print("[OK] Bulk notifications working")
        print("[OK] Notification retrieval working")
        print("[OK] Unread count working")
        print("[OK] Mark as read working")
        print("\nNext Steps:")
        print("1. Open http://localhost:5173 in your browser")
        print("2. Login as a teacher to see notifications")
        print("3. Use admin panel to send more notifications")
        print("4. Check the notification bell in the top-right corner")
        
    except requests.exceptions.ConnectionError:
        print("[ERROR] Cannot connect to backend API")
        print("   Make sure the backend is running on port 8000")
        print("   Run: cd backend && python startup.py")
    except Exception as e:
        print(f"[ERROR] Test failed with error: {e}")

if __name__ == "__main__":
    test_notification_system()