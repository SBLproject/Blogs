from django.urls import path
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path("aboutus", views.aboutus, name='aboutus'),
    path("marketing", views.marketing, name='marketing'),
    path("blog", views.blog, name='blog'),
    path("blogs/<slug:slug>", views.blogs, name='blogs'),
    path("contactus", views.contactus, name='contactus'),
    path("newblog", views.newblog, name='newblog'),
    path("blogview/<int:myid>", views.blogview , name="blogview"),
    path("register",views.register, name='register'),
    path("login",views.login, name='login'),
    path("logout",views.logout, name='logout'),
    # path("login", views.lo, name='login'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)