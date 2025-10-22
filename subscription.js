// Simple subscription management using localStorage
const SUBSCRIPTION_KEY = 'rtb_subscription';
const FREE_SESSION_PLANS = 2;
const FREE_SCHEMES = 2;
const WHATSAPP_NUMBER = '+250789751597';

function getSubscriptionData() {
    const data = localStorage.getItem(SUBSCRIPTION_KEY);
    if (!data) {
        const initial = {
            sessionPlansDownloaded: 0,
            schemesDownloaded: 0,
            isPremium: false,
            premiumUntil: null
        };
        localStorage.setItem(SUBSCRIPTION_KEY, JSON.stringify(initial));
        return initial;
    }
    return JSON.parse(data);
}

function saveSubscriptionData(data) {
    localStorage.setItem(SUBSCRIPTION_KEY, JSON.stringify(data));
}



function recordSessionPlanDownload() {
    const data = getSubscriptionData();
    data.sessionPlansDownloaded++;
    saveSubscriptionData(data);
}

function recordSchemeDownload() {
    const data = getSubscriptionData();
    data.schemesDownloaded++;
    saveSubscriptionData(data);
}



function showPaymentModal() {
    const remaining = getRemainingDownloads();
    const modal = document.createElement('div');
    modal.style.cssText = 'position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.8); display: flex; align-items: center; justify-content: center; z-index: 9999; overflow-y: auto; padding: 2rem;';
    modal.innerHTML = `
        <div style="background: white; padding: 2.5rem; border-radius: 1rem; max-width: 600px; text-align: center; max-height: 90vh; overflow-y: auto;">
            <i class="fas fa-lock" style="font-size: 3rem; color: #6366f1; margin-bottom: 1rem;"></i>
            <h2 style="color: #1e293b; margin-bottom: 0.5rem; font-size: 1.75rem;">Free Downloads Used</h2>
            <p style="color: #64748b; margin-bottom: 2rem; font-size: 0.95rem;">Choose a package to continue generating documents</p>
            
            <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 1rem; margin-bottom: 2rem;">
                <div style="background: linear-gradient(135deg, #10b981, #059669); padding: 1.5rem; border-radius: 0.75rem; color: white; text-align: left;">
                    <div style="font-size: 1.75rem; font-weight: 700; margin-bottom: 0.5rem;">500 RWF</div>
                    <div style="opacity: 0.9; font-size: 0.875rem; margin-bottom: 1rem;">Starter Package</div>
                    <div style="font-size: 0.875rem;">✓ 10 Session Plans<br>✓ 5 Schemes of Work</div>
                </div>
                
                <div style="background: linear-gradient(135deg, #3b82f6, #2563eb); padding: 1.5rem; border-radius: 0.75rem; color: white; text-align: left;">
                    <div style="font-size: 1.75rem; font-weight: 700; margin-bottom: 0.5rem;">1,000 RWF</div>
                    <div style="opacity: 0.9; font-size: 0.875rem; margin-bottom: 1rem;">Basic Package</div>
                    <div style="font-size: 0.875rem;">✓ 20 Session Plans<br>✓ 10 Schemes of Work</div>
                </div>
                
                <div style="background: linear-gradient(135deg, #8b5cf6, #7c3aed); padding: 1.5rem; border-radius: 0.75rem; color: white; text-align: left;">
                    <div style="font-size: 1.75rem; font-weight: 700; margin-bottom: 0.5rem;">2,000 RWF</div>
                    <div style="opacity: 0.9; font-size: 0.875rem; margin-bottom: 1rem;">Pro Package</div>
                    <div style="font-size: 0.875rem;">✓ 50 Session Plans<br>✓ 20 Schemes of Work</div>
                </div>
                
                <div style="background: linear-gradient(135deg, #f59e0b, #d97706); padding: 1.5rem; border-radius: 0.75rem; color: white; text-align: left; position: relative; overflow: hidden;">
                    <div style="position: absolute; top: 0.5rem; right: 0.5rem; background: rgba(255,255,255,0.3); padding: 0.25rem 0.5rem; border-radius: 0.25rem; font-size: 0.75rem; font-weight: 600;">BEST VALUE</div>
                    <div style="font-size: 1.75rem; font-weight: 700; margin-bottom: 0.5rem;">5,000 RWF</div>
                    <div style="opacity: 0.9; font-size: 0.875rem; margin-bottom: 1rem;">Unlimited</div>
                    <div style="font-size: 0.875rem;">✓ Unlimited Session Plans<br>✓ Unlimited Schemes<br>✓ Priority Support</div>
                </div>
            </div>
            
            <div style="background: #dcfce7; padding: 1.5rem; border-radius: 0.75rem; margin-bottom: 1.5rem; border-left: 4px solid #10b981;">
                <p style="color: #166534; font-size: 0.95rem; margin: 0; font-weight: 600;">
                    <i class="fab fa-whatsapp" style="font-size: 1.5rem; vertical-align: middle;"></i> To Purchase:
                </p>
                <p style="color: #166534; font-size: 0.875rem; margin: 0.5rem 0 0 0;">
                    1. Send payment via MTN MoMo to <strong>250789751597</strong><br>
                    <span style="margin-left: 1.5rem; font-style: italic;">(Leonard TUYISINGIZE)</span><br>
                    2. Contact us on WhatsApp: <strong>+250789751597</strong><br>
                    3. Share your transaction ID<br>
                    4. Get instant activation!
                </p>
            </div>
            
            <div style="display: flex; flex-direction: column; gap: 1rem;">
                <a href="https://wa.me/250789751597?text=Hello,%20I%20want%20to%20purchase%20RTB%20Document%20Planner%20access" target="_blank" style="padding: 1rem; background: linear-gradient(135deg, #10b981, #059669); color: white; border: none; border-radius: 0.5rem; cursor: pointer; font-weight: 600; text-decoration: none; display: block; text-align: center;">
                    <i class="fab fa-whatsapp"></i> Contact on WhatsApp
                </a>
                <a href="https://wa.me/250789751597?text=Mwaramutse,%20nkeneye%20ubufasha%20kugura%20RTB%20Document%20Planner" target="_blank" style="padding: 1rem; background: linear-gradient(135deg, #3b82f6, #2563eb); color: white; border: none; border-radius: 0.5rem; cursor: pointer; font-weight: 600; text-decoration: none; display: block; text-align: center;">
                    <i class="fab fa-whatsapp"></i> Nyandikira / Chat With Me
                </a>
                <button onclick="this.parentElement.parentElement.parentElement.remove()" style="padding: 1rem; background: #e2e8f0; border: none; border-radius: 0.5rem; cursor: pointer; font-weight: 600; color: #334155;">
                    <i class="fas fa-times"></i> Cancel
                </button>
            </div>
        </div>
    `;
    document.body.appendChild(modal);
}

function activatePremium(sessionPlans, schemes) {
    const data = getSubscriptionData();
    if (sessionPlans === 'unlimited') {
        data.isPremium = true;
        data.premiumUntil = new Date(Date.now() + 30 * 24 * 60 * 60 * 1000).toISOString();
    } else {
        data.sessionPlansLimit = (data.sessionPlansLimit || 0) + parseInt(sessionPlans);
        data.schemesLimit = (data.schemesLimit || 0) + parseInt(schemes);
    }
    saveSubscriptionData(data);
    return true;
}

function canDownloadSessionPlan() {
    const data = getSubscriptionData();
    if (data.isPremium) return true;
    if (data.sessionPlansLimit && data.sessionPlansDownloaded < data.sessionPlansLimit) return true;
    return data.sessionPlansDownloaded < FREE_SESSION_PLANS;
}

function canDownloadScheme() {
    const data = getSubscriptionData();
    if (data.isPremium) return true;
    if (data.schemesLimit && data.schemesDownloaded < data.schemesLimit) return true;
    return data.schemesDownloaded < FREE_SCHEMES;
}

function getRemainingDownloads() {
    const data = getSubscriptionData();
    if (data.isPremium) {
        return { sessionPlans: 'Unlimited', schemes: 'Unlimited', isPremium: true };
    }
    const sessionLimit = data.sessionPlansLimit || FREE_SESSION_PLANS;
    const schemeLimit = data.schemesLimit || FREE_SCHEMES;
    return {
        sessionPlans: Math.max(0, sessionLimit - data.sessionPlansDownloaded),
        schemes: Math.max(0, schemeLimit - data.schemesDownloaded),
        isPremium: false
    };
}
