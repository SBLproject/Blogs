# from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import blogger
# Create your views here.

def index(request):
    blogs = blogger.objects.all()
    categories = []
    count = []
    for blg in blogs:
        if blg.category not in categories:
            categories.append(blg.category)
    for i in categories:
        count.append(blogger.objects.filter(category=i).count())
    myfile = zip(categories, count)
    context = {
        'myfile':myfile,
    }
    return render(request, "index.html",context)
def aboutus(request):
    return render(request, "about.html")
def marketing(request):
    return render(request, "marketing.html")
def blog(request):
    bloggers= blogger.objects.all()
    return render(request, "blog.html",{'bloggers':bloggers})
def blogs(request,slug):
    bloggers= blogger.objects.filter(category=slug)
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

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'User name not avaliable..')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken..')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username,password=password1,email=email, first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,'User created')
                return redirect('login')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
        return redirect('/')

        

    else:
        return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')