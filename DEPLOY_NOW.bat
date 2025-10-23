@echo off
echo ==========================================
echo    DEPLOYING LATEST VERSION NOW...
echo ==========================================

echo [1/3] Creating fixed files...

REM Create version-controlled index.html with cache busting
echo ^<!DOCTYPE html^>
echo ^<html^>
echo ^<head^>
echo     ^<title^>RTB Document Planner v2.1^</title^>
echo     ^<meta charset="UTF-8"^>
echo     ^<meta name="viewport" content="width=device-width, initial-scale=1.0"^>
echo     ^<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet"^>
echo     ^<style^>
echo         * { margin: 0; padding: 0; box-sizing: border-box; }
echo         body { font-family: Arial, sans-serif; background: linear-gradient(135deg, #667eea 0%%, #764ba2 100%%); min-height: 100vh; display: flex; align-items: center; justify-content: center; }
echo         .container { text-align: center; max-width: 800px; padding: 3rem; }
echo         h1 { color: white; font-size: 3rem; margin-bottom: 1rem; }
echo         p { color: rgba(255,255,255,0.9); font-size: 1.25rem; margin-bottom: 3rem; }
echo         .buttons { display: flex; gap: 2rem; justify-content: center; flex-wrap: wrap; }
echo         .btn { background: white; border: none; border-radius: 1rem; padding: 2rem 1.5rem; width: 250px; cursor: pointer; transition: all 0.3s; box-shadow: 0 4px 12px rgba(0,0,0,0.15); text-decoration: none; display: block; }
echo         .btn:hover { transform: translateY(-10px); box-shadow: 0 20px 40px rgba(0,0,0,0.3); }
echo         .btn i { font-size: 2.5rem; color: #6366f1; margin-bottom: 0.75rem; }
echo         .btn h2 { color: #1e293b; font-size: 1.25rem; margin-bottom: 0.25rem; }
echo         .btn p { color: #64748b; font-size: 0.8rem; margin: 0; }
echo         .user-menu { position: fixed; top: 2rem; right: 2rem; }
echo         .auth-btn { padding: 0.75rem 1.5rem; background: white; color: #333; text-decoration: none; border-radius: 2rem; font-weight: 600; margin: 0 0.5rem; }
echo         .logout-btn { background: #ef4444; color: white; border: none; padding: 0.5rem 1rem; border-radius: 0.5rem; cursor: pointer; }
echo         .user-info { background: white; padding: 1rem 1.5rem; border-radius: 2rem; box-shadow: 0 4px 12px rgba(0,0,0,0.15); display: flex; align-items: center; gap: 1rem; }
echo         .version { position: fixed; bottom: 1rem; left: 1rem; color: rgba(255,255,255,0.7); font-size: 0.8rem; }
echo     ^</style^>
echo ^</head^>
echo ^<body^>
echo     ^<div class="version"^>v2.1 - %date% %time%^</div^>
echo     ^<div class="user-menu" id="userMenu"^>
echo         ^<a href="#" onclick="showLogin()" class="auth-btn"^>^<i class="fas fa-sign-in-alt"^>^</i^> Login^</a^>
echo     ^</div^>
echo     ^<div class="container"^>
echo         ^<h1^>^<i class="fas fa-graduation-cap"^>^</i^> RTB Document Planner^</h1^>
echo         ^<p^>Professional TVET Session Plans ^& Schemes of Work Generator^</p^>
echo         ^<div class="buttons"^>
echo             ^<a href="wizard.html" class="btn" onclick="return checkAuth()"^>
echo                 ^<i class="fas fa-chalkboard-teacher"^>^</i^>
echo                 ^<h2^>Session Plan^</h2^>
echo                 ^<p^>Create RTB-formatted session plans^</p^>
echo             ^</a^>
echo             ^<a href="scheme.html" class="btn" onclick="return checkAuth()"^>
echo                 ^<i class="fas fa-clipboard-list"^>^</i^>
echo                 ^<h2^>Scheme of Work^</h2^>
echo                 ^<p^>Generate comprehensive schemes^</p^>
echo             ^</a^>
echo         ^</div^>
echo     ^</div^>
echo     ^<script^>
echo         const API_BASE = 'https://leonardus437.pythonanywhere.com';
echo         const APP_VERSION = '2.1';
echo         let currentUser = null;
echo         
echo         console.log('RTB App v' + APP_VERSION + ' loaded');
echo         
echo         function saveUser(userData) {
echo             console.log('Saving user:', userData);
echo             if (!userData ^|^| !userData.name) {
echo                 console.error('Invalid user data - no name field');
echo                 alert('Login error: Invalid user data received');
echo                 return;
echo             }
echo             currentUser = userData;
echo             localStorage.setItem('rtb_user', JSON.stringify(userData));
echo             updateUI();
echo         }
echo         
echo         function getUser() {
echo             if (currentUser ^&^& currentUser.name) return currentUser;
echo             
echo             try {
echo                 const stored = localStorage.getItem('rtb_user');
echo                 if (stored) {
echo                     const userData = JSON.parse(stored);
echo                     if (userData ^&^& userData.name) {
echo                         currentUser = userData;
echo                         return currentUser;
echo                     }
echo                 }
echo             } catch (error) {
echo                 console.error('Error parsing stored user:', error);
echo                 localStorage.removeItem('rtb_user');
echo             }
echo             return null;
echo         }
echo         
echo         function logout() {
echo             if (confirm('Are you sure you want to logout?')) {
echo                 currentUser = null;
echo                 localStorage.removeItem('rtb_user');
echo                 updateUI();
echo                 alert('Logged out successfully');
echo             }
echo         }
echo         
echo         function updateUI() {
echo             const user = getUser();
echo             const menu = document.getElementById('userMenu');
echo             
echo             if (user ^&^& user.name) {
echo                 console.log('Updating UI for user:', user.name);
echo                 menu.innerHTML = `
echo                     ^<div class="user-info"^>
echo                         ^<span style="color: #333; font-weight: 600;"^>
echo                             ^<i class="fas fa-user-circle" style="color: #6366f1;"^>^</i^> ${user.name}
echo                         ^</span^>
echo                         ^<button onclick="logout()" class="logout-btn"^>
echo                             ^<i class="fas fa-sign-out-alt"^>^</i^> Logout
echo                         ^</button^>
echo                     ^</div^>
echo                 `;
echo             } else {
echo                 console.log('No user logged in');
echo                 menu.innerHTML = `^<a href="#" onclick="showLogin()" class="auth-btn"^>^<i class="fas fa-sign-in-alt"^>^</i^> Login^</a^>`;
echo             }
echo         }
echo         
echo         function checkAuth() {
echo             const user = getUser();
echo             if (!user ^|^| !user.name) {
echo                 showLogin();
echo                 return false;
echo             }
echo             return true;
echo         }
echo         
echo         function showLogin() {
echo             const phone = prompt('Enter your phone number (e.g., +250788123456):');
echo             if (!phone) return;
echo             
echo             const password = prompt('Enter your password:');
echo             if (!password) return;
echo             
echo             login(phone, password);
echo         }
echo         
echo         async function login(phone, password) {
echo             try {
echo                 console.log('Attempting login for:', phone);
echo                 
echo                 const response = await fetch(`${API_BASE}/users/login`, {
echo                     method: 'POST',
echo                     headers: { 
echo                         'Content-Type': 'application/json',
echo                         'Accept': 'application/json'
echo                     },
echo                     body: JSON.stringify({ phone, password })
echo                 });
echo                 
echo                 console.log('Login response status:', response.status);
echo                 
echo                 if (response.ok) {
echo                     const userData = await response.json();
echo                     console.log('Login successful, user data:', userData);
echo                     
echo                     if (userData ^&^& userData.name) {
echo                         saveUser(userData);
echo                         alert(`Welcome back, ${userData.name}!`);
echo                     } else {
echo                         console.error('Invalid user data received:', userData);
echo                         alert('Login error: Invalid user data received');
echo                     }
echo                 } else {
echo                     const errorData = await response.json();
echo                     console.error('Login failed:', errorData);
echo                     alert(errorData.detail ^|^| 'Login failed. Please check your credentials.');
echo                 }
echo             } catch (error) {
echo                 console.error('Login error:', error);
echo                 alert('Connection error. Please check your internet and try again.');
echo             }
echo         }
echo         
echo         document.addEventListener('DOMContentLoaded', function() {
echo             console.log('Page loaded, initializing...');
echo             updateUI();
echo         });
echo     ^</script^>
echo ^</body^>
echo ^</html^> > frontend\index.html

echo [2/3] Committing and pushing to GitHub...
cd frontend
git add .
git commit -m "Deploy v2.1: Fixed undefined user + version control"
git push origin main

echo [3/3] Deployment complete!
echo.
echo ==========================================
echo    ✅ LATEST VERSION DEPLOYED!
echo ==========================================
echo.
echo Live URL: https://tuyisingize750.github.io/rtb-document-planner/
echo Version: 2.1
echo Deployed: %date% %time%
echo.
echo HOW TO ENSURE LATEST VERSION:
echo 1. Hard refresh: Ctrl+F5 (Windows) or Cmd+Shift+R (Mac)
echo 2. Check version number in bottom-left corner
echo 3. Clear cache: Ctrl+Shift+Delete
echo 4. Use incognito/private mode for testing
echo.
echo ==========================================