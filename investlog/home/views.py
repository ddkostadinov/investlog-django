from django.shortcuts import render
from django.contrib.staticfiles.views import serve
from django.contrib import messages
import smtplib
import dotenv
import os

dotenv.load_dotenv()

def index(request):
    context = {'user': request.user}
    return render(request, 'home/index.html', context)


def about(request):
    context = {'user': request.user}
    return render(request, 'home/about.html', context)


def contact(request):
    if request.method == "POST":
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=os.environ.get("EMAIL_SENDER"), password=os.environ.get("EMAIL_PASSWORD"))
            connection.sendmail(
                from_addr=os.environ.get("EMAIL_SENDER"),
                to_addrs=os.environ.get("EMAIL_RECEIVER"),
                msg=f"Subject:From {request.POST.get('name')}\n\nEmail:{request.POST.get('email')}\n\n{request.POST.get('message')}",
            )
        messages.success(request, "Message sent successfully. Thank you for contacting us!")
    context = {'user': request.user}
    return render(request, 'home/contact.html', context)