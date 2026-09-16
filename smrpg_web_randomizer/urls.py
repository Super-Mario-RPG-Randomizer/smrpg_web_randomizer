"""smrpg_web_randomizer URL Configuration

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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

from django.conf import settings
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

urlpatterns = [
    path('', include('randomizer.urls')),

    # Login/admin
    path("accounts/login/", auth_views.LoginView.as_view(template_name='admin/login.html'), name='login'),
    path("admin/", admin.site.urls),
]

# Serve static files automatically during local development
if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
