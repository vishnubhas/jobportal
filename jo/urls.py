
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
]