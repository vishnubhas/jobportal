
from . views  import *
from django.urls import path

urlpatterns = [
    path('company_register/',company_register,name='company_register'),
    path('login/',login_view,name='login'),
    path('user_register/',user_register,name='user_register'),
    path('logout/',logout_view,name='logout'),
    path('alert/',alert,name='alert'),
   
]