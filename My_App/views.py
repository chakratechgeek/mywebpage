from django.shortcuts import render
from django.http import HttpResponse
from .models import Datas
from .models import Fun
from .models import Contact
from django.contrib import messages
# Create your views here.


class MyPlc:
    def __init__(self):
        pass
    
    def home (request):
        return render(request,"webpage_new.html")
    
    def aboutMe (request):
        return render (request,"aboutMe.html")
    
    def contact(request):
        if request.method == 'POST':
            obj_Contact = Contact() 
            obj_Contact.Name = request.POST['Name'] #capital N in Name represents the column name
            obj_Contact.Email = request.POST['Email']
            obj_Contact.Message = request.POST['Message']
            obj_Contact.save()
      
        return render(request,"contact.html")

    def certification (request):
        return render(request,"certification.html")
    
    def thisweb (request):
        return render(request,"thisweb.html")

    def rds_onboarding (request):
        return render(request,"rds_onboarding.html")
    
    def services (request):
        return render(request,"webpage_v2.html")
    
    def index (request):
        return render(request,"index.html")
    