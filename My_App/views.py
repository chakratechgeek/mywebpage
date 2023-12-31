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
    
    def signup (request):
        if request.method == 'POST':
            obj_datas = Datas() 
            obj_datas.Name = request.POST['name'] #capital N in Name represents the column name
            obj_datas.Age = request.POST['age']
            obj_datas.Address = request.POST['address']
            obj_datas.Contact = request.POST['contact']
            obj_datas.Email = request.POST['email']
            obj_datas.save()
            messages.success(request, 'Signup successful!')
         
        return render (request,"signup.html")
    
    def contact(request):
        if request.method == 'POST':
            obj_Contact = Contact() 
            obj_Contact.Name = request.POST['Name'] #capital N in Name represents the column name
            obj_Contact.Email = request.POST['Email']
            obj_Contact.Message = request.POST['Message']
            obj_Contact.save()
      
        return render(request,"contact.html")
    
    def fun (request):
        if request.method == 'POST':
            obj_Fun = Fun() 
            obj_Fun.Num1 = request.POST['val1'] #capital N in Name represents the column name
            obj_Fun.Num2 = request.POST['val2']
            obj_Fun.save()
        return render(request,"javaScript.html")   
     
    def register(request):
        if request.method == 'POST':
            name=request.POST['name']
            password=request.POST['password']
            address=request.POST['address']
            mail=request.POST['mail']
            return render(request,"result.html",{'Name':name,'Password':password,'Address':address,'Mail':mail})
        
    def certification (request):
        return render(request,"certification.html")
    
    def learning (request):
        return render(request,"learning.html")

    def web (request):
        return render(request,"web.html")
    