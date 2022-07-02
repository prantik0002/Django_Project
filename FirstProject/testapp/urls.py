from django.urls import path
from testapp.views import *
urlpatterns=[
    path('new-employee/',newEmployee),
    path('save-employee/',saveEmployee),
    path('contact/',showContact),
    path('about/',about),
    path('',greeting),
    path('show-employee/',employee_info),  
    path('login/',userLogin),
    path('logout/',userLogout),
]