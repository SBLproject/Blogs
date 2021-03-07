from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("aboutus", views.aboutus, name='aboutus'),
    path("marketing", views.marketing, name='marketing'),
    path("blog", views.blog, name='blog'),
    path("contactus", views.contactus, name='contactus'),
    # path("login", views.lo, name='login'),
]