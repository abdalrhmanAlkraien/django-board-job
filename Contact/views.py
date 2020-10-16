from django.shortcuts import render
from .models import information
from django.core.mail import send_mail

from django.conf import settings
# Create your views here.
def send_message(request):
    info=information.objects.first()
    if request.method=="POST":
        subject=request.POST['subject']
        email=request.POST['email']
        message=request.POST['message']
        send_mail(subject,message,'abdlarhmanalkraien@gmail.com',[email] )
    context={'info':info}
    return render(request,'contact/contact.html',context)
