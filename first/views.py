#import requests
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login

# Create your views here.

'''def home(request):
    if request.user.is_anonymous:
        return redirect('/')
    return render(request,'home/')'''

def index(request):
    if request.method=='POST':
        if 'login' in request.POST:
            email = request.POST.get('email')
            passw = request.POST.get('pass')
            user = authenticate(username=email, password=passw)
            if user is not None:
                login(request, user)
                return redirect('home/')
            else:
                return redirect('/')
        if 'create' in request.POST:
            print(request.POST)
            email = request.POST.get('emailCreate')
            username = request.POST.get('username')
            passw = request.POST.get('newpass')
            #chpassw = request.POST.get('chkpass')
            usr = User.objects.create_user(is_superuser=False,email=email,password=passw,username=username, is_staff= False)
            usr.save()


    return render(request, "index.html")
    #return HttpResponse("Hekk")

def abc(request):
    return render(request, "index2.html")

def functionh(request):
    return HttpResponse("wtf")

def loggedout(request):
    logout(request)
    return redirect('/')
    #return render(request,'logout.html')

def homerender(request):
    if request.user.is_anonymous:
        return redirect('/')
    return render(request, 'home.html')