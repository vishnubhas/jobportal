from . models import User1,User2,Company
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,redirect
from django.contrib import messages
from adminapp.models import Admin_view
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
                password=password
                
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
                approvel=Admin_view.objects.filter(approvel=False)
                if  approvel:
                    
                    return redirect('login')
                else:
                    messages.success(request,"wait for the approvel!")
                    return redirect('com_index')
            elif request.user.role=="USER":
                return redirect('user_index')
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

