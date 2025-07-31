#!/bin/bash

# Railway startup script
echo "🚀 Starting Railway deployment..."

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Run migrations
echo "🗄️ Running database migrations..."
python manage.py migrate

# Create superuser if no users exist
echo "👤 Setting up admin user..."
python -c "
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')
django.setup()
from django.contrib.auth.models import User
if User.objects.count() == 0:
    User.objects.create_superuser('admin', 'admin@jobportal.com', 'admin123')
    print('✅ Admin user created: admin/admin123')
else:
    print('✅ Users already exist')
"

echo "✅ Setup complete! Starting server..."
exec gunicorn jobportal.wsgi:application
