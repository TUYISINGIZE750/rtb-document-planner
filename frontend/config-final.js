// RTB Document Planner - Final Configuration
// Production-only API configuration to eliminate localhost issues

const API_BASE = 'https://rtb-document-planner.onrender.com';

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = { API_BASE };
}

console.log('Config loaded - API Base:', API_BASE);