#!/bin/bash

# Build script for Vercel with full Django setup
echo "BUILD_START"

pip3 install -r requirements.txt

# Run database migrations
echo "Running migrations..."
python3 manage.py migrate --noinput

# Create superuser if needed
echo "Setting up admin user..."
python3 manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Admin user created: admin/admin123')
"

# Collect static files
python3 manage.py collectstatic --noinput --clear

echo "BUILD_END"

echo "BUILD_END"
