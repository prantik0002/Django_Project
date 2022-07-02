from django.urls import path
from exam.views import *
urlpatterns=[
    path('test-paper/',testPaper),
    path('result/',result),
]