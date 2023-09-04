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
      

# PROFILE SECTION OF USER

#creating a profile
@login_required(login_url='404_Error') 
def profile(request):
      
        if request.user.role=='USER':
          
  
            userprofile=Userprofile.objects.filter( ref_user=request.user.id).first()
            # job=JobApplication.objects.filter(ref_job_id=request.user.id)
            print(userprofile)
            if userprofile:
                   return redirect('user_index')
        
            else:
        
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
                                ref_gender=gender2,name=firstname,s_name=secondname,phone=phone,age=age,email=email,image=image,description= description,git=git,youtube=website,street=street,city=city,state=state,pincode=pincode,skill=skill,ref_user=request.user,
                                

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
        
#profile view by user
@login_required(login_url='404_Error') 
def personal(request):
            if request.user.role=='USER':
            
                    userprofile2=Userprofile.objects.filter(ref_user=request.user.id)
                    education=Educations.objects.filter(ref_user=request.user.id)
                    workexperiance=Workexperiance.objects.filter(ref_user=request.user.id)
                    project=Projects.objects.filter(ref_user=request.user.id)
                    itskill=ITskills.objects.filter(ref_user=request.user.id)
                    certificate=Certificates.objects.filter(ref_user=request.user.id)
                    language=Language.objects.filter(user=request.user.id)
                    soft=Softskill.objects.filter(user=request.user.id)
                
                    print(certificate)
                    context={
                           'certificate':certificate,
                        'project':project,
                        'userprofile':userprofile2,
                        'education':education,
                        'work':workexperiance,
                        'skill':itskill,
                        "lang":language,
                        "softskill":soft
                
                    
                        
                }
                
                    return render (request,'user/profile.html',context)
            else:
                return redirect('user_404_Error')
def admin_index(request):
    admin=User2.objects.count()
    com=Company.objects.count()
    context={
                            'user':admin,
                            'com':com
                          
                        }
    return render(request,'admin/main_index.html',context)
def error_404(request):
 
   return render(request,'user/user_404_Error.html')

#profile edit section

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
       
#profile delete sections

@login_required(login_url='404_Error')
def profile_delete(request,id):
        if request.user.role=='USER':
            delete=Userprofile.objects.get(id=id)
            delete.delete(id=id)
            return redirect('profile')
        else:
                return redirect('user_404_Error')

#COMPANY DETAILS FOR USER


@login_required(login_url='404_Error') 
def user_com_profile(request,id):
        if request.user.role=='USER':
               Job=Jobpost.objects.filter(id=id).first()
               print(Job.user)
               
               profile2=Companyprofile.objects.filter(ref_profle=Job.user)
               print(profile2)
               recent=RecentWork.objects.all()
              #  print(recent)
               context={
                        'data':profile2,
                         'work':recent
                        
                    }   
               return render(request,'user/user_com_profile.html',context)
          
        else:
                return redirect('user_404_Error')

#rencent post details of company

@login_required(login_url='404_Error') 
def  comrecent_post_detail(request):
       if request.user.role=='USER':
                recent=RecentWork.objects.filter(ref_profile2=request.user.id).first()
                all=RecentWork.objects.all()
                print(recent)
                
                
                context={
                      
                         
                         'data':all,
                         
                         
                        
                    }   
                return render(request,'user/comrecent_post_detail.html',context)
          
       else:
                return redirect('user_404_Error')
#DEFINING JOB DETAILS

@login_required(login_url='404_Error')
def search_job(request):
        if request.user.role=='USER':
            search=Jobpost.objects.all()
          
            word=request.GET.get('keyword')
            if word:
                    search=search.filter(title__contains=word)
            context={
                    'word':word,
                    "serach":search,
                    
                }              
            return render(request,'user/job.html',context)
        else:
                return redirect('user_404_Error')




#job application form
@login_required(login_url='404_Error') 
def job_apply(request,id):
        if request.user.role=='USER':
               
                    user3=Userprofile.objects.filter(ref_user=request.user.id).first()
                    job_obj=Jobpost.objects.get(id=id)
                    applicante=JobApplication.objects.filter(user=request.user.id).first()
                    print(applicante)
                    if applicante:
                        job_apply=JobApplication.objects.filter(user_id=request.user.id,ref_job_id=id)
                        print(job_apply)
                        print(job_obj)
                        if job_apply:
                                return redirect('error_job')
                   
                    
                    
                    if request.method == 'POST' :
                               
                                cv=request.FILES.get('resume')
                                
                                my_obj=JobApplication.objects.create(
                                        user=request.user,
                                        ref_job=job_obj,
                                        
                                      ref_profile= user3,
                                        resume=cv,
                                        is_accepted=False
                                      
                                    

                                )
                                my_obj.save()
                                return redirect('user_index')
                     
                      
                    return render(request,'user/jobapply_from.html')
            
        else:
                return redirect('user_404_Error')

#job error page
def error_job(request):


        return render(request,'user/error_job.html')

#job history (how many job applied by user)full details

@login_required(login_url='404_Error') 
def  job_history(request):
       if request.user.role=='USER':
              history=JobApplication.objects.filter(user=request.user.id)
              
             
             
             
              context={
                        
                         'history':history,
                        
                    }   
              return render(request,'user/job_history.html',context)
          
       else:
                return redirect('user_404_Error')
       
#job full details for user

@login_required(login_url='404_Error')
def job_details_history(request,id):
       job=Jobpost.objects.filter(user=request.user.id)
      
       print(job)
      
        
       context={
              'job':job
             
       }
       return render(request,'user/job_details_history.html',context)

#ADDING EXTRA DETAILS TO THE USER PROFILE

# adding education

@login_required(login_url='404_Error') 
def  education(request):
       if request.user.role=='USER':
              user=User2.objects.filter(id=request.user.id).first()
              userprofile=Userprofile.objects.filter(ref_user=request.user.id).first()
              if request.method == 'POST':
                     institute=request.POST.get('institute')
                     department=request.POST.get('department')
                     date=request.POST.get('date')
                     edate=request.POST.get('edate')
                     Educations.objects.create(user=userprofile,ref_user=user, college=institute,department=department,start=date,end=edate).save()
                     return redirect('personal')

              return render(request,'user/education.html')
       else:
                return redirect('user_404_Error')
       
#adding workexperiance

@login_required(login_url='404_Error') 
def   workexperiance(request):
       if request.user.role=='USER':
              user=User2.objects.filter(id=request.user.id).first()
              userprofile=Userprofile.objects.filter(ref_user=request.user.id).first()
              if request.method == 'POST':
                     title=request.POST.get('title')
                     position=request.POST.get('position')
                     date=request.POST.get('date')
                     edate=request.POST.get('edate')
                     description=request.POST.get('description')
                     Workexperiance.objects.create(user=userprofile,ref_user=user, title=title,position=position,stating_date=date,end_date=edate,discription=description).save()
                     return redirect('personal')

              return render(request,'user/workexperiance.html')
       else:
                return redirect('user_404_Error')
       
#adding projects
@login_required(login_url='404_Error') 
def   project(request):
       if request.user.role=='USER':
              user=User2.objects.filter(id=request.user.id).first()
              userprofile=Userprofile.objects.filter(ref_user=request.user.id).first()
              if request.method == 'POST':
                     project=request.POST.get('project')
                    
                     date=request.POST.get('date')
                     edate=request.POST.get('edate')
                     description=request.POST.get('description')
                     Projects.objects.create(user=userprofile,ref_user=user,project=project,start=date,end=edate,description=description).save()
                     return redirect('personal')

              return render(request,'user/project.html')
       else:
                return redirect('user_404_Error')

#adding ITskills

@login_required(login_url='404_Error') 
def   itskill(request):
       if request.user.role=='USER':
              user=User2.objects.filter(id=request.user.id).first()
              userprofile=Userprofile.objects.filter(ref_user=request.user.id).first()
              if request.method == 'POST':
                     
                     skill=request.POST.get('skill')
                     version=request.POST.get('version')
                     last_used=request.POST.get('used')
                     experiance=request.POST.get('experiance')
                     ITskills.objects.create(user=userprofile,ref_user=user,skills=skill,vertion=version,last_used=last_used,experiance=experiance).save()
                     return redirect('personal')

              return render(request,'user/itskill.html')
       else:
                return redirect('user_404_Error')
#adding certificate

@login_required(login_url='404_Error') 
def   certificate(request):
       if request.user.role=='USER':
              user=User2.objects.filter(id=request.user.id).first()
              userprofile=Userprofile.objects.filter(ref_user=request.user.id).first()
              if request.method == 'POST':
                     company_name=request.POST.get('name')
                     certificate=request.POST.get('cname')
                     file=request.FILES.get('certificate')
                  
                     Certificates.objects.create(user=userprofile,ref_user=user,company=company_name,certificate_name=certificate,certificate=file).save()
                     return redirect('personal')

              return render(request,'user/certificate.html')
       else:
                return redirect('user_404_Error')
#adding language
@login_required(login_url='404_Error') 
def   language(request):
       if request.user.role=='USER':
              user=User2.objects.filter(id=request.user.id).first()
              userprofile=Userprofile.objects.filter(ref_user=request.user.id).first()
              if request.method == 'POST':
                     lang=request.POST.get('lang')
                     experiance=request.POST.get('experiance')
                     Language.objects.create(user=user,ref_user=userprofile,language=lang,level=experiance)
                     return redirect('personal')
              return render(request,"user/language.html")
              
       else:
                return redirect('user_404_Error')
#adding language delete
@login_required(login_url='404_Error')
def language_delete(request,id):
        if request.user.role=='USER':
            delete=Language.objects.get(id=id)
            delete.delete()
            return redirect('personal')
        else:
                return redirect('user_404_Error')
#adding softskill
@login_required(login_url='404_Error') 
def  softskill(request):
       if request.user.role=='USER':
              user=User2.objects.filter(id=request.user.id).first()
              userprofile=Userprofile.objects.filter(ref_user=request.user.id).first()
              if request.method == 'POST':
                     lang=request.POST.get('skill')
                    
                     Softskill.objects.create(user=user,ref_user=userprofile,softskill=lang)
                     return redirect('personal')
              return render(request,"user/softskill.html")
              
       else:
                return redirect('user_404_Error')

#adding softskill delete

@login_required(login_url='404_Error')
def sskill_delete(request,id):
       
            delete=Softskill.objects.get(id=id)
            delete.delete()
            return redirect('personal')

              
