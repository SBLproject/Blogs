# from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import blogger
# Create your views here.

def index(request):
    return render(request, "index.html")
def aboutus(request):
    return render(request, "about.html")
def marketing(request):
    return render(request, "marketing.html")
def blog(request):
    bloggers= blogger.objects.all()
    return render(request, "blog.html",{'bloggers':bloggers})
def contactus(request):
    return render(request, "contact.html")
def newblog(request):
    if request.method == 'POST':
        blgr = blogger()
        blgr.fname = request.POST['fname']
        blgr.lname = request.POST['lname']
        blgr.title = request.POST['title']
        blgr.age = request.POST['age']
        blgr.gender = request.POST['gender']
        blgr.content = request.POST['content']
        blgr.category = request.POST['category']
        blgr.email_id = request.POST['emailId']
        files = request.FILES  # multivalued dict
        blgr.avatar = files.get("image")
        blgr.save()
        return redirect('blog')
    return render(request, "newblog.html")
def blogview(request, myid):
    blog = blogger.objects.filter(id=myid)
    # print(sliced)
    return render(request,'prodView.html', {'blog': blog[0]})