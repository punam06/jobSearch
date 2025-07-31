#!/usr/bin/env python
"""
Minimal production setup - just ensure Django can start
"""
import os
import django

try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')
    django.setup()
    
    from django.contrib.auth.models import User
    
    # Only create admin if no users exist
    if User.objects.count() == 0:
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@jobportal.com',
            password='admin123'
        )
        print("✅ Admin user created: admin/admin123")
    else:
        print("✅ Users already exist")
        
except Exception as e:
    print(f"⚠️ Setup script completed with warnings: {e}")
    
print("✅ Minimal setup complete!")
