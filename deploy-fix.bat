@echo off
echo Deploying admin dashboard fix to Netlify...
cd frontend
git add .
git commit -m "Fix admin dashboard API endpoints - use production backend instead of localhost"
git push origin main
echo.
echo Deployment complete! Changes will be live in 1-2 minutes.
echo Visit: https://schemesession.netlify.app/admin-fixed.html
pause