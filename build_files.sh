#!/bin/bash

# Build script for Vercel
pip3 install -r requirements.txt

# Run migrations
python3 manage.py migrate --noinput

# Collect static files
python3 manage.py collectstatic --noinput --clear

# Create sample data (optional, comment out if not needed)
python3 manage.py create_sample_data || echo "Sample data creation failed or command doesn't exist"
