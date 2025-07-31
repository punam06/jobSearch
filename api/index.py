import os
import sys
from django.core.wsgi import get_wsgi_application

# Add project directory to Python path
sys.path.append('/vercel/path0')

# Set Django settings module for production
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')

# Configure for production
os.environ.setdefault('DEBUG', 'False')

# Get the WSGI application
application = get_wsgi_application()

# Vercel handler
app = application
