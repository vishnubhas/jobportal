
from . views  import *
from django.urls import path

urlpatterns = [
path('user_index/' ,index,name='user_index'),
    
    path('profile/',profile,name='profile'),
    path('profileviwe/',personal,name='personal'),
    path('',admin_index,name="index"),
    path('user_404_Error/',error_404,name='user_404_Error'),
    path('log_profile/',log_profile,name='logging_profile'),
    path('profile/<int:id>/edit/',profile_edit_user,name='edit'),
    path('profile/<int:id>/delete/',profile_delete,name='profile_delete'),
    path('serachjob/',search_job,name="search"),
    path('job/<int:id>/apply',job_apply,name="jobapply"),
    path('com/<int:id>/viwe/',user_com_profile,name="com"),
    path('comrecent/',comrecent_post_detail,name="comrecent"),
    path('already_applied/',error_job,name="error_job"),
    path('job/history/',job_history,name='job_history'),
    path('job/<int:id>/details',job_details_history,name='job_de_history'),
    path('education/',education,name='education'),
    path('work/expeeraince/',workexperiance,name='work_experiance'),
    path('project/add/',project,name='project'),
    path('it/skills/add/',itskill,name='itskill'),
    path('certificate/add/',certificate,name='certificate'),
    path('language/add',language,name='lang'),
    path('del/<int:id>/',language_delete,name='l_d'),
    path('soft/skill/',softskill,name='sskill'),
    path('del/<int:id>/',sskill_delete,name='s_d'),
    # path('user/<int:id>/profile' ,user_profile,name='user_profile')
 
                    
]