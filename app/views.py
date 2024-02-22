from django.shortcuts import render
from django.core.mail import EmailMessage
from django.http import HttpResponse
from .models import *

def home(request):
    if request.method == 'POST':
        recipient = request.POST.get('recipient')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        files = request.FILES.getlist('files')
        
        try:
            email = EmailMessage(
                subject,
                message,
                'mamadaminov001@gmail.com',
                [recipient],
            )
            
            for file in files:
                email.attach(file.name, file.read(), file.content_type)
            
            email.send()
            
            return render(request, "index.html", {'message': 'Message sent successfully'})
        except Exception as e:
            return HttpResponse("Message not sent: " + str(e))

    return render(request, "index.html", {})