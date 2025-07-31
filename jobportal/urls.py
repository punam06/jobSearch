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
    from demo_views import demo_home, demo_view

urlpatterns = []

# For Vercel deployment, use demo view
if 'VERCEL' in os.environ:
    urlpatterns = [
        path('', demo_home, name='demo_home'),
        path('jobs/', demo_view, name='demo_jobs'),
        path('accounts/register/', demo_view, name='demo_register'),
        path('accounts/login/', demo_view, name='demo_login'),
        path('post-job/', demo_view, name='demo_post_job'),
        path('admin/', demo_view, name='demo_admin'),
        path('demo/', demo_view, name='demo_page'),
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
