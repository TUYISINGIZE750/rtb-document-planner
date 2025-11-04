// Stable Real-time Chat Widget
class ChatWidget {
    constructor(userType) {
        this.userType = userType; // 'teacher' or 'admin'
        this.isOpen = false;
        this.activeChat = null;
        this.messages = {};
        this.lastUpdate = {};
        this.init();
    }

    init() {
        this.injectCSS();
        this.injectHTML();
        this.bindEvents();
        this.startPolling();
    }

    injectCSS() {
        const css = `
            .chat-widget-btn{position:fixed;bottom:20px;right:20px;width:60px;height:60px;background:linear-gradient(135deg,#6366f1,#4f46e5);color:#fff;border:none;border-radius:50%;cursor:pointer;box-shadow:0 8px 24px rgba(99,102,241,0.4);z-index:9998;font-size:1.5rem;transition:transform 0.2s}
            .chat-widget-btn:hover{transform:scale(1.05)}
            .chat-widget-badge{position:absolute;top:-5px;right:-5px;background:#ef4444;color:#fff;border-radius:50%;width:24px;height:24px;font-size:0.7rem;font-weight:700;display:none;align-items:center;justify-content:center}
            .chat-widget-badge.show{display:flex}
            .chat-widget-window{position:fixed;bottom:90px;right:20px;width:400px;height:550px;background:#fff;border-radius:12px;box-shadow:0 20px 60px rgba(0,0,0,0.3);z-index:9999;display:none;flex-direction:column}
            .chat-widget-window.open{display:flex}
            .chat-widget-header{padding:16px;background:linear-gradient(135deg,#6366f1,#4f46e5);color:#fff;border-radius:12px 12px 0 0;display:flex;justify-content:space-between;align-items:center}
            .chat-widget-header h3{margin:0;font-size:1rem;font-weight:600}
            .chat-widget-close{background:rgba(255,255,255,0.2);border:none;color:#fff;border-radius:50%;width:28px;height:28px;cursor:pointer;font-size:1.2rem;line-height:1}
            .chat-widget-messages{flex:1;overflow-y:auto;padding:16px;background:#f9fafb;display:flex;flex-direction:column;gap:12px}
            .chat-msg{padding:10px 14px;border-radius:12px;max-width:75%;word-wrap:break-word}
            .chat-msg.admin{background:#fff;border:1px solid #e5e7eb;align-self:flex-start}
            .chat-msg.user{background:#6366f1;color:#fff;align-self:flex-end}
            .chat-msg-time{font-size:0.7rem;opacity:0.7;margin-top:4px}
            .chat-widget-input{padding:12px;border-top:1px solid #e5e7eb;display:flex;gap:8px;background:#fff;border-radius:0 0 12px 12px}
            .chat-widget-input textarea{flex:1;border:1px solid #d1d5db;border-radius:8px;padding:8px;font-size:0.9rem;resize:none;height:40px;font-family:inherit}
            .chat-widget-input button{background:#6366f1;color:#fff;border:none;border-radius:8px;padding:8px 16px;cursor:pointer;font-weight:600}
            .chat-widget-input button:disabled{background:#9ca3af;cursor:not-allowed}
            .chat-empty{text-align:center;color:#9ca3af;padding:40px 20px}
        `;
        const style = document.createElement('style');
        style.textContent = css;
        document.head.appendChild(style);
    }

    injectHTML() {
        const html = `
            <button class="chat-widget-btn" id="chatWidgetBtn">
                <i class="fas fa-comments"></i>
                <span class="chat-widget-badge" id="chatWidgetBadge">0</span>
            </button>
            <div class="chat-widget-window" id="chatWidgetWindow">
                <div class="chat-widget-header">
                    <h3 id="chatWidgetTitle">Messages</h3>
                    <button class="chat-widget-close" id="chatWidgetClose">&times;</button>
                </div>
                <div class="chat-widget-messages" id="chatWidgetMessages"></div>
                <div class="chat-widget-input">
                    <textarea id="chatWidgetInput" placeholder="Type message..."></textarea>
                    <button id="chatWidgetSend">Send</button>
                </div>
            </div>
        `;
        document.body.insertAdjacentHTML('beforeend', html);
    }

    bindEvents() {
        document.getElementById('chatWidgetBtn').onclick = () => this.toggle();
        document.getElementById('chatWidgetClose').onclick = () => this.close();
        document.getElementById('chatWidgetSend').onclick = () => this.send();
        document.getElementById('chatWidgetInput').onkeydown = (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.send();
            }
        };
    }

    toggle() {
        this.isOpen = !this.isOpen;
        document.getElementById('chatWidgetWindow').classList.toggle('open', this.isOpen);
        if (this.isOpen) this.loadChat();
    }

    close() {
        this.isOpen = false;
        document.getElementById('chatWidgetWindow').classList.remove('open');
    }

    async loadChat() {
        const session = getCurrentSession();
        if (!session) return;

        try {
            const url = this.userType === 'admin' 
                ? `${API_BASE}/admin/conversations`
                : `${API_BASE}/users/${encodeURIComponent(session.phone)}/notifications`;
            
            const res = await fetch(url);
            if (!res.ok) return;
            
            const data = await res.json();
            
            if (this.userType === 'admin') {
                if (data.length > 0) {
                    this.activeChat = data[0].notification_id;
                    await this.loadMessages();
                }
            } else {
                if (data.length > 0) {
                    this.activeChat = data[0].id;
                    await this.loadMessages();
                    await this.markRead(this.activeChat);
                }
            }
        } catch (err) {
            console.error('Load chat error:', err);
        }
    }

    async loadMessages() {
        if (!this.activeChat) return;

        try {
            const [notifRes, repliesRes] = await Promise.all([
                fetch(`${API_BASE}/notifications/${this.activeChat}`),
                fetch(`${API_BASE}/notifications/${this.activeChat}/replies`)
            ]);

            if (!notifRes.ok || !repliesRes.ok) return;

            const notif = await notifRes.json();
            const replies = await repliesRes.json();

            const msgs = [
                { sender: 'admin', message: notif.message, created_at: notif.created_at },
                ...replies
            ];

            this.renderMessages(msgs);
        } catch (err) {
            console.error('Load messages error:', err);
        }
    }

    renderMessages(msgs) {
        const container = document.getElementById('chatWidgetMessages');
        const wasAtBottom = container.scrollHeight - container.scrollTop <= container.clientHeight + 50;

        container.innerHTML = msgs.map(m => {
            const isAdmin = m.sender === 'admin';
            const label = this.userType === 'admin' ? (isAdmin ? 'You' : 'Teacher') : (isAdmin ? 'Admin' : 'You');
            return `
                <div class="chat-msg ${m.sender}">
                    <div>${m.message}</div>
                    <div class="chat-msg-time">${label} • ${this.formatTime(m.created_at)}</div>
                </div>
            `;
        }).join('');

        if (wasAtBottom) container.scrollTop = container.scrollHeight;
    }

    async send() {
        const input = document.getElementById('chatWidgetInput');
        const btn = document.getElementById('chatWidgetSend');
        const msg = input.value.trim();
        
        if (!msg || !this.activeChat) return;

        btn.disabled = true;
        
        try {
            const session = getCurrentSession();
            const res = await fetch(`${API_BASE}/notifications/${this.activeChat}/reply`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({
                    message: msg,
                    sender: this.userType === 'admin' ? 'admin' : 'user',
                    sender_phone: this.userType === 'admin' ? 'admin' : session.phone
                })
            });

            if (res.ok) {
                input.value = '';
                await this.loadMessages();
            }
        } catch (err) {
            console.error('Send error:', err);
        } finally {
            btn.disabled = false;
        }
    }

    async markRead(id) {
        try {
            await fetch(`${API_BASE}/notifications/${id}/read`, { method: 'PUT' });
        } catch (err) {}
    }

    async updateBadge() {
        const session = getCurrentSession();
        if (!session) return;

        try {
            const url = this.userType === 'admin'
                ? `${API_BASE}/admin/conversations`
                : `${API_BASE}/users/${encodeURIComponent(session.phone)}/notifications`;
            
            const res = await fetch(url);
            if (!res.ok) return;
            
            const data = await res.json();
            const unread = this.userType === 'admin'
                ? data.filter(c => c.has_unread).length
                : data.filter(n => !n.is_read).length;
            
            const badge = document.getElementById('chatWidgetBadge');
            badge.textContent = unread;
            badge.classList.toggle('show', unread > 0);
        } catch (err) {}
    }

    startPolling() {
        this.updateBadge();
        setInterval(() => this.updateBadge(), 5000);
        setInterval(() => {
            if (this.isOpen && this.activeChat) this.loadMessages();
        }, 3000);
    }

    formatTime(ts) {
        if (!ts) return '';
        const d = new Date(ts);
        const diff = Date.now() - d;
        const m = Math.floor(diff / 60000);
        if (m < 1) return 'now';
        if (m < 60) return m + 'm';
        const h = Math.floor(m / 60);
        if (h < 24) return h + 'h';
        return Math.floor(h / 24) + 'd';
    }
}

// Auto-init
document.addEventListener('DOMContentLoaded', () => {
    const session = getCurrentSession?.();
    if (session) {
        new ChatWidget(session.role === 'admin' ? 'admin' : 'teacher');
    }
});
