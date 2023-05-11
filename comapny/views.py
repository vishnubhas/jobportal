from django.shortcuts import render,redirect
from . models import Jobpost,Companyprofile

# Create your views here.
def create_job(request):
    if request.method=='POST':
        companyname=request.POST.get('companyname')
        jobname=request.POST.get('jobname')
        qualification=request.POST.get('qualification')
        experiance=request.POST.get('experiance')   
        description=request.POST.get('description')
        shortdesc=request.POST.get('shortdes')
        required=request.POST.get('skill') 
        vaccancy=request.POST.get('vaccancy')
        Jobpost.objects.create(
            companyname=companyname,
            jobname=jobname,
            qualification=qualification,
            experiances=experiance,
            description=description,
            shortdes=shortdesc,
            requiredskill=required,
            vaccancy=vaccancy
        )
        return redirect('search')
    context={
    'edu':Jobpost.education,
    'exp':Jobpost.experiance
    }
    return render(request,'company/jobcreate.html',context)

def search_job(request):
        search=Jobpost.objects.all()
        word=request.GET.get('keyword')
        if word:
            search=search.filter(jobname__contains=word)
        context={
            'word':word,
            "serach":search
        }
        
        
        return render(request,'jobserch.html',context)
def job_details(request,id):
    Job=Jobpost.objects.filter(id=id)
    

   
    context={
         'job':Job
        
     }
     
    return render(request,'company/jobdetails.html',context)
def com_index(request):
    return render(request,'company/c_index.html')
def com_profile(request):
    if request.method=='POST':
        companyname=request.POST.get('cname')
        
        phone=request.POST.get('cphone')
        established=request.POST.get('established')
        field=request.POST.get('field')
        email=request.POST.get('cemail')
       
        image=request.FILES.get('cimage')
        description=request.POST.get('cabout')
        quote=request.POST.get('quote')
        git=request.POST.get('cgit')
        youtube=request.POST.get('cyoutube')
        website=request.POST.get('cwebsite')
      
        street=request.POST.get('cstreet')
        city=request.POST.get('ccity')
        state=request.POST.get('cstate')
        pincode=request.POST.get('cpincode')
        work=request.POST.get('wwork')
        wabout=request.POST.get('wabout')
        wimage=request.FILES.get('wphoto')     
        Companyprofile.objects.create(
           companynames=companyname,
            
            phones=phone,
            establishes=established,
            fields=field,
            emails=email,
            quotes=quote,
            images=image,
            descriptions= description,
            gits=git,
            youtubes=youtube,
            websites=website,
            
            street=street,
            city=city,
            state=state,
            pincode=pincode,
            work=work,
            workpic=wimage,
            workdisc=wabout
            
        )
        return redirect('company_profile')
    data=Companyprofile.objects.all()
    
    context={
        "all":data
    }
    return render(request,"company/company_profile.html",context)
def profileview(request):
    profile=Companyprofile.objects.all()
    context={
        'profile':profile
    }
    return render(request,'company/profileview.html',context)




