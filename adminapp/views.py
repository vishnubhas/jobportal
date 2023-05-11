from django.shortcuts import render
from  account. models import Company
from jo.models import Userprofile,User2
# Create your views here.
def admin_view(request):
    return render (request,'admin/admin.html')
def company_view(request):
    
    company=Company.objects.filter()
    context={
            'comapny':company
        }

    return render(request,'admin/company_view.html',context)