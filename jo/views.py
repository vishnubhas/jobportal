from django.shortcuts import render,redirect
from . models import  *
from   comapny.models import *
from  django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout



# Create your views here.
@login_required(login_url='404_Error') 

def index(request):

    if request.user.role=='USER':
       
  
    
        return render (request,'user/index.html')
    else:
             return redirect('user_404_Error')

@login_required(login_url='404_Error') 
def log_profile(request):

        emp_user= Userprofile.objects.filter(  ref_user=request.user.id)
        if emp_user:
              return redirect('user_index')
        else:
                return redirect('profile')
      
@login_required(login_url='404_Error') 
def profile(request):
      
        if request.user.role=='USER':
          
  
            userprofile=Userprofile.objects.filter( ref_user=request.user.id).first()
            # job=JobApplication.objects.filter(ref_job_id=request.user.id)
        
        
        
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
                    
                        street=request.POST.get('street')
                        city=request.POST.get('city')
                        state=request.POST.get('state')
                        pincode=request.POST.get('pincode')
                        skill=request.POST.get('skill')
                        gender_2=request.POST.get('gender')
                        gender2=Gender.objects.create(  gender_choice=gender_2)  
                
                        Userprofile.objects.create(
                            ref_gender=gender2,
                        
                            name=firstname,
                            s_name=secondname,
                            phone=phone,
                            age=age,
                            email=email,
                        
                            image=image,
                            description= description,
                            git=git,
                            youtube=website,
                        
                            street=street,
                            city=city,
                            state=state,
                            pincode=pincode,
                            skill=skill,
                            ref_user=request.user,
                            

                        )
                    
                        return redirect('user_index')
        
        
            userprofile2=Userprofile.objects.filter(ref_user=request.user.id)
            userprofile=User2.objects.filter(id=request.user.id).first()
        
            context={
            
                    'userprofile':userprofile2,
                    
                    'user':userprofile,
                    
                    
                    
                }
            return render(request,'user/profileset.html',context)
        else:
             return redirect('user_404_Error')
@login_required(login_url='404_Error') 
def personal(request):
            if request.user.role=='USER':
            
                    userprofile2=Userprofile.objects.filter(ref_user=request.user.id)
            
                
                    print(userprofile2)
                    context={
                
                        'userprofile':userprofile2,
                
                    
                        
                }
                
                    return render (request,'user/personal.html',context)
            else:
                return redirect('user_404_Error')
def admin_index(request):
    admin=User2.objects.all()
    context={
                            'User':admin,
                          
                        }
    return render(request,'admin/main_index.html',context)
def error_404(request):
#  
   return render(request,'user/user_404_Error.html')
@login_required(login_url='404_Error') 
def profile_edit_user(request,id):
        if request.user.role=='USER':
                profile_edit1=Userprofile.objects.get(id=id)
                gender1=Gender.objects.get(id=id)
                if request.method == 'POST' :
                        firstname=request.POST.get('fname')
                        secondname=request.POST.get('sname')
                        phone=request.POST.get('phone')
                        age=request.POST.get('age')
                        email=request.POST.get('email')
                    
                        image=request.FILES.get('image')
                        description=request.POST.get('about')
                        git=request.POST.get('git')
                        website=request.POST.get('website')
                    
                        street=request.POST.get('street')
                        city=request.POST.get('city')
                        state=request.POST.get('state')
                        pincode=request.POST.get('pincode')
                        skill=request.POST.get('skill')
                        gender_2=request.POST.get('gender')
                        gender1. gender_choice=gender_2
                    
                        profile_edit1.name=firstname
                        profile_edit1.s_name=secondname
                        profile_edit1.phone=phone
                        profile_edit1.age=age
                        profile_edit1.email=email
                        
                        profile_edit1.image=image
                        profile_edit1.description= description
                        profile_edit1.git=git
                        profile_edit1.youtube=website
                        
                        profile_edit1.street=street
                        profile_edit1.city=city
                        profile_edit1.state=state
                        profile_edit1.pincode=pincode
                        profile_edit1.skill=skill
                        
                        
                        profile_edit1.save()

                        return redirect('personal')
                context={
                            'edit':profile_edit1,
                            'gender':gender1
                        }
                return render(request,'user/profile_edit.html',context)
        else:
                return redirect('user_404_Error')
@login_required(login_url='404_Error')
def profile_delete(request,id):
        if request.user.role=='USER':
            delete=Userprofile.objects.get(id=id)
            delete.delete(id=id)
            return redirect('profile')
        else:
                return redirect('user_404_Error')
@login_required(login_url='404_Error')
def search_job(request):
        if request.user.role=='USER':
            search=Jobpost.objects.all()
            word=request.GET.get('keyword')
            if word:
                    search=search.filter(title__contains=word)
            context={
                    'word':word,
                    "serach":search
                }              
            return render(request,'user/job.html',context)
        else:
                return redirect('user_404_Error')
@login_required(login_url='404_Error') 
def job_apply(request,id):
        if request.user.role=='USER':
               try:
                    user3=Userprofile.objects.filter(id=id)
                    job_apply=JobApplication.objects.filter(user=request.user,ref_job=id)
                    if job_apply:
                            return redirect('user_404_Error')
                    else:
                        job_obj=Jobpost.objects.get(id=id)
                        if request.method == 'POST' :
                               
                                cv=request.FILES.get('resume')
                                
                                my_obj=JobApplication.objects.create(
                                        user=request.user,
                                        ref_job=job_obj,
                                        
                                      ref_profile= user3,
                                        resume=cv,
                                      
                                    

                                )
                                my_obj.save()
                                return redirect('user_index')
                        print(user3)
                      
                        return render(request,'user/jobapply_from.html')
               except(FileNotFoundError):
                      return redirect('user_404_Error')
        else:
                return redirect('user_404_Error')
@login_required(login_url='404_Error') 
def user_com_profile(request,id):
        if request.user.role=='USER':
               profile2=Companyprofile.objects.get(id=id)
            #    recent=RecentWork.objects.filter(id=request.user.id)
            #    print(recent)
               context={
                        'data':profile2,
                        #  'work':recent
                        
                    }   
               return render(request,'user/user_com_profile.html',context)
          
        else:
                return redirect('user_404_Error')