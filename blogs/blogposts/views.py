# from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import blogger
# Create your views here.

def index(request):  
    bl= blogger.objects.all()
    return render(request, "index.html")
def aboutus(request):  
    return render(request, "about.html")
def marketing(request):  
    return render(request, "marketing.html")
def blog(request):  
    return render(request, "blog.html")
def contactus(request):  
    return render(request, "contact.html")