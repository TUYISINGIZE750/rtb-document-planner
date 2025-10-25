# Cloudflare Pages Deployment Guide

## Cloudflare Build Settings

### Framework preset
**Select**: `None`

### Build command
**Leave empty** (no build command needed)

### Build output directory
**Enter**: `PRODUCTION_READY/frontend`

### Root directory (advanced)
**Leave as**: `/` (default)

### Environment variables (advanced)
**Add this variable**:
- **Variable name**: `API_BASE`
- **Value**: `https://leonardus437.pythonanywhere.com`

---

## Step-by-Step Deployment

### 1. Connect GitHub Repository
- Go to Cloudflare Dashboard
- Click **Pages** → **Create a project**
- Select **Connect to Git**
- Choose your repository: `rtb-document-planner`
- Click **Begin setup**

### 2. Configure Build Settings
```
Framework preset: None
Build command: (leave empty)
Build output directory: PRODUCTION_READY/frontend
Root directory: /
```

### 3. Add Environment Variable
Click **Environment variables (advanced)**
```
Variable name: API_BASE
Value: https://leonardus437.pythonanywhere.com
```

### 4. Deploy
- Click **Save and Deploy**
- Wait 2-3 minutes for deployment
- Your site will be live at: `https://rtb-document-planner.pages.dev`

---

## Why These Settings?

1. **Framework preset: None** - This is a static HTML/CSS/JS site, no framework needed

2. **Build command: empty** - No compilation or build process required

3. **Build output directory: PRODUCTION_READY/frontend** - This folder contains all your HTML, CSS, JS files ready to serve

4. **Root directory: /** - Deploy from repository root

5. **API_BASE environment variable** - Points frontend to your PythonAnywhere backend API

---

## After Deployment

### Update config.js (if needed)
If API calls fail, update `PRODUCTION_READY/frontend/config.js`:
```javascript
const API_BASE = 'https://leonardus437.pythonanywhere.com';
```

### Custom Domain (Optional)
1. Go to your Cloudflare Pages project
2. Click **Custom domains**
3. Add your domain (e.g., `rtb-planner.com`)
4. Follow DNS setup instructions

---

## Troubleshooting

### Issue: 404 errors
**Solution**: Make sure build output directory is `PRODUCTION_READY/frontend` (not just `frontend`)

### Issue: API calls fail
**Solution**: Check that API_BASE environment variable is set correctly

### Issue: Login doesn't work
**Solution**: Verify PythonAnywhere backend is running at https://leonardus437.pythonanywhere.com

---

## Quick Summary

```
Framework: None
Build command: (empty)
Output directory: PRODUCTION_READY/frontend
Environment variable: API_BASE = https://leonardus437.pythonanywhere.com
```

**That's it!** Your site will be live in 2-3 minutes. 🚀
