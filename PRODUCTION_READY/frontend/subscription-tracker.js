// Subscription Tracking System
class SubscriptionTracker {
    constructor() {
        this.updateInterval = null;
        this.init();
    }

    init() {
        // Start tracking when page loads
        this.startTracking();
        
        // Update every 30 seconds
        this.updateInterval = setInterval(() => {
            this.updateSubscriptionStatus();
        }, 30000);
    }

    async startTracking() {
        const session = getCurrentSession();
        if (!session || session.role === 'admin') return;

        await this.updateSubscriptionStatus();
    }

    async updateSubscriptionStatus() {
        try {
            const session = getCurrentSession();
            if (!session) return;

            const response = await fetch(`${API_BASE}/user-limits/${encodeURIComponent(session.phone)}`);
            if (response.ok) {
                const limits = await response.json();
                this.displaySubscriptionBadge(limits);
                this.updateProgressBars(limits);
            }
        } catch (error) {
            console.error('Error updating subscription status:', error);
        }
    }

    displaySubscriptionBadge(limits) {
        // Create or update subscription badge in header
        let badge = document.getElementById('subscription-badge');
        if (!badge) {
            badge = document.createElement('div');
            badge.id = 'subscription-badge';
            badge.style.cssText = `
                position: fixed;
                top: 1rem;
                left: 1rem;
                z-index: 1000;
                padding: 0.5rem 1rem;
                border-radius: 2rem;
                font-size: 0.8rem;
                font-weight: 600;
                box-shadow: 0 2px 8px rgba(0,0,0,0.15);
                transition: all 0.3s;
            `;
            document.body.appendChild(badge);
        }

        if (limits.is_premium) {
            badge.innerHTML = `<i class="fas fa-crown"></i> Premium Active`;
            badge.style.background = 'linear-gradient(135deg, #10b981, #059669)';
            badge.style.color = 'white';
        } else {
            const sessionRemaining = Math.max(0, limits.session_plans_limit - limits.session_plans_downloaded);
            const schemeRemaining = Math.max(0, limits.schemes_limit - limits.schemes_downloaded);
            
            if (sessionRemaining === 0 && schemeRemaining === 0) {
                badge.innerHTML = `<i class="fas fa-exclamation-triangle"></i> Upgrade Needed`;
                badge.style.background = 'linear-gradient(135deg, #ef4444, #dc2626)';
                badge.style.color = 'white';
            } else {
                badge.innerHTML = `<i class="fas fa-user"></i> Free: ${sessionRemaining}/${schemeRemaining} left`;
                badge.style.background = 'linear-gradient(135deg, #6366f1, #4f46e5)';
                badge.style.color = 'white';
            }
        }
    }

    updateProgressBars(limits) {
        // Update existing progress bars if they exist
        const sessionProgress = document.querySelector('.status-item.session-plans .progress-fill');
        const schemeProgress = document.querySelector('.status-item.schemes .progress-fill');

        if (sessionProgress && !limits.is_premium) {
            const sessionUsed = limits.session_plans_downloaded;
            const sessionTotal = limits.session_plans_limit;
            const sessionPercent = sessionTotal > 0 ? (sessionUsed / sessionTotal) * 100 : 0;
            sessionProgress.style.width = `${100 - sessionPercent}%`;
        }

        if (schemeProgress && !limits.is_premium) {
            const schemeUsed = limits.schemes_downloaded;
            const schemeTotal = limits.schemes_limit;
            const schemePercent = schemeTotal > 0 ? (schemeUsed / schemeTotal) * 100 : 0;
            schemeProgress.style.width = `${100 - schemePercent}%`;
        }
    }

    showUpgradeNotification() {
        // Show upgrade notification
        const notification = document.createElement('div');
        notification.style.cssText = `
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: white;
            padding: 2rem;
            border-radius: 1rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            z-index: 10000;
            text-align: center;
            max-width: 400px;
        `;
        
        notification.innerHTML = `
            <h3 style="color: #ef4444; margin-bottom: 1rem;">
                <i class="fas fa-exclamation-triangle"></i> Upgrade Required
            </h3>
            <p style="margin-bottom: 1.5rem; color: #6b7280;">
                You've reached your download limit. Upgrade to continue creating professional RTB documents.
            </p>
            <button onclick="showSubscriptionModal(); this.parentElement.remove();" 
                    style="padding: 0.75rem 2rem; background: #ef4444; color: white; border: none; border-radius: 0.5rem; font-weight: 600; cursor: pointer;">
                <i class="fas fa-crown"></i> View Upgrade Plans
            </button>
            <button onclick="this.parentElement.remove();" 
                    style="margin-left: 1rem; padding: 0.75rem 1rem; background: #6b7280; color: white; border: none; border-radius: 0.5rem; cursor: pointer;">
                Later
            </button>
        `;
        
        document.body.appendChild(notification);
        
        // Auto-remove after 10 seconds
        setTimeout(() => {
            if (notification.parentElement) {
                notification.remove();
            }
        }, 10000);
    }

    destroy() {
        if (this.updateInterval) {
            clearInterval(this.updateInterval);
        }
        
        const badge = document.getElementById('subscription-badge');
        if (badge) {
            badge.remove();
        }
    }
}

// Initialize subscription tracker when page loads
let subscriptionTracker;
document.addEventListener('DOMContentLoaded', function() {
    subscriptionTracker = new SubscriptionTracker();
});

// Clean up when page unloads
window.addEventListener('beforeunload', function() {
    if (subscriptionTracker) {
        subscriptionTracker.destroy();
    }
});
