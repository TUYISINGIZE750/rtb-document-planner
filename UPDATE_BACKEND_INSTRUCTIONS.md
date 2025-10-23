# 🔧 Update PythonAnywhere Backend

## Quick Update Steps

### 1. Login to PythonAnywhere
Go to: https://www.pythonanywhere.com/
Login as: leonardus437

### 2. Upload New Files

Go to **Files** tab and upload these files to your project directory:

#### Required Files:
1. `backend/rtb_professional_generator.py` ⭐ NEW FILE
2. `backend/main_minimal.py` (updated version)
3. `backend/requirements.txt` (updated version)

### 3. Install Dependencies

Open a **Bash console** and run:

```bash
cd ~
pip3.10 install --user flask flask-cors python-docx lxml
```

### 4. Update WSGI Configuration

Go to **Web** tab → Click on your WSGI configuration file

Make sure it imports from the correct file:
```python
from main_minimal import app as application
```

### 5. Reload Web App

On the **Web** tab, click the green **Reload** button.

## 🧪 Test Your Backend

After reloading, test these endpoints:

### 1. Health Check
```
https://leonardus437.pythonanywhere.com/
```
Should return: `{"message": "RTB API", "status": "online"}`

### 2. Create Test Session Plan
Use Postman or curl:
```bash
curl -X POST https://leonardus437.pythonanywhere.com/session-plans \
  -H "Content-Type: application/json" \
  -d '{
    "sector": "ICT",
    "sub_sector": "Software Development",
    "trainer_name": "Test Teacher",
    "topic_of_session": "Test Topic",
    "duration": "40"
  }'
```

### 3. Download Test Document
If you get an ID (e.g., 1), test download:
```
https://leonardus437.pythonanywhere.com/session-plans/1/download
```

## 📋 Verification Checklist

After updating, verify:

- [ ] Backend responds at root URL
- [ ] Can create session plans (POST /session-plans)
- [ ] Can download session plans (GET /session-plans/X/download)
- [ ] Downloaded documents have proper RTB structure
- [ ] Documents open correctly in Microsoft Word
- [ ] Can create schemes (POST /schemes)
- [ ] Can download schemes (GET /schemes/X/download)

## 🐛 Troubleshooting

### Error: Module not found
```bash
# Install missing dependencies
pip3.10 install --user python-docx lxml flask flask-cors
```

### Error: Import error for rtb_professional_generator
- Make sure `rtb_professional_generator.py` is in the same directory as `main_minimal.py`
- Check file permissions (should be readable)

### Error: CORS issues
- Verify `flask-cors` is installed
- Check CORS configuration in `main_minimal.py`:
  ```python
  CORS(app, origins=["https://tuyisingize750.github.io"])
  ```

### Documents not generating correctly
- Check error logs in PythonAnywhere
- Verify `python-docx` and `lxml` are installed
- Test locally first with `backend/test_generator.py`

## 📁 File Locations on PythonAnywhere

Your files should be at:
```
/home/leonardus437/
├── main_minimal.py
├── rtb_professional_generator.py  ← NEW FILE
└── requirements.txt
```

## 🔄 Alternative: Upload via Web Interface

1. Go to **Files** tab
2. Navigate to your project directory
3. Click **Upload a file**
4. Select and upload:
   - `rtb_professional_generator.py`
   - `main_minimal.py`
   - `requirements.txt`

## ✅ Success Indicators

You'll know it's working when:
- ✅ No errors in error log
- ✅ Can access root URL
- ✅ Can create and download documents
- ✅ Documents have proper RTB structure
- ✅ Frontend can connect and download documents

## 🎯 Quick Test from Frontend

1. Go to: https://tuyisingize750.github.io/rtb-document-planner/
2. Login with: +250796014803 / teacher123
3. Click "Create Session Plan"
4. Fill out the form
5. Click "Generate Session Plan"
6. Document should download automatically
7. Open in Microsoft Word
8. Verify structure matches RTB template

## 📞 Need Help?

If you encounter issues:
1. Check PythonAnywhere error logs (Web tab → Log files)
2. Verify all files are uploaded
3. Confirm dependencies are installed
4. Test endpoints individually
5. Check CORS configuration

## 🎉 You're Done!

Once the backend is updated:
- Frontend: ✅ Live on GitHub Pages
- Backend: ✅ Updated on PythonAnywhere
- Documents: ✅ RTB-compliant and professional
- System: ✅ Ready for production use!
