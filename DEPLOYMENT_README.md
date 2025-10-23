# RTB Document Planner - Deployment Guide

## ✅ What's Been Fixed

### 1. Professional Document Generation
- **Session Plans**: Now match the official RTB template structure exactly
  - 23-row table with proper cell merging
  - All required sections: Introduction, Development/Body, Conclusion, Assessment, Evaluation
  - Professional formatting with Calibri font, proper spacing
  
- **Schemes of Work**: Follow official RTB format
  - 9-column table structure
  - Headers: Weeks, Learning Outcome, Duration, Indicative Content, etc.
  - Landscape A4 orientation

### 2. Backend Updates
- Created `rtb_professional_generator.py` with functions:
  - `generate_rtb_session_plan(data)` - Generates RTB-compliant session plans
  - `generate_rtb_scheme_of_work(data)` - Generates RTB-compliant schemes
- Updated `main_minimal.py` to use the professional generator
- Documents now download with proper names: `RTB_Session_Plan_X.docx`

### 3. GitHub Pages Configuration
- Root `index.html` redirects to `frontend/index.html`
- GitHub Actions workflow configured for automatic deployment
- CORS configured to allow GitHub Pages origin

## 🚀 Deployment Steps

### Option 1: Automatic Deployment (Recommended)
```bash
# Run the deployment script
deploy_github_pages.bat
```

### Option 2: Manual Deployment
```bash
# Navigate to project directory
cd "c:\Users\PC\Music\Scheme of work and session plan planner"

# Add all changes
git add .

# Commit changes
git commit -m "Deploy: Professional RTB document generator"

# Push to GitHub
git push origin main
```

## 🌐 Access Your Application

After deployment (1-2 minutes), your application will be available at:
**https://tuyisingize750.github.io/Scheme-of-work-and-session-plan-planner/**

## 📋 Testing Checklist

After deployment, test the following:

1. **Login System**
   - [ ] Login with test credentials: +250796014803 / teacher123
   - [ ] User info displays correctly

2. **Session Plan Generation**
   - [ ] Fill out all required fields
   - [ ] Click "Generate Session Plan"
   - [ ] Document downloads automatically
   - [ ] Open in Microsoft Word
   - [ ] Verify structure matches RTB template

3. **Scheme of Work Generation**
   - [ ] Fill out scheme details
   - [ ] Add multiple weeks
   - [ ] Generate and download
   - [ ] Verify 9-column table structure

## 🔧 Backend Configuration

The frontend is configured to use:
```javascript
const API_BASE = 'https://leonardus437.pythonanywhere.com';
```

Make sure your PythonAnywhere backend has:
1. `rtb_professional_generator.py` uploaded
2. `main_minimal.py` updated with the new imports
3. CORS configured for GitHub Pages origin

## 📁 File Structure

```
/
├── index.html (redirects to frontend)
├── frontend/
│   ├── index.html (login page)
│   ├── wizard.html (session plan creator)
│   ├── scheme-wizard.html (scheme creator)
│   └── admin.html (admin panel)
├── backend/
│   ├── main_minimal.py (Flask API)
│   ├── rtb_professional_generator.py (NEW!)
│   └── requirements.txt
└── RTB Templates/ (reference templates)
    ├── TUYISINGIZE LEONARD_SESSION PLAN_S4F3.docx
    └── CSAPA 301 Scheme of work.docx
```

## 🎯 Key Features

1. **RTB-Compliant Documents**
   - Exact match to official templates
   - Professional formatting
   - Proper table structures

2. **User Authentication**
   - Phone number + password login
   - Session management
   - Admin panel for user activation

3. **Easy Document Generation**
   - Step-by-step wizards
   - Form validation
   - Instant download

## 🐛 Troubleshooting

### Documents not downloading?
- Check browser console for errors
- Verify backend is running
- Check CORS configuration

### Document structure incorrect?
- Verify `rtb_professional_generator.py` is uploaded to backend
- Check that `main_minimal.py` imports the new generator
- Restart backend server

### GitHub Pages not updating?
- Check GitHub Actions tab for deployment status
- Clear browser cache
- Wait 2-3 minutes after push

## 📞 Support

For issues or questions:
1. Check the browser console (F12)
2. Review backend logs on PythonAnywhere
3. Verify all files are committed and pushed

## 🎉 Success Indicators

You'll know everything is working when:
- ✅ Login page loads on GitHub Pages
- ✅ Can login with test credentials
- ✅ Session plan wizard opens
- ✅ Documents download automatically
- ✅ Documents open correctly in Microsoft Word
- ✅ Document structure matches RTB templates exactly
