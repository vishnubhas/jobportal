
from . views  import *
from django.urls import path

urlpatterns = [
    path('create_job/',create_job,name='jobcreate'),
    path('job/<int:id>/edit/',job_edit,name='job_edit'),
    path('job/<int:id>/delete/',job_delete,name='job_delete'),

     path('job_details/<int:id>/',job_details,name='job_details'),
     path('c_index/',com_index,name='com_index'),
     path('c_profile/',com_profile_create,name='com_profile_create'),
     path('com_profileview/',profileview,name="view"),
     path('recent/work_add/',Recentwork_add,name='recent_add'),
     path('recent/post_detail',recent_post_detail,name='recent_post_detail'),
     path('recent/<int:id>/post_edit/',recent_post_edit,name='recent_post_edit'),
     path('recent/<int:id>/post_delete  /',recent_post_delete,name='recent_post_delete'),
     path('404_Error/',error,name="404_Error"),
     path('skip/',Skip,name="skip"),
     path('about/',about,name="com_about"),
     path('company_404_Error/',company_error,name="company_404_Error"),
     path('company_profile/<int:id>/edit/',company_profile_edit,name='profile_edit2'),
    #  path('job/<int:id>/applicant/',job_confirm,name="job_confirm"),
      path('job/<int:id>/applicant/',job_view,name="job_view"),
    
    path('request/mes/',request_mes,name='request_mes'),
    path('go/back',approvel,name='approvel'),
    path('user/<int:id>/profile/',user_profile_view,name='user_profile'),
    path("job/<int:id>/invitation/",job_invite,name='invite')
    
      


    
]                                                  