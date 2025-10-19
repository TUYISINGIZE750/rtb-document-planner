// Modern Chat Widget with Multiple Contact Options
const CONTACT_INFO = {
    whatsapp: '+250789751597',
    phone: '250789751597',
    email: 'niyonkurufabrice@gmail.com',
    name: 'Leonard TUYISINGIZE'
};

function createChatWidget() {
    const widget = document.createElement('div');
    widget.innerHTML = `
        <!-- Floating Chat Button -->
        <div id="chatButton" style="position: fixed; bottom: 1.5rem; right: 1.5rem; z-index: 9998; cursor: pointer;" onclick="toggleChatWidget()">
            <div style="width: 56px; height: 56px; background: linear-gradient(135deg, #10b981, #059669); border-radius: 50%; display: flex; align-items: center; justify-content: center; box-shadow: 0 4px 12px rgba(16, 185, 129, 0.4); transition: all 0.3s; animation: pulse 2s infinite;">
                <i class="fas fa-comments" style="color: white; font-size: 1.4rem;"></i>
            </div>
            <div style="position: absolute; top: -3px; right: -3px; width: 18px; height: 18px; background: #ef4444; border-radius: 50%; border: 2px solid white; animation: bounce 1s infinite;"></div>
        </div>

        <!-- Chat Widget Panel -->
        <div id="chatWidget" style="position: fixed; bottom: 5.5rem; right: 1.5rem; width: 280px; background: white; border-radius: 1rem; box-shadow: 0 10px 40px rgba(0,0,0,0.2); z-index: 9999; display: none; animation: slideUp 0.3s; max-height: 70vh; overflow-y: auto;">
            <!-- Header -->
            <div style="background: linear-gradient(135deg, #10b981, #059669); padding: 1rem; border-radius: 1rem 1rem 0 0; color: white;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <h3 style="margin: 0; font-size: 1rem; font-weight: 700;">Need Help?</h3>
                        <p style="margin: 0.25rem 0 0 0; font-size: 0.75rem; opacity: 0.9;">Contact us</p>
                    </div>
                    <button onclick="toggleChatWidget()" style="background: rgba(255,255,255,0.2); border: none; color: white; width: 28px; height: 28px; border-radius: 50%; cursor: pointer; font-size: 1.1rem; display: flex; align-items: center; justify-content: center;">×</button>
                </div>
            </div>

            <!-- Contact Options -->
            <div style="padding: 1rem;">

                <!-- WhatsApp -->
                <a href="https://wa.me/${CONTACT_INFO.whatsapp}?text=Hello,%20I%20need%20help%20with%20RTB%20Document%20Planner" target="_blank" style="display: flex; align-items: center; gap: 0.75rem; padding: 0.75rem; background: linear-gradient(135deg, #10b981, #059669); color: white; border-radius: 0.5rem; text-decoration: none; margin-bottom: 0.5rem; transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='translateY(0)'">
                    <i class="fab fa-whatsapp" style="font-size: 1.25rem;"></i>
                    <div style="flex: 1;">
                        <div style="font-weight: 600; font-size: 0.85rem;">WhatsApp</div>
                        <div style="font-size: 0.7rem; opacity: 0.9;">Instant chat</div>
                    </div>
                </a>

                <!-- Kinyarwanda -->
                <a href="https://wa.me/${CONTACT_INFO.whatsapp}?text=Mwaramutse,%20nkeneye%20ubufasha" target="_blank" style="display: flex; align-items: center; gap: 0.75rem; padding: 0.75rem; background: linear-gradient(135deg, #3b82f6, #2563eb); color: white; border-radius: 0.5rem; text-decoration: none; margin-bottom: 0.5rem; transition: transform 0.2s;" onmouseover="this.style.transform='translateY(-2px)'" onmouseout="this.style.transform='translateY(0)'">
                    <i class="fab fa-whatsapp" style="font-size: 1.25rem;"></i>
                    <div style="flex: 1;">
                        <div style="font-weight: 600; font-size: 0.85rem;">Nyandikira</div>
                        <div style="font-size: 0.7rem; opacity: 0.9;">Kinyarwanda</div>
                    </div>
                </a>

                <!-- Phone -->
                <a href="tel:${CONTACT_INFO.phone}" style="display: flex; align-items: center; gap: 0.75rem; padding: 0.75rem; background: #f8fafc; color: #1e293b; border-radius: 0.5rem; text-decoration: none; margin-bottom: 0.5rem; border: 1px solid #e2e8f0; transition: all 0.2s;" onmouseover="this.style.borderColor='#6366f1'" onmouseout="this.style.borderColor='#e2e8f0'">
                    <i class="fas fa-phone" style="font-size: 1.1rem; color: #6366f1;"></i>
                    <div style="flex: 1;">
                        <div style="font-weight: 600; font-size: 0.85rem;">Call</div>
                        <div style="font-size: 0.7rem; color: #64748b;">${CONTACT_INFO.phone}</div>
                    </div>
                </a>

                <!-- Email -->
                <a href="mailto:${CONTACT_INFO.email}" style="display: flex; align-items: center; gap: 0.75rem; padding: 0.75rem; background: #f8fafc; color: #1e293b; border-radius: 0.5rem; text-decoration: none; border: 1px solid #e2e8f0; transition: all 0.2s;" onmouseover="this.style.borderColor='#8b5cf6'" onmouseout="this.style.borderColor='#e2e8f0'">
                    <i class="fas fa-envelope" style="font-size: 1.1rem; color: #8b5cf6;"></i>
                    <div style="flex: 1;">
                        <div style="font-weight: 600; font-size: 0.85rem;">Email</div>
                        <div style="font-size: 0.7rem; color: #64748b;">leotuyi10@gmail.com</div>
                    </div>
                </a>
            </div>
        </div>

        <style>
            @keyframes pulse {
                0%, 100% { transform: scale(1); }
                50% { transform: scale(1.05); }
            }
            @keyframes bounce {
                0%, 100% { transform: translateY(0); }
                50% { transform: translateY(-5px); }
            }
            @keyframes slideUp {
                from { opacity: 0; transform: translateY(20px); }
                to { opacity: 1; transform: translateY(0); }
            }
            #chatButton:hover > div:first-child {
                transform: scale(1.1);
                box-shadow: 0 6px 20px rgba(16, 185, 129, 0.5);
            }
        </style>
    `;
    document.body.appendChild(widget);
}

function toggleChatWidget() {
    const widget = document.getElementById('chatWidget');
    if (widget.style.display === 'none' || !widget.style.display) {
        widget.style.display = 'block';
    } else {
        widget.style.display = 'none';
    }
}

function sendQuickMessage(event) {
    event.preventDefault();
    const name = document.getElementById('userName').value;
    const message = document.getElementById('userMessage').value;
    
    // Send via WhatsApp
    const whatsappMessage = `Hello, I'm ${name}. ${message}`;
    const whatsappUrl = `https://wa.me/${CONTACT_INFO.whatsapp}?text=${encodeURIComponent(whatsappMessage)}`;
    window.open(whatsappUrl, '_blank');
    
    // Clear form
    document.getElementById('quickMessageForm').reset();
    
    // Show success message
    alert('Opening WhatsApp to send your message!');
}

// Initialize widget when page loads
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', createChatWidget);
} else {
    createChatWidget();
}
