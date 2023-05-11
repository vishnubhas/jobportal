from django.db import models
from account.models import Company


# Create your models here.
class Admin_view(models.Model):
    approvel=models.BooleanField(default=False)
    ref_comapany_name=models.ForeignKey(Company,on_delete=models.CASCADE)