// In-app notification system with backend integration
const NOTIFICATIONS_KEY = 'rtb_notifications';
let currentUserId = null;

// Get current user ID from session
function getCurrentUserId() {
    const session = getCurrentSession();
    return session ? session.user_id : null;
}

// Fetch notifications from backend
async function getNotifications() {
    try {
        const session = getCurrentSession();
        if (!session) return [];
        
        // Get user ID from backend
        const usersResponse = await fetch(`${API_BASE}/users/`);
        const users = await usersResponse.json();
        const user = users.find(u => u.user_id === session.user_id);
        
        if (!user) return [];
        
        const response = await fetch(`${API_BASE}/notifications/user/${user.id}`);
        if (response.ok) {
            return await response.json();
        }
    } catch (error) {
        console.error('Error fetching notifications:', error);
    }
    return [];
}

// Mark notification as read
async function markNotificationAsRead(notificationId) {
    try {
        await fetch(`${API_BASE}/notifications/${notificationId}/read`, {
            method: 'PUT'
        });
    } catch (error) {
        console.error('Error marking notification as read:', error);
    }
}

// Get unread count
async function getUnreadCount() {
    try {
        const session = getCurrentSession();
        if (!session) return 0;
        
        const usersResponse = await fetch(`${API_BASE}/users/`);
        const users = await usersResponse.json();
        const user = users.find(u => u.user_id === session.user_id);
        
        if (!user) return 0;
        
        const response = await fetch(`${API_BASE}/notifications/unread/${user.id}`);
        if (response.ok) {
            const result = await response.json();
            return result.unread_count;
        }
    } catch (error) {
        console.error('Error getting unread count:', error);
    }
    return 0;
}

function clearAllNotifications() {
    // This will be handled by backend in future versions
    localStorage.removeItem(NOTIFICATIONS_KEY);
}

// Display notification widget on user pages
async function displayNotificationWidget() {
    let widget = document.getElementById('notificationWidget');
    
    if (!widget) {
        widget = document.createElement('div');
        widget.id = 'notificationWidget';
        widget.style.cssText = 'position: fixed; top: 1rem; right: 1rem; z-index: 10000; max-width: 400px;';
        document.body.appendChild(widget);
    }
    
    const allNotifications = await getNotifications();
    const notifications = allNotifications.filter(n => !n.is_read).slice(0, 3);
    
    widget.innerHTML = notifications.map(notif => {
        const typeIcon = notif.type === 'success' ? 'fa-check-circle' : 
                        notif.type === 'warning' ? 'fa-exclamation-triangle' : 
                        notif.type === 'error' ? 'fa-times-circle' : 'fa-info-circle';
        const typeColor = notif.type === 'success' ? '#10b981' : 
                         notif.type === 'warning' ? '#f59e0b' : 
                         notif.type === 'error' ? '#ef4444' : '#6366f1';
        
        return `
        <div style="background: white; padding: 1.5rem; border-radius: 0.75rem; margin-bottom: 1rem; box-shadow: 0 10px 40px rgba(0,0,0,0.2); border-left: 4px solid ${typeColor}; animation: slideIn 0.3s ease;">
            <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 0.5rem;">
                <h4 style="color: #1e293b; font-size: 1rem; margin: 0; display: flex; align-items: center; gap: 0.5rem;">
                    <i class="fas ${typeIcon}" style="color: ${typeColor};"></i>
                    ${notif.title}
                </h4>
                <button onclick="dismissNotification(${notif.id})" style="background: none; border: none; color: #64748b; cursor: pointer; font-size: 1.25rem; padding: 0; line-height: 1;">
                    ×
                </button>
            </div>
            <p style="color: #64748b; font-size: 0.875rem; margin: 0; white-space: pre-line;">${notif.message}</p>
            <div style="margin-top: 0.75rem; font-size: 0.75rem; color: #94a3b8;">
                ${new Date(notif.created_at).toLocaleString()}
            </div>
        </div>
    `}).join('');
    
    if (notifications.length > 0) {
        setTimeout(() => {
            notifications.forEach(n => markNotificationAsRead(n.id));
            updateNotificationBell();
        }, 5000);
    }
}

async function dismissNotification(notificationId) {
    await markNotificationAsRead(notificationId);
    displayNotificationWidget();
    updateNotificationBell();
}

// Add notification bell to pages
async function addNotificationBell() {
    const bell = document.createElement('div');
    bell.id = 'notificationBell';
    bell.style.cssText = 'position: fixed; top: 1rem; right: 1rem; z-index: 9999; cursor: pointer;';
    
    const unreadCount = await getUnreadCount();
    
    bell.innerHTML = `
        <div style="position: relative; background: white; width: 56px; height: 56px; border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 12px rgba(0,0,0,0.15); transition: all 0.3s;">
            <i class="fas fa-bell" style="font-size: 1.5rem; color: #6366f1;"></i>
            ${unreadCount > 0 ? `<span style="position: absolute; top: 0; right: 0; background: #ef4444; color: white; width: 20px; height: 20px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 700;">${unreadCount}</span>` : ''}
        </div>
    `;
    
    bell.onclick = () => {
        const panel = document.getElementById('notificationPanel');
        if (panel) {
            panel.remove();
        } else {
            showNotificationPanel();
        }
    };
    
    document.body.appendChild(bell);
}

async function showNotificationPanel() {
    const panel = document.createElement('div');
    panel.id = 'notificationPanel';
    panel.style.cssText = 'position: fixed; top: 5rem; right: 1rem; width: 400px; max-height: 500px; background: white; border-radius: 1rem; box-shadow: 0 20px 60px rgba(0,0,0,0.3); z-index: 9998; overflow: hidden; animation: slideDown 0.3s ease;';
    
    const notifications = await getNotifications();
    
    panel.innerHTML = `
        <div style="padding: 1.5rem; border-bottom: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center;">
            <h3 style="margin: 0; color: #1e293b; font-size: 1.25rem;">
                <i class="fas fa-bell"></i> Notifications
            </h3>
            <button onclick="document.getElementById('notificationPanel').remove()" style="background: none; border: none; color: #64748b; cursor: pointer; font-size: 1.5rem; padding: 0;">×</button>
        </div>
        <div style="max-height: 400px; overflow-y: auto; padding: 1rem;">
            ${notifications.length === 0 ? 
                '<p style="text-align: center; color: #64748b; padding: 2rem;">No notifications</p>' :
                notifications.map(notif => {
                    const typeColor = notif.type === 'success' ? '#10b981' : 
                                     notif.type === 'warning' ? '#f59e0b' : 
                                     notif.type === 'error' ? '#ef4444' : '#6366f1';
                    return `
                    <div style="padding: 1rem; border-radius: 0.5rem; margin-bottom: 0.75rem; background: ${notif.is_read ? '#f8fafc' : '#eef2ff'}; border-left: 3px solid ${notif.is_read ? '#cbd5e1' : typeColor};">
                        <h4 style="margin: 0 0 0.5rem 0; color: #1e293b; font-size: 0.95rem;">${notif.title}</h4>
                        <p style="margin: 0; color: #64748b; font-size: 0.875rem; white-space: pre-line;">${notif.message}</p>
                        <div style="margin-top: 0.5rem; font-size: 0.75rem; color: #94a3b8;">
                            ${new Date(notif.created_at).toLocaleString()}
                        </div>
                    </div>
                `}).join('')
            }
        </div>
        ${notifications.length > 0 ? `
            <div style="padding: 1rem; border-top: 1px solid #e2e8f0; text-align: center;">
                <button onclick="clearAllNotifications(); document.getElementById('notificationPanel').remove(); updateNotificationBell();" style="background: none; border: none; color: #6366f1; cursor: pointer; font-weight: 600;">
                    <i class="fas fa-trash"></i> Clear All
                </button>
            </div>
        ` : ''}
    `;
    
    document.body.appendChild(panel);
}

async function updateNotificationBell() {
    const bell = document.getElementById('notificationBell');
    if (bell) {
        const unreadCount = await getUnreadCount();
        const badge = bell.querySelector('span');
        if (unreadCount > 0) {
            if (badge) {
                badge.textContent = unreadCount;
            } else {
                const newBadge = document.createElement('span');
                newBadge.style.cssText = 'position: absolute; top: 0; right: 0; background: #ef4444; color: white; width: 20px; height: 20px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 0.75rem; font-weight: 700;';
                newBadge.textContent = unreadCount;
                bell.querySelector('div').appendChild(newBadge);
            }
        } else if (badge) {
            badge.remove();
        }
    }
}

// Initialize notifications on pages that need them
if (typeof window !== 'undefined') {
    document.addEventListener('DOMContentLoaded', function() {
        const session = getCurrentSession();
        if (session && session.role !== 'admin') {
            // Only show notifications for regular users, not admins
            setTimeout(() => {
                addNotificationBell();
                displayNotificationWidget();
            }, 1000);
        }
    });
}

// Auto-refresh notifications every 30 seconds
setInterval(async () => {
    const session = getCurrentSession();
    if (session && session.role !== 'admin') {
        await updateNotificationBell();
    }
}, 30000);

// Export functions for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        getNotifications,
        markNotificationAsRead,
        getUnreadCount,
        displayNotificationWidget,
        addNotificationBell,
        updateNotificationBell
    };
}ionBell() {
    const bell = document.getElementById('notificationBell');
    if (bell) {
        bell.remove();
        await addNotificationBell();
    }
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes slideIn {
        from {
            transform: translateX(400px);
            opacity: 0;
        }
        to {
            transform: translateX(0);
            opacity: 1;
        }
    }
    @keyframes slideDown {
        from {
            transform: translateY(-20px);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }
`;
document.head.appendChild(style);

// Auto-initialize on user pages (not admin)
if (window.location.pathname.includes('wizard') || window.location.pathname.includes('scheme') || window.location.pathname.includes('index')) {
    window.addEventListener('load', async () => {
        await addNotificationBell();
        await displayNotificationWidget();
        
        // Refresh notifications every 30 seconds
        setInterval(async () => {
            await updateNotificationBell();
            await displayNotificationWidget();
        }, 30000);
    });
}
