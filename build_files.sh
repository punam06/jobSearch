#!/bin/bash

# Build script for Vercel
pip install -r requirements.txt

# Run migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput --clear

# Create sample data (optional, comment out if not needed)
python manage.py create_sample_data || echo "Sample data creation failed or command doesn't exist"
