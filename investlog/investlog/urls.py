"""
URL configuration for investlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from users import views



urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('home.urls')), 
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.LogOutView.as_view(), name='logout'),
    path('settings/', views.SettingsView.as_view(), name='settings'),
    path('change-username/', views.UsernameChangeView.as_view(), name='change-username'),
    path('change-password/', views.PasswordChangeView.as_view(), name='change-password'),
    path('dashboard/', include('dashboard.urls')), 
]
