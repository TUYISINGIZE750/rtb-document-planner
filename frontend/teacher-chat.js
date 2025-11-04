// Teacher Real-time Chat System
class TeacherChatSystem {
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
        this.pollInterval = setInterval(() => this.loadConversations(), 5000);
    }

    injectStyles() {
        const style = document.createElement('style');
        style.textContent = `
            .teacher-chat-btn { position: fixed; bottom: 20px; right: 20px; width: 60px; height: 60px; background: linear-gradient(135deg, #6366f1, #4f46e5); color: #fff; border: none; border-radius: 50%; cursor: pointer; box-shadow: 0 8px 24px rgba(99,102,241,0.4); z-index: 1000; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; transition: 0.2s; }
            .teacher-chat-btn:hover { transform: scale(1.05); }
            .teacher-chat-btn.has-new { animation: pulse 2s infinite; }
            .teacher-chat-badge { position: absolute; top: -5px; right: -5px; background: #ef4444; color: #fff; border-radius: 999px; padding: 4px 8px; font-size: 0.7rem; font-weight: 700; min-width: 22px; text-align: center; }
            
            .teacher-chat-panel { position: fixed; bottom: 90px; right: 20px; width: 450px; max-height: 650px; background: #fff; border-radius: 1rem; box-shadow: 0 20px 60px rgba(0,0,0,0.3); z-index: 1001; display: none; flex-direction: column; }
            .teacher-chat-panel.active { display: flex; }
            
            .teacher-chat-header { padding: 1.25rem; border-bottom: 1px solid #e5e7eb; display: flex; justify-content: space-between; align-items: center; background: linear-gradient(135deg, #6366f1, #4f46e5); color: #fff; border-radius: 1rem 1rem 0 0; }
            .teacher-chat-header h3 { margin: 0; font-size: 1.1rem; font-weight: 700; }
            .teacher-chat-close { background: rgba(255,255,255,0.2); border: none; color: #fff; border-radius: 50%; width: 32px; height: 32px; font-size: 1.2rem; cursor: pointer; }
            
            .teacher-conv-list { flex: 1; overflow-y: auto; max-height: 400px; }
            .teacher-conv-item { padding: 1rem 1.25rem; border-bottom: 1px solid #f3f4f6; cursor: pointer; transition: 0.2s; }
            .teacher-conv-item:hover { background: #f9fafb; }
            .teacher-conv-item.unread { background: #eff6ff; border-left: 3px solid #3b82f6; }
            .teacher-conv-header { display: flex; justify-content: space-between; align-items: start; margin-bottom: 0.5rem; }
            .teacher-conv-name { font-weight: 600; font-size: 0.95rem; color: #1f2937; }
            .teacher-conv-time { font-size: 0.75rem; color: #9ca3af; }
            .teacher-conv-preview { font-size: 0.85rem; color: #6b7280; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
            .teacher-conv-empty { padding: 3rem; text-align: center; color: #9ca3af; }
            
            .teacher-msg-thread { flex: 1; overflow-y: auto; padding: 1.5rem; display: flex; flex-direction: column; gap: 1rem; max-height: 450px; background: #f9fafb; }
            .teacher-msg-bubble { padding: 1rem; border-radius: 1rem; max-width: 75%; }
            .teacher-msg-bubble.admin { background: #fff; border: 1px solid #e5e7eb; align-self: flex-start; border-bottom-left-radius: 0.25rem; }
            .teacher-msg-bubble.user { background: #6366f1; color: #fff; align-self: flex-end; border-bottom-right-radius: 0.25rem; }
            .teacher-msg-bubble-header { display: flex; justify-content: space-between; margin-bottom: 0.5rem; font-size: 0.8rem; opacity: 0.8; }
            .teacher-msg-bubble-text { line-height: 1.5; }
            .teacher-msg-reply { padding: 1rem 1.5rem; border-top: 1px solid #e5e7eb; display: flex; gap: 0.75rem; background: #fff; }
            .teacher-msg-input { flex: 1; border: 1px solid #d1d5db; border-radius: 0.5rem; padding: 0.75rem; font-size: 0.95rem; resize: none; min-height: 60px; }
            .teacher-msg-send { background: #6366f1; color: #fff; border: none; border-radius: 0.5rem; padding: 0.75rem 1.5rem; cursor: pointer; font-weight: 600; }
            .teacher-msg-send:hover { background: #4f46e5; }
            .teacher-msg-send:disabled { background: #9ca3af; cursor: not-allowed; }
        `;
        document.head.appendChild(style);
    }

    injectHTML() {
        const html = `
            <button class="teacher-chat-btn" id="teacherChatBtn">
                <i class="fas fa-comments"></i>
                <span class="teacher-chat-badge" id="teacherChatBadge" style="display: none;">0</span>
            </button>
            <div class="teacher-chat-panel" id="teacherChatPanel">
                <div class="teacher-chat-header">
                    <h3 id="teacherChatTitle"><i class="fas fa-comments"></i> Messages</h3>
                    <button class="teacher-chat-close" id="teacherChatClose">&times;</button>
                </div>
                <div id="teacherChatContent"></div>
            </div>
        `;
        document.body.insertAdjacentHTML('beforeend', html);
    }

    attachEventListeners() {
        document.getElementById('teacherChatBtn').addEventListener('click', () => this.togglePanel());
        document.getElementById('teacherChatClose').addEventListener('click', () => this.closePanel());
    }

    togglePanel() {
        this.isOpen = !this.isOpen;
        const panel = document.getElementById('teacherChatPanel');
        panel.classList.toggle('active', this.isOpen);
        if (this.isOpen && this.conversations.length > 0) {
            this.openConversation(this.conversations[0].notification_id);
        }
    }

    closePanel() {
        this.isOpen = false;
        document.getElementById('teacherChatPanel').classList.remove('active');
        if (this.messagePollInterval) {
            clearInterval(this.messagePollInterval);
            this.messagePollInterval = null;
        }
    }

    async loadConversations() {
        const session = getCurrentSession();
        if (!session) return;

        try {
            const response = await fetch(`${API_BASE}/users/${encodeURIComponent(session.phone)}/notifications`);
            if (response.ok) {
                const notifications = await response.json();
                const oldUnreadCount = this.conversations.filter(c => !c.is_read).length;
                this.conversations = notifications;
                const unreadCount = this.conversations.filter(c => !c.is_read).length;
                
                if (unreadCount > oldUnreadCount) {
                    const btn = document.getElementById('teacherChatBtn');
                    btn.classList.add('has-new');
                    setTimeout(() => btn.classList.remove('has-new'), 500);
                }
                
                this.updateBadge();
                if (this.isOpen && this.currentConversation) {
                    this.loadMessageThread(this.currentConversation, true);
                }
            }
        } catch (error) {
            console.error('Failed to load conversations:', error);
        }
    }

    updateBadge() {
        const badge = document.getElementById('teacherChatBadge');
        const unreadCount = this.conversations.filter(c => !c.is_read).length;
        
        if (unreadCount > 0) {
            badge.textContent = unreadCount;
            badge.style.display = 'block';
        } else {
            badge.style.display = 'none';
        }
    }

    async openConversation(notificationId) {
        const conversation = this.conversations.find(c => c.id === notificationId);
        if (!conversation) return;

        this.currentConversation = notificationId;
        await this.markAsRead(notificationId);
        this.renderMessageView();
        await this.loadMessageThread(notificationId);
        
        if (this.messagePollInterval) clearInterval(this.messagePollInterval);
        this.messagePollInterval = setInterval(() => {
            if (this.isOpen && this.currentConversation) {
                this.loadMessageThread(this.currentConversation, true);
            }
        }, 3000);
    }

    renderMessageView() {
        const content = document.getElementById('teacherChatContent');
        content.innerHTML = `
            <div class="teacher-msg-thread" id="teacherMsgThread"></div>
            <div class="teacher-msg-reply">
                <textarea id="teacherMsgInput" class="teacher-msg-input" placeholder="Type your reply..."></textarea>
                <button id="teacherMsgSend" class="teacher-msg-send"><i class="fas fa-paper-plane"></i></button>
            </div>
        `;
        
        document.getElementById('teacherMsgSend').addEventListener('click', () => this.sendReply());
        document.getElementById('teacherMsgInput').addEventListener('keydown', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendReply();
            }
        });
    }

    async loadMessageThread(notificationId, silent = false) {
        const thread = document.getElementById('teacherMsgThread');
        if (!thread) return;
        
        const previousScrollHeight = thread.scrollHeight;
        const wasAtBottom = thread.scrollTop + thread.clientHeight >= previousScrollHeight - 50;

        try {
            const notif = this.conversations.find(c => c.id === notificationId);
            if (!notif) return;

            let html = `
                <div class="teacher-msg-bubble admin">
                    <div class="teacher-msg-bubble-header">
                        <strong>Admin</strong>
                        <span>${this.formatTime(notif.created_at)}</span>
                    </div>
                    <div class="teacher-msg-bubble-text">${notif.message}</div>
                </div>
            `;

            const repliesResponse = await fetch(`${API_BASE}/notifications/${notificationId}/replies`);
            if (repliesResponse.ok) {
                const replies = await repliesResponse.json();
                replies.forEach(reply => {
                    html += `
                        <div class="teacher-msg-bubble ${reply.sender === 'admin' ? 'admin' : 'user'}">
                            <div class="teacher-msg-bubble-header">
                                <strong>${reply.sender === 'admin' ? 'Admin' : 'You'}</strong>
                                <span>${this.formatTime(reply.created_at)}</span>
                            </div>
                            <div class="teacher-msg-bubble-text">${reply.message}</div>
                        </div>
                    `;
                });
            }

            thread.innerHTML = html;
            
            if (wasAtBottom || !silent) {
                thread.scrollTop = thread.scrollHeight;
            }
        } catch (error) {
            if (!silent) console.error('Failed to load thread:', error);
        }
    }

    async sendReply() {
        const input = document.getElementById('teacherMsgInput');
        const message = input.value.trim();
        if (!message || !this.currentConversation) return;

        const btn = document.getElementById('teacherMsgSend');
        btn.disabled = true;
        btn.innerHTML = '<i class="fas fa-circle-notch fa-spin"></i>';

        try {
            const session = getCurrentSession();
            const response = await fetch(`${API_BASE}/notifications/${this.currentConversation}/reply`, {
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
                await this.loadMessageThread(this.currentConversation);
            }
        } catch (error) {
            console.error('Failed to send reply:', error);
        } finally {
            btn.disabled = false;
            btn.innerHTML = '<i class="fas fa-paper-plane"></i>';
        }
    }

    async markAsRead(notificationId) {
        try {
            await fetch(`${API_BASE}/notifications/${notificationId}/read`, {
                method: 'PUT',
                headers: { 'Content-Type': 'application/json' }
            });
            const notif = this.conversations.find(c => c.id === notificationId);
            if (notif) notif.is_read = true;
            this.updateBadge();
        } catch (error) {
            console.error('Failed to mark as read:', error);
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

document.addEventListener('DOMContentLoaded', () => {
    const session = typeof getCurrentSession === 'function' ? getCurrentSession() : null;
    if (session && session.role !== 'admin') {
        new TeacherChatSystem();
    }
});
