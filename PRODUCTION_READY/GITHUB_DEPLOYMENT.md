# GitHub Deployment Guide

## Quick Commit & Push

### Windows Command Prompt

```bash
cd C:\Users\PC\Music\Scheme of work and session plan planner
git add -A
git commit -m "Deploy: Enhanced document formatting, smart APA references, and admin panel improvements"
git push origin main
```

### Windows PowerShell

```powershell
Set-Location "C:\Users\PC\Music\Scheme of work and session plan planner"
git add -A
git commit -m "Deploy: Enhanced document formatting, smart APA references, and admin panel improvements"
git push origin main
```

### Git Bash

```bash
cd "C:\Users\PC\Music\Scheme of work and session plan planner"
git add -A
git commit -m "Deploy: Enhanced document formatting, smart APA references, and admin panel improvements"
git push origin main
```

## What Gets Deployed

### To GitHub
- ✅ All backend files from `PRODUCTION_READY/backend/`
- ✅ All frontend files from `PRODUCTION_READY/frontend/`
- ✅ Documentation files
- ✅ Configuration files

### Automatic Cloudflare Deployment
Once pushed to GitHub `main` branch:
1. GitHub triggers webhook to Cloudflare
2. Cloudflare Pages automatically builds and deploys
3. Live at: https://rtb-document-planner.pages.dev

## Verification

After push, check:

```bash
# See recent commits
git log --oneline -5

# Check remote status
git status
```

Expected output:
```
On branch main
Your branch is ahead of 'origin/main' by 1 commit.
(use "git push" to publish your local commits)
```

After push:
```
On branch main
Your branch is up to date with 'origin/main'.
```

## Check Cloudflare Deployment

1. Go to: https://dash.cloudflare.com/
2. Select: rtb-document-planner
3. Go to: Pages → Deployments
4. Should show new deployment with status "Success"

## Files Changed

Run this to see what changed:

```bash
git diff --name-only HEAD~1
```

This shows files modified since last commit.

## Rollback (if needed)

If something went wrong:

```bash
# See commit history
git log --oneline -10

# Revert to previous commit (replace HASH with actual commit hash)
git revert HASH

# Push the revert
git push origin main
```

## Tips

- Always test locally before pushing
- Use descriptive commit messages
- Push during off-peak hours if possible
- Check Cloudflare dashboard for deployment status

---

**Status**: Ready to deploy to production! ✅
