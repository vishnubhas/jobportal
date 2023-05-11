from django.db import models
from account.models import Company
from adminapp.models import Admin_view

# Create your models here.

class  Companyprofile(models.Model):
    fields=(
    ('IT Field','IT Field'),
    ('e-Commerce','e-Commerce'),
    ('electrical', 'Elecrical'),
    ('Auto-mobile', 'Auto-mobile'),
    ('Engeneering','Engeneering')
    

    
    )
    companynames=models.CharField(max_length=250)
    fields=models.CharField(max_length=200,choices=fields,default="IT Field")
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
    work=models.CharField(max_length=200) 
    workpic=models.ImageField(upload_to='work_image/',null=True,blank=True)
    workdisc=models.TextField()
    ref_comodel=models.ForeignKey(Company,on_delete=models.CASCADE)  
    ref_admin=models.OneToOneField(Admin_view,on_delete=models.CASCADE)
    def __str__(self) :
        return self.companynames
class Jobpost(models.Model):
    education=(
    ('+2','+2'),
    ('Degree','Degree'),
    ('btech', 'Btech'),
    
    )
    experiance=(
        ('fresher','fresher'),
        ('1 year above','1 year above'),
        ('2-3year above','2-3year above'),
        ('4-5 year above ','4-5 year above ')
    )
    
    companyname=models.CharField(max_length=200)
    jobname=models.CharField(max_length=200)
    qualification=models.CharField(max_length=100,choices=education,default='+2')
    experiances=models.CharField(max_length=100,choices=experiance,default='fresher')
    description=models.TextField()
    shortdes=models.TextField()
    requiredskill=models.CharField(max_length=200)
    vaccancy=models.IntegerField(10)
    created=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    refmodel=models.OneToOneField(Companyprofile,on_delete=models.CASCADE)
    ref_company=models.ForeignKey(Company,on_delete=models.CASCADE)
    
   
  


        
   
    
    
    def __str__(self) :
        return self.jobname