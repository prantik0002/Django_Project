from django.urls import path#check
from testsystem.views import *
urlpatterns=[
    path('',greeting),
    path('login/',userLogin),
    path('logout/',userLogout),
    path('test/',test),  
    path('questions/',question),
    path('result/',result),
    path('again_test/',again_test),
    path('signup/',signup),
    path('savedata/',savedata),
    path('contact/',showContact),
    path('about/',about),

]