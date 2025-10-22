// Simple user identification system without login
const USER_KEY = 'rtb_user_profile';

function generateUserId() {
    return 'USER_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
}

function getUserProfile() {
    const data = localStorage.getItem(USER_KEY);
    return data ? JSON.parse(data) : null;
}

function saveUserProfile(profile) {
    localStorage.setItem(USER_KEY, JSON.stringify(profile));
}

function isUserRegistered() {
    return getUserProfile() !== null;
}

function showRegistrationModal() {
    if (isUserRegistered()) return;
    
    const modal = document.createElement('div');
    modal.id = 'registrationModal';
    modal.style.cssText = 'position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.9); display: flex; align-items: center; justify-content: center; z-index: 99999;';
    modal.innerHTML = `
        <div style="background: white; padding: 3rem; border-radius: 1rem; max-width: 500px; width: 90%;">
            <h2 style="color: #1e293b; margin-bottom: 0.5rem; text-align: center;">
                <i class="fas fa-user-circle" style="color: #6366f1;"></i> Welcome!
            </h2>
            <p style="color: #64748b; margin-bottom: 2rem; text-align: center; font-size: 0.95rem;">
                Please provide your contact information to continue
            </p>
            
            <form id="registrationForm" style="display: flex; flex-direction: column; gap: 1rem;">
                <div>
                    <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #334155; font-size: 0.875rem;">
                        <i class="fas fa-user"></i> Full Name *
                    </label>
                    <input type="text" id="userName" required style="width: 100%; padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 0.5rem; font-size: 1rem;" placeholder="e.g., John Doe">
                </div>
                
                <div>
                    <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #334155; font-size: 0.875rem;">
                        <i class="fas fa-phone"></i> Phone Number *
                    </label>
                    <input type="tel" id="userPhone" required style="width: 100%; padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 0.5rem; font-size: 1rem;" placeholder="e.g., +250789123456">
                </div>
                
                <div>
                    <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #334155; font-size: 0.875rem;">
                        <i class="fas fa-envelope"></i> Email (Optional)
                    </label>
                    <input type="email" id="userEmail" style="width: 100%; padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 0.5rem; font-size: 1rem;" placeholder="e.g., teacher@school.rw">
                </div>
                
                <div>
                    <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #334155; font-size: 0.875rem;">
                        <i class="fas fa-school"></i> Institution *
                    </label>
                    <input type="text" id="userInstitution" required style="width: 100%; padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 0.5rem; font-size: 1rem;" placeholder="e.g., IPRC Kigali">
                </div>
                
                <div style="background: #dbeafe; padding: 1rem; border-radius: 0.5rem; font-size: 0.875rem; color: #1e40af;">
                    <i class="fas fa-info-circle"></i> Your information helps us provide better support and send payment confirmations.
                </div>
                
                <button type="submit" style="padding: 1rem; background: linear-gradient(135deg, #6366f1, #4f46e5); color: white; border: none; border-radius: 0.5rem; font-size: 1rem; font-weight: 600; cursor: pointer; margin-top: 0.5rem;">
                    <i class="fas fa-check-circle"></i> Continue to RTB Planner
                </button>
            </form>
        </div>
    `;
    
    document.body.appendChild(modal);
    
    document.getElementById('registrationForm').addEventListener('submit', (e) => {
        e.preventDefault();
        
        const profile = {
            userId: generateUserId(),
            name: document.getElementById('userName').value.trim(),
            phone: document.getElementById('userPhone').value.trim(),
            email: document.getElementById('userEmail').value.trim() || 'Not provided',
            institution: document.getElementById('userInstitution').value.trim(),
            registeredAt: new Date().toISOString()
        };
        
        saveUserProfile(profile);
        
        // Save to admin's user list
        saveToUserList(profile);
        
        modal.remove();
        
        // Show welcome notification
        if (typeof sendUserNotification === 'function') {
            sendUserNotification(
                'Welcome to RTB Planner! 🎉',
                `Hello ${profile.name}!\n\nYou have 2 free session plans and 2 free schemes to get started.\n\nNeed more? Contact us on WhatsApp: +250789751597`
            );
        }
    });
}

function saveToUserList(profile) {
    const USERS_LIST_KEY = 'rtb_all_users';
    let users = localStorage.getItem(USERS_LIST_KEY);
    users = users ? JSON.parse(users) : [];
    users.push(profile);
    localStorage.setItem(USERS_LIST_KEY, JSON.stringify(users));
}

// These functions are now in auth.js for consistency
// Keeping stubs for backward compatibility
if (typeof getAllRegisteredUsers === 'undefined') {
    function getAllRegisteredUsers() {
        const USERS_LIST_KEY = 'rtb_all_users';
        const users = localStorage.getItem(USERS_LIST_KEY);
        return users ? JSON.parse(users) : [];
    }
}

if (typeof getUserByPhone === 'undefined') {
    function getUserByPhone(phone) {
        const users = getAllRegisteredUsers();
        return users.find(u => u.phone === phone);
    }
}

if (typeof getUserById === 'undefined') {
    function getUserById(userId) {
        const users = getAllRegisteredUsers();
        return users.find(u => u.userId === userId);
    }
}

// Auto-show registration on first visit (disabled - using login system now)
// Registration modal removed in favor of proper login/register pages
