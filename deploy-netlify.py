#!/usr/bin/env python3
"""
Automated Netlify Deployment Script for RTB Document Planner
Handles frontend deployment with custom domain configuration
"""

import os
import json
import subprocess
import sys
from pathlib import Path

class NetlifyDeployer:
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.frontend_dir = self.project_root / "frontend"
        
    def install_netlify_cli(self):
        """Install Netlify CLI if not present"""
        print("📦 Installing Netlify CLI...")
        try:
            subprocess.run(["npm", "install", "-g", "netlify-cli"], check=True)
            print("✅ Netlify CLI installed successfully")
        except subprocess.CalledProcessError:
            print("❌ Failed to install Netlify CLI. Please install Node.js first.")
            sys.exit(1)
    
    def check_netlify_auth(self):
        """Check if user is authenticated with Netlify"""
        try:
            result = subprocess.run(["netlify", "status"], capture_output=True, text=True)
            if "Not logged in" in result.stdout:
                print("🔐 Please login to Netlify...")
                subprocess.run(["netlify", "login"], check=True)
            print("✅ Netlify authentication verified")
        except subprocess.CalledProcessError:
            print("❌ Netlify CLI not found. Installing...")
            self.install_netlify_cli()
    
    def create_netlify_config(self):
        """Create optimized netlify.toml configuration"""
        config = """[build]
  publish = "frontend"
  command = ""

[build.environment]
  NODE_VERSION = "18"

[[redirects]]
  from = "/*"
  to = "/index.html"
  status = 200

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-XSS-Protection = "1; mode=block"
    X-Content-Type-Options = "nosniff"
    Referrer-Policy = "strict-origin-when-cross-origin"

[[headers]]
  for = "/api/*"
  [headers.values]
    Access-Control-Allow-Origin = "*"
    Access-Control-Allow-Methods = "GET, POST, PUT, DELETE, OPTIONS"
    Access-Control-Allow-Headers = "Content-Type, Authorization"
"""
        
        with open(self.project_root / "netlify.toml", "w") as f:
            f.write(config)
        
        # Create _redirects file
        with open(self.frontend_dir / "_redirects", "w") as f:
            f.write("/*    /index.html   200\n")
        
        print("✅ Netlify configuration files created")
    
    def deploy_to_netlify(self, site_name=None, custom_domain=None):
        """Deploy frontend to Netlify"""
        print("🚀 Deploying to Netlify...")
        
        os.chdir(self.project_root)
        
        # Initial deployment
        if site_name:
            cmd = ["netlify", "deploy", "--prod", "--dir", "frontend", "--site", site_name]
        else:
            cmd = ["netlify", "deploy", "--prod", "--dir", "frontend"]
        
        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            print("✅ Deployment successful!")
            
            # Extract site URL
            for line in result.stdout.split('\n'):
                if 'Website URL:' in line:
                    site_url = line.split('Website URL:')[1].strip()
                    print(f"🌐 Site URL: {site_url}")
                    
                    if custom_domain:
                        self.setup_custom_domain(custom_domain)
                    
                    return site_url
                    
        except subprocess.CalledProcessError as e:
            print(f"❌ Deployment failed: {e}")
            print(f"Error output: {e.stderr}")
            sys.exit(1)
    
    def setup_custom_domain(self, domain):
        """Configure custom domain"""
        print(f"🔗 Setting up custom domain: {domain}")
        try:
            subprocess.run(["netlify", "domains:add", domain], check=True)
            print(f"✅ Custom domain {domain} added successfully")
            print(f"📋 DNS Configuration Required:")
            print(f"   CNAME: www -> your-site.netlify.app")
            print(f"   A Record: @ -> Netlify IP (check Netlify dashboard)")
        except subprocess.CalledProcessError:
            print(f"⚠️  Custom domain setup requires manual configuration in Netlify dashboard")

def main():
    print("🎯 RTB Document Planner - Netlify Deployment")
    print("=" * 50)
    
    deployer = NetlifyDeployer()
    
    # Get user input
    site_name = input("Enter Netlify site name (optional, press Enter to skip): ").strip()
    custom_domain = input("Enter your custom domain (optional, e.g., mydomain.com): ").strip()
    
    # Execute deployment steps
    deployer.check_netlify_auth()
    deployer.create_netlify_config()
    
    site_url = deployer.deploy_to_netlify(
        site_name if site_name else None,
        custom_domain if custom_domain else None
    )
    
    print("\n🎉 Deployment Complete!")
    print("=" * 30)
    print(f"Frontend: {site_url}")
    print(f"Backend: https://leonardus437.pythonanywhere.com")
    
    if custom_domain:
        print(f"\n📝 Next Steps for Custom Domain:")
        print(f"1. Update DNS records for {custom_domain}")
        print(f"2. Wait for DNS propagation (up to 24 hours)")
        print(f"3. SSL certificate will be auto-generated")

if __name__ == "__main__":
    main()