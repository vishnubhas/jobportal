from django.db import models

from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver 
# Create your models here.
class User1(AbstractUser):
    class Role(models.TextChoices):
        ADMIN='ADMIN','Admin'
        USER='USER','user'
        COMPANY='COMPANY','company'
    base_role=Role.ADMIN
    role=models.CharField(max_length=100,choices=Role.choices)
    def save(self,*args,**kwargs):
        if not self.pk:
            self.role=self.base_role
        return super().save(*args,**kwargs)
class UserManger(BaseUserManager):
    def get_queryset(self,*args,**kwargs) :
        result= super().get_queryset(*args,**kwargs)
        return result.filter(role=User1.Role.USER)
class User2(User1):
    base_role=User1.Role.USER
    user=UserManger()
    class Meta:
        proxy=True
    def wel(self):
        return 'only for user'

    

class ComapnyManger(BaseUserManager):
    def get_queryset(self,*args,**kwargs) :
        result= super().get_queryset(*args,**kwargs)
        return result.filter(role=User1.Role.COMPANY)
class Company(User1):
    
    base_role=User1.Role.COMPANY
    user=UserManger()
    class Meta:
        proxy=True
    def wel(self):
        return 'only for company'
    
    


