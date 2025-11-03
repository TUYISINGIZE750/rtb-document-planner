"""Check deployment status and test downloads"""
import requests
import time

API_BASE = "https://rtb-document-planner.onrender.com"

print("\n" + "="*70)
print("DEPLOYMENT STATUS CHECK")
print("="*70)

# Check API status
print("\n[1] Checking API status...")
try:
    response = requests.get(f"{API_BASE}/", timeout=10)
    if response.status_code == 200:
        data = response.json()
        print(f"[OK] API is online")
        print(f"    Version: {data.get('version', 'unknown')}")
        print(f"    Deployment: {data.get('deployment', 'unknown')}")
        print(f"    Users: {data.get('users_count', 0)}")
    else:
        print(f"[FAIL] API returned {response.status_code}")
except Exception as e:
    print(f"[ERROR] Cannot reach API: {e}")

# Check test endpoint
print("\n[2] Checking scheme generation endpoint...")
try:
    response = requests.get(f"{API_BASE}/test-scheme", timeout=30)
    if response.status_code == 200:
        data = response.json()
        print(f"[OK] Scheme generation working")
        print(f"    Status: {data.get('status')}")
        print(f"    File size: {data.get('file_size', 0):,} bytes")
    else:
        print(f"[FAIL] Test returned {response.status_code}")
        print(f"    Response: {response.text[:200]}")
except Exception as e:
    print(f"[ERROR] Test failed: {e}")

print("\n" + "="*70)
print("DEPLOYMENT CHECK COMPLETE")
print("="*70)
print("\nRender will auto-deploy from GitHub push.")
print("Wait 2-3 minutes for deployment to complete.")
print("\nCheck deployment at:")
print("https://dashboard.render.com/")
print("="*70 + "\n")
