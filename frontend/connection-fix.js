// Robust connection handler for cross-device compatibility
class ConnectionManager {
    constructor() {
        this.maxRetries = 3;
        this.retryDelay = 1000;
        this.timeout = 10000;
    }

    async makeRequest(url, options = {}) {
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), this.timeout);
        
        const defaultOptions = {
            method: 'GET',
            mode: 'cors',
            credentials: 'omit',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            signal: controller.signal,
            ...options
        };

        for (let attempt = 1; attempt <= this.maxRetries; attempt++) {
            try {
                const response = await fetch(url, defaultOptions);
                clearTimeout(timeoutId);
                
                if (!response.ok) {
                    throw new Error(`HTTP ${response.status}: ${response.statusText}`);
                }
                
                return response;
            } catch (error) {
                console.warn(`Attempt ${attempt} failed:`, error.message);
                
                if (attempt === this.maxRetries) {
                    clearTimeout(timeoutId);
                    throw new Error(`Connection failed after ${this.maxRetries} attempts: ${error.message}`);
                }
                
                await this.delay(this.retryDelay * attempt);
            }
        }
    }

    delay(ms) {
        return new Promise(resolve => setTimeout(resolve, ms));
    }
}

// Global connection manager instance
window.connectionManager = new ConnectionManager();

// Enhanced API configuration with fallback
const API_CONFIG = {
    development: 'http://localhost:8000',
    production: 'https://leonardus437.pythonanywhere.com'
};

const isLocalDevelopment = window.location.hostname === 'localhost' || 
                          window.location.hostname === '127.0.0.1' ||
                          window.location.port === '5173';

const API_BASE = isLocalDevelopment ? API_CONFIG.development : API_CONFIG.production;

// Test API connectivity with robust error handling
async function testAPIConnection() {
    try {
        const response = await connectionManager.makeRequest(`${API_BASE}/`);
        const data = await response.json();
        console.log('✅ API connection successful:', data);
        return true;
    } catch (error) {
        console.error('❌ API connection failed:', error.message);
        return false;
    }
}

// Enhanced user limits fetching with retry logic
async function fetchUserLimits(phone) {
    try {
        const encodedPhone = encodeURIComponent(phone);
        const response = await connectionManager.makeRequest(`${API_BASE}/user-limits/${encodedPhone}`);
        return await response.json();
    } catch (error) {
        console.error('Failed to fetch user limits:', error.message);
        throw error;
    }
}

// Enhanced user authentication with retry logic
async function authenticateUser(phone, password) {
    try {
        const response = await connectionManager.makeRequest(`${API_BASE}/users/login`, {
            method: 'POST',
            body: JSON.stringify({ phone, password })
        });
        return await response.json();
    } catch (error) {
        console.error('Authentication failed:', error.message);
        throw error;
    }
}

// Enhanced user registration with retry logic
async function registerUser(userData) {
    try {
        const response = await connectionManager.makeRequest(`${API_BASE}/users/register`, {
            method: 'POST',
            body: JSON.stringify(userData)
        });
        return await response.json();
    } catch (error) {
        console.error('Registration failed:', error.message);
        throw error;
    }
}

// Initialize connection test on load
document.addEventListener('DOMContentLoaded', () => {
    testAPIConnection();
});

console.log('Connection manager initialized');
console.log('Environment:', isLocalDevelopment ? 'local development' : 'production');
console.log('API Base URL:', API_BASE);