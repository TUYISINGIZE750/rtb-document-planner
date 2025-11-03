// Developer Modal Handler
function showDeveloperModal() {
    const modalHTML = `
        <div class="developer-modal-overlay" id="developerModalOverlay">
            <div class="developer-modal">
                <div class="developer-modal-header">
                    <button class="developer-modal-close" onclick="closeDeveloperModal()">×</button>
                    <div class="developer-avatar">
                        <i class="fas fa-user-tie"></i>
                    </div>
                    <h2>Leonard TUYISINGIZE</h2>
                    <p>Full-Stack Software Developer</p>
                </div>
                
                <div class="developer-modal-body">
                    <div class="developer-bio">
                        <h4><i class="fas fa-info-circle"></i> About Me</h4>
                        <p>
                            I'm a passionate software developer with <strong>5 years of experience</strong> 
                            building innovative solutions. I specialize in creating custom software, 
                            programs, and applications for companies and individuals. Whether you need 
                            a business management system, educational platform, or any custom software 
                            solution, I'm here to help bring your ideas to life.
                        </p>
                    </div>
                    
                    <div class="developer-info-card">
                        <div class="developer-info-item">
                            <i class="fas fa-user"></i>
                            <strong>Name:</strong>
                            <span>Leonard TUYISINGIZE</span>
                        </div>
                        <div class="developer-info-item">
                            <i class="fas fa-mobile-alt"></i>
                            <strong>Phone:</strong>
                            <span>+250 789 751 597</span>
                        </div>
                        <div class="developer-info-item">
                            <i class="fas fa-envelope"></i>
                            <strong>Email:</strong>
                            <span>leotuyi100@outlook.com</span>
                        </div>
                        <div class="developer-info-item">
                            <i class="fas fa-briefcase"></i>
                            <strong>Experience:</strong>
                            <span>5+ Years</span>
                        </div>
                        <div class="developer-info-item">
                            <i class="fas fa-code"></i>
                            <strong>Specialization:</strong>
                            <span>Full-Stack Development</span>
                        </div>
                    </div>
                    
                    <div class="developer-cta">
                        <h4><i class="fas fa-handshake"></i> Business Inquiries</h4>
                        <p>Need a custom software solution? Don't hesitate to reach out!</p>
                        <p style="font-size: 0.875rem; opacity: 0.9;">
                            I build all kinds of software and programs for companies and individuals. 
                            Let's discuss your project and turn your vision into reality.
                        </p>
                    </div>
                </div>
                
                <div class="developer-modal-footer">
                    <a href="tel:+250789751597" class="developer-btn developer-btn-success">
                        <i class="fas fa-phone"></i> Call Now
                    </a>
                    <a href="mailto:leotuyi100@outlook.com" class="developer-btn developer-btn-primary">
                        <i class="fas fa-envelope"></i> Send Email
                    </a>
                </div>
            </div>
        </div>
    `;
    
    // Remove existing modal if any
    const existingModal = document.getElementById('developerModalOverlay');
    if (existingModal) {
        existingModal.remove();
    }
    
    // Add modal to body
    document.body.insertAdjacentHTML('beforeend', modalHTML);
    
    // Show modal
    setTimeout(() => {
        document.getElementById('developerModalOverlay').classList.add('active');
    }, 10);
    
    // Close on overlay click
    document.getElementById('developerModalOverlay').addEventListener('click', function(e) {
        if (e.target === this) {
            closeDeveloperModal();
        }
    });
}

function closeDeveloperModal() {
    const modal = document.getElementById('developerModalOverlay');
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
        closeDeveloperModal();
    }
});
