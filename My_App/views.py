from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


class MyPlc:
    def __init__(self):
        pass
    
    def home (request):
        return render(request,"webpage.html")
    
    def aboutMe (request):
        return render (request,"aboutMe.html")
    
    def register(request):
        if request.method == 'POST':
            name=request.POST['name']
            password=request.POST['password']
            address=request.POST['address']
            mail=request.POST['mail']
            return render(request,"result.html",{'Name':name,'Password':password,'Address':address,'Mail':mail})
        