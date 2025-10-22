@echo off
echo ========================================
echo RTB DOCUMENT PLANNER - FINAL VERIFICATION
echo ========================================
echo.

echo Testing Backend API...
powershell -Command "try { $api = Invoke-RestMethod -Uri 'https://leonardus437.pythonanywhere.com/'; Write-Host 'Backend Status:' $api.status; Write-Host 'Version:' $api.version; Write-Host 'Session Plans:' $api.session_plans_count } catch { Write-Host 'Backend Error:' $_.Exception.Message }"
echo.

echo Testing Frontend Deployment...
powershell -Command "try { $site = Invoke-WebRequest -Uri 'https://tuyisingize750.github.io/rtb-document-planner/' -UseBasicParsing; Write-Host 'Site Status: OK (200)' } catch { Write-Host 'Site Error:' $_.Exception.Message }"
echo.

echo Testing Bulletproof Wizard...
powershell -Command "try { $wizard = Invoke-WebRequest -Uri 'https://tuyisingize750.github.io/rtb-document-planner/wizard-fixed.html' -UseBasicParsing; Write-Host 'Wizard Status: OK (200)' } catch { Write-Host 'Wizard Error:' $_.Exception.Message }"
echo.

echo ========================================
echo TESTING INSTRUCTIONS:
echo 1. Visit: https://tuyisingize750.github.io/rtb-document-planner/
echo 2. Click "Create Session Plan" 
echo 3. Fill out the form and submit
echo 4. Login: +250789751597 / admin123
echo ========================================
pause