// RTB Document Planner - Authentication System (FIXED)
console.log('✅ auth-fixed.js loaded - Session enforcement enabled');

// Session management
function saveSession(userData) {
    const sessionData = {
        ...userData,
        loginTime: Date.now(),
        expiresAt: Date.now() + (24 * 60 * 60 * 1000) // 24 hours
    };
    localStorage.setItem('rtb_session', JSON.stringify(sessionData));
    console.log('✅ Session saved:', sessionData.phone);
}

function getCurrentSession() {
    try {
        const sessionStr = localStorage.getItem('rtb_session');
        if (!sessionStr) return null;
        
        const session = JSON.parse(sessionStr);
        
        // Check if session expired
        if (Date.now() > session.expiresAt) {
            localStorage.removeItem('rtb_session');
            console.log('❌ Session expired');
            return null;
        }
        
        return session;
    } catch (error) {
        console.error('Session error:', error);
        localStorage.removeItem('rtb_session');
        return null;
    }
}

function clearSession() {
    localStorage.removeItem('rtb_session');
    console.log('🔓 Session cleared');
}

function isLoggedIn() {
    const session = getCurrentSession();
    return session !== null;
}

function requireAuth() {
    if (!isLoggedIn()) {
        console.log('🚫 Authentication required - redirecting to login');
        showAuthModal();
        return false;
    }
    return true;
}

// Protect wizard and scheme pages - STRICT ENFORCEMENT
function protectPage() {
    const currentPage = window.location.pathname;
    const protectedPages = ['wizard.html', 'scheme-wizard.html'];
    
    if (protectedPages.some(page => currentPage.includes(page))) {
        const session = getCurrentSession();
        if (!session) {
            // Immediately redirect to home and show login
            window.location.replace('index.html');
            setTimeout(() => showAuthModal(), 500);
            return false;
        }
    }
    return true;
}

// Auth modal for login/register
function showAuthModal() {
    // Remove existing modal
    const existingModal = document.getElementById('authModal');
    if (existingModal) {
        existingModal.remove();
    }
    
    const modal = document.createElement('div');
    modal.id = 'authModal';
    modal.innerHTML = `
        <div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); z-index: 10000; display: flex; align-items: center; justify-content: center;">
            <div style="background: white; padding: 2rem; border-radius: 1rem; max-width: 400px; width: 90%; box-shadow: 0 20px 40px rgba(0,0,0,0.3);">
                <h2 style="margin: 0 0 1rem 0; color: #1e293b; text-align: center;">
                    <i class="fas fa-lock" style="color: #6366f1;"></i> Login Required
                </h2>
                <p style="color: #64748b; text-align: center; margin-bottom: 2rem;">
                    Please login to create and download documents
                </p>
                
                <div id="authTabs" style="display: flex; margin-bottom: 1.5rem; border-bottom: 2px solid #e2e8f0;">
                    <button onclick="showLoginForm()" id="loginTab" class="auth-tab active" style="flex: 1; padding: 0.75rem; border: none; background: none; cursor: pointer; font-weight: 600; color: #6366f1; border-bottom: 2px solid #6366f1;">
                        Login
                    </button>
                    <button onclick="showRegisterForm()" id="registerTab" class="auth-tab" style="flex: 1; padding: 0.75rem; border: none; background: none; cursor: pointer; font-weight: 600; color: #64748b;">
                        Register
                    </button>
                </div>
                
                <!-- Login Form -->
                <form id="loginForm" style="display: block;">
                    <div style="margin-bottom: 1rem;">
                        <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #334155;">Phone Number</label>
                        <input type="tel" id="loginPhone" placeholder="+250788123456" required style="width: 100%; padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 0.5rem; font-size: 1rem;">
                    </div>
                    <div style="margin-bottom: 1.5rem;">
                        <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #334155;">Password</label>
                        <input type="password" id="loginPassword" required style="width: 100%; padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 0.5rem; font-size: 1rem;">
                    </div>
                    <button type="submit" style="width: 100%; padding: 0.875rem; background: linear-gradient(135deg, #6366f1, #4f46e5); color: white; border: none; border-radius: 0.5rem; font-size: 1rem; font-weight: 600; cursor: pointer;">
                        <i class="fas fa-sign-in-alt"></i> Login
                    </button>
                </form>
                
                <!-- Register Form -->
                <form id="registerForm" style="display: none;">
                    <div style="margin-bottom: 1rem;">
                        <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #334155;">Full Name</label>
                        <input type="text" id="registerName" required style="width: 100%; padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 0.5rem; font-size: 1rem;">
                    </div>
                    <div style="margin-bottom: 1rem;">
                        <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #334155;">Phone Number</label>
                        <input type="tel" id="registerPhone" placeholder="+250788123456" required style="width: 100%; padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 0.5rem; font-size: 1rem;">
                    </div>
                    <div style="margin-bottom: 1rem;">
                        <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #334155;">Institution</label>
                        <input type="text" id="registerInstitution" style="width: 100%; padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 0.5rem; font-size: 1rem;">
                    </div>
                    <div style="margin-bottom: 1.5rem;">
                        <label style="display: block; margin-bottom: 0.5rem; font-weight: 600; color: #334155;">Password</label>
                        <input type="password" id="registerPassword" required style="width: 100%; padding: 0.75rem; border: 2px solid #e2e8f0; border-radius: 0.5rem; font-size: 1rem;">
                    </div>
                    <button type="submit" style="width: 100%; padding: 0.875rem; background: linear-gradient(135deg, #10b981, #059669); color: white; border: none; border-radius: 0.5rem; font-size: 1rem; font-weight: 600; cursor: pointer;">
                        <i class="fas fa-user-plus"></i> Register
                    </button>
                </form>
                
                <div style="text-align: center; margin-top: 1.5rem;">
                    <button onclick="closeAuthModal()" style="color: #64748b; background: none; border: none; cursor: pointer; text-decoration: underline;">
                        Cancel
                    </button>
                </div>
            </div>
        </div>
    `;
    
    document.body.appendChild(modal);
    
    // Add event listeners
    document.getElementById('loginForm').addEventListener('submit', handleLogin);
    document.getElementById('registerForm').addEventListener('submit', handleRegister);
}

function showLoginForm() {
    document.getElementById('loginForm').style.display = 'block';
    document.getElementById('registerForm').style.display = 'none';
    document.getElementById('loginTab').className = 'auth-tab active';
    document.getElementById('registerTab').className = 'auth-tab';
    document.getElementById('loginTab').style.color = '#6366f1';
    document.getElementById('loginTab').style.borderBottom = '2px solid #6366f1';
    document.getElementById('registerTab').style.color = '#64748b';
    document.getElementById('registerTab').style.borderBottom = 'none';
}

function showRegisterForm() {
    document.getElementById('loginForm').style.display = 'none';
    document.getElementById('registerForm').style.display = 'block';
    document.getElementById('loginTab').className = 'auth-tab';
    document.getElementById('registerTab').className = 'auth-tab active';
    document.getElementById('registerTab').style.color = '#6366f1';
    document.getElementById('registerTab').style.borderBottom = '2px solid #6366f1';
    document.getElementById('loginTab').style.color = '#64748b';
    document.getElementById('loginTab').style.borderBottom = 'none';
}

function closeAuthModal() {
    const modal = document.getElementById('authModal');
    if (modal) {
        modal.remove();
    }
    // Redirect to home if on protected page
    const currentPage = window.location.pathname;
    if (currentPage.includes('wizard') || currentPage.includes('scheme')) {
        window.location.href = 'index.html';
    }
}

async function handleLogin(event) {
    event.preventDefault();
    
    const phone = document.getElementById('loginPhone').value.trim();
    const password = document.getElementById('loginPassword').value;
    const submitBtn = event.target.querySelector('button[type="submit"]');
    
    if (!phone || !password) {
        showNotification('Please fill in all fields', 'error');
        return;
    }
    
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Logging in...';
    
    try {
        const response = await fetch(`${API_BASE}/users/login`, {
            method: 'POST',
            mode: 'cors',
            credentials: 'omit',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({ phone, password })
        });
        
        if (response.ok) {
            const userData = await response.json();
            saveSession(userData);
            closeAuthModal();
            showNotification(`Welcome back, ${userData.name}!`, 'success');
            
            // Update UI immediately without reload
            updateAuthUI();
            if (typeof updateUserInterface === 'function') {
                updateUserInterface();
            }
        } else {
            const error = await response.json();
            showNotification(error.detail || 'Login failed', 'error');
        }
    } catch (error) {
        console.error('Login error:', error);
        if (error.name === 'TypeError' && error.message.includes('fetch')) {
            showNotification('Backend not available. Please contact admin.', 'error');
        } else {
            showNotification('Connection error. Please try again.', 'error');
        }
    } finally {
        submitBtn.disabled = false;
        submitBtn.innerHTML = '<i class="fas fa-sign-in-alt"></i> Login';
    }
}

async function handleRegister(event) {
    event.preventDefault();
    
    const name = document.getElementById('registerName').value.trim();
    const phone = document.getElementById('registerPhone').value.trim();
    const institution = document.getElementById('registerInstitution').value.trim();
    const password = document.getElementById('registerPassword').value;
    const submitBtn = event.target.querySelector('button[type="submit"]');
    
    if (!name || !phone || !password) {
        showNotification('Please fill in required fields', 'error');
        return;
    }
    
    if (password.length < 6) {
        showNotification('Password must be at least 6 characters', 'error');
        return;
    }
    
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Registering...';
    
    try {
        const response = await fetch(`${API_BASE}/users/register`, {
            method: 'POST',
            mode: 'cors',
            credentials: 'omit',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({ name, phone, institution, password })
        });
        
        if (response.ok) {
            showNotification('Registration successful! Please login.', 'success');
            showLoginForm();
            document.getElementById('loginPhone').value = phone;
        } else {
            const error = await response.json();
            showNotification(error.detail || 'Registration failed', 'error');
        }
    } catch (error) {
        console.error('Registration error:', error);
        if (error.name === 'TypeError' && error.message.includes('fetch')) {
            showNotification('Backend not available. Please contact admin.', 'error');
        } else {
            showNotification('Connection error. Please try again.', 'error');
        }
    } finally {
        submitBtn.disabled = false;
        submitBtn.innerHTML = '<i class="fas fa-user-plus"></i> Register';
    }
}

// Logout function
function logoutUser() {
    clearSession();
    showNotification('Logged out successfully', 'success');
    setTimeout(() => {
        window.location.href = 'index.html';
    }, 1000);
}

// Update UI based on login status
function updateAuthUI() {
    const session = getCurrentSession();
    const authButtons = document.querySelectorAll('.auth-buttons');
    const userInfo = document.querySelectorAll('.user-info');
    
    if (session) {
        // User is logged in
        authButtons.forEach(el => el.style.display = 'none');
        userInfo.forEach(el => {
            el.style.display = 'block';
            el.innerHTML = `
                <span style="color: #6366f1; font-weight: 600;">
                    <i class="fas fa-user"></i> ${session.name}
                </span>
                <button onclick="logoutUser()" style="margin-left: 1rem; padding: 0.5rem 1rem; background: #ef4444; color: white; border: none; border-radius: 0.25rem; cursor: pointer;">
                    <i class="fas fa-sign-out-alt"></i> Logout
                </button>
            `;
        });
    } else {
        // User is not logged in
        authButtons.forEach(el => el.style.display = 'block');
        userInfo.forEach(el => el.style.display = 'none');
    }
}

// Enhanced download functions with proper authentication
async function checkDownloadLimits(type, id) {
    console.log('Checking limits for:', type, 'ID:', id);
    
    if (!id || id === 'undefined' || id === undefined) {
        showNotification('Error: Invalid document ID', 'error');
        return;
    }
    
    const session = getCurrentSession();
    if (!session) {
        showNotification('Please login to download documents', 'error');
        showAuthModal();
        return;
    }
    
    try {
        const response = await fetch(`${API_BASE}/user-limits/${encodeURIComponent(session.phone)}`, {
            method: 'GET',
            mode: 'cors',
            credentials: 'omit',
            headers: {
                'Accept': 'application/json'
            }
        });
        
        if (response.ok) {
            const limits = await response.json();
            
            if (type === 'session_plan') {
                if (limits.is_premium || limits.session_plans_remaining > 0) {
                    downloadSessionPlan(id);
                    if (!limits.is_premium) {
                        showNotification(`Download successful! ${limits.session_plans_remaining - 1} session plans remaining`, 'success');
                    }
                } else {
                    showNotification('Download limit reached. Upgrade to premium for unlimited downloads.', 'error');
                }
            } else if (type === 'scheme') {
                if (limits.is_premium || limits.schemes_remaining > 0) {
                    downloadScheme(id);
                    if (!limits.is_premium) {
                        showNotification(`Download successful! ${limits.schemes_remaining - 1} schemes remaining`, 'success');
                    }
                } else {
                    showNotification('Download limit reached. Upgrade to premium for unlimited downloads.', 'error');
                }
            }
        } else {
            showNotification('Error checking download limits', 'error');
        }
    } catch (error) {
        showNotification('Network error: ' + error.message, 'error');
    }
}

function downloadSessionPlan(id) {
    if (!id || id === 'undefined') {
        showNotification('Error: Invalid session plan ID', 'error');
        return;
    }
    
    const session = getCurrentSession();
    if (!session) {
        showNotification('Please login to download', 'error');
        return;
    }
    
    const phone = encodeURIComponent(session.phone);
    const link = document.createElement('a');
    link.href = `${API_BASE}/session-plans/${id}/download?phone=${phone}`;
    link.download = `session_plan_${id}.docx`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

function downloadScheme(id) {
    if (!id || id === 'undefined') {
        showNotification('Error: Invalid scheme ID', 'error');
        return;
    }
    
    const session = getCurrentSession();
    if (!session) {
        showNotification('Please login to download', 'error');
        return;
    }
    
    const phone = encodeURIComponent(session.phone);
    const link = document.createElement('a');
    link.href = `${API_BASE}/schemes/${id}/download?phone=${phone}`;
    link.download = `scheme_of_work_${id}.docx`;
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// Notification function
function showNotification(message, type = 'info') {
    const notification = document.createElement('div');
    notification.style.cssText = `
        position: fixed;
        top: 2rem;
        right: 2rem;
        padding: 1rem 1.5rem;
        border-radius: 0.5rem;
        color: white;
        font-weight: 500;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        z-index: 10001;
        transform: translateX(400px);
        transition: transform 0.3s;
        max-width: 400px;
    `;
    
    const colors = {
        success: 'linear-gradient(135deg, #10b981, #059669)',
        error: 'linear-gradient(135deg, #ef4444, #dc2626)',
        warning: 'linear-gradient(135deg, #f59e0b, #d97706)',
        info: 'linear-gradient(135deg, #6366f1, #4f46e5)'
    };
    
    const icons = {
        success: 'fas fa-check-circle',
        error: 'fas fa-exclamation-circle',
        warning: 'fas fa-exclamation-triangle',
        info: 'fas fa-info-circle'
    };
    
    notification.style.background = colors[type] || colors.info;
    notification.innerHTML = `<i class="${icons[type] || icons.info}"></i> ${message}`;
    
    document.body.appendChild(notification);
    
    setTimeout(() => notification.style.transform = 'translateX(0)', 100);
    setTimeout(() => {
        notification.style.transform = 'translateX(400px)';
        setTimeout(() => document.body.removeChild(notification), 300);
    }, 4000);
}

// Initialize auth system
document.addEventListener('DOMContentLoaded', function() {
    console.log('🔐 Auth system initialized');
    updateAuthUI();
    
    // Protect current page
    protectPage();
    
    // Update UI every 30 seconds to check session expiry
    setInterval(updateAuthUI, 30000);
});

// Export functions for global use
window.getCurrentSession = getCurrentSession;
window.requireAuth = requireAuth;
window.logoutUser = logoutUser;
window.checkDownloadLimits = checkDownloadLimits;
window.showNotification = showNotification;