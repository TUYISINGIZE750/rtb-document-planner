// Simple Authentication System
const API_BASE = 'https://leonardus437.pythonanywhere.com';
const AUTH_KEY = 'rtb_auth_session';

async function loginUser(phone, password, remember) {
    try {
        const response = await fetch(`${API_BASE}/users/login`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ phone, password })
        });
        
        if (response.ok) {
            const user = await response.json();
            const session = { ...user, loggedInAt: new Date().toISOString(), remember };
            localStorage.setItem(AUTH_KEY, JSON.stringify(session));
            return { success: true, role: user.role };
        } else {
            const error = await response.json();
            return { success: false, message: error.detail || 'Login failed' };
        }
    } catch (error) {
        return { success: false, message: 'Connection error' };
    }
}

function getCurrentSession() {
    try {
        const session = localStorage.getItem(AUTH_KEY);
        return session ? JSON.parse(session) : null;
    } catch (e) {
        return null;
    }
}

function logout() {
    localStorage.removeItem(AUTH_KEY);
    window.location.href = 'login.html';
}

console.log('✅ auth.js loaded');