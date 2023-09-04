from . models import User1,User2,Company
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.contrib import messages
from adminapp.models import Admin_view
from comapny.models import *
from  jo.models import *
# Create your views here.
def company_register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('firstname')
        email=request.POST.get('email')
        cpassword=request.POST.get('cpassword')
        password=request.POST.get('password')
        user=Company.objects.filter(username=username)
        if not user:
            if password==cpassword:
                Company.objects.create_user(
                username=username,
                first_name=first_name,
                email=email,
                password=password,
                
                
        )
                
                return redirect('login')
            else:
                messages.error(request,"password mismatch")
        else:
            messages.error(request,'username already exist!!')
            return redirect('company_register')

    return render(request,'account/register.html')
def user_register(request):
    if request.method=='POST':
        username=request.POST.get('username')
        first_name=request.POST.get('firstname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        user=User2.objects.filter(username=username)
        if not user:
            if password==cpassword:
                User2.objects.create_user(
                username=username,
                first_name=first_name,
                email=email,
                password=password
                
            )   
               
                messages.success(request,'User registration completed')
                return redirect('login')
            else:
                messages.error(request,"password mismatch")

        else:
                
            messages.error(request, 'username is incorrect')
            return redirect('user_register')
    return render(request,'account/register.html')

def login_view(request):
    if request.method =="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        log=authenticate(request,username=username,password=password)
        if log is not None:
            login(request,log)
            if request.user.role=="COMPANY":
                    is_request1=Companyprofile.objects.filter(ref_profle=request.user.id , is_request=False)
                    print(is_request1)
                    if is_request1  :
                        messages.success(request,'register is completed and wait for admin approvel')
                        return redirect('login')
                    
                    else:
               
                        return redirect('com_profile_create')
            elif request.user.role=="USER":
                return redirect('profile')
            elif request.user.role=="ADMIN":
                return redirect('admin')
            
        else:
            messages.error(request,'password or username is incorrect')
            return redirect('login')
    return render(request,'account/login.html')
def logout_view(request):
    logout(request)
    return redirect('login')
def forgot_password(request):
    
    return render('account/forgot.html')

    
def alert(request):
    return render(request,'account/alert.html')

def page_not(request, exception):
    return render(request,'account/404_pagenot.html')

def error_500(request):
    userprofile=Userprofile.objects.filter( ref_user=request.user.id).first()
    user=Companyprofile.objects.filter( ref_profle=request.user.id)
    print(userprofile)
    print(user)
    context={
        'userprofile':userprofile,
        "user":user
    }
    return render(request,'account/500_error.html',context)
# def error_403(request,exception):
#     return render(request,'account/error_403.html')
