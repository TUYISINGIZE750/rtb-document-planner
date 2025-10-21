# PythonAnywhere Backend Update - URGENT

## 🚨 CRITICAL: Update Your PythonAnywhere Backend NOW

### 1. Login to PythonAnywhere Console
Go to: https://www.pythonanywhere.com/user/leonardus437/

### 2. Edit Your main.py File
Add this CORS configuration at the top after imports:

```python
from fastapi.middleware.cors import CORSMiddleware

# Add this IMMEDIATELY after: app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://schemesession.netlify.app",
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=[
        "Accept",
        "Accept-Language", 
        "Content-Language",
        "Content-Type",
        "Authorization",
        "X-Requested-With"
    ],
    expose_headers=["*"],
    max_age=3600
)
```

### 3. Reload Your Web App
- Go to Web tab in PythonAnywhere
- Click "Reload leonardus437.pythonanywhere.com"

### 4. Test Integration
Visit: https://schemesession.netlify.app/test-connection.html

## ✅ Expected Results:
- API Connection: SUCCESS
- CORS Headers: SUCCESS  
- User Endpoints: ACCESSIBLE

## 🎯 Your System URLs:
- **Frontend:** https://schemesession.netlify.app
- **Backend:** https://leonardus437.pythonanywhere.com
- **Test Page:** https://schemesession.netlify.app/test-connection.html