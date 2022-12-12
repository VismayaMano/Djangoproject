from django.db import models

# Create your models here.
class Gallery(models.Model):
    Name=models.CharField(max_length=20)
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
    Brand=models.CharField(max_length=20)
    Model=models.CharField(max_length=20)
    Price=models.IntegerField(default=0)
    Engine=models.CharField(max_length=20)

class Signup(models.Model): 
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Photo=models.ImageField(upload_to='media/',null=True,blank=True)
    Place=models.CharField(max_length=20)
    Email=models.EmailField()
    Password=models.CharField(max_length=8)

