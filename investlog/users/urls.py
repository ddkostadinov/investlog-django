# users/urls.py
from django.urls import path
from .views import CustomLoginView, RegisterView, LogOutView, SettingsView, UsernameChangeView, PasswordChangeView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('settings/', SettingsView.as_view(), name='settings'),
    path('change-username/', UsernameChangeView.as_view(), name='change-username'),
    path('change-password/', PasswordChangeView.as_view(), name='change-password'),
    
]