// Subscription Modal System
let subscriptionModal = null;
let currentSettings = null;

// Load system settings
async function loadSystemSettings() {
    try {
        const response = await fetch(`${API_BASE}/settings`);
        if (response.ok) {
            currentSettings = await response.json();
            return currentSettings;
        }
    } catch (error) {
        console.error('Error loading settings:', error);
    }
    return null;
}

// Show subscription modal
async function showSubscriptionModal(type = 'both') {
    const settings = await loadSystemSettings();
    if (!settings) return;

    // Create modal if it doesn't exist
    if (!subscriptionModal) {
        subscriptionModal = document.createElement('div');
        subscriptionModal.className = 'subscription-modal-overlay';
        document.body.appendChild(subscriptionModal);
    }

    subscriptionModal.innerHTML = `
        <div class="subscription-modal">
            <div class="modal-header">
                <h2><i class="fas fa-crown"></i> Choose Your Plan</h2>
                <button class="close-btn" onclick="closeSubscriptionModal()">
                    <i class="fas fa-times"></i>
                </button>
            </div>
            
            <div class="modal-content">
                <div class="upgrade-message">
                    <i class="fas fa-info-circle"></i>
                    <p>You've reached your free download limit. Choose a subscription to continue creating professional RTB documents.</p>
                </div>
                
                <div class="subscription-plans" style="grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
                    <div class="plan-card" onclick="selectPlan('per_session', 36)">
                        <div class="plan-header">
                            <i class="fas fa-file-alt"></i>
                            <h3>Per Session Plan</h3>
                        </div>
                        <div class="plan-price">36 RWF</div>
                        <div class="plan-features">
                            <div class="feature"><i class="fas fa-check"></i> 1 Session Plan</div>
                            <div class="feature"><i class="fas fa-check"></i> RTB Format</div>
                        </div>
                        <button class="select-plan-btn">Select</button>
                    </div>
                    
                    <div class="plan-card" onclick="selectPlan('per_scheme', 47)">
                        <div class="plan-header">
                            <i class="fas fa-clipboard-list"></i>
                            <h3>Per Scheme</h3>
                        </div>
                        <div class="plan-price">47 RWF</div>
                        <div class="plan-features">
                            <div class="feature"><i class="fas fa-check"></i> 1 Scheme of Work</div>
                            <div class="feature"><i class="fas fa-check"></i> Professional Format</div>
                        </div>
                        <button class="select-plan-btn">Select</button>
                    </div>
                    
                    <div class="plan-card" onclick="selectPlan('weekly_sessions', 474)">
                        <div class="plan-header">
                            <i class="fas fa-calendar-week"></i>
                            <h3>Weekly Sessions</h3>
                        </div>
                        <div class="plan-price">474 RWF</div>
                        <div class="plan-features">
                            <div class="feature"><i class="fas fa-check"></i> 15 Session Plans</div>
                            <div class="feature"><i class="fas fa-check"></i> 7 Days Access</div>
                        </div>
                        <button class="select-plan-btn">Select</button>
                    </div>
                    
                    <div class="plan-card" onclick="selectPlan('weekly_schemes', 526)">
                        <div class="plan-header">
                            <i class="fas fa-calendar-week"></i>
                            <h3>Weekly Schemes</h3>
                        </div>
                        <div class="plan-price">526 RWF</div>
                        <div class="plan-features">
                            <div class="feature"><i class="fas fa-check"></i> 10 Schemes of Work</div>
                            <div class="feature"><i class="fas fa-check"></i> 7 Days Access</div>
                        </div>
                        <button class="select-plan-btn">Select</button>
                    </div>
                    
                    <div class="plan-card" onclick="selectPlan('monthly_sessions', 1000)">
                        <div class="plan-header">
                            <i class="fas fa-calendar-alt"></i>
                            <h3>Monthly Sessions</h3>
                        </div>
                        <div class="plan-price">1,000 RWF</div>
                        <div class="plan-features">
                            <div class="feature"><i class="fas fa-check"></i> 50 Session Plans</div>
                            <div class="feature"><i class="fas fa-check"></i> 30 Days Access</div>
                        </div>
                        <button class="select-plan-btn">Select</button>
                    </div>
                    
                    <div class="plan-card" onclick="selectPlan('monthly_schemes', 1889)">
                        <div class="plan-header">
                            <i class="fas fa-calendar-alt"></i>
                            <h3>Monthly Schemes</h3>
                        </div>
                        <div class="plan-price">1,889 RWF</div>
                        <div class="plan-features">
                            <div class="feature"><i class="fas fa-check"></i> 20 Schemes of Work</div>
                            <div class="feature"><i class="fas fa-check"></i> 30 Days Access</div>
                        </div>
                        <button class="select-plan-btn">Select</button>
                    </div>
                    
                    <div class="plan-card premium" onclick="selectPlan('unlimited', 5200)">
                        <div class="plan-badge">BEST VALUE</div>
                        <div class="plan-header">
                            <i class="fas fa-infinity"></i>
                            <h3>School Year Unlimited</h3>
                        </div>
                        <div class="plan-price">5,200 RWF</div>
                        <div class="plan-features">
                            <div class="feature"><i class="fas fa-check"></i> Unlimited Session Plans</div>
                            <div class="feature"><i class="fas fa-check"></i> Unlimited Schemes</div>
                            <div class="feature"><i class="fas fa-check"></i> Online Support</div>
                            <div class="feature"><i class="fas fa-check"></i> Training & Bonuses</div>
                        </div>
                        <button class="select-plan-btn premium-btn">Select Premium</button>
                    </div>
                </div>
            </div>
        </div>
    `;

    subscriptionModal.style.display = 'flex';
    document.body.style.overflow = 'hidden';
}

// Select a plan and show payment instructions
function selectPlan(planType, price) {
    const planNames = {
        'per_session': 'Per Session Plan (1 Session)',
        'per_scheme': 'Per Scheme (1 Scheme of Work)',
        'weekly_sessions': 'Weekly Sessions (15 Session Plans)',
        'weekly_schemes': 'Weekly Schemes (10 Schemes of Work)',
        'monthly_sessions': 'Monthly Sessions (50 Session Plans)',
        'monthly_schemes': 'Monthly Schemes (20 Schemes of Work)',
        'unlimited': 'School Year Unlimited'
    };

    subscriptionModal.innerHTML = `
        <div class="subscription-modal">
            <div class="modal-header">
                <h2><i class="fas fa-credit-card"></i> Payment Instructions</h2>
                <button class="close-btn" onclick="closeSubscriptionModal()">
                    <i class="fas fa-times"></i>
                </button>
            </div>
            
            <div class="modal-content">
                <div class="selected-plan">
                    <h3><i class="fas fa-check-circle"></i> Selected Plan: ${planNames[planType]}</h3>
                    <div class="plan-price-large">${price.toLocaleString()} RWF</div>
                </div>
                
                <div class="payment-instructions">
                    <div class="payment-highlight">
                        <h3><i class="fas fa-mobile-alt"></i> Mobile Money Payment Details</h3>
                        <div class="payment-card">
                            <div class="payment-row">
                                <div class="payment-label"><i class="fas fa-phone"></i> Phone Number:</div>
                                <div class="payment-value">+250789751597</div>
                            </div>
                            <div class="payment-row">
                                <div class="payment-label"><i class="fas fa-user"></i> Account Name:</div>
                                <div class="payment-value">Leonard TUYISINGIZE</div>
                            </div>
                            <div class="payment-row">
                                <div class="payment-label"><i class="fas fa-money-bill-wave"></i> Amount to Send:</div>
                                <div class="payment-value amount">${price.toLocaleString()} RWF</div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="payment-step">
                        <div class="step-number">1</div>
                        <div class="step-content">
                            <h4>Send Payment via Mobile Money</h4>
                            <p>Use MTN Mobile Money, Airtel Money, or any mobile money service to send the exact amount above.</p>
                        </div>
                    </div>
                    
                    <div class="payment-step">
                        <div class="step-number">2</div>
                        <div class="step-content">
                            <h4>After Payment Confirmation</h4>
                            <p>Once you've sent the payment, click the "Refresh Account" button below to activate your subscription.</p>
                        </div>
                    </div>
                    
                    <div class="payment-step">
                        <div class="step-number">3</div>
                        <div class="step-content">
                            <h4>Start Creating Documents</h4>
                            <p>Your account will be upgraded immediately and you can start downloading unlimited documents.</p>
                        </div>
                    </div>
                </div>
                
                <div class="payment-actions">
                    <button class="refresh-btn" onclick="refreshAccount('${planType}')">
                        <i class="fas fa-sync-alt"></i> Refresh Account
                    </button>
                    <button class="back-btn" onclick="showSubscriptionModal()">
                        <i class="fas fa-arrow-left"></i> Back to Plans
                    </button>
                </div>
                
                <div class="payment-note">
                    <i class="fas fa-info-circle"></i>
                    <p><strong>Important:</strong> Send exactly <strong>${price.toLocaleString()} RWF</strong> to <strong>+250789751597</strong> (Leonard TUYISINGIZE). Your account will be activated by admin after payment confirmation.</p>
                </div>
                
                <div class="payment-warning">
                    <i class="fas fa-exclamation-triangle"></i>
                    <p><strong>Payment Instructions:</strong></p>
                    <ul>
                        <li>Send to: <strong>+250789751597</strong></li>
                        <li>Name: <strong>Leonard TUYISINGIZE</strong></li>
                        <li>Amount: <strong>${price.toLocaleString()} RWF</strong></li>
                        <li>Wait for admin activation after payment</li>
                    </ul>
                </div>
            </div>
        </div>
    `;
}

// Refresh account after payment
async function refreshAccount(planType) {
    const refreshBtn = document.querySelector('.refresh-btn');
    const originalText = refreshBtn.innerHTML;
    
    refreshBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Checking Payment...';
    refreshBtn.disabled = true;
    
    try {
        const session = getCurrentSession();
        if (!session) {
            throw new Error('No active session');
        }
        
        // Show pending message - admin will activate after receiving payment
        subscriptionModal.innerHTML = `
            <div class="subscription-modal">
                <div class="modal-header">
                    <h2><i class="fas fa-clock" style="color: #f59e0b;"></i> Payment Submitted</h2>
                </div>
                
                <div class="modal-content">
                    <div class="success-message">
                        <i class="fas fa-hourglass-half" style="color: #6366f1; font-size: 3rem;"></i>
                        <h3>Payment Confirmation Pending</h3>
                        <p>Your payment request has been submitted. An administrator will activate your premium account once payment is confirmed.</p>
                        <p style="margin-top: 1rem; font-size: 0.9rem; color: #64748b;">You will receive a notification when your account is upgraded.</p>
                    </div>
                    
                    <div class="success-actions">
                        <button class="continue-btn" onclick="closeSubscriptionModal();">
                            <i class="fas fa-arrow-right"></i> Continue
                        </button>
                    </div>
                </div>
            </div>
        `;
    } catch (error) {
        console.error('Error submitting payment:', error);
        refreshBtn.innerHTML = '<i class="fas fa-exclamation-triangle"></i> Submission Failed';
        refreshBtn.style.background = '#ef4444';
        
        setTimeout(() => {
            refreshBtn.innerHTML = originalText;
            refreshBtn.style.background = '';
            refreshBtn.disabled = false;
        }, 3000);
    }
}

// Close subscription modal
function closeSubscriptionModal() {
    if (subscriptionModal) {
        subscriptionModal.style.display = 'none';
        document.body.style.overflow = '';
    }
}

// Check if user has reached limits and show modal
async function checkDownloadLimits(type) {
    try {
        const session = getCurrentSession();
        if (!session) return false;
        
        const response = await fetch(`${API_BASE}/user-limits/${encodeURIComponent(session.phone)}`);
        if (response.ok) {
            const limits = await response.json();
            
            if (limits.is_premium) return true; // Premium users have unlimited access
            
            const sessionPlansRemaining = Math.max(0, limits.session_plans_limit - limits.session_plans_downloaded);
            const schemesRemaining = Math.max(0, limits.schemes_limit - limits.schemes_downloaded);
            
            if (type === 'session_plan' && sessionPlansRemaining === 0) {
                showSubscriptionModal('session_plans');
                return false;
            }
            
            if (type === 'scheme' && schemesRemaining === 0) {
                showSubscriptionModal('schemes');
                return false;
            }
            
            return true;
        }
    } catch (error) {
        console.error('Error checking limits:', error);
    }
    return true;
}