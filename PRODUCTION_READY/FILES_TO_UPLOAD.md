# Files to Upload for Deployment

## BACKEND → PythonAnywhere
**Location**: `/home/leonardus437/rtb-document-planner/`

### Core Application Files
```
✓ main.py                                 (54 KB) - Main Flask application
✓ requirements.txt                        (208 B) - Python dependencies
✓ init_db.py                              (1.26 KB) - Database initialization script
```

### Document Generation Modules
```
✓ document_generator.py                   (17 KB) - DOCX/PDF document generation
✓ ai_content_generator.py                 (19 KB) - AI-powered content generation
✓ facilitation_content_generator.py       (19 KB) - Facilitation technique content
✓ content_formatter.py                    (7.39 KB) - Content formatting utilities
✓ enhanced_document_generator.py          (22 KB) - Enhanced document features
```

### RTB Templates (CRITICAL!)
```
✓ RTB Templates/RTB Session plan template.docx    (109.73 MB)
✓ RTB Templates/Scheme of work.docx               (75.18 MB)
```

**NOTE**: Create folder `RTB Templates/` inside `/home/leonardus437/rtb-document-planner/` before uploading template files

---

## FRONTEND → Cloudflare Pages
**Source Directory**: `PRODUCTION_READY/frontend/`

### Main HTML Files
```
✓ index.html                              (21.94 KB) - Landing page
✓ login.html                              (10.66 KB) - Login page
✓ register.html                           (6.62 KB) - Registration page
✓ teacher-dashboard.html                  (18.36 KB) - Teacher dashboard
✓ admin.html                              (10.29 KB) - Admin panel
✓ admin-final.html                        (310 B) - Admin redirect
✓ scheme-wizard.html                      (30.63 KB) - Scheme wizard
✓ wizard.html                             (15.06 KB) - Session plan wizard
```

### JavaScript Files
```
✓ config.js                               (1.14 KB) - API configuration (UPDATED)
✓ auth.js                                 (15.56 KB) - Authentication functions
✓ subscription-modal.js                   (15.38 KB) - Subscription modal
✓ subscription-tracker.js                 (6.18 KB) - Subscription tracking
```

### CSS Files
```
✓ subscription-modal.css                  (8.13 KB) - Modal styling
```

---

## DEPLOYMENT FILES (Keep locally, refer to)

```
✓ CLOUDFLARE_PYTHONANYWHERE_DEPLOYMENT.md         - Complete deployment guide
✓ FILES_TO_UPLOAD.md                              - This file
✓ PYTHONANYWHERE_WSGI_FILE.txt                    - WSGI configuration
```

---

## UPLOAD SUMMARY

### PythonAnywhere
- **Total Files**: 10 required
- **Total Size**: ~150 MB (mostly templates)
- **Upload Method**: Web interface files browser
- **Database**: Auto-created with init_db.py

### Cloudflare Pages
- **Total Files**: 12 required  
- **Total Size**: ~150 KB
- **Upload Method**: GitHub integration or drag-and-drop
- **Build**: None required (static files)

---

## UPLOAD CHECKLIST

### Backend Upload ✓
- [ ] Create `/home/leonardus437/rtb-document-planner/` folder
- [ ] Upload all .py files (main.py, document_generator.py, etc.)
- [ ] Upload requirements.txt
- [ ] Create `RTB Templates/` subfolder
- [ ] Upload template .docx files to subfolder
- [ ] Run: `pip install -r requirements.txt`
- [ ] Run: `python init_db.py`
- [ ] Configure WSGI file (see PYTHONANYWHERE_WSGI_FILE.txt)
- [ ] Click Reload in PythonAnywhere Web tab
- [ ] Test: https://leonardus437.pythonanywhere.com/

### Frontend Upload ✓
- [ ] Connect GitHub to Cloudflare Pages OR
- [ ] Prepare PRODUCTION_READY/frontend/ for upload
- [ ] Upload all .html files
- [ ] Upload all .js files
- [ ] Upload all .css files
- [ ] Configure custom domain (optional)
- [ ] Wait for deployment (auto-redeploy if using GitHub)
- [ ] Test: https://your-domain.pages.dev

---

## QUICK START AFTER UPLOAD

1. **Test Backend API**:
   ```
   Visit: https://leonardus437.pythonanywhere.com/
   Expected: {"message":"RTB Document Planner API is running"}
   ```

2. **Test Frontend**:
   ```
   Visit: https://your-domain.pages.dev
   Open Browser Console (F12)
   Look for: ✅ config.js loaded
   Look for: ✅ API connection successful
   ```

3. **Test Integration**:
   ```
   - Try to register an account
   - Try to log in
   - Create a session plan
   - Download the document
   - Verify file is valid DOCX
   ```

---

## TROUBLESHOOTING

**Backend not responding?**
- Check PythonAnywhere error log
- Verify WSGI file saved correctly
- Ensure templates folder exists
- Run init_db.py again

**Frontend loads blank?**
- Check browser console for JavaScript errors
- Verify API URL in config.js
- Check CORS errors in console
- Verify all HTML/JS/CSS files uploaded

**API timeout?**
- Increase timeout in PythonAnywhere Web settings
- Check for long-running queries
- Monitor error logs

**Documents not generating?**
- Verify RTB template files uploaded
- Check file paths in document_generator.py
- Test with simple content first

---

**Last Updated**: October 26, 2025
