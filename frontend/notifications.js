// Real-time Notification System
class NotificationSystem {
    constructor() {
        this.notifications = [];
        this.unreadCount = 0;
        this.isOpen = false;
        this.isMessageModalOpen = false;
        this.currentNotification = null;
        this.pollInterval = null;
        this.messagePollInterval = null;
        this.init();
    }

    init() {
        this.injectStyles();
        this.injectHTML();
        this.attachEventListeners();
        this.loadNotifications();
        // Poll for new notifications every 5 seconds
        this.pollInterval = setInterval(() => this.loadNotifications(), 5000);
    }

    injectStyles() {
        const style = document.createElement('style');
        style.textContent = `
            .notif-bell { position: relative; cursor: pointer; margin-left: 1rem; }
            .notif-bell i { font-size: 1.3rem; color: #fff; transition: 0.2s; }
            .notif-bell:hover i { color: #6366f1; }
            .notif-bell.has-new i { animation: bellRing 0.5s ease; }
            @keyframes bellRing { 0%, 100% { transform: rotate(0deg); } 25% { transform: rotate(-15deg); } 75% { transform: rotate(15deg); } }
            .notif-badge { position: absolute; top: -8px; right: -8px; background: #ef4444; color: #fff; border-radius: 999px; padding: 2px 6px; font-size: 0.7rem; font-weight: 700; min-width: 18px; text-align: center; animation: pulse 2s infinite; }
            @keyframes pulse { 0%, 100% { transform: scale(1); } 50% { transform: scale(1.1); } }
            .notif-panel { position: fixed; bottom: 80px; right: 20px; width: 420px; max-height: 600px; background: #fff; border-radius: 1rem; box-shadow: 0 20px 60px rgba(0,0,0,0.3); z-index: 1000; display: none; flex-direction: column; }
            .notif-panel.active { display: flex; animation: slideInBottom 0.3s ease; }
            @keyframes slideInBottom { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
            .notif-header { padding: 1.25rem; border-bottom: 1px solid #e5e7eb; display: flex; justify-content: space-between; align-items: center; }
            .notif-header h3 { margin: 0; font-size: 1.1rem; font-weight: 700; }
            .notif-close { background: none; border: none; font-size: 1.5rem; cursor: pointer; color: #6b7280; }
            .notif-list { flex: 1; overflow-y: auto; max-height: 400px; }
            .notif-item { padding: 1rem 1.25rem; border-bottom: 1px solid #f3f4f6; cursor: pointer; transition: 0.2s; }
            .notif-item:hover { background: #f9fafb; }
            .notif-item.unread { background: #eff6ff; border-left: 3px solid #3b82f6; }
            .notif-item-header { display: flex; justify-content: space-between; align-items: start; margin-bottom: 0.5rem; }
            .notif-title { font-weight: 600; font-size: 0.95rem; color: #1f2937; }
            .notif-time { font-size: 0.75rem; color: #9ca3af; }
            .notif-message { font-size: 0.9rem; color: #4b5563; line-height: 1.5; }
            .notif-empty { padding: 3rem; text-align: center; color: #9ca3af; }
            .notif-overlay { position: fixed; inset: 0; background: rgba(0,0,0,0.3); z-index: 999; display: none; }
            .notif-overlay.active { display: block; }
            
            .msg-modal { position: fixed; inset: 0; background: rgba(0,0,0,0.5); z-index: 2000; display: none; align-items: center; justify-content: center; }
            .msg-modal.active { display: flex; }
            .msg-box { background: #fff; border-radius: 1rem; width: 90%; max-width: 600px; max-height: 80vh; display: flex; flex-direction: column; box-shadow: 0 25px 80px rgba(0,0,0,0.4); }
            .msg-header { padding: 1.5rem; border-bottom: 1px solid #e5e7eb; display: flex; justify-content: space-between; align-items: center; }
            .msg-header h3 { margin: 0; font-size: 1.2rem; font-weight: 700; }
            .msg-close { background: none; border: none; font-size: 1.5rem; cursor: pointer; color: #6b7280; }
            .msg-thread { flex: 1; overflow-y: auto; padding: 1.5rem; display: flex; flex-direction: column; gap: 1rem; max-height: 400px; }
            .msg-bubble { padding: 1rem; border-radius: 1rem; max-width: 80%; }
            .msg-bubble.admin { background: #eff6ff; align-self: flex-start; border-bottom-left-radius: 0.25rem; }
            .msg-bubble.user { background: #6366f1; color: #fff; align-self: flex-end; border-bottom-right-radius: 0.25rem; }
            .msg-bubble-header { display: flex; justify-content: space-between; margin-bottom: 0.5rem; font-size: 0.8rem; opacity: 0.8; }
            .msg-bubble-text { line-height: 1.5; }
            .msg-reply { padding: 1rem 1.5rem; border-top: 1px solid #e5e7eb; display: flex; gap: 0.75rem; }
            .msg-input { flex: 1; border: 1px solid #d1d5db; border-radius: 0.5rem; padding: 0.75rem; font-size: 0.95rem; resize: none; min-height: 60px; }
            .msg-send { background: #6366f1; color: #fff; border: none; border-radius: 0.5rem; padding: 0.75rem 1.5rem; cursor: pointer; font-weight: 600; }
            .msg-send:hover { background: #4f46e5; }
            .msg-send:disabled { background: #9ca3af; cursor: not-allowed; }
        `;
        document.head.appendChild(style);
    }

    injectHTML() {
        const html = `
            <div class="notif-bell" id="notifBell">
                <i class="fas fa-bell"></i>
                <span class="notif-badge" id="notifBadge" style="display: none;">0</span>
            </div>
            <div class="notif-overlay" id="notifOverlay"></div>
            <div class="notif-panel" id="notifPanel">
                <div class="notif-header">
                    <h3><i class="fas fa-bell"></i> Notifications</h3>
                    <button class="notif-close" id="notifClose">&times;</button>
                </div>
                <div class="notif-list" id="notifList"></div>
            </div>
            <div class="msg-modal" id="msgModal">
                <div class="msg-box">
                    <div class="msg-header">
                        <h3><i class="fas fa-comments"></i> Message Thread</h3>
                        <button class="msg-close" id="msgClose">&times;</button>
                    </div>
                    <div class="msg-thread" id="msgThread"></div>
                    <div class="msg-reply">
                        <textarea id="msgInput" class="msg-input" placeholder="Type your reply..."></textarea>
                        <button id="msgSend" class="msg-send"><i class="fas fa-paper-plane"></i> Send</button>
                    </div>
                </div>
            </div>
        `;
        
        const userInfo = document.querySelector('.user-info');
        if (userInfo) {
            userInfo.insertAdjacentHTML('afterbegin', html);
        }
    }

    attachEventListeners() {
        document.getElementById('notifBell').addEventListener('click', () => this.togglePanel());
        document.getElementById('notifClose').addEventListener('click', () => this.closePanel());
        document.getElementById('notifOverlay').addEventListener('click', () => this.closePanel());
        document.getElementById('msgClose').addEventListener('click', () => this.closeMessageModal());
        document.getElementById('msgSend').addEventListener('click', () => this.sendReply());
        
        // Support Enter key to send (Shift+Enter for new line)
        document.getElementById('msgInput').addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendReply();
            }
        });
    }

    togglePanel() {
        this.isOpen = !this.isOpen;
        document.getElementById('notifPanel').classList.toggle('active', this.isOpen);
        document.getElementById('notifOverlay').classList.toggle('active', this.isOpen);
    }

    closePanel() {
        this.isOpen = false;
        document.getElementById('notifPanel').classList.remove('active');
        document.getElementById('notifOverlay').classList.remove('active');
    }

    async loadNotifications() {
        const session = getCurrentSession();
        if (!session) return;

        try {
            const response = await fetch(`${API_BASE}/users/${encodeURIComponent(session.phone)}/notifications`);
            if (response.ok) {
                const newNotifications = await response.json();
                const oldUnreadCount = this.unreadCount;
                this.notifications = newNotifications;
                this.unreadCount = this.notifications.filter(n => !n.is_read).length;
                
                // Trigger bell animation if new unread messages
                if (this.unreadCount > oldUnreadCount) {
                    const bell = document.getElementById('notifBell');
                    bell.classList.add('has-new');
                    setTimeout(() => bell.classList.remove('has-new'), 500);
                }
                
                this.updateUI();
            }
        } catch (error) {
            console.error('Failed to load notifications:', error);
        }
    }

    updateUI() {
        const badge = document.getElementById('notifBadge');
        if (this.unreadCount > 0) {
            badge.textContent = this.unreadCount;
            badge.style.display = 'block';
        } else {
            badge.style.display = 'none';
        }

        const list = document.getElementById('notifList');
        if (this.notifications.length === 0) {
            list.innerHTML = '<div class="notif-empty"><i class="fas fa-inbox fa-2x"></i><p>No notifications yet</p></div>';
            return;
        }

        list.innerHTML = this.notifications.map(n => `
            <div class="notif-item ${n.is_read ? '' : 'unread'}" data-id="${n.id}">
                <div class="notif-item-header">
                    <span class="notif-title">${n.title}</span>
                    <span class="notif-time">${this.formatTime(n.created_at)}</span>
                </div>
                <div class="notif-message">${n.message}</div>
            </div>
        `).join('');

        list.querySelectorAll('.notif-item').forEach(item => {
            item.addEventListener('click', () => this.openNotification(parseInt(item.dataset.id)));
        });
    }

    async openNotification(id) {
        const notification = this.notifications.find(n => n.id === id);
        if (!notification) return;

        // Mark as read
        if (!notification.is_read) {
            await this.markAsRead(id);
        }

        this.closePanel();
        this.openMessageModal(notification);
    }

    async markAsRead(id) {
        try {
            await fetch(`${API_BASE}/notifications/${id}/read`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' }
            });
            const notif = this.notifications.find(n => n.id === id);
            if (notif) notif.is_read = true;
            this.unreadCount = Math.max(0, this.unreadCount - 1);
            this.updateUI();
        } catch (error) {
            console.error('Failed to mark as read:', error);
        }
    }

    openMessageModal(notification) {
        this.currentNotification = notification;
        this.isMessageModalOpen = true;
        document.getElementById('msgModal').classList.add('active');
        this.loadMessageThread(notification.id);
        // Start real-time polling for new replies every 3 seconds
        this.messagePollInterval = setInterval(() => {
            if (this.isMessageModalOpen && this.currentNotification) {
                this.loadMessageThread(this.currentNotification.id, true);
            }
        }, 3000);
    }

    closeMessageModal() {
        this.isMessageModalOpen = false;
        document.getElementById('msgModal').classList.remove('active');
        this.currentNotification = null;
        // Stop real-time polling
        if (this.messagePollInterval) {
            clearInterval(this.messagePollInterval);
            this.messagePollInterval = null;
        }
    }

    async loadMessageThread(notificationId, silent = false) {
        const thread = document.getElementById('msgThread');
        const previousScrollHeight = thread.scrollHeight;
        const wasAtBottom = thread.scrollTop + thread.clientHeight >= previousScrollHeight - 50;
        
        thread.innerHTML = `
            <div class="msg-bubble admin">
                <div class="msg-bubble-header">
                    <strong>Admin</strong>
                    <span>${this.formatTime(this.currentNotification.created_at)}</span>
                </div>
                <div class="msg-bubble-text">${this.currentNotification.message}</div>
            </div>
        `;

        // Load replies
        try {
            const response = await fetch(`${API_BASE}/notifications/${notificationId}/replies`);
            if (response.ok) {
                const replies = await response.json();
                replies.forEach(reply => {
                    thread.innerHTML += `
                        <div class="msg-bubble ${reply.sender === 'admin' ? 'admin' : 'user'}">
                            <div class="msg-bubble-header">
                                <strong>${reply.sender === 'admin' ? 'Admin' : 'You'}</strong>
                                <span>${this.formatTime(reply.created_at)}</span>
                            </div>
                            <div class="msg-bubble-text">${reply.message}</div>
                        </div>
                    `;
                });
                // Auto-scroll to bottom if user was already at bottom or if new message
                if (wasAtBottom || !silent) {
                    thread.scrollTop = thread.scrollHeight;
                }
            }
        } catch (error) {
            if (!silent) console.error('Failed to load replies:', error);
        }
    }

    async sendReply() {
        const input = document.getElementById('msgInput');
        const message = input.value.trim();
        if (!message || !this.currentNotification) return;

        const btn = document.getElementById('msgSend');
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i>';

        try {
            const session = getCurrentSession();
            const response = await fetch(`${API_BASE}/notifications/${this.currentNotification.id}/reply`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    message,
                    sender: 'user',
                    sender_phone: session.phone
                })
            });

            if (response.ok) {
                input.value = '';
                // Immediately reload thread to show new reply
                await this.loadMessageThread(this.currentNotification.id);
            } else {
                throw new Error('Failed to send');
            }
        } catch (error) {
            console.error('Failed to send reply:', error);
            alert('Failed to send reply. Please try again.');
        } finally {
            btn.disabled = false;
            btn.innerHTML = '<i class="fas fa-paper-plane"></i> Send';
        }
    }

    formatTime(timestamp) {
        if (!timestamp) return '';
        const date = new Date(timestamp);
        const now = new Date();
        const diff = now - date;
        const minutes = Math.floor(diff / 60000);
        const hours = Math.floor(diff / 3600000);
        const days = Math.floor(diff / 86400000);

        if (minutes < 1) return 'Just now';
        if (minutes < 60) return `${minutes}m ago`;
        if (hours < 24) return `${hours}h ago`;
        if (days < 7) return `${days}d ago`;
        return date.toLocaleDateString();
    }
}

// Auto-initialize on page load
if (typeof getCurrentSession === 'function') {
    document.addEventListener('DOMContentLoaded', () => {
        const session = getCurrentSession();
        if (session && session.role !== 'admin') {
            new NotificationSystem();
        }
    });
}
