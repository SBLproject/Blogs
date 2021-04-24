from django.db import models
import os
# Create your models here.
class blogger(models.Model):
    fname = models.TextField()
    lname = models.TextField(default=" ")
    username = models.TextField(default=" ")
    gender = models.CharField(max_length=5)
    age = models.IntegerField()
    email_id = models.EmailField()
    content = models.TextField()
    category = models.TextField()
    avatar = models.ImageField(null=True, blank=True,  upload_to='pics')
    title =models.TextField()
    likes = models.IntegerField(default=0)
    def _str_(self):
        return self.title

class like(models.Model):
    likedby = models.TextField(default=" ")
    blogliked = models.ForeignKey(blogger, on_delete=models.CASCADE, default="")
    def _str_(self):
        return self.pk

