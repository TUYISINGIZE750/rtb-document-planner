// Load connection manager first
if (!window.connectionManager) {
    const script = document.createElement('script');
    script.src = 'connection-fix.js';
    document.head.appendChild(script);
}

// API Configuration with enhanced fallback
const API_CONFIG = {
    development: 'http://localhost:8000',
    production: 'https://leonardus437.pythonanywhere.com'
};

// Enhanced environment detection
const isLocalDevelopment = window.location.hostname === 'localhost' || 
                          window.location.hostname === '127.0.0.1' ||
                          window.location.port === '5173';

const API_BASE = isLocalDevelopment ? API_CONFIG.development : API_CONFIG.production;

console.log('Environment:', isLocalDevelopment ? 'local development' : 'production');
console.log('API Base URL:', API_BASE);

// Enhanced API connectivity test
async function testAPIConnection() {
    if (!window.connectionManager) {
        console.warn('Connection manager not loaded, using fallback');
        try {
            const response = await fetch(`${API_BASE}/`, { 
                method: 'GET',
                mode: 'cors',
                credentials: 'omit',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                }
            });
            if (response.ok) {
                console.log('✅ API connection successful (fallback)');
                return true;
            }
        } catch (error) {
            console.error('❌ API connection failed (fallback):', error);
            return false;
        }
        return false;
    }
    
    try {
        const response = await window.connectionManager.makeRequest(`${API_BASE}/`);
        const data = await response.json();
        console.log('✅ API connection successful:', data);
        return true;
    } catch (error) {
        console.error('❌ API connection failed:', error.message);
        return false;
    }
}

// Initialize with delay to ensure connection manager loads
setTimeout(testAPIConnection, 100);