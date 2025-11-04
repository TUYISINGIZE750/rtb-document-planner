// Admin Real-time Notification System
class AdminNotificationSystem {
    constructor() {
        this.conversations = [];
        this.isOpen = false;
        this.currentConversation = null;
        this.pollInterval = null;
        this.messagePollInterval = null;
        this.init();
    }

    init() {
        this.injectStyles();
        this.injectHTML();
        this.attachEventListeners();
        this.loadConversations();
        // Poll for new messages every 5 seconds
        this.pollInterval = setInterval(() => this.loadConversations(), 5000);
    }

    injectStyles() {
        const style = document.createElement('style');
        style.textContent = `
            .admin-chat-btn { position: fixed; bottom: 20px; right: 20px; width: 60px; height: 60px; background: #6366f1; color: #fff; border: none; border-radius: 50%; cursor: pointer; box-shadow: 0 8px 24px rgba(99,102,241,0.4); z-index: 1000; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; transition: 0.2s; }
            .admin-chat-btn:hover { background: #4f46e5; transform: scale(1.05); }
            .admin-chat-btn.has-new { animation: pulse 2s infinite; }
            .admin-chat-badge { position: absolute; top: -5px; right: -5px; background: #ef4444; color: #fff; border-radius: 999px; padding: 4px 8px; font-size: 0.7rem; font-weight: 700; min-width: 22px; text-align: center; }
            
            .admin-chat-panel { position: fixed; bottom: 90px; right: 20px; width: 450px; max-height: 650px; background: #fff; border-radius: 1rem; box-shadow: 0 20px 60px rgba(0,0,0,0.3); z-index: 1001; display: none; flex-direction: column; }
            .admin-chat-panel.active { display: flex; animation: slideInBottom 0.3s ease; }
            @keyframes slideInBottom { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
            
            .admin-chat-header { padding: 1.25rem; border-bottom: 1px solid #e5e7eb; display: flex; justify-content: space-between; align-items: center; background: linear-gradient(135deg, #6366f1, #4f46e5); color: #fff; border-radius: 1rem 1rem 0 0; }
            .admin-chat-header h3 { margin: 0; font-size: 1.1rem; font-weight: 700; }
            .admin-chat-close { background: rgba(255,255,255,0.2); border: none; color: #fff; border-radius: 50%; width: 32px; height: 32px; font-size: 1.2rem; cursor: pointer; }
            
            .admin-conv-list { flex: 1; overflow-y: auto; max-height: 400px; }
            .admin-conv-item { padding: 1rem 1.25rem; border-bottom: 1px solid #f3f4f6; cursor: pointer; transition: 0.2s; }
            .admin-conv-item:hover { background: #f9fafb; }
            .admin-conv-item.unread { background: #eff6ff; border-left: 3px solid #3b82f6; }
            .admin-conv-header { display: flex; justify-content: space-between; align-items: start; margin-bottom: 0.5rem; }
            .admin-conv-name { font-weight: 600; font-size: 0.95rem; color: #1f2937; }
            .admin-conv-time { font-size: 0.75rem; color: #9ca3af; }
            .admin-conv-preview { font-size: 0.85rem; color: #6b7280; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
            .admin-conv-empty { padding: 3rem; text-align: center; color: #9ca3af; }
            
            .admin-msg-modal { position: fixed; inset: 0; background: rgba(0,0,0,0.5); z-index: 2000; display: none; align-items: center; justify-content: center; }
            .admin-msg-modal.active { display: flex; }
            .admin-msg-box { background: #fff; border-radius: 1rem; width: 90%; max-width: 650px; max-height: 85vh; display: flex; flex-direction: column; box-shadow: 0 25px 80px rgba(0,0,0,0.4); }
            .admin-msg-header { padding: 1.5rem; border-bottom: 1px solid #e5e7eb; display: flex; justify-content: space-between; align-items: center; background: linear-gradient(135deg, #6366f1, #4f46e5); color: #fff; border-radius: 1rem 1rem 0 0; }
            .admin-msg-header h3 { margin: 0; font-size: 1.2rem; font-weight: 700; }
            .admin-msg-close { background: rgba(255,255,255,0.2); border: none; color: #fff; border-radius: 50%; width: 36px; height: 36px; font-size: 1.3rem; cursor: pointer; }
            .admin-msg-thread { flex: 1; overflow-y: auto; padding: 1.5rem; display: flex; flex-direction: column; gap: 1rem; max-height: 450px; background: #f9fafb; }
            .admin-msg-bubble { padding: 1rem; border-radius: 1rem; max-width: 75%; }
            .admin-msg-bubble.admin { background: #6366f1; color: #fff; align-self: flex-end; border-bottom-right-radius: 0.25rem; }
            .admin-msg-bubble.user { background: #fff; border: 1px solid #e5e7eb; align-self: flex-start; border-bottom-left-radius: 0.25rem; }
            .admin-msg-bubble-header { display: flex; justify-content: space-between; margin-bottom: 0.5rem; font-size: 0.8rem; opacity: 0.8; }
            .admin-msg-bubble-text { line-height: 1.5; }
            .admin-msg-reply { padding: 1rem 1.5rem; border-top: 1px solid #e5e7eb; display: flex; gap: 0.75rem; background: #fff; }
            .admin-msg-input { flex: 1; border: 1px solid #d1d5db; border-radius: 0.5rem; padding: 0.75rem; font-size: 0.95rem; resize: none; min-height: 60px; }
            .admin-msg-send { background: #6366f1; color: #fff; border: none; border-radius: 0.5rem; padding: 0.75rem 1.5rem; cursor: pointer; font-weight: 600; }
            .admin-msg-send:hover { background: #4f46e5; }
            .admin-msg-send:disabled { background: #9ca3af; cursor: not-allowed; }
        `;
        document.head.appendChild(style);
    }

    injectHTML() {
        const html = `
            <button class="admin-chat-btn" id="adminChatBtn">
                <i class="fas fa-comments"></i>
                <span class="admin-chat-badge" id="adminChatBadge" style="display: none;">0</span>
            </button>
            <div class="admin-chat-panel" id="adminChatPanel">
                <div class="admin-chat-header">
                    <h3><i class="fas fa-comments"></i> Messages</h3>
                    <button class="admin-chat-close" id="adminChatClose">&times;</button>
                </div>
                <div class="admin-conv-list" id="adminConvList"></div>
            </div>
            <div class="admin-msg-modal" id="adminMsgModal">
                <div class="admin-msg-box">
                    <div class="admin-msg-header">
                        <h3 id="adminMsgTitle"><i class="fas fa-user"></i> Conversation</h3>
                        <button class="admin-msg-close" id="adminMsgClose">&times;</button>
                    </div>
                    <div class="admin-msg-thread" id="adminMsgThread"></div>
                    <div class="admin-msg-reply">
                        <textarea id="adminMsgInput" class="admin-msg-input" placeholder="Type your reply..."></textarea>
                        <button id="adminMsgSend" class="admin-msg-send"><i class="fas fa-paper-plane"></i> Send</button>
                    </div>
                </div>
            </div>
        `;
        document.body.insertAdjacentHTML('beforeend', html);
    }

    attachEventListeners() {
        document.getElementById('adminChatBtn').addEventListener('click', () => this.togglePanel());
        document.getElementById('adminChatClose').addEventListener('click', () => this.closePanel());
        document.getElementById('adminMsgClose').addEventListener('click', () => this.closeMessageModal());
        document.getElementById('adminMsgSend').addEventListener('click', () => this.sendReply());
        
        // Support Enter key to send (Shift+Enter for new line)
        document.getElementById('adminMsgInput').addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendReply();
            }
        });
    }

    togglePanel() {
        this.isOpen = !this.isOpen;
        document.getElementById('adminChatPanel').classList.toggle('active', this.isOpen);
    }

    closePanel() {
        this.isOpen = false;
        document.getElementById('adminChatPanel').classList.remove('active');
    }

    async loadConversations() {
        try {
            const response = await fetch(`${apiBase}/admin/conversations`);
            if (response.ok) {
                const newConversations = await response.json();
                const oldUnreadCount = this.conversations.filter(c => c.has_unread).length;
                this.conversations = newConversations;
                const unreadCount = this.conversations.filter(c => c.has_unread).length;
                
                // Trigger animation if new unread messages
                if (unreadCount > oldUnreadCount) {
                    const btn = document.getElementById('adminChatBtn');
                    btn.classList.add('has-new');
                    setTimeout(() => btn.classList.remove('has-new'), 500);
                }
                
                this.updateUI();
            }
        } catch (error) {
            console.error('Failed to load conversations:', error);
        }
    }

    updateUI() {
        const badge = document.getElementById('adminChatBadge');
        const unreadCount = this.conversations.filter(c => c.has_unread).length;
        
        if (unreadCount > 0) {
            badge.textContent = unreadCount;
            badge.style.display = 'block';
        } else {
            badge.style.display = 'none';
        }

        const list = document.getElementById('adminConvList');
        if (this.conversations.length === 0) {
            list.innerHTML = '<div class="admin-conv-empty"><i class="fas fa-inbox fa-2x"></i><p>No conversations yet</p></div>';
            return;
        }

        list.innerHTML = this.conversations.map(c => `
            <div class="admin-conv-item ${c.has_unread ? 'unread' : ''}" data-phone="${c.user_phone}">
                <div class="admin-conv-header">
                    <span class="admin-conv-name">${c.user_name || c.user_phone}</span>
                    <span class="admin-conv-time">${this.formatTime(c.last_message_time)}</span>
                </div>
                <div class="admin-conv-preview">${c.last_message || 'No messages'}</div>
            </div>
        `).join('');

        list.querySelectorAll('.admin-conv-item').forEach(item => {
            item.addEventListener('click', () => this.openConversation(item.dataset.phone));
        });
    }

    async openConversation(userPhone) {
        const conversation = this.conversations.find(c => c.user_phone === userPhone);
        if (!conversation) return;

        this.currentConversation = conversation;
        this.closePanel();
        this.openMessageModal(conversation);
    }

    openMessageModal(conversation) {
        document.getElementById('adminMsgTitle').innerHTML = `<i class="fas fa-user"></i> ${conversation.user_name || conversation.user_phone}`;
        document.getElementById('adminMsgModal').classList.add('active');
        this.loadMessageThread(conversation.notification_id);
        
        // Start real-time polling for new replies every 3 seconds
        this.messagePollInterval = setInterval(() => {
            if (this.currentConversation) {
                this.loadMessageThread(this.currentConversation.notification_id, true);
            }
        }, 3000);
    }

    closeMessageModal() {
        document.getElementById('adminMsgModal').classList.remove('active');
        this.currentConversation = null;
        
        // Stop real-time polling
        if (this.messagePollInterval) {
            clearInterval(this.messagePollInterval);
            this.messagePollInterval = null;
        }
        
        // Reload conversations to update unread status
        this.loadConversations();
    }

    async loadMessageThread(notificationId, silent = false) {
        const thread = document.getElementById('adminMsgThread');
        const previousScrollHeight = thread.scrollHeight;
        const wasAtBottom = thread.scrollTop + thread.clientHeight >= previousScrollHeight - 50;

        try {
            const response = await fetch(`${apiBase}/notifications/${notificationId}`);
            if (response.ok) {
                const notification = await response.json();
                
                thread.innerHTML = `
                    <div class="admin-msg-bubble admin">
                        <div class="admin-msg-bubble-header">
                            <strong>You (Admin)</strong>
                            <span>${this.formatTime(notification.created_at)}</span>
                        </div>
                        <div class="admin-msg-bubble-text">${notification.message}</div>
                    </div>
                `;

                // Load replies
                const repliesResponse = await fetch(`${apiBase}/notifications/${notificationId}/replies`);
                if (repliesResponse.ok) {
                    const replies = await repliesResponse.json();
                    replies.forEach(reply => {
                        thread.innerHTML += `
                            <div class="admin-msg-bubble ${reply.sender === 'admin' ? 'admin' : 'user'}">
                                <div class="admin-msg-bubble-header">
                                    <strong>${reply.sender === 'admin' ? 'You (Admin)' : this.currentConversation.user_name || 'Teacher'}</strong>
                                    <span>${this.formatTime(reply.created_at)}</span>
                                </div>
                                <div class="admin-msg-bubble-text">${reply.message}</div>
                            </div>
                        `;
                    });
                    
                    // Auto-scroll to bottom if user was already at bottom or if new message
                    if (wasAtBottom || !silent) {
                        thread.scrollTop = thread.scrollHeight;
                    }
                }
            }
        } catch (error) {
            if (!silent) console.error('Failed to load thread:', error);
        }
    }

    async sendReply() {
        const input = document.getElementById('adminMsgInput');
        const message = input.value.trim();
        if (!message || !this.currentConversation) return;

        const btn = document.getElementById('adminMsgSend');
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i>';

        try {
            const response = await fetch(`${apiBase}/notifications/${this.currentConversation.notification_id}/reply`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    message,
                    sender: 'admin',
                    sender_phone: 'admin'
                })
            });

            if (response.ok) {
                input.value = '';
                // Immediately reload thread to show new reply
                await this.loadMessageThread(this.currentConversation.notification_id);
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

// Auto-initialize on admin page
document.addEventListener('DOMContentLoaded', () => {
    const session = typeof getCurrentSession === 'function' ? getCurrentSession() : null;
    if (session && session.role === 'admin') {
        new AdminNotificationSystem();
    }
});
