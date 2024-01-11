from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterView(View):
    def post(self, request):
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            user = User.objects.create_user(username=request.POST.get("username"), email=request.POST.get("email"), password=request.POST.get("password1"))
            user.save()
            
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
        return render(request, 'users/register.html', {
        'form': form
    })
        
    def get(self, request):
        form = UserRegisterForm()
        
        return render(request, 'users/register.html', {
            'form': form
        })
      
             
class CustomLoginView(View):
    def post(self, request):
        form = UserLoginForm(request.POST)
        
        username = request.POST.get("username", False)
        password = request.POST.get("password", False)
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        
        messages.error(request, 'Invalid credentials. Please try again.')
        return render(request, 'users/login.html', {
            'form': form
        })
    
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'users/login.html', {
            'form': form
        })
        
class LogOutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect('index')
        