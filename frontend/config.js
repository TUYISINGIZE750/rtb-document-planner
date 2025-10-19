// API Configuration
const API_CONFIG = {
    development: 'http://localhost:8000',
    production: 'https://rtb-document-planner.onrender.com'
};

// Detect environment
const isProduction = window.location.hostname !== 'localhost' && window.location.hostname !== '127.0.0.1';
const API_BASE = isProduction ? API_CONFIG.production : API_CONFIG.development;

console.log('Environment:', isProduction ? 'production' : 'development');
console.log('API Base URL:', API_BASE);