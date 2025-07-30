#!/bin/bash

# Vercel build script
echo "Starting Vercel build process..."

# Install requirements
echo "Installing requirements..."
pip3 install -r requirements.txt

# Set Django settings
export DJANGO_SETTINGS_MODULE=jobportal.settings

# Run Django migrations
echo "Running migrations..."
python3 manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python3 manage.py collectstatic --noinput --clear

# Create superuser if it doesn't exist
echo "Creating superuser..."
python3 manage.py shell << EOF
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
    print('Superuser created')
else:
    print('Superuser already exists')
EOF

echo "Build process completed!"
