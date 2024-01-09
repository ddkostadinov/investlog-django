from django.shortcuts import render
from django.contrib.staticfiles.views import serve

def index(request):
    context = {'user': request.user}
    return render(request, 'home/index.html', context)

def about(request):
    context = {'user': request.user}
    return render(request, 'home/about.html', context)

def contact(request):
    context = {'user': request.user}
    return render(request, 'home/contact.html', context)