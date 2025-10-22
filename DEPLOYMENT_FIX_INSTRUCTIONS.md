# RTB Document Planner - Deployment Fix Instructions

## Issues Fixed

1. **Session Rules Not Enforced** - Users could access wizard pages without login
2. **Documents Downloading as .txt** - Backend wasn't generating proper DOCX files
3. **No Authentication System** - Anyone could create documents without limits

## Files Created/Updated

### Backend Files (Upload to PythonAnywhere)
- `main_production.py` - Complete production backend with authentication and DOCX generation
- `document_generator.py` - Already exists (DOCX generation functions)
- `models.py` - Already exists (Database models)

### Frontend Files (Deploy to GitHub Pages)
- `auth-fixed.js` - Fixed authentication system with session enforcement
- `wizard.html` - Updated to use fixed auth
- `scheme-wizard.html` - Updated to use fixed auth
- `index.html` - Updated to use fixed auth
- `config.js` - Updated with deployment notes

## Deployment Steps

### 1. PythonAnywhere Backend Setup

1. **Upload Backend Files:**
   ```bash
   # Upload these files to your PythonAnywhere account:
   - main_production.py
   - document_generator.py (already exists)
   - models.py (already exists)
   - schemas.py (already exists)
   ```

2. **Set as WSGI Application:**
   - In PythonAnywhere dashboard, go to "Web" tab
   - Set WSGI file to point to `main_production.py`
   - Or rename `main_production.py` to `main.py`

3. **Install Required Packages:**
   ```bash
   pip install --user flask flask-cors sqlalchemy python-docx
   ```

4. **Database Setup:**
   - The database will be created automatically when the app starts
   - Admin user will be created: `+250789751597` / `admin123`

### 2. GitHub Pages Frontend Setup

1. **Update Repository:**
   ```bash
   # Push the updated frontend files to your GitHub repository
   git add .
   git commit -m "Fix authentication and DOCX generation"
   git push origin main
   ```

2. **GitHub Pages Settings:**
   - Go to repository Settings > Pages
   - Set source to "Deploy from a branch"
   - Select "main" branch and "/ (root)" folder
   - Your site will be available at: `https://yourusername.github.io/repository-name`

### 3. Update API Configuration

1. **Update config.js:**
   ```javascript
   const API_BASE = 'https://leonardus437.pythonanywhere.com';
   ```

2. **Update CORS in Backend:**
   - Make sure your GitHub Pages URL is in the CORS origins list in `main_production.py`
   - Replace `https://tuyisingize750.github.io` with your actual GitHub Pages URL

## Testing the Fixed System

### 1. Authentication Test
1. Visit your GitHub Pages site
2. Try to access wizard or scheme pages directly
3. Should be redirected to login modal
4. Register a new account
5. Login and verify access is granted

### 2. Document Generation Test
1. Login to the system
2. Create a session plan through the wizard
3. Verify it downloads as a proper .docx file (not .txt)
4. Open the file in Microsoft Word to verify formatting

### 3. Download Limits Test
1. Create multiple documents with a free account
2. Verify limits are enforced (2 session plans, 2 schemes)
3. Test that premium accounts have unlimited access

## Key Features Now Working

✅ **Session Authentication:** Users must login to access creation pages
✅ **Proper DOCX Generation:** Documents download as formatted Word files
✅ **Download Limits:** Free users limited to 2 of each document type
✅ **Admin Panel:** Admin can manage users and view statistics
✅ **User Registration:** New users can register and login
✅ **Session Management:** Sessions expire after 24 hours

## Admin Access

- **Phone:** +250789751597
- **Password:** admin123
- **Admin Panel:** Visit `/admin-final.html` after login

## Troubleshooting

### If Documents Still Download as .txt:
1. Check PythonAnywhere error logs
2. Verify `python-docx` is installed
3. Check file permissions in PythonAnywhere

### If Authentication Doesn't Work:
1. Clear browser cache and localStorage
2. Check browser console for JavaScript errors
3. Verify API_BASE URL in config.js

### If CORS Errors Occur:
1. Update the origins list in `main_production.py`
2. Add your exact GitHub Pages URL
3. Restart the PythonAnywhere web app

## File Structure After Deployment

```
Frontend (GitHub Pages):
├── index.html (updated)
├── wizard.html (updated)
├── scheme-wizard.html (updated)
├── auth-fixed.js (new)
├── config.js (updated)
└── other existing files...

Backend (PythonAnywhere):
├── main_production.py (new - use as main.py)
├── document_generator.py (existing)
├── models.py (existing)
├── schemas.py (existing)
└── rtb_planner.db (auto-created)
```

## Next Steps

1. Upload `main_production.py` to PythonAnywhere
2. Update GitHub repository with frontend changes
3. Test the complete system
4. Monitor for any issues and check logs

The system should now properly enforce authentication and generate professional DOCX documents instead of text files.