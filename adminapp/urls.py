
from . views  import *
from django.urls import path

urlpatterns = [
            path('admin_view/',admin_view,name='admin'),
            path('company_view',company_view,name='company_view')
]