from django.shortcuts import render,redirect
from . models import Userprofile
from   comapny.models import Jobpost,Companyprofile


# Create your views here.
def index(request):
    
    return render (request,'index.html')



def resume(request):
    if request.method=="POST":
        cv=request.POST.get('cv')
        return redirect('user_index')
    return render (request,'resume.html')
def profile(request):
   
    if request.method=='POST':
        firstname=request.POST.get('fname')
        secondname=request.POST.get('sname')
        phone=request.POST.get('phone')
        age=request.POST.get('age')
        email=request.POST.get('email')
       
        image=request.FILES.get('image')
        description=request.POST.get('about')
        git=request.POST.get('git')
        website=request.POST.get('website')
        linkedin=request.POST.get('linkedin')
        street=request.POST.get('street')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincode=request.POST.get('pincode')
        skill=request.POST.get('skill')
             
        Userprofile.objects.create(
            name=firstname,
            s_name=secondname,
            phone=phone,
            age=age,
            email=email,
           
            image=image,
            description= description,
            git=git,
            youtube=website,
            linkedin=linkedin,
            street=street,
            city=city,
            state=state,
            pincode=pincode,
            skill=skill
        )
        return redirect('profile')
    all=Userprofile.objects.all()
    
    context={
        'all':all
        
        
    }
    return render(request,'profileset.html',context)
def personal(request):
    profile=Userprofile.objects.all()
    context={
        'profile':profile
    }
    
    return render (request,'personal.html',context)
def admin_index(request):
    return render(request,'admin/main_index.html')