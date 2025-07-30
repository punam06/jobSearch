"""
URL configuration for jobportal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import os

# Import demo view for Vercel deployment
if 'VERCEL' in os.environ:
    from demo_views import demo_view

urlpatterns = []

# For Vercel deployment, use simple demo view
if 'VERCEL' in os.environ:
    urlpatterns = [
        path('', demo_view, name='demo'),
        path('admin/', demo_view, name='demo_admin'),
        path('accounts/', demo_view, name='demo_accounts'),
        path('jobs/', demo_view, name='demo_jobs'),
    ]
else:
    # Local development with full functionality
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('jobs.urls')),
        path('accounts/', include('accounts.urls')),
        path('accounts/', include('django.contrib.auth.urls')),
    ]

if settings.DEBUG and 'VERCEL' not in os.environ:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0] if settings.STATICFILES_DIRS else None)
