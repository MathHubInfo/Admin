"""mhadmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based viewsgit lo
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .views import healthcheck
from .views.nginx import check, check_staff, authenticate, authenticate_staff
from .views.admin import index, login, login_staff, logout

from .admin import admin_site

urlpatterns = [
    # healthcheck for docker image
    path('', healthcheck), 

    path('admin/', index, name='index'), 
    path('admin/login', login, name='login'), 
    path('admin/login_staff', login_staff, name='login_staff'), 
    path('admin/logout', logout, name='logout'), 

    # nginx login backend
    path('admin/nginx/check', check, name='check'), 
    path('admin/nginx/check_staff', check_staff, name='check_staff'),
    path('admin/nginx/authenticate', authenticate, name='authenticate'), 
    path('admin/nginx/authenticate_staff', authenticate_staff, name='authenticate_staff'), 

    # Django Admin
    path('admin/django/', admin_site.urls) 
]
