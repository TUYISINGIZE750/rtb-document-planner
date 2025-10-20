// Quick fix for registration connection issues
function fixRegistration() {
    // Override the registerUser function with better error handling
    window.originalRegisterUser = window.registerUser;
    
    window.registerUser = async function(name, phone, email, institution, password) {
        const userId = 'USER_' + Date.now() + '_' + Math.random().toString(36).substr(2, 9);
        const userData = { user_id: userId, name, phone, email, institution, password, role: 'user' };
        
        // Try multiple methods
        const methods = [
            // Method 1: Connection manager
            async () => {
                if (window.connectionManager) {
                    const response = await window.connectionManager.makeRequest(
                        `${API_BASE}/users/register`, 
                        { method: 'POST', body: JSON.stringify(userData) }
                    );
                    return await response.json();
                }
                throw new Error('Connection manager not available');
            },
            
            // Method 2: Direct fetch with enhanced headers
            async () => {
                const response = await fetch(`${API_BASE}/users/register`, {
                    method: 'POST',
                    mode: 'cors',
                    credentials: 'omit',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'Origin': window.location.origin
                    },
                    body: JSON.stringify(userData)
                });
                
                if (!response.ok) {
                    const error = await response.json().catch(() => ({ detail: 'Registration failed' }));
                    throw new Error(error.detail || `HTTP ${response.status}`);
                }
                
                return await response.json();
            }
        ];
        
        // Try each method
        for (let i = 0; i < methods.length; i++) {
            try {
                await methods[i]();
                return { success: true };
            } catch (error) {
                console.warn(`Registration method ${i + 1} failed:`, error.message);
                if (i === methods.length - 1) {
                    // Last method failed
                    if (error.message.includes('already registered')) {
                        return { success: false, message: 'Phone number already registered' };
                    }
                    return { success: false, message: 'Registration failed. Please try again.' };
                }
            }
        }
    };
}

// Apply fix when page loads
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', fixRegistration);
} else {
    fixRegistration();
}