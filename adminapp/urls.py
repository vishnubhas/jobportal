
from . views  import *
from django.urls import path

urlpatterns = [
            path('admin/',admin_view,name='admin'),
            path('com_request/',company_request,name="com_request"),
            path('acc/<int:id>/',com_request
                 ,name='accept'),
            path('user/details/',user_details,name='u_details')
            
            
]