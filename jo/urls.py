
from . views  import *
from django.urls import path

urlpatterns = [
path('user_index/' ,index,name='user_index'),
    path('upload_cv/',resume,name='upload_cv'),
    path('profile/',profile,name='profile'),
    path('profileviwe/',personal,name='personal'),
    path('',admin_index,name="index")
   
]