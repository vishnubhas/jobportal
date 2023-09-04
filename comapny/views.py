from django.shortcuts import render,redirect
from . models import *
from  django.contrib.auth.decorators import login_required
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
                                title=title,
                                description=description,
                                short_description =shortdes,
                                job_field=field,
                                location=location,
                                salary = salary ,
                                education_rqmnts=education,
                                vacancies=vaccancy,
                                job_type=type,
                                experience=experience,
                                image=image,
                                user=request.user,
                                
                            



                            )


            
                            return redirect('com_index')

                return render(request,'company/jobcreate.html')
        else:
               return redirect('company_404_Error')


def job_details(request,id):
    Job=Jobpost.objects.filter(id=id)
  
    

   
    context={
         'job':Job,
        
        
     }
     
    return render(request,'company/jobdetails.html',context)
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
                if user:
                    return redirect('com_index')
                else :
                    if profile:
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
                              
                                #  is_request = False
                            
                            ) 
                        
                            return redirect('com_index')

                    
                return render(request,"company/company_profile.html")
            else:
               return redirect('company_404_Error')

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
                profile=Companyprofile.objects.filter(ref_profle=request.user.id)
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
        context={
        'data1':data
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
              ref_profile=Userprofile.objects.filter(ref_job=id)
              job1=JobApplication.objects.filter(ref_job=id)
              job_list=Jobpost.objects.filter(id=id)
              print(ref_profile)
              context={
                'job':job_list,
                  'job1':job1,
                  'joprofile':ref_profile
                
            }
            
              return render(request,'company/job_view.html',context)