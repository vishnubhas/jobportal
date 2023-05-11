
from . views  import *
from django.urls import path

urlpatterns = [
    path('create_job/',create_job,name='jobcreate'),
     path('serachjob/',search_job,name="search"),
     path('job_details/<int:id>/',job_details,name='job_details'),
     path('c_index/',com_index,name='com_index'),
     path('c_profile/',com_profile,name='company_profile'),
     path('com_profileview/',profileview,name="view")
    
]                                                  