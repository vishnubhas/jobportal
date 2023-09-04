from django.db import models
from account.models import *
from adminapp.models import Admin_view

# Create your models here.

class  Companyprofile(models.Model):
  
    companynames=models.CharField(max_length=250)
    
    descriptions=models.TextField(max_length=200)
    phones=models.CharField(max_length=200)
    emails=models.EmailField(null=True,blank=True)
    establishes=models.CharField(max_length=200)
    quotes=models.TextField(max_length=200)
    websites=models.CharField(max_length=300,unique=True)
    gits=models.CharField(max_length=300,unique=True)
    youtubes=models.CharField(max_length=300,unique=True)
   
    images=models.ImageField(upload_to='company_image/',null=True,blank=True)
   
    street=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    pincode=models.PositiveBigIntegerField()
    ref_profle=models.ForeignKey(Company,on_delete=models.CASCADE)
    # is_request = models.BooleanField(default=False)
   
 
    
    def __str__(self) :
        return self.companynames
    


class   RecentWork(models.Model):
    work=models.CharField(max_length=200)
    image=models.ImageField(upload_to='work_image/',null=True,blank=True)
    short_dic=models.CharField(max_length=200)
    long_dic=models.CharField(max_length=200)
    Post_date=models.DateTimeField(auto_now_add=True)
    ref_company=models.ForeignKey(Company,on_delete=models.CASCADE )
    ref_profile2=models.ForeignKey(Companyprofile,on_delete=models.CASCADE )
    
class Jobpost(models.Model):
    user=models.ForeignKey(Company,on_delete=models.CASCADE)
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    short_description = models.TextField()
    job_field=models.CharField(max_length=20)
    
    location = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    # year
    experience=models.TextField()   

    # education
    education_rqmnts=models.CharField(max_length=20)

    vacancies=models.DecimalField(max_digits=10, decimal_places=1)  
    job_type=models.CharField(max_length=100)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='job_image/',null=True,blank=True)
   

    # education=(
    # ('+2','+2'),
    # ('Degree','Degree'),
    # ('btech', 'Btech'),
    
    # )
    # experiance=(
    #     ('fresher','fresher'),
    #     ('1 year above','1 year above'),
    #     ('2-3year above','2-3year above'),
    #     ('4-5 year above ','4-5 year above ')
    # )
    
    # companyname=models.CharField(max_length=200)
    # jobname=models.CharField(max_length=200)
    # qualification=models.CharField(max_length=100,choices=education,default='+2')
    # experiances=models.CharField(max_length=100,choices=experiance,default='fresher')
    # description=models.TextField()
    # shortdes=models.TextField()
    # requiredskill=models.CharField(max_length=200)
    # vaccancy=models.IntegerField(10)
    # created=models.DateTimeField(auto_now_add=True)
    # update=models.DateTimeField(auto_now=True)
    # refmodel=models.OneToOneField(Companyprofile,on_delete=models.CASCADE)
    # ref_company=models.ForeignKey(Company,on_delete=models.CASCADE)
    
   
  


        
   
    
    
    def __str__(self) :
        return self.title     
    


class Fields(models.Model):
    fields=(
    ('IT Field','IT Field'),
    ('e-Commerce','e-Commerce'),
    ('electrical', 'Elecrical'),
    ('Auto-mobile', 'Auto-mobile'),
    ('Engeneering','Engeneering')
    

    
    )
    fields=models.CharField(max_length=200,choices=fields,default="IT Field")
    company_profile=models.ForeignKey(Companyprofile,on_delete=models.CASCADE)
    company_user=models.ForeignKey(Company,on_delete=models.CASCADE)