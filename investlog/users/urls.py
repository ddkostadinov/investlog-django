# users/urls.py
from django.urls import path
from .views import CustomLoginView, RegisterView, LogOutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogOutView.as_view(), name='logout'),
    
]