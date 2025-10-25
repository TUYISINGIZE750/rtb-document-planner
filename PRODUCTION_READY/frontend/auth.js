// Authentication system with admin role protection
console.log('✅ auth.js loaded successfully (v1.0.1-ts-20250120T105300Z-CACHE-BUSTED)');

// DEFENSIVE: Ensure config.js has loaded and API_BASE is defined
if (typeof API_BASE === 'undefined') {
    console.error('⚠️ CRITICAL: API_BASE is not defined! config.js may not have loaded.');
    console.error('This is a script loading order issue - config.js must load BEFORE auth.js');
    // Fallback API_BASE for production
    window.API_BASE = 'https://leonardus437.pythonanywhere.com';
    console.log('Using fallback API_BASE:', window.API_BASE);
}

const AUTH_KEY = 'rtb_auth_session';
const USERS_KEY = 'rtb_users_db';
const LOGOUT_FLAG_KEY = 'rtb_logged_out';
const SESSION_EXPIRY_COOKIE = 'rtb_session_expired';

// Default admin credentials
const DEFAULT_ADMIN = {
    phone: '+250789751597',
    password: 'admin123',
    name: 'Administrator',
    email: 'admin@rtb.rw',
    institution: 'RTB',
    role: 'admin'
};

// Initialize users database
function initUsersDB() {
    let users = localStorage.getItem(USERS_KEY);
    if (!users) {
        users = [DEFAULT_ADMIN];
        localStorage.setItem(USERS_KEY, JSON.stringify(users));
    }
}

// Register new user with robust connection
async function registerUser(name, phone, email, institution, password) {
    const userId = 'USER_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
    const userData = { user_id: userId, name, phone, email, institution, password, role: 'user' };
    
    // Ensure API_BASE is available (fallback safety)
    const apiBase = (typeof API_BASE !== 'undefined') ? API_BASE : (window.API_BASE || 'https://leonardus437.pythonanywhere.com');
    
    try {
        const response = await fetch(`${apiBase}/users/register`, {
            method: 'POST',
            mode: 'cors',
            credentials: 'omit',
            headers: { 
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify(userData)
        });
        
        if (!response.ok) {
            const errorText = await response.text();
            let errorMessage = 'Registration failed';
            try {
                const errorJson = JSON.parse(errorText);
                errorMessage = errorJson.detail || errorJson.message || 'Registration failed';
            } catch (e) {
                if (response.status === 400) {
                    errorMessage = 'Phone number already registered';
                }
            }
            return { success: false, message: errorMessage };
        }
        
        return { success: true };
    } catch (error) {
        console.error('Registration error:', error);
        return { success: false, message: 'Unable to connect to server. Please try again.' };
    }
}

// Login user with robust connection
async function loginUser(phone, password, remember) {
    // Ensure API_BASE is available
    const apiBase = (typeof API_BASE !== 'undefined') ? API_BASE : (window.API_BASE || 'https://leonardus437.pythonanywhere.com');
    
    console.log('🔐 Login attempt:', { phone, apiBase });
    
    try {
        // Clear any existing session data first
        clearSessionStorage();
        clearLogoutMarkers();
        clearLogoutFlag();
        
        console.log('📡 Sending login request...');
        const response = await fetch(`${apiBase}/users/login`, {
            method: 'POST',
            mode: 'cors',
            credentials: 'omit',
            headers: { 
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({ phone, password })
        });
        
        console.log('📥 Response status:', response.status);
        
        if (!response.ok) {
            const errorText = await response.text();
            console.error('❌ Login failed:', errorText);
            let errorMessage = 'Login failed';
            try {
                const errorJson = JSON.parse(errorText);
                errorMessage = errorJson.detail || errorJson.message || 'Incorrect phone number or password';
            } catch (e) {
                if (response.status === 401) {
                    errorMessage = 'Incorrect phone number or password';
                } else if (response.status === 404) {
                    errorMessage = 'User not found. Please register first.';
                }
            }
            return { success: false, message: errorMessage };
        }
        
        const result = await response.json();
        const user = result && result.user ? result.user : result;
        console.log('✅ User data received:', { ...user, password: '***' });
        
        const expiryTime = remember ? 30 * 24 * 60 * 60 * 1000 : 24 * 60 * 60 * 1000;
        const session = { 
            ...user, 
            loggedInAt: new Date().toISOString(),
            expiresAt: new Date(Date.now() + expiryTime).toISOString(),
            remember,
            sessionId: 'SESSION_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9)
        };
        
        localStorage.setItem(AUTH_KEY, JSON.stringify(session));
        console.log('💾 Session saved to localStorage');
        console.log('👤 User role:', user.role);
        
        clearLogoutFlag();
        return { success: true, role: user.role };
    } catch (error) {
        console.error('❌ Login error:', error);
        return { success: false, message: 'Unable to connect to server. Please try again.' };
    }
}

// Logout user
function clearSessionStorage() {
    localStorage.removeItem(AUTH_KEY);
    sessionStorage.removeItem(AUTH_KEY);
}

function setLogoutMarkers() {
    const logoutTime = Date.now().toString();
    localStorage.setItem(LOGOUT_FLAG_KEY, logoutTime);
    sessionStorage.setItem(LOGOUT_FLAG_KEY, logoutTime);
}

function clearLogoutMarkers() {
    localStorage.removeItem(LOGOUT_FLAG_KEY);
    sessionStorage.removeItem(LOGOUT_FLAG_KEY);
}

// Clear logout flag when user logs in successfully
function clearLogoutFlag() {
    clearLogoutMarkers();
}

function setSessionExpiredCookie() {
    document.cookie = `${SESSION_EXPIRY_COOKIE}=true;path=/;max-age=31536000`;
}

function hasSessionExpiredCookie() {
    return document.cookie.indexOf(`${SESSION_EXPIRY_COOKIE}=true`) !== -1;
}

function clearAllCookies() {
    document.cookie.split(";").forEach(function(cookie) {
        document.cookie = cookie.replace(/^ +/, "").replace(/=.*/, "=;expires=" + new Date().toUTCString() + ";path=/");
    });
}

async function validateSessionWithBackend() {
    try {
        const session = getCurrentSession();
        if (!session) return false;
        const response = await fetch(`${API_BASE}/users/${encodeURIComponent(session.phone)}`);
        if (!response.ok) {
            return false;
        }
        const user = await response.json();
        if (!user || user.phone !== session.phone) {
            return false;
        }
        return true;
    } catch (error) {
        console.warn('Session validation failed:', error);
        return false;
    }
}

function logoutUser() {
    // Get current session to determine redirect
    const session = getCurrentSession();
    const isAdmin = session && session.role === 'admin';
    
    // Clear ALL session data
    localStorage.removeItem(AUTH_KEY);
    sessionStorage.removeItem(AUTH_KEY);
    localStorage.clear(); // Clear everything
    sessionStorage.clear();
    
    // Set logout marker with timestamp
    const logoutTime = Date.now().toString();
    localStorage.setItem(LOGOUT_FLAG_KEY, logoutTime);
    sessionStorage.setItem(LOGOUT_FLAG_KEY, logoutTime);
    
    // Clear all cookies
    document.cookie.split(";").forEach(function(c) { 
        document.cookie = c.replace(/^ +/, "").replace(/=.*/, "=;expires=" + new Date().toUTCString() + ";path=/"); 
    });
    
    // Manipulate history to prevent back button access
    window.history.pushState(null, null, window.location.href);
    window.history.pushState(null, null, window.location.href);
    window.history.go(1);
    
    // Redirect based on role
    const redirectPage = isAdmin ? 'login.html' : 'login.html';
    window.location.replace(redirectPage);
}

function destroyStaleSession() {
    clearSessionStorage();
    clearLogoutMarkers();
    setSessionExpiredCookie();
}

async function ensureSessionValidity() {
    const valid = await isLoggedIn();
    if (!valid) {
        window.location.replace('direct-login.html');
    }
    return valid;
}

function wasExplicitlyLoggedOut() {
    return Boolean(localStorage.getItem(LOGOUT_FLAG_KEY) || sessionStorage.getItem(LOGOUT_FLAG_KEY));
}

// Enhanced back button prevention for teachers
function preventBackAfterLogout() {
    if (wasExplicitlyLoggedOut()) {
        window.history.pushState(null, null, window.location.href);
        window.location.replace('login.html');
        return true;
    }
    return false;
}

// Set up global back button prevention
if (typeof window !== 'undefined') {
    window.addEventListener('popstate', function() {
        if (preventBackAfterLogout()) {
            return;
        }
    });
    
    window.addEventListener('pageshow', function(event) {
        if (event.persisted && wasExplicitlyLoggedOut()) {
            window.location.replace('login.html');
        }
    });
}

async function shouldInvalidateSession(sessionData) {
    if (!sessionData) {
        return true;
    }

    if (hasSessionExpiredCookie()) {
        return true;
    }

    if (wasExplicitlyLoggedOut()) {
        return true;
    }

    if (sessionData.expiresAt) {
        const expiryDate = new Date(sessionData.expiresAt);
        if (expiryDate < new Date()) {
            return true;
        }
    }

    const loggedInAt = new Date(sessionData.loggedInAt || 0);
    const currentTime = new Date();
    const sessionAgeHours = (currentTime - loggedInAt) / (1000 * 60 * 60);
    if (sessionAgeHours > 24) {
        return true;
    }

    const backendValid = await validateSessionWithBackend();
    if (!backendValid) {
        return true;
    }

    return false;
}

function isLoggedIn() {
    // Check for explicit logout markers first
    if (wasExplicitlyLoggedOut()) {
        return false;
    }
    
    const session = getCurrentSession();
    return session !== null;
}

// Get current session
function getCurrentSession() {
    try {
        const session = localStorage.getItem(AUTH_KEY);
        return session ? JSON.parse(session) : null;
    } catch (e) {
        return null;
    }
}

// Check if user is admin
function isAdmin() {
    const session = getCurrentSession();
    return session && session.role === 'admin';
}

// Protect admin pages
function protectAdminPage() {
    // Add cache control meta tags
    const metaTags = [
        '<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">',
        '<meta http-equiv="Pragma" content="no-cache">',
        '<meta http-equiv="Expires" content="0">'
    ];
    
    metaTags.forEach(tag => {
        if (!document.head.innerHTML.includes(tag)) {
            document.head.innerHTML += tag;
        }
    });
    
    // Disable browser back/forward cache
    window.onpageshow = function(event) {
        if (event.persisted || wasExplicitlyLoggedOut()) {
            window.location.replace('direct-login.html');
        }
    };
    
    // Prevent caching and handle back button
    if (window.history && window.history.pushState) {
        window.history.pushState(null, null, window.location.href);
        
        window.onpopstate = async function() {
            window.history.pushState(null, null, window.location.href);
            
            const loggedIn = await isLoggedIn();
            if (!loggedIn || wasExplicitlyLoggedOut()) {
                window.location.replace('direct-login.html');
                return;
            }
        };
    }
    
    // Async session validation
    (async function() {
        const loggedIn = await isLoggedIn();
        if (!loggedIn) {
            window.location.replace('login.html');
            return;
        }
        
        if (!isAdmin()) {
            alert('Access denied. Admin privileges required.');
            window.location.replace('login.html');
            return;
        }
    })();
    
    // Set up periodic session check
    setInterval(async function() {
        const loggedIn = await isLoggedIn();
        if (!loggedIn || !isAdmin() || wasExplicitlyLoggedOut()) {
            window.location.replace('login.html');
        }
    }, 10000); // Check every 10 seconds
    
    return true;
}

// Protect user pages
function protectUserPage() {
    // Add cache control meta tags
    const metaTags = [
        '<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">',
        '<meta http-equiv="Pragma" content="no-cache">',
        '<meta http-equiv="Expires" content="0">'
    ];
    
    metaTags.forEach(tag => {
        if (!document.head.innerHTML.includes(tag)) {
            document.head.innerHTML += tag;
        }
    });
    
    // Disable browser back/forward cache
    window.onpageshow = function(event) {
        if (event.persisted || wasExplicitlyLoggedOut()) {
            window.location.replace('login.html');
        }
    };
    
    // Prevent caching and handle back button
    if (window.history && window.history.pushState) {
        window.history.pushState(null, null, window.location.href);
        
        window.onpopstate = async function() {
            window.history.pushState(null, null, window.location.href);
            
            const loggedIn = await isLoggedIn();
            if (!loggedIn || wasExplicitlyLoggedOut()) {
                window.location.replace('login.html');
            }
        };
    }
    
    // Async session validation
    (async function() {
        const loggedIn = await isLoggedIn();
        if (!loggedIn) {
            window.location.replace('login.html');
            return;
        }
    })();
    
    // Set up periodic session check
    setInterval(async function() {
        const loggedIn = await isLoggedIn();
        if (!loggedIn || wasExplicitlyLoggedOut()) {
            window.location.replace('login.html');
        }
    }, 10000); // Check every 10 seconds
    
    return true;
}

// Simple user verification without aggressive protection
function verifyUserSession() {
    const session = getCurrentSession();
    return session !== null;
}

// Check if user can access user pages
function canAccessUserPages() {
    if (wasExplicitlyLoggedOut()) {
        return false;
    }
    return verifyUserSession();
}

// Get all users (admin only)
async function getAllUsers() {
    if (!isAdmin()) return [];
    try {
        const response = await fetch(`${API_BASE}/users/`);
        if (response.ok) {
            return await response.json();
        }
    } catch (error) {
        console.error('Error fetching users:', error);
    }
    return [];
}

// Compatibility function
function saveToUserList(profile) {
    const USERS_LIST_KEY = 'rtb_all_users';
    let users = localStorage.getItem(USERS_LIST_KEY);
    users = users ? JSON.parse(users) : [];
    if (!users.find(u => u.phone === profile.phone)) {
        users.push(profile);
        localStorage.setItem(USERS_LIST_KEY, JSON.stringify(users));
    }
}

// Get user by ID or phone
function getUserById(userId) {
    const users = getAllUsers();
    return users.find(u => u.userId === userId || u.phone === userId);
}

function getUserByPhone(phone) {
    const users = getAllUsers();
    return users.find(u => u.phone === phone);
}

// Get all registered users (compatibility)
async function getAllRegisteredUsers() {
    return await getAllUsers();
}

// Initialize on load
initUsersDB();
