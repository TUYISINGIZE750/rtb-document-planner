# MTN MoMo Payment Integration Guide

## ⚠️ IMPORTANT: Current Implementation

The current system uses **localStorage** to track free downloads (2 session plans + 2 schemes). This is a **temporary solution** that can be bypassed by clearing browser data. It's suitable for demonstration but NOT for production.

## 💰 How to Receive Real Payments

### Option 1: Manual Payment (Simplest - Works Now!)

**How it works:**
1. User exhausts free downloads
2. System shows your MTN number: **250796888309**
3. User sends 5,000 RWF via MTN MoMo
4. User contacts you with transaction ID
5. You manually activate their account

**To activate a user manually:**
```javascript
// In browser console, run:
activatePremium("any-code-here");
```

**Pros:**
- Works immediately
- No technical setup needed
- You receive money directly
- Simple to manage

**Cons:**
- Manual work required
- Not scalable for many users

---

### Option 2: MTN MoMo API Integration (Automated - Requires Setup)

To receive payments automatically to your phone (250796888309), you need:

#### Step 1: Backend Setup Required

You CANNOT use MTN MoMo API from frontend. You need a backend server:

**Required Technologies:**
- Python FastAPI (you already have this!)
- Environment variables for API keys
- Database to track payments
- User authentication system

#### Step 2: MTN MoMo Developer Account

1. Register at: https://momodeveloper.mtn.com/
2. Get your API credentials (keep them SECRET!)
3. Use **Collections API** to receive payments

#### Step 3: Backend Implementation

Create new file: `backend/payment.py`

```python
import os
import requests
import uuid
from fastapi import HTTPException

# NEVER hardcode these - use environment variables!
MTN_COLLECTION_KEY = os.getenv('MTN_COLLECTION_KEY')
MTN_API_USER = os.getenv('MTN_API_USER')
MTN_API_KEY = os.getenv('MTN_API_KEY')
MTN_ENVIRONMENT = 'mtnrwanda'  # or 'sandbox' for testing

def request_payment(phone_number: str, amount: int, reference: str):
    """Request payment from user's MTN MoMo account"""
    
    # Generate access token
    token_url = f"https://proxy.momoapi.mtn.com/collection/token/"
    token_response = requests.post(
        token_url,
        headers={
            'Ocp-Apim-Subscription-Key': MTN_COLLECTION_KEY,
            'Authorization': f'Basic {MTN_API_KEY}'
        }
    )
    access_token = token_response.json()['access_token']
    
    # Request payment
    transaction_id = str(uuid.uuid4())
    payment_url = f"https://proxy.momoapi.mtn.com/collection/v1_0/requesttopay"
    
    payload = {
        "amount": str(amount),
        "currency": "RWF",
        "externalId": reference,
        "payer": {
            "partyIdType": "MSISDN",
            "partyId": phone_number
        },
        "payerMessage": "RTB Document Planner Subscription",
        "payeeNote": "Monthly subscription payment"
    }
    
    response = requests.post(
        payment_url,
        json=payload,
        headers={
            'Authorization': f'Bearer {access_token}',
            'X-Reference-Id': transaction_id,
            'X-Target-Environment': MTN_ENVIRONMENT,
            'Ocp-Apim-Subscription-Key': MTN_COLLECTION_KEY,
            'Content-Type': 'application/json'
        }
    )
    
    return transaction_id

def check_payment_status(transaction_id: str):
    """Check if payment was successful"""
    # Implementation to check transaction status
    pass
```

#### Step 4: Add Payment Endpoints

In `backend/main.py`:

```python
from payment import request_payment, check_payment_status

@app.post("/api/subscribe")
async def subscribe(phone: str, db: Session = Depends(get_db)):
    """Initiate subscription payment"""
    try:
        transaction_id = request_payment(phone, 5000, f"SUB-{phone}")
        # Save transaction to database
        return {"transaction_id": transaction_id, "status": "pending"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/api/check-payment/{transaction_id}")
async def check_payment(transaction_id: str):
    """Check payment status"""
    status = check_payment_status(transaction_id)
    if status == "SUCCESSFUL":
        # Activate user's premium account
        return {"status": "success"}
    return {"status": "pending"}
```

#### Step 5: Environment Variables

Create `.env` file (NEVER commit this to git!):

```
MTN_COLLECTION_KEY=your_primary_key_here
MTN_API_USER=your_api_user_here
MTN_API_KEY=your_api_key_here
```

#### Step 6: Database Schema

Add to `backend/models.py`:

```python
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    phone = Column(String, unique=True)
    is_premium = Column(Boolean, default=False)
    premium_until = Column(DateTime, nullable=True)

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    transaction_id = Column(String, unique=True)
    phone = Column(String)
    amount = Column(Integer)
    status = Column(String)  # pending, success, failed
    created_at = Column(DateTime, default=datetime.utcnow)
```

---

### Option 3: Third-Party Payment Gateway (Easiest Automated)

Use services that handle MTN MoMo for you:

**Flutterwave (Recommended for Rwanda):**
- Website: https://flutterwave.com/rw
- Supports MTN MoMo Rwanda
- Easier integration than direct MTN API
- They handle security and compliance
- Money goes to your account

**Integration Steps:**
1. Sign up at Flutterwave
2. Get API keys
3. Use their payment widget
4. Money deposited to your bank/mobile money

---

## 🎯 Recommended Approach for You

**For Now (Immediate):**
- Use the localStorage system I just implemented
- Accept manual payments to 250796888309
- Manually activate users

**For Future (When you have many users):**
- Hire a developer to implement Option 2 or 3
- Or use Flutterwave for easier integration
- Deploy to a proper hosting service (not localhost)

---

## 📱 Testing Current System

1. Open the app
2. Download 2 session plans
3. Try to download a 3rd one
4. Payment modal will appear with your number
5. User sends money to 250796888309
6. You activate them manually

---

## 🔒 Security Notes

- NEVER put API keys in frontend code
- NEVER commit credentials to GitHub
- Always use HTTPS in production
- Validate all payments on backend
- Keep transaction records

---

## 💡 Cost Estimate for Full Implementation

If hiring a developer:
- Backend payment integration: $200-500
- User authentication system: $300-600
- Hosting (per month): $10-50
- Total: ~$500-1000 one-time + monthly hosting

---

## 📞 Support

For MTN MoMo API support:
- Email: api@mtn.com
- Developer Portal: https://momodeveloper.mtn.com/

For Flutterwave:
- Support: https://flutterwave.com/rw/support
