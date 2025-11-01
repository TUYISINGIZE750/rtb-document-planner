# 🤖 Google Gemini AI Setup Guide

## Get FREE Gemini API Key

1. Go to: https://makersuite.google.com/app/apikey
2. Click: **"Get API Key"** or **"Create API Key"**
3. Select: **"Create API key in new project"**
4. Copy the API key (starts with `AIza...`)

## Add API Key to PythonAnywhere

### Method 1: Environment Variable (Recommended)

1. Go to PythonAnywhere **Web** tab
2. Scroll to **"Environment variables"** section
3. Click **"Add a new environment variable"**
4. Name: `GEMINI_API_KEY`
5. Value: Paste your API key (e.g., `AIzaSyC...`)
6. Click **"Save"**
7. Reload your web app

### Method 2: Direct in Code (Quick Test)

1. Open `ai_content_generator.py` on PythonAnywhere
2. Change line 6 from:
   ```python
   GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
   ```
   To:
   ```python
   GEMINI_API_KEY = 'YOUR_API_KEY_HERE'
   ```
3. Save and reload

## Test AI Generation

1. Go to: https://rtb-document-planner.pages.dev/
2. Create a session plan with:
   - Module: "CSAPA 301 - Computer Systems"
   - Topic: "Introduction to Operating Systems"
   - Learning Outcomes: "Identify different types of operating systems"
   - Indicative Contents: "Windows, Linux, macOS basics"
3. Click Generate
4. Download the document
5. Check if objectives, activities, and references are AI-generated!

## What AI Generates

✅ **Objectives** - 3-5 specific, measurable learning objectives
✅ **Facilitation Techniques** - Teaching methods for TVET
✅ **Learning Activities** - Detailed step-by-step activities (intro, development, conclusion)
✅ **Resources** - Materials and equipment needed
✅ **Assessment Details** - How to assess learning
✅ **References** - Relevant textbooks, manuals, online resources

## Free Tier Limits

- **1,500 requests per day** (more than enough!)
- **60 requests per minute**
- No credit card required

## Troubleshooting

**If AI doesn't work:**
- Check API key is correct
- Check environment variable is set
- Check error log on PythonAnywhere Web tab
- System will fall back to teacher's original input if AI fails

**If content is not good:**
- The AI prompt can be adjusted in `ai_content_generator.py`
- Edit the prompt to be more specific about what you want
