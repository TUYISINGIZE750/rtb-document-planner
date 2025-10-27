# GitHub Setup Using CMD (Windows Command Prompt)

## No Git Bash Needed - Use Regular CMD!

The commands are **exactly the same** in CMD. Here's how to do it:

---

## Step 1: Open Command Prompt in Project Folder

1. **Navigate to your project folder** using File Explorer
2. **Hold SHIFT** and **right-click** in the folder (empty space)
3. Select **"Open command window here"** or **"Open PowerShell window here"**

(If you don't see this option, you can also open CMD and type:)
```cmd
cd "C:\Users\PC\Music\Scheme of work and session plan planner"
```

---

## Step 2: Initialize Git

In CMD, type:
```cmd
git init
```

Press **Enter**. You should see:
```
Initialized empty Git repository in C:\Users\PC\Music\Scheme of work and session plan planner\.git/
```

---

## Step 3: Configure Your Git User

Type these two commands (one at a time):

```cmd
git config --global user.email "your_email@gmail.com"
```

```cmd
git config --global user.name "Your Name"
```

**Replace** `your_email@gmail.com` and `Your Name` with your actual details.

---

## Step 4: Create .gitignore File

In CMD, type this entire block:

```cmd
(
echo __pycache__/
echo *.py[cod]
echo .Python
echo env/
echo venv/
echo *.db
echo *.sqlite
echo *.sqlite3
echo .env
echo .vscode/
echo .idea/
echo TEST_*.docx
echo test_*.py
) > .gitignore
```

This creates a `.gitignore` file that tells Git to ignore temporary/test files.

---

## Step 5: Add GitHub Remote

Go to **GitHub.com** and create a new repository called `rtb-document-planner`

Then in CMD, type (replace `YOUR_USERNAME` with your GitHub username):

```cmd
git remote add origin https://github.com/YOUR_USERNAME/rtb-document-planner.git
```

---

## Step 6: Stage All Files

In CMD, type:

```cmd
git add .
```

This prepares all files for commit (should be silent, no output).

---

## Step 7: Check What Will Be Committed

Type:

```cmd
git status
```

You should see **green** lines showing files ready to commit. If you see test files or `__pycache__`, the .gitignore isn't working (but proceed anyway).

---

## Step 8: Create First Commit

In CMD, type:

```cmd
git commit -m "Initial commit: RTB Document Planner production ready"
```

You should see output like:
```
[main (root-commit) abc1234] Initial commit: RTB Document Planner production ready
 45 files changed, 1000+ insertions(+)
 create mode 100644 ...
```

---

## Step 9: Set Branch Name & Push

Type:

```cmd
git branch -M main
```

Then push to GitHub:

```cmd
git push -u origin main
```

You'll be prompted for your **GitHub credentials**:
- **Username:** Your GitHub username
- **Password:** Your GitHub **Personal Access Token** (not your password!)

### Getting Your Personal Access Token

1. Go to GitHub.com → **Settings** (top right)
2. **Developer settings** → **Personal access tokens** → **Tokens (classic)**
3. Click **Generate new token (classic)**
4. Give it a name: `RTB Planner`
5. Check `repo` (full control of private repositories)
6. Scroll down, click **Generate token**
7. **Copy the token** (you won't see it again!)
8. Use this token as your password when Git asks

---

## Complete Command Sequence (Copy & Paste)

If you want to just copy-paste all at once, open CMD and run these one by one:

```cmd
cd "C:\Users\PC\Music\Scheme of work and session plan planner"
git init
git config --global user.email "your_email@gmail.com"
git config --global user.name "Your Name"
```

Then create .gitignore:
```cmd
(
echo __pycache__/
echo *.py[cod]
echo .Python
echo env/
echo venv/
echo *.db
echo *.sqlite
echo *.sqlite3
echo .env
echo .vscode/
echo .idea/
echo TEST_*.docx
echo test_*.py
) > .gitignore
```

Then continue:
```cmd
git remote add origin https://github.com/YOUR_USERNAME/rtb-document-planner.git
git add .
git status
git commit -m "Initial commit: RTB Document Planner production ready"
git branch -M main
git push -u origin main
```

---

## Expected Output at End

If everything worked, you should see:
```
Enumerating objects: 45, done.
Counting objects: 100% (45/45), done.
...
 * [new branch]      main -> main
Branch 'main' set up to track remote branch 'main' from 'origin'.
```

Then go to `https://github.com/YOUR_USERNAME/rtb-document-planner` and you'll see all your files uploaded! ✅

---

## Troubleshooting

**"git is not recognized"**
- Git not installed. Install from https://git-scm.com/
- Restart CMD after installing

**"fatal: not a git repository"**
- You're in the wrong folder
- Run: `cd "C:\Users\PC\Music\Scheme of work and session plan planner"`

**"remote origin already exists"**
- You already ran the remote add command
- Skip that step

**"Please tell me who you are" error**
- Didn't run the git config commands
- Run them again with your email and name

**Can't push - authentication fails**
- Make sure you're using **Personal Access Token**, not your password
- Or use: `git config --global credential.helper wincred` and save token

---

## Next: PythonAnywhere Upload

Once GitHub is done, follow `PYTHONANYWHERE_FILES_TO_UPLOAD.md` for uploading to PythonAnywhere.
