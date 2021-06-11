# from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .models import blogger,like
import smtplib
from email.mime.text import MIMEText
from getpass import getpass
# Create your views here.

def index(request):
    blogs = blogger.objects.all()
    categories = []
    count = []
    images =[]
    for blg in blogs:
        if blg.category not in categories:
            categories.append(blg.category)
            images.append(blg.avatar)
    for i in categories:
        count.append(blogger.objects.filter(category=i).count())
    myfile = zip(categories, count, images)
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
def myblog(request,slug):
    print(slug)
    bloggers= blogger.objects.filter(username=slug)
    return render(request, "blog.html",{'bloggers':bloggers})
def blogs(request,slug):
    bloggers= blogger.objects.filter(category=slug)
    return render(request, "blog.html",{'bloggers':bloggers})
def contactus(request):
    if request.method == 'POST':
        name = request.POST['name']
        fromid = request.POST['email']
        password = request.POST['password']
        subj = request.POST['subject']
        body = request.POST['body']

        toid=["akshatasangwai1234@gmail.com","skaliappan1908@gmail.com","shriyad2303@gmail.com"]
        
        msg=MIMEText(body)
        msg['From']=fromid
        msg['To']=(',').join(toid)
        msg['subject']=name+" says "+subj

        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(fromid,password)
        server.send_message(msg)
        print("Your mail is sent")
        server.quit()
        return redirect('/')
    return render(request, "contact.html")
def newblog(request):
    if request.method == 'POST':
        blgr = blogger()
        blgr.fname = request.POST['fname']
        blgr.lname = request.POST['lname']
        blgr.username = request.POST['username']
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

def liked(request,slug,blogid):
    blog = blogger.objects.get(pk=blogid)
    userliked = like.objects.filter(likedby=slug)
    for li in userliked:
        if li.pk is blogid:
            return redirect('blog')
    else:
        blog.likes+=1
        blog.save()
        likeobj = like()
        likeobj.likedby = slug
        likeobj.blogliked = blog
        likeobj.save()
        return redirect('blog')

def myliked(request,slug):
    likelist=like.objects.filter(likedby=slug)
    bloggers = []
    for li in likelist:
        bloggers.append(li.blogliked)
    return render(request, "blog.html",{'bloggers':bloggers})
