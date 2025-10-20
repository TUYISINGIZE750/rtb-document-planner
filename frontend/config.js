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

// Enhanced environment detection - detects local development including network access
function detectEnvironment() {
    const hostname = window.location.hostname;
    const isLocalhost = hostname === 'localhost' || hostname === '127.0.0.1';
    const isLocalIP = /^(192\.168|10\.|172\.(1[6-9]|2[0-9]|3[01]))/.test(hostname);
    const isDevelopmentPort = window.location.port === '5173';
    
    return isLocalhost || isLocalIP || isDevelopmentPort;
}

const isLocalDevelopment = detectEnvironment();

// Build API_BASE - uses local machine IP for network access
let API_BASE;
if (isLocalDevelopment) {
    // For local development, replace localhost with the actual hostname to support network access
    if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
        // User is accessing via localhost - use localhost
        API_BASE = API_CONFIG.development;
    } else {
        // User is accessing via network IP - use same IP for backend
        API_BASE = `http://${window.location.hostname}:8000`;
    }
} else {
    API_BASE = API_CONFIG.production;
}

console.log('✅ config.js loaded successfully (v1.0.1-ts-20250103T120000Z-CDN-FRESH)');
console.log('Environment:', isLocalDevelopment ? 'local development' : 'production');
console.log('API Base URL:', API_BASE);
console.log('Timestamp Bust:', '20250103T120000Z');

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