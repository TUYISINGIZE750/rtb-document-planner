# ✅ Render Deployment Testing Checklist

## 🎯 Your Service Details
- **Service Name:** rtb-document-planner
- **Service ID:** srv-d40umep5pdvs73deja8g
- **Expected URL:** https://rtb-document-planner.onrender.com
- **Frontend:** https://rtb-document-planner.pages.dev

---

## Phase 1: Deploy Backend on Render ⏳

### Step 1.1: Trigger Deploy
- [ ] Go to Render dashboard
- [ ] Click **"Manual Deploy"** button
- [ ] Select **"Deploy latest commit"** (e7c5c40)
- [ ] Click **"Deploy"**

### Step 1.2: Monitor Deployment (2-4 minutes)
Watch for these success messages:
- [ ] `==> Installing Python version 3.13.4...` ✅
- [ ] `Successfully installed sqlalchemy-2.0.36` ✅
- [ ] `==> Build successful 🎉` ✅
- [ ] `==> Your service is live 🎉` ✅

### Step 1.3: Copy Your Live URL
- [ ] Copy the URL from top of Render dashboard
- [ ] Example: `https://rtb-document-planner.onrender.com`

---

## Phase 2: Test Backend API 🧪

### Test 2.1: Root Endpoint
Open in browser:
```
https://rtb-document-planner.onrender.com/
```

**Expected Response:**
```json
{
  "message": "RTB API Online",
  "status": "ok",
  "cors": "enabled"
}
```
- [ ] ✅ API responds correctly

### Test 2.2: Stats Endpoint
```
https://rtb-document-planner.onrender.com/api/stats
```

**Expected Response:**
```json
{
  "total_users": 0,
  "active_users": 0,
  "total_documents": 0
}
```
- [ ] ✅ Stats endpoint works

### Test 2.3: CORS Headers
Open browser console (F12) and run:
```javascript
fetch('https://rtb-document-planner.onrender.com/')
  .then(r => r.json())
  .then(d => console.log('✅ CORS working:', d))
  .catch(e => console.error('❌ CORS error:', e));
```
- [ ] ✅ No CORS errors

---

## Phase 3: Update Frontend (Already Done!) ✅

The frontend config has been updated automatically:
- [x] Updated `config.js` to use Render URL
- [x] Committed to GitHub (22642d7)
- [x] Cloudflare Pages will auto-deploy in 1-2 minutes

---

## Phase 4: Test Full System End-to-End 🎯

### Test 4.1: User Registration
1. Go to: https://rtb-document-planner.pages.dev/register.html
2. Register a new test account:
   - Username: `test_teacher_001`
   - Email: `test@example.com`
   - Password: `Test123!`
3. Check browser console for API calls

- [ ] ✅ Registration successful
- [ ] ✅ No console errors

### Test 4.2: User Login
1. Go to: https://rtb-document-planner.pages.dev/login.html
2. Login with test account
3. Should redirect to wizard

- [ ] ✅ Login successful
- [ ] ✅ Redirected to wizard

### Test 4.3: Create Session Plan (CRITICAL TEST!)
1. Fill in session plan form:
   - **Module:** Computer Programming
   - **Unit:** Introduction to Python
   - **Lesson:** Variables and Data Types
   - **Duration:** 90 minutes
   - **Facilitation Technique:** Group Discussion
2. Click **"Generate Session Plan"**
3. Wait for AI generation (10-15 seconds)
4. Document should auto-download

- [ ] ✅ Form submission works
- [ ] ✅ AI content generated
- [ ] ✅ Document downloads successfully
- [ ] ✅ No "write error" or disk space errors

### Test 4.4: Open Downloaded Document
1. Open the downloaded `.docx` file
2. Check formatting:
   - [ ] ✅ Bookman Old Style 12pt font
   - [ ] ✅ RTB logo present
   - [ ] ✅ All fields filled correctly
   - [ ] ✅ AI-generated content is professional

### Test 4.5: Create Scheme of Work
1. Go to scheme wizard
2. Fill in scheme details
3. Generate and download

- [ ] ✅ Scheme downloads successfully
- [ ] ✅ Formatting correct

---

## Phase 5: Admin Panel Test 👨‍💼

### Test 5.1: Create Admin User
SSH into Render or use their shell:
```bash
cd PRODUCTION_READY/backend
python create_admin.py
```

Or manually via API:
```bash
curl -X POST https://rtb-document-planner.onrender.com/api/register \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","email":"admin@rtb.com","password":"Admin123!"}'
```

Then activate via database or API.

- [ ] ✅ Admin user created

### Test 5.2: Admin Login
1. Go to: https://rtb-document-planner.pages.dev/admin.html
2. Login with admin credentials
3. Check user list

- [ ] ✅ Admin panel loads
- [ ] ✅ Can see all users
- [ ] ✅ Can activate/deactivate users

---

## Phase 6: Performance & Monitoring 📊

### Test 6.1: Response Times
- [ ] Root endpoint: < 500ms
- [ ] Registration: < 1s
- [ ] Document generation: < 20s
- [ ] Download: < 5s

### Test 6.2: Free Tier Behavior
- [ ] Service sleeps after 15 min inactivity
- [ ] First request after sleep: ~30s wake time
- [ ] Subsequent requests: fast

### Test 6.3: Database Persistence
- [ ] Create user, wait 1 hour, login again
- [ ] User data persists ✅

---

## 🚨 Troubleshooting

### If Backend Deploy Fails:
1. Check Render logs for errors
2. Verify `requirements.txt` has `sqlalchemy==2.0.36`
3. Check environment variable `GEMINI_API_KEY` is set

### If Frontend Can't Connect:
1. Check browser console for CORS errors
2. Verify `config.js` has correct Render URL
3. Wait 2 minutes for Cloudflare Pages to redeploy

### If Downloads Fail:
1. Check Render logs during download attempt
2. Verify `/tmp` directory has space (should be fine on Render)
3. Check document generation logs

### If AI Generation Fails:
1. Verify `GEMINI_API_KEY` environment variable
2. Check Render logs for API errors
3. Test with simple content first

---

## 🎉 Success Criteria

All these must pass:
- [x] Backend deployed on Render
- [ ] API endpoints respond correctly
- [ ] Frontend connects to backend
- [ ] User registration works
- [ ] User login works
- [ ] Session plan generates and downloads
- [ ] Scheme of work generates and downloads
- [ ] No disk space errors
- [ ] No CORS errors
- [ ] Documents have correct formatting

---

## 📝 Final Notes

**If ALL tests pass:**
🎉 **Your RTB Document Planner is LIVE and WORKING!**

**Your Live URLs:**
- Frontend: https://rtb-document-planner.pages.dev
- Backend API: https://rtb-document-planner.onrender.com
- Admin Panel: https://rtb-document-planner.pages.dev/admin.html

**Share with teachers:**
"Visit https://rtb-document-planner.pages.dev to create professional RTB-compliant session plans and schemes of work!"

---

## 🔄 Auto-Deploy Setup (Already Active!)

Every time you push to GitHub:
1. Render auto-deploys backend (2-3 min)
2. Cloudflare auto-deploys frontend (1-2 min)
3. Zero downtime!

**Test auto-deploy:**
- Make a small change to README.md
- Push to GitHub
- Watch both services redeploy automatically

---

## 📞 Support

If you encounter issues:
1. Check Render logs (real-time)
2. Check browser console (F12)
3. Check Cloudflare Pages deployment logs
4. Verify environment variables are set

**Common Issues:**
- Service sleeping: First request takes 30s (normal on free tier)
- CORS errors: Clear browser cache, check config.js
- Download fails: Check Render logs for disk/memory issues
