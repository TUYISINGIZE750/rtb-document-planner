# 🚀 Render.com Deployment Guide

## Step 1: Sign Up for Render
1. Go to: https://render.com
2. Click **"Get Started"**
3. Sign up with **GitHub** (easiest option)
4. Authorize Render to access your GitHub repositories

## Step 2: Create New Web Service
1. Click **"New +"** button (top right)
2. Select **"Web Service"**
3. Click **"Connect a repository"**
4. Find and select: **rtb-document-planner**
5. Click **"Connect"**

## Step 3: Configure Service
Fill in these settings:

**Name:** `rtb-api` (or any name you like)

**Region:** `Oregon (US West)` (free tier available)

**Branch:** `main`

**Root Directory:** Leave empty

**Runtime:** `Python 3`

**Build Command:**
```
pip install -r PRODUCTION_READY/backend/requirements.txt
```

**Start Command:**
```
cd PRODUCTION_READY/backend && python main.py
```

## Step 4: Add Environment Variables
Click **"Advanced"** → **"Add Environment Variable"**

Add this variable:
- **Key:** `GEMINI_API_KEY`
- **Value:** `AIzaSyDuEdAygLcQ4aEuq2Vqj-9Kl0qZpJcg3A8`

## Step 5: Select Free Plan
- Scroll down to **"Instance Type"**
- Select: **"Free"** (512 MB RAM, 0.1 CPU)
- Click **"Create Web Service"**

## Step 6: Wait for Deployment
- Render will start building your app (takes 2-5 minutes)
- Watch the logs in real-time
- Wait for: **"Your service is live 🎉"**

## Step 7: Get Your API URL
- After deployment, you'll see your URL at the top
- Example: `https://rtb-api.onrender.com`
- Copy this URL!

## Step 8: Update Frontend Config
1. Go to your Cloudflare Pages dashboard
2. Go to: **Settings** → **Environment Variables**
3. Update `API_BASE_URL` to your new Render URL
4. Or update `config.js` in your frontend code:
```javascript
const API_BASE = 'https://rtb-api.onrender.com';
```

## Step 9: Test Your API
Open in browser:
```
https://rtb-api.onrender.com/
```

Should see:
```json
{
  "message": "RTB API Online",
  "status": "ok",
  "cors": "enabled"
}
```

## Step 10: Test Full System
1. Go to: https://rtb-document-planner.pages.dev/
2. Register/Login
3. Create a session plan
4. Download should work! 🎉

## ✅ Benefits of Render vs PythonAnywhere
- ✅ 512MB RAM (vs limited on PA)
- ✅ No disk space issues
- ✅ Auto-deploy from GitHub
- ✅ Better performance
- ✅ Free SSL certificate
- ✅ Custom domain support

## 🔧 Troubleshooting

### Build fails with "requirements.txt not found"
**Fix:** Check Build Command path is correct:
```
pip install -r PRODUCTION_READY/backend/requirements.txt
```

### App crashes on start
**Fix:** Check Start Command:
```
cd PRODUCTION_READY/backend && python main.py
```

### Database not found
**Fix:** Render will create a fresh database automatically on first run

### CORS errors
**Fix:** Update frontend config.js with new Render URL

## 📝 Notes
- Free tier sleeps after 15 minutes of inactivity
- First request after sleep takes ~30 seconds to wake up
- Upgrade to paid plan ($7/month) for always-on service
- Database persists even on free tier

## 🎯 Your URLs After Deployment
- **Backend API:** https://rtb-api.onrender.com
- **Frontend:** https://rtb-document-planner.pages.dev (already deployed)
- **Admin:** https://rtb-document-planner.pages.dev/admin.html

## 🚀 Auto-Deploy
Every time you push to GitHub main branch, Render will automatically:
1. Pull latest code
2. Rebuild the app
3. Deploy new version
4. Zero downtime!
