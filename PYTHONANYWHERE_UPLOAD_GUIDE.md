# PythonAnywhere Upload Guide - Step by Step

## Your Current PythonAnywhere Structure

Your backend files are currently in:
```
/home/leonardus437/rtb-document-planner/
```

## Files to Upload from Local Computer

From your local folder:
```
C:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\backend\
```

Upload these files:
1. `main.py` (UPDATED - has Cloudflare CORS)
2. `facilitation_content_generator.py` (UPDATED - simplified content)
3. `content_formatter.py`
4. `rtb_template_filler_exact.py`
5. `document_generator.py`

---

## Step-by-Step Upload Process

### Method 1: Via PythonAnywhere Web Interface (EASIEST)

#### Step 1: Open Files Tab
1. Login to PythonAnywhere
2. Click **Files** tab at top

#### Step 2: Navigate to Your Project
1. You'll see: `/home/leonardus437/`
2. Click on folder: `rtb-document-planner`
3. You should now be in: `/home/leonardus437/rtb-document-planner/`

#### Step 3: Upload Files One by One
For each file:

1. Click **Upload a file** button (top right)
2. Click **Choose File**
3. Navigate to: `C:\Users\PC\Music\Scheme of work and session plan planner\PRODUCTION_READY\backend\`
4. Select file (e.g., `main.py`)
5. Click **Upload**
6. If file exists, click **Replace** to overwrite

Repeat for all 5 files.

#### Step 4: Verify Files Uploaded
In `/home/leonardus437/rtb-document-planner/`, you should see:
- ✅ main.py (updated today)
- ✅ facilitation_content_generator.py (updated today)
- ✅ content_formatter.py
- ✅ rtb_template_filler_exact.py
- ✅ document_generator.py
- ✅ rtb_session_plan_template.docx
- ✅ rtb_scheme_template.docx
- ✅ rtb_planner.db

---

### Method 2: Via Git Pull (FASTER)

#### Step 1: Open Bash Console
1. Click **Consoles** tab
2. Click **Bash**

#### Step 2: Navigate and Pull
```bash
cd ~/rtb-document-planner
git pull origin main
```

#### Step 3: Copy Files to Root
```bash
cp PRODUCTION_READY/backend/*.py .
```

This copies all Python files from PRODUCTION_READY/backend to your project root.

---

## After Upload: Reload Web App

### Step 1: Go to Web Tab
1. Click **Web** tab at top
2. Find your app: `leonardus437.pythonanywhere.com`

### Step 2: Reload
1. Scroll down to **Reload** button (big green button)
2. Click **Reload leonardus437.pythonanywhere.com**
3. Wait for green checkmark (5-10 seconds)

### Step 3: Verify
Open new browser tab:
```
https://leonardus437.pythonanywhere.com/
```

Should return:
```json
{
  "message": "RTB Document Planner API",
  "status": "online",
  "version": "2.0"
}
```

---

## Test Cloudflare Connection

### Step 1: Open Cloudflare Site
```
https://rtb-document-planner.pages.dev
```

### Step 2: Open Browser Console (F12)
Look for:
```
✅ config.js loaded
✅ API connection successful
```

### Step 3: Test Login
- Phone: `+250789751597`
- Password: `admin123`
- Should login successfully

---

## File Locations Summary

### Local Computer:
```
C:\Users\PC\Music\Scheme of work and session plan planner\
  └── PRODUCTION_READY\
      └── backend\
          ├── main.py ← Upload this
          ├── facilitation_content_generator.py ← Upload this
          ├── content_formatter.py ← Upload this
          ├── rtb_template_filler_exact.py ← Upload this
          └── document_generator.py ← Upload this
```

### PythonAnywhere:
```
/home/leonardus437/
  └── rtb-document-planner/
      ├── main.py ← Files go here
      ├── facilitation_content_generator.py
      ├── content_formatter.py
      ├── rtb_template_filler_exact.py
      ├── document_generator.py
      ├── rtb_session_plan_template.docx
      ├── rtb_scheme_template.docx
      └── rtb_planner.db
```

---

## Quick Checklist

- [ ] Login to PythonAnywhere
- [ ] Go to Files tab
- [ ] Navigate to `rtb-document-planner` folder
- [ ] Upload 5 Python files from `PRODUCTION_READY\backend`
- [ ] Go to Web tab
- [ ] Click Reload button
- [ ] Test API: https://leonardus437.pythonanywhere.com/
- [ ] Test Cloudflare site
- [ ] Test login and document generation

---

## Need Help?

If files are in wrong location, use Bash console:
```bash
cd ~/rtb-document-planner
ls -la
```

This shows all files in your project folder.

**Done!** 🎉
