// API Configuration with fallback
const API_CONFIG = {
    development: 'http://localhost:8000',
    production: 'https://leonardus437.pythonanywhere.com'
};

// Detect environment
const isLocalDevelopment = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
const API_BASE = isLocalDevelopment ? API_CONFIG.development : API_CONFIG.production;

console.log('Environment:', isLocalDevelopment ? 'local development' : 'production');
console.log('API Base URL:', API_BASE);

// Test API connectivity
async function testAPIConnection() {
    try {
        const response = await fetch(`${API_BASE}/`, { 
            method: 'GET',
            mode: 'cors',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (response.ok) {
            console.log('✅ API connection successful');
            return true;
        }
    } catch (error) {
        console.error('❌ API connection failed:', error);
        return false;
    }
    return false;
}

// Initialize API connection test
testAPIConnection();