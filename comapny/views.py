from django.shortcuts import render,redirect
from . models import *
from  django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from  jo.models import *
# Create your views here.
@login_required(login_url='404_Error')
def create_job(request):
  
        if request.user.role=='COMPANY':
            

            

                jobpost =Company.objects.filter(id=request.user.id).first() 
                profile=Companyprofile.objects.filter( ref_profle=request.user.id)
              
                
                if not profile :
                    return redirect('com_profile_create')
            
            
                if jobpost:
                    if request.method=='POST':
                            title=request.POST.get('title')
                            field=request.POST.get('field')
                            location=request.POST.get('location')
                            education=request.POST.get('education')
                            salary=request.POST.get('salary')
                            description=request.POST.get('description')
                            shortdes=request.POST.get('shortdes')
                            vaccancy=request.POST.get('vaccancy')
                            type=request.POST.get('type')
                            experience=request.POST.get('experience')
                            image=request.FILES.get('image')
                            Jobpost.objects.create(
                                title=title,description=description,short_description=shortdes,job_field=field,location=location,salary = salary,education_rqmnts=education,vacancies=vaccancy,job_type=type,experience=experience,image=image,user=request.user,
                            )


            
                            return redirect('com_index')

                return render(request,'company/jobcreate.html')
        else:
               return redirect('company_404_Error')
@login_required(login_url='404_Error')
def job_edit(request,id):
  
        if request.user.role=='COMPANY':
              job_edit=Jobpost.objects.get(id=id)

              if request.method=='POST':
                            title=request.POST.get('title')
                            field=request.POST.get('field')
                            location=request.POST.get('location')
                            education=request.POST.get('education')
                            salary=request.POST.get('salary')
                            description=request.POST.get('description')
                            shortdes=request.POST.get('shortdes')
                            vaccancy=request.POST.get('vaccancy')
                            type=request.POST.get('type')
                            experience=request.POST.get('experience')
                            image=request.FILES.get('image')
                            job_edit.title=title
                            job_edit.description=description
                            job_edit.short_description=shortdes
                            job_edit.job_field=field
                            job_edit.location=location
                            job_edit.salary =salary 
                            job_edit.education_rqmnts=education
                            job_edit.vacancies=vaccancy
                            job_edit.job_type=type
                            job_edit.experience=experience
                            job_edit.image=image
                            job_edit.save()
                            return redirect('job_details')
              context={
                     'job':job_edit
              }
              return render(request,'company/job_edit.html',context)
              


        else:
               return redirect('company_404_Error')
@login_required(login_url='404_Error')  
def job_delete(request,id):
    if request.user.role=='COMPANY':
          
        delete=Jobpost.objects.filter(id=id)
        delete.delete()
        return redirect('com_index')
    else:
               return redirect('company_404_Error')
@login_required(login_url='404_Error')  
def job_details(request,id):
    if request.user.role=='USER':
        Job=Jobpost.objects.filter(id=id)
        j=Jobpost.objects.filter(id=id).first()
        

        print(j)
        userprofile=User2.objects.filter(id=request.user.id).first()
        user=Userprofile.objects.filter(ref_user=request.user.id).first()
        
        # print(jobpost)
        print(userprofile)
        print(user)
        if request.method == 'POST' :
                   comment=request.POST.get('comment')
                   Jobcomments.objects.create(ref_profile=user,user=userprofile,comment=comment,jobpost=j)
        comment1=Jobcomments.objects.filter(jobpost=j)
        print(comment1)
        total=comment1.count()
        
        
        context={
            'job':Job,
            'total':total,
            'comment':comment1
            
            
        }
        
        return render(request,'company/jobdetails.html',context)
    else:
                return redirect('user_404_Error')
@login_required(login_url='404_Error')
def com_index(request):  
    
         if request.user.role=='COMPANY':
             

    
            job=Jobpost.objects.filter( user=request.user.id)
            company=Companyprofile.objects.filter(ref_profle=request.user.id)
            print(company)
            context={
                'job':job,
                'company':company
            
            }
            return render(request,'company/c_index.html',context)
         else:
               return redirect('company_404_Error')
@login_required(login_url='404_Error')
def com_profile_create(request):
    
            if request.user.role=='COMPANY':
             

                profile=Company.objects.filter(id=request.user.id).first()
                user=Companyprofile.objects.filter( ref_profle=request.user.id)
                print(user)
                if user:
                    return redirect('com_index')
                else :
                    
                        if request.method=='POST':
                            companyname=request.POST.get('cname')
                            
                            phone=request.POST.get('cphone')
                            established=request.POST.get('established')
                        
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
                            
                            Companyprofile.objects.create(
                            companynames=companyname,
                                
                                phones=phone,
                                establishes=established,
                                
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
                                ref_profle=request.user,
                              
                                 is_request = False
                            
                            ) 
                            is_request1=Companyprofile.objects.filter(ref_profle=request.user.id , is_request=False)
                            if is_request1:
                                   return redirect('request_mes')
                        
                            return redirect('com_index')

                    
                return render(request,"company/company_profile.html")
            else:
               return redirect('company_404_Error')
@login_required(login_url='404_Error')
def request_mes(request):
       return render(request,'admin/request_mes.html')
def approvel(request):
    logout(request)
    return redirect('login')

def  company_profile_edit(request,id):
 
            profile_edit1=Companyprofile.objects.get(id=id)
            if request.method=='POST':
                            companyname=request.POST.get('cname')
                            
                            phone=request.POST.get('cphone')
                            established=request.POST.get('established')
                        
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
                            profile_edit1.companynames=companyname
                                
                            profile_edit1.phones=phone
                            profile_edit1.establishes=established
                                
                            profile_edit1.emails=email
                            profile_edit1.quotes=quote
                            profile_edit1.images=image
                            profile_edit1.descriptions= description
                            profile_edit1.gits=git
                            profile_edit1.youtubes=youtube
                            profile_edit1.websites=website
                                
                            profile_edit1.street=street
                            profile_edit1.city=city
                            profile_edit1.state=state
                            profile_edit1.pincode=pincode
                            profile_edit1.save()
                            return redirect('view')
            context={
                        'data1':profile_edit1
                        }
            
            return render(request,"company/company_profile_edit.html",context)
   
                               
                            


@login_required(login_url='404_Error')
def Recentwork_add(request):
     
            if request.user.role=='COMPANY':
         

                company=Company.objects.filter(id=request.user.id).first()
                profile=Companyprofile.objects.filter(ref_profle=request.user.id).first()
    
                print(profile)
             
                if company :
                        if request.method == 'POST' :
                            works=request.POST.get('works')
                            image=request.FILES.get('image')
                            short_dic=request.POST.get('shortdic')
                            long_dic=request.POST.get('longdic')
                            addwork=RecentWork.objects.create(
                            
                            work=works,
                            image=image,
                                short_dic= short_dic,
                                long_dic= long_dic,
                                ref_company=request.user,
                                ref_profile2=profile


                            )   
                            addwork.save()
                            return redirect('view')
                    
                return render(request,'company/recentwork.html',)
            else:
               return redirect('company_404_Error')
@login_required(login_url='404_Error')
def profileview(request):
    if request.user.role=='COMPANY':
                
        profile=Companyprofile.objects.filter( ref_profle=request.user.id)
        work1=RecentWork.objects.filter(ref_company=request.user.id)
        print(profile)
        context={
            'profile':profile,
            'work':work1
        }
        return render(request,'company/profileview.html',context)
    else:
               return redirect('company_404_Error')
@login_required(login_url='404_Error')
def recent_post_detail(request):
    if request.user.role=='COMPANY':
                
        data=RecentWork.objects.filter(ref_company=request.user.id)
        all=RecentWork.objects.all()
        context={
        'data1':data,
        'all':all
        }

        return render(request,'company/recent_post_detail.html  ',context)
    else:
               return redirect('company_404_Error')
@login_required(login_url='404_Error')
def recent_post_edit(request,id):
    if request.user.role=='COMPANY':
             
        Edit=RecentWork.objects.get(id=id)
        
    
        if request.method == 'POST' :
                works=request.POST.get('works')
                image=request.FILES.get('image')
                short_dic=request.POST.get('shortdic')
                long_dic=request.POST.get('longdic')
            
                
                Edit.work=works
                Edit.image=image
                Edit.short_dic= short_dic
                Edit.long_dic= long_dic
                
        

                
                Edit.save()
                return redirect('view' )
        context={
        'edit':Edit
        }

        
        return render(request,'company/recentwork_edit.html',context)
    else:
               return redirect('company_404_Error')
@login_required(login_url='404_Error')  
def recent_post_delete(request,id):
    if request.user.role=='COMPANY':
          
        delete=RecentWork.objects.filter(id=id)
        delete.delete()
        return redirect('view')
    else:
               return redirect('company_404_Error')
def error(request):
  
    return render(request,'company/login_error.html')
@login_required(login_url='404_Error')  
def Skip(request):
     if request.user.role=='COMPANY':
            
        return redirect('com_index')
     else:
               return redirect('company_404_Error')
@login_required(login_url='404_Error')  
def about(request):
    if request.user.role=='COMPANY':
            
        profile=Companyprofile.objects.filter( ref_profle=request.user.id)
        work1=RecentWork.objects.filter(ref_company=request.user.id)
    
        print(profile)
        context={
            'profile':profile,
            'work':work1
        }
        return render(request,'company/about.html',context)
    else:
               return redirect('company_404_Error')
def company_error(request):

   return render(request,'company/company_404_Error.html')
@login_required(login_url='404_Error')  
def job_confirm(request,id):
        if request.user.role=='COMPANY':
              job_confirm2=JobApplication.objects.get(id= id)
              print(job_confirm2)
              image=Userprofile.objects.filter(image=request.user.id)
              context={
                'job':job_confirm2,
                  'image':image
                
            }
      
              return render(request,'company/job_confirm.html',context)
        else:
               return redirect('company_404_Error')
        
@login_required(login_url='404_Error')  
def job_view(request,id):
        if request.user.role=='COMPANY':
              jobpost=Jobpost.objects.filter(id=id).first()
              print(jobpost)
              #creating replay sections
              company=Jobcomments.objects.filter(id=id).first()
              user=company.ref_profile
              print(company)
              company_profile=Companyprofile.objects.filter(ref_profle=request.user.id).first()
              if request.method =="POST":
                     replay=request.POST.get('replay')
                     Replay.objects.create(jobcomments=company,user_profile=user,ref_profile=company_profile,replay=replay,job=jobpost)
                     #ending of replay section
              #getting repalys
              repaly1=Replay.objects.filter(user_profile=user)
              total_rpaly=repaly1.count()
              print(repaly1)
              comment1=Jobcomments.objects.filter(jobpost=jobpost)
            #   print(comment1)
              total=comment1.count()
              user=JobApplication.objects.filter(ref_profile_id=id)
            #   print(user)
              jo=JobApplication.objects.filter(ref_job=jobpost)              
              job1=JobApplication.objects.filter(ref_job=id)
              job_list=Jobpost.objects.filter(id=id)
             
              
              print(jo)
              context={
                'job':job_list,
                  'job1':job1,
                   'total':total,
            'comment':comment1,
            'repaly':repaly1,
            "total_replay":total_rpaly,
            'jo':jo

                  
                
              
                
            }
            
              return render(request,'company/job_view.html',context)
        else:
               return redirect('company_404_Error')
@login_required(login_url='404_Error')
def job_invite(request,id):
       if request.user.role =='COMPANY':
            cmp_obj=JobApplication.objects.get(id=id)
            print(cmp_obj)
            cmp_obj.is_accepted = not cmp_obj.is_accepted
            cmp_obj.save()
            return redirect('com_index')
   
@login_required(login_url='404_Error')  
def user_profile_view(request,id):
        if request.user.role=='COMPANY':
            company=Company.objects.filter(id=request.user.id)
            jo=JobApplication.objects.get(id=id).user
            print(company)
            user=Userprofile.objects.filter(ref_user=jo).first()
            print(user)
            work=Workexperiance.objects.filter(ref_user_id=jo).first()
            education=Educations.objects.filter(ref_user_id=jo).first()
            project=Projects.objects.filter(ref_user_id=jo).first()
            certificate=Certificates.objects.filter(ref_user_id=jo).first()
            itskill=ITskills.objects.filter(ref_user_id=jo).first()
            print(itskill)
            lang=Language.objects.filter(user_id=jo).first()
            soft=Softskill.objects.filter(user_id=jo).first()
            context={
                    "user_data":user,
                    "work":work,
                    'education':education,
                    'project':project,
                   'certificate':certificate,
                   'skill':itskill,
                    'lang':lang,
                    'soft':soft,
                    'company':company
            }
            return render(request,'company/user_profile.html',context)