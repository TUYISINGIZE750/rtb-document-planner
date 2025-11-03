// Upgrade Modal Handler
function showUpgradeModal() {
    const modalHTML = `
        <div class="upgrade-modal-overlay" id="upgradeModalOverlay">
            <div class="upgrade-modal">
                <div class="upgrade-modal-header">
                    <button class="upgrade-modal-close" onclick="closeUpgradeModal()">×</button>
                    <h2><i class="fas fa-crown"></i> Upgrade to Premium</h2>
                    <p>Unlock unlimited access to all features</p>
                </div>
                
                <div class="upgrade-modal-body">
                    <div class="upgrade-plan-card">
                        <h3><i class="fas fa-file-alt"></i> Pay Per Document</h3>
                        <ul class="upgrade-features">
                            <li><i class="fas fa-check-circle"></i> 1 Session Plan = <strong>33 RWF</strong></li>
                            <li><i class="fas fa-check-circle"></i> 1 Scheme of Work = <strong>79 RWF</strong></li>
                        </ul>
                    </div>
                    
                    <div class="upgrade-plan-card">
                        <h3><i class="fas fa-calendar-week"></i> Weekly Bundles</h3>
                        <ul class="upgrade-features">
                            <li><i class="fas fa-check-circle"></i> 15 Session Plans = <strong>556 RWF</strong></li>
                            <li><i class="fas fa-check-circle"></i> 5 Schemes of Work = <strong>777 RWF</strong></li>
                        </ul>
                    </div>
                    
                    <div class="upgrade-plan-card">
                        <h3><i class="fas fa-calendar-alt"></i> Monthly Bundles</h3>
                        <ul class="upgrade-features">
                            <li><i class="fas fa-check-circle"></i> 30 Session Plans = <strong>1,109 RWF</strong></li>
                            <li><i class="fas fa-check-circle"></i> 15 Schemes of Work = <strong>2,300 RWF</strong></li>
                        </ul>
                    </div>
                    
                    <div class="upgrade-plan-card" style="border: 3px solid #10b981; background: linear-gradient(135deg, #f0fdf4, #dcfce7);">
                        <h3><i class="fas fa-crown"></i> Unlimited Access</h3>
                        <div class="upgrade-price">5,300 RWF <span>/ month</span></div>
                        <ul class="upgrade-features">
                            <li><i class="fas fa-check-circle"></i> Unlimited Session Plans</li>
                            <li><i class="fas fa-check-circle"></i> Unlimited Schemes of Work</li>
                            <li><i class="fas fa-check-circle"></i> Priority Support</li>
                            <li><i class="fas fa-check-circle"></i> All Future Features</li>
                        </ul>
                    </div>
                    
                    <div class="upgrade-instructions">
                        <h4><i class="fas fa-info-circle"></i> How to Purchase</h4>
                        <ol class="upgrade-steps">
                            <li>
                                <span class="upgrade-step-number">1</span>
                                <span>Choose your plan and send payment via <strong>MTN/Airtel Mobile Money</strong></span>
                            </li>
                            <li>
                                <span class="upgrade-step-number">2</span>
                                <span>Send to: <strong>+250 789 751 597</strong> (TUYISINGIZE Leonard)</span>
                            </li>
                            <li>
                                <span class="upgrade-step-number">3</span>
                                <span>Contact us with payment confirmation and your registered phone number</span>
                            </li>
                            <li>
                                <span class="upgrade-step-number">4</span>
                                <span>Your account will be activated within <strong>24 hours</strong></span>
                            </li>
                        </ol>
                    </div>
                    
                    <div class="upgrade-contact">
                        <h4><i class="fas fa-phone-alt"></i> Payment & Support Contact</h4>
                        <div class="upgrade-contact-info">
                            <div class="upgrade-contact-item">
                                <i class="fas fa-user"></i>
                                <strong>Name:</strong>
                                <span>TUYISINGIZE Leonard</span>
                            </div>
                            <div class="upgrade-contact-item">
                                <i class="fas fa-mobile-alt"></i>
                                <strong>MoMo:</strong>
                                <span>+250 789 751 597</span>
                            </div>
                            <div class="upgrade-contact-item">
                                <i class="fas fa-envelope"></i>
                                <strong>Email:</strong>
                                <span>leotuyi100@outlook.com</span>
                            </div>
                            <div class="upgrade-contact-item">
                                <i class="fas fa-money-bill-wave"></i>
                                <strong>Payment:</strong>
                                <span>MTN/Airtel Mobile Money</span>
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="upgrade-modal-footer">
                    <button class="upgrade-btn upgrade-btn-secondary" onclick="closeUpgradeModal()">
                        <i class="fas fa-times"></i> Close
                    </button>
                    <a href="tel:+250789751597" class="upgrade-btn upgrade-btn-primary">
                        <i class="fas fa-phone"></i> Call Now
                    </a>
                </div>
            </div>
        </div>
    `;
    
    // Remove existing modal if any
    const existingModal = document.getElementById('upgradeModalOverlay');
    if (existingModal) {
        existingModal.remove();
    }
    
    // Add modal to body
    document.body.insertAdjacentHTML('beforeend', modalHTML);
    
    // Show modal
    setTimeout(() => {
        document.getElementById('upgradeModalOverlay').classList.add('active');
    }, 10);
    
    // Close on overlay click
    document.getElementById('upgradeModalOverlay').addEventListener('click', function(e) {
        if (e.target === this) {
            closeUpgradeModal();
        }
    });
}

function closeUpgradeModal() {
    const modal = document.getElementById('upgradeModalOverlay');
    if (modal) {
        modal.classList.remove('active');
        setTimeout(() => {
            modal.remove();
        }, 300);
    }
}

// Close modal on Escape key
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape') {
        closeUpgradeModal();
    }
});
