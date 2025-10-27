# GitHub Commit & Push Guide

## Prerequisites
- Git installed on your Windows machine
- GitHub account set up
- Repository created on GitHub (e.g., `rtb-document-planner`)

---

## Step 1: Initialize Git Repository Locally

Open **Git Bash** (or PowerShell) in your project directory:

```bash
cd "C:\Users\PC\Music\Scheme of work and session plan planner"
```

Initialize git:
```bash
git init
```

---

## Step 2: Create .gitignore File

Create a `.gitignore` file to exclude unnecessary files:

```bash
# Create .gitignore
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*.so
.Python
env/
venv/
*.egg-info/
dist/
build/

# Database
*.db
*.sqlite
*.sqlite3

# Environment variables
.env
.env.local
.env.*.local

# Temporary files
*.tmp
*.log
temp/
tmp/

# Test files and reports
TEST_*.docx
test_*.py
.coverage
htmlcov/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
EOF
```

---

## Step 3: Configure Git User (First Time Only)

```bash
git config --global user.email "your_email@example.com"
git config --global user.name "Your Name"
```

---

## Step 4: Add Remote Repository

On GitHub, create a repository named `rtb-document-planner`, then:

```bash
git remote add origin https://github.com/YOUR_USERNAME/rtb-document-planner.git
```

---

## Step 5: Stage All Files

```bash
git add .
```

Or stage specific directories:
```bash
git add PRODUCTION_READY/
```

---

## Step 6: Verify Changes

Check what will be committed:

```bash
git status
```

You should see **green** lines for staged files (ready to commit).

---

## Step 7: Create Initial Commit

```bash
git commit -m "Initial commit: RTB Document Planner - Production Ready

- Backend: Flask API with CORS for Cloudflare Pages
- Document Generation: Fixed RTB template structure (no more unstructured text)
- Frontend: HTML/JS with dynamic API URL detection
- Features: Session plans, Schemes of work, AI content generation
- Deployment: Ready for PythonAnywhere + Cloudflare Pages"
```

---

## Step 8: Push to GitHub

For the **first push**, use:

```bash
git branch -M main
git push -u origin main
```

For **subsequent pushes**:

```bash
git push origin main
```

---

## Step 9: Verify on GitHub

1. Go to https://github.com/YOUR_USERNAME/rtb-document-planner
2. You should see all your files committed
3. Verify the commit message in the history

---

## Making Future Changes

When you make changes and want to commit them:

```bash
# See what changed
git status

# Stage changes
git add PRODUCTION_READY/

# Commit with message
git commit -m "Feature: Description of what changed"

# Push to GitHub
git push origin main
```

---

## Recommended Commit Messages Format

Use descriptive commit messages following this pattern:

```
<Type>: <Short description>

<Detailed explanation if needed>
```

**Types:**
- `Fix:` - Bug fixes
- `Feature:` - New functionality
- `Docs:` - Documentation updates
- `Refactor:` - Code reorganization
- `Deploy:` - Deployment-related changes
- `Update:` - Dependency or configuration updates

**Examples:**
```bash
git commit -m "Fix: Document generation produces proper RTB tables

- Fixed fallback logic that was creating plain text
- Ensured template-first approach always maintains format
- Added proper margin and font settings"
```

```bash
git commit -m "Feature: Add AI content generation for session plans"
```

```bash
git commit -m "Update: CORS configuration for PythonAnywhere deployment"
```

---

## Cleanup: Remove Test Files Before Commit

Before committing, clean up test/temporary files:

```bash
# List test files that will be ignored
git status | grep TEST_

# They should NOT appear in git status if .gitignore is working
```

---

## Troubleshooting

**"fatal: not a git repository"**
- Make sure you ran `git init` in the correct directory
- Run `git status` to verify

**"Permission denied" when pushing**
- Generate GitHub Personal Access Token: Settings → Developer settings → Personal access tokens
- Use token instead of password when prompted

**Want to undo last commit?**
```bash
git reset --soft HEAD~1
```

**Want to see all commits?**
```bash
git log --oneline
```

**Want to undo all local changes and revert to GitHub version?**
```bash
git reset --hard origin/main
```
