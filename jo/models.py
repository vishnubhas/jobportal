from django.db import models
from comapny.models import  *
from account.models import *
# Create your models here.


class Gender(models.Model):
    gender_choice=models.CharField(max_length=200)
    def __str__(self) :
            return self.gender_choice

class Userprofile(models.Model):
    ref_user=models.ForeignKey(User2,on_delete=models.CASCADE)
    ref_gender=models.ForeignKey(Gender,on_delete=models.CASCADE)
    
    name=models.CharField(max_length=250)
    s_name=models.CharField(max_length=250)
    description=models.TextField(max_length=200)
    phone=models.CharField(max_length=200)
    email=models.EmailField(null=True,blank=True)
    
    skill=models.CharField(max_length=200)
    git=models.CharField(max_length=300,unique=True)
    youtube=models.CharField(max_length=300,unique=True)
    
    image=models.ImageField(upload_to='image/',null=True,blank=True)
    age=models.IntegerField(3)                  
    street=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    pincode=models.PositiveBigIntegerField()
    def __str__(self) :
        return self.name
    
   
class JobApplication(models.Model):
     user=models.ForeignKey(User2,on_delete=models.CASCADE)
     ref_job=models.ForeignKey(Jobpost,on_delete=models.CASCADE)
     ref_profile=models.ForeignKey(Userprofile,on_delete=models.CASCADE)
     resume=models.FileField(upload_to='files/',null=True)
   
    

    
     
