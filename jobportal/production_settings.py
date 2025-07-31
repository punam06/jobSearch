"""
Production settings for Railway/Heroku deployment
"""
from .settings import *
import dj_database_url
import os

# Override DEBUG for production
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# Production hosts
ALLOWED_HOSTS = [
    '.railway.app',
    '.herokuapp.com',
    '.onrender.com',
    'localhost',
    '127.0.0.1',
    '*'  # Remove this in actual production
]

# Database configuration for production
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR}/db.sqlite3",
        conn_max_age=600,
        conn_health_checks=True,
    )
}

# Static files configuration
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Security settings for production
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
