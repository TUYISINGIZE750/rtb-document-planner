#!/bin/bash
set -e

echo "Starting build process..."

# Install Python dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Initialize database
echo "Initializing database..."
cd backend
python init_db.py
cd ..

echo "Build completed successfully!"