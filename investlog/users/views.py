from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
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
            
            return HttpResponse("Form submitted successfully!")
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
            return redirect("dashboard")
        else:
            return render(request, 'users/login.html', {
            'form': form
        })
    
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'users/login.html', {
            'form': form
        })
        
class LogOutView(LoginRequiredMixin, View):
    #TODO: add a Logout Button in home/index.html and to dashboard settings
    def get(self, request):
        logout(request)
        return redirect('index')
        