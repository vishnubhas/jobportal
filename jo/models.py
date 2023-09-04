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
     resume=models.ImageField(upload_to='files/',null=True)
     is_accepted=models.BooleanField(default=False)
class Workexperiance(models.Model):
     user=models.ForeignKey(Userprofile,on_delete=models.CASCADE)
     ref_user=models.ForeignKey(User2,on_delete=models.CASCADE)
     title=models.CharField(max_length=250)
     discription=models.TextField()
     position=models.CharField(max_length=250)
     stating_date=models.DateField()
     end_date=models.DateField()
     def __str__(self) :
          return self.title
class Educations(models.Model):
     ref_user=models.ForeignKey(User2,on_delete=models.CASCADE)
     user=models.ForeignKey(Userprofile,on_delete=models.CASCADE)
     department=models.CharField(max_length=250)
     college=models.CharField(max_length=250)
     start=models.DateField()
     end=models.DateField()
     def __str__(self):
          return self.department
class Projects(models.Model):
     ref_user=models.ForeignKey(User2,on_delete=models.CASCADE)
     user=models.ForeignKey(Userprofile,on_delete=models.CASCADE)
     project=models.CharField(max_length=250)
     start=models.DateField()
     end=models.DateField()
     description=models.TextField()
     def __str__(self):
          return self.project
class Certificates(models.Model):
     user=models.ForeignKey(Userprofile,on_delete=models.CASCADE)
     ref_user=models.ForeignKey(User2,on_delete=models.CASCADE)
     company=models.CharField(max_length=200)
     certificate_name=models.CharField(max_length=250)
     certificate=models.FileField(upload_to='files/' ,null=True)
     def __str__(self):
          return self.certificate_name
class ITskills(models.Model):
     user=models.ForeignKey(Userprofile,on_delete=models.CASCADE)
     ref_user=models.ForeignKey(User2,on_delete=models.CASCADE)
     skills=models.CharField(max_length=260)
     vertion=models.FloatField()
     last_used=models.DateField()
     experiance=models.IntegerField()
     def __str__(self):
          return self.skills
class Language(models.Model):
     user=models.ForeignKey(User2,on_delete=models.CASCADE)
     ref_user=models.ForeignKey(Userprofile,on_delete=models.CASCADE)
     language=models.CharField(max_length=200)
     level=models.CharField(max_length=100)
     def __str__(self):
          return self.language
class Softskill(models.Model):
     user=models.ForeignKey(User2,on_delete=models.CASCADE)
     ref_user=models.ForeignKey(Userprofile,on_delete=models.CASCADE)
     softskill=models.CharField(max_length=200)
     def __str__(self):
          return self.softskill
class Comment(models.Model):
     ref_user=models.ForeignKey(User2,on_delete=models.CASCADE)
     user=models.ForeignKey(Userprofile,on_delete=models.CASCADE)
     comment=models.CharField(max_length=300)
     date=models.DateField(auto_now_add=True)
     def __str__(self):
          return self.comment
class Jobcomments(models.Model):
    user=models.ForeignKey(User1,on_delete=models.CASCADE)
    ref_profile=models.ForeignKey(Userprofile,on_delete=models.CASCADE)
    jobpost=models.ForeignKey(Jobpost,on_delete=models.CASCADE)
    
    comment=models.CharField(max_length=200)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.comment
class Replay(models.Model):
    
    ref_profile=models.ForeignKey(Companyprofile,on_delete=models.CASCADE)
    jobcomments=models.ForeignKey(Jobcomments,on_delete=models.CASCADE)
    job=models.ForeignKey(Jobpost,on_delete=models.CASCADE)
    user_profile=models.ForeignKey(Userprofile,on_delete=models.CASCADE)
    replay=models.CharField(max_length=200)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.replay
     
    

    
     
