# 🚨 URGENT: Registration Connection Error Fix

## 🔍 **Root Cause**
The registration error "Cannot reach server" is caused by **CORS configuration** on PythonAnywhere backend not allowing the new GitHub Pages URL.

## 🛠️ **IMMEDIATE FIX REQUIRED**

### **Step 1: Update PythonAnywhere Backend**
1. Go to **PythonAnywhere.com** → Login
2. Go to **Files** tab
3. Open your **main.py** file
4. Find the CORS section (around lines 20-40)
5. Replace it with this code:

```python
CORS(app, 
     origins=[
         "https://tuyisingize750.github.io",
         "https://tuyisingize750.github.io/rtb-document-planner",
         "https://schemesession.netlify.app",
         "http://localhost:5173",
         "http://localhost:8000"
     ],
     methods=["GET", "POST", "OPTIONS", "PUT"],
     allow_headers=["Content-Type", "Authorization"],
     supports_credentials=False)

@app.after_request
def after_request(response):
    origin = request.headers.get('Origin')
    allowed_origins = [
        "https://tuyisingize750.github.io",
        "https://tuyisingize750.github.io/rtb-document-planner", 
        "https://schemesession.netlify.app",
        "http://localhost:5173",
        "http://localhost:8000"
    ]
    if origin in allowed_origins:
        response.headers.add('Access-Control-Allow-Origin', origin)
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,POST,OPTIONS,PUT')
    return response
```

### **Step 2: Reload Web App**
1. Go to **Web** tab in PythonAnywhere
2. Click **Reload** button for your web app
3. Wait for reload to complete

### **Step 3: Test Connection**
Open: `test-backend-connection.html` to verify backend is working

## 🌐 **Correct URLs After Fix**

- **Registration**: `https://tuyisingize750.github.io/rtb-document-planner/register.html`
- **Login**: `https://tuyisingize750.github.io/rtb-document-planner/login.html`
- **Backend**: `https://leonardus437.pythonanywhere.com`

## ✅ **Expected Result**
After updating CORS and reloading:
- ✅ Registration will work without connection errors
- ✅ Login will work properly
- ✅ All API calls will succeed

## 🚨 **CRITICAL**
The backend MUST be updated on PythonAnywhere for registration to work. The frontend is ready, but the backend needs the CORS fix.

**Files to upload to PythonAnywhere:**
- `PYTHONANYWHERE_UPDATE_CORS.py` (contains the exact code to use)