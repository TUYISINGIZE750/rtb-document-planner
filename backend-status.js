// Backend Status Checker for RTB Document Planner
console.log('🔍 Backend status checker loaded');

async function checkBackendStatus() {
    try {
        const response = await fetch(`${API_BASE}/`, {
            method: 'GET',
            mode: 'cors',
            credentials: 'omit',
            headers: {
                'Accept': 'application/json'
            }
        });
        
        if (response.ok) {
            const data = await response.json();
            console.log('✅ Backend online:', data);
            return { online: true, data };
        } else {
            console.log('❌ Backend returned error:', response.status);
            return { online: false, error: `HTTP ${response.status}` };
        }
    } catch (error) {
        console.log('❌ Backend connection failed:', error.message);
        return { online: false, error: error.message };
    }
}

function showBackendStatus() {
    checkBackendStatus().then(status => {
        const statusDiv = document.createElement('div');
        statusDiv.id = 'backendStatus';
        statusDiv.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            padding: 0.75rem;
            text-align: center;
            font-weight: 600;
            z-index: 9999;
            font-size: 0.875rem;
        `;
        
        if (status.online) {
            statusDiv.style.background = 'linear-gradient(135deg, #10b981, #059669)';
            statusDiv.style.color = 'white';
            statusDiv.innerHTML = `
                <i class="fas fa-check-circle"></i> 
                Backend Online - Authentication & Downloads Available
            `;
            // Auto-hide after 3 seconds
            setTimeout(() => {
                if (statusDiv.parentNode) {
                    statusDiv.style.transform = 'translateY(-100%)';
                    setTimeout(() => statusDiv.remove(), 300);
                }
            }, 3000);
        } else {
            statusDiv.style.background = 'linear-gradient(135deg, #ef4444, #dc2626)';
            statusDiv.style.color = 'white';
            statusDiv.innerHTML = `
                <i class="fas fa-exclamation-triangle"></i> 
                Backend Offline - Please upload main_production.py to PythonAnywhere
                <button onclick="this.parentNode.remove()" style="margin-left: 1rem; padding: 0.25rem 0.5rem; background: rgba(255,255,255,0.2); border: none; color: white; border-radius: 0.25rem; cursor: pointer;">
                    <i class="fas fa-times"></i>
                </button>
            `;
        }
        
        statusDiv.style.transform = 'translateY(-100%)';
        document.body.appendChild(statusDiv);
        
        // Animate in
        setTimeout(() => {
            statusDiv.style.transition = 'transform 0.3s ease';
            statusDiv.style.transform = 'translateY(0)';
        }, 100);
    });
}

// Show status on page load
document.addEventListener('DOMContentLoaded', showBackendStatus);