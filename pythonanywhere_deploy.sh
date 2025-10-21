#!/bin/bash

# PythonAnywhere deployment helper for leonardus437
# Usage: bash pythonanywhere_deploy.sh

set -euo pipefail

PROJECT_DIR="/home/leonardus437/rtb-document-planner"
VENV_DIR="${PROJECT_DIR}/venv"

cd "${PROJECT_DIR}"

echo "🔄 Pulling latest code..."
git pull origin main

if [ -d "${VENV_DIR}" ]; then
  echo "🐍 Activating virtual environment..."
  source "${VENV_DIR}/bin/activate"
else
  echo "⚠️ Virtual environment not found at ${VENV_DIR}. Skipping activation."
fi

if [ -f requirements.txt ]; then
  echo "📦 Installing/Updating dependencies..."
  pip install -r requirements.txt
fi

if [ -f backend/requirements.txt ]; then
  echo "📦 Installing backend-specific dependencies..."
  pip install -r backend/requirements.txt
fi

if [ -f backend/main.py ]; then
  echo "✅ Backend code is up to date (backend/main.py present)."
else
  echo "❌ backend/main.py not found! Please check the repository."
fi

echo "🔁 Touching WSGI file to trigger reload..."
.touch /var/www/leonardus437_pythonanywhere_com_wsgi.py

if [ -n "${VIRTUAL_ENV:-}" ]; then
  echo "📤 Deactivating virtual environment..."
  deactivate
fi

echo "✅ Deployment steps complete. Remember to reload the web app via the Dashboard if needed."