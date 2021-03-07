from django.db import models

# Create your models here.
class blogger(models.Model):
    fname = models.TextField()
    lname = models.TextField(default=" ")
    gender = models.CharField(max_length=5)
    age = models.IntegerField()
    email_id = models.EmailField()
    content = models.TextField()
    category = models.TextField()
    avatar = models.ImageField(upload_to='pics')
    title =models.TextField()

