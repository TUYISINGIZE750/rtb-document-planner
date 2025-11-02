// RTB Document Planner - Production Configuration
console.log('✅ config.js loaded (PRODUCTION-ONLY v2.0)');

// FORCE PRODUCTION API - NO LOCAL DEVELOPMENT
const API_BASE = 'https://rtb-document-planner.onrender.com';

console.log('🌐 API Base URL:', API_BASE);
console.log('🚀 Environment: PRODUCTION ONLY');
console.log('📡 Backend: Render.com');

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
        console.error('❌ API connection failed:', error);
        return false;
    }
    return false;
}

// Initialize API test
setTimeout(testAPIConnection, 100);