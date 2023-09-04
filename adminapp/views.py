
from django.shortcuts import render,redirect
from  account. models import *
from jo.models import *
from  comapny. models import *
from  django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='404_Error')
def admin_view(request):
    return render (request,'admin/admin_home.html')
@login_required(login_url='404_Error')
def company_request(request):
     if request.user.role=='ADMIN':
        request1=Companyprofile.objects.all()
        print(request1)
        context={
            "request":request1
        }
        return render(request,'admin/com_request.html',context)
     else:
         return redirect('user_404_Error')

@login_required(login_url='404_Error')
def com_request(request,id):
    
        cmp_obj=Companyprofile.objects.get(id=id)
        
        cmp_obj.is_request = not cmp_obj.is_request
        cmp_obj.save()
        return redirect('com_request')
@login_required(login_url='404_Error')
def user_details(request):
     user=Userprofile.objects.all()
     context={
          'user':user
     }
     return render(request,'admin/user_details.html',context)