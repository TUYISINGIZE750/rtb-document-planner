// Authentication system with admin role protection
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

// Register new user
async function registerUser(name, phone, email, institution, password) {
    const userId = 'USER_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
    
    try {
        const response = await fetch('http://localhost:8000/users/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ user_id: userId, name, phone, email, institution, password, role: 'user' })
        });
        
        if (response.ok) {
            return { success: true };
        } else {
            const error = await response.json();
            return { success: false, message: error.detail };
        }
    } catch (error) {
        return { success: false, message: 'Network error' };
    }
}

// Login user
async function loginUser(phone, password, remember) {
    try {
        // Clear any existing session data first
        clearSessionStorage();
        clearLogoutMarkers();
        clearLogoutFlag();
        
        const response = await fetch('http://localhost:8000/users/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ phone, password })
        });
        
        if (response.ok) {
            const user = await response.json();
            const expiryTime = remember ? 30 * 24 * 60 * 60 * 1000 : 24 * 60 * 60 * 1000;
            const session = { 
                ...user, 
                loggedInAt: new Date().toISOString(),
                expiresAt: new Date(Date.now() + expiryTime).toISOString(),
                remember,
                sessionId: 'SESSION_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9)
            };
            localStorage.setItem(AUTH_KEY, JSON.stringify(session));
            // Clear logout flags on successful login
            clearLogoutFlag();
            return { success: true, role: user.role };
        } else {
            return { success: false, message: 'Incorrect phone number or password' };
        }
    } catch (error) {
        return { success: false, message: 'Network error' };
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
        const response = await fetch(`http://localhost:8000/users/${encodeURIComponent(session.phone)}`);
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
    
    // Clear session data
    localStorage.removeItem(AUTH_KEY);
    sessionStorage.removeItem(AUTH_KEY);
    
    // Set logout marker with timestamp
    const logoutTime = Date.now().toString();
    localStorage.setItem(LOGOUT_FLAG_KEY, logoutTime);
    sessionStorage.setItem(LOGOUT_FLAG_KEY, logoutTime);
    
    // Manipulate history to prevent back button access
    window.history.pushState(null, null, window.location.href);
    window.history.pushState(null, null, window.location.href);
    
    // Redirect based on role
    const redirectPage = isAdmin ? 'direct-login.html' : 'login-select.html';
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
        window.location.replace('login-select.html');
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
            window.location.replace('login-select.html');
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
            window.location.replace('direct-login.html');
            return;
        }
        
        if (!isAdmin()) {
            alert('Access denied. Admin privileges required.');
            window.location.replace('index.html');
            return;
        }
    })();
    
    // Set up periodic session check
    setInterval(async function() {
        const loggedIn = await isLoggedIn();
        if (!loggedIn || !isAdmin() || wasExplicitlyLoggedOut()) {
            window.location.replace('direct-login.html');
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
        const response = await fetch('http://localhost:8000/users/');
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
