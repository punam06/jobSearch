#!/bin/bash

# Build script for Vercel with demo setup
echo "BUILD_START"

pip3 install -r requirements.txt

# Set VERCEL environment variable for proper settings
export VERCEL=1

# Skip database operations for Vercel (using dummy backend)
echo "Skipping database operations for Vercel deployment..."

# Collect static files
python3 manage.py collectstatic --noinput --clear

echo "BUILD_END"

echo "BUILD_END"
