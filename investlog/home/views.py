from django.shortcuts import render
from django.contrib.staticfiles.views import serve
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

def index(request):
    context = {'user': request.user}
    return render(request, 'home/index.html', context)


def about(request):
    context = {'user': request.user}
    return render(request, 'home/about.html', context)


def contact(request):
    context = {'user': request.user}
    if request.method == "POST":
        sender_email = settings.EMAIL_HOST_USER
        receiver_email = settings.EMAIL_RECEIVER
        subject = f"From {request.POST.get('name')}"
        message = f"Email:{request.POST.get('email')}\n\n{request.POST.get('message')}"
        try:
            send_mail(subject, message, sender_email, [receiver_email])
            messages.success(request, "Message sent successfully. Thank you for contacting us!")
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
        
    return render(request, 'home/contact.html', context)