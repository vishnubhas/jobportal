from django.db import models
from comapny.models import Jobpost
from account.models import User2
# Create your models here.

class Userprofile(models.Model):
  
    name=models.CharField(max_length=250)
    s_name=models.CharField(max_length=250)
    description=models.TextField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.EmailField(null=True,blank=True)
    
    skill=models.CharField(max_length=200)
    git=models.CharField(max_length=300,unique=True)
    youtube=models.CharField(max_length=300,unique=True)
    linkedin=models.CharField(max_length=300,unique=True)
    image=models.ImageField(upload_to='image/',null=True,blank=True)
    age=models.IntegerField(3)                  
    street=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    pincode=models.PositiveBigIntegerField()
    ref_user=models.OneToOneField(User2,on_delete=models.CASCADE)
    ref_comfile=models.OneToOneField(Jobpost,on_delete=models.CASCADE)
    

     
     
