// API Configuration
const API_CONFIG = {
    development: 'http://localhost:8000',
    production: 'https://leonardus437.pythonanywhere.com'  // Your PythonAnywhere backend
};

// Detect environment - both localhost and Vercel should use production API
const isLocalDevelopment = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1';
const API_BASE = isLocalDevelopment ? API_CONFIG.development : API_CONFIG.production;

console.log('Environment:', isLocalDevelopment ? 'local development' : 'production');
console.log('API Base URL:', API_BASE);
console.log('Current hostname:', window.location.hostname);