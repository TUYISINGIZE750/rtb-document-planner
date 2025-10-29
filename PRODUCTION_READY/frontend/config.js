// RTB Document Planner - Production Configuration
console.log('✅ config.js loaded (PRODUCTION CLOUDFLARE + RENDER)');

// DYNAMIC API URL - Works on Cloudflare Pages & Local
const API_BASE = (() => {
    // Cloudflare Pages deployment
    if (window.location.hostname.includes('pages.dev') || window.location.hostname.includes('rtb-planner')) {
        return 'https://rtb-document-planner.onrender.com';
    }
    // Local development
    if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
        return 'http://localhost:8000';
    }
    // Default to Render
    return 'https://rtb-document-planner.onrender.com';
})();

console.log('🌐 API Base URL:', API_BASE);
console.log('🚀 Environment: PRODUCTION');
console.log('📡 Detected Host:', window.location.hostname);
console.log('📡 Backend: Render.com (rtb-document-planner.onrender.com)');

// Test API connection
async function testAPIConnection() {
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
            const data = await response.json();
            console.log('✅ API connection successful:', data);
            return true;
        }
    } catch (error) {
        console.error('❌ API connection failed:', error.message);
        console.error('Attempting connection to:', `${API_BASE}/`);
        return false;
    }
    return false;
}

// Initialize API test after DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => setTimeout(testAPIConnection, 500));
} else {
    setTimeout(testAPIConnection, 500);
}